
//------------------------------------------------------------------------------
// <auto-generated>
// This code was generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
//
// Changes to this file may cause incorrect behavior and will be lost when
// the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------
#nullable enable
namespace Shippo.Models.Components
{
    using Newtonsoft.Json;
    using Shippo.Models.Components;
    using Shippo.Utils;
    
    public class ExampleComplex
    {

        [JsonProperty("responseType")]
        public ExampleComplexResponseType? ResponseType { get; set; }

        [JsonProperty("complex")]
        public string? Complex { get; set; }
    }
}