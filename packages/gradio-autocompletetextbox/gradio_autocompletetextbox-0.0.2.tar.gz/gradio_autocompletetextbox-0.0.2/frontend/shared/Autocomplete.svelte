<script lang="ts">
    import { createEventDispatcher, onMount, afterUpdate } from 'svelte';
    import { fly } from 'svelte/transition';
  
    export let suggestions: string[] = [];
    export let highlightedIndex: number | null = null;
    export let container = true;
    export let show_label = true;
  
    const dispatch = createEventDispatcher();
  
    let listElement: HTMLUListElement;
    let isMouseOver = false;
    let wrapperElement: HTMLDivElement;

    function updatePosition() {
        if (listElement && wrapperElement) {
            const listHeight = listElement.offsetHeight;
            wrapperElement.style.transform = `translateY(-${listHeight}px)`;
        }
    }
    $: if (suggestions.length > 0 && highlightedIndex === null) {
        highlightedIndex = 0;
    }

    function handleKeyDown(event: KeyboardEvent) {
        if ((event.key === 'Enter' || event.key === 'Tab') && highlightedIndex !== null) {
            event.preventDefault();
            dispatch('select', suggestions[highlightedIndex]);
        } else if (event.key === "ArrowDown") {
            event.preventDefault();
            highlightedIndex = highlightedIndex === null ? 0 : (highlightedIndex + 1) % suggestions.length;
        } else if (event.key === "ArrowUp") {
            event.preventDefault();
            highlightedIndex = highlightedIndex === null ? suggestions.length - 1 : (highlightedIndex - 1 + suggestions.length) % suggestions.length;
        } else if (event.key === "Escape") {
            event.preventDefault();
            dispatch('close');
        }
    }
  
    function handleMouseDown(suggestion: string) {
        dispatch('select', suggestion);
    }

    function handleMouseOver(index: number) {
        isMouseOver = true;
        highlightedIndex = index;
    }

    function handleMouseLeave() {
        isMouseOver = false;
    }
  
    onMount(() => {
        console.log(container)
        if (listElement) {
            listElement.style.maxHeight = '200px';
        }
    });

    afterUpdate(() => {
        updatePosition();
        if (listElement && highlightedIndex !== null && !isMouseOver) {
            const highlightedElement = listElement.children[highlightedIndex] as HTMLElement;
            if (highlightedElement) {
                highlightedElement.scrollIntoView({ block: 'nearest' });
            }
        }
    });
</script>
  
<svelte:window on:keydown={handleKeyDown} />
  
<div bind:this={wrapperElement}>
{#if suggestions.length > 0}
    <ul 
        class="autocomplete-list"
        class:contained={container}
        class:nolabel={!show_label && container}
        bind:this={listElement} 
        transition:fly="{{ y: 5, duration: 100 }}"
        on:mouseleave={handleMouseLeave}
    >
        {#each suggestions as suggestion, i}
            <li
                class="autocomplete-item"
                class:highlighted={i === highlightedIndex}
                on:mousedown|preventDefault={() => handleMouseDown(suggestion)}
                on:mouseover={() => handleMouseOver(i)}
            >
                {suggestion}
            </li>
        {/each}
    </ul>
{/if}
</div>

  <style>
    .autocomplete-list {
      position: absolute;
      /* width: 100%; */
      left: 5px;
      top: -1px;
      max-height: 300px;
      overflow-y: auto;
      list-style-type: none;
      padding: 0;
      margin: 0;
      border: 1px solid var(--input-border-color);
      /* border-bottom: none; */
      border-radius: var(--input-radius);
      background-color: var(--input-background-fill);
      z-index: 99;
    }
    .contained {
        left: 0px;
        top: 25px;
    }
    .nolabel {
        top: -3px;
    }
    .autocomplete-item {
      padding: 8px 12px;
      cursor: pointer;
    }
  
    .autocomplete-item.highlighted {
      background-color: var(--input-border-color-focus);
      color: var(--body-text-color);
    }
  </style>