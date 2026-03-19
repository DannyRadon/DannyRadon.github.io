using UnityEngine;

public class StarSelectController : MonoBehaviour
{
    public UniverseLoader u_loader;
    public static StarSelectController instance;

    
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        u_loader = GetComponent<UniverseLoader>();
    }

    // Update is called once per frame
    void Update()
    {

        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            u_loader.SetCurrentSystem("Yaaua");
        }

        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            u_loader.SetCurrentSystem("Pago");
        }
        
    }

    
}
