# Neon Arcade Portal

A professional browser-based arcade containing **50 standalone offline games** built with vanilla HTML, CSS, and JavaScript. Each game is a self-contained `.html` file with inline CSS/JS, a `‹ Menu` link back to `index.html`, game-specific rules and rendering, responsive controls, Web Audio API effects, particle feedback, pause/restart flow, session-only statistics, and cyber-arcade styling.

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
| 1 | Snake | `snake.html` | Core Arcade | Medium | Arrows/WASD steer; Space pause; R restart. | Guide the neon snake through a grid, eating food and avoiding your tail. |
| 2 | Pong | `pong.html` | Core Arcade | Easy | Mouse/touch or arrows/W/S; Space pause; R restart. | Deflect the puck past the rival paddle before the AI scores. |
| 3 | Breakout | `breakout.html` | Core Arcade | Easy | Mouse/touch or arrows; Space launch/pause; R restart. | Launch the ball, clear every brick, and keep your lives alive. |
| 4 | Tetris | `tetris.html` | Core Arcade | Hard | Arrows move/rotate; Space hard drop; R restart. | Drop tetromino cores and clear full neon rows. |
| 5 | 2048 | `2048.html` | Core Arcade | Medium | Arrows or swipe; R restart. | Slide matching numbers together to build the 2048 core. |
| 6 | Flappy | `flappy.html` | Core Arcade | Medium | Click/tap/Space/Up flap; R restart. | Tap to flap through reactor gates without touching them. |
| 7 | Tic Tac Toe | `tictactoe.html` | Core Arcade | Easy | Click/tap a cell; R restart. | Place three X glyphs in a row before the CPU O glyphs. |
| 8 | Minesweeper | `minesweeper.html` | Core Arcade | Medium | Click reveal; right-click/long-press flag; R restart. | Reveal all safe nodes and avoid hidden mines. |
| 9 | Memory | `memory.html` | Core Arcade | Easy | Click/tap cards; R restart. | Flip cards and match every pair with the fewest moves. |
| 10 | Space Invaders | `spaceinvaders.html` | Classic Arcade | Medium | Arrows move; Space fire; P pause. | Blast descending alien rows before they reach your cannon. |
| 11 | Asteroids | `asteroids.html` | Classic Arcade | Hard | Arrows thrust/turn; Space fire. | Rotate, thrust, and split drifting asteroids. |
| 12 | Pac-Man | `pacman.html` | Classic Arcade | Medium | Arrows/WASD move. | Collect pellets inside the maze while dodging ghosts. |
| 13 | Frogger | `frogger.html` | Classic Arcade | Medium | Arrows/WASD hop. | Hop lane by lane through traffic to the safe bank. |
| 14 | Galaga | `galaga.html` | Classic Arcade | Medium | Arrows move; Space fire. | Shoot swooping alien formations for combo chains. |
| 15 | Missile Command | `missilecommand.html` | Classic Arcade | Hard | Click/tap targets; Space pause. | Click interception points to protect your cities. |
| 16 | Centipede | `centipede.html` | Classic Arcade | Medium | Move mouse/arrows; Space fire. | Blast the segmented centipede through mushroom fields. |
| 17 | Lunar Lander | `lunarlander.html` | Classic Arcade | Hard | Arrows/Space thrust. | Balance thrust and gravity to land gently on the pad. |
| 18 | Dig Dug | `digdug.html` | Classic Arcade | Medium | Arrows dig; Space pulse. | Tunnel through dirt, collect gems, and avoid underground foes. |
| 19 | Connect 4 | `connect4.html` | Puzzle | Easy | Click/tap a column. | Drop discs and connect four before the CPU blocks you. |
| 20 | Sudoku | `sudoku.html` | Puzzle | Hard | Click cell, press 1-9. | Fill missing cells without repeating numbers in rows or columns. |
| 21 | Hangman | `hangman.html` | Puzzle | Easy | Keyboard or on-screen letters. | Guess the hidden arcade word before the neon avatar is complete. |
| 22 | Wordle | `wordle.html` | Puzzle | Medium | Keyboard input; Enter submit. | Discover the secret five-letter word in six guesses. |
| 23 | Nonogram | `nonogram.html` | Puzzle | Hard | Click paint; right-click mark. | Paint cells that match the row and column clues. |
| 24 | Lights Out | `lightsout.html` | Puzzle | Medium | Click/tap lights. | Toggle crosses until every light is dark. |
| 25 | Sokoban | `sokoban.html` | Puzzle | Hard | Arrows/WASD move. | Push crates onto glowing target docks. |
| 26 | Pipe Connect | `pipeconnect.html` | Puzzle | Medium | Click/tap pipes. | Rotate pipe tiles to connect inlet to outlet. |
| 27 | SameGame | `samegame.html` | Puzzle | Easy | Click matching groups. | Pop connected color clusters to clear the board. |
| 28 | Solitaire | `solitaire.html` | Card & Board | Medium | Click/drag cards; double-click auto. | Move cards into ordered foundation stacks. |
| 29 | Chess | `chess.html` | Card & Board | Hard | Click piece then destination. | Command pieces on a compact chess board and capture the king. |
| 30 | Checkers | `checkers.html` | Card & Board | Medium | Click piece then square. | Jump rival pieces and crown your kings. |
| 31 | Reversi | `reversi.html` | Card & Board | Medium | Click legal square. | Place discs to flip rows and own the board. |
| 32 | Battleship | `battleship.html` | Card & Board | Medium | Click grid to fire. | Fire at grid sectors to find and sink the fleet. |
| 33 | Mastermind | `mastermind.html` | Card & Board | Medium | Click colors then submit. | Deduce the hidden color code from feedback pegs. |
| 34 | Mancala | `mancala.html` | Card & Board | Medium | Click your pits. | Sow stones around the board and outscore the CPU. |
| 35 | Doodle Jump | `doodlejump.html` | Endless & Platform | Medium | Arrows/drag steer. | Bounce upward from platform to platform. |
| 36 | Endless Runner | `endlessrunner.html` | Endless & Platform | Medium | Space/Up jump; Down slide. | Jump and slide past a stream of hazards. |
| 37 | Color Switch | `colorswitch.html` | Endless & Platform | Hard | Tap/Space to rise. | Pass through rotating gates only on your matching color. |
| 38 | Jetpack | `jetpack.html` | Endless & Platform | Medium | Hold Space/touch to boost. | Feather your jetpack through laser corridors. |
| 39 | Helicopter | `helicopter.html` | Endless & Platform | Medium | Hold mouse/Space to climb. | Pilot through a scrolling cave without clipping walls. |
| 40 | Platformer | `platformer.html` | Endless & Platform | Medium | Arrows/WASD; Space jump. | Collect keys and jump to the exit portal. |
| 41 | Tower Defense | `towerdefense.html` | Action & Sports | Hard | Click build nodes; Space wave. | Place turrets to stop creeps from reaching the core. |
| 42 | Pinball | `pinball.html` | Action & Sports | Medium | A/D or arrows flippers. | Keep the ball alive with flippers and hit bumpers. |
| 43 | Air Hockey | `airhockey.html` | Action & Sports | Easy | Mouse/touch move. | Control your mallet and score goals on the AI. |
| 44 | Breakout Plus | `breakoutplus.html` | Action & Sports | Medium | Mouse/touch/arrows. | Clear armored bricks and catch falling powerups. |
| 45 | Bubble Shooter | `bubbleshooter.html` | Action & Sports | Easy | Aim mouse/touch, click fire. | Aim bubbles to match three and clear the ceiling. |
| 46 | Brick Crusher | `brickcrusher.html` | Action & Sports | Medium | Mouse/touch/arrows. | Smash heavy brick waves with multi-ball chaos. |
| 47 | Simon | `simon.html` | Casual & Skill | Easy | Click/tap pads. | Repeat the growing sequence of glowing pads. |
| 48 | Whack-a-Mole | `whackamole.html` | Casual & Skill | Easy | Click/tap targets. | Hit moles before they vanish from the grid. |
| 49 | Typing Challenge | `typingchallenge.html` | Casual & Skill | Medium | Keyboard typing. | Type falling words before they hit the bottom. |
| 50 | Mini Golf | `minigolf.html` | Casual & Skill | Medium | Drag/release to shoot. | Drag, aim, and putt around obstacles into the cup. |

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
