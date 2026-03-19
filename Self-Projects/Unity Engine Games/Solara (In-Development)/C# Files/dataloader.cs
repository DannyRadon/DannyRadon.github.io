// ---------------------------------------------------------------------------------------------------------
// This is the Data Loader Script File Used with the Unity Engine to Load-In the Python-Generated Universe
// data which had been exported to JSON. This takes in the JSON, the Star-System Data and Loads It into 
// engine.
// ----------------------------------------------------------------------------------------------------------


// Import Pool
using System.IO;
using UnityEngine;
using Newtonsoft.Json;
using System.Collections.Generic;
public class UniverseLoader : MonoBehaviour

{
    // Class Object Attributes

    public GameObject starPrefab;
    public GameObject starSpritePrefab;

    public GameObject MapStarIcon;

    public GameObject planetPrefab;

    public GameUniverse universe_data;

    // Calling in the Projection Controller
    public Star_Projection star_projection;

    // Player Location Initialization

    public Star p_curr_sys = null;
    public Star last_system_id;
    
    // This is here to use initialize as a check/compare for same-positioned stars...
    Vector3 star_pos_last = new Vector3 (0, 0, 0);

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        // Loading in the Python-Generated JSON Universe Data File and Reading it into Engine...
        string file_path = Path.Combine(Application.streamingAssetsPath, "universe_data.json");
        string json_file = File.ReadAllText(file_path);

        universe_data = JsonConvert.DeserializeObject<GameUniverse>(json_file);

        // Initializing Playeer Start Position and Previous Star Position Tracker
        Star p_curr_sys = universe_data.Star["Was"];
        last_system_id = p_curr_sys;
        
        // Looping Through Star Data taken from JSON -- Making the Stars
        foreach (var StarPair in universe_data.Star)
        {

            Star star = StarPair.Value;
            star.id = StarPair.Key;



            // Generating Randomized Star Positions Here for Testing

            star.star_pos = new Vector3(
                Random.Range(-100f, 100f),
                Random.Range(-100f, 100f),
                Random.Range(-100f, 100f)
            );

            Debug.Log("star_pos = " + star.star_pos);
            Debug.Log("star_pos_last = " + star_pos_last);

            // If-Condition to Catch Identical Vector Positions of Stars
            if (star_pos_last == star.star_pos) {

                Debug.Log("IDENTICAL STAR POSITIONS FOUND...");

                star.star_pos = new Vector3(

                    Random.Range(-100f, 100f),
                    Random.Range(-100f, 100f),
                    Random.Range(-100f, 100f)

                );

                Debug.Log("New star_pos = " + star.star_pos);

            };

            // Catching the Last Updated Star Position to use as Comparison for the Newer Generated Vector Star Position
            star_pos_last = star.star_pos;

            Debug.Log("STAR NAME: " + star.id);
            Debug.Log($"STAR POSITION: {star.star_pos}");
            
            // Spawning Sprites & Mesh for Stars...
            if (star.id == p_curr_sys.id) {

                star.spawnedInstance = Instantiate(starPrefab, star.star_pos, Quaternion.identity);
                star.spawnedInstance.name = star.id;

                Vector3 flatMapPos = new Vector3(star.star_pos.x, 200f, star.star_pos.z);

                GameObject icon = Instantiate(MapStarIcon, flatMapPos, MapStarIcon.transform.rotation);
                icon.name = star.id;


                
            }

            else
            {
                star.spawnedInstance = Instantiate(starSpritePrefab, star.star_pos, Quaternion.identity);
                star.spawnedInstance.name = star.id;

                Vector3 flatMapPos = new Vector3(star.star_pos.x, 200f, star.star_pos.z);

                GameObject icon = Instantiate(MapStarIcon, flatMapPos, MapStarIcon.transform.rotation);
                icon.name = star.id;

                MapStarIcon iconScript = icon.GetComponent<MapStarIcon>();

                iconScript.star_name = star.id;
                
            }
        }
    }

    
    // Update is called once per frame
    void Update()
    {

    }

    public void SetCurrentSystem(string star_id)
    {
        if (universe_data.Star.ContainsKey(star_id))
        {
            Destroy(last_system_id.spawnedInstance);
            last_system_id.spawnedInstance = Instantiate(starSpritePrefab, last_system_id.star_pos, Quaternion.identity);
            last_system_id.spawnedInstance.name = last_system_id.id;

            p_curr_sys = universe_data.Star[star_id];

            Destroy(p_curr_sys.spawnedInstance);
            p_curr_sys.spawnedInstance = Instantiate(starPrefab, p_curr_sys.star_pos, Quaternion.identity);
            p_curr_sys.spawnedInstance.name = p_curr_sys.id;

            last_system_id = p_curr_sys;

            

            Debug.Log("Star System Changed to: " + p_curr_sys.id);
        }

        else
        {
            Debug.LogError("Star Not Found: " + star_id);
        }
    }
}