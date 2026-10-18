/**
 * FastStrap - ModernToast Runtime
 *
 * Provides auto-dismiss, keyboard dismiss, pause-on-hover, swipe-to-dismiss,
 * and queue management for ModernToast components.
 *
 * Loaded only when ModernToast or ModernToastStack is used.
 */

(() => {
  'use strict';

  const TOAST_KEY = 'fsModernToast';
  const STACK_KEY = 'fsModernToastStack';
  const DISMISS_REASONS = { MANUAL: 'manual', AUTO: 'auto', ESCAPE: 'escape', SWIPE: 'swipe' };

  const readNumber = (value, fallback) => {
    if (value === undefined || value === null || value === '') return fallback;
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : fallback;
  };

  // ── Toast instance management ──────────────────────────────────────────

  const toastInstances = new Map();
  let toastIdCounter = 0;

  const registerToast = (el) => {
    const id = `modern-toast-${++toastIdCounter}`;
    el.dataset[TOAST_KEY] = id;
    const instance = {
      id,
      el,
      timer: null,
      remaining: readNumber(el.dataset.fsDuration, 4000),
      paused: false,
      startTime: 0,
      pauseTime: 0,
      dismissed: false,
    };
    toastInstances.set(id, instance);
    return instance;
  };

  const startTimer = (instance) => {
    if (instance.remaining <= 0) return;
    instance.startTime = Date.now();
    instance.timer = setTimeout(() => {
      dismissToast(instance.el, DISMISS_REASONS.AUTO);
    }, instance.remaining);
  };

  const pauseTimer = (instance) => {
    if (!instance.timer || instance.paused) return;
    clearTimeout(instance.timer);
    instance.timer = null;
    instance.remaining -= Date.now() - instance.startTime;
    instance.paused = true;
    instance.pauseTime = Date.now();
  };

  const resumeTimer = (instance) => {
    if (!instance.paused || instance.remaining <= 0) return;
    instance.paused = false;
    startTimer(instance);
  };

  // ?? Stack queue management ??????????????????????????????????????????????

  const stackOf = (el) => el.closest('[data-fs-modern-toast-stack]');
  const stackQueues = new Map();

  const visibleCount = (stack) =>
    stack.querySelectorAll(
      '.faststrap-modern-toast:not(.faststrap-modern-toast-queued):not(.faststrap-modern-toast-exit)',
    ).length;

  const dequeueNext = (stack) => {
    const queue = stackQueues.get(stack);
    if (!queue || !queue.length) return;
    const next = queue.shift();
    next.classList.remove('faststrap-modern-toast-queued');
    const instance = toastInstances.get(next.dataset[TOAST_KEY]);
    if (instance) resumeTimer(instance);
  };

  const enqueueToast = (el) => {
    const stack = stackOf(el);
    if (!stack) return;
    const max = readNumber(stack.dataset.fsMaxVisible, 5);
    if (max > 0 && visibleCount(stack) > max) {
      let queue = stackQueues.get(stack);
      if (!queue) {
        queue = [];
        stackQueues.set(stack, queue);
      }
      el.classList.add('faststrap-modern-toast-queued');
      queue.push(el);
      const instance = toastInstances.get(el.dataset[TOAST_KEY]);
      if (instance) pauseTimer(instance);
    }
  };

  const dismissToast = (el, reason) => {
    const id = el.dataset[TOAST_KEY];
    const instance = toastInstances.get(id);
    if (!instance || instance.dismissed) return;
    instance.dismissed = true;
    if (instance.timer) clearTimeout(instance.timer);

    const detail = { id: el.id || null, reason, element: el };
    el.dispatchEvent(new CustomEvent('faststrap:toast-dismiss', {
      bubbles: true,
      detail,
    }));
    const dismissEvent = el.dataset.fsDismissEvent;
    if (dismissEvent && dismissEvent !== 'faststrap:toast-dismiss') {
      el.dispatchEvent(new CustomEvent(dismissEvent, {
        bubbles: true,
        detail,
      }));
    }

    const stack = stackOf(el);
    if (stack) dequeueNext(stack);

    el.classList.add('faststrap-modern-toast-exit');
    const onAnimationEnd = () => {
      el.removeEventListener('animationend', onAnimationEnd);
      if (document.body.contains(el)) el.remove();
    };
    el.addEventListener('animationend', onAnimationEnd);

    // Fallback removal if animationend does not fire
    setTimeout(() => {
      el.removeEventListener('animationend', onAnimationEnd);
      if (document.body.contains(el)) el.remove();
    }, 500);

    toastInstances.delete(id);
  };

  const dismissAll = () => {
    toastInstances.forEach((instance) => {
      if (!instance.dismissed) dismissToast(instance.el, DISMISS_REASONS.MANUAL);
    });
    toastInstances.clear();
  };

  // ── Initialization ─────────────────────────────────────────────────────

  const initModernToasts = (scope = document) => {
    const selector = '[data-fs-modern-toast="true"]';
    const elements = [];
    if (scope && typeof scope.matches === 'function' && scope.matches(selector)) {
      elements.push(scope);
    }
    if (scope && typeof scope.querySelectorAll === 'function') {
      scope.querySelectorAll(selector).forEach((el) => elements.push(el));
    }

    elements.forEach((el) => {
      if (el.dataset.fsModernToastInit === 'true') return;
      el.dataset.fsModernToastInit = 'true';

      const instance = registerToast(el);
      const duration = readNumber(el.dataset.fsDuration, 4000);
      if (duration > 0) startTimer(instance);
      enqueueToast(el);

      const pauseOnHover = el.dataset.fsPauseOnHover !== 'false';

      if (pauseOnHover) {
        el.addEventListener('mouseenter', () => pauseTimer(instance));
        el.addEventListener('mouseleave', () => resumeTimer(instance));
        el.addEventListener('focusin', () => pauseTimer(instance));
        el.addEventListener('focusout', () => resumeTimer(instance));
      }

      const escapeHandler = (e) => {
        if (e.key === 'Escape') {
          e.preventDefault();
          dismissToast(el, DISMISS_REASONS.ESCAPE);
        }
      };
      el.addEventListener('keydown', escapeHandler);
      el.dataset.fsEscapeHandler = 'true';

      // Dismiss controls (close button, etc.) anywhere inside the toast.
      const dismissControls = el.querySelectorAll('[data-fs-dismiss]');
      dismissControls.forEach((control) => {
        if (control.dataset.fsDismissInit === 'true') return;
        control.dataset.fsDismissInit = 'true';
        control.addEventListener('click', () => {
          dismissToast(el, DISMISS_REASONS.MANUAL);
        });
      });

      // Action specs dispatch named browser events without embedding arbitrary JS.
      const actionControls = el.querySelectorAll('[data-fs-action-event]');
      actionControls.forEach((control) => {
        if (control.dataset.fsActionEventInit === 'true') return;
        control.dataset.fsActionEventInit = 'true';
        control.addEventListener('click', () => {
          const eventName = control.dataset.fsActionEvent;
          if (!eventName) return;
          control.dispatchEvent(new CustomEvent(eventName, {
            bubbles: true,
            detail: { toast: el, action: control },
          }));
        });
      });

      let touchStartX = 0;
      let touchCurrentX = 0;
      let swiping = false;

      el.addEventListener('touchstart', (e) => {
        touchStartX = e.touches[0].clientX;
        touchCurrentX = touchStartX;
        swiping = true;
      }, { passive: true });

      el.addEventListener('touchmove', (e) => {
        if (!swiping) return;
        touchCurrentX = e.touches[0].clientX;
        const diff = touchCurrentX - touchStartX;
        if (Math.abs(diff) > 10) {
          el.style.transition = 'none';
          el.style.transform = `translateX(${diff}px)`;
          el.style.opacity = String(Math.max(0, 1 - Math.abs(diff) / 220));
        }
      }, { passive: true });

      el.addEventListener('touchend', () => {
        if (!swiping) return;
        swiping = false;
        const diff = touchCurrentX - touchStartX;
        if (Math.abs(diff) > 80) {
          el.style.transition = '';
          el.style.transform = '';
          el.style.opacity = '';
          dismissToast(el, DISMISS_REASONS.SWIPE);
        } else {
          el.style.transition = '';
          el.style.transform = '';
          el.style.opacity = '';
        }
      });
    });
  };

  // ── Public API ──────────────────────────────────────────────────────────

  window.FaststrapModernToast = {
    dismiss: (el) => {
      const target = typeof el === 'string' ? document.querySelector(el) : el;
      if (target) dismissToast(target, DISMISS_REASONS.MANUAL);
    },
    dismissAll,
    registerToast,
    DISMISS_REASONS,
  };

  // ── Boot ────────────────────────────────────────────────────────────────

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => initModernToasts());
  } else {
    initModernToasts();
  }

  // Re-scan swapped content on both htmx 2 and htmx 4 (bridge-normalized scope).
  const rescope = (event, elt) => initModernToasts(elt || document);
  if (window.FaststrapHtmx) {
    window.FaststrapHtmx.onSwap(rescope);
  } else {
    document.addEventListener('htmx:afterSwap', (event) => initModernToasts(event.target));
  }
})();
