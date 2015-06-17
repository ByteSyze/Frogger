using UnityEngine;
using System.Collections;

public class EnemyLogic : MonoBehaviour {
	
	GameObject enemy;
	GameObject player;
	
	// Use this for initialization
	void Start () {
		enemy = GameObject.FindWithTag ("Enemy");
		player = GameObject.FindWithTag ("Player");
	}
	
	// Update is called once per frame
	void Update () {
		enemy.transform.LookAt (player.transform);
		enemy.transform.position += enemy.transform.forward * .05f;
	}
}
