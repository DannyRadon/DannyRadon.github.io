using UnityEngine;
using TMPro;

public class StarUIManager : MonoBehaviour
{
    public static StarUIManager Instance;

    public GameObject infoWindow;
    public TextMeshProUGUI nameText;
    public TextMeshProUGUI dataText;

   
    void Awake() { Instance = this; }
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    public void ShowStarInfo(string name, string data)
    {
        infoWindow.SetActive(true);
        nameText.text = name;
        dataText.text = data;
    }

    public void CloseStarWindow() { 
        infoWindow.SetActive(false);
    }
}
