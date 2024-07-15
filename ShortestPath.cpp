#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <tuple>

using namespace std;

class Solution {
public:
    vector<int> shortestPath(int n, int m, vector<vector<int>>& edges) {
        vector<vector<pair<int, int>>> graph(n + 1);
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }

        vector<int> dist(n + 1, INT_MAX);
        vector<int> prev(n + 1, -1);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        dist[1] = 0;
        pq.push({0, 1});

        while (!pq.empty()) {
            auto current = pq.top();
            int current_dist = current.first;
            int u = current.second;
            pq.pop();

            if (current_dist > dist[u]) continue;

            for (auto& neighbor : graph[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    prev[v] = u;
                    pq.push({dist[v], v});
                }
            }
        }

        if (dist[n] == INT_MAX) {
            return {-1};
        }

        vector<int> path;
        for (int at = n; at != -1; at = prev[at]) {
            path.push_back(at);
        }
        reverse(path.begin(), path.end());

        path.insert(path.begin(), dist[n]);
        return path;
    }
};

// Driver code to test the solution
int main() {
    Solution sol;
    int n = 5;
    int m = 6;
    vector<vector<int>> edges = {
        {1, 2, 2},
        {2, 5, 5},
        {2, 3, 4},
        {1, 4, 1},
        {4, 3, 3},
        {3, 5, 1}
    };

    vector<int> result = sol.shortestPath(n, m, edges);
    if (result[0] == -1) {
        cout << -1 << endl;
    } else {
        for (int i = 0; i < result.size(); i++) {
            if (i == 0) {
                cout << result[i];
            } else {
                cout << " " << result[i];
            }
        }
        cout << endl;
    }

    return 0;
}

