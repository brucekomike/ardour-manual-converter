# Using the MCP HTTP Surface
The [[MCP]{.dfn}]{.abbr title="Model Context Protocol"} HTTP control
surface is an experimental server that lets an MCP-capable assistant
inspect and control a running Ardour session.

In this context, MCP means *Model Context Protocol*. It is not the
Mackie Control Protocol used by hardware control surfaces. Model Context
Protocol is a way for applications to expose tools and data to AI
assistants and other compatible clients.

It is intended for practical assisted workflows such as session setup,
transport control, track and bus management, plugin adjustment, marker
and range editing, and MIDI region editing. The surface exposes these
operations as MCP tools over a local HTTP endpoint.

MCP clients can make changes to the current session. Use snapshots or
save the session before asking an assistant to perform destructive edits
such as deleting markers, moving regions, normalizing audio, or changing
many plugin parameters.

## Enabling the MCP HTTP Surface

To enable the surface, open the *Preferences* dialog and go to the
*Control Surfaces* page. Enable *MCPHttp*, then open its settings
dialog.

The settings dialog provides the MCP endpoint information and these
options:

- The HTTP listen port. The default port is `4820`.
- A debug level for logging MCP requests in Ardour\'s log window.
- An option to listen on all network interfaces.

By default, the server listens on all interfaces of the local machine,
including but not limited to localhost:

    http://127.0.0.1:4820/mcp

Listening on all network interfaces can expose Ardour control to other
devices on the network. Only enable this on trusted networks and only
when a remote MCP client needs to connect to Ardour.

## Client Setup

Use the endpoint shown in the MCPHttp settings dialog when configuring
an MCP client. The transport is HTTP. Server-Sent Events transport is
not used.

### Codex CLI

    codex mcp add ardour_http --url http://127.0.0.1:4820/mcp

The equivalent entry in `~/.codex/config.toml` is:

    [mcp_servers.ardour_http]
    url = "http://127.0.0.1:4820/mcp"

### Gemini CLI

    gemini mcp add ardour-http http://127.0.0.1:4820/mcp --type http

### Claude Desktop

Claude Desktop can connect through `mcp-remote`. In *Settings \>
Developer*, add:

    {
      "mcpServers": {
        "ardour-http": {
          "command": "npx",
          "args": [
            "mcp-remote@latest",
            "http://127.0.0.1:4820/mcp"
          ]
        }
      }
    }

### Copilot CLI

In Copilot CLI, run `/mcp add` and fill in the form with an HTTP MCP
server named `ardour-http` using the URL `http://127.0.0.1:4820/mcp`.

## Available Tool Areas

Exact tool names can be inspected through the MCP client\'s tool
listing. The MCP HTTP surface currently exposes tools in these areas:

- Session information, saving, undo, redo, renaming, snapshots, and
  mixer scenes.
- Transport state, locate, play, stop, loop, punch, record enable, and
  marker navigation.
- Track and bus listing, creation, selection, renaming, fader, pan,
  mute, solo, record enable, and record safe.
- Sends, including adding sends, removing sends, level control, and
  pre-fader or post-fader placement.
- Plugin discovery, insertion, removal, order, position, bypass, and
  parameter control.
- Markers, ranges, loop ranges, punch ranges, and arrangement markers.
- Region inspection, move, copy, resize, split, gain, and normalization.
- MIDI region creation, note insertion, note listing, note editing, and
  bulk JSON import or export.

## Example Tool Names

Some tools use explicit names to avoid ambiguous argument combinations.
For example, locating by bars and beats uses a different tool from
locating by sample.

- `transport_get_state`
- `transport_locate_bbt`
- `transport_locate_sample`
- `tracks_list`
- `tracks_add`
- `buses_add`
- `track_get_info`
- `track_set_fader_db`
- `track_set_fader_position`
- `track_set_send_level_db`
- `plugin_list_available`
- `plugin_add_by_plugin_id`
- `plugin_set_parameter_by_index_value`
- `markers_list`
- `markers_add`
- `markers_add_range_bbt`
- `region_move_by_beats`
- `region_copy_to_bbt`
- `midi_region_add_bbt`
- `midi_note_import_json_into_region`

## Working With MIDI JSON

For creating more than a few notes, prefer the MIDI JSON tools over
adding one note at a time. They allow an assistant to create or edit a
complete phrase, drum groove, or chord pattern in one tool call.

MIDI JSON timing is relative to the start of the target region. In this
format, `bar: 1` and `b: 1` mean the first beat of the region,
regardless of where that region starts in the session timeline.

The `b` value is the beat within the bar and may be fractional. For
example, `b: 1.5` represents an off-beat eighth-note position in common
4/4 timing. The `t` value is an additional tick offset within the beat,
using the JSON file\'s `ticks_per_quarter` value.

In drum mode, note-off events are optional. Drum hits can be supplied as
note-on events only; Ardour writes them as zero-length notes, with
note-on and note-off at the same timestamp. For non-drum material, use
note-on and note-off timing pairs for sustained notes and chords.

## Prompt Examples

Some MCP clients allow a system message, startup message, project
instruction, or reusable chat preamble. The following text can help an
assistant use Ardour MCP tools more reliably:

    You are connected to Ardour through the Ardour MCP HTTP control surface.

    Use Ardour MCP tools when answering questions about the current Ardour session
    or when making requested session changes. Prefer reading current state before
    editing: list tracks, get track info, list markers, inspect regions, and inspect
    plugins as needed.

    When changing the session, use exact IDs returned by Ardour whenever possible.
    Track names, marker names, plugin names, and region names may not be unique. If
    there is ambiguity, ask before making the change.

    Use musical time when the user describes bars and beats. Bar and beat values are
    one-based. Fractional beats are allowed, for example beat 3.5 means halfway
    between beats 3 and 4. MIDI JSON note positions are relative to the start of the
    target region: bar 1 beat 1 is the start of that region, not the session.

    For larger generated MIDI parts, prefer the MIDI JSON import tools instead of
    adding one note at a time. Use individual note tools for small corrections or
    short phrases. In MIDI JSON, provide clear timing, pitch, velocity, and channel
    data, and use drum mode for drum grooves when appropriate.

    When setting levels, prefer dB values when the tool supports them. Do not assume
    linear fader positions are dB. For panning, follow the Ardour MCP tool
    description because Ardour's pan value convention may differ from other systems.

    Before destructive actions such as deleting markers, deleting plugins, deleting
    sends, overwriting ranges, or moving/copying many regions, briefly confirm the
    target if the user's request is not explicit.

    After making a change, verify it with a readback call and summarize what changed
    using track names, region names, marker names, plugin names, and musical
    locations where useful.

The following examples show the kind of requests an MCP-capable
assistant can translate into Ardour operations:

- Show the transport state and list all markers.
- Set the loop range from bar 32 for 8 bars and enable loop playback.
- Create tracks for a live band: lead vocal, two backing vocals, two
  guitars, bass, stereo drums, and stereo keys.
- Create a bus called Vocal Verb and add post-fader sends from the vocal
  tracks to it.
- List available EQ plugins and add one to the Rose track.
- Set the send level from Frank to Vocal Verb to -12 dB.
- Add marker Frank at bar 7 beat 3.5.
- Add arrangement section Solo 2 at bar 40.
- Create a MIDI region on MCP MIDI Test from bar 3 for 2 bars.
- Insert a C major up-and-down scale using eighth notes with velocity
  around 80.
- Add 4 bars of steady drum groove in the existing drum MIDI region.
- In bar 4, add solid quarter-note chords in the key of F on each beat.
- Move region Test Part A by 2.5 beats later on the same track.
- Copy this region four times every two bars.

## Client Compatibility

Tool responses include structured MCP data and a JSON text fallback. The
text fallback is intentional because some MCP clients display only text
content and do not expose structured result data to the assistant.

## Known Limitations

- The surface is experimental and may change based on user feedback.
- Most edit operations identify tracks, plugins, regions, and markers by
  explicit IDs or names.
- Selected-region targeting is not implemented.
- MCP clients and models vary in how well they use tool descriptions and
  structured return data.
