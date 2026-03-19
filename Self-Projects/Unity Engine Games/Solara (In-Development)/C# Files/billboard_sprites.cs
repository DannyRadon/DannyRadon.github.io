using UnityEngine;

public class BillboardSprites : MonoBehaviour
{
    
    // Forward Facing Sprites
    void LateUpdate()
    {
        if (Camera.main != null)
        {
            transform.forward = Camera.main.transform.forward;

        }
        
    }
}