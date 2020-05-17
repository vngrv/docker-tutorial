package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Article struct {
	Id      int    `json:"Id"`
	Message string `json:"Message"`
}

type Articles []Article

func allArticles(w http.ResponseWriter, r *http.Request) {
	articles := Articles{
		Article{
			Id:      1,
			Message: "Hello world",
		},
		Article{
			Id:      2,
			Message: "Nice to meet you",
		},
	}

	enableCors(&w)
	fmt.Println("Endpoint Hit: Api")
	json.NewEncoder(w).Encode(articles)
}

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: Homepage")
	fmt.Fprint(w, "Endpoint Hit: Homepage")
}

func handleRequests() {
	http.HandleFunc("/", homePage)
	http.HandleFunc("/api/v1", allArticles)
	log.Fatal(http.ListenAndServe(":8081", nil))
}

func enableCors(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
}

func main() {
	handleRequests()
}
