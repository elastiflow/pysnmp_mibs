# SNMP MIB module (TROPIC-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-GLOBAL-REG.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:18 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

tropicGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tropicGlobalRegModule.setRevisions(
        ("2014-07-07 12:00",
         "2008-05-29 12:00",
         "2008-07-24 12:00",
         "2009-02-13 12:00",
         "2009-03-02 12:00",
         "2009-03-15 12:00",
         "2009-03-18 12:00",
         "2009-03-31 12:00",
         "2009-04-23 12:00",
         "2009-05-14 12:00",
         "2009-09-25 12:00",
         "2009-11-01 12:00",
         "2009-12-10 12:00",
         "2009-12-29 12:00",
         "2010-01-04 12:00",
         "2010-01-24 12:00",
         "2010-02-17 12:00",
         "2010-05-07 12:00",
         "2010-05-10 12:00",
         "2010-05-11 12:00",
         "2010-06-04 12:00",
         "2010-06-23 12:00",
         "2010-06-28 12:00",
         "2010-07-20 12:00",
         "2010-08-02 12:00",
         "2010-09-10 12:00",
         "2010-09-20 12:00",
         "2010-09-24 12:00",
         "2010-09-28 12:00",
         "2010-10-12 12:00",
         "2010-10-17 12:00",
         "2010-10-19 12:00",
         "2010-11-10 12:00",
         "2010-11-14 12:00",
         "2010-11-22 12:00",
         "2011-05-04 12:00",
         "2011-05-17 12:00",
         "2011-06-07 12:00",
         "2011-06-13 12:00",
         "2011-06-30 12:00",
         "2011-07-07 12:00",
         "2011-07-19 12:00",
         "2011-08-31 12:00",
         "2011-09-06 12:00",
         "2011-09-16 12:00",
         "2011-11-14 12:00",
         "2011-11-21 12:00",
         "2012-01-10 12:00",
         "2012-01-18 12:00",
         "2012-01-19 12:00",
         "2012-02-16 12:00",
         "2012-03-15 12:00",
         "2012-03-18 12:00",
         "2012-03-29 12:00",
         "2012-04-06 12:00",
         "2012-04-24 12:00",
         "2012-04-27 12:00",
         "2012-05-01 12:00",
         "2012-06-18 12:00",
         "2012-07-24 12:00",
         "2012-08-28 12:00",
         "2012-10-12 12:00",
         "2012-11-06 12:00",
         "2013-01-24 12:00",
         "2013-03-07 12:00",
         "2013-03-16 12:00",
         "2013-04-11 12:00",
         "2013-04-19 12:00",
         "2013-05-15 12:00",
         "2013-05-24 12:00",
         "2013-06-24 12:00",
         "2013-06-27 12:00",
         "2013-08-12 12:00",
         "2013-09-04 12:00",
         "2013-10-07 12:00",
         "2013-10-10 12:00",
         "2013-11-25 12:00",
         "2013-12-17 12:00",
         "2014-01-22 12:00",
         "2014-02-19 12:00",
         "2014-04-08 12:00",
         "2014-05-06 12:00",
         "2014-05-09 12:00",
         "2014-05-18 12:00",
         "2014-06-20 12:00",
         "2014-07-07 12:00",
         "2014-08-08 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tropic_ObjectIdentity = ObjectIdentity
tropic = _Tropic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483)
)
if mibBuilder.loadTexts:
    tropic.setStatus("current")
_TropicRegistry_ObjectIdentity = ObjectIdentity
tropicRegistry = _TropicRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1)
)
if mibBuilder.loadTexts:
    tropicRegistry.setStatus("current")
_TropicModules_ObjectIdentity = ObjectIdentity
tropicModules = _TropicModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1)
)
if mibBuilder.loadTexts:
    tropicModules.setStatus("current")
_TnGenericModules_ObjectIdentity = ObjectIdentity
tnGenericModules = _TnGenericModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnGenericModules.setStatus("current")
_TnSystemModules_ObjectIdentity = ObjectIdentity
tnSystemModules = _TnSystemModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnSystemModules.setStatus("current")
_TnEquipmentModules_ObjectIdentity = ObjectIdentity
tnEquipmentModules = _TnEquipmentModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnEquipmentModules.setStatus("current")
_TnShelfModules_ObjectIdentity = ObjectIdentity
tnShelfModules = _TnShelfModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnShelfModules.setStatus("current")
_TnSlotModules_ObjectIdentity = ObjectIdentity
tnSlotModules = _TnSlotModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSlotModules.setStatus("current")
_TnCardModules_ObjectIdentity = ObjectIdentity
tnCardModules = _TnCardModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tnCardModules.setStatus("current")
_TnPortModules_ObjectIdentity = ObjectIdentity
tnPortModules = _TnPortModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tnPortModules.setStatus("current")
_TnMiscModules_ObjectIdentity = ObjectIdentity
tnMiscModules = _TnMiscModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tnMiscModules.setStatus("current")
_TnServiceModules_ObjectIdentity = ObjectIdentity
tnServiceModules = _TnServiceModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tnServiceModules.setStatus("current")
_TnProtocolModules_ObjectIdentity = ObjectIdentity
tnProtocolModules = _TnProtocolModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tnProtocolModules.setStatus("current")
_TropicExprModules_ObjectIdentity = ObjectIdentity
tropicExprModules = _TropicExprModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tropicExprModules.setStatus("current")
_TnGmplsMIBModules_ObjectIdentity = ObjectIdentity
tnGmplsMIBModules = _TnGmplsMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tnGmplsMIBModules.setStatus("current")
_TnTypeDefinitionModules_ObjectIdentity = ObjectIdentity
tnTypeDefinitionModules = _TnTypeDefinitionModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnTypeDefinitionModules.setStatus("current")
_TropicMetroReg_ObjectIdentity = ObjectIdentity
tropicMetroReg = _TropicMetroReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3)
)
if mibBuilder.loadTexts:
    tropicMetroReg.setStatus("current")
_TropicMetroNodeReg_ObjectIdentity = ObjectIdentity
tropicMetroNodeReg = _TropicMetroNodeReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tropicMetroNodeReg.setStatus("current")
_TropicTRX24000_ObjectIdentity = ObjectIdentity
tropicTRX24000 = _TropicTRX24000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tropicTRX24000.setStatus("current")
_AluWdm1830PSS32_ObjectIdentity = ObjectIdentity
aluWdm1830PSS32 = _AluWdm1830PSS32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS32.setStatus("current")
_AluWdm1830PSS1_ObjectIdentity = ObjectIdentity
aluWdm1830PSS1 = _AluWdm1830PSS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS1.setStatus("current")
_AluWdm1830PSS1MD4H_ObjectIdentity = ObjectIdentity
aluWdm1830PSS1MD4H = _AluWdm1830PSS1MD4H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS1MD4H.setStatus("current")
_AluWdm1830PSS1GBEH_ObjectIdentity = ObjectIdentity
aluWdm1830PSS1GBEH = _AluWdm1830PSS1GBEH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS1GBEH.setStatus("current")
_AluWdm1830PSS_ObjectIdentity = ObjectIdentity
aluWdm1830PSS = _AluWdm1830PSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS.setStatus("current")
_AluWdm1830PSS4_ObjectIdentity = ObjectIdentity
aluWdm1830PSS4 = _AluWdm1830PSS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS4.setStatus("current")
_AluWdm1830PSS1MSAH_ObjectIdentity = ObjectIdentity
aluWdm1830PSS1MSAH = _AluWdm1830PSS1MSAH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 9)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS1MSAH.setStatus("current")
_TropicShelfReg_ObjectIdentity = ObjectIdentity
tropicShelfReg = _TropicShelfReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4)
)
if mibBuilder.loadTexts:
    tropicShelfReg.setStatus("current")
_TropicEmptyShelf_ObjectIdentity = ObjectIdentity
tropicEmptyShelf = _TropicEmptyShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tropicEmptyShelf.setStatus("current")
_TropicUnknownShelf_ObjectIdentity = ObjectIdentity
tropicUnknownShelf = _TropicUnknownShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tropicUnknownShelf.setStatus("current")
_AluWdmSfd44Shelf_ObjectIdentity = ObjectIdentity
aluWdmSfd44Shelf = _AluWdmSfd44Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 7)
)
if mibBuilder.loadTexts:
    aluWdmSfd44Shelf.setStatus("current")
_AluWdmDcmShelf_ObjectIdentity = ObjectIdentity
aluWdmDcmShelf = _AluWdmDcmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 8)
)
if mibBuilder.loadTexts:
    aluWdmDcmShelf.setStatus("current")
_AluWdmUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmUniversalShelf = _AluWdmUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 9)
)
if mibBuilder.loadTexts:
    aluWdmUniversalShelf.setStatus("current")
_AluWdmSfd44bShelf_ObjectIdentity = ObjectIdentity
aluWdmSfd44bShelf = _AluWdmSfd44bShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 10)
)
if mibBuilder.loadTexts:
    aluWdmSfd44bShelf.setStatus("current")
_AluWdmItlbShelf_ObjectIdentity = ObjectIdentity
aluWdmItlbShelf = _AluWdmItlbShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 11)
)
if mibBuilder.loadTexts:
    aluWdmItlbShelf.setStatus("current")
_AluWdmPSS32UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS32UniversalShelf = _AluWdmPSS32UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 12)
)
if mibBuilder.loadTexts:
    aluWdmPSS32UniversalShelf.setStatus("current")
_AluWdmPSS16UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS16UniversalShelf = _AluWdmPSS16UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 13)
)
if mibBuilder.loadTexts:
    aluWdmPSS16UniversalShelf.setStatus("current")
_AluWdmSfd40Shelf_ObjectIdentity = ObjectIdentity
aluWdmSfd40Shelf = _AluWdmSfd40Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 14)
)
if mibBuilder.loadTexts:
    aluWdmSfd40Shelf.setStatus("current")
_AluWdmSfd40bShelf_ObjectIdentity = ObjectIdentity
aluWdmSfd40bShelf = _AluWdmSfd40bShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 15)
)
if mibBuilder.loadTexts:
    aluWdmSfd40bShelf.setStatus("current")
_AluWdmPSS4UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS4UniversalShelf = _AluWdmPSS4UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 16)
)
if mibBuilder.loadTexts:
    aluWdmPSS4UniversalShelf.setStatus("current")
_AluWdmPSS36UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS36UniversalShelf = _AluWdmPSS36UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 18)
)
if mibBuilder.loadTexts:
    aluWdmPSS36UniversalShelf.setStatus("current")
_AluWdmPSS64UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS64UniversalShelf = _AluWdmPSS64UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 23)
)
if mibBuilder.loadTexts:
    aluWdmPSS64UniversalShelf.setStatus("current")
_AluWdmItluShelf_ObjectIdentity = ObjectIdentity
aluWdmItluShelf = _AluWdmItluShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 24)
)
if mibBuilder.loadTexts:
    aluWdmItluShelf.setStatus("current")
_AluWdmPSS32SwitchUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS32SwitchUniversalShelf = _AluWdmPSS32SwitchUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 25)
)
if mibBuilder.loadTexts:
    aluWdmPSS32SwitchUniversalShelf.setStatus("current")
_AluWdmPSS32Switch1P2TUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS32Switch1P2TUniversalShelf = _AluWdmPSS32Switch1P2TUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 26)
)
if mibBuilder.loadTexts:
    aluWdmPSS32Switch1P2TUniversalShelf.setStatus("current")
_AluWdmPsc1x6Shelf_ObjectIdentity = ObjectIdentity
aluWdmPsc1x6Shelf = _AluWdmPsc1x6Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 27)
)
if mibBuilder.loadTexts:
    aluWdmPsc1x6Shelf.setStatus("current")
_AluWdmPSS8UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS8UniversalShelf = _AluWdmPSS8UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 28)
)
if mibBuilder.loadTexts:
    aluWdmPSS8UniversalShelf.setStatus("current")
_AluWdmPSS16IIUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS16IIUniversalShelf = _AluWdmPSS16IIUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 29)
)
if mibBuilder.loadTexts:
    aluWdmPSS16IIUniversalShelf.setStatus("current")
_AluWdmPSS48UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS48UniversalShelf = _AluWdmPSS48UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 30)
)
if mibBuilder.loadTexts:
    aluWdmPSS48UniversalShelf.setStatus("current")
_AluWdmPSS96UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS96UniversalShelf = _AluWdmPSS96UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 31)
)
if mibBuilder.loadTexts:
    aluWdmPSS96UniversalShelf.setStatus("current")
_AluWdmMsh8fsmShelf_ObjectIdentity = ObjectIdentity
aluWdmMsh8fsmShelf = _AluWdmMsh8fsmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 32)
)
if mibBuilder.loadTexts:
    aluWdmMsh8fsmShelf.setStatus("current")
_AluWdmVwmCwUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmVwmCwUniversalShelf = _AluWdmVwmCwUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 33)
)
if mibBuilder.loadTexts:
    aluWdmVwmCwUniversalShelf.setStatus("current")
_AluWdmVwmDwUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmVwmDwUniversalShelf = _AluWdmVwmDwUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 34)
)
if mibBuilder.loadTexts:
    aluWdmVwmDwUniversalShelf.setStatus("current")
_TropicCardReg_ObjectIdentity = ObjectIdentity
tropicCardReg = _TropicCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5)
)
if mibBuilder.loadTexts:
    tropicCardReg.setStatus("current")
_TropicMiscCardReg_ObjectIdentity = ObjectIdentity
tropicMiscCardReg = _TropicMiscCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tropicMiscCardReg.setStatus("current")
_TropicEmptyCard_ObjectIdentity = ObjectIdentity
tropicEmptyCard = _TropicEmptyCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tropicEmptyCard.setStatus("current")
_TropicUnknownCard_ObjectIdentity = ObjectIdentity
tropicUnknownCard = _TropicUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    tropicUnknownCard.setStatus("current")
_TropicInvalidCard_ObjectIdentity = ObjectIdentity
tropicInvalidCard = _TropicInvalidCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    tropicInvalidCard.setStatus("current")
_TropicReservedCard_ObjectIdentity = ObjectIdentity
tropicReservedCard = _TropicReservedCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    tropicReservedCard.setStatus("current")
_TropicHalfHeightCarrierCard_ObjectIdentity = ObjectIdentity
tropicHalfHeightCarrierCard = _TropicHalfHeightCarrierCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    tropicHalfHeightCarrierCard.setStatus("current")
_AluWdmVirtualCard_ObjectIdentity = ObjectIdentity
aluWdmVirtualCard = _AluWdmVirtualCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    aluWdmVirtualCard.setStatus("current")
_AluWdmGmreCard_ObjectIdentity = ObjectIdentity
aluWdmGmreCard = _AluWdmGmreCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    aluWdmGmreCard.setStatus("current")
_AluWdmMsh8fsmCard_ObjectIdentity = ObjectIdentity
aluWdmMsh8fsmCard = _AluWdmMsh8fsmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    aluWdmMsh8fsmCard.setStatus("current")
_TropicControlCardReg_ObjectIdentity = ObjectIdentity
tropicControlCardReg = _TropicControlCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tropicControlCardReg.setStatus("current")
_TropicMasterControlCard_ObjectIdentity = ObjectIdentity
tropicMasterControlCard = _TropicMasterControlCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    tropicMasterControlCard.setStatus("current")
_AluWdmEquipmentControllerCard_ObjectIdentity = ObjectIdentity
aluWdmEquipmentControllerCard = _AluWdmEquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    aluWdmEquipmentControllerCard.setStatus("current")
_AluWdmFirstLevelControllerCard_ObjectIdentity = ObjectIdentity
aluWdmFirstLevelControllerCard = _AluWdmFirstLevelControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    aluWdmFirstLevelControllerCard.setStatus("current")
_AluWdmMatrix3T8Card_ObjectIdentity = ObjectIdentity
aluWdmMatrix3T8Card = _AluWdmMatrix3T8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    aluWdmMatrix3T8Card.setStatus("current")
_AluWdmMatrix1T9Card_ObjectIdentity = ObjectIdentity
aluWdmMatrix1T9Card = _AluWdmMatrix1T9Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    aluWdmMatrix1T9Card.setStatus("current")
_AluWdmPSS4EquipmentControllerCard_ObjectIdentity = ObjectIdentity
aluWdmPSS4EquipmentControllerCard = _AluWdmPSS4EquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    aluWdmPSS4EquipmentControllerCard.setStatus("current")
_AluWdmMatrix0CompactCard_ObjectIdentity = ObjectIdentity
aluWdmMatrix0CompactCard = _AluWdmMatrix0CompactCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 9)
)
if mibBuilder.loadTexts:
    aluWdmMatrix0CompactCard.setStatus("current")
_AluWdmUniversalMatrixFirstLevelControllerCard_ObjectIdentity = ObjectIdentity
aluWdmUniversalMatrixFirstLevelControllerCard = _AluWdmUniversalMatrixFirstLevelControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 10)
)
if mibBuilder.loadTexts:
    aluWdmUniversalMatrixFirstLevelControllerCard.setStatus("current")
_AluWdmEndOfShelfMiddleCard_ObjectIdentity = ObjectIdentity
aluWdmEndOfShelfMiddleCard = _AluWdmEndOfShelfMiddleCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 12)
)
if mibBuilder.loadTexts:
    aluWdmEndOfShelfMiddleCard.setStatus("current")
_AluWdmUniversalMatrixFirstLevelController1p2TCard_ObjectIdentity = ObjectIdentity
aluWdmUniversalMatrixFirstLevelController1p2TCard = _AluWdmUniversalMatrixFirstLevelController1p2TCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 14)
)
if mibBuilder.loadTexts:
    aluWdmUniversalMatrixFirstLevelController1p2TCard.setStatus("current")
_AluWdmPSS8EquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmPSS8EquipmentController2Card = _AluWdmPSS8EquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 15)
)
if mibBuilder.loadTexts:
    aluWdmPSS8EquipmentController2Card.setStatus("current")
_AluWdmPSS16IIEquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmPSS16IIEquipmentController2Card = _AluWdmPSS16IIEquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 16)
)
if mibBuilder.loadTexts:
    aluWdmPSS16IIEquipmentController2Card.setStatus("current")
_AluWdmPSS32EquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmPSS32EquipmentController2Card = _AluWdmPSS32EquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 17)
)
if mibBuilder.loadTexts:
    aluWdmPSS32EquipmentController2Card.setStatus("current")
_AluWdmClockControllerCard96Card_ObjectIdentity = ObjectIdentity
aluWdmClockControllerCard96Card = _AluWdmClockControllerCard96Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 18)
)
if mibBuilder.loadTexts:
    aluWdmClockControllerCard96Card.setStatus("current")
_AluWdmVwmCwEquipmentControllerCard_ObjectIdentity = ObjectIdentity
aluWdmVwmCwEquipmentControllerCard = _AluWdmVwmCwEquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 19)
)
if mibBuilder.loadTexts:
    aluWdmVwmCwEquipmentControllerCard.setStatus("current")
_AluWdmVwmDwEquipmentControllerCard_ObjectIdentity = ObjectIdentity
aluWdmVwmDwEquipmentControllerCard = _AluWdmVwmDwEquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 20)
)
if mibBuilder.loadTexts:
    aluWdmVwmDwEquipmentControllerCard.setStatus("current")
_TropicOpticalSwitchCardReg_ObjectIdentity = ObjectIdentity
tropicOpticalSwitchCardReg = _TropicOpticalSwitchCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tropicOpticalSwitchCardReg.setStatus("current")
_TropicPhotonicProtectionSwitchCard_ObjectIdentity = ObjectIdentity
tropicPhotonicProtectionSwitchCard = _TropicPhotonicProtectionSwitchCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    tropicPhotonicProtectionSwitchCard.setStatus("current")
_AluWdmOpsaCard_ObjectIdentity = ObjectIdentity
aluWdmOpsaCard = _AluWdmOpsaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    aluWdmOpsaCard.setStatus("current")
_AluWdmOpsbCard_ObjectIdentity = ObjectIdentity
aluWdmOpsbCard = _AluWdmOpsbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    aluWdmOpsbCard.setStatus("current")
_AluWdmMcs8x16Card_ObjectIdentity = ObjectIdentity
aluWdmMcs8x16Card = _AluWdmMcs8x16Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    aluWdmMcs8x16Card.setStatus("current")
_AluWdmSwitchingCard_ObjectIdentity = ObjectIdentity
aluWdmSwitchingCard = _AluWdmSwitchingCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    aluWdmSwitchingCard.setStatus("current")
_AluWdm12p120Card_ObjectIdentity = ObjectIdentity
aluWdm12p120Card = _AluWdm12p120Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    aluWdm12p120Card.setStatus("current")
_AluWdm20p200Card_ObjectIdentity = ObjectIdentity
aluWdm20p200Card = _AluWdm20p200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    aluWdm20p200Card.setStatus("current")
_AluWdm1ud200Card_ObjectIdentity = ObjectIdentity
aluWdm1ud200Card = _AluWdm1ud200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    aluWdm1ud200Card.setStatus("current")
_TropicDWDMFilterCardReg_ObjectIdentity = ObjectIdentity
tropicDWDMFilterCardReg = _TropicDWDMFilterCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6)
)
if mibBuilder.loadTexts:
    tropicDWDMFilterCardReg.setStatus("current")
_AluWdmCwr8Card_ObjectIdentity = ObjectIdentity
aluWdmCwr8Card = _AluWdmCwr8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 9)
)
if mibBuilder.loadTexts:
    aluWdmCwr8Card.setStatus("current")
_AluWdmSfd44Card_ObjectIdentity = ObjectIdentity
aluWdmSfd44Card = _AluWdmSfd44Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 10)
)
if mibBuilder.loadTexts:
    aluWdmSfd44Card.setStatus("current")
_AluWdmSVACCard_ObjectIdentity = ObjectIdentity
aluWdmSVACCard = _AluWdmSVACCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 11)
)
if mibBuilder.loadTexts:
    aluWdmSVACCard.setStatus("current")
_AluWdmCwr8c88Card_ObjectIdentity = ObjectIdentity
aluWdmCwr8c88Card = _AluWdmCwr8c88Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 12)
)
if mibBuilder.loadTexts:
    aluWdmCwr8c88Card.setStatus("current")
_AluWdmSfd44bCard_ObjectIdentity = ObjectIdentity
aluWdmSfd44bCard = _AluWdmSfd44bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 13)
)
if mibBuilder.loadTexts:
    aluWdmSfd44bCard.setStatus("current")
_AluWdmItlbCard_ObjectIdentity = ObjectIdentity
aluWdmItlbCard = _AluWdmItlbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 14)
)
if mibBuilder.loadTexts:
    aluWdmItlbCard.setStatus("current")
_AluWdmSfd40Card_ObjectIdentity = ObjectIdentity
aluWdmSfd40Card = _AluWdmSfd40Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 19)
)
if mibBuilder.loadTexts:
    aluWdmSfd40Card.setStatus("current")
_AluWdmSfd40bCard_ObjectIdentity = ObjectIdentity
aluWdmSfd40bCard = _AluWdmSfd40bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 20)
)
if mibBuilder.loadTexts:
    aluWdmSfd40bCard.setStatus("current")
_AluWdmWr2c88Card_ObjectIdentity = ObjectIdentity
aluWdmWr2c88Card = _AluWdmWr2c88Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 21)
)
if mibBuilder.loadTexts:
    aluWdmWr2c88Card.setStatus("current")
_AluWdmMVACCard_ObjectIdentity = ObjectIdentity
aluWdmMVACCard = _AluWdmMVACCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 22)
)
if mibBuilder.loadTexts:
    aluWdmMVACCard.setStatus("current")
_AluWdmItluCard_ObjectIdentity = ObjectIdentity
aluWdmItluCard = _AluWdmItluCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 23)
)
if mibBuilder.loadTexts:
    aluWdmItluCard.setStatus("current")
_AluWdmWr8c88aCard_ObjectIdentity = ObjectIdentity
aluWdmWr8c88aCard = _AluWdmWr8c88aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 24)
)
if mibBuilder.loadTexts:
    aluWdmWr8c88aCard.setStatus("current")
_AluWdmMesh4Card_ObjectIdentity = ObjectIdentity
aluWdmMesh4Card = _AluWdmMesh4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 25)
)
if mibBuilder.loadTexts:
    aluWdmMesh4Card.setStatus("current")
_AluWdmMVAC8BCard_ObjectIdentity = ObjectIdentity
aluWdmMVAC8BCard = _AluWdmMVAC8BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 26)
)
if mibBuilder.loadTexts:
    aluWdmMVAC8BCard.setStatus("current")
_AluWdmWr8c88afCard_ObjectIdentity = ObjectIdentity
aluWdmWr8c88afCard = _AluWdmWr8c88afCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 27)
)
if mibBuilder.loadTexts:
    aluWdmWr8c88afCard.setStatus("current")
_AluWdmPsc1x6Card_ObjectIdentity = ObjectIdentity
aluWdmPsc1x6Card = _AluWdmPsc1x6Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 28)
)
if mibBuilder.loadTexts:
    aluWdmPsc1x6Card.setStatus("current")
_AluWdmWr20tfCard_ObjectIdentity = ObjectIdentity
aluWdmWr20tfCard = _AluWdmWr20tfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 29)
)
if mibBuilder.loadTexts:
    aluWdmWr20tfCard.setStatus("current")
_AluWdmWr20tfmCard_ObjectIdentity = ObjectIdentity
aluWdmWr20tfmCard = _AluWdmWr20tfmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 30)
)
if mibBuilder.loadTexts:
    aluWdmWr20tfmCard.setStatus("current")
_TropicAmplifierCardReg_ObjectIdentity = ObjectIdentity
tropicAmplifierCardReg = _TropicAmplifierCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7)
)
if mibBuilder.loadTexts:
    tropicAmplifierCardReg.setStatus("current")
_AluWdmAhphgCard_ObjectIdentity = ObjectIdentity
aluWdmAhphgCard = _AluWdmAhphgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 4)
)
if mibBuilder.loadTexts:
    aluWdmAhphgCard.setStatus("current")
_AluWdmAlphgCard_ObjectIdentity = ObjectIdentity
aluWdmAlphgCard = _AluWdmAlphgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 5)
)
if mibBuilder.loadTexts:
    aluWdmAlphgCard.setStatus("current")
_AluWdmAhplgCard_ObjectIdentity = ObjectIdentity
aluWdmAhplgCard = _AluWdmAhplgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 6)
)
if mibBuilder.loadTexts:
    aluWdmAhplgCard.setStatus("current")
_AluWdmAlpfgkCard_ObjectIdentity = ObjectIdentity
aluWdmAlpfgkCard = _AluWdmAlpfgkCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 7)
)
if mibBuilder.loadTexts:
    aluWdmAlpfgkCard.setStatus("current")
_AluWdmOscCard_ObjectIdentity = ObjectIdentity
aluWdmOscCard = _AluWdmOscCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 8)
)
if mibBuilder.loadTexts:
    aluWdmOscCard.setStatus("current")
_AluWdmA2325aCard_ObjectIdentity = ObjectIdentity
aluWdmA2325aCard = _AluWdmA2325aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 10)
)
if mibBuilder.loadTexts:
    aluWdmA2325aCard.setStatus("current")
_AluWdmAlpfgtCard_ObjectIdentity = ObjectIdentity
aluWdmAlpfgtCard = _AluWdmAlpfgtCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 11)
)
if mibBuilder.loadTexts:
    aluWdmAlpfgtCard.setStatus("current")
_AluWdmOsctCard_ObjectIdentity = ObjectIdentity
aluWdmOsctCard = _AluWdmOsctCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 12)
)
if mibBuilder.loadTexts:
    aluWdmOsctCard.setStatus("current")
_AluWdmWtocmCard_ObjectIdentity = ObjectIdentity
aluWdmWtocmCard = _AluWdmWtocmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 13)
)
if mibBuilder.loadTexts:
    aluWdmWtocmCard.setStatus("current")
_AluWdmAm2017bCard_ObjectIdentity = ObjectIdentity
aluWdmAm2017bCard = _AluWdmAm2017bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 14)
)
if mibBuilder.loadTexts:
    aluWdmAm2017bCard.setStatus("current")
_AluWdmAm2325bCard_ObjectIdentity = ObjectIdentity
aluWdmAm2325bCard = _AluWdmAm2325bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 15)
)
if mibBuilder.loadTexts:
    aluWdmAm2325bCard.setStatus("current")
_AluWdmRa2pCard_ObjectIdentity = ObjectIdentity
aluWdmRa2pCard = _AluWdmRa2pCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 16)
)
if mibBuilder.loadTexts:
    aluWdmRa2pCard.setStatus("current")
_AluWdmAm2318aCard_ObjectIdentity = ObjectIdentity
aluWdmAm2318aCard = _AluWdmAm2318aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 17)
)
if mibBuilder.loadTexts:
    aluWdmAm2318aCard.setStatus("current")
_AluWdmAm2125aCard_ObjectIdentity = ObjectIdentity
aluWdmAm2125aCard = _AluWdmAm2125aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 18)
)
if mibBuilder.loadTexts:
    aluWdmAm2125aCard.setStatus("current")
_AluWdmAm2125bCard_ObjectIdentity = ObjectIdentity
aluWdmAm2125bCard = _AluWdmAm2125bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 19)
)
if mibBuilder.loadTexts:
    aluWdmAm2125bCard.setStatus("current")
_AluWdmWtocmaCard_ObjectIdentity = ObjectIdentity
aluWdmWtocmaCard = _AluWdmWtocmaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 20)
)
if mibBuilder.loadTexts:
    aluWdmWtocmaCard.setStatus("current")
_AluWdmA2p2125Card_ObjectIdentity = ObjectIdentity
aluWdmA2p2125Card = _AluWdmA2p2125Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 21)
)
if mibBuilder.loadTexts:
    aluWdmA2p2125Card.setStatus("current")
_AluWdmAm2625aCard_ObjectIdentity = ObjectIdentity
aluWdmAm2625aCard = _AluWdmAm2625aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 22)
)
if mibBuilder.loadTexts:
    aluWdmAm2625aCard.setStatus("current")
_AluWdmAm2032aCard_ObjectIdentity = ObjectIdentity
aluWdmAm2032aCard = _AluWdmAm2032aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 23)
)
if mibBuilder.loadTexts:
    aluWdmAm2032aCard.setStatus("current")
_AluWdmAa2donwCard_ObjectIdentity = ObjectIdentity
aluWdmAa2donwCard = _AluWdmAa2donwCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 24)
)
if mibBuilder.loadTexts:
    aluWdmAa2donwCard.setStatus("current")
_AluWdmWtocmfCard_ObjectIdentity = ObjectIdentity
aluWdmWtocmfCard = _AluWdmWtocmfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 25)
)
if mibBuilder.loadTexts:
    aluWdmWtocmfCard.setStatus("current")
_AluWdmAswgCard_ObjectIdentity = ObjectIdentity
aluWdmAswgCard = _AluWdmAswgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 26)
)
if mibBuilder.loadTexts:
    aluWdmAswgCard.setStatus("current")
_AluWdmA4pswgCard_ObjectIdentity = ObjectIdentity
aluWdmA4pswgCard = _AluWdmA4pswgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 27)
)
if mibBuilder.loadTexts:
    aluWdmA4pswgCard.setStatus("current")
_AluWdmOtdrCard_ObjectIdentity = ObjectIdentity
aluWdmOtdrCard = _AluWdmOtdrCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 28)
)
if mibBuilder.loadTexts:
    aluWdmOtdrCard.setStatus("current")
_AluWdmAar8aCard_ObjectIdentity = ObjectIdentity
aluWdmAar8aCard = _AluWdmAar8aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 29)
)
if mibBuilder.loadTexts:
    aluWdmAar8aCard.setStatus("current")
_TropicDispersionCompCardReg_ObjectIdentity = ObjectIdentity
tropicDispersionCompCardReg = _TropicDispersionCompCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 8)
)
if mibBuilder.loadTexts:
    tropicDispersionCompCardReg.setStatus("current")
_AluWdmDcmCard_ObjectIdentity = ObjectIdentity
aluWdmDcmCard = _AluWdmDcmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 8, 3)
)
if mibBuilder.loadTexts:
    aluWdmDcmCard.setStatus("current")
_AluWdmOpticalTransponderCardReg_ObjectIdentity = ObjectIdentity
aluWdmOpticalTransponderCardReg = _AluWdmOpticalTransponderCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11)
)
if mibBuilder.loadTexts:
    aluWdmOpticalTransponderCardReg.setStatus("current")
_AluWdm11star1Card_ObjectIdentity = ObjectIdentity
aluWdm11star1Card = _AluWdm11star1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 1)
)
if mibBuilder.loadTexts:
    aluWdm11star1Card.setStatus("current")
_AluWdm11stge12Card_ObjectIdentity = ObjectIdentity
aluWdm11stge12Card = _AluWdm11stge12Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 2)
)
if mibBuilder.loadTexts:
    aluWdm11stge12Card.setStatus("current")
_AluWdm11dpge12Card_ObjectIdentity = ObjectIdentity
aluWdm11dpge12Card = _AluWdm11dpge12Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 3)
)
if mibBuilder.loadTexts:
    aluWdm11dpge12Card.setStatus("current")
_AluWdm11stmm10Card_ObjectIdentity = ObjectIdentity
aluWdm11stmm10Card = _AluWdm11stmm10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 4)
)
if mibBuilder.loadTexts:
    aluWdm11stmm10Card.setStatus("current")
_AluWdm4dpa4Card_ObjectIdentity = ObjectIdentity
aluWdm4dpa4Card = _AluWdm4dpa4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 5)
)
if mibBuilder.loadTexts:
    aluWdm4dpa4Card.setStatus("current")
_AluWdm43stx4Card_ObjectIdentity = ObjectIdentity
aluWdm43stx4Card = _AluWdm43stx4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 6)
)
if mibBuilder.loadTexts:
    aluWdm43stx4Card.setStatus("current")
_AluWdm4dpa2Card_ObjectIdentity = ObjectIdentity
aluWdm4dpa2Card = _AluWdm4dpa2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 7)
)
if mibBuilder.loadTexts:
    aluWdm4dpa2Card.setStatus("current")
_AluWdm43sta1pCard_ObjectIdentity = ObjectIdentity
aluWdm43sta1pCard = _AluWdm43sta1pCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 8)
)
if mibBuilder.loadTexts:
    aluWdm43sta1pCard.setStatus("current")
_AluWdm43stx4pCard_ObjectIdentity = ObjectIdentity
aluWdm43stx4pCard = _AluWdm43stx4pCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 9)
)
if mibBuilder.loadTexts:
    aluWdm43stx4pCard.setStatus("current")
_AluWdm11qpa4Card_ObjectIdentity = ObjectIdentity
aluWdm11qpa4Card = _AluWdm11qpa4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 12)
)
if mibBuilder.loadTexts:
    aluWdm11qpa4Card.setStatus("current")
_AluWdm112scx10Card_ObjectIdentity = ObjectIdentity
aluWdm112scx10Card = _AluWdm112scx10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 13)
)
if mibBuilder.loadTexts:
    aluWdm112scx10Card.setStatus("current")
_AluWdm112sca1Card_ObjectIdentity = ObjectIdentity
aluWdm112sca1Card = _AluWdm112sca1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 14)
)
if mibBuilder.loadTexts:
    aluWdm112sca1Card.setStatus("current")
_AluWdm1dpp21Card_ObjectIdentity = ObjectIdentity
aluWdm1dpp21Card = _AluWdm1dpp21Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 15)
)
if mibBuilder.loadTexts:
    aluWdm1dpp21Card.setStatus("current")
_AluWdm43scx4Card_ObjectIdentity = ObjectIdentity
aluWdm43scx4Card = _AluWdm43scx4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 16)
)
if mibBuilder.loadTexts:
    aluWdm43scx4Card.setStatus("current")
_AluWdm11dpe12eCard_ObjectIdentity = ObjectIdentity
aluWdm11dpe12eCard = _AluWdm11dpe12eCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 17)
)
if mibBuilder.loadTexts:
    aluWdm11dpe12eCard.setStatus("current")
_AluWdm112sx10lCard_ObjectIdentity = ObjectIdentity
aluWdm112sx10lCard = _AluWdm112sx10lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 18)
)
if mibBuilder.loadTexts:
    aluWdm112sx10lCard.setStatus("current")
_AluWdm112sa1lCard_ObjectIdentity = ObjectIdentity
aluWdm112sa1lCard = _AluWdm112sa1lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 19)
)
if mibBuilder.loadTexts:
    aluWdm112sa1lCard.setStatus("current")
_AluWdm11dpm12Card_ObjectIdentity = ObjectIdentity
aluWdm11dpm12Card = _AluWdm11dpm12Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 20)
)
if mibBuilder.loadTexts:
    aluWdm11dpm12Card.setStatus("current")
_AluWdm43sca1Card_ObjectIdentity = ObjectIdentity
aluWdm43sca1Card = _AluWdm43sca1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 21)
)
if mibBuilder.loadTexts:
    aluWdm43sca1Card.setStatus("current")
_AluWdm43scx4lCard_ObjectIdentity = ObjectIdentity
aluWdm43scx4lCard = _AluWdm43scx4lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 22)
)
if mibBuilder.loadTexts:
    aluWdm43scx4lCard.setStatus("current")
_AluWdm112snx10Card_ObjectIdentity = ObjectIdentity
aluWdm112snx10Card = _AluWdm112snx10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 23)
)
if mibBuilder.loadTexts:
    aluWdm112snx10Card.setStatus("current")
_AluWdm112sna1Card_ObjectIdentity = ObjectIdentity
aluWdm112sna1Card = _AluWdm112sna1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 24)
)
if mibBuilder.loadTexts:
    aluWdm112sna1Card.setStatus("current")
_AluWdm1dpp24mCard_ObjectIdentity = ObjectIdentity
aluWdm1dpp24mCard = _AluWdm1dpp24mCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 26)
)
if mibBuilder.loadTexts:
    aluWdm1dpp24mCard.setStatus("current")
_AluWdmul43scupCard_ObjectIdentity = ObjectIdentity
aluWdmul43scupCard = _AluWdmul43scupCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 27)
)
if mibBuilder.loadTexts:
    aluWdmul43scupCard.setStatus("current")
_AluWdmul11qcupCard_ObjectIdentity = ObjectIdentity
aluWdmul11qcupCard = _AluWdmul11qcupCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 28)
)
if mibBuilder.loadTexts:
    aluWdmul11qcupCard.setStatus("current")
_AluWdm11qpen4Card_ObjectIdentity = ObjectIdentity
aluWdm11qpen4Card = _AluWdm11qpen4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 29)
)
if mibBuilder.loadTexts:
    aluWdm11qpen4Card.setStatus("current")
_AluWdm43scx4eCard_ObjectIdentity = ObjectIdentity
aluWdm43scx4eCard = _AluWdm43scx4eCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 30)
)
if mibBuilder.loadTexts:
    aluWdm43scx4eCard.setStatus("current")
_AluWdm43scge1Card_ObjectIdentity = ObjectIdentity
aluWdm43scge1Card = _AluWdm43scge1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 31)
)
if mibBuilder.loadTexts:
    aluWdm43scge1Card.setStatus("current")
_AluWdm11qpe24Card_ObjectIdentity = ObjectIdentity
aluWdm11qpe24Card = _AluWdm11qpe24Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 32)
)
if mibBuilder.loadTexts:
    aluWdm11qpe24Card.setStatus("current")
_AluWdm11star1aCard_ObjectIdentity = ObjectIdentity
aluWdm11star1aCard = _AluWdm11star1aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 33)
)
if mibBuilder.loadTexts:
    aluWdm11star1aCard.setStatus("current")
_AluWdmcl10an10gCard_ObjectIdentity = ObjectIdentity
aluWdmcl10an10gCard = _AluWdmcl10an10gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 34)
)
if mibBuilder.loadTexts:
    aluWdmcl10an10gCard.setStatus("current")
_AluWdmcl24anmCard_ObjectIdentity = ObjectIdentity
aluWdmcl24anmCard = _AluWdmcl24anmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 35)
)
if mibBuilder.loadTexts:
    aluWdmcl24anmCard.setStatus("current")
_AluWdm11dpe12aCard_ObjectIdentity = ObjectIdentity
aluWdm11dpe12aCard = _AluWdm11dpe12aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 36)
)
if mibBuilder.loadTexts:
    aluWdm11dpe12aCard.setStatus("current")
_AluWdmul130scupCard_ObjectIdentity = ObjectIdentity
aluWdmul130scupCard = _AluWdmul130scupCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 37)
)
if mibBuilder.loadTexts:
    aluWdmul130scupCard.setStatus("current")
_AluWdm130scx10Card_ObjectIdentity = ObjectIdentity
aluWdm130scx10Card = _AluWdm130scx10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 38)
)
if mibBuilder.loadTexts:
    aluWdm130scx10Card.setStatus("current")
_AluWdm4qpa8Card_ObjectIdentity = ObjectIdentity
aluWdm4qpa8Card = _AluWdm4qpa8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 39)
)
if mibBuilder.loadTexts:
    aluWdm4qpa8Card.setStatus("current")
_AluWdmOt112pdm11Card_ObjectIdentity = ObjectIdentity
aluWdmOt112pdm11Card = _AluWdmOt112pdm11Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 40)
)
if mibBuilder.loadTexts:
    aluWdmOt112pdm11Card.setStatus("current")
_AluWdmPtpctlCard_ObjectIdentity = ObjectIdentity
aluWdmPtpctlCard = _AluWdmPtpctlCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 41)
)
if mibBuilder.loadTexts:
    aluWdmPtpctlCard.setStatus("current")
_AluWdmPtpioCard_ObjectIdentity = ObjectIdentity
aluWdmPtpioCard = _AluWdmPtpioCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 42)
)
if mibBuilder.loadTexts:
    aluWdmPtpioCard.setStatus("current")
_AluWdmIo24et1gbCard_ObjectIdentity = ObjectIdentity
aluWdmIo24et1gbCard = _AluWdmIo24et1gbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 43)
)
if mibBuilder.loadTexts:
    aluWdmIo24et1gbCard.setStatus("current")
_AluWdmIo4an10gCard_ObjectIdentity = ObjectIdentity
aluWdmIo4an10gCard = _AluWdmIo4an10gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 44)
)
if mibBuilder.loadTexts:
    aluWdmIo4an10gCard.setStatus("current")
_AluWdmIo8et1gbCard_ObjectIdentity = ObjectIdentity
aluWdmIo8et1gbCard = _AluWdmIo8et1gbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 45)
)
if mibBuilder.loadTexts:
    aluWdmIo8et1gbCard.setStatus("current")
_AluWdmIo10et10gCard_ObjectIdentity = ObjectIdentity
aluWdmIo10et10gCard = _AluWdmIo10et10gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 46)
)
if mibBuilder.loadTexts:
    aluWdmIo10et10gCard.setStatus("current")
_AluWdmUl11qcupcCard_ObjectIdentity = ObjectIdentity
aluWdmUl11qcupcCard = _AluWdmUl11qcupcCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 47)
)
if mibBuilder.loadTexts:
    aluWdmUl11qcupcCard.setStatus("current")
_AluWdmOt520scx4Card_ObjectIdentity = ObjectIdentity
aluWdmOt520scx4Card = _AluWdmOt520scx4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 48)
)
if mibBuilder.loadTexts:
    aluWdmOt520scx4Card.setStatus("current")
_AluWdm11ope8Card_ObjectIdentity = ObjectIdentity
aluWdm11ope8Card = _AluWdm11ope8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 49)
)
if mibBuilder.loadTexts:
    aluWdm11ope8Card.setStatus("current")
_AluWdm11qce12xCard_ObjectIdentity = ObjectIdentity
aluWdm11qce12xCard = _AluWdm11qce12xCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 50)
)
if mibBuilder.loadTexts:
    aluWdm11qce12xCard.setStatus("current")
_AluWdmOt260scx2Card_ObjectIdentity = ObjectIdentity
aluWdmOt260scx2Card = _AluWdmOt260scx2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 51)
)
if mibBuilder.loadTexts:
    aluWdmOt260scx2Card.setStatus("current")
_AluWdmOt130snx10Card_ObjectIdentity = ObjectIdentity
aluWdmOt130snx10Card = _AluWdmOt130snx10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 52)
)
if mibBuilder.loadTexts:
    aluWdmOt130snx10Card.setStatus("current")
_AluWdmIo24anmbCard_ObjectIdentity = ObjectIdentity
aluWdmIo24anmbCard = _AluWdmIo24anmbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 53)
)
if mibBuilder.loadTexts:
    aluWdmIo24anmbCard.setStatus("current")
_AluWdmOt11dpm8Card_ObjectIdentity = ObjectIdentity
aluWdmOt11dpm8Card = _AluWdmOt11dpm8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 54)
)
if mibBuilder.loadTexts:
    aluWdmOt11dpm8Card.setStatus("current")
_AluWdmOt11dpm4mCard_ObjectIdentity = ObjectIdentity
aluWdmOt11dpm4mCard = _AluWdmOt11dpm4mCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 55)
)
if mibBuilder.loadTexts:
    aluWdmOt11dpm4mCard.setStatus("current")
_AluWdmOt11dpm4eCard_ObjectIdentity = ObjectIdentity
aluWdmOt11dpm4eCard = _AluWdmOt11dpm4eCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 56)
)
if mibBuilder.loadTexts:
    aluWdmOt11dpm4eCard.setStatus("current")
_AluWdmUl130scupbCard_ObjectIdentity = ObjectIdentity
aluWdmUl130scupbCard = _AluWdmUl130scupbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 57)
)
if mibBuilder.loadTexts:
    aluWdmUl130scupbCard.setStatus("current")
_AluWdmOt112sdx11Card_ObjectIdentity = ObjectIdentity
aluWdmOt112sdx11Card = _AluWdmOt112sdx11Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 58)
)
if mibBuilder.loadTexts:
    aluWdmOt112sdx11Card.setStatus("current")
_AluWdmOt130sca1Card_ObjectIdentity = ObjectIdentity
aluWdmOt130sca1Card = _AluWdmOt130sca1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 59)
)
if mibBuilder.loadTexts:
    aluWdmOt130sca1Card.setStatus("current")
_AluWdmIo10an10gbCard_ObjectIdentity = ObjectIdentity
aluWdmIo10an10gbCard = _AluWdmIo10an10gbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 60)
)
if mibBuilder.loadTexts:
    aluWdmIo10an10gbCard.setStatus("current")
_AluWdmIo10et10gbCard_ObjectIdentity = ObjectIdentity
aluWdmIo10et10gbCard = _AluWdmIo10et10gbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 61)
)
if mibBuilder.loadTexts:
    aluWdmIo10et10gbCard.setStatus("current")
_AluWdmIo4an100gCard_ObjectIdentity = ObjectIdentity
aluWdmIo4an100gCard = _AluWdmIo4an100gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 62)
)
if mibBuilder.loadTexts:
    aluWdmIo4an100gCard.setStatus("current")
_AluWdmIo30an10gCard_ObjectIdentity = ObjectIdentity
aluWdmIo30an10gCard = _AluWdmIo30an10gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 63)
)
if mibBuilder.loadTexts:
    aluWdmIo30an10gCard.setStatus("current")
_AluWdmIo30an300Card_ObjectIdentity = ObjectIdentity
aluWdmIo30an300Card = _AluWdmIo30an300Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 64)
)
if mibBuilder.loadTexts:
    aluWdmIo30an300Card.setStatus("current")
_AluWdmIo4an400Card_ObjectIdentity = ObjectIdentity
aluWdmIo4an400Card = _AluWdmIo4an400Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 65)
)
if mibBuilder.loadTexts:
    aluWdmIo4an400Card.setStatus("current")
_AluWdmStaticFilterCardReg_ObjectIdentity = ObjectIdentity
aluWdmStaticFilterCardReg = _AluWdmStaticFilterCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12)
)
if mibBuilder.loadTexts:
    aluWdmStaticFilterCardReg.setStatus("current")
_AluWdmSFD5ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD5ACard = _AluWdmSFD5ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 1)
)
if mibBuilder.loadTexts:
    aluWdmSFD5ACard.setStatus("current")
_AluWdmSFD5BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5BCard = _AluWdmSFD5BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 2)
)
if mibBuilder.loadTexts:
    aluWdmSFD5BCard.setStatus("current")
_AluWdmSFD5CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5CCard = _AluWdmSFD5CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 3)
)
if mibBuilder.loadTexts:
    aluWdmSFD5CCard.setStatus("current")
_AluWdmSFD5DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5DCard = _AluWdmSFD5DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 4)
)
if mibBuilder.loadTexts:
    aluWdmSFD5DCard.setStatus("current")
_AluWdmSFD5ECard_ObjectIdentity = ObjectIdentity
aluWdmSFD5ECard = _AluWdmSFD5ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 5)
)
if mibBuilder.loadTexts:
    aluWdmSFD5ECard.setStatus("current")
_AluWdmSFD5FCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5FCard = _AluWdmSFD5FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 6)
)
if mibBuilder.loadTexts:
    aluWdmSFD5FCard.setStatus("current")
_AluWdmSFD5GCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5GCard = _AluWdmSFD5GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 7)
)
if mibBuilder.loadTexts:
    aluWdmSFD5GCard.setStatus("current")
_AluWdmSFD5HCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5HCard = _AluWdmSFD5HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 8)
)
if mibBuilder.loadTexts:
    aluWdmSFD5HCard.setStatus("current")
_AluWdmSFD10ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD10ACard = _AluWdmSFD10ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 9)
)
if mibBuilder.loadTexts:
    aluWdmSFD10ACard.setStatus("current")
_AluWdmSFD10BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD10BCard = _AluWdmSFD10BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 10)
)
if mibBuilder.loadTexts:
    aluWdmSFD10BCard.setStatus("current")
_AluWdmSFD10CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD10CCard = _AluWdmSFD10CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 11)
)
if mibBuilder.loadTexts:
    aluWdmSFD10CCard.setStatus("current")
_AluWdmSFD10DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD10DCard = _AluWdmSFD10DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 12)
)
if mibBuilder.loadTexts:
    aluWdmSFD10DCard.setStatus("current")
_AluWdmSFC2ACard_ObjectIdentity = ObjectIdentity
aluWdmSFC2ACard = _AluWdmSFC2ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 13)
)
if mibBuilder.loadTexts:
    aluWdmSFC2ACard.setStatus("current")
_AluWdmSFC2BCard_ObjectIdentity = ObjectIdentity
aluWdmSFC2BCard = _AluWdmSFC2BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 14)
)
if mibBuilder.loadTexts:
    aluWdmSFC2BCard.setStatus("current")
_AluWdmSFC2CCard_ObjectIdentity = ObjectIdentity
aluWdmSFC2CCard = _AluWdmSFC2CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 15)
)
if mibBuilder.loadTexts:
    aluWdmSFC2CCard.setStatus("current")
_AluWdmSFC2DCard_ObjectIdentity = ObjectIdentity
aluWdmSFC2DCard = _AluWdmSFC2DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 16)
)
if mibBuilder.loadTexts:
    aluWdmSFC2DCard.setStatus("current")
_AluWdmSFC4ACard_ObjectIdentity = ObjectIdentity
aluWdmSFC4ACard = _AluWdmSFC4ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 17)
)
if mibBuilder.loadTexts:
    aluWdmSFC4ACard.setStatus("current")
_AluWdmSFC4BCard_ObjectIdentity = ObjectIdentity
aluWdmSFC4BCard = _AluWdmSFC4BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 18)
)
if mibBuilder.loadTexts:
    aluWdmSFC4BCard.setStatus("current")
_AluWdmSFC8Card_ObjectIdentity = ObjectIdentity
aluWdmSFC8Card = _AluWdmSFC8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 19)
)
if mibBuilder.loadTexts:
    aluWdmSFC8Card.setStatus("current")
_AluWdmSFC1ACard_ObjectIdentity = ObjectIdentity
aluWdmSFC1ACard = _AluWdmSFC1ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 20)
)
if mibBuilder.loadTexts:
    aluWdmSFC1ACard.setStatus("current")
_AluWdmSFC1BCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1BCard = _AluWdmSFC1BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 21)
)
if mibBuilder.loadTexts:
    aluWdmSFC1BCard.setStatus("current")
_AluWdmSFC1CCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1CCard = _AluWdmSFC1CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 22)
)
if mibBuilder.loadTexts:
    aluWdmSFC1CCard.setStatus("current")
_AluWdmSFC1DCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1DCard = _AluWdmSFC1DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 23)
)
if mibBuilder.loadTexts:
    aluWdmSFC1DCard.setStatus("current")
_AluWdmSFC1ECard_ObjectIdentity = ObjectIdentity
aluWdmSFC1ECard = _AluWdmSFC1ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 24)
)
if mibBuilder.loadTexts:
    aluWdmSFC1ECard.setStatus("current")
_AluWdmSFC1FCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1FCard = _AluWdmSFC1FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 25)
)
if mibBuilder.loadTexts:
    aluWdmSFC1FCard.setStatus("current")
_AluWdmSFC1GCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1GCard = _AluWdmSFC1GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 26)
)
if mibBuilder.loadTexts:
    aluWdmSFC1GCard.setStatus("current")
_AluWdmSFC1HCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1HCard = _AluWdmSFC1HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 27)
)
if mibBuilder.loadTexts:
    aluWdmSFC1HCard.setStatus("current")
_AluWdmSFD8ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD8ACard = _AluWdmSFD8ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 28)
)
if mibBuilder.loadTexts:
    aluWdmSFD8ACard.setStatus("current")
_AluWdmSFD8BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD8BCard = _AluWdmSFD8BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 29)
)
if mibBuilder.loadTexts:
    aluWdmSFD8BCard.setStatus("current")
_AluWdmSFD8CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD8CCard = _AluWdmSFD8CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 30)
)
if mibBuilder.loadTexts:
    aluWdmSFD8CCard.setStatus("current")
_AluWdmSFD8DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD8DCard = _AluWdmSFD8DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 31)
)
if mibBuilder.loadTexts:
    aluWdmSFD8DCard.setStatus("current")
_AluWdmSFD4ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD4ACard = _AluWdmSFD4ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 32)
)
if mibBuilder.loadTexts:
    aluWdmSFD4ACard.setStatus("current")
_AluWdmSFD4BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4BCard = _AluWdmSFD4BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 33)
)
if mibBuilder.loadTexts:
    aluWdmSFD4BCard.setStatus("current")
_AluWdmSFD4CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4CCard = _AluWdmSFD4CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 34)
)
if mibBuilder.loadTexts:
    aluWdmSFD4CCard.setStatus("current")
_AluWdmSFD4DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4DCard = _AluWdmSFD4DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 35)
)
if mibBuilder.loadTexts:
    aluWdmSFD4DCard.setStatus("current")
_AluWdmSFD4ECard_ObjectIdentity = ObjectIdentity
aluWdmSFD4ECard = _AluWdmSFD4ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 36)
)
if mibBuilder.loadTexts:
    aluWdmSFD4ECard.setStatus("current")
_AluWdmSFD4FCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4FCard = _AluWdmSFD4FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 37)
)
if mibBuilder.loadTexts:
    aluWdmSFD4FCard.setStatus("current")
_AluWdmSFD4GCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4GCard = _AluWdmSFD4GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 38)
)
if mibBuilder.loadTexts:
    aluWdmSFD4GCard.setStatus("current")
_AluWdmSFD4HCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4HCard = _AluWdmSFD4HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 39)
)
if mibBuilder.loadTexts:
    aluWdmSFD4HCard.setStatus("current")
_AluWdmSFD2ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD2ACard = _AluWdmSFD2ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 40)
)
if mibBuilder.loadTexts:
    aluWdmSFD2ACard.setStatus("current")
_AluWdmSFD2BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2BCard = _AluWdmSFD2BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 41)
)
if mibBuilder.loadTexts:
    aluWdmSFD2BCard.setStatus("current")
_AluWdmSFD2CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2CCard = _AluWdmSFD2CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 42)
)
if mibBuilder.loadTexts:
    aluWdmSFD2CCard.setStatus("current")
_AluWdmSFD2DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2DCard = _AluWdmSFD2DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 43)
)
if mibBuilder.loadTexts:
    aluWdmSFD2DCard.setStatus("current")
_AluWdmSFD2ECard_ObjectIdentity = ObjectIdentity
aluWdmSFD2ECard = _AluWdmSFD2ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 44)
)
if mibBuilder.loadTexts:
    aluWdmSFD2ECard.setStatus("current")
_AluWdmSFD2FCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2FCard = _AluWdmSFD2FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 45)
)
if mibBuilder.loadTexts:
    aluWdmSFD2FCard.setStatus("current")
_AluWdmSFD2GCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2GCard = _AluWdmSFD2GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 46)
)
if mibBuilder.loadTexts:
    aluWdmSFD2GCard.setStatus("current")
_AluWdmSFD2HCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2HCard = _AluWdmSFD2HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 47)
)
if mibBuilder.loadTexts:
    aluWdmSFD2HCard.setStatus("current")
_AluWdmSFD2ICard_ObjectIdentity = ObjectIdentity
aluWdmSFD2ICard = _AluWdmSFD2ICard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 48)
)
if mibBuilder.loadTexts:
    aluWdmSFD2ICard.setStatus("current")
_AluWdmSFD2LCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2LCard = _AluWdmSFD2LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 49)
)
if mibBuilder.loadTexts:
    aluWdmSFD2LCard.setStatus("current")
_AluWdmSFD2MCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2MCard = _AluWdmSFD2MCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 50)
)
if mibBuilder.loadTexts:
    aluWdmSFD2MCard.setStatus("current")
_AluWdmSFD2NCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2NCard = _AluWdmSFD2NCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 51)
)
if mibBuilder.loadTexts:
    aluWdmSFD2NCard.setStatus("current")
_AluWdmSFD2OCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2OCard = _AluWdmSFD2OCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 52)
)
if mibBuilder.loadTexts:
    aluWdmSFD2OCard.setStatus("current")
_AluWdmSFD2PCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2PCard = _AluWdmSFD2PCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 53)
)
if mibBuilder.loadTexts:
    aluWdmSFD2PCard.setStatus("current")
_AluWdmSFD2QCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2QCard = _AluWdmSFD2QCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 54)
)
if mibBuilder.loadTexts:
    aluWdmSFD2QCard.setStatus("current")
_AluWdmSFD2RCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2RCard = _AluWdmSFD2RCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 55)
)
if mibBuilder.loadTexts:
    aluWdmSFD2RCard.setStatus("current")
_AluWdmVwmSFD8ACard_ObjectIdentity = ObjectIdentity
aluWdmVwmSFD8ACard = _AluWdmVwmSFD8ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 56)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFD8ACard.setStatus("current")
_AluWdmVwmSFD8BCard_ObjectIdentity = ObjectIdentity
aluWdmVwmSFD8BCard = _AluWdmVwmSFD8BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 57)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFD8BCard.setStatus("current")
_AluWdmVwmSFD8CCard_ObjectIdentity = ObjectIdentity
aluWdmVwmSFD8CCard = _AluWdmVwmSFD8CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 58)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFD8CCard.setStatus("current")
_AluWdmVwmSFD8DCard_ObjectIdentity = ObjectIdentity
aluWdmVwmSFD8DCard = _AluWdmVwmSFD8DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 59)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFD8DCard.setStatus("current")
_AluWdmVwmSFC8Card_ObjectIdentity = ObjectIdentity
aluWdmVwmSFC8Card = _AluWdmVwmSFC8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 60)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFC8Card.setStatus("current")
_TropicCommonEquipmentReg_ObjectIdentity = ObjectIdentity
tropicCommonEquipmentReg = _TropicCommonEquipmentReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6)
)
if mibBuilder.loadTexts:
    tropicCommonEquipmentReg.setStatus("current")
_AluWdmPowerFilterCard_ObjectIdentity = ObjectIdentity
aluWdmPowerFilterCard = _AluWdmPowerFilterCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 4)
)
if mibBuilder.loadTexts:
    aluWdmPowerFilterCard.setStatus("current")
_AluWdmFanUnitCard_ObjectIdentity = ObjectIdentity
aluWdmFanUnitCard = _AluWdmFanUnitCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 5)
)
if mibBuilder.loadTexts:
    aluWdmFanUnitCard.setStatus("current")
_AluWdmUserInterfacePanelCard_ObjectIdentity = ObjectIdentity
aluWdmUserInterfacePanelCard = _AluWdmUserInterfacePanelCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 6)
)
if mibBuilder.loadTexts:
    aluWdmUserInterfacePanelCard.setStatus("current")
_AluWdmBusTerminationCard_ObjectIdentity = ObjectIdentity
aluWdmBusTerminationCard = _AluWdmBusTerminationCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 7)
)
if mibBuilder.loadTexts:
    aluWdmBusTerminationCard.setStatus("current")
_AluWdmBusTerminationOnlyCard_ObjectIdentity = ObjectIdentity
aluWdmBusTerminationOnlyCard = _AluWdmBusTerminationOnlyCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 8)
)
if mibBuilder.loadTexts:
    aluWdmBusTerminationOnlyCard.setStatus("current")
_AluWdmPSS8ShelfPanelCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8ShelfPanelCard = _AluWdmPSS8ShelfPanelCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 9)
)
if mibBuilder.loadTexts:
    aluWdmPSS8ShelfPanelCard.setStatus("current")
_AluWdmPSS8UserInterfacePanelCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8UserInterfacePanelCard = _AluWdmPSS8UserInterfacePanelCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 10)
)
if mibBuilder.loadTexts:
    aluWdmPSS8UserInterfacePanelCard.setStatus("current")
_AluWdmMultiFunctionCard_ObjectIdentity = ObjectIdentity
aluWdmMultiFunctionCard = _AluWdmMultiFunctionCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 11)
)
if mibBuilder.loadTexts:
    aluWdmMultiFunctionCard.setStatus("current")
_AluWdmPSS8PowerFilterAcCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8PowerFilterAcCard = _AluWdmPSS8PowerFilterAcCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 12)
)
if mibBuilder.loadTexts:
    aluWdmPSS8PowerFilterAcCard.setStatus("current")
_TropicGeneric_ObjectIdentity = ObjectIdentity
tropicGeneric = _TropicGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2)
)
if mibBuilder.loadTexts:
    tropicGeneric.setStatus("current")
_TnSystem_ObjectIdentity = ObjectIdentity
tnSystem = _TnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1)
)
if mibBuilder.loadTexts:
    tnSystem.setStatus("current")
_TnSystemMIB_ObjectIdentity = ObjectIdentity
tnSystemMIB = _TnSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnSystemMIB.setStatus("current")
_TnNotificationMIB_ObjectIdentity = ObjectIdentity
tnNotificationMIB = _TnNotificationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnNotificationMIB.setStatus("current")
_TnLogMIB_ObjectIdentity = ObjectIdentity
tnLogMIB = _TnLogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnLogMIB.setStatus("current")
_TnDiagnosticMIB_ObjectIdentity = ObjectIdentity
tnDiagnosticMIB = _TnDiagnosticMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnDiagnosticMIB.setStatus("current")
_TnSoftwareMIB_ObjectIdentity = ObjectIdentity
tnSoftwareMIB = _TnSoftwareMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnSoftwareMIB.setStatus("current")
_TnPowerMgmtMIB_ObjectIdentity = ObjectIdentity
tnPowerMgmtMIB = _TnPowerMgmtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnPowerMgmtMIB.setStatus("current")
_TnUserMgmtMIB_ObjectIdentity = ObjectIdentity
tnUserMgmtMIB = _TnUserMgmtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnUserMgmtMIB.setStatus("current")
_TnPhMNotificationMIB_ObjectIdentity = ObjectIdentity
tnPhMNotificationMIB = _TnPhMNotificationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnPhMNotificationMIB.setStatus("current")
_TnAsonMIB_ObjectIdentity = ObjectIdentity
tnAsonMIB = _TnAsonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnAsonMIB.setStatus("current")
_TnGmplsMIB_ObjectIdentity = ObjectIdentity
tnGmplsMIB = _TnGmplsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnGmplsMIB.setStatus("current")
_TnGmplsObjs_ObjectIdentity = ObjectIdentity
tnGmplsObjs = _TnGmplsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tnGmplsObjs.setStatus("current")
_TnEquipment_ObjectIdentity = ObjectIdentity
tnEquipment = _TnEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2)
)
if mibBuilder.loadTexts:
    tnEquipment.setStatus("current")
_TnShelf_ObjectIdentity = ObjectIdentity
tnShelf = _TnShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnShelf.setStatus("current")
_TnShelfMIB_ObjectIdentity = ObjectIdentity
tnShelfMIB = _TnShelfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnShelfMIB.setStatus("current")
_TnSlot_ObjectIdentity = ObjectIdentity
tnSlot = _TnSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSlot.setStatus("current")
_TnSlotMIB_ObjectIdentity = ObjectIdentity
tnSlotMIB = _TnSlotMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSlotMIB.setStatus("current")
_TnCard_ObjectIdentity = ObjectIdentity
tnCard = _TnCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tnCard.setStatus("current")
_TnCardMIB_ObjectIdentity = ObjectIdentity
tnCardMIB = _TnCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnCardMIB.setStatus("current")
_TnWaveKeyMIB_ObjectIdentity = ObjectIdentity
tnWaveKeyMIB = _TnWaveKeyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnWaveKeyMIB.setStatus("current")
_TnControlCardMIB_ObjectIdentity = ObjectIdentity
tnControlCardMIB = _TnControlCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    tnControlCardMIB.setStatus("current")
_TnEthernetCardMIB_ObjectIdentity = ObjectIdentity
tnEthernetCardMIB = _TnEthernetCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    tnEthernetCardMIB.setStatus("current")
_TnOpticalCardMIB_ObjectIdentity = ObjectIdentity
tnOpticalCardMIB = _TnOpticalCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    tnOpticalCardMIB.setStatus("current")
_TnSwitchCardMIB_ObjectIdentity = ObjectIdentity
tnSwitchCardMIB = _TnSwitchCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 6)
)
if mibBuilder.loadTexts:
    tnSwitchCardMIB.setStatus("current")
_TnAmplifierMIB_ObjectIdentity = ObjectIdentity
tnAmplifierMIB = _TnAmplifierMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7)
)
if mibBuilder.loadTexts:
    tnAmplifierMIB.setStatus("current")
_TnPort_ObjectIdentity = ObjectIdentity
tnPort = _TnPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tnPort.setStatus("current")
_TnAccessPortMIB_ObjectIdentity = ObjectIdentity
tnAccessPortMIB = _TnAccessPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnAccessPortMIB.setStatus("current")
_TnEthernetPortMIB_ObjectIdentity = ObjectIdentity
tnEthernetPortMIB = _TnEthernetPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tnEthernetPortMIB.setStatus("current")
_TnOpticalPortMIB_ObjectIdentity = ObjectIdentity
tnOpticalPortMIB = _TnOpticalPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    tnOpticalPortMIB.setStatus("current")
_TnSwitchPortMIB_ObjectIdentity = ObjectIdentity
tnSwitchPortMIB = _TnSwitchPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    tnSwitchPortMIB.setStatus("current")
_TnOchMIB_ObjectIdentity = ObjectIdentity
tnOchMIB = _TnOchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    tnOchMIB.setStatus("current")
_TnVtsConnMIB_ObjectIdentity = ObjectIdentity
tnVtsConnMIB = _TnVtsConnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6)
)
if mibBuilder.loadTexts:
    tnVtsConnMIB.setStatus("current")
_TnOtuOduMIB_ObjectIdentity = ObjectIdentity
tnOtuOduMIB = _TnOtuOduMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7)
)
if mibBuilder.loadTexts:
    tnOtuOduMIB.setStatus("current")
_TnSyncEMIB_ObjectIdentity = ObjectIdentity
tnSyncEMIB = _TnSyncEMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8)
)
if mibBuilder.loadTexts:
    tnSyncEMIB.setStatus("current")
_TnPtpMIB_ObjectIdentity = ObjectIdentity
tnPtpMIB = _TnPtpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9)
)
if mibBuilder.loadTexts:
    tnPtpMIB.setStatus("current")
_TnOthMIB_ObjectIdentity = ObjectIdentity
tnOthMIB = _TnOthMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10)
)
if mibBuilder.loadTexts:
    tnOthMIB.setStatus("current")
_TnMiscEquipment_ObjectIdentity = ObjectIdentity
tnMiscEquipment = _TnMiscEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tnMiscEquipment.setStatus("current")
_TnFanMIB_ObjectIdentity = ObjectIdentity
tnFanMIB = _TnFanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tnFanMIB.setStatus("current")
_TnBreakerMIB_ObjectIdentity = ObjectIdentity
tnBreakerMIB = _TnBreakerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    tnBreakerMIB.setStatus("current")
_TnAlarmPanelMIB_ObjectIdentity = ObjectIdentity
tnAlarmPanelMIB = _TnAlarmPanelMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    tnAlarmPanelMIB.setStatus("current")
_TnServices_ObjectIdentity = ObjectIdentity
tnServices = _TnServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3)
)
if mibBuilder.loadTexts:
    tnServices.setStatus("current")
_TnL1ServiceMIB_ObjectIdentity = ObjectIdentity
tnL1ServiceMIB = _TnL1ServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnL1ServiceMIB.setStatus("current")
_TnL2ServiceMIB_ObjectIdentity = ObjectIdentity
tnL2ServiceMIB = _TnL2ServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnL2ServiceMIB.setStatus("current")
_TnStatistics_ObjectIdentity = ObjectIdentity
tnStatistics = _TnStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4)
)
if mibBuilder.loadTexts:
    tnStatistics.setStatus("current")
_TnStatisticsMIB_ObjectIdentity = ObjectIdentity
tnStatisticsMIB = _TnStatisticsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnStatisticsMIB.setStatus("current")
_TnProtocols_ObjectIdentity = ObjectIdentity
tnProtocols = _TnProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5)
)
if mibBuilder.loadTexts:
    tnProtocols.setStatus("current")
_TnOspfMIB_ObjectIdentity = ObjectIdentity
tnOspfMIB = _TnOspfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tnOspfMIB.setStatus("current")
_TropicProducts_ObjectIdentity = ObjectIdentity
tropicProducts = _TropicProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 3)
)
if mibBuilder.loadTexts:
    tropicProducts.setStatus("current")
_TropicExpr_ObjectIdentity = ObjectIdentity
tropicExpr = _TropicExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4)
)
if mibBuilder.loadTexts:
    tropicExpr.setStatus("current")
_TnExprOpticalCardMIB_ObjectIdentity = ObjectIdentity
tnExprOpticalCardMIB = _TnExprOpticalCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1)
)
if mibBuilder.loadTexts:
    tnExprOpticalCardMIB.setStatus("current")
_TnExprOpticalPortMIB_ObjectIdentity = ObjectIdentity
tnExprOpticalPortMIB = _TnExprOpticalPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 2)
)
if mibBuilder.loadTexts:
    tnExprOpticalPortMIB.setStatus("current")
_TnExprScalarsMIB_ObjectIdentity = ObjectIdentity
tnExprScalarsMIB = _TnExprScalarsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3)
)
if mibBuilder.loadTexts:
    tnExprScalarsMIB.setStatus("current")
_TnReg_ObjectIdentity = ObjectIdentity
tnReg = _TnReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5)
)
if mibBuilder.loadTexts:
    tnReg.setStatus("current")
_TnModules_ObjectIdentity = ObjectIdentity
tnModules = _TnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1)
)
if mibBuilder.loadTexts:
    tnModules.setStatus("current")
_TnSRMIBModules_ObjectIdentity = ObjectIdentity
tnSRMIBModules = _TnSRMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3)
)
if mibBuilder.loadTexts:
    tnSRMIBModules.setStatus("current")
_TnRmdMIBModules_ObjectIdentity = ObjectIdentity
tnRmdMIBModules = _TnRmdMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 4)
)
if mibBuilder.loadTexts:
    tnRmdMIBModules.setStatus("current")
_TnProducts_ObjectIdentity = ObjectIdentity
tnProducts = _TnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6)
)
if mibBuilder.loadTexts:
    tnProducts.setStatus("current")
_TnSRMIB_ObjectIdentity = ObjectIdentity
tnSRMIB = _TnSRMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1)
)
if mibBuilder.loadTexts:
    tnSRMIB.setStatus("current")
_TnSRObjs_ObjectIdentity = ObjectIdentity
tnSRObjs = _TnSRObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2)
)
if mibBuilder.loadTexts:
    tnSRObjs.setStatus("current")
_TnSRNotifyPrefix_ObjectIdentity = ObjectIdentity
tnSRNotifyPrefix = _TnSRNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3)
)
if mibBuilder.loadTexts:
    tnSRNotifyPrefix.setStatus("current")
_TnRmdMIB_ObjectIdentity = ObjectIdentity
tnRmdMIB = _TnRmdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4)
)
if mibBuilder.loadTexts:
    tnRmdMIB.setStatus("current")
_TnRmdObjs_ObjectIdentity = ObjectIdentity
tnRmdObjs = _TnRmdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1)
)
if mibBuilder.loadTexts:
    tnRmdObjs.setStatus("current")
_TnSASProducts_ObjectIdentity = ObjectIdentity
tnSASProducts = _TnSASProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7)
)
if mibBuilder.loadTexts:
    tnSASProducts.setStatus("current")
_TnServiceAccessSwitches_ObjectIdentity = ObjectIdentity
tnServiceAccessSwitches = _TnServiceAccessSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2)
)
if mibBuilder.loadTexts:
    tnServiceAccessSwitches.setStatus("current")
_TnSASRegistry_ObjectIdentity = ObjectIdentity
tnSASRegistry = _TnSASRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1)
)
if mibBuilder.loadTexts:
    tnSASRegistry.setStatus("current")
_TnSASModules_ObjectIdentity = ObjectIdentity
tnSASModules = _TnSASModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnSASModules.setStatus("current")
_TnSASMIBModules_ObjectIdentity = ObjectIdentity
tnSASMIBModules = _TnSASMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnSASMIBModules.setStatus("current")
_TnSASMIB_ObjectIdentity = ObjectIdentity
tnSASMIB = _TnSASMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2)
)
if mibBuilder.loadTexts:
    tnSASMIB.setStatus("current")
_TnSASObjs_ObjectIdentity = ObjectIdentity
tnSASObjs = _TnSASObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSASObjs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-GLOBAL-REG",
    **{"tropic": tropic,
       "tropicRegistry": tropicRegistry,
       "tropicModules": tropicModules,
       "tropicGlobalRegModule": tropicGlobalRegModule,
       "tnGenericModules": tnGenericModules,
       "tnSystemModules": tnSystemModules,
       "tnEquipmentModules": tnEquipmentModules,
       "tnShelfModules": tnShelfModules,
       "tnSlotModules": tnSlotModules,
       "tnCardModules": tnCardModules,
       "tnPortModules": tnPortModules,
       "tnMiscModules": tnMiscModules,
       "tnServiceModules": tnServiceModules,
       "tnProtocolModules": tnProtocolModules,
       "tropicExprModules": tropicExprModules,
       "tnGmplsMIBModules": tnGmplsMIBModules,
       "tnTypeDefinitionModules": tnTypeDefinitionModules,
       "tropicMetroReg": tropicMetroReg,
       "tropicMetroNodeReg": tropicMetroNodeReg,
       "tropicTRX24000": tropicTRX24000,
       "aluWdm1830PSS32": aluWdm1830PSS32,
       "aluWdm1830PSS1": aluWdm1830PSS1,
       "aluWdm1830PSS1MD4H": aluWdm1830PSS1MD4H,
       "aluWdm1830PSS1GBEH": aluWdm1830PSS1GBEH,
       "aluWdm1830PSS": aluWdm1830PSS,
       "aluWdm1830PSS4": aluWdm1830PSS4,
       "aluWdm1830PSS1MSAH": aluWdm1830PSS1MSAH,
       "tropicShelfReg": tropicShelfReg,
       "tropicEmptyShelf": tropicEmptyShelf,
       "tropicUnknownShelf": tropicUnknownShelf,
       "aluWdmSfd44Shelf": aluWdmSfd44Shelf,
       "aluWdmDcmShelf": aluWdmDcmShelf,
       "aluWdmUniversalShelf": aluWdmUniversalShelf,
       "aluWdmSfd44bShelf": aluWdmSfd44bShelf,
       "aluWdmItlbShelf": aluWdmItlbShelf,
       "aluWdmPSS32UniversalShelf": aluWdmPSS32UniversalShelf,
       "aluWdmPSS16UniversalShelf": aluWdmPSS16UniversalShelf,
       "aluWdmSfd40Shelf": aluWdmSfd40Shelf,
       "aluWdmSfd40bShelf": aluWdmSfd40bShelf,
       "aluWdmPSS4UniversalShelf": aluWdmPSS4UniversalShelf,
       "aluWdmPSS36UniversalShelf": aluWdmPSS36UniversalShelf,
       "aluWdmPSS64UniversalShelf": aluWdmPSS64UniversalShelf,
       "aluWdmItluShelf": aluWdmItluShelf,
       "aluWdmPSS32SwitchUniversalShelf": aluWdmPSS32SwitchUniversalShelf,
       "aluWdmPSS32Switch1P2TUniversalShelf": aluWdmPSS32Switch1P2TUniversalShelf,
       "aluWdmPsc1x6Shelf": aluWdmPsc1x6Shelf,
       "aluWdmPSS8UniversalShelf": aluWdmPSS8UniversalShelf,
       "aluWdmPSS16IIUniversalShelf": aluWdmPSS16IIUniversalShelf,
       "aluWdmPSS48UniversalShelf": aluWdmPSS48UniversalShelf,
       "aluWdmPSS96UniversalShelf": aluWdmPSS96UniversalShelf,
       "aluWdmMsh8fsmShelf": aluWdmMsh8fsmShelf,
       "aluWdmVwmCwUniversalShelf": aluWdmVwmCwUniversalShelf,
       "aluWdmVwmDwUniversalShelf": aluWdmVwmDwUniversalShelf,
       "tropicCardReg": tropicCardReg,
       "tropicMiscCardReg": tropicMiscCardReg,
       "tropicEmptyCard": tropicEmptyCard,
       "tropicUnknownCard": tropicUnknownCard,
       "tropicInvalidCard": tropicInvalidCard,
       "tropicReservedCard": tropicReservedCard,
       "tropicHalfHeightCarrierCard": tropicHalfHeightCarrierCard,
       "aluWdmVirtualCard": aluWdmVirtualCard,
       "aluWdmGmreCard": aluWdmGmreCard,
       "aluWdmMsh8fsmCard": aluWdmMsh8fsmCard,
       "tropicControlCardReg": tropicControlCardReg,
       "tropicMasterControlCard": tropicMasterControlCard,
       "aluWdmEquipmentControllerCard": aluWdmEquipmentControllerCard,
       "aluWdmFirstLevelControllerCard": aluWdmFirstLevelControllerCard,
       "aluWdmMatrix3T8Card": aluWdmMatrix3T8Card,
       "aluWdmMatrix1T9Card": aluWdmMatrix1T9Card,
       "aluWdmPSS4EquipmentControllerCard": aluWdmPSS4EquipmentControllerCard,
       "aluWdmMatrix0CompactCard": aluWdmMatrix0CompactCard,
       "aluWdmUniversalMatrixFirstLevelControllerCard": aluWdmUniversalMatrixFirstLevelControllerCard,
       "aluWdmEndOfShelfMiddleCard": aluWdmEndOfShelfMiddleCard,
       "aluWdmUniversalMatrixFirstLevelController1p2TCard": aluWdmUniversalMatrixFirstLevelController1p2TCard,
       "aluWdmPSS8EquipmentController2Card": aluWdmPSS8EquipmentController2Card,
       "aluWdmPSS16IIEquipmentController2Card": aluWdmPSS16IIEquipmentController2Card,
       "aluWdmPSS32EquipmentController2Card": aluWdmPSS32EquipmentController2Card,
       "aluWdmClockControllerCard96Card": aluWdmClockControllerCard96Card,
       "aluWdmVwmCwEquipmentControllerCard": aluWdmVwmCwEquipmentControllerCard,
       "aluWdmVwmDwEquipmentControllerCard": aluWdmVwmDwEquipmentControllerCard,
       "tropicOpticalSwitchCardReg": tropicOpticalSwitchCardReg,
       "tropicPhotonicProtectionSwitchCard": tropicPhotonicProtectionSwitchCard,
       "aluWdmOpsaCard": aluWdmOpsaCard,
       "aluWdmOpsbCard": aluWdmOpsbCard,
       "aluWdmMcs8x16Card": aluWdmMcs8x16Card,
       "aluWdmSwitchingCard": aluWdmSwitchingCard,
       "aluWdm12p120Card": aluWdm12p120Card,
       "aluWdm20p200Card": aluWdm20p200Card,
       "aluWdm1ud200Card": aluWdm1ud200Card,
       "tropicDWDMFilterCardReg": tropicDWDMFilterCardReg,
       "aluWdmCwr8Card": aluWdmCwr8Card,
       "aluWdmSfd44Card": aluWdmSfd44Card,
       "aluWdmSVACCard": aluWdmSVACCard,
       "aluWdmCwr8c88Card": aluWdmCwr8c88Card,
       "aluWdmSfd44bCard": aluWdmSfd44bCard,
       "aluWdmItlbCard": aluWdmItlbCard,
       "aluWdmSfd40Card": aluWdmSfd40Card,
       "aluWdmSfd40bCard": aluWdmSfd40bCard,
       "aluWdmWr2c88Card": aluWdmWr2c88Card,
       "aluWdmMVACCard": aluWdmMVACCard,
       "aluWdmItluCard": aluWdmItluCard,
       "aluWdmWr8c88aCard": aluWdmWr8c88aCard,
       "aluWdmMesh4Card": aluWdmMesh4Card,
       "aluWdmMVAC8BCard": aluWdmMVAC8BCard,
       "aluWdmWr8c88afCard": aluWdmWr8c88afCard,
       "aluWdmPsc1x6Card": aluWdmPsc1x6Card,
       "aluWdmWr20tfCard": aluWdmWr20tfCard,
       "aluWdmWr20tfmCard": aluWdmWr20tfmCard,
       "tropicAmplifierCardReg": tropicAmplifierCardReg,
       "aluWdmAhphgCard": aluWdmAhphgCard,
       "aluWdmAlphgCard": aluWdmAlphgCard,
       "aluWdmAhplgCard": aluWdmAhplgCard,
       "aluWdmAlpfgkCard": aluWdmAlpfgkCard,
       "aluWdmOscCard": aluWdmOscCard,
       "aluWdmA2325aCard": aluWdmA2325aCard,
       "aluWdmAlpfgtCard": aluWdmAlpfgtCard,
       "aluWdmOsctCard": aluWdmOsctCard,
       "aluWdmWtocmCard": aluWdmWtocmCard,
       "aluWdmAm2017bCard": aluWdmAm2017bCard,
       "aluWdmAm2325bCard": aluWdmAm2325bCard,
       "aluWdmRa2pCard": aluWdmRa2pCard,
       "aluWdmAm2318aCard": aluWdmAm2318aCard,
       "aluWdmAm2125aCard": aluWdmAm2125aCard,
       "aluWdmAm2125bCard": aluWdmAm2125bCard,
       "aluWdmWtocmaCard": aluWdmWtocmaCard,
       "aluWdmA2p2125Card": aluWdmA2p2125Card,
       "aluWdmAm2625aCard": aluWdmAm2625aCard,
       "aluWdmAm2032aCard": aluWdmAm2032aCard,
       "aluWdmAa2donwCard": aluWdmAa2donwCard,
       "aluWdmWtocmfCard": aluWdmWtocmfCard,
       "aluWdmAswgCard": aluWdmAswgCard,
       "aluWdmA4pswgCard": aluWdmA4pswgCard,
       "aluWdmOtdrCard": aluWdmOtdrCard,
       "aluWdmAar8aCard": aluWdmAar8aCard,
       "tropicDispersionCompCardReg": tropicDispersionCompCardReg,
       "aluWdmDcmCard": aluWdmDcmCard,
       "aluWdmOpticalTransponderCardReg": aluWdmOpticalTransponderCardReg,
       "aluWdm11star1Card": aluWdm11star1Card,
       "aluWdm11stge12Card": aluWdm11stge12Card,
       "aluWdm11dpge12Card": aluWdm11dpge12Card,
       "aluWdm11stmm10Card": aluWdm11stmm10Card,
       "aluWdm4dpa4Card": aluWdm4dpa4Card,
       "aluWdm43stx4Card": aluWdm43stx4Card,
       "aluWdm4dpa2Card": aluWdm4dpa2Card,
       "aluWdm43sta1pCard": aluWdm43sta1pCard,
       "aluWdm43stx4pCard": aluWdm43stx4pCard,
       "aluWdm11qpa4Card": aluWdm11qpa4Card,
       "aluWdm112scx10Card": aluWdm112scx10Card,
       "aluWdm112sca1Card": aluWdm112sca1Card,
       "aluWdm1dpp21Card": aluWdm1dpp21Card,
       "aluWdm43scx4Card": aluWdm43scx4Card,
       "aluWdm11dpe12eCard": aluWdm11dpe12eCard,
       "aluWdm112sx10lCard": aluWdm112sx10lCard,
       "aluWdm112sa1lCard": aluWdm112sa1lCard,
       "aluWdm11dpm12Card": aluWdm11dpm12Card,
       "aluWdm43sca1Card": aluWdm43sca1Card,
       "aluWdm43scx4lCard": aluWdm43scx4lCard,
       "aluWdm112snx10Card": aluWdm112snx10Card,
       "aluWdm112sna1Card": aluWdm112sna1Card,
       "aluWdm1dpp24mCard": aluWdm1dpp24mCard,
       "aluWdmul43scupCard": aluWdmul43scupCard,
       "aluWdmul11qcupCard": aluWdmul11qcupCard,
       "aluWdm11qpen4Card": aluWdm11qpen4Card,
       "aluWdm43scx4eCard": aluWdm43scx4eCard,
       "aluWdm43scge1Card": aluWdm43scge1Card,
       "aluWdm11qpe24Card": aluWdm11qpe24Card,
       "aluWdm11star1aCard": aluWdm11star1aCard,
       "aluWdmcl10an10gCard": aluWdmcl10an10gCard,
       "aluWdmcl24anmCard": aluWdmcl24anmCard,
       "aluWdm11dpe12aCard": aluWdm11dpe12aCard,
       "aluWdmul130scupCard": aluWdmul130scupCard,
       "aluWdm130scx10Card": aluWdm130scx10Card,
       "aluWdm4qpa8Card": aluWdm4qpa8Card,
       "aluWdmOt112pdm11Card": aluWdmOt112pdm11Card,
       "aluWdmPtpctlCard": aluWdmPtpctlCard,
       "aluWdmPtpioCard": aluWdmPtpioCard,
       "aluWdmIo24et1gbCard": aluWdmIo24et1gbCard,
       "aluWdmIo4an10gCard": aluWdmIo4an10gCard,
       "aluWdmIo8et1gbCard": aluWdmIo8et1gbCard,
       "aluWdmIo10et10gCard": aluWdmIo10et10gCard,
       "aluWdmUl11qcupcCard": aluWdmUl11qcupcCard,
       "aluWdmOt520scx4Card": aluWdmOt520scx4Card,
       "aluWdm11ope8Card": aluWdm11ope8Card,
       "aluWdm11qce12xCard": aluWdm11qce12xCard,
       "aluWdmOt260scx2Card": aluWdmOt260scx2Card,
       "aluWdmOt130snx10Card": aluWdmOt130snx10Card,
       "aluWdmIo24anmbCard": aluWdmIo24anmbCard,
       "aluWdmOt11dpm8Card": aluWdmOt11dpm8Card,
       "aluWdmOt11dpm4mCard": aluWdmOt11dpm4mCard,
       "aluWdmOt11dpm4eCard": aluWdmOt11dpm4eCard,
       "aluWdmUl130scupbCard": aluWdmUl130scupbCard,
       "aluWdmOt112sdx11Card": aluWdmOt112sdx11Card,
       "aluWdmOt130sca1Card": aluWdmOt130sca1Card,
       "aluWdmIo10an10gbCard": aluWdmIo10an10gbCard,
       "aluWdmIo10et10gbCard": aluWdmIo10et10gbCard,
       "aluWdmIo4an100gCard": aluWdmIo4an100gCard,
       "aluWdmIo30an10gCard": aluWdmIo30an10gCard,
       "aluWdmIo30an300Card": aluWdmIo30an300Card,
       "aluWdmIo4an400Card": aluWdmIo4an400Card,
       "aluWdmStaticFilterCardReg": aluWdmStaticFilterCardReg,
       "aluWdmSFD5ACard": aluWdmSFD5ACard,
       "aluWdmSFD5BCard": aluWdmSFD5BCard,
       "aluWdmSFD5CCard": aluWdmSFD5CCard,
       "aluWdmSFD5DCard": aluWdmSFD5DCard,
       "aluWdmSFD5ECard": aluWdmSFD5ECard,
       "aluWdmSFD5FCard": aluWdmSFD5FCard,
       "aluWdmSFD5GCard": aluWdmSFD5GCard,
       "aluWdmSFD5HCard": aluWdmSFD5HCard,
       "aluWdmSFD10ACard": aluWdmSFD10ACard,
       "aluWdmSFD10BCard": aluWdmSFD10BCard,
       "aluWdmSFD10CCard": aluWdmSFD10CCard,
       "aluWdmSFD10DCard": aluWdmSFD10DCard,
       "aluWdmSFC2ACard": aluWdmSFC2ACard,
       "aluWdmSFC2BCard": aluWdmSFC2BCard,
       "aluWdmSFC2CCard": aluWdmSFC2CCard,
       "aluWdmSFC2DCard": aluWdmSFC2DCard,
       "aluWdmSFC4ACard": aluWdmSFC4ACard,
       "aluWdmSFC4BCard": aluWdmSFC4BCard,
       "aluWdmSFC8Card": aluWdmSFC8Card,
       "aluWdmSFC1ACard": aluWdmSFC1ACard,
       "aluWdmSFC1BCard": aluWdmSFC1BCard,
       "aluWdmSFC1CCard": aluWdmSFC1CCard,
       "aluWdmSFC1DCard": aluWdmSFC1DCard,
       "aluWdmSFC1ECard": aluWdmSFC1ECard,
       "aluWdmSFC1FCard": aluWdmSFC1FCard,
       "aluWdmSFC1GCard": aluWdmSFC1GCard,
       "aluWdmSFC1HCard": aluWdmSFC1HCard,
       "aluWdmSFD8ACard": aluWdmSFD8ACard,
       "aluWdmSFD8BCard": aluWdmSFD8BCard,
       "aluWdmSFD8CCard": aluWdmSFD8CCard,
       "aluWdmSFD8DCard": aluWdmSFD8DCard,
       "aluWdmSFD4ACard": aluWdmSFD4ACard,
       "aluWdmSFD4BCard": aluWdmSFD4BCard,
       "aluWdmSFD4CCard": aluWdmSFD4CCard,
       "aluWdmSFD4DCard": aluWdmSFD4DCard,
       "aluWdmSFD4ECard": aluWdmSFD4ECard,
       "aluWdmSFD4FCard": aluWdmSFD4FCard,
       "aluWdmSFD4GCard": aluWdmSFD4GCard,
       "aluWdmSFD4HCard": aluWdmSFD4HCard,
       "aluWdmSFD2ACard": aluWdmSFD2ACard,
       "aluWdmSFD2BCard": aluWdmSFD2BCard,
       "aluWdmSFD2CCard": aluWdmSFD2CCard,
       "aluWdmSFD2DCard": aluWdmSFD2DCard,
       "aluWdmSFD2ECard": aluWdmSFD2ECard,
       "aluWdmSFD2FCard": aluWdmSFD2FCard,
       "aluWdmSFD2GCard": aluWdmSFD2GCard,
       "aluWdmSFD2HCard": aluWdmSFD2HCard,
       "aluWdmSFD2ICard": aluWdmSFD2ICard,
       "aluWdmSFD2LCard": aluWdmSFD2LCard,
       "aluWdmSFD2MCard": aluWdmSFD2MCard,
       "aluWdmSFD2NCard": aluWdmSFD2NCard,
       "aluWdmSFD2OCard": aluWdmSFD2OCard,
       "aluWdmSFD2PCard": aluWdmSFD2PCard,
       "aluWdmSFD2QCard": aluWdmSFD2QCard,
       "aluWdmSFD2RCard": aluWdmSFD2RCard,
       "aluWdmVwmSFD8ACard": aluWdmVwmSFD8ACard,
       "aluWdmVwmSFD8BCard": aluWdmVwmSFD8BCard,
       "aluWdmVwmSFD8CCard": aluWdmVwmSFD8CCard,
       "aluWdmVwmSFD8DCard": aluWdmVwmSFD8DCard,
       "aluWdmVwmSFC8Card": aluWdmVwmSFC8Card,
       "tropicCommonEquipmentReg": tropicCommonEquipmentReg,
       "aluWdmPowerFilterCard": aluWdmPowerFilterCard,
       "aluWdmFanUnitCard": aluWdmFanUnitCard,
       "aluWdmUserInterfacePanelCard": aluWdmUserInterfacePanelCard,
       "aluWdmBusTerminationCard": aluWdmBusTerminationCard,
       "aluWdmBusTerminationOnlyCard": aluWdmBusTerminationOnlyCard,
       "aluWdmPSS8ShelfPanelCard": aluWdmPSS8ShelfPanelCard,
       "aluWdmPSS8UserInterfacePanelCard": aluWdmPSS8UserInterfacePanelCard,
       "aluWdmMultiFunctionCard": aluWdmMultiFunctionCard,
       "aluWdmPSS8PowerFilterAcCard": aluWdmPSS8PowerFilterAcCard,
       "tropicGeneric": tropicGeneric,
       "tnSystem": tnSystem,
       "tnSystemMIB": tnSystemMIB,
       "tnNotificationMIB": tnNotificationMIB,
       "tnLogMIB": tnLogMIB,
       "tnDiagnosticMIB": tnDiagnosticMIB,
       "tnSoftwareMIB": tnSoftwareMIB,
       "tnPowerMgmtMIB": tnPowerMgmtMIB,
       "tnUserMgmtMIB": tnUserMgmtMIB,
       "tnPhMNotificationMIB": tnPhMNotificationMIB,
       "tnAsonMIB": tnAsonMIB,
       "tnGmplsMIB": tnGmplsMIB,
       "tnGmplsObjs": tnGmplsObjs,
       "tnEquipment": tnEquipment,
       "tnShelf": tnShelf,
       "tnShelfMIB": tnShelfMIB,
       "tnSlot": tnSlot,
       "tnSlotMIB": tnSlotMIB,
       "tnCard": tnCard,
       "tnCardMIB": tnCardMIB,
       "tnWaveKeyMIB": tnWaveKeyMIB,
       "tnControlCardMIB": tnControlCardMIB,
       "tnEthernetCardMIB": tnEthernetCardMIB,
       "tnOpticalCardMIB": tnOpticalCardMIB,
       "tnSwitchCardMIB": tnSwitchCardMIB,
       "tnAmplifierMIB": tnAmplifierMIB,
       "tnPort": tnPort,
       "tnAccessPortMIB": tnAccessPortMIB,
       "tnEthernetPortMIB": tnEthernetPortMIB,
       "tnOpticalPortMIB": tnOpticalPortMIB,
       "tnSwitchPortMIB": tnSwitchPortMIB,
       "tnOchMIB": tnOchMIB,
       "tnVtsConnMIB": tnVtsConnMIB,
       "tnOtuOduMIB": tnOtuOduMIB,
       "tnSyncEMIB": tnSyncEMIB,
       "tnPtpMIB": tnPtpMIB,
       "tnOthMIB": tnOthMIB,
       "tnMiscEquipment": tnMiscEquipment,
       "tnFanMIB": tnFanMIB,
       "tnBreakerMIB": tnBreakerMIB,
       "tnAlarmPanelMIB": tnAlarmPanelMIB,
       "tnServices": tnServices,
       "tnL1ServiceMIB": tnL1ServiceMIB,
       "tnL2ServiceMIB": tnL2ServiceMIB,
       "tnStatistics": tnStatistics,
       "tnStatisticsMIB": tnStatisticsMIB,
       "tnProtocols": tnProtocols,
       "tnOspfMIB": tnOspfMIB,
       "tropicProducts": tropicProducts,
       "tropicExpr": tropicExpr,
       "tnExprOpticalCardMIB": tnExprOpticalCardMIB,
       "tnExprOpticalPortMIB": tnExprOpticalPortMIB,
       "tnExprScalarsMIB": tnExprScalarsMIB,
       "tnReg": tnReg,
       "tnModules": tnModules,
       "tnSRMIBModules": tnSRMIBModules,
       "tnRmdMIBModules": tnRmdMIBModules,
       "tnProducts": tnProducts,
       "tnSRMIB": tnSRMIB,
       "tnSRObjs": tnSRObjs,
       "tnSRNotifyPrefix": tnSRNotifyPrefix,
       "tnRmdMIB": tnRmdMIB,
       "tnRmdObjs": tnRmdObjs,
       "tnSASProducts": tnSASProducts,
       "tnServiceAccessSwitches": tnServiceAccessSwitches,
       "tnSASRegistry": tnSASRegistry,
       "tnSASModules": tnSASModules,
       "tnSASMIBModules": tnSASMIBModules,
       "tnSASMIB": tnSASMIB,
       "tnSASObjs": tnSASObjs}
)
