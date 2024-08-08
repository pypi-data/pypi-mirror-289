from clients.base_client import APIConsumer


class CompanyHouseStreaming(APIConsumer):
    def __init__(self, api_key: str):
        super().__init__(api_key=api_key)

    async def get_company_profile(self):
        return await self.make_stream_request(
            method="GET",
            path=f"companies"
        )


if __name__ == '__main__':
    import asyncio

    client = CompanyHouseStreaming(api_key="d17791c3-a0c2-4df4-87b5-35dc06ea5f17")


    async def main():
        officers = await client.get_company_profile()
        print(officers)


    asyncio.run(main())
