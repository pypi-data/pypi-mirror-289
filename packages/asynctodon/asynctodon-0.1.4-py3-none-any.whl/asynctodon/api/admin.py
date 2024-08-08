from collections.abc import AsyncIterable

from .base import ClientBase, object_to_id, parse_data

from ..enums import BlockSeverity
from ..objects import AdminDomainBlock, ListDeserializer


class AdminBase(ClientBase):
	async def admin_block_domain(self,
						domain: str,
						severity: BlockSeverity | str = BlockSeverity.SILENCE,
						reject_media: bool = False,
						reject_reports: bool = False,
						private_comment: str | None = None,
						public_comment: str | None = None,
						obfuscate: bool = False) -> AdminDomainBlock:

		data = parse_data(
			domain = domain,
			severity = BlockSeverity.parse(severity),
			reject_media = reject_media,
			reject_reports = reject_reports,
			private_comment = private_comment,
			public_comment = public_comment,
			obfuscate = obfuscate
		)

		return await self.send("POST", "/api/v1/admin/domain_blocks", AdminDomainBlock, data)


	async def admin_domain_block(self, block_id: int | str) -> AdminDomainBlock:
		return await self.send(
			"GET", f"/api/v1/admin/domain_blocks/{block_id}", AdminDomainBlock
		)


	async def admin_domain_blocks(self,
						min_id: int | None = None,
						max_id: int | None = None,
						since_id: int | None = None,
						limit: int = 100) -> list[AdminDomainBlock]:

		assert 0 <= limit <= 200, "Limit range must be 0 - 200"

		query = parse_data(
			limit = limit,
			min_id = min_id,
			max_id = max_id,
			since_id = since_id
		)

		return await self.send(
			"GET", "/api/v1/admin/domain_blocks", ListDeserializer(AdminDomainBlock), query = query
		)


	async def admin_update_domain(self,
						block: AdminDomainBlock | int | str,
						severity: BlockSeverity | str | None = None,
						reject_media: bool | None = None,
						reject_reports: bool | None = None,
						private_comment: str | None = None,
						public_comment: str | None = None,
						obfuscate: bool | None = None) -> AdminDomainBlock:

		block_id = object_to_id(block)
		data = parse_data(
			severity = BlockSeverity.parse(severity) if severity else None,
			reject_media = reject_media,
			reject_reports = reject_reports,
			private_comment = private_comment,
			public_comment = public_comment,
			obfuscate = obfuscate
		)

		return await self.send(
			"PUT", f"/api/v1/admin/domain_blocks/{block_id}", AdminDomainBlock, data
		)


	async def admin_unblock_domain(self, block: AdminDomainBlock | int | str) -> None:
		await self.send("DELETE", f"/api/v1/admin/domain_blocks/{object_to_id(block)}", None)


	# todo: create function based on this to work on any paginated endpoint
	async def all_admin_domain_blocks(self, chunk_size: int = 100) -> AsyncIterable[AdminDomainBlock]:
		max_id: int = 0

		while True:
			new_items = await self.admin_domain_blocks(max_id = max_id or None, limit = chunk_size)

			if not len(new_items):
				break

			max_id = int(new_items[-1].id)

			for item in new_items:
				yield item

			if len(new_items) < chunk_size:
				break
