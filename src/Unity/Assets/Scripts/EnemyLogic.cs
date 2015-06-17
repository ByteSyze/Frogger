using UnityEngine;
using System.Collections;

public class EnemyLogic : MonoBehaviour {
	
	GameObject enemy;
	Rigidbody enemyRigidBody;

	GameObject player;
	
	// Use this for initialization
	void Start () {
		enemy = GameObject.FindWithTag ("Enemy");
		enemyRigidBody = GetComponent <Rigidbody> ();

		player = GameObject.FindWithTag ("Player");
	}
	
	// Update is called once per frame
	void Update () {
		enemy.transform.LookAt (player.transform);
		enemyRigidBody.transform.position += enemy.transform.forward * .05f;
	}
}
