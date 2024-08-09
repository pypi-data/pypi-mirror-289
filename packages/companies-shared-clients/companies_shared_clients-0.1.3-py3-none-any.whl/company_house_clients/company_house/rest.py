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

    async def get_list_of_all_persons_with_significant_control(self, company_number: str):
        return await self.make_api_request(
            method="GET",
            path=f"company/{company_number}/persons-with-significant-control"
        )

    async def get_corporate_entity_beneficial_owner(self, company_number: str, psc_id: str):
        return await self.make_api_request(
            method="GET",
            path=f"company/{company_number}/persons-with-significant-control/corporate-entity-beneficial-owner/{psc_id}"
        )

    async def get_corporate_officers_disqualifications(self, officer_id):
        return await self.make_api_request(
            method="GET",
            path=f"disqualified-officers/corporate/{officer_id}"
        )

    async def get_natural_officers_disqualifications(self, officer_id):
        return await self.make_api_request(
            method="GET",
            path=f"disqualified-officers/natural/{officer_id}"
        )


if __name__ == '__main__':
    import asyncio

    client = CompanyHouseRest(api_key="febf1ec9-add6-48bb-a534-d42de294dd07")


    async def main():
        officers = await client.get_list_of_all_persons_with_significant_control(
            company_number="13543786",
        )
        print(officers)


    asyncio.run(main())
