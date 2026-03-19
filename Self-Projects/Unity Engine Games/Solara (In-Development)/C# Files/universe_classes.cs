using Newtonsoft.Json;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class GameUniverse   // Class Object -- Game Universe (Collection of Stars)
{
    [JsonProperty("Star")]
    public Dictionary<string, Star> Star;
}

[System.Serializable]       // Class Object -- Star Object
public class Star
{
    public string id;
    public string name;
    public string type;
    public float mass;
    public Vector3 star_pos;
    public bool sprite_active;
    public bool mesh_active;

    public Dictionary<string, Planet> Planets;

    [Newtonsoft.Json.JsonIgnore]
    public GameObject spawnedInstance;
}

[System.Serializable]
public class Planet         // Class Object -- Planet Object
{
    public string id;
    public string name;
    public string type;
    public float mass;
    public float grav;
    public string host_star;

}