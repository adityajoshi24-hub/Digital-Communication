
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Rectangle

# ============================================================
# Wi-Fi 6 / 6E: OFDMA, Modulation and Coding Visualization
# Educational animation for a PowerPoint presentation
# ============================================================

np.random.seed(7)

# Professional dark theme
BG = "#1C3E7E"
PANEL = "#172438"
WHITE = "#F1F5F9"
MUTED = "#A9B8CC"
COLORS = ["#38BDF8", "#A78BFA", "#34D399", "#FBBF24"]
USER_NAMES = ["User 1", "User 2", "User 3", "User 4"]

fig, axes = plt.subplots(1, 3, figsize=(16, 7))
fig.patch.set_facecolor(BG)

for ax in axes:
    ax.set_facecolor(PANEL)
    ax.tick_params(colors=MUTED, labelsize=8)
    for spine in ax.spines.values():
        spine.set_color("#42516A")

fig.suptitle(
    "WI-FI 6 / 6E | OFDMA, MODULATION & CODING",
    fontsize=19, fontweight="bold", color=WHITE, y=0.97
)

# ------------------------------------------------------------
# PANEL 1: OFDMA RESOURCE ALLOCATION
# ------------------------------------------------------------
ax1 = axes[0]
ax1.set_title(
    "1. OFDMA: Multi-user access",
    color=WHITE, fontsize=12, fontweight="bold", pad=14
)

n_subcarriers = 20
n_symbols = 8
ru_width = 5

ax1.set_xlim(0, n_subcarriers)
ax1.set_ylim(-1.6, n_symbols)
ax1.set_xlabel("Frequency → (illustrative subcarriers)", color=MUTED)
ax1.set_ylabel("OFDM symbols / time →", color=MUTED)
ax1.set_xticks([0, 5, 10, 15, 20])
ax1.set_yticks([0, 2, 4, 6, 7])
ax1.set_yticklabels(["0", "2", "4", "6", "7"])

ru_patches = []

for row in range(n_symbols):
    for col in range(n_subcarriers):
        user = col // ru_width
        rect = Rectangle(
            (col, row), 1, 1,
            facecolor=COLORS[user],
            edgecolor=BG,
            linewidth=0.6,
            alpha=0.68
        )
        ax1.add_patch(rect)
        ru_patches.append((rect, row, user))

legend_handles = [
    Rectangle((0, 0), 1, 1, facecolor=COLORS[i], label=USER_NAMES[i])
    for i in range(4)
]

ax1.legend(
    handles=legend_handles,
    loc="lower left",
    bbox_to_anchor=(0, -0.31),
    ncol=2,
    frameon=False,
    labelcolor=WHITE,
    fontsize=9
)

ru_status = ax1.text(
    0.5, 1.02, "",
    transform=ax1.transAxes,
    ha="center", color=COLORS[0], fontsize=10
)

# ------------------------------------------------------------
# PANEL 2: MODULATION CONSTELLATION
# ------------------------------------------------------------
ax2 = axes[1]
ax2.set_title(
    "2. Modulation: Bits per symbol",
    color=WHITE, fontsize=12, fontweight="bold", pad=14
)

ax2.set_xlim(-1.3, 1.3)
ax2.set_ylim(-1.3, 1.3)
ax2.set_aspect("equal")
ax2.set_xlabel("In-phase (I)", color=MUTED)
ax2.set_ylabel("Quadrature (Q)", color=MUTED)
ax2.axhline(0, color="#53657D", linewidth=0.7)
ax2.axvline(0, color="#53657D", linewidth=0.7)
ax2.grid(True, color="#34445B", linewidth=0.5, alpha=0.7)

mod_orders = [4, 16, 64, 256, 1024]
mod_names = ["QPSK", "16-QAM", "64-QAM", "256-QAM", "1024-QAM"]
bits_per_symbol = [2, 4, 6, 8, 10]

scatter = ax2.scatter(
    [], [], s=13, c="#38BDF8",
    edgecolors="white", linewidths=0.25
)

mod_label = ax2.text(
    0.5, 1.02, "",
    transform=ax2.transAxes,
    ha="center", color="#38BDF8", fontsize=12,
    fontweight="bold"
)

mod_explanation = ax2.text(
    0.5, -0.18, "",
    transform=ax2.transAxes,
    ha="center", color=WHITE, fontsize=9
)

def qam_constellation(order):
    """Generate normalized square-QAM constellation points."""
    side = int(np.sqrt(order))
    levels = np.arange(-(side - 1), side, 2)
    xx, yy = np.meshgrid(levels, levels)
    points = np.column_stack((xx.ravel(), yy.ravel()))
    points = points / np.max(np.abs(points))
    return points

# ------------------------------------------------------------
# PANEL 3: CODING / REDUNDANCY
# ------------------------------------------------------------
ax3 = axes[2]
ax3.set_title(
    "3. Coding: Reliability vs. rate",
    color=WHITE, fontsize=12, fontweight="bold", pad=14
)

ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.set_xticks([])
ax3.set_yticks([])

ax3.text(
    0.5, 9.0, "INFORMATION BITS",
    color=WHITE, fontsize=11, fontweight="bold"
)

info_bits = [1, 0, 1, 1, 0, 1]
bit_patches = []

for i, bit in enumerate(info_bits):
    x = 0.5 + i * 1.45
    rect = Rectangle(
        (x, 7.2), 1.0, 1.0,
        facecolor=COLORS[0] if bit else "#35445B",
        edgecolor=WHITE, linewidth=0.8
    )
    ax3.add_patch(rect)
    ax3.text(
        x + 0.5, 7.7, str(bit),
        color=WHITE, ha="center", va="center",
        fontsize=14, fontweight="bold"
    )
    bit_patches.append(rect)

ax3.annotate(
    "", xy=(5, 5.8), xytext=(5, 6.9),
    arrowprops=dict(arrowstyle="->", color=WHITE, lw=1.8)
)

ax3.text(
    0.5, 5.0, "ENCODING ADDS CHECK / PARITY INFORMATION",
    color=WHITE, fontsize=9, fontweight="bold"
)

coding_boxes = []
for i in range(6):
    x = 0.5 + i * 1.45
    rect = Rectangle(
        (x, 3.1), 1.0, 1.0,
        facecolor="#24374E",
        edgecolor=COLORS[2],
        linewidth=1.2
    )
    ax3.add_patch(rect)
    coding_boxes.append(rect)

coding_text = ax3.text(
    5, 2.55, "",
    ha="center", color=COLORS[2],
    fontsize=12, fontweight="bold"
)

ax3.text(
    5, 1.3,
    "Redundancy can help recover data\n"
    "when transmission errors occur.",
    color=MUTED, ha="center", fontsize=9
)

ax3.text(
    5, 0.25,
    "Conceptual illustration — not a real encoder",
    color="#FBBF24", ha="center", fontsize=8
)

# ------------------------------------------------------------
# ANIMATION
# ------------------------------------------------------------
TOTAL_FRAMES = 100
FRAMES_PER_MOD = 20

def update(frame):
    # OFDMA: highlight the currently scheduled RU group.
    # Multiple users still occupy separate frequency groups.
    active_user = (frame // 10) % 4

    for rect, row, user in ru_patches:
        rect.set_alpha(
            1.0 if user == active_user else 0.42
        )
        rect.set_linewidth(
            1.5 if user == active_user else 0.4
        )
        rect.set_edgecolor(
            WHITE if user == active_user else BG
        )

    ru_status.set_text(
        f"RU allocation | Highlight: User {active_user + 1}"
    )
    ru_status.set_color(COLORS[active_user])

    # Modulation: progress through five modulation schemes.
    mod_index = min(frame // FRAMES_PER_MOD, 4)
    order = mod_orders[mod_index]
    points = qam_constellation(order)

    scatter.set_offsets(points)
    scatter.set_sizes(
        np.full(order, 25 if order <= 64 else
                12 if order <= 256 else 5)
    )

    mod_label.set_text(
        f"{mod_names[mod_index]} | {bits_per_symbol[mod_index]} bits/symbol"
    )
    mod_explanation.set_text(
        f"{order} constellation points\n"
        "Higher order: more bits per symbol,\n"
        "but greater sensitivity to noise."
    )

    # Coding: illustrate changing emphasis on redundancy.
    # This is a conceptual graphic, not an implemented code.
    phase = (frame // 15) % 3
    coding_labels = [
        "Higher-rate coding (conceptual)",
        "Balanced coding (conceptual)",
        "More redundancy (conceptual)"
    ]
    highlighted = [6, 4, 2][phase]

    for i, rect in enumerate(coding_boxes):
        rect.set_facecolor(
            COLORS[2] if i < highlighted else "#24374E"
        )
        rect.set_alpha(0.95 if i < highlighted else 0.45)

    coding_text.set_text(coding_labels[phase])

    return (
        [p[0] for p in ru_patches]
        + [ru_status, scatter, mod_label, mod_explanation]
        + coding_boxes + [coding_text]
    )

fig.subplots_adjust(
    left=0.055, right=0.98, top=0.86, bottom=0.20, wspace=0.30
)

animation = FuncAnimation(
    fig,
    update,
    frames=TOTAL_FRAMES,
    interval=140,
    blit=False,
    repeat=True
)

# Save animated visual for PowerPoint
print("Saving animation... Please wait.")
animation.save(
    "wifi6_ofdma_modulation_coding.gif",
    writer=PillowWriter(fps=7),
    dpi=90
)

# Save a static image for a theory slide
update(79)
fig.savefig(
    "wifi6_visualization_static.png",
    dpi=180,
    facecolor=fig.get_facecolor(),
    bbox_inches="tight"
)

print("Done!")
print("Created: wifi6_ofdma_modulation_coding.gif")
print("Created: wifi6_visualization_static.png")

plt.show()
