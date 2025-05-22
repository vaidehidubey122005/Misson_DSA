#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

struct Edge {
    int to, weight;
};

void dijkstra(int start, int n, vector<vector<Edge>>& adj, vector<int>& dist) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});
    dist[start] = 0;

    while (!pq.empty()) {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();

        if (d > dist[u]) continue;

        for (const Edge& e : adj[u]) {
            int v = e.to;
            int weight = e.weight;

            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<Edge>> adj(n + 1);
    vector<int> dist(n + 1, INT_MAX);

    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    dijkstra(1, n, adj, dist);

    for (int i = 1; i <= n; i++) {
        if (dist[i] == INT_MAX) {
            cout << -1 << " ";
        } else {
            cout << dist[i] << " ";
        }
    }

    return 0;
}
