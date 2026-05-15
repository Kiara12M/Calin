import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Tes } from './tes';

describe('Tes', () => {
  let component: Tes;
  let fixture: ComponentFixture<Tes>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Tes]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Tes);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
