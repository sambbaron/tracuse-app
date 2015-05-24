var Tracuse = Tracuse || {};

// Custom HTML Elements
Tracuse.customEl = Tracuse.customEl || {};

// Initialize Custom Elements

Tracuse.customEl.Viewuse = document.registerElement(
    'x-viewuse',
    {prototype: Object.create(HTMLElement.prototype)}
);

Tracuse.customEl.DatumObject = document.registerElement(
    'x-datum',
    {prototype: Object.create(HTMLElement.prototype)}
);

Tracuse.customEl.DatumElement = document.registerElement(
    'x-datum-element',
    {
        prototype: Object.create(HTMLInputElement.prototype),
        extends: 'input'
    }
);