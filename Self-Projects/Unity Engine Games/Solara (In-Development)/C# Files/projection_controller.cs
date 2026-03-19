using UnityEngine;

public class Star_Projection : MonoBehaviour
{
    // Creating the Sprite & 3D Objects for Projection Swapping Later...
    public GameObject SpriteVisual;
    public GameObject MeshVisual;

    public Star prev_update_star = null;

    // Initializing Player's Current Star System Location...

    public UniverseLoader universe_loader;

    // Setting Up 'Player' container for transforming after update...
    private Transform player;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        // Instantiating the Player at Camera Position
        //player = Camera.main.transform;
        
    }

    // Update is called once per frame
    void Update()
    {
        if (player == null) return;

        if (prev_update_star == null)
        {
            prev_update_star = universe_loader.p_curr_sys;
        }

        if (prev_update_star == universe_loader.p_curr_sys)
        {
            ShowMesh();
        }

        else
        {
            ShowSprite();
        }

        
    }

    public void ShowSprite()
    {
        SpriteVisual.SetActive(true);
        MeshVisual.SetActive(false);
    }

    public void ShowMesh()
    {
        SpriteVisual.SetActive(false);
        MeshVisual.SetActive(true);
    }


}