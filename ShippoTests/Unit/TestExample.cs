using WireMock.RequestBuilders;
using WireMock.ResponseBuilders;
using WireMock.Server;

namespace ShippoTests.Unit;

[Collection("Unit")]
public class TestExample
{
    private readonly WireMockServer _server;

    public TestExample()
    {
        _server = WireMockServer.Start();
    }
    
    [Fact]
    public async void TestExampleFieldSimple()
    {
        var sdk = new ShippoSDK(
            serverUrl: "http://localhost:" + _server.Port
        );
        
        _server.Given(Request.Create().WithPath("/example").UsingGet())
            .RespondWith(Response.Create()
                .WithHeader("Content-Type", "application/json")
                .WithBody("{\"field\": \"value\"}"));

        var result = await sdk.GetExampleAsync();
        result.Field.Should().Be("value");
    }
}