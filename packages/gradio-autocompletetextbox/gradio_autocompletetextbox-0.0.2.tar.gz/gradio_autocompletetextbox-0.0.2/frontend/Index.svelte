<svelte:options accessors={true} />

<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import type { CommandData } from "./shared/utils.ts"
	import { BlockTitle } from "@gradio/atoms";
	import { Block } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { tick, onMount } from "svelte";
	import AutocompleteSuggestions from './shared/Autocomplete.svelte';
	import TextBox from "./shared/Textbox.svelte";

	export let gradio: Gradio<{
		change: never;
		submit: never;
		input: never;
		clear_status: LoadingStatus;
	}>;
	export let label: string = "Command Bar";
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let placeholder: string = "";
	export let show_label: boolean;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus | undefined = undefined;
	export let value_is_output = false;
	export let interactive: boolean;
	export let rtl = false;
	export let container = true;

	// Customized props
	export let value: CommandData = { command: null, text: "" };
	export let commands: string[] = [];
	export let maxLines = 5; // Default to 5 lines, adjust as needed

	// Autocomplete functionality
	let el: HTMLInputElement;
	let filteredCommands: string[] = [];
	let highlightedIndex: number | null = null;
	let showSuggestions = false;

	let inputWrapper: HTMLDivElement;
    let inputElement: HTMLTextAreaElement | HTMLInputElement;

    onMount(() => { 
        adjustInputPadding();
    });

    function adjustInputPadding() {
        if (inputWrapper && inputElement && value.command) {
            const commandWidth = inputWrapper.querySelector('.command')?.getBoundingClientRect().width || 0;
            inputElement.style.paddingLeft = `${commandWidth + 10}px`;
        } else if (inputElement) {
            inputElement.style.paddingLeft = '';
        }
    }

	function filterCommands() {
        if (value.text.startsWith('/') && !value.command) {
            filteredCommands = commands.filter(cmd => 
                cmd.toLowerCase().startsWith(value.text.toLowerCase())
            );
            showSuggestions = filteredCommands.length > 0;
        } else {
            filteredCommands = [];
            showSuggestions = false;
        }
        highlightedIndex = null;
    }

    function handleSuggestionSelect(event: CustomEvent<string>) {
        value = { command: event.detail, text: "" };
        showSuggestions = false;
        el.focus();
        handle_change();
    }

    function handle_change(): void {
        if (!value.command && value.text.endsWith(' ')) {
            const possibleCommand = value.text.trim();
            if (commands.includes(possibleCommand)) {
                value = { command: possibleCommand, text: "" };
            }
        }
        filterCommands();
        gradio.dispatch("change");
        if (!value_is_output) {
            gradio.dispatch("input");
        }
    }

    function handleSuggestionClose() {
        showSuggestions = false;
    }

    async function handle_keypress(e: KeyboardEvent): Promise<void> {
        await tick();
        if (e.key === "Enter" && !showSuggestions) {
            e.preventDefault();
            gradio.dispatch("submit");
        }
    }

	function handle_keydown(e: KeyboardEvent): void {
        if (e.key === "Backspace" && value.command && inputElement.selectionStart === 0 && inputElement.selectionEnd === 0) {
            e.preventDefault();
            value = { command: null, text: value.text };
            handle_change();
            adjustInputPadding();
        }
    }

    $: if (value.text === null) value.text = "";
    $: value, handle_change();
	$: console.log(value);
	$: value.command, adjustInputPadding();
</script>

<Block
	{visible}
	{elem_id}
	{elem_classes}
	{scale}
	{min_width}
	allow_overflow={true}
	padding={container}
>
	{#if loading_status}
		<StatusTracker
			autoscroll={gradio.autoscroll}
			i18n={gradio.i18n}
			{...loading_status}
			on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
		/>
	{/if}
	<div class="autocomplete-wrapper">
		{#if showSuggestions}
			<AutocompleteSuggestions
				suggestions={filteredCommands}
				{container}
				{show_label}
				bind:highlightedIndex
				on:select={handleSuggestionSelect}
				on:close={handleSuggestionClose}
			/>
		{/if}
	</div>
	<label class:container>
        <BlockTitle {show_label} info={undefined}>{label}</BlockTitle>
		
		<div class="input-wrapper" bind:this={inputWrapper}>
            {#if value.command}
				<span class="command">{value.command}</span>
			{/if}
			<input
				data-testid="textbox"
				type="text"
				class="scroll-hide"
				bind:value={value.text}
				bind:this={inputElement}
				{placeholder}
				disabled={!interactive}
				dir={rtl ? "rtl" : "ltr"}
				on:keypress={handle_keypress}
				on:keydown={handle_keydown}
				on:input={handle_change}
			/>
			

		</div>
	</label>


<!-- <TextBox
bind:value
bind:value_is_output
{label}
{info}
{show_label}
{lines}
{type}
{rtl}
{text_align}
max_lines={!max_lines ? lines + 1 : max_lines}
{placeholder}
{show_copy_button}
{autofocus}
{container}
{autoscroll}
on:change={() => gradio.dispatch("change", value)}
on:input={() => gradio.dispatch("input")}
on:submit={() => gradio.dispatch("submit")}
on:blur={() => gradio.dispatch("blur")}
on:select={(e) => gradio.dispatch("select", e.detail)}
on:focus={() => gradio.dispatch("focus")}
disabled={!interactive}
/> -->

</Block>

		
<style>
	.command {
        position: absolute;
        left: 5px;
        font-weight: bold;
        background-color: var(--input-border-color-focus);
        padding: 0 5px;
        border-radius: 3px;
        z-index:1;
    }

	.input-wrapper {
        position: relative;
        display: flex;
        align-items: center;
        width: 100%;
        background: var(--input-background-fill);
        /* border: var(--input-border-width) solid var(--input-border-color); */
        border-radius: var(--input-radius);
    }

	label {
		width: 100%;
	}
	.autocomplete-wrapper {
		position: fixed;
		width: 100%;
		z-index: 99;
	}

	.input-wrapper input {
        width: 100%;
        border: none;
        background: transparent;
    }

	input {
		display: block;
		position: relative;
		outline: none !important;
		box-shadow: var(--input-shadow);
		background: var(--input-background-fill);
		padding: var(--input-padding);
		width: 100%;
		color: var(--body-text-color);
		font-weight: var(--input-text-weight);
		font-size: var(--input-text-size);
		line-height: var(--line-sm);
		border: var(--input-border-width) solid var(--input-border-color);
		border-radius: var(--input-radius);
	}

	.container > .input-wrapper > input {
		border: var(--input-border-width) solid var(--input-border-color);
		border-radius: var(--input-radius);
	}

	input:disabled {
		-webkit-text-fill-color: var(--body-text-color);
		-webkit-opacity: 1;
		opacity: 1;
	}

	input:focus {
		box-shadow: var(--input-shadow-focus);
		border-color: var(--input-border-color-focus);
	}

	input::placeholder {
		color: var(--input-placeholder-color);
	}

	label:not(.container),
	label:not(.container) > .input-wrapper > input {
		height: 100%;
	}

</style>