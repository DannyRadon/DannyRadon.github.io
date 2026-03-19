// ------------------------------------------------------------------------------------
// Name: billboard_sprites
// Date: 
// 
// Description:
//
// -------------------------------------------------------------------------------------

// Referencing the Unity Engine
using UnityEngine;

// Creating a UnityEngine Class - MonoBehavior (Single Script Action)
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