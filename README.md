# Neon Arcade Portal

A professional browser-based arcade containing **50 standalone offline games** built with vanilla HTML, CSS, and JavaScript. Each game is a self-contained `.html` file with inline CSS/JS, a `‹ Menu` link back to `index.html`, responsive controls, Web Audio API effects, particle feedback, pause/restart flow, session-only statistics, and cyber-arcade styling.

## Folder structure

```text
.
├── index.html              # Premium searchable launcher
├── snake.html ...          # 50 standalone game files
├── README.md               # Project documentation
└── src/                    # Original summarization coursework files
```

## Installation

No installation is required. Download or keep the files in one folder and open **`index.html`** in a modern browser. Games work offline when opened directly from disk.

## Complete game catalog, controls, and objectives

| # | Game | File | Genre | Difficulty | Controls | Objective |
|---:|---|---|---|---|---|---|
| 1 | Snake | `snake.html` | Core Arcade | Medium | Arrows/WASD steer; Space pause/start; R restart. | Guide a neon trail to collect food while avoiding crashes. |
| 2 | Pong | `pong.html` | Core Arcade | Easy | Mouse/touch or arrows/W/S; Space pause; R restart. | Deflect the puck past the rival paddle. |
| 3 | Breakout | `breakout.html` | Core Arcade | Easy | Mouse/touch or arrows; Space launch/pause; R restart. | Break every shield brick with your energy ball. |
| 4 | Tetris | `tetris.html` | Core Arcade | Hard | Arrows move/rotate; Space drop/pause; R restart. | Stack falling blocks and clear horizontal rows. |
| 5 | 2048 | `2048.html` | Core Arcade | Medium | Arrows or swipe; Space pause; R restart. | Merge numbered power cores toward 2048. |
| 6 | Flappy | `flappy.html` | Core Arcade | Medium | Click/tap/Space/Up flap; P pause; R restart. | Flap through reactor gates without touching them. |
| 7 | Tic Tac Toe | `tictactoe.html` | Core Arcade | Easy | Click/tap a cell; R restart. | Place three glyphs in a row before the CPU. |
| 8 | Minesweeper | `minesweeper.html` | Core Arcade | Medium | Click reveal; right-click/long-press flag; R restart. | Reveal safe nodes while flagging hidden mines. |
| 9 | Memory | `memory.html` | Core Arcade | Easy | Click/tap cards; R restart. | Match all hidden cyber cards. |
| 10 | Space Invaders | `spaceinvaders.html` | Classic Arcade | Medium | Arrows move; Space fire; P pause. | Blast descending alien formations. |
| 11 | Asteroids | `asteroids.html` | Classic Arcade | Hard | Arrows thrust/turn; Space fire. | Split and dodge drifting asteroids. |
| 12 | Pac-Man | `pacman.html` | Classic Arcade | Medium | Arrows/WASD move. | Collect pellets while evading ghosts. |
| 13 | Frogger | `frogger.html` | Classic Arcade | Medium | Arrows/WASD hop. | Hop through traffic to safe zones. |
| 14 | Galaga | `galaga.html` | Classic Arcade | Medium | Arrows move; Space fire. | Shoot swooping alien waves. |
| 15 | Missile Command | `missilecommand.html` | Classic Arcade | Hard | Click/tap targets; Space pause. | Intercept falling missiles before impact. |
| 16 | Centipede | `centipede.html` | Classic Arcade | Medium | Move mouse/arrows; Space fire. | Clear mushroom fields and the centipede. |
| 17 | Lunar Lander | `lunarlander.html` | Classic Arcade | Hard | Arrows/Space thrust. | Land gently on a glowing pad. |
| 18 | Dig Dug | `digdug.html` | Classic Arcade | Medium | Arrows dig; Space pulse. | Tunnel underground and collect gems. |
| 19 | Connect 4 | `connect4.html` | Puzzle | Easy | Click/tap column. | Drop four discs in a row. |
| 20 | Sudoku | `sudoku.html` | Puzzle | Hard | Click cell, press 1-9. | Complete the number grid. |
| 21 | Hangman | `hangman.html` | Puzzle | Easy | Keyboard or on-screen letters. | Guess the hidden arcade word. |
| 22 | Wordle | `wordle.html` | Puzzle | Medium | Keyboard input; Enter submit. | Find the five-letter secret in six tries. |
| 23 | Nonogram | `nonogram.html` | Puzzle | Hard | Click paint; right-click mark. | Paint cells matching row and column clues. |
| 24 | Lights Out | `lightsout.html` | Puzzle | Medium | Click toggles cross. | Turn off every neon light. |
| 25 | Sokoban | `sokoban.html` | Puzzle | Hard | Arrows/WASD move. | Push crates onto glowing docks. |
| 26 | Pipe Connect | `pipeconnect.html` | Puzzle | Medium | Click/tap pipes. | Rotate pipes to link inlet to outlet. |
| 27 | SameGame | `samegame.html` | Puzzle | Easy | Click matching groups. | Pop large color clusters. |
| 28 | Solitaire | `solitaire.html` | Card & Board | Medium | Click/drag cards; double-click auto. | Stack cards into foundations. |
| 29 | Chess | `chess.html` | Card & Board | Hard | Click piece then destination. | Capture the rival king in mini chess. |
| 30 | Checkers | `checkers.html` | Card & Board | Medium | Click piece then square. | Jump rival pieces and crown kings. |
| 31 | Reversi | `reversi.html` | Card & Board | Medium | Click legal square. | Flip discs to own the board. |
| 32 | Battleship | `battleship.html` | Card & Board | Medium | Click grid to fire. | Find and sink the hidden fleet. |
| 33 | Mastermind | `mastermind.html` | Card & Board | Medium | Click colors then submit. | Deduce the secret color code. |
| 34 | Mancala | `mancala.html` | Card & Board | Medium | Click your pits. | Sow stones to outscore the CPU. |
| 35 | Doodle Jump | `doodlejump.html` | Endless & Platform | Medium | Tilt with arrows or drag. | Bounce upward through platforms. |
| 36 | Endless Runner | `endlessrunner.html` | Endless & Platform | Medium | Space/Up jump; Down slide. | Jump and slide through hazards. |
| 37 | Color Switch | `colorswitch.html` | Endless & Platform | Hard | Tap/Space to rise. | Pass only through matching color gates. |
| 38 | Jetpack | `jetpack.html` | Endless & Platform | Medium | Hold Space/touch to boost. | Feather the jetpack through lasers. |
| 39 | Helicopter | `helicopter.html` | Endless & Platform | Medium | Hold mouse/Space to climb. | Pilot through a scrolling cave. |
| 40 | Platformer | `platformer.html` | Endless & Platform | Medium | Arrows/WASD; Space jump. | Run, jump, collect keys, reach portal. |
| 41 | Tower Defense | `towerdefense.html` | Action & Sports | Hard | Click build nodes; Space wave. | Place turrets to stop creeps. |
| 42 | Pinball | `pinball.html` | Action & Sports | Medium | A/D or arrows flippers. | Keep the ball alive and hit bumpers. |
| 43 | Air Hockey | `airhockey.html` | Action & Sports | Easy | Mouse/touch move. | Score goals with a neon mallet. |
| 44 | Breakout Plus | `breakoutplus.html` | Action & Sports | Medium | Mouse/touch/arrows. | Break armored bricks and catch powerups. |
| 45 | Bubble Shooter | `bubbleshooter.html` | Action & Sports | Easy | Aim mouse/touch, click fire. | Match three bubbles to clear the ceiling. |
| 46 | Brick Crusher | `brickcrusher.html` | Action & Sports | Medium | Mouse/touch/arrows. | Smash bricks with multi-ball chaos. |
| 47 | Simon | `simon.html` | Casual & Skill | Easy | Click/tap pads. | Repeat the growing light sequence. |
| 48 | Whack-a-Mole | `whackamole.html` | Casual & Skill | Easy | Click/tap targets. | Hit moles before they vanish. |
| 49 | Typing Challenge | `typingchallenge.html` | Casual & Skill | Medium | Keyboard typing. | Type falling words before impact. |
| 50 | Mini Golf | `minigolf.html` | Casual & Skill | Medium | Drag/release to shoot. | Putt around obstacles into the cup. |

## Supported platforms

- Desktop browsers with keyboard, mouse, or trackpad.
- Mobile and tablet browsers with touch or pointer input.
- Offline local-file usage; no server or internet connection is required.

## Browser compatibility

Tested design targets current Chromium, Firefox, Safari, and Edge releases. The games use standard Canvas 2D, CSS media queries, pointer events, `requestAnimationFrame`, session storage for launcher recency, and the Web Audio API.

## Accessibility features

- Keyboard shortcuts and visible `‹ Menu` navigation.
- Responsive layouts for narrow screens.
- High-contrast toggle inside each game.
- `prefers-reduced-motion` CSS support to suppress decorative animation.
- Text instructions, HUD labels, pause/restart controls, and session-only feedback.

## Performance notes

- Each game uses a single canvas and an FPS-independent `requestAnimationFrame` loop.
- Assets are procedurally drawn; no external images, fonts, CDNs, packages, or build tools are needed.
- Session statistics stay in memory for each game; the launcher's recently played sort uses `sessionStorage` only for the current browser session.

## Credits

Created as a vanilla web arcade assignment expansion. All visuals, animation, controls, and sound effects are implemented directly in the standalone HTML files.
