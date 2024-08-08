from company_house_clients.base_client import APIConsumer


class CompanyHouseRest(APIConsumer):
    def __init__(self, api_key: str):
        super().__init__(api_key=api_key)

    async def get_company_profile(self, company_number: str):
        return await self.make_api_request(
            method="GET",
            path=f"company/{company_number}"
        )

    async def get_officers_list(self, company_number: str):
        return await self.make_api_request(
            method="GET",
            path=f"company/{company_number}/officers"
        )

    async def get_officer_appointment(self, company_number: str, appointment_id: str):
        return await self.make_api_request(
            method="GET",
            path=f"company/{company_number}/appointments/{appointment_id}"
        )

    async def get_company_charges(self, company_number: str):
        return await self.make_api_request(
            method="GET",
            path=f"company/{company_number}/charges"
        )

    async def get_individual_charge(self, company_number: str, charge_id: str):
        return await self.make_api_request(
            method="GET",
            path=f"company/{company_number}/charges/{charge_id}"
        )

    async def get_filing_history_list(self, company_number: str):
        return await self.make_api_request(
            method="GET",
            path=f"company/{company_number}/filing-history"
        )

    async def get_filing_history_item(self, company_number: str, transaction_id: str):
        return await self.make_api_request(
            method="GET",
            path=f"company/{company_number}/filing-history/{transaction_id}"
        )


if __name__ == '__main__':
    import asyncio

    client = CompanyHouseRest(api_key="febf1ec9-add6-48bb-a534-d42de294dd07")


    async def main():
        officers = await client.get_filing_history_item(
            company_number="00420431",
            transaction_id="MzEyNTk1NzQ1M2FkaXF6a2N4"
        )
        print(officers)


    asyncio.run(main())
