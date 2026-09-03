/**
 * FastStrap - Automatic Initialization Script
 *
 * Initializes Bootstrap Tooltips/Popovers, ToggleGroups, TextClamp,
 * FocusTraps, SearchableSelect, DateRangePresets, InfiniteScroll,
 * SSETargets, Mermaid diagrams, OTP groups, Tags, SwapOnEvent,
 * and KaTeX math rendering.
 *
 * Re-runs on htmx:afterSwap for dynamic content.
 * Minified version available in faststrap-init.min.js.
 */
document.addEventListener('DOMContentLoaded', () => {
    const initBS = (scope) => {
        if (!window.bootstrap) return;
        // Tooltips
        scope.querySelectorAll('[data-bs-toggle="tooltip"]')
             .forEach(el => new bootstrap.Tooltip(el));
        // Popovers
        scope.querySelectorAll('[data-bs-toggle="popover"]')
             .forEach(el => new bootstrap.Popover(el));
        // Toasts
        scope.querySelectorAll('.toast').forEach(el => {
            if (el.dataset.fsToastInit === 'true') return;
            el.dataset.fsToastInit = 'true';
            const delay = parseInt(el.dataset.bsDelay || '5000', 10);
            new bootstrap.Toast(el, { delay }).show();
        });
    };

    const initToggleGroups = (scope) => {
        scope.querySelectorAll('[data-fs-toggle-group="true"]').forEach(group => {
            if (group.dataset.fsToggleInit === 'true') return;
            group.dataset.fsToggleInit = 'true';

            const activeClass = group.dataset.fsActiveClass || 'active';
            const inputId = group.dataset.fsInputId;
            const hiddenInput = inputId ? document.getElementById(inputId) : null;

            const setActive = (btn) => {
                group.querySelectorAll('[data-fs-toggle-item="true"]').forEach(item => {
                    item.classList.remove(activeClass);
                    item.setAttribute('aria-pressed', 'false');
                    item.setAttribute('aria-current', 'false');
                });
                btn.classList.add(activeClass);
                btn.setAttribute('aria-pressed', 'true');
                btn.setAttribute('aria-current', 'true');
                if (hiddenInput) hiddenInput.value = btn.dataset.fsValue || '';
            };

            group.querySelectorAll('[data-fs-toggle-item="true"]').forEach(btn => {
                btn.addEventListener('click', () => setActive(btn));
            });
        });
    };

    const initTextClamp = (scope) => {
        scope.querySelectorAll('[data-fs-text-clamp="true"]').forEach(container => {
            if (container.dataset.fsTextClampInit === 'true') return;
            container.dataset.fsTextClampInit = 'true';

            const btn = container.querySelector('[data-fs-text-toggle="true"]');
            const preview = container.querySelector('[data-fs-preview="true"]');
            const full = container.querySelector('[data-fs-full="true"]');
            if (!btn || !preview || !full) return;

            const expandLabel = btn.dataset.fsExpandLabel || 'Show more';
            const collapseLabel = btn.dataset.fsCollapseLabel || 'Show less';
            let expanded = false;

            btn.addEventListener('click', () => {
                expanded = !expanded;
                preview.classList.toggle('d-none', expanded);
                full.classList.toggle('d-none', !expanded);
                btn.textContent = expanded ? collapseLabel : expandLabel;
                btn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
            });
        });
    };

    const initFocusTraps = (scope) => {
        const FOCUSABLE =
            'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';
        const focusTrapStates = window.__fsFocusTrapStates || new WeakMap();
        window.__fsFocusTrapStates = focusTrapStates;

        const isVisible = (node) => {
            if (!(node instanceof HTMLElement)) return false;
            const style = window.getComputedStyle(node);
            return style.display !== 'none'
                && style.visibility !== 'hidden'
                && node.getClientRects().length > 0;
        };

        const getFocusable = (container) => {
            return Array.from(container.querySelectorAll(FOCUSABLE))
                .filter(node => isVisible(node));
        };

        const activateFocusTrap = (container) => {
            if (!isVisible(container)) return;

            const focusables = getFocusable(container);
            if (focusables.length === 0) return;

            const existing = focusTrapStates.get(container);
            if (existing && existing.active) return;

            const previous = document.activeElement instanceof HTMLElement
                ? document.activeElement
                : null;
            const first = focusables[0];
            const last = focusables[focusables.length - 1];

            const handler = (e) => {
                if (e.key !== 'Tab') return;

                const currentFocusables = getFocusable(container);
                if (currentFocusables.length === 0) return;

                const currentFirst = currentFocusables[0];
                const currentLast = currentFocusables[currentFocusables.length - 1];

                if (e.shiftKey && document.activeElement === currentFirst) {
                    e.preventDefault();
                    currentLast.focus();
                } else if (!e.shiftKey && document.activeElement === currentLast) {
                    e.preventDefault();
                    currentFirst.focus();
                }
            };

            container.addEventListener('keydown', handler);
            focusTrapStates.set(container, { active: true, handler, previous });

            const autofocusSelector = container.dataset.fsAutofocus;
            if (autofocusSelector) {
                const target = container.querySelector(autofocusSelector);
                if (isVisible(target)) {
                    target.focus();
                    return;
                }
            }

            first.focus();
        };

        const deactivateFocusTrap = (container) => {
            const state = focusTrapStates.get(container);
            if (!state || !state.active) return;

            container.removeEventListener('keydown', state.handler);
            state.active = false;
            focusTrapStates.set(container, state);

            if (state.previous && document.body.contains(state.previous)) {
                state.previous.focus();
            }
        };

        scope.querySelectorAll('[data-fs-focus-trap="true"]').forEach(container => {
            if (container.dataset.fsFocusTrapInit === 'true') return;
            container.dataset.fsFocusTrapInit = 'true';

            const owner = container.closest('.modal, .offcanvas') || container;
            const ownerIsModal = owner.classList.contains('modal');
            const ownerIsOffcanvas = owner.classList.contains('offcanvas');

            if (ownerIsModal) {
                owner.addEventListener('shown.bs.modal', () => activateFocusTrap(container));
                owner.addEventListener('hidden.bs.modal', () => deactivateFocusTrap(container));
                if (owner.classList.contains('show')) {
                    activateFocusTrap(container);
                }
                return;
            }

            if (ownerIsOffcanvas) {
                owner.addEventListener('shown.bs.offcanvas', () => activateFocusTrap(container));
                owner.addEventListener('hidden.bs.offcanvas', () => deactivateFocusTrap(container));
                if (owner.classList.contains('show')) {
                    activateFocusTrap(container);
                }
                return;
            }

            activateFocusTrap(container);
        });
    };

    const initSearchableSelect = (scope) => {
        scope.querySelectorAll('[data-fs-searchable-select="true"]').forEach(container => {
            if (container.dataset.fsSearchableInit === 'true') return;
            container.dataset.fsSearchableInit = 'true';

            container.addEventListener('click', (e) => {
                const option = e.target.closest('[data-fs-searchable-option="true"]');
                if (!option || !container.contains(option)) return;
                e.preventDefault();

                const selectId = option.dataset.fsSelectId;
                const inputId = option.dataset.fsInputId;
                const resultsId = option.dataset.fsResultsId;
                if (!selectId) return;

                const hiddenSelect = document.getElementById(selectId);
                if (!hiddenSelect) return;

                const value = option.dataset.fsValue || '';
                const label = option.dataset.fsLabel || option.textContent || '';

                hiddenSelect.innerHTML = '';
                const selectedOption = document.createElement('option');
                selectedOption.value = value;
                selectedOption.text = label;
                selectedOption.selected = true;
                hiddenSelect.appendChild(selectedOption);

                if (inputId) {
                    const input = document.getElementById(inputId);
                    if (input) input.value = label;
                }
                if (resultsId) {
                    const results = document.getElementById(resultsId);
                    if (results) results.innerHTML = '';
                }
            });
        });
    };

    const initDateRangePresets = (scope) => {
        scope.querySelectorAll('[data-fs-date-range="true"]').forEach(form => {
            if (form.dataset.fsDateRangeInit === 'true') return;
            form.dataset.fsDateRangeInit = 'true';

            form.addEventListener('click', (e) => {
                const button = e.target.closest('[data-fs-date-preset="true"]');
                if (!button || !form.contains(button)) return;

                e.preventDefault();

                const startName = button.dataset.fsDateStartName;
                const endName = button.dataset.fsDateEndName;
                const startValue = button.dataset.fsDateStart || '';
                const endValue = button.dataset.fsDateEnd || '';

                const startInput = startName ? form.elements.namedItem(startName) : null;
                const endInput = endName ? form.elements.namedItem(endName) : null;

                if (startInput) startInput.value = startValue;
                if (endInput) endInput.value = endValue;

                if (button.dataset.fsDatePresetSubmit === 'true') {
                    if (typeof form.requestSubmit === 'function') {
                        form.requestSubmit();
                    } else {
                        form.submit();
                    }
                }
            });
        });
    };

    const initInfiniteScroll = (scope) => {
        scope.querySelectorAll('[data-fs-infinite-scroll="true"]').forEach(el => {
            if (el.dataset.fsInfiniteInit === 'true') return;
            el.dataset.fsInfiniteInit = 'true';

            const margin = el.dataset.fsInfiniteMargin || '0px';
            if (!('IntersectionObserver' in window) || !window.htmx) {
                return;
            }

            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) return;
                    window.htmx.trigger(el, 'faststrap:infinite-scroll');
                    observer.disconnect();
                });
            }, {
                root: null,
                rootMargin: `0px 0px ${margin} 0px`,
                threshold: 0,
            });

            observer.observe(el);

            const cleanup = new MutationObserver(() => {
                if (!document.body.contains(el)) {
                    observer.disconnect();
                    cleanup.disconnect();
                }
            });
            cleanup.observe(document.body, { childList: true, subtree: true });
        });
    };

    const initSseTargets = (scope) => {
        scope.querySelectorAll('[data-fs-sse="true"]').forEach(el => {
            if (el.dataset.fsSseInit === 'true') return;
            el.dataset.fsSseInit = 'true';

            if (!window.EventSource) return;

            const endpoint = el.dataset.fsSseEndpoint;
            if (!endpoint) return;

            const eventName = el.dataset.fsSseEvent || 'message';
            const swap = el.dataset.fsSseSwap || 'inner';
            const targetSelector = el.dataset.fsSseTarget;
            const withCredentials = el.dataset.fsSseCredentials === 'true';
            const reconnect = el.dataset.fsSseReconnect !== 'false';
            const retryRaw = el.dataset.fsSseRetry;
            const retry = retryRaw ? parseInt(retryRaw, 10) : null;

            let connectionRoot = el;
            let target = el;
            if (targetSelector) {
                const candidate = document.querySelector(targetSelector);
                if (candidate) target = candidate;
            }

            const toFragment = (html) => {
                const template = document.createElement('template');
                template.innerHTML = html;
                return template.content;
            };

            const applySwap = (html) => {
                if (targetSelector && !document.body.contains(target)) {
                    const candidate = document.querySelector(targetSelector);
                    if (candidate) target = candidate;
                }

                switch (swap) {
                    case 'outer':
                    case 'replace':
                        {
                            const parent = target.parentNode;
                            if (!parent) return;

                            const marker = document.createElement('span');
                            marker.hidden = true;
                            marker.setAttribute('data-fs-sse-marker', 'true');
                            parent.insertBefore(marker, target);
                            target.remove();
                            marker.insertAdjacentHTML('afterend', html);
                            const replacement = marker.nextElementSibling;
                            marker.remove();

                            if (!replacement) {
                                if (source) source.close();
                                if (observer) observer.disconnect();
                                return;
                            }

                            const replacedConnectionRoot = target === connectionRoot;
                            target = replacement;
                            if (replacedConnectionRoot) {
                                connectionRoot = replacement;
                            }
                        }
                        break;
                    case 'before':
                        target.insertAdjacentHTML('beforebegin', html);
                        break;
                    case 'after':
                        target.insertAdjacentHTML('afterend', html);
                        break;
                    case 'append':
                        target.insertAdjacentHTML('beforeend', html);
                        break;
                    case 'prepend':
                        target.insertAdjacentHTML('afterbegin', html);
                        break;
                    default:
                        target.innerHTML = html;
                }
            };
            const handler = (evt) => {
                const data = evt.data ?? '';
                if (swap === 'text') {
                    target.textContent = data;
                    return;
                }
                applySwap(data);
            };

            let source = null;
            let reconnectTimer = null;
            let observer = null;

            const connect = () => {
                if (!document.body.contains(connectionRoot)) return;
                source = new EventSource(endpoint, { withCredentials });
                source.addEventListener(eventName, handler);
                source.onerror = () => {
                    if (!reconnect) {
                        source.close();
                        source = null;
                        return;
                    }

                    if (retry !== null && Number.isFinite(retry)) {
                        source.close();
                        source = null;
                        if (reconnectTimer) {
                            window.clearTimeout(reconnectTimer);
                        }
                        reconnectTimer = window.setTimeout(() => {
                            reconnectTimer = null;
                            connect();
                        }, retry);
                    }
                };
            };

            connect();

            observer = new MutationObserver(() => {
                if (!document.body.contains(connectionRoot)) {
                    if (source) {
                        source.close();
                        source = null;
                    }
                    if (reconnectTimer) {
                        window.clearTimeout(reconnectTimer);
                        reconnectTimer = null;
                    }
                    observer.disconnect();
                }
            });
            observer.observe(document.body, { childList: true, subtree: true });
        });
    };

    const initMermaid = (scope) => {
        if (!window.mermaid) return;

        const nodes = Array.from(scope.querySelectorAll('[data-fs-mermaid="true"]'))
            .filter(el => el.dataset.fsMermaidInit !== 'true');
        if (nodes.length === 0) return;

        if (!window.__fsMermaidInit) {
            const first = nodes[0];
            const config = { startOnLoad: false };
            const theme = first.dataset.fsMermaidTheme;
            const security = first.dataset.fsMermaidSecurity;
            if (theme) config.theme = theme;
            if (security) config.securityLevel = security;
            try {
                window.mermaid.initialize(config);
            } catch (e) {
                return;
            }
            window.__fsMermaidInit = true;
        }

        try {
            if (window.mermaid.run) {
                window.mermaid.run({ nodes });
            } else if (window.mermaid.init) {
                window.mermaid.init(undefined, nodes);
            }
        } catch (e) {
            return;
        }

        nodes.forEach(el => {
            el.dataset.fsMermaidInit = 'true';
        });
    };

    // OTP Group auto-advance for multi-field OTP inputs
    const initOtpGroups = (scope) => {
        scope.querySelectorAll('[data-fs-otp-group="true"]').forEach(group => {
            if (group.dataset.fsOtpInit === 'true') return;
            group.dataset.fsOtpInit = 'true';
            const inputs = group.querySelectorAll('.otp-digit-input');
            inputs.forEach((input, idx) => {
                input.addEventListener('input', (e) => {
                    const val = e.target.value.replace(/\D/g, '');
                    e.target.value = val.slice(-1);
                    if (val && idx < inputs.length - 1) {
                        inputs[idx + 1].focus();
                    }
                });
                input.addEventListener('keydown', (e) => {
                    if (e.key === 'Backspace' && !e.target.value && idx > 0) {
                        inputs[idx - 1].focus();
                    }
                });
                input.addEventListener('paste', (e) => {
                    e.preventDefault();
                    const pasted = (e.clipboardData || window.clipboardData).getData('text').replace(/\D/g, '');
                    for (let i = 0; i < Math.min(pasted.length, inputs.length); i++) {
                        inputs[i].value = pasted[i];
                    }
                    const focusIdx = Math.min(pasted.length, inputs.length - 1);
                    inputs[focusIdx].focus();
                });
            });
        });
    };

    // Tag remove animation
    const initTags = (scope) => {
        scope.querySelectorAll('[data-fs-tag="true"]').forEach(tag => {
            if (tag.dataset.fsTagInit === 'true') return;
            tag.dataset.fsTagInit = 'true';

            const removeBtn = tag.querySelector('.btn-close');
            if (!removeBtn) return;

            removeBtn.addEventListener('click', () => {
                if (tag.dataset.fsTagRemoving === 'true') return;
                tag.dataset.fsTagRemoving = 'true';
                tag.classList.add('faststrap-tag-exit');
                tag.addEventListener('animationend', () => {
                    if (document.body.contains(tag)) tag.remove();
                }, { once: true });
            });
        });
    };

    // SwapOnEvent: trigger HTMX swap from custom client events
    const initSwapOnEvent = (scope) => {
        scope.querySelectorAll('[data-fs-swap-event]').forEach(el => {
            if (el.dataset.fsSwapInit === 'true') return;
            el.dataset.fsSwapInit = 'true';

            const eventName = el.dataset.fsSwapEvent;
            const target = el.dataset.fsSwapTarget || 'this';
            const swap = el.dataset.fsSwap || 'innerHTML';

            el.addEventListener(eventName, () => {
                if (!window.htmx) return;
                htmx.ajax('GET', el.dataset.fsSwapEndpoint || window.location.href, {
                    target,
                    swap,
                });
            });
        });
    };

    // KaTeX math auto-rendering for .faststrap-math elements
    const initMath = (scope) => {
        if (typeof renderMathInElement !== 'function') return;

        scope.querySelectorAll('.faststrap-math').forEach(el => {
            if (el.dataset.fsMathInit === 'true') return;
            el.dataset.fsMathInit = 'true';

            const throwOnError = el.dataset.fsMathThrowOnError === 'true';

            try {
                renderMathInElement(el, {
                    throwOnError,
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '\\(', right: '\\)', display: false},
                    ],
                });
            } catch (e) {
                // KaTeX will render the source as fallback text on error
            }
        });
    };

    // Initialize all modules on DOMContentLoaded
    initBS(document);
    initToggleGroups(document);
    initTextClamp(document);
    initFocusTraps(document);
    initSearchableSelect(document);
    initDateRangePresets(document);
    initInfiniteScroll(document);
    initSseTargets(document);
    initMermaid(document);
    initOtpGroups(document);
    initTags(document);
    initSwapOnEvent(document);
    initMath(document);

    // HTMX support: Re-initialize on content swap.
    // Cross-version: uses FaststrapHtmx bridge so this fires on htmx 2
    // (htmx:afterSwap) and htmx 4 (htmx:after:swap), with a normalized scope.
    const reinitAfterSwap = (evt) => {
        const scope = (window.FaststrapHtmx && window.FaststrapHtmx.swap(evt)) || evt.detail?.elt || document;
        initBS(scope);
        initToggleGroups(scope);
        initTextClamp(scope);
        initFocusTraps(scope);
        initSearchableSelect(scope);
        initDateRangePresets(scope);
        initInfiniteScroll(scope);
        initSseTargets(scope);
        initMermaid(scope);
        initOtpGroups(scope);
        initTags(scope);
        initSwapOnEvent(scope);
        initMath(scope);
    };
    if (window.FaststrapHtmx) {
        window.FaststrapHtmx.onSwap(reinitAfterSwap);
    } else if (document.body) {
        document.body.addEventListener('htmx:afterSwap', reinitAfterSwap);
    }
});