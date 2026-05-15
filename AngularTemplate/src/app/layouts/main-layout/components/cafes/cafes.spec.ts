import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Cafes } from './cafes';

describe('Cafes', () => {
  let component: Cafes;
  let fixture: ComponentFixture<Cafes>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Cafes]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Cafes);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
