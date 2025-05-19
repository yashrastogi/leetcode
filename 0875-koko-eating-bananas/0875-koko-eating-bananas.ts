
function minEatingSpeed(piles: number[], h: number): number {
    let minBph = 1;
    let maxBph = Math.max(...piles);
    let answer = 0;
    while (minBph <= maxBph) {
        const mid = Math.floor(minBph + (maxBph - minBph) / 2);
        const timeTaken = calculateTimeTaken(piles, mid);
        if (timeTaken <= h) {
            answer = mid;
            maxBph = mid - 1;
        } else {
            minBph = mid + 1;
        }
    }
    return answer;
}

function calculateTimeTaken(piles: number[], bph: number): number {
    let time = 0;
    for (const pile of piles) {
        time += Math.floor((pile + bph - 1) / bph);
    }
    return time;
}
