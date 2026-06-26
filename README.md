# Neon Byte Arcade

A premium browser-based mini-game arcade made with pure vanilla HTML, CSS, and JavaScript. It uses a cohesive cyber-arcade visual system with neon accents, responsive layouts, inline styles/scripts, lightweight generated Web Audio UI feedback, and no frameworks, libraries, CDNs, external images, web fonts, build tools, or storage APIs.

## How to play

Keep **all files in this repository folder together in one flat folder**. Open `index.html` directly in a browser to launch the arcade. Each tile links to a standalone game file, and each game includes a `‹ Menu` link back to `index.html`.

## Games and controls

| Game | File | Controls | Goal |
|---|---|---|---|
| Snake | `snake.html` | Arrow keys or WASD; Space restarts | Eat food, grow, avoid walls and yourself |
| Pong | `pong.html` | W/S, arrow keys, or mouse/touch | Beat the AI; first to 7 wins |
| Breakout | `breakout.html` | Mouse/touch or Left/Right; click/Space launches | Clear all bricks with 3 lives |
| Tetris | `tetris.html` | Left/Right move, Up rotate, Down soft drop, Space hard drop | Clear lines; level rises every 10 lines |
| 2048 | `2048.html` | Arrow keys or touch swipe | Merge tiles to reach 2048, optionally continue |
| Flappy | `flappy.html` | Click/tap, Space, or Up to flap | Pass pipes without hitting obstacles |
| Tic Tac Toe | `tictactoe.html` | Click/tap a cell | Play X against unbeatable O; track wins/losses/ties |
| Minesweeper | `minesweeper.html` | Left-click reveal, right-click flag | Reveal all safe cells on a 9×9 board with 10 mines |
| Memory | `memory.html` | Click/tap cards | Match all 8 pairs with as few moves as possible |


## Design notes

- Every game is a standalone `.html` document with inline CSS and JavaScript.
- The arcade uses system UI fonts only and keeps scores/bests in memory for the current page session.
- Each game includes a polished start menu, floating HUD, large controls, a generated sound toggle, animated overlays, and a `‹ Menu` link back to the launcher.
- Motion effects respect `prefers-reduced-motion`.
