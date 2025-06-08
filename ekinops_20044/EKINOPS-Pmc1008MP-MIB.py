# SNMP MIB module (EKINOPS-Pmc1008MP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmc1008MP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:48 2025
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

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

modulePmc1008mp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47)
)
if mibBuilder.loadTexts:
    modulePmc1008mp.setRevisions(
        ("2010-05-25 00:00",
         "2010-11-09 00:00",
         "2011-01-06 00:00",
         "2011-01-13 00:00",
         "2012-07-03 00:00",
         "2013-04-03 00:00",
         "2014-03-27 00:00",
         "2015-01-14 00:00",
         "2015-01-14 00:00",
         "2016-05-19 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pmc1008mpModeTimeSlot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("dualPassThrough", 1),
          ("addDropTsA", 2),
          ("addDropTsB", 4),
          ("splitSelectTsA", 8),
          ("splitSelectTsB", 16),
          ("splitSelectTsATsB", 32))
    )



class Pmc1008mpModeAddDropA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("passThroughA", 1),
          ("addDropTsA", 2),
          ("splitSelectTsA", 4))
    )



class Pmc1008mpModeAddDrop(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("dualPassThrough", 1),
          ("addDropTsA", 2),
          ("addDropTsB", 4),
          ("splitSelectTsA", 8),
          ("splitSelectTsB", 16),
          ("splitSelectTsATsB", 32))
    )



class Pmc1008mpProtectionTimeSlot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              257,
              513)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manualX1Line1", 257),
          ("manualX2Line2", 513))
    )



class Pmc1008mpProtectionStartUp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manualX2Line2", 0),
          ("manualX1Line1", 1),
          ("auto", 2))
    )



class Pmc1008mpDccMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dccNo", 0),
          ("dcctermLine1", 1),
          ("dcctermLine2", 2),
          ("dcctermLines12", 3),
          ("dccmaster", 4),
          ("dccslaveLine12", 7))
    )



class Pmc1008mpOtxMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("otx80mode", 1),
          ("otx60mode", 2),
          ("otxadjustmode", 4))
    )



class Pmc1008mpOtxGrid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("otxgrid50", 50),
          ("otxgrid100", 100),
          ("otxgrid200", 200))
    )



class Pmc1008mpAdjustValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("otxadjustvalue0", 0),
          ("otxadjustvalue1", 1),
          ("otxadjustvalue2", 2),
          ("otxadjustvalue3", 3),
          ("otxadjustvalue4", 4),
          ("otxadjustvalue5", 5),
          ("otxadjustvalue6", 6),
          ("otxadjustvalue7", 7),
          ("otxadjustvalue8", 8),
          ("otxadjustvalue9", 9),
          ("otxadjustvalue10", 10))
    )



class Pmc1008mpOtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pmc1008mpalarms_ObjectIdentity = ObjectIdentity
pmc1008mpalarms = _Pmc1008mpalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2)
)
_Pmc1008mpAlmOther_ObjectIdentity = ObjectIdentity
pmc1008mpAlmOther = _Pmc1008mpAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1)
)
_Pmc1008mpAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmc1008mpAlmOtherNurg = _Pmc1008mpAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 1)
)
_Pmc1008mpAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmc1008mpAlmsynthAlm2 = _Pmc1008mpAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 1, 2)
)
_Pmc1008mpAlmConfTableSave_Type = EkiOnOff
_Pmc1008mpAlmConfTableSave_Object = MibScalar
pmc1008mpAlmConfTableSave = _Pmc1008mpAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 1, 2, 1),
    _Pmc1008mpAlmConfTableSave_Type()
)
pmc1008mpAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmConfTableSave.setStatus("current")
_Pmc1008mpAlmInvUpload_Type = EkiOnOff
_Pmc1008mpAlmInvUpload_Object = MibScalar
pmc1008mpAlmInvUpload = _Pmc1008mpAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 1, 2, 2),
    _Pmc1008mpAlmInvUpload_Type()
)
pmc1008mpAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmInvUpload.setStatus("current")
_Pmc1008mpAlmConfTableLoad_Type = EkiOnOff
_Pmc1008mpAlmConfTableLoad_Object = MibScalar
pmc1008mpAlmConfTableLoad = _Pmc1008mpAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 1, 2, 3),
    _Pmc1008mpAlmConfTableLoad_Type()
)
pmc1008mpAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmConfTableLoad.setStatus("current")
_Pmc1008mpAlmCorrelatOff_Type = EkiOnOff
_Pmc1008mpAlmCorrelatOff_Object = MibScalar
pmc1008mpAlmCorrelatOff = _Pmc1008mpAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 1, 2, 4),
    _Pmc1008mpAlmCorrelatOff_Type()
)
pmc1008mpAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmCorrelatOff.setStatus("current")
_Pmc1008mpAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmc1008mpAlmOtherUrg = _Pmc1008mpAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2)
)
_Pmc1008mpAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pmc1008mpAlmmodInitFailLevel2 = _Pmc1008mpAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 194)
)
_Pmc1008mpAlmLedFail_Type = EkiOnOff
_Pmc1008mpAlmLedFail_Object = MibScalar
pmc1008mpAlmLedFail = _Pmc1008mpAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 194, 1),
    _Pmc1008mpAlmLedFail_Type()
)
pmc1008mpAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLedFail.setStatus("current")
_Pmc1008mpAlmNextColdBootForced_Type = EkiOnOff
_Pmc1008mpAlmNextColdBootForced_Object = MibScalar
pmc1008mpAlmNextColdBootForced = _Pmc1008mpAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 194, 2),
    _Pmc1008mpAlmNextColdBootForced_Type()
)
pmc1008mpAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmNextColdBootForced.setStatus("current")
_Pmc1008mpAlmBootUndone_Type = EkiOnOff
_Pmc1008mpAlmBootUndone_Object = MibScalar
pmc1008mpAlmBootUndone = _Pmc1008mpAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 194, 3),
    _Pmc1008mpAlmBootUndone_Type()
)
pmc1008mpAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmBootUndone.setStatus("current")
_Pmc1008mpAlmResetHwInitFail_Type = EkiOnOff
_Pmc1008mpAlmResetHwInitFail_Object = MibScalar
pmc1008mpAlmResetHwInitFail = _Pmc1008mpAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 194, 4),
    _Pmc1008mpAlmResetHwInitFail_Type()
)
pmc1008mpAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmResetHwInitFail.setStatus("current")
_Pmc1008mpAlmSwInitFail_Type = EkiOnOff
_Pmc1008mpAlmSwInitFail_Object = MibScalar
pmc1008mpAlmSwInitFail = _Pmc1008mpAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 194, 5),
    _Pmc1008mpAlmSwInitFail_Type()
)
pmc1008mpAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmSwInitFail.setStatus("current")
_Pmc1008mpAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pmc1008mpAlmmodInitFailLevel3 = _Pmc1008mpAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195)
)
_Pmc1008mpAlmGwIdentFail_Type = EkiOnOff
_Pmc1008mpAlmGwIdentFail_Object = MibScalar
pmc1008mpAlmGwIdentFail = _Pmc1008mpAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 1),
    _Pmc1008mpAlmGwIdentFail_Type()
)
pmc1008mpAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmGwIdentFail.setStatus("current")
_Pmc1008mpAlmObmTypeReadFail_Type = EkiOnOff
_Pmc1008mpAlmObmTypeReadFail_Object = MibScalar
pmc1008mpAlmObmTypeReadFail = _Pmc1008mpAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 2),
    _Pmc1008mpAlmObmTypeReadFail_Type()
)
pmc1008mpAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmObmTypeReadFail.setStatus("current")
_Pmc1008mpAlmInitModuleFail_Type = EkiOnOff
_Pmc1008mpAlmInitModuleFail_Object = MibScalar
pmc1008mpAlmInitModuleFail = _Pmc1008mpAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 3),
    _Pmc1008mpAlmInitModuleFail_Type()
)
pmc1008mpAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmInitModuleFail.setStatus("current")
_Pmc1008mpAlmXfp1InitFail_Type = EkiOnOff
_Pmc1008mpAlmXfp1InitFail_Object = MibScalar
pmc1008mpAlmXfp1InitFail = _Pmc1008mpAlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 5),
    _Pmc1008mpAlmXfp1InitFail_Type()
)
pmc1008mpAlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmXfp1InitFail.setStatus("current")
_Pmc1008mpAlmXfp2InitFail_Type = EkiOnOff
_Pmc1008mpAlmXfp2InitFail_Object = MibScalar
pmc1008mpAlmXfp2InitFail = _Pmc1008mpAlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 6),
    _Pmc1008mpAlmXfp2InitFail_Type()
)
pmc1008mpAlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmXfp2InitFail.setStatus("current")
_Pmc1008mpAlmLine1InitFail_Type = EkiOnOff
_Pmc1008mpAlmLine1InitFail_Object = MibScalar
pmc1008mpAlmLine1InitFail = _Pmc1008mpAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 7),
    _Pmc1008mpAlmLine1InitFail_Type()
)
pmc1008mpAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLine1InitFail.setStatus("current")
_Pmc1008mpAlmLine2InitFail_Type = EkiOnOff
_Pmc1008mpAlmLine2InitFail_Object = MibScalar
pmc1008mpAlmLine2InitFail = _Pmc1008mpAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 8),
    _Pmc1008mpAlmLine2InitFail_Type()
)
pmc1008mpAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLine2InitFail.setStatus("current")
_Pmc1008mpAlmClient1InitFail_Type = EkiOnOff
_Pmc1008mpAlmClient1InitFail_Object = MibScalar
pmc1008mpAlmClient1InitFail = _Pmc1008mpAlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 9),
    _Pmc1008mpAlmClient1InitFail_Type()
)
pmc1008mpAlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClient1InitFail.setStatus("current")
_Pmc1008mpAlmClient2InitFail_Type = EkiOnOff
_Pmc1008mpAlmClient2InitFail_Object = MibScalar
pmc1008mpAlmClient2InitFail = _Pmc1008mpAlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 10),
    _Pmc1008mpAlmClient2InitFail_Type()
)
pmc1008mpAlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClient2InitFail.setStatus("current")
_Pmc1008mpAlmClient3InitFail_Type = EkiOnOff
_Pmc1008mpAlmClient3InitFail_Object = MibScalar
pmc1008mpAlmClient3InitFail = _Pmc1008mpAlmClient3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 11),
    _Pmc1008mpAlmClient3InitFail_Type()
)
pmc1008mpAlmClient3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClient3InitFail.setStatus("current")
_Pmc1008mpAlmClient4InitFail_Type = EkiOnOff
_Pmc1008mpAlmClient4InitFail_Object = MibScalar
pmc1008mpAlmClient4InitFail = _Pmc1008mpAlmClient4InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 12),
    _Pmc1008mpAlmClient4InitFail_Type()
)
pmc1008mpAlmClient4InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClient4InitFail.setStatus("current")
_Pmc1008mpAlmClient5InitFail_Type = EkiOnOff
_Pmc1008mpAlmClient5InitFail_Object = MibScalar
pmc1008mpAlmClient5InitFail = _Pmc1008mpAlmClient5InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 13),
    _Pmc1008mpAlmClient5InitFail_Type()
)
pmc1008mpAlmClient5InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClient5InitFail.setStatus("current")
_Pmc1008mpAlmClient6InitFail_Type = EkiOnOff
_Pmc1008mpAlmClient6InitFail_Object = MibScalar
pmc1008mpAlmClient6InitFail = _Pmc1008mpAlmClient6InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 14),
    _Pmc1008mpAlmClient6InitFail_Type()
)
pmc1008mpAlmClient6InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClient6InitFail.setStatus("current")
_Pmc1008mpAlmClient7InitFail_Type = EkiOnOff
_Pmc1008mpAlmClient7InitFail_Object = MibScalar
pmc1008mpAlmClient7InitFail = _Pmc1008mpAlmClient7InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 15),
    _Pmc1008mpAlmClient7InitFail_Type()
)
pmc1008mpAlmClient7InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClient7InitFail.setStatus("current")
_Pmc1008mpAlmClient8InitFail_Type = EkiOnOff
_Pmc1008mpAlmClient8InitFail_Object = MibScalar
pmc1008mpAlmClient8InitFail = _Pmc1008mpAlmClient8InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 195, 16),
    _Pmc1008mpAlmClient8InitFail_Type()
)
pmc1008mpAlmClient8InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClient8InitFail.setStatus("current")
_Pmc1008mpAlmadddropTsClientRxProt_ObjectIdentity = ObjectIdentity
pmc1008mpAlmadddropTsClientRxProt = _Pmc1008mpAlmadddropTsClientRxProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198)
)
_Pmc1008mpAlmAdddropClient1West_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient1West_Object = MibScalar
pmc1008mpAlmAdddropClient1West = _Pmc1008mpAlmAdddropClient1West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 1),
    _Pmc1008mpAlmAdddropClient1West_Type()
)
pmc1008mpAlmAdddropClient1West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient1West.setStatus("current")
_Pmc1008mpAlmAdddropClient2West_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient2West_Object = MibScalar
pmc1008mpAlmAdddropClient2West = _Pmc1008mpAlmAdddropClient2West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 2),
    _Pmc1008mpAlmAdddropClient2West_Type()
)
pmc1008mpAlmAdddropClient2West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient2West.setStatus("current")
_Pmc1008mpAlmAdddropClient3West_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient3West_Object = MibScalar
pmc1008mpAlmAdddropClient3West = _Pmc1008mpAlmAdddropClient3West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 3),
    _Pmc1008mpAlmAdddropClient3West_Type()
)
pmc1008mpAlmAdddropClient3West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient3West.setStatus("current")
_Pmc1008mpAlmAdddropClient4West_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient4West_Object = MibScalar
pmc1008mpAlmAdddropClient4West = _Pmc1008mpAlmAdddropClient4West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 4),
    _Pmc1008mpAlmAdddropClient4West_Type()
)
pmc1008mpAlmAdddropClient4West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient4West.setStatus("current")
_Pmc1008mpAlmAdddropClient5West_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient5West_Object = MibScalar
pmc1008mpAlmAdddropClient5West = _Pmc1008mpAlmAdddropClient5West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 5),
    _Pmc1008mpAlmAdddropClient5West_Type()
)
pmc1008mpAlmAdddropClient5West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient5West.setStatus("current")
_Pmc1008mpAlmAdddropClient6West_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient6West_Object = MibScalar
pmc1008mpAlmAdddropClient6West = _Pmc1008mpAlmAdddropClient6West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 6),
    _Pmc1008mpAlmAdddropClient6West_Type()
)
pmc1008mpAlmAdddropClient6West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient6West.setStatus("current")
_Pmc1008mpAlmAdddropClient7West_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient7West_Object = MibScalar
pmc1008mpAlmAdddropClient7West = _Pmc1008mpAlmAdddropClient7West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 7),
    _Pmc1008mpAlmAdddropClient7West_Type()
)
pmc1008mpAlmAdddropClient7West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient7West.setStatus("current")
_Pmc1008mpAlmAdddropClient8West_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient8West_Object = MibScalar
pmc1008mpAlmAdddropClient8West = _Pmc1008mpAlmAdddropClient8West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 8),
    _Pmc1008mpAlmAdddropClient8West_Type()
)
pmc1008mpAlmAdddropClient8West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient8West.setStatus("current")
_Pmc1008mpAlmAdddropClient1East_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient1East_Object = MibScalar
pmc1008mpAlmAdddropClient1East = _Pmc1008mpAlmAdddropClient1East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 9),
    _Pmc1008mpAlmAdddropClient1East_Type()
)
pmc1008mpAlmAdddropClient1East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient1East.setStatus("current")
_Pmc1008mpAlmAdddropClient2East_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient2East_Object = MibScalar
pmc1008mpAlmAdddropClient2East = _Pmc1008mpAlmAdddropClient2East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 10),
    _Pmc1008mpAlmAdddropClient2East_Type()
)
pmc1008mpAlmAdddropClient2East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient2East.setStatus("current")
_Pmc1008mpAlmAdddropClient3East_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient3East_Object = MibScalar
pmc1008mpAlmAdddropClient3East = _Pmc1008mpAlmAdddropClient3East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 11),
    _Pmc1008mpAlmAdddropClient3East_Type()
)
pmc1008mpAlmAdddropClient3East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient3East.setStatus("current")
_Pmc1008mpAlmAdddropClient4East_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient4East_Object = MibScalar
pmc1008mpAlmAdddropClient4East = _Pmc1008mpAlmAdddropClient4East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 12),
    _Pmc1008mpAlmAdddropClient4East_Type()
)
pmc1008mpAlmAdddropClient4East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient4East.setStatus("current")
_Pmc1008mpAlmAdddropClient5East_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient5East_Object = MibScalar
pmc1008mpAlmAdddropClient5East = _Pmc1008mpAlmAdddropClient5East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 13),
    _Pmc1008mpAlmAdddropClient5East_Type()
)
pmc1008mpAlmAdddropClient5East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient5East.setStatus("current")
_Pmc1008mpAlmAdddropClient6East_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient6East_Object = MibScalar
pmc1008mpAlmAdddropClient6East = _Pmc1008mpAlmAdddropClient6East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 14),
    _Pmc1008mpAlmAdddropClient6East_Type()
)
pmc1008mpAlmAdddropClient6East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient6East.setStatus("current")
_Pmc1008mpAlmAdddropClient7East_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient7East_Object = MibScalar
pmc1008mpAlmAdddropClient7East = _Pmc1008mpAlmAdddropClient7East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 15),
    _Pmc1008mpAlmAdddropClient7East_Type()
)
pmc1008mpAlmAdddropClient7East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient7East.setStatus("current")
_Pmc1008mpAlmAdddropClient8East_Type = EkiOnOff
_Pmc1008mpAlmAdddropClient8East_Object = MibScalar
pmc1008mpAlmAdddropClient8East = _Pmc1008mpAlmAdddropClient8East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 2, 198, 16),
    _Pmc1008mpAlmAdddropClient8East_Type()
)
pmc1008mpAlmAdddropClient8East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmAdddropClient8East.setStatus("current")
_Pmc1008mpAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmc1008mpAlmOtherCrit = _Pmc1008mpAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 3)
)
_Pmc1008mpAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmc1008mpAlmsynthAlm0 = _Pmc1008mpAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 3, 0)
)
_Pmc1008mpAlmModGlobFail_Type = EkiOnOff
_Pmc1008mpAlmModGlobFail_Object = MibScalar
pmc1008mpAlmModGlobFail = _Pmc1008mpAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 3, 0, 9),
    _Pmc1008mpAlmModGlobFail_Type()
)
pmc1008mpAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmModGlobFail.setStatus("current")
_Pmc1008mpAlmDefFuseA_Type = EkiOnOff
_Pmc1008mpAlmDefFuseA_Object = MibScalar
pmc1008mpAlmDefFuseA = _Pmc1008mpAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 3, 0, 15),
    _Pmc1008mpAlmDefFuseA_Type()
)
pmc1008mpAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDefFuseA.setStatus("current")
_Pmc1008mpAlmDefFuseB_Type = EkiOnOff
_Pmc1008mpAlmDefFuseB_Object = MibScalar
pmc1008mpAlmDefFuseB = _Pmc1008mpAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 1, 3, 0, 16),
    _Pmc1008mpAlmDefFuseB_Type()
)
pmc1008mpAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDefFuseB.setStatus("current")
_Pmc1008mpAlmClient_ObjectIdentity = ObjectIdentity
pmc1008mpAlmClient = _Pmc1008mpAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2)
)
_Pmc1008mpAlmClientNurg_ObjectIdentity = ObjectIdentity
pmc1008mpAlmClientNurg = _Pmc1008mpAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1)
)
_Pmc1008mpAlmsfpWarnDdmTable_Object = MibTable
pmc1008mpAlmsfpWarnDdmTable = _Pmc1008mpAlmsfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmsfpWarnDdmTable.setStatus("current")
_Pmc1008mpAlmsfpWarnDdmEntry_Object = MibTableRow
pmc1008mpAlmsfpWarnDdmEntry = _Pmc1008mpAlmsfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1)
)
pmc1008mpAlmsfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmsfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmsfpWarnDdmEntry.setStatus("current")


class _Pmc1008mpAlmsfpWarnDdmIndex_Type(Integer32):
    """Custom type pmc1008mpAlmsfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmsfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmsfpWarnDdmIndex_Object = MibTableColumn
pmc1008mpAlmsfpWarnDdmIndex = _Pmc1008mpAlmsfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 1),
    _Pmc1008mpAlmsfpWarnDdmIndex_Type()
)
pmc1008mpAlmsfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmsfpWarnDdmIndex.setStatus("current")
_Pmc1008mpAlmTxPwLowWngPortn_Type = EkiOnOff
_Pmc1008mpAlmTxPwLowWngPortn_Object = MibTableColumn
pmc1008mpAlmTxPwLowWngPortn = _Pmc1008mpAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 2),
    _Pmc1008mpAlmTxPwLowWngPortn_Type()
)
pmc1008mpAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxPwLowWngPortn.setStatus("current")
_Pmc1008mpAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pmc1008mpAlmTxPwrHighWngPortn_Object = MibTableColumn
pmc1008mpAlmTxPwrHighWngPortn = _Pmc1008mpAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 3),
    _Pmc1008mpAlmTxPwrHighWngPortn_Type()
)
pmc1008mpAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxPwrHighWngPortn.setStatus("current")
_Pmc1008mpAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pmc1008mpAlmTxBiasLowWngPortn_Object = MibTableColumn
pmc1008mpAlmTxBiasLowWngPortn = _Pmc1008mpAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 4),
    _Pmc1008mpAlmTxBiasLowWngPortn_Type()
)
pmc1008mpAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxBiasLowWngPortn.setStatus("current")
_Pmc1008mpAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pmc1008mpAlmTxBiasHighWngPortn_Object = MibTableColumn
pmc1008mpAlmTxBiasHighWngPortn = _Pmc1008mpAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 5),
    _Pmc1008mpAlmTxBiasHighWngPortn_Type()
)
pmc1008mpAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxBiasHighWngPortn.setStatus("current")
_Pmc1008mpAlmVccLowWngPortn_Type = EkiOnOff
_Pmc1008mpAlmVccLowWngPortn_Object = MibTableColumn
pmc1008mpAlmVccLowWngPortn = _Pmc1008mpAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 6),
    _Pmc1008mpAlmVccLowWngPortn_Type()
)
pmc1008mpAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVccLowWngPortn.setStatus("current")
_Pmc1008mpAlmVccHighWngPortn_Type = EkiOnOff
_Pmc1008mpAlmVccHighWngPortn_Object = MibTableColumn
pmc1008mpAlmVccHighWngPortn = _Pmc1008mpAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 7),
    _Pmc1008mpAlmVccHighWngPortn_Type()
)
pmc1008mpAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVccHighWngPortn.setStatus("current")
_Pmc1008mpAlmTempLowWngPortn_Type = EkiOnOff
_Pmc1008mpAlmTempLowWngPortn_Object = MibTableColumn
pmc1008mpAlmTempLowWngPortn = _Pmc1008mpAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 8),
    _Pmc1008mpAlmTempLowWngPortn_Type()
)
pmc1008mpAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTempLowWngPortn.setStatus("current")
_Pmc1008mpAlmTempHighWngPortn_Type = EkiOnOff
_Pmc1008mpAlmTempHighWngPortn_Object = MibTableColumn
pmc1008mpAlmTempHighWngPortn = _Pmc1008mpAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 9),
    _Pmc1008mpAlmTempHighWngPortn_Type()
)
pmc1008mpAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTempHighWngPortn.setStatus("current")
_Pmc1008mpAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pmc1008mpAlmRxPwrLowWngPortn_Object = MibTableColumn
pmc1008mpAlmRxPwrLowWngPortn = _Pmc1008mpAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 16),
    _Pmc1008mpAlmRxPwrLowWngPortn_Type()
)
pmc1008mpAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxPwrLowWngPortn.setStatus("current")
_Pmc1008mpAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pmc1008mpAlmRxPwrHighWngPortn_Object = MibTableColumn
pmc1008mpAlmRxPwrHighWngPortn = _Pmc1008mpAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 1, 48, 1, 17),
    _Pmc1008mpAlmRxPwrHighWngPortn_Type()
)
pmc1008mpAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxPwrHighWngPortn.setStatus("current")
_Pmc1008mpAlmClientUrg_ObjectIdentity = ObjectIdentity
pmc1008mpAlmClientUrg = _Pmc1008mpAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2)
)
_Pmc1008mpAlmsfpAlmDdmTable_Object = MibTable
pmc1008mpAlmsfpAlmDdmTable = _Pmc1008mpAlmsfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmsfpAlmDdmTable.setStatus("current")
_Pmc1008mpAlmsfpAlmDdmEntry_Object = MibTableRow
pmc1008mpAlmsfpAlmDdmEntry = _Pmc1008mpAlmsfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1)
)
pmc1008mpAlmsfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmsfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmsfpAlmDdmEntry.setStatus("current")


class _Pmc1008mpAlmsfpAlmDdmIndex_Type(Integer32):
    """Custom type pmc1008mpAlmsfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmsfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmsfpAlmDdmIndex_Object = MibTableColumn
pmc1008mpAlmsfpAlmDdmIndex = _Pmc1008mpAlmsfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 1),
    _Pmc1008mpAlmsfpAlmDdmIndex_Type()
)
pmc1008mpAlmsfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmsfpAlmDdmIndex.setStatus("current")
_Pmc1008mpAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmTxPwrLowAlaPortn_Object = MibTableColumn
pmc1008mpAlmTxPwrLowAlaPortn = _Pmc1008mpAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 2),
    _Pmc1008mpAlmTxPwrLowAlaPortn_Type()
)
pmc1008mpAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxPwrLowAlaPortn.setStatus("current")
_Pmc1008mpAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmTxPwrHighAlaPortn_Object = MibTableColumn
pmc1008mpAlmTxPwrHighAlaPortn = _Pmc1008mpAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 3),
    _Pmc1008mpAlmTxPwrHighAlaPortn_Type()
)
pmc1008mpAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxPwrHighAlaPortn.setStatus("current")
_Pmc1008mpAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmTxBiasLowAlaPortn_Object = MibTableColumn
pmc1008mpAlmTxBiasLowAlaPortn = _Pmc1008mpAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 4),
    _Pmc1008mpAlmTxBiasLowAlaPortn_Type()
)
pmc1008mpAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxBiasLowAlaPortn.setStatus("current")
_Pmc1008mpAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmTxBiasHighAlaPortn_Object = MibTableColumn
pmc1008mpAlmTxBiasHighAlaPortn = _Pmc1008mpAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 5),
    _Pmc1008mpAlmTxBiasHighAlaPortn_Type()
)
pmc1008mpAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxBiasHighAlaPortn.setStatus("current")
_Pmc1008mpAlmVccLowAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmVccLowAlaPortn_Object = MibTableColumn
pmc1008mpAlmVccLowAlaPortn = _Pmc1008mpAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 6),
    _Pmc1008mpAlmVccLowAlaPortn_Type()
)
pmc1008mpAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVccLowAlaPortn.setStatus("current")
_Pmc1008mpAlmVccHighAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmVccHighAlaPortn_Object = MibTableColumn
pmc1008mpAlmVccHighAlaPortn = _Pmc1008mpAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 7),
    _Pmc1008mpAlmVccHighAlaPortn_Type()
)
pmc1008mpAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVccHighAlaPortn.setStatus("current")
_Pmc1008mpAlmTempLowAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmTempLowAlaPortn_Object = MibTableColumn
pmc1008mpAlmTempLowAlaPortn = _Pmc1008mpAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 8),
    _Pmc1008mpAlmTempLowAlaPortn_Type()
)
pmc1008mpAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTempLowAlaPortn.setStatus("current")
_Pmc1008mpAlmTempHighAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmTempHighAlaPortn_Object = MibTableColumn
pmc1008mpAlmTempHighAlaPortn = _Pmc1008mpAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 9),
    _Pmc1008mpAlmTempHighAlaPortn_Type()
)
pmc1008mpAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTempHighAlaPortn.setStatus("current")
_Pmc1008mpAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmRxPwrLowAlaPortn_Object = MibTableColumn
pmc1008mpAlmRxPwrLowAlaPortn = _Pmc1008mpAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 16),
    _Pmc1008mpAlmRxPwrLowAlaPortn_Type()
)
pmc1008mpAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxPwrLowAlaPortn.setStatus("current")
_Pmc1008mpAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmRxPwrHighAlaPortn_Object = MibTableColumn
pmc1008mpAlmRxPwrHighAlaPortn = _Pmc1008mpAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 2, 32, 1, 17),
    _Pmc1008mpAlmRxPwrHighAlaPortn_Type()
)
pmc1008mpAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxPwrHighAlaPortn.setStatus("current")
_Pmc1008mpAlmClientCrit_ObjectIdentity = ObjectIdentity
pmc1008mpAlmClientCrit = _Pmc1008mpAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3)
)
_Pmc1008mpAlmsynthAlmPortTable_Object = MibTable
pmc1008mpAlmsynthAlmPortTable = _Pmc1008mpAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmsynthAlmPortTable.setStatus("current")
_Pmc1008mpAlmsynthAlmPortEntry_Object = MibTableRow
pmc1008mpAlmsynthAlmPortEntry = _Pmc1008mpAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1)
)
pmc1008mpAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmsynthAlmPortEntry.setStatus("current")


class _Pmc1008mpAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pmc1008mpAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmsynthAlmPortIndex_Object = MibTableColumn
pmc1008mpAlmsynthAlmPortIndex = _Pmc1008mpAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 1),
    _Pmc1008mpAlmsynthAlmPortIndex_Type()
)
pmc1008mpAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmsynthAlmPortIndex.setStatus("current")
_Pmc1008mpAlmSfpAbsentPortn_Type = EkiOnOff
_Pmc1008mpAlmSfpAbsentPortn_Object = MibTableColumn
pmc1008mpAlmSfpAbsentPortn = _Pmc1008mpAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 2),
    _Pmc1008mpAlmSfpAbsentPortn_Type()
)
pmc1008mpAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmSfpAbsentPortn.setStatus("current")
_Pmc1008mpAlmDdmAbsentPortn_Type = EkiOnOff
_Pmc1008mpAlmDdmAbsentPortn_Object = MibTableColumn
pmc1008mpAlmDdmAbsentPortn = _Pmc1008mpAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 3),
    _Pmc1008mpAlmDdmAbsentPortn_Type()
)
pmc1008mpAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDdmAbsentPortn.setStatus("current")
_Pmc1008mpAlmHwFailAccPortn_Type = EkiOnOff
_Pmc1008mpAlmHwFailAccPortn_Object = MibTableColumn
pmc1008mpAlmHwFailAccPortn = _Pmc1008mpAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 5),
    _Pmc1008mpAlmHwFailAccPortn_Type()
)
pmc1008mpAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmHwFailAccPortn.setStatus("current")
_Pmc1008mpAlmDwLsdPortn_Type = EkiOnOff
_Pmc1008mpAlmDwLsdPortn_Object = MibTableColumn
pmc1008mpAlmDwLsdPortn = _Pmc1008mpAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 6),
    _Pmc1008mpAlmDwLsdPortn_Type()
)
pmc1008mpAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwLsdPortn.setStatus("current")
_Pmc1008mpAlmClientLocalOosPortn_Type = EkiOnOff
_Pmc1008mpAlmClientLocalOosPortn_Object = MibTableColumn
pmc1008mpAlmClientLocalOosPortn = _Pmc1008mpAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 7),
    _Pmc1008mpAlmClientLocalOosPortn_Type()
)
pmc1008mpAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClientLocalOosPortn.setStatus("current")
_Pmc1008mpAlmClientRemoteOosPortn_Type = EkiOnOff
_Pmc1008mpAlmClientRemoteOosPortn_Object = MibTableColumn
pmc1008mpAlmClientRemoteOosPortn = _Pmc1008mpAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 8),
    _Pmc1008mpAlmClientRemoteOosPortn_Type()
)
pmc1008mpAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClientRemoteOosPortn.setStatus("current")
_Pmc1008mpAlmDwCaisPortn_Type = EkiOnOff
_Pmc1008mpAlmDwCaisPortn_Object = MibTableColumn
pmc1008mpAlmDwCaisPortn = _Pmc1008mpAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 9),
    _Pmc1008mpAlmDwCaisPortn_Type()
)
pmc1008mpAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwCaisPortn.setStatus("current")
_Pmc1008mpAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmSfpDdmWarningPortn_Object = MibTableColumn
pmc1008mpAlmSfpDdmWarningPortn = _Pmc1008mpAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 10),
    _Pmc1008mpAlmSfpDdmWarningPortn_Type()
)
pmc1008mpAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmSfpDdmWarningPortn.setStatus("current")
_Pmc1008mpAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pmc1008mpAlmSfpDdmAlmPortn_Object = MibTableColumn
pmc1008mpAlmSfpDdmAlmPortn = _Pmc1008mpAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 11),
    _Pmc1008mpAlmSfpDdmAlmPortn_Type()
)
pmc1008mpAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmSfpDdmAlmPortn.setStatus("current")
_Pmc1008mpAlmFailAccPortn_Type = EkiOnOff
_Pmc1008mpAlmFailAccPortn_Object = MibTableColumn
pmc1008mpAlmFailAccPortn = _Pmc1008mpAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 13),
    _Pmc1008mpAlmFailAccPortn_Type()
)
pmc1008mpAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmFailAccPortn.setStatus("current")
_Pmc1008mpAlmClientActivePortn_Type = EkiOnOff
_Pmc1008mpAlmClientActivePortn_Object = MibTableColumn
pmc1008mpAlmClientActivePortn = _Pmc1008mpAlmClientActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 16),
    _Pmc1008mpAlmClientActivePortn_Type()
)
pmc1008mpAlmClientActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmClientActivePortn.setStatus("current")
_Pmc1008mpAlmUpCsfPortn_Type = EkiOnOff
_Pmc1008mpAlmUpCsfPortn_Object = MibTableColumn
pmc1008mpAlmUpCsfPortn = _Pmc1008mpAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 8, 1, 17),
    _Pmc1008mpAlmUpCsfPortn_Type()
)
pmc1008mpAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmUpCsfPortn.setStatus("current")
_Pmc1008mpAlmaccessioAlmTable_Object = MibTable
pmc1008mpAlmaccessioAlmTable = _Pmc1008mpAlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmaccessioAlmTable.setStatus("current")
_Pmc1008mpAlmaccessioAlmEntry_Object = MibTableRow
pmc1008mpAlmaccessioAlmEntry = _Pmc1008mpAlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 16, 1)
)
pmc1008mpAlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmaccessioAlmEntry.setStatus("current")


class _Pmc1008mpAlmaccessioAlmIndex_Type(Integer32):
    """Custom type pmc1008mpAlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmaccessioAlmIndex_Object = MibTableColumn
pmc1008mpAlmaccessioAlmIndex = _Pmc1008mpAlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 16, 1, 1),
    _Pmc1008mpAlmaccessioAlmIndex_Type()
)
pmc1008mpAlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmaccessioAlmIndex.setStatus("current")
_Pmc1008mpAlmDwLasFailPortn_Type = EkiOnOff
_Pmc1008mpAlmDwLasFailPortn_Object = MibTableColumn
pmc1008mpAlmDwLasFailPortn = _Pmc1008mpAlmDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 16, 1, 2),
    _Pmc1008mpAlmDwLasFailPortn_Type()
)
pmc1008mpAlmDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwLasFailPortn.setStatus("current")
_Pmc1008mpAlmUpLosPortn_Type = EkiOnOff
_Pmc1008mpAlmUpLosPortn_Object = MibTableColumn
pmc1008mpAlmUpLosPortn = _Pmc1008mpAlmUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 16, 1, 5),
    _Pmc1008mpAlmUpLosPortn_Type()
)
pmc1008mpAlmUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmUpLosPortn.setStatus("current")
_Pmc1008mpAlmmapperDeAlmTable_Object = MibTable
pmc1008mpAlmmapperDeAlmTable = _Pmc1008mpAlmmapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmmapperDeAlmTable.setStatus("current")
_Pmc1008mpAlmmapperDeAlmEntry_Object = MibTableRow
pmc1008mpAlmmapperDeAlmEntry = _Pmc1008mpAlmmapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 72, 1)
)
pmc1008mpAlmmapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmmapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmmapperDeAlmEntry.setStatus("current")


class _Pmc1008mpAlmmapperDeAlmIndex_Type(Integer32):
    """Custom type pmc1008mpAlmmapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmmapperDeAlmIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmmapperDeAlmIndex_Object = MibTableColumn
pmc1008mpAlmmapperDeAlmIndex = _Pmc1008mpAlmmapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 72, 1, 1),
    _Pmc1008mpAlmmapperDeAlmIndex_Type()
)
pmc1008mpAlmmapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmmapperDeAlmIndex.setStatus("current")
_Pmc1008mpAlmUpAccOosPortn_Type = EkiOnOff
_Pmc1008mpAlmUpAccOosPortn_Object = MibTableColumn
pmc1008mpAlmUpAccOosPortn = _Pmc1008mpAlmUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 72, 1, 2),
    _Pmc1008mpAlmUpAccOosPortn_Type()
)
pmc1008mpAlmUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmUpAccOosPortn.setStatus("current")
_Pmc1008mpAlmUpBufferOvlPortn_Type = EkiOnOff
_Pmc1008mpAlmUpBufferOvlPortn_Object = MibTableColumn
pmc1008mpAlmUpBufferOvlPortn = _Pmc1008mpAlmUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 72, 1, 11),
    _Pmc1008mpAlmUpBufferOvlPortn_Type()
)
pmc1008mpAlmUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmUpBufferOvlPortn.setStatus("current")
_Pmc1008mpAlmDwCsfDetPortn_Type = EkiOnOff
_Pmc1008mpAlmDwCsfDetPortn_Object = MibTableColumn
pmc1008mpAlmDwCsfDetPortn = _Pmc1008mpAlmDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 72, 1, 12),
    _Pmc1008mpAlmDwCsfDetPortn_Type()
)
pmc1008mpAlmDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwCsfDetPortn.setStatus("current")
_Pmc1008mpAlmDwBufferOvlPortn_Type = EkiOnOff
_Pmc1008mpAlmDwBufferOvlPortn_Object = MibTableColumn
pmc1008mpAlmDwBufferOvlPortn = _Pmc1008mpAlmDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 2, 3, 72, 1, 15),
    _Pmc1008mpAlmDwBufferOvlPortn_Type()
)
pmc1008mpAlmDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwBufferOvlPortn.setStatus("current")
_Pmc1008mpAlmLine_ObjectIdentity = ObjectIdentity
pmc1008mpAlmLine = _Pmc1008mpAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3)
)
_Pmc1008mpAlmLineNurg_ObjectIdentity = ObjectIdentity
pmc1008mpAlmLineNurg = _Pmc1008mpAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1)
)
_Pmc1008mpAlmlineXfp1WarningsTable_Object = MibTable
pmc1008mpAlmlineXfp1WarningsTable = _Pmc1008mpAlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1WarningsTable.setStatus("current")
_Pmc1008mpAlmlineXfp1WarningsEntry_Object = MibTableRow
pmc1008mpAlmlineXfp1WarningsEntry = _Pmc1008mpAlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1)
)
pmc1008mpAlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1WarningsEntry.setStatus("current")


class _Pmc1008mpAlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pmc1008mpAlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmlineXfp1WarningsIndex_Object = MibTableColumn
pmc1008mpAlmlineXfp1WarningsIndex = _Pmc1008mpAlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1, 1),
    _Pmc1008mpAlmlineXfp1WarningsIndex_Type()
)
pmc1008mpAlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1WarningsIndex.setStatus("current")
_Pmc1008mpAlmTxPowerLowWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmTxPowerLowWarningPortn_Object = MibTableColumn
pmc1008mpAlmTxPowerLowWarningPortn = _Pmc1008mpAlmTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1, 2),
    _Pmc1008mpAlmTxPowerLowWarningPortn_Type()
)
pmc1008mpAlmTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxPowerLowWarningPortn.setStatus("current")
_Pmc1008mpAlmTxPowerHighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmTxPowerHighWarningPortn_Object = MibTableColumn
pmc1008mpAlmTxPowerHighWarningPortn = _Pmc1008mpAlmTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1, 3),
    _Pmc1008mpAlmTxPowerHighWarningPortn_Type()
)
pmc1008mpAlmTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxPowerHighWarningPortn.setStatus("current")
_Pmc1008mpAlmTxBiasLowWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmTxBiasLowWarningPortn_Object = MibTableColumn
pmc1008mpAlmTxBiasLowWarningPortn = _Pmc1008mpAlmTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1, 4),
    _Pmc1008mpAlmTxBiasLowWarningPortn_Type()
)
pmc1008mpAlmTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxBiasLowWarningPortn.setStatus("current")
_Pmc1008mpAlmTxBiasHighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmTxBiasHighWarningPortn_Object = MibTableColumn
pmc1008mpAlmTxBiasHighWarningPortn = _Pmc1008mpAlmTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1, 5),
    _Pmc1008mpAlmTxBiasHighWarningPortn_Type()
)
pmc1008mpAlmTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxBiasHighWarningPortn.setStatus("current")
_Pmc1008mpAlmTempLowWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmTempLowWarningPortn_Object = MibTableColumn
pmc1008mpAlmTempLowWarningPortn = _Pmc1008mpAlmTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1, 8),
    _Pmc1008mpAlmTempLowWarningPortn_Type()
)
pmc1008mpAlmTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTempLowWarningPortn.setStatus("current")
_Pmc1008mpAlmTempHighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmTempHighWarningPortn_Object = MibTableColumn
pmc1008mpAlmTempHighWarningPortn = _Pmc1008mpAlmTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1, 9),
    _Pmc1008mpAlmTempHighWarningPortn_Type()
)
pmc1008mpAlmTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTempHighWarningPortn.setStatus("current")
_Pmc1008mpAlmRxPowerLowWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmRxPowerLowWarningPortn_Object = MibTableColumn
pmc1008mpAlmRxPowerLowWarningPortn = _Pmc1008mpAlmRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1, 16),
    _Pmc1008mpAlmRxPowerLowWarningPortn_Type()
)
pmc1008mpAlmRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxPowerLowWarningPortn.setStatus("current")
_Pmc1008mpAlmRxPowerHighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmRxPowerHighWarningPortn_Object = MibTableColumn
pmc1008mpAlmRxPowerHighWarningPortn = _Pmc1008mpAlmRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 209, 1, 17),
    _Pmc1008mpAlmRxPowerHighWarningPortn_Type()
)
pmc1008mpAlmRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxPowerHighWarningPortn.setStatus("current")
_Pmc1008mpAlmlineOtx1TlhWarningsTable_Object = MibTable
pmc1008mpAlmlineOtx1TlhWarningsTable = _Pmc1008mpAlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineOtx1TlhWarningsTable.setStatus("current")
_Pmc1008mpAlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pmc1008mpAlmlineOtx1TlhWarningsEntry = _Pmc1008mpAlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 225, 1)
)
pmc1008mpAlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pmc1008mpAlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pmc1008mpAlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pmc1008mpAlmlineOtx1TlhWarningsIndex = _Pmc1008mpAlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 225, 1, 1),
    _Pmc1008mpAlmlineOtx1TlhWarningsIndex_Type()
)
pmc1008mpAlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pmc1008mpAlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pmc1008mpAlmLineModulatorAgingHighWarningPortn = _Pmc1008mpAlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 225, 1, 6),
    _Pmc1008mpAlmLineModulatorAgingHighWarningPortn_Type()
)
pmc1008mpAlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pmc1008mpAlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmLineAgingHighWarningPortn_Object = MibTableColumn
pmc1008mpAlmLineAgingHighWarningPortn = _Pmc1008mpAlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 225, 1, 7),
    _Pmc1008mpAlmLineAgingHighWarningPortn_Type()
)
pmc1008mpAlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineAgingHighWarningPortn.setStatus("current")
_Pmc1008mpAlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pmc1008mpAlmLineFreqDevHighWarningPortn = _Pmc1008mpAlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 225, 1, 13),
    _Pmc1008mpAlmLineFreqDevHighWarningPortn_Type()
)
pmc1008mpAlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineFreqDevHighWarningPortn.setStatus("current")
_Pmc1008mpAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pmc1008mpAlmLineLaserTempHighWarningPortn = _Pmc1008mpAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 1, 225, 1, 15),
    _Pmc1008mpAlmLineLaserTempHighWarningPortn_Type()
)
pmc1008mpAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pmc1008mpAlmLineUrg_ObjectIdentity = ObjectIdentity
pmc1008mpAlmLineUrg = _Pmc1008mpAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2)
)
_Pmc1008mpAlmdfrmBerTable_Object = MibTable
pmc1008mpAlmdfrmBerTable = _Pmc1008mpAlmdfrmBerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 129)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmdfrmBerTable.setStatus("current")
_Pmc1008mpAlmdfrmBerEntry_Object = MibTableRow
pmc1008mpAlmdfrmBerEntry = _Pmc1008mpAlmdfrmBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 129, 1)
)
pmc1008mpAlmdfrmBerEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmdfrmBerIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmdfrmBerEntry.setStatus("current")


class _Pmc1008mpAlmdfrmBerIndex_Type(Integer32):
    """Custom type pmc1008mpAlmdfrmBerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmdfrmBerIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmdfrmBerIndex_Object = MibTableColumn
pmc1008mpAlmdfrmBerIndex = _Pmc1008mpAlmdfrmBerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 129, 1, 1),
    _Pmc1008mpAlmdfrmBerIndex_Type()
)
pmc1008mpAlmdfrmBerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmdfrmBerIndex.setStatus("current")
_Pmc1008mpAlmLineSignalDegradePortn_Type = EkiOnOff
_Pmc1008mpAlmLineSignalDegradePortn_Object = MibTableColumn
pmc1008mpAlmLineSignalDegradePortn = _Pmc1008mpAlmLineSignalDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 129, 1, 2),
    _Pmc1008mpAlmLineSignalDegradePortn_Type()
)
pmc1008mpAlmLineSignalDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineSignalDegradePortn.setStatus("current")
_Pmc1008mpAlmLineSignalFailPortn_Type = EkiOnOff
_Pmc1008mpAlmLineSignalFailPortn_Object = MibTableColumn
pmc1008mpAlmLineSignalFailPortn = _Pmc1008mpAlmLineSignalFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 129, 1, 3),
    _Pmc1008mpAlmLineSignalFailPortn_Type()
)
pmc1008mpAlmLineSignalFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineSignalFailPortn.setStatus("current")
_Pmc1008mpAlmLineDegradePortn_Type = EkiOnOff
_Pmc1008mpAlmLineDegradePortn_Object = MibTableColumn
pmc1008mpAlmLineDegradePortn = _Pmc1008mpAlmLineDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 129, 1, 6),
    _Pmc1008mpAlmLineDegradePortn_Type()
)
pmc1008mpAlmLineDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineDegradePortn.setStatus("current")
_Pmc1008mpAlmlineXfp1AlarmTable_Object = MibTable
pmc1008mpAlmlineXfp1AlarmTable = _Pmc1008mpAlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1AlarmTable.setStatus("current")
_Pmc1008mpAlmlineXfp1AlarmEntry_Object = MibTableRow
pmc1008mpAlmlineXfp1AlarmEntry = _Pmc1008mpAlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1)
)
pmc1008mpAlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1AlarmEntry.setStatus("current")


class _Pmc1008mpAlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pmc1008mpAlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmlineXfp1AlarmIndex_Object = MibTableColumn
pmc1008mpAlmlineXfp1AlarmIndex = _Pmc1008mpAlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1, 1),
    _Pmc1008mpAlmlineXfp1AlarmIndex_Type()
)
pmc1008mpAlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1AlarmIndex.setStatus("current")
_Pmc1008mpAlmTxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmTxPowerLowAlarmPortn_Object = MibTableColumn
pmc1008mpAlmTxPowerLowAlarmPortn = _Pmc1008mpAlmTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1, 2),
    _Pmc1008mpAlmTxPowerLowAlarmPortn_Type()
)
pmc1008mpAlmTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxPowerLowAlarmPortn.setStatus("current")
_Pmc1008mpAlmTxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmTxPowerHighAlarmPortn_Object = MibTableColumn
pmc1008mpAlmTxPowerHighAlarmPortn = _Pmc1008mpAlmTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1, 3),
    _Pmc1008mpAlmTxPowerHighAlarmPortn_Type()
)
pmc1008mpAlmTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxPowerHighAlarmPortn.setStatus("current")
_Pmc1008mpAlmTxBiasLowAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmTxBiasLowAlarmPortn_Object = MibTableColumn
pmc1008mpAlmTxBiasLowAlarmPortn = _Pmc1008mpAlmTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1, 4),
    _Pmc1008mpAlmTxBiasLowAlarmPortn_Type()
)
pmc1008mpAlmTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxBiasLowAlarmPortn.setStatus("current")
_Pmc1008mpAlmTxBiasHighAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmTxBiasHighAlarmPortn_Object = MibTableColumn
pmc1008mpAlmTxBiasHighAlarmPortn = _Pmc1008mpAlmTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1, 5),
    _Pmc1008mpAlmTxBiasHighAlarmPortn_Type()
)
pmc1008mpAlmTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxBiasHighAlarmPortn.setStatus("current")
_Pmc1008mpAlmTempLowAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmTempLowAlarmPortn_Object = MibTableColumn
pmc1008mpAlmTempLowAlarmPortn = _Pmc1008mpAlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1, 8),
    _Pmc1008mpAlmTempLowAlarmPortn_Type()
)
pmc1008mpAlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTempLowAlarmPortn.setStatus("current")
_Pmc1008mpAlmTempHighAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmTempHighAlarmPortn_Object = MibTableColumn
pmc1008mpAlmTempHighAlarmPortn = _Pmc1008mpAlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1, 9),
    _Pmc1008mpAlmTempHighAlarmPortn_Type()
)
pmc1008mpAlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTempHighAlarmPortn.setStatus("current")
_Pmc1008mpAlmRxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmRxPowerLowAlarmPortn_Object = MibTableColumn
pmc1008mpAlmRxPowerLowAlarmPortn = _Pmc1008mpAlmRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1, 16),
    _Pmc1008mpAlmRxPowerLowAlarmPortn_Type()
)
pmc1008mpAlmRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxPowerLowAlarmPortn.setStatus("current")
_Pmc1008mpAlmRxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmRxPowerHighAlarmPortn_Object = MibTableColumn
pmc1008mpAlmRxPowerHighAlarmPortn = _Pmc1008mpAlmRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 208, 1, 17),
    _Pmc1008mpAlmRxPowerHighAlarmPortn_Type()
)
pmc1008mpAlmRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxPowerHighAlarmPortn.setStatus("current")
_Pmc1008mpAlmlineXfp1SupplyAlarmTable_Object = MibTable
pmc1008mpAlmlineXfp1SupplyAlarmTable = _Pmc1008mpAlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pmc1008mpAlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pmc1008mpAlmlineXfp1SupplyAlarmEntry = _Pmc1008mpAlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1)
)
pmc1008mpAlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pmc1008mpAlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pmc1008mpAlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pmc1008mpAlmlineXfp1SupplyAlarmIndex = _Pmc1008mpAlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 1),
    _Pmc1008mpAlmlineXfp1SupplyAlarmIndex_Type()
)
pmc1008mpAlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pmc1008mpAlmVee5LowAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmVee5LowAlarmPortn_Object = MibTableColumn
pmc1008mpAlmVee5LowAlarmPortn = _Pmc1008mpAlmVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 2),
    _Pmc1008mpAlmVee5LowAlarmPortn_Type()
)
pmc1008mpAlmVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVee5LowAlarmPortn.setStatus("current")
_Pmc1008mpAlmVee5HighAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmVee5HighAlarmPortn_Object = MibTableColumn
pmc1008mpAlmVee5HighAlarmPortn = _Pmc1008mpAlmVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 3),
    _Pmc1008mpAlmVee5HighAlarmPortn_Type()
)
pmc1008mpAlmVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVee5HighAlarmPortn.setStatus("current")
_Pmc1008mpAlmVcc2LowAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc2LowAlarmPortn_Object = MibTableColumn
pmc1008mpAlmVcc2LowAlarmPortn = _Pmc1008mpAlmVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 4),
    _Pmc1008mpAlmVcc2LowAlarmPortn_Type()
)
pmc1008mpAlmVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc2LowAlarmPortn.setStatus("current")
_Pmc1008mpAlmVcc2HighAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc2HighAlarmPortn_Object = MibTableColumn
pmc1008mpAlmVcc2HighAlarmPortn = _Pmc1008mpAlmVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 5),
    _Pmc1008mpAlmVcc2HighAlarmPortn_Type()
)
pmc1008mpAlmVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc2HighAlarmPortn.setStatus("current")
_Pmc1008mpAlmVcc3LowAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc3LowAlarmPortn_Object = MibTableColumn
pmc1008mpAlmVcc3LowAlarmPortn = _Pmc1008mpAlmVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 6),
    _Pmc1008mpAlmVcc3LowAlarmPortn_Type()
)
pmc1008mpAlmVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc3LowAlarmPortn.setStatus("current")
_Pmc1008mpAlmVcc3HighAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc3HighAlarmPortn_Object = MibTableColumn
pmc1008mpAlmVcc3HighAlarmPortn = _Pmc1008mpAlmVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 7),
    _Pmc1008mpAlmVcc3HighAlarmPortn_Type()
)
pmc1008mpAlmVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc3HighAlarmPortn.setStatus("current")
_Pmc1008mpAlmVcc5LowAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc5LowAlarmPortn_Object = MibTableColumn
pmc1008mpAlmVcc5LowAlarmPortn = _Pmc1008mpAlmVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 8),
    _Pmc1008mpAlmVcc5LowAlarmPortn_Type()
)
pmc1008mpAlmVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc5LowAlarmPortn.setStatus("current")
_Pmc1008mpAlmVcc5HighAlarmPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc5HighAlarmPortn_Object = MibTableColumn
pmc1008mpAlmVcc5HighAlarmPortn = _Pmc1008mpAlmVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 9),
    _Pmc1008mpAlmVcc5HighAlarmPortn_Type()
)
pmc1008mpAlmVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc5HighAlarmPortn.setStatus("current")
_Pmc1008mpAlmVee5LowWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmVee5LowWarningPortn_Object = MibTableColumn
pmc1008mpAlmVee5LowWarningPortn = _Pmc1008mpAlmVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 10),
    _Pmc1008mpAlmVee5LowWarningPortn_Type()
)
pmc1008mpAlmVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVee5LowWarningPortn.setStatus("current")
_Pmc1008mpAlmVee5HighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmVee5HighWarningPortn_Object = MibTableColumn
pmc1008mpAlmVee5HighWarningPortn = _Pmc1008mpAlmVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 11),
    _Pmc1008mpAlmVee5HighWarningPortn_Type()
)
pmc1008mpAlmVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVee5HighWarningPortn.setStatus("current")
_Pmc1008mpAlmVcc2LowWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc2LowWarningPortn_Object = MibTableColumn
pmc1008mpAlmVcc2LowWarningPortn = _Pmc1008mpAlmVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 12),
    _Pmc1008mpAlmVcc2LowWarningPortn_Type()
)
pmc1008mpAlmVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc2LowWarningPortn.setStatus("current")
_Pmc1008mpAlmVcc2HighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc2HighWarningPortn_Object = MibTableColumn
pmc1008mpAlmVcc2HighWarningPortn = _Pmc1008mpAlmVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 13),
    _Pmc1008mpAlmVcc2HighWarningPortn_Type()
)
pmc1008mpAlmVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc2HighWarningPortn.setStatus("current")
_Pmc1008mpAlmVcc3LowWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc3LowWarningPortn_Object = MibTableColumn
pmc1008mpAlmVcc3LowWarningPortn = _Pmc1008mpAlmVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 14),
    _Pmc1008mpAlmVcc3LowWarningPortn_Type()
)
pmc1008mpAlmVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc3LowWarningPortn.setStatus("current")
_Pmc1008mpAlmVcc3HighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc3HighWarningPortn_Object = MibTableColumn
pmc1008mpAlmVcc3HighWarningPortn = _Pmc1008mpAlmVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 15),
    _Pmc1008mpAlmVcc3HighWarningPortn_Type()
)
pmc1008mpAlmVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc3HighWarningPortn.setStatus("current")
_Pmc1008mpAlmVcc5LowWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc5LowWarningPortn_Object = MibTableColumn
pmc1008mpAlmVcc5LowWarningPortn = _Pmc1008mpAlmVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 16),
    _Pmc1008mpAlmVcc5LowWarningPortn_Type()
)
pmc1008mpAlmVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc5LowWarningPortn.setStatus("current")
_Pmc1008mpAlmVcc5HighWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmVcc5HighWarningPortn_Object = MibTableColumn
pmc1008mpAlmVcc5HighWarningPortn = _Pmc1008mpAlmVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 212, 1, 17),
    _Pmc1008mpAlmVcc5HighWarningPortn_Type()
)
pmc1008mpAlmVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmVcc5HighWarningPortn.setStatus("current")
_Pmc1008mpAlmlineOtx1TlhAlarmsTable_Object = MibTable
pmc1008mpAlmlineOtx1TlhAlarmsTable = _Pmc1008mpAlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pmc1008mpAlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pmc1008mpAlmlineOtx1TlhAlarmsEntry = _Pmc1008mpAlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 224, 1)
)
pmc1008mpAlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pmc1008mpAlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pmc1008mpAlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pmc1008mpAlmlineOtx1TlhAlarmsIndex = _Pmc1008mpAlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 224, 1, 1),
    _Pmc1008mpAlmlineOtx1TlhAlarmsIndex_Type()
)
pmc1008mpAlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pmc1008mpAlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pmc1008mpAlmLineModulatorAgingHighAlaPortn = _Pmc1008mpAlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 224, 1, 6),
    _Pmc1008mpAlmLineModulatorAgingHighAlaPortn_Type()
)
pmc1008mpAlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pmc1008mpAlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmLineAgingHighAlaPortn_Object = MibTableColumn
pmc1008mpAlmLineAgingHighAlaPortn = _Pmc1008mpAlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 224, 1, 7),
    _Pmc1008mpAlmLineAgingHighAlaPortn_Type()
)
pmc1008mpAlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineAgingHighAlaPortn.setStatus("current")
_Pmc1008mpAlmLineCdrNotReadyPortn_Type = EkiOnOff
_Pmc1008mpAlmLineCdrNotReadyPortn_Object = MibTableColumn
pmc1008mpAlmLineCdrNotReadyPortn = _Pmc1008mpAlmLineCdrNotReadyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 224, 1, 10),
    _Pmc1008mpAlmLineCdrNotReadyPortn_Type()
)
pmc1008mpAlmLineCdrNotReadyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineCdrNotReadyPortn.setStatus("current")
_Pmc1008mpAlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pmc1008mpAlmLineFreqDevHighAlaPortn = _Pmc1008mpAlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 224, 1, 13),
    _Pmc1008mpAlmLineFreqDevHighAlaPortn_Type()
)
pmc1008mpAlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineFreqDevHighAlaPortn.setStatus("current")
_Pmc1008mpAlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pmc1008mpAlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pmc1008mpAlmLineLaserTempHighAlaPortn = _Pmc1008mpAlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 2, 224, 1, 15),
    _Pmc1008mpAlmLineLaserTempHighAlaPortn_Type()
)
pmc1008mpAlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineLaserTempHighAlaPortn.setStatus("current")
_Pmc1008mpAlmLineCrit_ObjectIdentity = ObjectIdentity
pmc1008mpAlmLineCrit = _Pmc1008mpAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3)
)
_Pmc1008mpAlmsynthAlmLineTable_Object = MibTable
pmc1008mpAlmsynthAlmLineTable = _Pmc1008mpAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmsynthAlmLineTable.setStatus("current")
_Pmc1008mpAlmsynthAlmLineEntry_Object = MibTableRow
pmc1008mpAlmsynthAlmLineEntry = _Pmc1008mpAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1)
)
pmc1008mpAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmsynthAlmLineEntry.setStatus("current")


class _Pmc1008mpAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pmc1008mpAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmsynthAlmLineIndex_Object = MibTableColumn
pmc1008mpAlmsynthAlmLineIndex = _Pmc1008mpAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 1),
    _Pmc1008mpAlmsynthAlmLineIndex_Type()
)
pmc1008mpAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmsynthAlmLineIndex.setStatus("current")
_Pmc1008mpAlmXfpAbsentPortn_Type = EkiOnOff
_Pmc1008mpAlmXfpAbsentPortn_Object = MibTableColumn
pmc1008mpAlmXfpAbsentPortn = _Pmc1008mpAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 2),
    _Pmc1008mpAlmXfpAbsentPortn_Type()
)
pmc1008mpAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmXfpAbsentPortn.setStatus("current")
_Pmc1008mpAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pmc1008mpAlmXfpInitNotComplPortn_Object = MibTableColumn
pmc1008mpAlmXfpInitNotComplPortn = _Pmc1008mpAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 3),
    _Pmc1008mpAlmXfpInitNotComplPortn_Type()
)
pmc1008mpAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmXfpInitNotComplPortn.setStatus("current")
_Pmc1008mpAlmLineHwFailPortn_Type = EkiOnOff
_Pmc1008mpAlmLineHwFailPortn_Object = MibTableColumn
pmc1008mpAlmLineHwFailPortn = _Pmc1008mpAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 5),
    _Pmc1008mpAlmLineHwFailPortn_Type()
)
pmc1008mpAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineHwFailPortn.setStatus("current")
_Pmc1008mpAlmXfpTxOffPortn_Type = EkiOnOff
_Pmc1008mpAlmXfpTxOffPortn_Object = MibTableColumn
pmc1008mpAlmXfpTxOffPortn = _Pmc1008mpAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 6),
    _Pmc1008mpAlmXfpTxOffPortn_Type()
)
pmc1008mpAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmXfpTxOffPortn.setStatus("current")
_Pmc1008mpAlmLineLocalOosPortn_Type = EkiOnOff
_Pmc1008mpAlmLineLocalOosPortn_Object = MibTableColumn
pmc1008mpAlmLineLocalOosPortn = _Pmc1008mpAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 7),
    _Pmc1008mpAlmLineLocalOosPortn_Type()
)
pmc1008mpAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineLocalOosPortn.setStatus("current")
_Pmc1008mpAlmUpRdiInsPortn_Type = EkiOnOff
_Pmc1008mpAlmUpRdiInsPortn_Object = MibTableColumn
pmc1008mpAlmUpRdiInsPortn = _Pmc1008mpAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 9),
    _Pmc1008mpAlmUpRdiInsPortn_Type()
)
pmc1008mpAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmUpRdiInsPortn.setStatus("current")
_Pmc1008mpAlmLineDdmWarningPortn_Type = EkiOnOff
_Pmc1008mpAlmLineDdmWarningPortn_Object = MibTableColumn
pmc1008mpAlmLineDdmWarningPortn = _Pmc1008mpAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 10),
    _Pmc1008mpAlmLineDdmWarningPortn_Type()
)
pmc1008mpAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineDdmWarningPortn.setStatus("current")
_Pmc1008mpAlmLineDdmAlmPortn_Type = EkiOnOff
_Pmc1008mpAlmLineDdmAlmPortn_Object = MibTableColumn
pmc1008mpAlmLineDdmAlmPortn = _Pmc1008mpAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 11),
    _Pmc1008mpAlmLineDdmAlmPortn_Type()
)
pmc1008mpAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineDdmAlmPortn.setStatus("current")
_Pmc1008mpAlmLineFailPortn_Type = EkiOnOff
_Pmc1008mpAlmLineFailPortn_Object = MibTableColumn
pmc1008mpAlmLineFailPortn = _Pmc1008mpAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 13),
    _Pmc1008mpAlmLineFailPortn_Type()
)
pmc1008mpAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineFailPortn.setStatus("current")
_Pmc1008mpAlmLineActivePortn_Type = EkiOnOff
_Pmc1008mpAlmLineActivePortn_Object = MibTableColumn
pmc1008mpAlmLineActivePortn = _Pmc1008mpAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 7, 1, 17),
    _Pmc1008mpAlmLineActivePortn_Type()
)
pmc1008mpAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmLineActivePortn.setStatus("current")
_Pmc1008mpAlmdfrmAlmTable_Object = MibTable
pmc1008mpAlmdfrmAlmTable = _Pmc1008mpAlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmdfrmAlmTable.setStatus("current")
_Pmc1008mpAlmdfrmAlmEntry_Object = MibTableRow
pmc1008mpAlmdfrmAlmEntry = _Pmc1008mpAlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 128, 1)
)
pmc1008mpAlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmdfrmAlmEntry.setStatus("current")


class _Pmc1008mpAlmdfrmAlmIndex_Type(Integer32):
    """Custom type pmc1008mpAlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmdfrmAlmIndex_Object = MibTableColumn
pmc1008mpAlmdfrmAlmIndex = _Pmc1008mpAlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 128, 1, 1),
    _Pmc1008mpAlmdfrmAlmIndex_Type()
)
pmc1008mpAlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmdfrmAlmIndex.setStatus("current")
_Pmc1008mpAlmDwAisDetPortn_Type = EkiOnOff
_Pmc1008mpAlmDwAisDetPortn_Object = MibTableColumn
pmc1008mpAlmDwAisDetPortn = _Pmc1008mpAlmDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 128, 1, 2),
    _Pmc1008mpAlmDwAisDetPortn_Type()
)
pmc1008mpAlmDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwAisDetPortn.setStatus("current")
_Pmc1008mpAlmDwRdiDetPortn_Type = EkiOnOff
_Pmc1008mpAlmDwRdiDetPortn_Object = MibTableColumn
pmc1008mpAlmDwRdiDetPortn = _Pmc1008mpAlmDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 128, 1, 3),
    _Pmc1008mpAlmDwRdiDetPortn_Type()
)
pmc1008mpAlmDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwRdiDetPortn.setStatus("current")
_Pmc1008mpAlmDwOofPortn_Type = EkiOnOff
_Pmc1008mpAlmDwOofPortn_Object = MibTableColumn
pmc1008mpAlmDwOofPortn = _Pmc1008mpAlmDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 128, 1, 4),
    _Pmc1008mpAlmDwOofPortn_Type()
)
pmc1008mpAlmDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwOofPortn.setStatus("current")
_Pmc1008mpAlmDwLofPortn_Type = EkiOnOff
_Pmc1008mpAlmDwLofPortn_Object = MibTableColumn
pmc1008mpAlmDwLofPortn = _Pmc1008mpAlmDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 128, 1, 5),
    _Pmc1008mpAlmDwLofPortn_Type()
)
pmc1008mpAlmDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwLofPortn.setStatus("current")
_Pmc1008mpAlmlineSyncAlarmsTable_Object = MibTable
pmc1008mpAlmlineSyncAlarmsTable = _Pmc1008mpAlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineSyncAlarmsTable.setStatus("current")
_Pmc1008mpAlmlineSyncAlarmsEntry_Object = MibTableRow
pmc1008mpAlmlineSyncAlarmsEntry = _Pmc1008mpAlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 133, 1)
)
pmc1008mpAlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineSyncAlarmsEntry.setStatus("current")


class _Pmc1008mpAlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pmc1008mpAlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmlineSyncAlarmsIndex_Object = MibTableColumn
pmc1008mpAlmlineSyncAlarmsIndex = _Pmc1008mpAlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 133, 1, 1),
    _Pmc1008mpAlmlineSyncAlarmsIndex_Type()
)
pmc1008mpAlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmlineSyncAlarmsIndex.setStatus("current")
_Pmc1008mpAlmDwLockerrPortn_Type = EkiOnOff
_Pmc1008mpAlmDwLockerrPortn_Object = MibTableColumn
pmc1008mpAlmDwLockerrPortn = _Pmc1008mpAlmDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 133, 1, 13),
    _Pmc1008mpAlmDwLockerrPortn_Type()
)
pmc1008mpAlmDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwLockerrPortn.setStatus("current")
_Pmc1008mpAlmUpLockerrPortn_Type = EkiOnOff
_Pmc1008mpAlmUpLockerrPortn_Object = MibTableColumn
pmc1008mpAlmUpLockerrPortn = _Pmc1008mpAlmUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 133, 1, 14),
    _Pmc1008mpAlmUpLockerrPortn_Type()
)
pmc1008mpAlmUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmUpLockerrPortn.setStatus("current")
_Pmc1008mpAlmDwLosPortn_Type = EkiOnOff
_Pmc1008mpAlmDwLosPortn_Object = MibTableColumn
pmc1008mpAlmDwLosPortn = _Pmc1008mpAlmDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 133, 1, 17),
    _Pmc1008mpAlmDwLosPortn_Type()
)
pmc1008mpAlmDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmDwLosPortn.setStatus("current")
_Pmc1008mpAlmlineXfp1AlarmsTable_Object = MibTable
pmc1008mpAlmlineXfp1AlarmsTable = _Pmc1008mpAlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1AlarmsTable.setStatus("current")
_Pmc1008mpAlmlineXfp1AlarmsEntry_Object = MibTableRow
pmc1008mpAlmlineXfp1AlarmsEntry = _Pmc1008mpAlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1)
)
pmc1008mpAlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1AlarmsEntry.setStatus("current")


class _Pmc1008mpAlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pmc1008mpAlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpAlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pmc1008mpAlmlineXfp1AlarmsIndex_Object = MibTableColumn
pmc1008mpAlmlineXfp1AlarmsIndex = _Pmc1008mpAlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 1),
    _Pmc1008mpAlmlineXfp1AlarmsIndex_Type()
)
pmc1008mpAlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmlineXfp1AlarmsIndex.setStatus("current")
_Pmc1008mpAlmModNrPortn_Type = EkiOnOff
_Pmc1008mpAlmModNrPortn_Object = MibTableColumn
pmc1008mpAlmModNrPortn = _Pmc1008mpAlmModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 3),
    _Pmc1008mpAlmModNrPortn_Type()
)
pmc1008mpAlmModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmModNrPortn.setStatus("current")
_Pmc1008mpAlmRxCdrNotLockedPortn_Type = EkiOnOff
_Pmc1008mpAlmRxCdrNotLockedPortn_Object = MibTableColumn
pmc1008mpAlmRxCdrNotLockedPortn = _Pmc1008mpAlmRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 4),
    _Pmc1008mpAlmRxCdrNotLockedPortn_Type()
)
pmc1008mpAlmRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxCdrNotLockedPortn.setStatus("current")
_Pmc1008mpAlmRxNrPortn_Type = EkiOnOff
_Pmc1008mpAlmRxNrPortn_Object = MibTableColumn
pmc1008mpAlmRxNrPortn = _Pmc1008mpAlmRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 6),
    _Pmc1008mpAlmRxNrPortn_Type()
)
pmc1008mpAlmRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmRxNrPortn.setStatus("current")
_Pmc1008mpAlmTxCdrNotLockedPortn_Type = EkiOnOff
_Pmc1008mpAlmTxCdrNotLockedPortn_Object = MibTableColumn
pmc1008mpAlmTxCdrNotLockedPortn = _Pmc1008mpAlmTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 7),
    _Pmc1008mpAlmTxCdrNotLockedPortn_Type()
)
pmc1008mpAlmTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxCdrNotLockedPortn.setStatus("current")
_Pmc1008mpAlmTxFaultPortn_Type = EkiOnOff
_Pmc1008mpAlmTxFaultPortn_Object = MibTableColumn
pmc1008mpAlmTxFaultPortn = _Pmc1008mpAlmTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 8),
    _Pmc1008mpAlmTxFaultPortn_Type()
)
pmc1008mpAlmTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxFaultPortn.setStatus("current")
_Pmc1008mpAlmTxNrPortn_Type = EkiOnOff
_Pmc1008mpAlmTxNrPortn_Object = MibTableColumn
pmc1008mpAlmTxNrPortn = _Pmc1008mpAlmTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 9),
    _Pmc1008mpAlmTxNrPortn_Type()
)
pmc1008mpAlmTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTxNrPortn.setStatus("current")
_Pmc1008mpAlmChannelNotAcquiredPortn_Type = EkiOnOff
_Pmc1008mpAlmChannelNotAcquiredPortn_Object = MibTableColumn
pmc1008mpAlmChannelNotAcquiredPortn = _Pmc1008mpAlmChannelNotAcquiredPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 11),
    _Pmc1008mpAlmChannelNotAcquiredPortn_Type()
)
pmc1008mpAlmChannelNotAcquiredPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmChannelNotAcquiredPortn.setStatus("current")
_Pmc1008mpAlmWavelengthUnlockedPortn_Type = EkiOnOff
_Pmc1008mpAlmWavelengthUnlockedPortn_Object = MibTableColumn
pmc1008mpAlmWavelengthUnlockedPortn = _Pmc1008mpAlmWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 15),
    _Pmc1008mpAlmWavelengthUnlockedPortn_Type()
)
pmc1008mpAlmWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmWavelengthUnlockedPortn.setStatus("current")
_Pmc1008mpAlmTecFaultPortn_Type = EkiOnOff
_Pmc1008mpAlmTecFaultPortn_Object = MibTableColumn
pmc1008mpAlmTecFaultPortn = _Pmc1008mpAlmTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 16),
    _Pmc1008mpAlmTecFaultPortn_Type()
)
pmc1008mpAlmTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmTecFaultPortn.setStatus("current")
_Pmc1008mpAlmApdSupplyFaultPortn_Type = EkiOnOff
_Pmc1008mpAlmApdSupplyFaultPortn_Object = MibTableColumn
pmc1008mpAlmApdSupplyFaultPortn = _Pmc1008mpAlmApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 2, 3, 3, 211, 1, 17),
    _Pmc1008mpAlmApdSupplyFaultPortn_Type()
)
pmc1008mpAlmApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpAlmApdSupplyFaultPortn.setStatus("current")
_Pmc1008mpmeasures_ObjectIdentity = ObjectIdentity
pmc1008mpmeasures = _Pmc1008mpmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3)
)
_Pmc1008mpMesrOther_ObjectIdentity = ObjectIdentity
pmc1008mpMesrOther = _Pmc1008mpMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 1)
)
_Pmc1008mpMesrsynth0_Type = EkiMeasureType
_Pmc1008mpMesrsynth0_Object = MibScalar
pmc1008mpMesrsynth0 = _Pmc1008mpMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 1, 0),
    _Pmc1008mpMesrsynth0_Type()
)
pmc1008mpMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrsynth0.setStatus("deprecated")
_Pmc1008mpMesrsynth1_Type = EkiMeasureType
_Pmc1008mpMesrsynth1_Object = MibScalar
pmc1008mpMesrsynth1 = _Pmc1008mpMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 1, 1),
    _Pmc1008mpMesrsynth1_Type()
)
pmc1008mpMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrsynth1.setStatus("deprecated")
_Pmc1008mpMesrClient_ObjectIdentity = ObjectIdentity
pmc1008mpMesrClient = _Pmc1008mpMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2)
)
_Pmc1008mpMesrtempMeasTable_Object = MibTable
pmc1008mpMesrtempMeasTable = _Pmc1008mpMesrtempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrtempMeasTable.setStatus("current")
_Pmc1008mpMesrtempMeasEntry_Object = MibTableRow
pmc1008mpMesrtempMeasEntry = _Pmc1008mpMesrtempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 16, 1)
)
pmc1008mpMesrtempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrtempMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrtempMeasEntry.setStatus("current")


class _Pmc1008mpMesrtempMeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrtempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrtempMeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrtempMeasIndex_Object = MibTableColumn
pmc1008mpMesrtempMeasIndex = _Pmc1008mpMesrtempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 16, 1, 1),
    _Pmc1008mpMesrtempMeasIndex_Type()
)
pmc1008mpMesrtempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrtempMeasIndex.setStatus("current")


class _Pmc1008mpMesrtempMeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrtempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrtempMeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrtempMeasPortn_Object = MibTableColumn
pmc1008mpMesrtempMeasPortn = _Pmc1008mpMesrtempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 16, 1, 2),
    _Pmc1008mpMesrtempMeasPortn_Type()
)
pmc1008mpMesrtempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrtempMeasPortn.setStatus("current")
_Pmc1008mpMesrvoltMeasTable_Object = MibTable
pmc1008mpMesrvoltMeasTable = _Pmc1008mpMesrvoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrvoltMeasTable.setStatus("current")
_Pmc1008mpMesrvoltMeasEntry_Object = MibTableRow
pmc1008mpMesrvoltMeasEntry = _Pmc1008mpMesrvoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 24, 1)
)
pmc1008mpMesrvoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrvoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrvoltMeasEntry.setStatus("current")


class _Pmc1008mpMesrvoltMeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrvoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrvoltMeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrvoltMeasIndex_Object = MibTableColumn
pmc1008mpMesrvoltMeasIndex = _Pmc1008mpMesrvoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 24, 1, 1),
    _Pmc1008mpMesrvoltMeasIndex_Type()
)
pmc1008mpMesrvoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrvoltMeasIndex.setStatus("current")


class _Pmc1008mpMesrvoltMeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrvoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrvoltMeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrvoltMeasPortn_Object = MibTableColumn
pmc1008mpMesrvoltMeasPortn = _Pmc1008mpMesrvoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 24, 1, 2),
    _Pmc1008mpMesrvoltMeasPortn_Type()
)
pmc1008mpMesrvoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrvoltMeasPortn.setStatus("current")
_Pmc1008mpMesrbiasMeasTable_Object = MibTable
pmc1008mpMesrbiasMeasTable = _Pmc1008mpMesrbiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrbiasMeasTable.setStatus("current")
_Pmc1008mpMesrbiasMeasEntry_Object = MibTableRow
pmc1008mpMesrbiasMeasEntry = _Pmc1008mpMesrbiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 32, 1)
)
pmc1008mpMesrbiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrbiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrbiasMeasEntry.setStatus("current")


class _Pmc1008mpMesrbiasMeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrbiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrbiasMeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrbiasMeasIndex_Object = MibTableColumn
pmc1008mpMesrbiasMeasIndex = _Pmc1008mpMesrbiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 32, 1, 1),
    _Pmc1008mpMesrbiasMeasIndex_Type()
)
pmc1008mpMesrbiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrbiasMeasIndex.setStatus("current")


class _Pmc1008mpMesrbiasMeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrbiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrbiasMeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrbiasMeasPortn_Object = MibTableColumn
pmc1008mpMesrbiasMeasPortn = _Pmc1008mpMesrbiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 32, 1, 2),
    _Pmc1008mpMesrbiasMeasPortn_Type()
)
pmc1008mpMesrbiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrbiasMeasPortn.setStatus("current")
_Pmc1008mpMesrtxpwrMeasTable_Object = MibTable
pmc1008mpMesrtxpwrMeasTable = _Pmc1008mpMesrtxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrtxpwrMeasTable.setStatus("current")
_Pmc1008mpMesrtxpwrMeasEntry_Object = MibTableRow
pmc1008mpMesrtxpwrMeasEntry = _Pmc1008mpMesrtxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 40, 1)
)
pmc1008mpMesrtxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrtxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrtxpwrMeasEntry.setStatus("current")


class _Pmc1008mpMesrtxpwrMeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrtxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrtxpwrMeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrtxpwrMeasIndex_Object = MibTableColumn
pmc1008mpMesrtxpwrMeasIndex = _Pmc1008mpMesrtxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 40, 1, 1),
    _Pmc1008mpMesrtxpwrMeasIndex_Type()
)
pmc1008mpMesrtxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrtxpwrMeasIndex.setStatus("current")


class _Pmc1008mpMesrtxpwrMeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrtxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrtxpwrMeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrtxpwrMeasPortn_Object = MibTableColumn
pmc1008mpMesrtxpwrMeasPortn = _Pmc1008mpMesrtxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 40, 1, 2),
    _Pmc1008mpMesrtxpwrMeasPortn_Type()
)
pmc1008mpMesrtxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrtxpwrMeasPortn.setStatus("current")
_Pmc1008mpMesrrxpwrMeasTable_Object = MibTable
pmc1008mpMesrrxpwrMeasTable = _Pmc1008mpMesrrxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrrxpwrMeasTable.setStatus("current")
_Pmc1008mpMesrrxpwrMeasEntry_Object = MibTableRow
pmc1008mpMesrrxpwrMeasEntry = _Pmc1008mpMesrrxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 48, 1)
)
pmc1008mpMesrrxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrrxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrrxpwrMeasEntry.setStatus("current")


class _Pmc1008mpMesrrxpwrMeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrrxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrrxpwrMeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrrxpwrMeasIndex_Object = MibTableColumn
pmc1008mpMesrrxpwrMeasIndex = _Pmc1008mpMesrrxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 48, 1, 1),
    _Pmc1008mpMesrrxpwrMeasIndex_Type()
)
pmc1008mpMesrrxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrrxpwrMeasIndex.setStatus("current")


class _Pmc1008mpMesrrxpwrMeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrrxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrrxpwrMeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrrxpwrMeasPortn_Object = MibTableColumn
pmc1008mpMesrrxpwrMeasPortn = _Pmc1008mpMesrrxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 2, 48, 1, 2),
    _Pmc1008mpMesrrxpwrMeasPortn_Type()
)
pmc1008mpMesrrxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrrxpwrMeasPortn.setStatus("current")
_Pmc1008mpMesrLine_ObjectIdentity = ObjectIdentity
pmc1008mpMesrLine = _Pmc1008mpMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3)
)
_Pmc1008mpMesrxfp1LxModTempMeasTable_Object = MibTable
pmc1008mpMesrxfp1LxModTempMeasTable = _Pmc1008mpMesrxfp1LxModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxModTempMeasTable.setStatus("current")
_Pmc1008mpMesrxfp1LxModTempMeasEntry_Object = MibTableRow
pmc1008mpMesrxfp1LxModTempMeasEntry = _Pmc1008mpMesrxfp1LxModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 208, 1)
)
pmc1008mpMesrxfp1LxModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrxfp1LxModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxModTempMeasEntry.setStatus("current")


class _Pmc1008mpMesrxfp1LxModTempMeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LxModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrxfp1LxModTempMeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LxModTempMeasIndex_Object = MibTableColumn
pmc1008mpMesrxfp1LxModTempMeasIndex = _Pmc1008mpMesrxfp1LxModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 208, 1, 1),
    _Pmc1008mpMesrxfp1LxModTempMeasIndex_Type()
)
pmc1008mpMesrxfp1LxModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxModTempMeasIndex.setStatus("current")


class _Pmc1008mpMesrxfp1LxModTempMeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LxModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrxfp1LxModTempMeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LxModTempMeasPortn_Object = MibTableColumn
pmc1008mpMesrxfp1LxModTempMeasPortn = _Pmc1008mpMesrxfp1LxModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 208, 1, 2),
    _Pmc1008mpMesrxfp1LxModTempMeasPortn_Type()
)
pmc1008mpMesrxfp1LxModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxModTempMeasPortn.setStatus("current")
_Pmc1008mpMesrxfp1ReservedTable_Object = MibTable
pmc1008mpMesrxfp1ReservedTable = _Pmc1008mpMesrxfp1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1ReservedTable.setStatus("deprecated")
_Pmc1008mpMesrxfp1ReservedEntry_Object = MibTableRow
pmc1008mpMesrxfp1ReservedEntry = _Pmc1008mpMesrxfp1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 209, 1)
)
pmc1008mpMesrxfp1ReservedEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrxfp1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1ReservedEntry.setStatus("deprecated")


class _Pmc1008mpMesrxfp1ReservedIndex_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrxfp1ReservedIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1ReservedIndex_Object = MibTableColumn
pmc1008mpMesrxfp1ReservedIndex = _Pmc1008mpMesrxfp1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 209, 1, 1),
    _Pmc1008mpMesrxfp1ReservedIndex_Type()
)
pmc1008mpMesrxfp1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1ReservedIndex.setStatus("deprecated")


class _Pmc1008mpMesrxfp1ReservedPortn_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrxfp1ReservedPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1ReservedPortn_Object = MibTableColumn
pmc1008mpMesrxfp1ReservedPortn = _Pmc1008mpMesrxfp1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 209, 1, 2),
    _Pmc1008mpMesrxfp1ReservedPortn_Type()
)
pmc1008mpMesrxfp1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1ReservedPortn.setStatus("deprecated")
_Pmc1008mpMesrxfp1LoBiasCurrentMeasTable_Object = MibTable
pmc1008mpMesrxfp1LoBiasCurrentMeasTable = _Pmc1008mpMesrxfp1LoBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LoBiasCurrentMeasTable.setStatus("current")
_Pmc1008mpMesrxfp1LoBiasCurrentMeasEntry_Object = MibTableRow
pmc1008mpMesrxfp1LoBiasCurrentMeasEntry = _Pmc1008mpMesrxfp1LoBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 210, 1)
)
pmc1008mpMesrxfp1LoBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrxfp1LoBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LoBiasCurrentMeasEntry.setStatus("current")


class _Pmc1008mpMesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LoBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrxfp1LoBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LoBiasCurrentMeasIndex_Object = MibTableColumn
pmc1008mpMesrxfp1LoBiasCurrentMeasIndex = _Pmc1008mpMesrxfp1LoBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 210, 1, 1),
    _Pmc1008mpMesrxfp1LoBiasCurrentMeasIndex_Type()
)
pmc1008mpMesrxfp1LoBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LoBiasCurrentMeasIndex.setStatus("current")


class _Pmc1008mpMesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LoBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrxfp1LoBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LoBiasCurrentMeasPortn_Object = MibTableColumn
pmc1008mpMesrxfp1LoBiasCurrentMeasPortn = _Pmc1008mpMesrxfp1LoBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 210, 1, 2),
    _Pmc1008mpMesrxfp1LoBiasCurrentMeasPortn_Type()
)
pmc1008mpMesrxfp1LoBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LoBiasCurrentMeasPortn.setStatus("current")
_Pmc1008mpMesrxfp1LoTxPowerMeasTable_Object = MibTable
pmc1008mpMesrxfp1LoTxPowerMeasTable = _Pmc1008mpMesrxfp1LoTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LoTxPowerMeasTable.setStatus("current")
_Pmc1008mpMesrxfp1LoTxPowerMeasEntry_Object = MibTableRow
pmc1008mpMesrxfp1LoTxPowerMeasEntry = _Pmc1008mpMesrxfp1LoTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 211, 1)
)
pmc1008mpMesrxfp1LoTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrxfp1LoTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LoTxPowerMeasEntry.setStatus("current")


class _Pmc1008mpMesrxfp1LoTxPowerMeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LoTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrxfp1LoTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LoTxPowerMeasIndex_Object = MibTableColumn
pmc1008mpMesrxfp1LoTxPowerMeasIndex = _Pmc1008mpMesrxfp1LoTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 211, 1, 1),
    _Pmc1008mpMesrxfp1LoTxPowerMeasIndex_Type()
)
pmc1008mpMesrxfp1LoTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LoTxPowerMeasIndex.setStatus("current")


class _Pmc1008mpMesrxfp1LoTxPowerMeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LoTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrxfp1LoTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LoTxPowerMeasPortn_Object = MibTableColumn
pmc1008mpMesrxfp1LoTxPowerMeasPortn = _Pmc1008mpMesrxfp1LoTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 211, 1, 2),
    _Pmc1008mpMesrxfp1LoTxPowerMeasPortn_Type()
)
pmc1008mpMesrxfp1LoTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LoTxPowerMeasPortn.setStatus("current")
_Pmc1008mpMesrxfp1LiRxPowerMeasTable_Object = MibTable
pmc1008mpMesrxfp1LiRxPowerMeasTable = _Pmc1008mpMesrxfp1LiRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LiRxPowerMeasTable.setStatus("current")
_Pmc1008mpMesrxfp1LiRxPowerMeasEntry_Object = MibTableRow
pmc1008mpMesrxfp1LiRxPowerMeasEntry = _Pmc1008mpMesrxfp1LiRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 212, 1)
)
pmc1008mpMesrxfp1LiRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrxfp1LiRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LiRxPowerMeasEntry.setStatus("current")


class _Pmc1008mpMesrxfp1LiRxPowerMeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LiRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrxfp1LiRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LiRxPowerMeasIndex_Object = MibTableColumn
pmc1008mpMesrxfp1LiRxPowerMeasIndex = _Pmc1008mpMesrxfp1LiRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 212, 1, 1),
    _Pmc1008mpMesrxfp1LiRxPowerMeasIndex_Type()
)
pmc1008mpMesrxfp1LiRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LiRxPowerMeasIndex.setStatus("current")


class _Pmc1008mpMesrxfp1LiRxPowerMeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LiRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrxfp1LiRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LiRxPowerMeasPortn_Object = MibTableColumn
pmc1008mpMesrxfp1LiRxPowerMeasPortn = _Pmc1008mpMesrxfp1LiRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 212, 1, 2),
    _Pmc1008mpMesrxfp1LiRxPowerMeasPortn_Type()
)
pmc1008mpMesrxfp1LiRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LiRxPowerMeasPortn.setStatus("current")
_Pmc1008mpMesrxfp1LxAux1MeasTable_Object = MibTable
pmc1008mpMesrxfp1LxAux1MeasTable = _Pmc1008mpMesrxfp1LxAux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxAux1MeasTable.setStatus("deprecated")
_Pmc1008mpMesrxfp1LxAux1MeasEntry_Object = MibTableRow
pmc1008mpMesrxfp1LxAux1MeasEntry = _Pmc1008mpMesrxfp1LxAux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 213, 1)
)
pmc1008mpMesrxfp1LxAux1MeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrxfp1LxAux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxAux1MeasEntry.setStatus("deprecated")


class _Pmc1008mpMesrxfp1LxAux1MeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LxAux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrxfp1LxAux1MeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LxAux1MeasIndex_Object = MibTableColumn
pmc1008mpMesrxfp1LxAux1MeasIndex = _Pmc1008mpMesrxfp1LxAux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 213, 1, 1),
    _Pmc1008mpMesrxfp1LxAux1MeasIndex_Type()
)
pmc1008mpMesrxfp1LxAux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxAux1MeasIndex.setStatus("deprecated")


class _Pmc1008mpMesrxfp1LxAux1MeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LxAux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrxfp1LxAux1MeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LxAux1MeasPortn_Object = MibTableColumn
pmc1008mpMesrxfp1LxAux1MeasPortn = _Pmc1008mpMesrxfp1LxAux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 213, 1, 2),
    _Pmc1008mpMesrxfp1LxAux1MeasPortn_Type()
)
pmc1008mpMesrxfp1LxAux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxAux1MeasPortn.setStatus("deprecated")
_Pmc1008mpMesrxfp1LxAux2MeasTable_Object = MibTable
pmc1008mpMesrxfp1LxAux2MeasTable = _Pmc1008mpMesrxfp1LxAux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxAux2MeasTable.setStatus("deprecated")
_Pmc1008mpMesrxfp1LxAux2MeasEntry_Object = MibTableRow
pmc1008mpMesrxfp1LxAux2MeasEntry = _Pmc1008mpMesrxfp1LxAux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 214, 1)
)
pmc1008mpMesrxfp1LxAux2MeasEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrxfp1LxAux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxAux2MeasEntry.setStatus("deprecated")


class _Pmc1008mpMesrxfp1LxAux2MeasIndex_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LxAux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrxfp1LxAux2MeasIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LxAux2MeasIndex_Object = MibTableColumn
pmc1008mpMesrxfp1LxAux2MeasIndex = _Pmc1008mpMesrxfp1LxAux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 214, 1, 1),
    _Pmc1008mpMesrxfp1LxAux2MeasIndex_Type()
)
pmc1008mpMesrxfp1LxAux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxAux2MeasIndex.setStatus("deprecated")


class _Pmc1008mpMesrxfp1LxAux2MeasPortn_Type(Integer32):
    """Custom type pmc1008mpMesrxfp1LxAux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrxfp1LxAux2MeasPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrxfp1LxAux2MeasPortn_Object = MibTableColumn
pmc1008mpMesrxfp1LxAux2MeasPortn = _Pmc1008mpMesrxfp1LxAux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 214, 1, 2),
    _Pmc1008mpMesrxfp1LxAux2MeasPortn_Type()
)
pmc1008mpMesrxfp1LxAux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrxfp1LxAux2MeasPortn.setStatus("deprecated")
_Pmc1008mpMesrotx1AgingTable_Object = MibTable
pmc1008mpMesrotx1AgingTable = _Pmc1008mpMesrotx1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1AgingTable.setStatus("current")
_Pmc1008mpMesrotx1AgingEntry_Object = MibTableRow
pmc1008mpMesrotx1AgingEntry = _Pmc1008mpMesrotx1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 224, 1)
)
pmc1008mpMesrotx1AgingEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrotx1AgingIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1AgingEntry.setStatus("current")


class _Pmc1008mpMesrotx1AgingIndex_Type(Integer32):
    """Custom type pmc1008mpMesrotx1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrotx1AgingIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrotx1AgingIndex_Object = MibTableColumn
pmc1008mpMesrotx1AgingIndex = _Pmc1008mpMesrotx1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 224, 1, 1),
    _Pmc1008mpMesrotx1AgingIndex_Type()
)
pmc1008mpMesrotx1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1AgingIndex.setStatus("current")


class _Pmc1008mpMesrotx1AgingPortn_Type(Integer32):
    """Custom type pmc1008mpMesrotx1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrotx1AgingPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrotx1AgingPortn_Object = MibTableColumn
pmc1008mpMesrotx1AgingPortn = _Pmc1008mpMesrotx1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 224, 1, 2),
    _Pmc1008mpMesrotx1AgingPortn_Type()
)
pmc1008mpMesrotx1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1AgingPortn.setStatus("current")
_Pmc1008mpMesrotx1LaserTemperatureTable_Object = MibTable
pmc1008mpMesrotx1LaserTemperatureTable = _Pmc1008mpMesrotx1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1LaserTemperatureTable.setStatus("deprecated")
_Pmc1008mpMesrotx1LaserTemperatureEntry_Object = MibTableRow
pmc1008mpMesrotx1LaserTemperatureEntry = _Pmc1008mpMesrotx1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 225, 1)
)
pmc1008mpMesrotx1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrotx1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1LaserTemperatureEntry.setStatus("deprecated")


class _Pmc1008mpMesrotx1LaserTemperatureIndex_Type(Integer32):
    """Custom type pmc1008mpMesrotx1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrotx1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrotx1LaserTemperatureIndex_Object = MibTableColumn
pmc1008mpMesrotx1LaserTemperatureIndex = _Pmc1008mpMesrotx1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 225, 1, 1),
    _Pmc1008mpMesrotx1LaserTemperatureIndex_Type()
)
pmc1008mpMesrotx1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1LaserTemperatureIndex.setStatus("deprecated")


class _Pmc1008mpMesrotx1LaserTemperaturePortn_Type(Integer32):
    """Custom type pmc1008mpMesrotx1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrotx1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrotx1LaserTemperaturePortn_Object = MibTableColumn
pmc1008mpMesrotx1LaserTemperaturePortn = _Pmc1008mpMesrotx1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 225, 1, 2),
    _Pmc1008mpMesrotx1LaserTemperaturePortn_Type()
)
pmc1008mpMesrotx1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1LaserTemperaturePortn.setStatus("deprecated")
_Pmc1008mpMesrotx1FreqDeviationTable_Object = MibTable
pmc1008mpMesrotx1FreqDeviationTable = _Pmc1008mpMesrotx1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1FreqDeviationTable.setStatus("current")
_Pmc1008mpMesrotx1FreqDeviationEntry_Object = MibTableRow
pmc1008mpMesrotx1FreqDeviationEntry = _Pmc1008mpMesrotx1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 226, 1)
)
pmc1008mpMesrotx1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrotx1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1FreqDeviationEntry.setStatus("current")


class _Pmc1008mpMesrotx1FreqDeviationIndex_Type(Integer32):
    """Custom type pmc1008mpMesrotx1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrotx1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrotx1FreqDeviationIndex_Object = MibTableColumn
pmc1008mpMesrotx1FreqDeviationIndex = _Pmc1008mpMesrotx1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 226, 1, 1),
    _Pmc1008mpMesrotx1FreqDeviationIndex_Type()
)
pmc1008mpMesrotx1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1FreqDeviationIndex.setStatus("current")


class _Pmc1008mpMesrotx1FreqDeviationPortn_Type(Integer32):
    """Custom type pmc1008mpMesrotx1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrotx1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrotx1FreqDeviationPortn_Object = MibTableColumn
pmc1008mpMesrotx1FreqDeviationPortn = _Pmc1008mpMesrotx1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 226, 1, 2),
    _Pmc1008mpMesrotx1FreqDeviationPortn_Type()
)
pmc1008mpMesrotx1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1FreqDeviationPortn.setStatus("current")
_Pmc1008mpMesrotx1LaserWvlengthTable_Object = MibTable
pmc1008mpMesrotx1LaserWvlengthTable = _Pmc1008mpMesrotx1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1LaserWvlengthTable.setStatus("current")
_Pmc1008mpMesrotx1LaserWvlengthEntry_Object = MibTableRow
pmc1008mpMesrotx1LaserWvlengthEntry = _Pmc1008mpMesrotx1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 227, 1)
)
pmc1008mpMesrotx1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMesrotx1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1LaserWvlengthEntry.setStatus("current")


class _Pmc1008mpMesrotx1LaserWvlengthIndex_Type(Integer32):
    """Custom type pmc1008mpMesrotx1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMesrotx1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pmc1008mpMesrotx1LaserWvlengthIndex_Object = MibTableColumn
pmc1008mpMesrotx1LaserWvlengthIndex = _Pmc1008mpMesrotx1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 227, 1, 1),
    _Pmc1008mpMesrotx1LaserWvlengthIndex_Type()
)
pmc1008mpMesrotx1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1LaserWvlengthIndex.setStatus("current")


class _Pmc1008mpMesrotx1LaserWvlengthPortn_Type(Integer32):
    """Custom type pmc1008mpMesrotx1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1008mpMesrotx1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pmc1008mpMesrotx1LaserWvlengthPortn_Object = MibTableColumn
pmc1008mpMesrotx1LaserWvlengthPortn = _Pmc1008mpMesrotx1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 3, 3, 227, 1, 2),
    _Pmc1008mpMesrotx1LaserWvlengthPortn_Type()
)
pmc1008mpMesrotx1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMesrotx1LaserWvlengthPortn.setStatus("current")
_Pmc1008mpcounters_ObjectIdentity = ObjectIdentity
pmc1008mpcounters = _Pmc1008mpcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4)
)
_Pmc1008mpCntOther_ObjectIdentity = ObjectIdentity
pmc1008mpCntOther = _Pmc1008mpCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 1)
)
_Pmc1008mpCntClient_ObjectIdentity = ObjectIdentity
pmc1008mpCntClient = _Pmc1008mpCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2)
)
_Pmc1008mpCntupRaRemCntTable_Object = MibTable
pmc1008mpCntupRaRemCntTable = _Pmc1008mpCntupRaRemCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pmc1008mpCntupRaRemCntTable.setStatus("current")
_Pmc1008mpCntupRaRemCntEntry_Object = MibTableRow
pmc1008mpCntupRaRemCntEntry = _Pmc1008mpCntupRaRemCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 16, 1)
)
pmc1008mpCntupRaRemCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntupRaRemCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntupRaRemCntEntry.setStatus("current")


class _Pmc1008mpCntupRaRemCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntupRaRemCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntupRaRemCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntupRaRemCntIndex_Object = MibTableColumn
pmc1008mpCntupRaRemCntIndex = _Pmc1008mpCntupRaRemCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 16, 1, 1),
    _Pmc1008mpCntupRaRemCntIndex_Type()
)
pmc1008mpCntupRaRemCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRaRemCntIndex.setStatus("current")
_Pmc1008mpCntupRaRemCntValuePortn_Type = Counter32
_Pmc1008mpCntupRaRemCntValuePortn_Object = MibTableColumn
pmc1008mpCntupRaRemCntValuePortn = _Pmc1008mpCntupRaRemCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 16, 1, 2),
    _Pmc1008mpCntupRaRemCntValuePortn_Type()
)
pmc1008mpCntupRaRemCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRaRemCntValuePortn.setStatus("current")
_Pmc1008mpCntupRaRemCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntupRaRemCntErrorPortn_Object = MibTableColumn
pmc1008mpCntupRaRemCntErrorPortn = _Pmc1008mpCntupRaRemCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 16, 1, 3),
    _Pmc1008mpCntupRaRemCntErrorPortn_Type()
)
pmc1008mpCntupRaRemCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRaRemCntErrorPortn.setStatus("current")
_Pmc1008mpCntupRaRemCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntupRaRemCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntupRaRemCntOverloadPortn = _Pmc1008mpCntupRaRemCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 16, 1, 4),
    _Pmc1008mpCntupRaRemCntOverloadPortn_Type()
)
pmc1008mpCntupRaRemCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRaRemCntOverloadPortn.setStatus("current")
_Pmc1008mpCntupRaInsCntTable_Object = MibTable
pmc1008mpCntupRaInsCntTable = _Pmc1008mpCntupRaInsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 24)
)
if mibBuilder.loadTexts:
    pmc1008mpCntupRaInsCntTable.setStatus("current")
_Pmc1008mpCntupRaInsCntEntry_Object = MibTableRow
pmc1008mpCntupRaInsCntEntry = _Pmc1008mpCntupRaInsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 24, 1)
)
pmc1008mpCntupRaInsCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntupRaInsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntupRaInsCntEntry.setStatus("current")


class _Pmc1008mpCntupRaInsCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntupRaInsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntupRaInsCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntupRaInsCntIndex_Object = MibTableColumn
pmc1008mpCntupRaInsCntIndex = _Pmc1008mpCntupRaInsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 24, 1, 1),
    _Pmc1008mpCntupRaInsCntIndex_Type()
)
pmc1008mpCntupRaInsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRaInsCntIndex.setStatus("current")
_Pmc1008mpCntupRaInsCntValuePortn_Type = Counter32
_Pmc1008mpCntupRaInsCntValuePortn_Object = MibTableColumn
pmc1008mpCntupRaInsCntValuePortn = _Pmc1008mpCntupRaInsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 24, 1, 2),
    _Pmc1008mpCntupRaInsCntValuePortn_Type()
)
pmc1008mpCntupRaInsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRaInsCntValuePortn.setStatus("current")
_Pmc1008mpCntupRaInsCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntupRaInsCntErrorPortn_Object = MibTableColumn
pmc1008mpCntupRaInsCntErrorPortn = _Pmc1008mpCntupRaInsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 24, 1, 3),
    _Pmc1008mpCntupRaInsCntErrorPortn_Type()
)
pmc1008mpCntupRaInsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRaInsCntErrorPortn.setStatus("current")
_Pmc1008mpCntupRaInsCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntupRaInsCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntupRaInsCntOverloadPortn = _Pmc1008mpCntupRaInsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 24, 1, 4),
    _Pmc1008mpCntupRaInsCntOverloadPortn_Type()
)
pmc1008mpCntupRaInsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRaInsCntOverloadPortn.setStatus("current")
_Pmc1008mpCntupRdErrCntTable_Object = MibTable
pmc1008mpCntupRdErrCntTable = _Pmc1008mpCntupRdErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pmc1008mpCntupRdErrCntTable.setStatus("current")
_Pmc1008mpCntupRdErrCntEntry_Object = MibTableRow
pmc1008mpCntupRdErrCntEntry = _Pmc1008mpCntupRdErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 32, 1)
)
pmc1008mpCntupRdErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntupRdErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntupRdErrCntEntry.setStatus("current")


class _Pmc1008mpCntupRdErrCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntupRdErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntupRdErrCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntupRdErrCntIndex_Object = MibTableColumn
pmc1008mpCntupRdErrCntIndex = _Pmc1008mpCntupRdErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 32, 1, 1),
    _Pmc1008mpCntupRdErrCntIndex_Type()
)
pmc1008mpCntupRdErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRdErrCntIndex.setStatus("current")
_Pmc1008mpCntupRdErrCntValuePortn_Type = Counter32
_Pmc1008mpCntupRdErrCntValuePortn_Object = MibTableColumn
pmc1008mpCntupRdErrCntValuePortn = _Pmc1008mpCntupRdErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 32, 1, 2),
    _Pmc1008mpCntupRdErrCntValuePortn_Type()
)
pmc1008mpCntupRdErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRdErrCntValuePortn.setStatus("current")
_Pmc1008mpCntupRdErrCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntupRdErrCntErrorPortn_Object = MibTableColumn
pmc1008mpCntupRdErrCntErrorPortn = _Pmc1008mpCntupRdErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 32, 1, 3),
    _Pmc1008mpCntupRdErrCntErrorPortn_Type()
)
pmc1008mpCntupRdErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRdErrCntErrorPortn.setStatus("current")
_Pmc1008mpCntupRdErrCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntupRdErrCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntupRdErrCntOverloadPortn = _Pmc1008mpCntupRdErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 32, 1, 4),
    _Pmc1008mpCntupRdErrCntOverloadPortn_Type()
)
pmc1008mpCntupRdErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupRdErrCntOverloadPortn.setStatus("current")
_Pmc1008mpCntupTimCntTable_Object = MibTable
pmc1008mpCntupTimCntTable = _Pmc1008mpCntupTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 40)
)
if mibBuilder.loadTexts:
    pmc1008mpCntupTimCntTable.setStatus("current")
_Pmc1008mpCntupTimCntEntry_Object = MibTableRow
pmc1008mpCntupTimCntEntry = _Pmc1008mpCntupTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 40, 1)
)
pmc1008mpCntupTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntupTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntupTimCntEntry.setStatus("current")


class _Pmc1008mpCntupTimCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntupTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntupTimCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntupTimCntIndex_Object = MibTableColumn
pmc1008mpCntupTimCntIndex = _Pmc1008mpCntupTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 40, 1, 1),
    _Pmc1008mpCntupTimCntIndex_Type()
)
pmc1008mpCntupTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupTimCntIndex.setStatus("current")
_Pmc1008mpCntupTimCntValuePortn_Type = Counter32
_Pmc1008mpCntupTimCntValuePortn_Object = MibTableColumn
pmc1008mpCntupTimCntValuePortn = _Pmc1008mpCntupTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 40, 1, 2),
    _Pmc1008mpCntupTimCntValuePortn_Type()
)
pmc1008mpCntupTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupTimCntValuePortn.setStatus("current")
_Pmc1008mpCntupTimCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntupTimCntErrorPortn_Object = MibTableColumn
pmc1008mpCntupTimCntErrorPortn = _Pmc1008mpCntupTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 40, 1, 3),
    _Pmc1008mpCntupTimCntErrorPortn_Type()
)
pmc1008mpCntupTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupTimCntErrorPortn.setStatus("current")
_Pmc1008mpCntupTimCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntupTimCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntupTimCntOverloadPortn = _Pmc1008mpCntupTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 40, 1, 4),
    _Pmc1008mpCntupTimCntOverloadPortn_Type()
)
pmc1008mpCntupTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupTimCntOverloadPortn.setStatus("current")
_Pmc1008mpCntupCvErrCntTable_Object = MibTable
pmc1008mpCntupCvErrCntTable = _Pmc1008mpCntupCvErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 48)
)
if mibBuilder.loadTexts:
    pmc1008mpCntupCvErrCntTable.setStatus("current")
_Pmc1008mpCntupCvErrCntEntry_Object = MibTableRow
pmc1008mpCntupCvErrCntEntry = _Pmc1008mpCntupCvErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 48, 1)
)
pmc1008mpCntupCvErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntupCvErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntupCvErrCntEntry.setStatus("current")


class _Pmc1008mpCntupCvErrCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntupCvErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntupCvErrCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntupCvErrCntIndex_Object = MibTableColumn
pmc1008mpCntupCvErrCntIndex = _Pmc1008mpCntupCvErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 48, 1, 1),
    _Pmc1008mpCntupCvErrCntIndex_Type()
)
pmc1008mpCntupCvErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupCvErrCntIndex.setStatus("current")
_Pmc1008mpCntupCvErrCntValuePortn_Type = Counter32
_Pmc1008mpCntupCvErrCntValuePortn_Object = MibTableColumn
pmc1008mpCntupCvErrCntValuePortn = _Pmc1008mpCntupCvErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 48, 1, 2),
    _Pmc1008mpCntupCvErrCntValuePortn_Type()
)
pmc1008mpCntupCvErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupCvErrCntValuePortn.setStatus("current")
_Pmc1008mpCntupCvErrCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntupCvErrCntErrorPortn_Object = MibTableColumn
pmc1008mpCntupCvErrCntErrorPortn = _Pmc1008mpCntupCvErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 48, 1, 3),
    _Pmc1008mpCntupCvErrCntErrorPortn_Type()
)
pmc1008mpCntupCvErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupCvErrCntErrorPortn.setStatus("current")
_Pmc1008mpCntupCvErrCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntupCvErrCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntupCvErrCntOverloadPortn = _Pmc1008mpCntupCvErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 48, 1, 4),
    _Pmc1008mpCntupCvErrCntOverloadPortn_Type()
)
pmc1008mpCntupCvErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntupCvErrCntOverloadPortn.setStatus("current")
_Pmc1008mpCntdwCbipCntTable_Object = MibTable
pmc1008mpCntdwCbipCntTable = _Pmc1008mpCntdwCbipCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 64)
)
if mibBuilder.loadTexts:
    pmc1008mpCntdwCbipCntTable.setStatus("current")
_Pmc1008mpCntdwCbipCntEntry_Object = MibTableRow
pmc1008mpCntdwCbipCntEntry = _Pmc1008mpCntdwCbipCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 64, 1)
)
pmc1008mpCntdwCbipCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntdwCbipCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntdwCbipCntEntry.setStatus("current")


class _Pmc1008mpCntdwCbipCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntdwCbipCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntdwCbipCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntdwCbipCntIndex_Object = MibTableColumn
pmc1008mpCntdwCbipCntIndex = _Pmc1008mpCntdwCbipCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 64, 1, 1),
    _Pmc1008mpCntdwCbipCntIndex_Type()
)
pmc1008mpCntdwCbipCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdwCbipCntIndex.setStatus("current")
_Pmc1008mpCntdwCbipCntValuePortn_Type = Counter32
_Pmc1008mpCntdwCbipCntValuePortn_Object = MibTableColumn
pmc1008mpCntdwCbipCntValuePortn = _Pmc1008mpCntdwCbipCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 64, 1, 2),
    _Pmc1008mpCntdwCbipCntValuePortn_Type()
)
pmc1008mpCntdwCbipCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdwCbipCntValuePortn.setStatus("current")
_Pmc1008mpCntdwCbipCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntdwCbipCntErrorPortn_Object = MibTableColumn
pmc1008mpCntdwCbipCntErrorPortn = _Pmc1008mpCntdwCbipCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 64, 1, 3),
    _Pmc1008mpCntdwCbipCntErrorPortn_Type()
)
pmc1008mpCntdwCbipCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdwCbipCntErrorPortn.setStatus("current")
_Pmc1008mpCntdwCbipCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntdwCbipCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntdwCbipCntOverloadPortn = _Pmc1008mpCntdwCbipCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 64, 1, 4),
    _Pmc1008mpCntdwCbipCntOverloadPortn_Type()
)
pmc1008mpCntdwCbipCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdwCbipCntOverloadPortn.setStatus("current")
_Pmc1008mpCntdwTimCntTable_Object = MibTable
pmc1008mpCntdwTimCntTable = _Pmc1008mpCntdwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 72)
)
if mibBuilder.loadTexts:
    pmc1008mpCntdwTimCntTable.setStatus("current")
_Pmc1008mpCntdwTimCntEntry_Object = MibTableRow
pmc1008mpCntdwTimCntEntry = _Pmc1008mpCntdwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 72, 1)
)
pmc1008mpCntdwTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntdwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntdwTimCntEntry.setStatus("current")


class _Pmc1008mpCntdwTimCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntdwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntdwTimCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntdwTimCntIndex_Object = MibTableColumn
pmc1008mpCntdwTimCntIndex = _Pmc1008mpCntdwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 72, 1, 1),
    _Pmc1008mpCntdwTimCntIndex_Type()
)
pmc1008mpCntdwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdwTimCntIndex.setStatus("current")
_Pmc1008mpCntdwTimCntValuePortn_Type = Counter32
_Pmc1008mpCntdwTimCntValuePortn_Object = MibTableColumn
pmc1008mpCntdwTimCntValuePortn = _Pmc1008mpCntdwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 72, 1, 2),
    _Pmc1008mpCntdwTimCntValuePortn_Type()
)
pmc1008mpCntdwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdwTimCntValuePortn.setStatus("current")
_Pmc1008mpCntdwTimCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntdwTimCntErrorPortn_Object = MibTableColumn
pmc1008mpCntdwTimCntErrorPortn = _Pmc1008mpCntdwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 72, 1, 3),
    _Pmc1008mpCntdwTimCntErrorPortn_Type()
)
pmc1008mpCntdwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdwTimCntErrorPortn.setStatus("current")
_Pmc1008mpCntdwTimCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntdwTimCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntdwTimCntOverloadPortn = _Pmc1008mpCntdwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 2, 72, 1, 4),
    _Pmc1008mpCntdwTimCntOverloadPortn_Type()
)
pmc1008mpCntdwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdwTimCntOverloadPortn.setStatus("current")
_Pmc1008mpCntLine_ObjectIdentity = ObjectIdentity
pmc1008mpCntLine = _Pmc1008mpCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3)
)
_Pmc1008mpCntdfrmB1ErrCntTable_Object = MibTable
pmc1008mpCntdfrmB1ErrCntTable = _Pmc1008mpCntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmB1ErrCntTable.setStatus("current")
_Pmc1008mpCntdfrmB1ErrCntEntry_Object = MibTableRow
pmc1008mpCntdfrmB1ErrCntEntry = _Pmc1008mpCntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 152, 1)
)
pmc1008mpCntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmB1ErrCntEntry.setStatus("current")


class _Pmc1008mpCntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntdfrmB1ErrCntIndex_Object = MibTableColumn
pmc1008mpCntdfrmB1ErrCntIndex = _Pmc1008mpCntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 152, 1, 1),
    _Pmc1008mpCntdfrmB1ErrCntIndex_Type()
)
pmc1008mpCntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmB1ErrCntIndex.setStatus("current")
_Pmc1008mpCntdfrmB1ErrCntValuePortn_Type = Counter32
_Pmc1008mpCntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pmc1008mpCntdfrmB1ErrCntValuePortn = _Pmc1008mpCntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 152, 1, 2),
    _Pmc1008mpCntdfrmB1ErrCntValuePortn_Type()
)
pmc1008mpCntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmB1ErrCntValuePortn.setStatus("current")
_Pmc1008mpCntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pmc1008mpCntdfrmB1ErrCntErrorPortn = _Pmc1008mpCntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 152, 1, 3),
    _Pmc1008mpCntdfrmB1ErrCntErrorPortn_Type()
)
pmc1008mpCntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pmc1008mpCntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntdfrmB1ErrCntOverloadPortn = _Pmc1008mpCntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 152, 1, 4),
    _Pmc1008mpCntdfrmB1ErrCntOverloadPortn_Type()
)
pmc1008mpCntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pmc1008mpCntdfrmTimCntTable_Object = MibTable
pmc1008mpCntdfrmTimCntTable = _Pmc1008mpCntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmTimCntTable.setStatus("current")
_Pmc1008mpCntdfrmTimCntEntry_Object = MibTableRow
pmc1008mpCntdfrmTimCntEntry = _Pmc1008mpCntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 153, 1)
)
pmc1008mpCntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmTimCntEntry.setStatus("current")


class _Pmc1008mpCntdfrmTimCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntdfrmTimCntIndex_Object = MibTableColumn
pmc1008mpCntdfrmTimCntIndex = _Pmc1008mpCntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 153, 1, 1),
    _Pmc1008mpCntdfrmTimCntIndex_Type()
)
pmc1008mpCntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmTimCntIndex.setStatus("current")
_Pmc1008mpCntdfrmTimCntValuePortn_Type = Counter32
_Pmc1008mpCntdfrmTimCntValuePortn_Object = MibTableColumn
pmc1008mpCntdfrmTimCntValuePortn = _Pmc1008mpCntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 153, 1, 2),
    _Pmc1008mpCntdfrmTimCntValuePortn_Type()
)
pmc1008mpCntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmTimCntValuePortn.setStatus("current")
_Pmc1008mpCntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntdfrmTimCntErrorPortn_Object = MibTableColumn
pmc1008mpCntdfrmTimCntErrorPortn = _Pmc1008mpCntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 153, 1, 3),
    _Pmc1008mpCntdfrmTimCntErrorPortn_Type()
)
pmc1008mpCntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmTimCntErrorPortn.setStatus("current")
_Pmc1008mpCntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntdfrmTimCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntdfrmTimCntOverloadPortn = _Pmc1008mpCntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 153, 1, 4),
    _Pmc1008mpCntdfrmTimCntOverloadPortn_Type()
)
pmc1008mpCntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmTimCntOverloadPortn.setStatus("current")
_Pmc1008mpCntdfrmPrimLineErrCntTable_Object = MibTable
pmc1008mpCntdfrmPrimLineErrCntTable = _Pmc1008mpCntdfrmPrimLineErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 154)
)
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmPrimLineErrCntTable.setStatus("current")
_Pmc1008mpCntdfrmPrimLineErrCntEntry_Object = MibTableRow
pmc1008mpCntdfrmPrimLineErrCntEntry = _Pmc1008mpCntdfrmPrimLineErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 154, 1)
)
pmc1008mpCntdfrmPrimLineErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCntdfrmPrimLineErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmPrimLineErrCntEntry.setStatus("current")


class _Pmc1008mpCntdfrmPrimLineErrCntIndex_Type(Integer32):
    """Custom type pmc1008mpCntdfrmPrimLineErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCntdfrmPrimLineErrCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpCntdfrmPrimLineErrCntIndex_Object = MibTableColumn
pmc1008mpCntdfrmPrimLineErrCntIndex = _Pmc1008mpCntdfrmPrimLineErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 154, 1, 1),
    _Pmc1008mpCntdfrmPrimLineErrCntIndex_Type()
)
pmc1008mpCntdfrmPrimLineErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmPrimLineErrCntIndex.setStatus("current")
_Pmc1008mpCntdfrmPrimLineErrCntValuePortn_Type = Counter32
_Pmc1008mpCntdfrmPrimLineErrCntValuePortn_Object = MibTableColumn
pmc1008mpCntdfrmPrimLineErrCntValuePortn = _Pmc1008mpCntdfrmPrimLineErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 154, 1, 2),
    _Pmc1008mpCntdfrmPrimLineErrCntValuePortn_Type()
)
pmc1008mpCntdfrmPrimLineErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmPrimLineErrCntValuePortn.setStatus("current")
_Pmc1008mpCntdfrmPrimLineErrCntErrorPortn_Type = EkiOnOff
_Pmc1008mpCntdfrmPrimLineErrCntErrorPortn_Object = MibTableColumn
pmc1008mpCntdfrmPrimLineErrCntErrorPortn = _Pmc1008mpCntdfrmPrimLineErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 154, 1, 3),
    _Pmc1008mpCntdfrmPrimLineErrCntErrorPortn_Type()
)
pmc1008mpCntdfrmPrimLineErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmPrimLineErrCntErrorPortn.setStatus("current")
_Pmc1008mpCntdfrmPrimLineErrCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpCntdfrmPrimLineErrCntOverloadPortn_Object = MibTableColumn
pmc1008mpCntdfrmPrimLineErrCntOverloadPortn = _Pmc1008mpCntdfrmPrimLineErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 3, 154, 1, 4),
    _Pmc1008mpCntdfrmPrimLineErrCntOverloadPortn_Type()
)
pmc1008mpCntdfrmPrimLineErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCntdfrmPrimLineErrCntOverloadPortn.setStatus("current")
_Pmc1008mpCntCountersReset_Type = EkiOnOff
_Pmc1008mpCntCountersReset_Object = MibScalar
pmc1008mpCntCountersReset = _Pmc1008mpCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 259),
    _Pmc1008mpCntCountersReset_Type()
)
pmc1008mpCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCntCountersReset.setStatus("current")
_Pmc1008mpCntCountersStop_Type = EkiOnOff
_Pmc1008mpCntCountersStop_Object = MibScalar
pmc1008mpCntCountersStop = _Pmc1008mpCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 4, 260),
    _Pmc1008mpCntCountersStop_Type()
)
pmc1008mpCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCntCountersStop.setStatus("current")
_Pmc1008mpcontrolsWrite_ObjectIdentity = ObjectIdentity
pmc1008mpcontrolsWrite = _Pmc1008mpcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6)
)
_Pmc1008mpCtrlOther_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlOther = _Pmc1008mpCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1)
)
_Pmc1008mpCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlconfMgnt1 = _Pmc1008mpCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 1)
)
_Pmc1008mpCtrlConf1Load1_Type = EkiOnOff
_Pmc1008mpCtrlConf1Load1_Object = MibScalar
pmc1008mpCtrlConf1Load1 = _Pmc1008mpCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 1, 1),
    _Pmc1008mpCtrlConf1Load1_Type()
)
pmc1008mpCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlConf1Load1.setStatus("current")
_Pmc1008mpCtrlConf2Load1_Type = EkiOnOff
_Pmc1008mpCtrlConf2Load1_Object = MibScalar
pmc1008mpCtrlConf2Load1 = _Pmc1008mpCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 1, 2),
    _Pmc1008mpCtrlConf2Load1_Type()
)
pmc1008mpCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlConf2Load1.setStatus("current")
_Pmc1008mpCtrlConf2Flash1_Type = EkiOnOff
_Pmc1008mpCtrlConf2Flash1_Object = MibScalar
pmc1008mpCtrlConf2Flash1 = _Pmc1008mpCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 1, 10),
    _Pmc1008mpCtrlConf2Flash1_Type()
)
pmc1008mpCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlConf2Flash1.setStatus("current")
_Pmc1008mpCtrlConf2Clear1_Type = EkiOnOff
_Pmc1008mpCtrlConf2Clear1_Object = MibScalar
pmc1008mpCtrlConf2Clear1 = _Pmc1008mpCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 1, 14),
    _Pmc1008mpCtrlConf2Clear1_Type()
)
pmc1008mpCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlConf2Clear1.setStatus("current")
_Pmc1008mpCtrlsynth4_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlsynth4 = _Pmc1008mpCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 4)
)
_Pmc1008mpCtrlCorrelatOn_Type = EkiOnOff
_Pmc1008mpCtrlCorrelatOn_Object = MibScalar
pmc1008mpCtrlCorrelatOn = _Pmc1008mpCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 4, 1),
    _Pmc1008mpCtrlCorrelatOn_Type()
)
pmc1008mpCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlCorrelatOn.setStatus("current")
_Pmc1008mpCtrlCorrelatOff_Type = EkiOnOff
_Pmc1008mpCtrlCorrelatOff_Object = MibScalar
pmc1008mpCtrlCorrelatOff = _Pmc1008mpCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 4, 2),
    _Pmc1008mpCtrlCorrelatOff_Type()
)
pmc1008mpCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlCorrelatOff.setStatus("current")
_Pmc1008mpCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlswMgnt = _Pmc1008mpCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 5)
)
_Pmc1008mpCtrlColdReset_Type = EkiOnOff
_Pmc1008mpCtrlColdReset_Object = MibScalar
pmc1008mpCtrlColdReset = _Pmc1008mpCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 5, 2),
    _Pmc1008mpCtrlColdReset_Type()
)
pmc1008mpCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlColdReset.setStatus("current")
_Pmc1008mpCtrlWarmReset_Type = EkiOnOff
_Pmc1008mpCtrlWarmReset_Object = MibScalar
pmc1008mpCtrlWarmReset = _Pmc1008mpCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 5, 3),
    _Pmc1008mpCtrlWarmReset_Type()
)
pmc1008mpCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlWarmReset.setStatus("current")
_Pmc1008mpCtrlLoadSwBank1_Type = EkiOnOff
_Pmc1008mpCtrlLoadSwBank1_Object = MibScalar
pmc1008mpCtrlLoadSwBank1 = _Pmc1008mpCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 5, 5),
    _Pmc1008mpCtrlLoadSwBank1_Type()
)
pmc1008mpCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlLoadSwBank1.setStatus("current")
_Pmc1008mpCtrlLoadSwBank2_Type = EkiOnOff
_Pmc1008mpCtrlLoadSwBank2_Object = MibScalar
pmc1008mpCtrlLoadSwBank2 = _Pmc1008mpCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 5, 6),
    _Pmc1008mpCtrlLoadSwBank2_Type()
)
pmc1008mpCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlLoadSwBank2.setStatus("current")
_Pmc1008mpCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlgwMgnt = _Pmc1008mpCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 6)
)
_Pmc1008mpCtrlCurrentGwReset_Type = EkiOnOff
_Pmc1008mpCtrlCurrentGwReset_Object = MibScalar
pmc1008mpCtrlCurrentGwReset = _Pmc1008mpCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 6, 1),
    _Pmc1008mpCtrlCurrentGwReset_Type()
)
pmc1008mpCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlCurrentGwReset.setStatus("current")
_Pmc1008mpCtrlLoadGwBank1_Type = EkiOnOff
_Pmc1008mpCtrlLoadGwBank1_Object = MibScalar
pmc1008mpCtrlLoadGwBank1 = _Pmc1008mpCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 6, 5),
    _Pmc1008mpCtrlLoadGwBank1_Type()
)
pmc1008mpCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlLoadGwBank1.setStatus("current")
_Pmc1008mpCtrlLoadGwBank2_Type = EkiOnOff
_Pmc1008mpCtrlLoadGwBank2_Object = MibScalar
pmc1008mpCtrlLoadGwBank2 = _Pmc1008mpCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 6, 6),
    _Pmc1008mpCtrlLoadGwBank2_Type()
)
pmc1008mpCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlLoadGwBank2.setStatus("current")
_Pmc1008mpCtrlLoadGwBank3_Type = EkiOnOff
_Pmc1008mpCtrlLoadGwBank3_Object = MibScalar
pmc1008mpCtrlLoadGwBank3 = _Pmc1008mpCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 6, 7),
    _Pmc1008mpCtrlLoadGwBank3_Type()
)
pmc1008mpCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlLoadGwBank3.setStatus("current")
_Pmc1008mpCtrlLoadGwBank4_Type = EkiOnOff
_Pmc1008mpCtrlLoadGwBank4_Object = MibScalar
pmc1008mpCtrlLoadGwBank4 = _Pmc1008mpCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 6, 8),
    _Pmc1008mpCtrlLoadGwBank4_Type()
)
pmc1008mpCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlLoadGwBank4.setStatus("current")
_Pmc1008mpCtrlledTest_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlledTest = _Pmc1008mpCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 192)
)
_Pmc1008mpCtrlGreenLed_Type = EkiOnOff
_Pmc1008mpCtrlGreenLed_Object = MibScalar
pmc1008mpCtrlGreenLed = _Pmc1008mpCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 192, 1),
    _Pmc1008mpCtrlGreenLed_Type()
)
pmc1008mpCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlGreenLed.setStatus("current")
_Pmc1008mpCtrlRedLed_Type = EkiOnOff
_Pmc1008mpCtrlRedLed_Object = MibScalar
pmc1008mpCtrlRedLed = _Pmc1008mpCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 192, 2),
    _Pmc1008mpCtrlRedLed_Type()
)
pmc1008mpCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlRedLed.setStatus("current")
_Pmc1008mpCtrlLedOff_Type = EkiOnOff
_Pmc1008mpCtrlLedOff_Object = MibScalar
pmc1008mpCtrlLedOff = _Pmc1008mpCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 192, 3),
    _Pmc1008mpCtrlLedOff_Type()
)
pmc1008mpCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlLedOff.setStatus("current")
_Pmc1008mpCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlmoduleOosMode = _Pmc1008mpCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 193)
)
_Pmc1008mpCtrlModuleOosMode_Type = EkiOnOff
_Pmc1008mpCtrlModuleOosMode_Object = MibScalar
pmc1008mpCtrlModuleOosMode = _Pmc1008mpCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 193, 1),
    _Pmc1008mpCtrlModuleOosMode_Type()
)
pmc1008mpCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlModuleOosMode.setStatus("current")
_Pmc1008mpCtrlmoduleDccMgnt_Type = Pmc1008mpDccMode
_Pmc1008mpCtrlmoduleDccMgnt_Object = MibScalar
pmc1008mpCtrlmoduleDccMgnt = _Pmc1008mpCtrlmoduleDccMgnt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 196),
    _Pmc1008mpCtrlmoduleDccMgnt_Type()
)
pmc1008mpCtrlmoduleDccMgnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlmoduleDccMgnt.setStatus("current")
_Pmc1008mpCtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlmaintenanceMode = _Pmc1008mpCtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 197)
)
_Pmc1008mpCtrlMaintenanceMode_Type = EkiOnOff
_Pmc1008mpCtrlMaintenanceMode_Object = MibScalar
pmc1008mpCtrlMaintenanceMode = _Pmc1008mpCtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 1, 197, 1),
    _Pmc1008mpCtrlMaintenanceMode_Type()
)
pmc1008mpCtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlMaintenanceMode.setStatus("current")
_Pmc1008mpCtrlClient_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlClient = _Pmc1008mpCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2)
)
_Pmc1008mpCtrlaccessLoopTable_Object = MibTable
pmc1008mpCtrlaccessLoopTable = _Pmc1008mpCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlaccessLoopTable.setStatus("current")
_Pmc1008mpCtrlaccessLoopEntry_Object = MibTableRow
pmc1008mpCtrlaccessLoopEntry = _Pmc1008mpCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 16, 1)
)
pmc1008mpCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlaccessLoopEntry.setStatus("current")


class _Pmc1008mpCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlaccessLoopIndex_Object = MibTableColumn
pmc1008mpCtrlaccessLoopIndex = _Pmc1008mpCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 16, 1, 1),
    _Pmc1008mpCtrlaccessLoopIndex_Type()
)
pmc1008mpCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlaccessLoopIndex.setStatus("current")
_Pmc1008mpCtrlaccessLoopPortn_Type = EkiState
_Pmc1008mpCtrlaccessLoopPortn_Object = MibTableColumn
pmc1008mpCtrlaccessLoopPortn = _Pmc1008mpCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 16, 1, 2),
    _Pmc1008mpCtrlaccessLoopPortn_Type()
)
pmc1008mpCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlaccessLoopPortn.setStatus("current")
_Pmc1008mpCtrlportOosModeTable_Object = MibTable
pmc1008mpCtrlportOosModeTable = _Pmc1008mpCtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlportOosModeTable.setStatus("current")
_Pmc1008mpCtrlportOosModeEntry_Object = MibTableRow
pmc1008mpCtrlportOosModeEntry = _Pmc1008mpCtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 18, 1)
)
pmc1008mpCtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlportOosModeEntry.setStatus("current")


class _Pmc1008mpCtrlportOosModeIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlportOosModeIndex_Object = MibTableColumn
pmc1008mpCtrlportOosModeIndex = _Pmc1008mpCtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 18, 1, 1),
    _Pmc1008mpCtrlportOosModeIndex_Type()
)
pmc1008mpCtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlportOosModeIndex.setStatus("current")
_Pmc1008mpCtrlportOosModePortn_Type = EkiState
_Pmc1008mpCtrlportOosModePortn_Object = MibTableColumn
pmc1008mpCtrlportOosModePortn = _Pmc1008mpCtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 18, 1, 2),
    _Pmc1008mpCtrlportOosModePortn_Type()
)
pmc1008mpCtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlportOosModePortn.setStatus("current")
_Pmc1008mpCtrlsfpOnCtrlTable_Object = MibTable
pmc1008mpCtrlsfpOnCtrlTable = _Pmc1008mpCtrlsfpOnCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 19)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlsfpOnCtrlTable.setStatus("current")
_Pmc1008mpCtrlsfpOnCtrlEntry_Object = MibTableRow
pmc1008mpCtrlsfpOnCtrlEntry = _Pmc1008mpCtrlsfpOnCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 19, 1)
)
pmc1008mpCtrlsfpOnCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlsfpOnCtrlIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlsfpOnCtrlEntry.setStatus("current")


class _Pmc1008mpCtrlsfpOnCtrlIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlsfpOnCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlsfpOnCtrlIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlsfpOnCtrlIndex_Object = MibTableColumn
pmc1008mpCtrlsfpOnCtrlIndex = _Pmc1008mpCtrlsfpOnCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 19, 1, 1),
    _Pmc1008mpCtrlsfpOnCtrlIndex_Type()
)
pmc1008mpCtrlsfpOnCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlsfpOnCtrlIndex.setStatus("current")
_Pmc1008mpCtrlsfpOnCtrlPortn_Type = EkiState
_Pmc1008mpCtrlsfpOnCtrlPortn_Object = MibTableColumn
pmc1008mpCtrlsfpOnCtrlPortn = _Pmc1008mpCtrlsfpOnCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 19, 1, 2),
    _Pmc1008mpCtrlsfpOnCtrlPortn_Type()
)
pmc1008mpCtrlsfpOnCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlsfpOnCtrlPortn.setStatus("current")
_Pmc1008mpCtrlsfpOffCtrlTable_Object = MibTable
pmc1008mpCtrlsfpOffCtrlTable = _Pmc1008mpCtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlsfpOffCtrlTable.setStatus("current")
_Pmc1008mpCtrlsfpOffCtrlEntry_Object = MibTableRow
pmc1008mpCtrlsfpOffCtrlEntry = _Pmc1008mpCtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 20, 1)
)
pmc1008mpCtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlsfpOffCtrlEntry.setStatus("current")


class _Pmc1008mpCtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlsfpOffCtrlIndex_Object = MibTableColumn
pmc1008mpCtrlsfpOffCtrlIndex = _Pmc1008mpCtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 20, 1, 1),
    _Pmc1008mpCtrlsfpOffCtrlIndex_Type()
)
pmc1008mpCtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlsfpOffCtrlIndex.setStatus("current")
_Pmc1008mpCtrlsfpOffCtrlPortn_Type = EkiState
_Pmc1008mpCtrlsfpOffCtrlPortn_Object = MibTableColumn
pmc1008mpCtrlsfpOffCtrlPortn = _Pmc1008mpCtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 20, 1, 2),
    _Pmc1008mpCtrlsfpOffCtrlPortn_Type()
)
pmc1008mpCtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlsfpOffCtrlPortn.setStatus("current")
_Pmc1008mpCtrlcsfUpInsTable_Object = MibTable
pmc1008mpCtrlcsfUpInsTable = _Pmc1008mpCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlcsfUpInsTable.setStatus("current")
_Pmc1008mpCtrlcsfUpInsEntry_Object = MibTableRow
pmc1008mpCtrlcsfUpInsEntry = _Pmc1008mpCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 21, 1)
)
pmc1008mpCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlcsfUpInsEntry.setStatus("current")


class _Pmc1008mpCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlcsfUpInsIndex_Object = MibTableColumn
pmc1008mpCtrlcsfUpInsIndex = _Pmc1008mpCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 21, 1, 1),
    _Pmc1008mpCtrlcsfUpInsIndex_Type()
)
pmc1008mpCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlcsfUpInsIndex.setStatus("current")
_Pmc1008mpCtrlcsfUpInsPortn_Type = EkiState
_Pmc1008mpCtrlcsfUpInsPortn_Object = MibTableColumn
pmc1008mpCtrlcsfUpInsPortn = _Pmc1008mpCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 21, 1, 2),
    _Pmc1008mpCtrlcsfUpInsPortn_Type()
)
pmc1008mpCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlcsfUpInsPortn.setStatus("current")
_Pmc1008mpCtrlcaisDwInsTable_Object = MibTable
pmc1008mpCtrlcaisDwInsTable = _Pmc1008mpCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlcaisDwInsTable.setStatus("current")
_Pmc1008mpCtrlcaisDwInsEntry_Object = MibTableRow
pmc1008mpCtrlcaisDwInsEntry = _Pmc1008mpCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 22, 1)
)
pmc1008mpCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlcaisDwInsEntry.setStatus("current")


class _Pmc1008mpCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlcaisDwInsIndex_Object = MibTableColumn
pmc1008mpCtrlcaisDwInsIndex = _Pmc1008mpCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 22, 1, 1),
    _Pmc1008mpCtrlcaisDwInsIndex_Type()
)
pmc1008mpCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlcaisDwInsIndex.setStatus("current")
_Pmc1008mpCtrlcaisDwInsPortn_Type = EkiState
_Pmc1008mpCtrlcaisDwInsPortn_Object = MibTableColumn
pmc1008mpCtrlcaisDwInsPortn = _Pmc1008mpCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 22, 1, 2),
    _Pmc1008mpCtrlcaisDwInsPortn_Type()
)
pmc1008mpCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlcaisDwInsPortn.setStatus("current")
_Pmc1008mpCtrlclientAccessTermLoopTable_Object = MibTable
pmc1008mpCtrlclientAccessTermLoopTable = _Pmc1008mpCtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlclientAccessTermLoopTable.setStatus("current")
_Pmc1008mpCtrlclientAccessTermLoopEntry_Object = MibTableRow
pmc1008mpCtrlclientAccessTermLoopEntry = _Pmc1008mpCtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 26, 1)
)
pmc1008mpCtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlclientAccessTermLoopEntry.setStatus("current")


class _Pmc1008mpCtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlclientAccessTermLoopIndex_Object = MibTableColumn
pmc1008mpCtrlclientAccessTermLoopIndex = _Pmc1008mpCtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 26, 1, 1),
    _Pmc1008mpCtrlclientAccessTermLoopIndex_Type()
)
pmc1008mpCtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlclientAccessTermLoopIndex.setStatus("current")
_Pmc1008mpCtrlclientAccessTermLoopPortn_Type = EkiState
_Pmc1008mpCtrlclientAccessTermLoopPortn_Object = MibTableColumn
pmc1008mpCtrlclientAccessTermLoopPortn = _Pmc1008mpCtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 26, 1, 2),
    _Pmc1008mpCtrlclientAccessTermLoopPortn_Type()
)
pmc1008mpCtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlclientAccessTermLoopPortn.setStatus("current")
_Pmc1008mpCtrlprotocolTable_Object = MibTable
pmc1008mpCtrlprotocolTable = _Pmc1008mpCtrlprotocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 48)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlprotocolTable.setStatus("current")
_Pmc1008mpCtrlprotocolEntry_Object = MibTableRow
pmc1008mpCtrlprotocolEntry = _Pmc1008mpCtrlprotocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 48, 1)
)
pmc1008mpCtrlprotocolEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlprotocolIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlprotocolEntry.setStatus("current")


class _Pmc1008mpCtrlprotocolIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlprotocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlprotocolIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlprotocolIndex_Object = MibTableColumn
pmc1008mpCtrlprotocolIndex = _Pmc1008mpCtrlprotocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 48, 1, 1),
    _Pmc1008mpCtrlprotocolIndex_Type()
)
pmc1008mpCtrlprotocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlprotocolIndex.setStatus("current")
_Pmc1008mpCtrlprotocolPortn_Type = EkiProtocol
_Pmc1008mpCtrlprotocolPortn_Object = MibTableColumn
pmc1008mpCtrlprotocolPortn = _Pmc1008mpCtrlprotocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 48, 1, 2),
    _Pmc1008mpCtrlprotocolPortn_Type()
)
pmc1008mpCtrlprotocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlprotocolPortn.setStatus("current")
_Pmc1008mpCtrladddropTsClientARxProtectTable_Object = MibTable
pmc1008mpCtrladddropTsClientARxProtectTable = _Pmc1008mpCtrladddropTsClientARxProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 128)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrladddropTsClientARxProtectTable.setStatus("current")
_Pmc1008mpCtrladddropTsClientARxProtectEntry_Object = MibTableRow
pmc1008mpCtrladddropTsClientARxProtectEntry = _Pmc1008mpCtrladddropTsClientARxProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 128, 1)
)
pmc1008mpCtrladddropTsClientARxProtectEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrladddropTsClientARxProtectIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrladddropTsClientARxProtectEntry.setStatus("current")


class _Pmc1008mpCtrladddropTsClientARxProtectIndex_Type(Integer32):
    """Custom type pmc1008mpCtrladddropTsClientARxProtectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrladddropTsClientARxProtectIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrladddropTsClientARxProtectIndex_Object = MibTableColumn
pmc1008mpCtrladddropTsClientARxProtectIndex = _Pmc1008mpCtrladddropTsClientARxProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 128, 1, 1),
    _Pmc1008mpCtrladddropTsClientARxProtectIndex_Type()
)
pmc1008mpCtrladddropTsClientARxProtectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrladddropTsClientARxProtectIndex.setStatus("current")
_Pmc1008mpCtrladddropTsClientARxProtectPortn_Type = Pmc1008mpProtectionTimeSlot
_Pmc1008mpCtrladddropTsClientARxProtectPortn_Object = MibTableColumn
pmc1008mpCtrladddropTsClientARxProtectPortn = _Pmc1008mpCtrladddropTsClientARxProtectPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 128, 1, 2),
    _Pmc1008mpCtrladddropTsClientARxProtectPortn_Type()
)
pmc1008mpCtrladddropTsClientARxProtectPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrladddropTsClientARxProtectPortn.setStatus("current")
_Pmc1008mpCtrladddropTsPairModeTable_Object = MibTable
pmc1008mpCtrladddropTsPairModeTable = _Pmc1008mpCtrladddropTsPairModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 136)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrladddropTsPairModeTable.setStatus("current")
_Pmc1008mpCtrladddropTsPairModeEntry_Object = MibTableRow
pmc1008mpCtrladddropTsPairModeEntry = _Pmc1008mpCtrladddropTsPairModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 136, 1)
)
pmc1008mpCtrladddropTsPairModeEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrladddropTsPairModeIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrladddropTsPairModeEntry.setStatus("current")


class _Pmc1008mpCtrladddropTsPairModeIndex_Type(Integer32):
    """Custom type pmc1008mpCtrladddropTsPairModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrladddropTsPairModeIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrladddropTsPairModeIndex_Object = MibTableColumn
pmc1008mpCtrladddropTsPairModeIndex = _Pmc1008mpCtrladddropTsPairModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 136, 1, 1),
    _Pmc1008mpCtrladddropTsPairModeIndex_Type()
)
pmc1008mpCtrladddropTsPairModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrladddropTsPairModeIndex.setStatus("current")
_Pmc1008mpCtrladddropTsPairModePortn_Type = Pmc1008mpModeTimeSlot
_Pmc1008mpCtrladddropTsPairModePortn_Object = MibTableColumn
pmc1008mpCtrladddropTsPairModePortn = _Pmc1008mpCtrladddropTsPairModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 136, 1, 2),
    _Pmc1008mpCtrladddropTsPairModePortn_Type()
)
pmc1008mpCtrladddropTsPairModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrladddropTsPairModePortn.setStatus("current")
_Pmc1008mpCtrlclientResetAllCountTable_Object = MibTable
pmc1008mpCtrlclientResetAllCountTable = _Pmc1008mpCtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 271)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlclientResetAllCountTable.setStatus("current")
_Pmc1008mpCtrlclientResetAllCountEntry_Object = MibTableRow
pmc1008mpCtrlclientResetAllCountEntry = _Pmc1008mpCtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 271, 1)
)
pmc1008mpCtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlclientResetAllCountEntry.setStatus("current")


class _Pmc1008mpCtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlclientResetAllCountIndex_Object = MibTableColumn
pmc1008mpCtrlclientResetAllCountIndex = _Pmc1008mpCtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 271, 1, 1),
    _Pmc1008mpCtrlclientResetAllCountIndex_Type()
)
pmc1008mpCtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlclientResetAllCountIndex.setStatus("current")
_Pmc1008mpCtrlclientResetAllCountsPortn_Type = EkiState
_Pmc1008mpCtrlclientResetAllCountsPortn_Object = MibTableColumn
pmc1008mpCtrlclientResetAllCountsPortn = _Pmc1008mpCtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 2, 271, 1, 2),
    _Pmc1008mpCtrlclientResetAllCountsPortn_Type()
)
pmc1008mpCtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlclientResetAllCountsPortn.setStatus("current")
_Pmc1008mpCtrlLine_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlLine = _Pmc1008mpCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3)
)
_Pmc1008mpCtrlcommAccessLoop_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlcommAccessLoop = _Pmc1008mpCtrlcommAccessLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 64)
)
_Pmc1008mpCtrlCommAccessloop_Type = EkiOnOff
_Pmc1008mpCtrlCommAccessloop_Object = MibScalar
pmc1008mpCtrlCommAccessloop = _Pmc1008mpCtrlCommAccessloop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 64, 1),
    _Pmc1008mpCtrlCommAccessloop_Type()
)
pmc1008mpCtrlCommAccessloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlCommAccessloop.setStatus("deprecated")
_Pmc1008mpCtrllineLoop_ObjectIdentity = ObjectIdentity
pmc1008mpCtrllineLoop = _Pmc1008mpCtrllineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 66)
)
_Pmc1008mpCtrlLineLoop_Type = EkiOnOff
_Pmc1008mpCtrlLineLoop_Object = MibScalar
pmc1008mpCtrlLineLoop = _Pmc1008mpCtrlLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 66, 1),
    _Pmc1008mpCtrlLineLoop_Type()
)
pmc1008mpCtrlLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlLineLoop.setStatus("deprecated")
_Pmc1008mpCtrlmsAis_ObjectIdentity = ObjectIdentity
pmc1008mpCtrlmsAis = _Pmc1008mpCtrlmsAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 67)
)
_Pmc1008mpCtrlMsAis_Type = EkiOnOff
_Pmc1008mpCtrlMsAis_Object = MibScalar
pmc1008mpCtrlMsAis = _Pmc1008mpCtrlMsAis_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 67, 1),
    _Pmc1008mpCtrlMsAis_Type()
)
pmc1008mpCtrlMsAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlMsAis.setStatus("current")
_Pmc1008mpCtrlfecDisableTable_Object = MibTable
pmc1008mpCtrlfecDisableTable = _Pmc1008mpCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlfecDisableTable.setStatus("current")
_Pmc1008mpCtrlfecDisableEntry_Object = MibTableRow
pmc1008mpCtrlfecDisableEntry = _Pmc1008mpCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 69, 1)
)
pmc1008mpCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlfecDisableEntry.setStatus("current")


class _Pmc1008mpCtrlfecDisableIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlfecDisableIndex_Object = MibTableColumn
pmc1008mpCtrlfecDisableIndex = _Pmc1008mpCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 69, 1, 1),
    _Pmc1008mpCtrlfecDisableIndex_Type()
)
pmc1008mpCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlfecDisableIndex.setStatus("current")
_Pmc1008mpCtrlfecDisablePortn_Type = EkiState
_Pmc1008mpCtrlfecDisablePortn_Object = MibTableColumn
pmc1008mpCtrlfecDisablePortn = _Pmc1008mpCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 69, 1, 2),
    _Pmc1008mpCtrlfecDisablePortn_Type()
)
pmc1008mpCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlfecDisablePortn.setStatus("current")
_Pmc1008mpCtrllineOosModeTable_Object = MibTable
pmc1008mpCtrllineOosModeTable = _Pmc1008mpCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineOosModeTable.setStatus("current")
_Pmc1008mpCtrllineOosModeEntry_Object = MibTableRow
pmc1008mpCtrllineOosModeEntry = _Pmc1008mpCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 74, 1)
)
pmc1008mpCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineOosModeEntry.setStatus("current")


class _Pmc1008mpCtrllineOosModeIndex_Type(Integer32):
    """Custom type pmc1008mpCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrllineOosModeIndex_Object = MibTableColumn
pmc1008mpCtrllineOosModeIndex = _Pmc1008mpCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 74, 1, 1),
    _Pmc1008mpCtrllineOosModeIndex_Type()
)
pmc1008mpCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineOosModeIndex.setStatus("current")
_Pmc1008mpCtrllineOosModePortn_Type = EkiState
_Pmc1008mpCtrllineOosModePortn_Object = MibTableColumn
pmc1008mpCtrllineOosModePortn = _Pmc1008mpCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 74, 1, 2),
    _Pmc1008mpCtrllineOosModePortn_Type()
)
pmc1008mpCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineOosModePortn.setStatus("current")
_Pmc1008mpCtrlxfpOnoffTable_Object = MibTable
pmc1008mpCtrlxfpOnoffTable = _Pmc1008mpCtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpOnoffTable.setStatus("current")
_Pmc1008mpCtrlxfpOnoffEntry_Object = MibTableRow
pmc1008mpCtrlxfpOnoffEntry = _Pmc1008mpCtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 208, 1)
)
pmc1008mpCtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpOnoffEntry.setStatus("current")


class _Pmc1008mpCtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlxfpOnoffIndex_Object = MibTableColumn
pmc1008mpCtrlxfpOnoffIndex = _Pmc1008mpCtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 208, 1, 1),
    _Pmc1008mpCtrlxfpOnoffIndex_Type()
)
pmc1008mpCtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpOnoffIndex.setStatus("current")
_Pmc1008mpCtrlxfpOnoffPortn_Type = EkiState
_Pmc1008mpCtrlxfpOnoffPortn_Object = MibTableColumn
pmc1008mpCtrlxfpOnoffPortn = _Pmc1008mpCtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 208, 1, 2),
    _Pmc1008mpCtrlxfpOnoffPortn_Type()
)
pmc1008mpCtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpOnoffPortn.setStatus("current")
_Pmc1008mpCtrlxfpLineLoopTable_Object = MibTable
pmc1008mpCtrlxfpLineLoopTable = _Pmc1008mpCtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpLineLoopTable.setStatus("current")
_Pmc1008mpCtrlxfpLineLoopEntry_Object = MibTableRow
pmc1008mpCtrlxfpLineLoopEntry = _Pmc1008mpCtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 209, 1)
)
pmc1008mpCtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpLineLoopEntry.setStatus("current")


class _Pmc1008mpCtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlxfpLineLoopIndex_Object = MibTableColumn
pmc1008mpCtrlxfpLineLoopIndex = _Pmc1008mpCtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 209, 1, 1),
    _Pmc1008mpCtrlxfpLineLoopIndex_Type()
)
pmc1008mpCtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpLineLoopIndex.setStatus("current")
_Pmc1008mpCtrlxfpLineLoopPortn_Type = EkiState
_Pmc1008mpCtrlxfpLineLoopPortn_Object = MibTableColumn
pmc1008mpCtrlxfpLineLoopPortn = _Pmc1008mpCtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 209, 1, 2),
    _Pmc1008mpCtrlxfpLineLoopPortn_Type()
)
pmc1008mpCtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpLineLoopPortn.setStatus("current")
_Pmc1008mpCtrlxfpXfiLoopTable_Object = MibTable
pmc1008mpCtrlxfpXfiLoopTable = _Pmc1008mpCtrlxfpXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpXfiLoopTable.setStatus("current")
_Pmc1008mpCtrlxfpXfiLoopEntry_Object = MibTableRow
pmc1008mpCtrlxfpXfiLoopEntry = _Pmc1008mpCtrlxfpXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 210, 1)
)
pmc1008mpCtrlxfpXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlxfpXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpXfiLoopEntry.setStatus("current")


class _Pmc1008mpCtrlxfpXfiLoopIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlxfpXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlxfpXfiLoopIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlxfpXfiLoopIndex_Object = MibTableColumn
pmc1008mpCtrlxfpXfiLoopIndex = _Pmc1008mpCtrlxfpXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 210, 1, 1),
    _Pmc1008mpCtrlxfpXfiLoopIndex_Type()
)
pmc1008mpCtrlxfpXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpXfiLoopIndex.setStatus("current")
_Pmc1008mpCtrlxfpXfiLoopPortn_Type = EkiState
_Pmc1008mpCtrlxfpXfiLoopPortn_Object = MibTableColumn
pmc1008mpCtrlxfpXfiLoopPortn = _Pmc1008mpCtrlxfpXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 210, 1, 2),
    _Pmc1008mpCtrlxfpXfiLoopPortn_Type()
)
pmc1008mpCtrlxfpXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlxfpXfiLoopPortn.setStatus("current")
_Pmc1008mpCtrllineTunableChannelTable_Object = MibTable
pmc1008mpCtrllineTunableChannelTable = _Pmc1008mpCtrllineTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineTunableChannelTable.setStatus("current")
_Pmc1008mpCtrllineTunableChannelEntry_Object = MibTableRow
pmc1008mpCtrllineTunableChannelEntry = _Pmc1008mpCtrllineTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 212, 1)
)
pmc1008mpCtrllineTunableChannelEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrllineTunableChannelIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineTunableChannelEntry.setStatus("current")


class _Pmc1008mpCtrllineTunableChannelIndex_Type(Integer32):
    """Custom type pmc1008mpCtrllineTunableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrllineTunableChannelIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrllineTunableChannelIndex_Object = MibTableColumn
pmc1008mpCtrllineTunableChannelIndex = _Pmc1008mpCtrllineTunableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 212, 1, 1),
    _Pmc1008mpCtrllineTunableChannelIndex_Type()
)
pmc1008mpCtrllineTunableChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineTunableChannelIndex.setStatus("current")
_Pmc1008mpCtrllineTunableChannelPortn_Type = Pmc1008mpOtxChannel
_Pmc1008mpCtrllineTunableChannelPortn_Object = MibTableColumn
pmc1008mpCtrllineTunableChannelPortn = _Pmc1008mpCtrllineTunableChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 212, 1, 2),
    _Pmc1008mpCtrllineTunableChannelPortn_Type()
)
pmc1008mpCtrllineTunableChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineTunableChannelPortn.setStatus("current")
_Pmc1008mpCtrllinePhotodiodeModeTable_Object = MibTable
pmc1008mpCtrllinePhotodiodeModeTable = _Pmc1008mpCtrllinePhotodiodeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 213)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePhotodiodeModeTable.setStatus("current")
_Pmc1008mpCtrllinePhotodiodeModeEntry_Object = MibTableRow
pmc1008mpCtrllinePhotodiodeModeEntry = _Pmc1008mpCtrllinePhotodiodeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 213, 1)
)
pmc1008mpCtrllinePhotodiodeModeEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrllinePhotodiodeModeIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePhotodiodeModeEntry.setStatus("current")


class _Pmc1008mpCtrllinePhotodiodeModeIndex_Type(Integer32):
    """Custom type pmc1008mpCtrllinePhotodiodeModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrllinePhotodiodeModeIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrllinePhotodiodeModeIndex_Object = MibTableColumn
pmc1008mpCtrllinePhotodiodeModeIndex = _Pmc1008mpCtrllinePhotodiodeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 213, 1, 1),
    _Pmc1008mpCtrllinePhotodiodeModeIndex_Type()
)
pmc1008mpCtrllinePhotodiodeModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePhotodiodeModeIndex.setStatus("current")
_Pmc1008mpCtrllinePhotodiodeModePortn_Type = Pmc1008mpOtxMode
_Pmc1008mpCtrllinePhotodiodeModePortn_Object = MibTableColumn
pmc1008mpCtrllinePhotodiodeModePortn = _Pmc1008mpCtrllinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 213, 1, 2),
    _Pmc1008mpCtrllinePhotodiodeModePortn_Type()
)
pmc1008mpCtrllinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePhotodiodeModePortn.setStatus("current")
_Pmc1008mpCtrllinePhotodiodeValueTable_Object = MibTable
pmc1008mpCtrllinePhotodiodeValueTable = _Pmc1008mpCtrllinePhotodiodeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 214)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePhotodiodeValueTable.setStatus("current")
_Pmc1008mpCtrllinePhotodiodeValueEntry_Object = MibTableRow
pmc1008mpCtrllinePhotodiodeValueEntry = _Pmc1008mpCtrllinePhotodiodeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 214, 1)
)
pmc1008mpCtrllinePhotodiodeValueEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrllinePhotodiodeValueIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePhotodiodeValueEntry.setStatus("current")


class _Pmc1008mpCtrllinePhotodiodeValueIndex_Type(Integer32):
    """Custom type pmc1008mpCtrllinePhotodiodeValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrllinePhotodiodeValueIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrllinePhotodiodeValueIndex_Object = MibTableColumn
pmc1008mpCtrllinePhotodiodeValueIndex = _Pmc1008mpCtrllinePhotodiodeValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 214, 1, 1),
    _Pmc1008mpCtrllinePhotodiodeValueIndex_Type()
)
pmc1008mpCtrllinePhotodiodeValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePhotodiodeValueIndex.setStatus("current")
_Pmc1008mpCtrllinePhotodiodeValuePortn_Type = Pmc1008mpAdjustValue
_Pmc1008mpCtrllinePhotodiodeValuePortn_Object = MibTableColumn
pmc1008mpCtrllinePhotodiodeValuePortn = _Pmc1008mpCtrllinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 214, 1, 2),
    _Pmc1008mpCtrllinePhotodiodeValuePortn_Type()
)
pmc1008mpCtrllinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePhotodiodeValuePortn.setStatus("current")
_Pmc1008mpCtrllinePowerLaserTable_Object = MibTable
pmc1008mpCtrllinePowerLaserTable = _Pmc1008mpCtrllinePowerLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 215)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePowerLaserTable.setStatus("current")
_Pmc1008mpCtrllinePowerLaserEntry_Object = MibTableRow
pmc1008mpCtrllinePowerLaserEntry = _Pmc1008mpCtrllinePowerLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 215, 1)
)
pmc1008mpCtrllinePowerLaserEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrllinePowerLaserIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePowerLaserEntry.setStatus("current")


class _Pmc1008mpCtrllinePowerLaserIndex_Type(Integer32):
    """Custom type pmc1008mpCtrllinePowerLaserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrllinePowerLaserIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrllinePowerLaserIndex_Object = MibTableColumn
pmc1008mpCtrllinePowerLaserIndex = _Pmc1008mpCtrllinePowerLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 215, 1, 1),
    _Pmc1008mpCtrllinePowerLaserIndex_Type()
)
pmc1008mpCtrllinePowerLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePowerLaserIndex.setStatus("current")


class _Pmc1008mpCtrllinePowerLaserPortn_Type(Integer32):
    """Custom type pmc1008mpCtrllinePowerLaserPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pmc1008mpCtrllinePowerLaserPortn_Type.__name__ = "Integer32"
_Pmc1008mpCtrllinePowerLaserPortn_Object = MibTableColumn
pmc1008mpCtrllinePowerLaserPortn = _Pmc1008mpCtrllinePowerLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 215, 1, 2),
    _Pmc1008mpCtrllinePowerLaserPortn_Type()
)
pmc1008mpCtrllinePowerLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrllinePowerLaserPortn.setStatus("current")
_Pmc1008mpCtrlotxVlhResetTable_Object = MibTable
pmc1008mpCtrlotxVlhResetTable = _Pmc1008mpCtrlotxVlhResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 216)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlotxVlhResetTable.setStatus("current")
_Pmc1008mpCtrlotxVlhResetEntry_Object = MibTableRow
pmc1008mpCtrlotxVlhResetEntry = _Pmc1008mpCtrlotxVlhResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 216, 1)
)
pmc1008mpCtrlotxVlhResetEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrlotxVlhResetIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrlotxVlhResetEntry.setStatus("current")


class _Pmc1008mpCtrlotxVlhResetIndex_Type(Integer32):
    """Custom type pmc1008mpCtrlotxVlhResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrlotxVlhResetIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrlotxVlhResetIndex_Object = MibTableColumn
pmc1008mpCtrlotxVlhResetIndex = _Pmc1008mpCtrlotxVlhResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 216, 1, 1),
    _Pmc1008mpCtrlotxVlhResetIndex_Type()
)
pmc1008mpCtrlotxVlhResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrlotxVlhResetIndex.setStatus("current")
_Pmc1008mpCtrlOtxVlhResetPortn_Type = EkiOnOff
_Pmc1008mpCtrlOtxVlhResetPortn_Object = MibTableColumn
pmc1008mpCtrlOtxVlhResetPortn = _Pmc1008mpCtrlOtxVlhResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 216, 1, 2),
    _Pmc1008mpCtrlOtxVlhResetPortn_Type()
)
pmc1008mpCtrlOtxVlhResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrlOtxVlhResetPortn.setStatus("current")
_Pmc1008mpCtrllineAccessLoopTable_Object = MibTable
pmc1008mpCtrllineAccessLoopTable = _Pmc1008mpCtrllineAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 217)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineAccessLoopTable.setStatus("current")
_Pmc1008mpCtrllineAccessLoopEntry_Object = MibTableRow
pmc1008mpCtrllineAccessLoopEntry = _Pmc1008mpCtrllineAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 217, 1)
)
pmc1008mpCtrllineAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrllineAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineAccessLoopEntry.setStatus("current")


class _Pmc1008mpCtrllineAccessLoopIndex_Type(Integer32):
    """Custom type pmc1008mpCtrllineAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrllineAccessLoopIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrllineAccessLoopIndex_Object = MibTableColumn
pmc1008mpCtrllineAccessLoopIndex = _Pmc1008mpCtrllineAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 217, 1, 1),
    _Pmc1008mpCtrllineAccessLoopIndex_Type()
)
pmc1008mpCtrllineAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineAccessLoopIndex.setStatus("current")
_Pmc1008mpCtrllineAccessLoopPortn_Type = EkiState
_Pmc1008mpCtrllineAccessLoopPortn_Object = MibTableColumn
pmc1008mpCtrllineAccessLoopPortn = _Pmc1008mpCtrllineAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 217, 1, 2),
    _Pmc1008mpCtrllineAccessLoopPortn_Type()
)
pmc1008mpCtrllineAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineAccessLoopPortn.setStatus("current")
_Pmc1008mpCtrllineLoopTransceiverTable_Object = MibTable
pmc1008mpCtrllineLoopTransceiverTable = _Pmc1008mpCtrllineLoopTransceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 218)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineLoopTransceiverTable.setStatus("current")
_Pmc1008mpCtrllineLoopTransceiverEntry_Object = MibTableRow
pmc1008mpCtrllineLoopTransceiverEntry = _Pmc1008mpCtrllineLoopTransceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 218, 1)
)
pmc1008mpCtrllineLoopTransceiverEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrllineLoopTransceiverIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineLoopTransceiverEntry.setStatus("current")


class _Pmc1008mpCtrllineLoopTransceiverIndex_Type(Integer32):
    """Custom type pmc1008mpCtrllineLoopTransceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrllineLoopTransceiverIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrllineLoopTransceiverIndex_Object = MibTableColumn
pmc1008mpCtrllineLoopTransceiverIndex = _Pmc1008mpCtrllineLoopTransceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 218, 1, 1),
    _Pmc1008mpCtrllineLoopTransceiverIndex_Type()
)
pmc1008mpCtrllineLoopTransceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineLoopTransceiverIndex.setStatus("current")
_Pmc1008mpCtrllineLoopTransceiverPortn_Type = EkiState
_Pmc1008mpCtrllineLoopTransceiverPortn_Object = MibTableColumn
pmc1008mpCtrllineLoopTransceiverPortn = _Pmc1008mpCtrllineLoopTransceiverPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 218, 1, 2),
    _Pmc1008mpCtrllineLoopTransceiverPortn_Type()
)
pmc1008mpCtrllineLoopTransceiverPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineLoopTransceiverPortn.setStatus("current")
_Pmc1008mpCtrllineResetAllCountTable_Object = MibTable
pmc1008mpCtrllineResetAllCountTable = _Pmc1008mpCtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 335)
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineResetAllCountTable.setStatus("current")
_Pmc1008mpCtrllineResetAllCountEntry_Object = MibTableRow
pmc1008mpCtrllineResetAllCountEntry = _Pmc1008mpCtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 335, 1)
)
pmc1008mpCtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCtrllineResetAllCountEntry.setStatus("current")


class _Pmc1008mpCtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pmc1008mpCtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pmc1008mpCtrllineResetAllCountIndex_Object = MibTableColumn
pmc1008mpCtrllineResetAllCountIndex = _Pmc1008mpCtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 335, 1, 1),
    _Pmc1008mpCtrllineResetAllCountIndex_Type()
)
pmc1008mpCtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineResetAllCountIndex.setStatus("current")
_Pmc1008mpCtrllineResetAllCountsPortn_Type = EkiState
_Pmc1008mpCtrllineResetAllCountsPortn_Object = MibTableColumn
pmc1008mpCtrllineResetAllCountsPortn = _Pmc1008mpCtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 6, 3, 335, 1, 2),
    _Pmc1008mpCtrllineResetAllCountsPortn_Type()
)
pmc1008mpCtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCtrllineResetAllCountsPortn.setStatus("current")
_Pmc1008mpri_ObjectIdentity = ObjectIdentity
pmc1008mpri = _Pmc1008mpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7)
)
_Pmc1008mpriTable_ObjectIdentity = ObjectIdentity
pmc1008mpriTable = _Pmc1008mpriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 1)
)
_Pmc1008mpRinvSfpTable_Object = MibTable
pmc1008mpRinvSfpTable = _Pmc1008mpRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmc1008mpRinvSfpTable.setStatus("current")
_Pmc1008mpRinvSfpEntry_Object = MibTableRow
pmc1008mpRinvSfpEntry = _Pmc1008mpRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 1, 1, 1)
)
pmc1008mpRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpRinvSfpEntry.setStatus("current")


class _Pmc1008mpRinvSfpIndex_Type(Integer32):
    """Custom type pmc1008mpRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmc1008mpRinvSfpIndex_Type.__name__ = "Integer32"
_Pmc1008mpRinvSfpIndex_Object = MibTableColumn
pmc1008mpRinvSfpIndex = _Pmc1008mpRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 1, 1, 1, 1),
    _Pmc1008mpRinvSfpIndex_Type()
)
pmc1008mpRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpRinvSfpIndex.setStatus("current")
_Pmc1008mpRinvsfp_Type = DisplayString
_Pmc1008mpRinvsfp_Object = MibTableColumn
pmc1008mpRinvsfp = _Pmc1008mpRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 1, 1, 1, 2),
    _Pmc1008mpRinvsfp_Type()
)
pmc1008mpRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpRinvsfp.setStatus("current")
_Pmc1008mpRinvLineTable_Object = MibTable
pmc1008mpRinvLineTable = _Pmc1008mpRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmc1008mpRinvLineTable.setStatus("current")
_Pmc1008mpRinvLineEntry_Object = MibTableRow
pmc1008mpRinvLineEntry = _Pmc1008mpRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 1, 2, 1)
)
pmc1008mpRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpRinvLineEntry.setStatus("current")


class _Pmc1008mpRinvLineIndex_Type(Integer32):
    """Custom type pmc1008mpRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmc1008mpRinvLineIndex_Type.__name__ = "Integer32"
_Pmc1008mpRinvLineIndex_Object = MibTableColumn
pmc1008mpRinvLineIndex = _Pmc1008mpRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 1, 2, 1, 1),
    _Pmc1008mpRinvLineIndex_Type()
)
pmc1008mpRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpRinvLineIndex.setStatus("current")
_Pmc1008mpRinvxfpLine_Type = DisplayString
_Pmc1008mpRinvxfpLine_Object = MibTableColumn
pmc1008mpRinvxfpLine = _Pmc1008mpRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 1, 2, 1, 2),
    _Pmc1008mpRinvxfpLine_Type()
)
pmc1008mpRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpRinvxfpLine.setStatus("current")
_Pmc1008mpRinvReloadInventory_Type = EkiOnOff
_Pmc1008mpRinvReloadInventory_Object = MibScalar
pmc1008mpRinvReloadInventory = _Pmc1008mpRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 2),
    _Pmc1008mpRinvReloadInventory_Type()
)
pmc1008mpRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpRinvReloadInventory.setStatus("current")
_Pmc1008mpRinvHwPlatform_Type = DisplayString
_Pmc1008mpRinvHwPlatform_Object = MibScalar
pmc1008mpRinvHwPlatform = _Pmc1008mpRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 3),
    _Pmc1008mpRinvHwPlatform_Type()
)
pmc1008mpRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpRinvHwPlatform.setStatus("current")
_Pmc1008mpRinvModulePlatform_Type = DisplayString
_Pmc1008mpRinvModulePlatform_Object = MibScalar
pmc1008mpRinvModulePlatform = _Pmc1008mpRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 4),
    _Pmc1008mpRinvModulePlatform_Type()
)
pmc1008mpRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpRinvModulePlatform.setStatus("current")
_Pmc1008mpRinvSwPlatform_Type = DisplayString
_Pmc1008mpRinvSwPlatform_Object = MibScalar
pmc1008mpRinvSwPlatform = _Pmc1008mpRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 5),
    _Pmc1008mpRinvSwPlatform_Type()
)
pmc1008mpRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpRinvSwPlatform.setStatus("current")
_Pmc1008mpRinvGwPlatform_Type = DisplayString
_Pmc1008mpRinvGwPlatform_Object = MibScalar
pmc1008mpRinvGwPlatform = _Pmc1008mpRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 7, 6),
    _Pmc1008mpRinvGwPlatform_Type()
)
pmc1008mpRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpRinvGwPlatform.setStatus("current")
_Pmc1008mpdownload_ObjectIdentity = ObjectIdentity
pmc1008mpdownload = _Pmc1008mpdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8)
)
_Pmc1008mpDwlOther_ObjectIdentity = ObjectIdentity
pmc1008mpDwlOther = _Pmc1008mpDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1)
)
_Pmc1008mpDwlrestartProcess_ObjectIdentity = ObjectIdentity
pmc1008mpDwlrestartProcess = _Pmc1008mpDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 0)
)
_Pmc1008mpDwlWarmRestartProcessed_Type = EkiOnOff
_Pmc1008mpDwlWarmRestartProcessed_Object = MibScalar
pmc1008mpDwlWarmRestartProcessed = _Pmc1008mpDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 0, 1),
    _Pmc1008mpDwlWarmRestartProcessed_Type()
)
pmc1008mpDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlWarmRestartProcessed.setStatus("current")
_Pmc1008mpDwlColdRestartProcessed_Type = EkiOnOff
_Pmc1008mpDwlColdRestartProcessed_Object = MibScalar
pmc1008mpDwlColdRestartProcessed = _Pmc1008mpDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 0, 2),
    _Pmc1008mpDwlColdRestartProcessed_Type()
)
pmc1008mpDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlColdRestartProcessed.setStatus("current")
_Pmc1008mpDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pmc1008mpDwlswBanksUsed = _Pmc1008mpDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 1)
)
_Pmc1008mpDwlSwBank1Used_Type = EkiOnOff
_Pmc1008mpDwlSwBank1Used_Object = MibScalar
pmc1008mpDwlSwBank1Used = _Pmc1008mpDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 1, 1),
    _Pmc1008mpDwlSwBank1Used_Type()
)
pmc1008mpDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlSwBank1Used.setStatus("current")
_Pmc1008mpDwlSwBank2Used_Type = EkiOnOff
_Pmc1008mpDwlSwBank2Used_Object = MibScalar
pmc1008mpDwlSwBank2Used = _Pmc1008mpDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 1, 2),
    _Pmc1008mpDwlSwBank2Used_Type()
)
pmc1008mpDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlSwBank2Used.setStatus("current")
_Pmc1008mpDwlSwBank1Notempty_Type = EkiOnOff
_Pmc1008mpDwlSwBank1Notempty_Object = MibScalar
pmc1008mpDwlSwBank1Notempty = _Pmc1008mpDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 1, 5),
    _Pmc1008mpDwlSwBank1Notempty_Type()
)
pmc1008mpDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlSwBank1Notempty.setStatus("current")
_Pmc1008mpDwlSwBank2Notempty_Type = EkiOnOff
_Pmc1008mpDwlSwBank2Notempty_Object = MibScalar
pmc1008mpDwlSwBank2Notempty = _Pmc1008mpDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 1, 6),
    _Pmc1008mpDwlSwBank2Notempty_Type()
)
pmc1008mpDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlSwBank2Notempty.setStatus("current")
_Pmc1008mpDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pmc1008mpDwlgwBanksUsed = _Pmc1008mpDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 2)
)
_Pmc1008mpDwlGwBank1Used_Type = EkiOnOff
_Pmc1008mpDwlGwBank1Used_Object = MibScalar
pmc1008mpDwlGwBank1Used = _Pmc1008mpDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 2, 1),
    _Pmc1008mpDwlGwBank1Used_Type()
)
pmc1008mpDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlGwBank1Used.setStatus("current")
_Pmc1008mpDwlGwBank2Used_Type = EkiOnOff
_Pmc1008mpDwlGwBank2Used_Object = MibScalar
pmc1008mpDwlGwBank2Used = _Pmc1008mpDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 2, 2),
    _Pmc1008mpDwlGwBank2Used_Type()
)
pmc1008mpDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlGwBank2Used.setStatus("current")
_Pmc1008mpDwlGwBank3Used_Type = EkiOnOff
_Pmc1008mpDwlGwBank3Used_Object = MibScalar
pmc1008mpDwlGwBank3Used = _Pmc1008mpDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 2, 3),
    _Pmc1008mpDwlGwBank3Used_Type()
)
pmc1008mpDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlGwBank3Used.setStatus("current")
_Pmc1008mpDwlGwBank4Used_Type = EkiOnOff
_Pmc1008mpDwlGwBank4Used_Object = MibScalar
pmc1008mpDwlGwBank4Used = _Pmc1008mpDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 2, 4),
    _Pmc1008mpDwlGwBank4Used_Type()
)
pmc1008mpDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlGwBank4Used.setStatus("current")
_Pmc1008mpDwlGwBank1Notempty_Type = EkiOnOff
_Pmc1008mpDwlGwBank1Notempty_Object = MibScalar
pmc1008mpDwlGwBank1Notempty = _Pmc1008mpDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 2, 5),
    _Pmc1008mpDwlGwBank1Notempty_Type()
)
pmc1008mpDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlGwBank1Notempty.setStatus("current")
_Pmc1008mpDwlGwBank2Notempty_Type = EkiOnOff
_Pmc1008mpDwlGwBank2Notempty_Object = MibScalar
pmc1008mpDwlGwBank2Notempty = _Pmc1008mpDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 2, 6),
    _Pmc1008mpDwlGwBank2Notempty_Type()
)
pmc1008mpDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlGwBank2Notempty.setStatus("current")
_Pmc1008mpDwlGwBank3Notempty_Type = EkiOnOff
_Pmc1008mpDwlGwBank3Notempty_Object = MibScalar
pmc1008mpDwlGwBank3Notempty = _Pmc1008mpDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 2, 7),
    _Pmc1008mpDwlGwBank3Notempty_Type()
)
pmc1008mpDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlGwBank3Notempty.setStatus("current")
_Pmc1008mpDwlGwBank4Notempty_Type = EkiOnOff
_Pmc1008mpDwlGwBank4Notempty_Object = MibScalar
pmc1008mpDwlGwBank4Notempty = _Pmc1008mpDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 1, 2, 8),
    _Pmc1008mpDwlGwBank4Notempty_Type()
)
pmc1008mpDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpDwlGwBank4Notempty.setStatus("current")
_Pmc1008mpDwlClient_ObjectIdentity = ObjectIdentity
pmc1008mpDwlClient = _Pmc1008mpDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 2)
)
_Pmc1008mpDwlLine_ObjectIdentity = ObjectIdentity
pmc1008mpDwlLine = _Pmc1008mpDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 8, 3)
)
_Pmc1008mpConfig_ObjectIdentity = ObjectIdentity
pmc1008mpConfig = _Pmc1008mpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9)
)
_Pmc1008mpCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pmc1008mpCfgAccessCAisCsf = _Pmc1008mpCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1)
)
_Pmc1008mpCfgClientcaiscsfTable_Object = MibTable
pmc1008mpCfgClientcaiscsfTable = _Pmc1008mpCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgClientcaiscsfTable.setStatus("current")
_Pmc1008mpCfgClientcaiscsfEntry_Object = MibTableRow
pmc1008mpCfgClientcaiscsfEntry = _Pmc1008mpCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1, 1)
)
pmc1008mpCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgClientcaiscsfEntry.setStatus("current")


class _Pmc1008mpCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pmc1008mpCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pmc1008mpCfgClientcaiscsfIndex_Object = MibTableColumn
pmc1008mpCfgClientcaiscsfIndex = _Pmc1008mpCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1, 1, 1),
    _Pmc1008mpCfgClientcaiscsfIndex_Type()
)
pmc1008mpCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgClientcaiscsfIndex.setStatus("current")


class _Pmc1008mpCfgCAisModePortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgCAisModePortn_Object = MibTableColumn
pmc1008mpCfgCAisModePortn = _Pmc1008mpCfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1, 1, 3),
    _Pmc1008mpCfgCAisModePortn_Type()
)
pmc1008mpCfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgCAisModePortn.setStatus("current")


class _Pmc1008mpCfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgUpAccessioAlmPortn_Object = MibTableColumn
pmc1008mpCfgUpAccessioAlmPortn = _Pmc1008mpCfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1, 1, 9),
    _Pmc1008mpCfgUpAccessioAlmPortn_Type()
)
pmc1008mpCfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgUpAccessioAlmPortn.setStatus("current")


class _Pmc1008mpCfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgUpMapperDeAlmPortn_Object = MibTableColumn
pmc1008mpCfgUpMapperDeAlmPortn = _Pmc1008mpCfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1, 1, 10),
    _Pmc1008mpCfgUpMapperDeAlmPortn_Type()
)
pmc1008mpCfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgUpMapperDeAlmPortn.setStatus("current")


class _Pmc1008mpCfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgDownAccessioAlmPortn_Object = MibTableColumn
pmc1008mpCfgDownAccessioAlmPortn = _Pmc1008mpCfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1, 1, 17),
    _Pmc1008mpCfgDownAccessioAlmPortn_Type()
)
pmc1008mpCfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgDownAccessioAlmPortn.setStatus("current")


class _Pmc1008mpCfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgDownMapperDeAlmPortn_Object = MibTableColumn
pmc1008mpCfgDownMapperDeAlmPortn = _Pmc1008mpCfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1, 1, 18),
    _Pmc1008mpCfgDownMapperDeAlmPortn_Type()
)
pmc1008mpCfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgDownMapperDeAlmPortn.setStatus("current")


class _Pmc1008mpCfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgDownDfrmAlmPortn_Object = MibTableColumn
pmc1008mpCfgDownDfrmAlmPortn = _Pmc1008mpCfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1, 1, 19),
    _Pmc1008mpCfgDownDfrmAlmPortn_Type()
)
pmc1008mpCfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgDownDfrmAlmPortn.setStatus("current")


class _Pmc1008mpCfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pmc1008mpCfgDownLineSyncAlarmsPortn = _Pmc1008mpCfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 1, 1, 1, 20),
    _Pmc1008mpCfgDownLineSyncAlarmsPortn_Type()
)
pmc1008mpCfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgDownLineSyncAlarmsPortn.setStatus("deprecated")
_Pmc1008mpCfgStartup_ObjectIdentity = ObjectIdentity
pmc1008mpCfgStartup = _Pmc1008mpCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2)
)
_Pmc1008mpCfgClientStartupTable_Object = MibTable
pmc1008mpCfgClientStartupTable = _Pmc1008mpCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgClientStartupTable.setStatus("current")
_Pmc1008mpCfgClientStartupEntry_Object = MibTableRow
pmc1008mpCfgClientStartupEntry = _Pmc1008mpCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 1, 1)
)
pmc1008mpCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgClientStartupEntry.setStatus("current")


class _Pmc1008mpCfgClientStartupIndex_Type(Integer32):
    """Custom type pmc1008mpCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pmc1008mpCfgClientStartupIndex_Object = MibTableColumn
pmc1008mpCfgClientStartupIndex = _Pmc1008mpCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 1, 1, 1),
    _Pmc1008mpCfgClientStartupIndex_Type()
)
pmc1008mpCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgClientStartupIndex.setStatus("current")


class _Pmc1008mpCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgSystConfPortPortn_Object = MibTableColumn
pmc1008mpCfgSystConfPortPortn = _Pmc1008mpCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 1, 1, 3),
    _Pmc1008mpCfgSystConfPortPortn_Type()
)
pmc1008mpCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgSystConfPortPortn.setStatus("current")


class _Pmc1008mpCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgNetConfPortPortn_Object = MibTableColumn
pmc1008mpCfgNetConfPortPortn = _Pmc1008mpCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 1, 1, 4),
    _Pmc1008mpCfgNetConfPortPortn_Type()
)
pmc1008mpCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgNetConfPortPortn.setStatus("current")


class _Pmc1008mpCfgAdddropConfPortPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgAdddropConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgAdddropConfPortPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgAdddropConfPortPortn_Object = MibTableColumn
pmc1008mpCfgAdddropConfPortPortn = _Pmc1008mpCfgAdddropConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 1, 1, 5),
    _Pmc1008mpCfgAdddropConfPortPortn_Type()
)
pmc1008mpCfgAdddropConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgAdddropConfPortPortn.setStatus("deprecated")
_Pmc1008mptablelineStartup_ObjectIdentity = ObjectIdentity
pmc1008mptablelineStartup = _Pmc1008mptablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 2)
)


class _Pmc1008mpCfgsystConfLine1_Type(Unsigned32):
    """Custom type pmc1008mpCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgsystConfLine1_Object = MibScalar
pmc1008mpCfgsystConfLine1 = _Pmc1008mpCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 2, 2),
    _Pmc1008mpCfgsystConfLine1_Type()
)
pmc1008mpCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgsystConfLine1.setStatus("current")


class _Pmc1008mpCfglineOptions1_Type(Unsigned32):
    """Custom type pmc1008mpCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfglineOptions1_Type.__name__ = "Unsigned32"
_Pmc1008mpCfglineOptions1_Object = MibScalar
pmc1008mpCfglineOptions1 = _Pmc1008mpCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 2, 5),
    _Pmc1008mpCfglineOptions1_Type()
)
pmc1008mpCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfglineOptions1.setStatus("current")


class _Pmc1008mpCfgsystConfLine2_Type(Unsigned32):
    """Custom type pmc1008mpCfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgsystConfLine2_Object = MibScalar
pmc1008mpCfgsystConfLine2 = _Pmc1008mpCfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 2, 6),
    _Pmc1008mpCfgsystConfLine2_Type()
)
pmc1008mpCfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgsystConfLine2.setStatus("current")


class _Pmc1008mpCfglineSelection_Type(Unsigned32):
    """Custom type pmc1008mpCfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfglineSelection_Type.__name__ = "Unsigned32"
_Pmc1008mpCfglineSelection_Object = MibScalar
pmc1008mpCfglineSelection = _Pmc1008mpCfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 2, 7),
    _Pmc1008mpCfglineSelection_Type()
)
pmc1008mpCfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfglineSelection.setStatus("current")


class _Pmc1008mpCfglineOptions2_Type(Unsigned32):
    """Custom type pmc1008mpCfglineOptions2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfglineOptions2_Type.__name__ = "Unsigned32"
_Pmc1008mpCfglineOptions2_Object = MibScalar
pmc1008mpCfglineOptions2 = _Pmc1008mpCfglineOptions2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 2, 9),
    _Pmc1008mpCfglineOptions2_Type()
)
pmc1008mpCfglineOptions2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfglineOptions2.setStatus("deprecated")
_Pmc1008mpCfgXfpTable_Object = MibTable
pmc1008mpCfgXfpTable = _Pmc1008mpCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgXfpTable.setStatus("current")
_Pmc1008mpCfgXfpEntry_Object = MibTableRow
pmc1008mpCfgXfpEntry = _Pmc1008mpCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 3, 1)
)
pmc1008mpCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgXfpEntry.setStatus("current")


class _Pmc1008mpCfgXfpIndex_Type(Integer32):
    """Custom type pmc1008mpCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgXfpIndex_Type.__name__ = "Integer32"
_Pmc1008mpCfgXfpIndex_Object = MibTableColumn
pmc1008mpCfgXfpIndex = _Pmc1008mpCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 3, 1, 1),
    _Pmc1008mpCfgXfpIndex_Type()
)
pmc1008mpCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgXfpIndex.setStatus("current")


class _Pmc1008mpCfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgSystConfXfpPortn_Object = MibTableColumn
pmc1008mpCfgSystConfXfpPortn = _Pmc1008mpCfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 3, 1, 3),
    _Pmc1008mpCfgSystConfXfpPortn_Type()
)
pmc1008mpCfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgSystConfXfpPortn.setStatus("current")


class _Pmc1008mpCfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgDataRateConfXfpPortn_Object = MibTableColumn
pmc1008mpCfgDataRateConfXfpPortn = _Pmc1008mpCfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 3, 1, 4),
    _Pmc1008mpCfgDataRateConfXfpPortn_Type()
)
pmc1008mpCfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgDataRateConfXfpPortn.setStatus("deprecated")
_Pmc1008mpCfgOtxtlhTable_Object = MibTable
pmc1008mpCfgOtxtlhTable = _Pmc1008mpCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgOtxtlhTable.setStatus("current")
_Pmc1008mpCfgOtxtlhEntry_Object = MibTableRow
pmc1008mpCfgOtxtlhEntry = _Pmc1008mpCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1)
)
pmc1008mpCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgOtxtlhEntry.setStatus("current")


class _Pmc1008mpCfgOtxtlhIndex_Type(Integer32):
    """Custom type pmc1008mpCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pmc1008mpCfgOtxtlhIndex_Object = MibTableColumn
pmc1008mpCfgOtxtlhIndex = _Pmc1008mpCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 1),
    _Pmc1008mpCfgOtxtlhIndex_Type()
)
pmc1008mpCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgOtxtlhIndex.setStatus("current")


class _Pmc1008mpCfgLineOtxMiscPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLineOtxMiscPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLineOtxMiscPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLineOtxMiscPortn_Object = MibTableColumn
pmc1008mpCfgLineOtxMiscPortn = _Pmc1008mpCfgLineOtxMiscPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 3),
    _Pmc1008mpCfgLineOtxMiscPortn_Type()
)
pmc1008mpCfgLineOtxMiscPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLineOtxMiscPortn.setStatus("current")


class _Pmc1008mpCfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLineDitherRatePortn_Object = MibTableColumn
pmc1008mpCfgLineDitherRatePortn = _Pmc1008mpCfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 4),
    _Pmc1008mpCfgLineDitherRatePortn_Type()
)
pmc1008mpCfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLineDitherRatePortn.setStatus("current")


class _Pmc1008mpCfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLineDitherFhzPortn_Object = MibTableColumn
pmc1008mpCfgLineDitherFhzPortn = _Pmc1008mpCfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 5),
    _Pmc1008mpCfgLineDitherFhzPortn_Type()
)
pmc1008mpCfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLineDitherFhzPortn.setStatus("current")


class _Pmc1008mpCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLinePwrLaserPortn_Object = MibTableColumn
pmc1008mpCfgLinePwrLaserPortn = _Pmc1008mpCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 6),
    _Pmc1008mpCfgLinePwrLaserPortn_Type()
)
pmc1008mpCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLinePwrLaserPortn.setStatus("current")


class _Pmc1008mpCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLineFCurrentPortn_Object = MibTableColumn
pmc1008mpCfgLineFCurrentPortn = _Pmc1008mpCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 7),
    _Pmc1008mpCfgLineFCurrentPortn_Type()
)
pmc1008mpCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLineFCurrentPortn.setStatus("current")


class _Pmc1008mpCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLineGridCurrentPortn_Object = MibTableColumn
pmc1008mpCfgLineGridCurrentPortn = _Pmc1008mpCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 8),
    _Pmc1008mpCfgLineGridCurrentPortn_Type()
)
pmc1008mpCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLineGridCurrentPortn.setStatus("current")


class _Pmc1008mpCfgFPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgFPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgFPortn_Object = MibTableColumn
pmc1008mpCfgFPortn = _Pmc1008mpCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 9),
    _Pmc1008mpCfgFPortn_Type()
)
pmc1008mpCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgFPortn.setStatus("current")


class _Pmc1008mpCfgReservedPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgReservedPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgReservedPortn_Object = MibTableColumn
pmc1008mpCfgReservedPortn = _Pmc1008mpCfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 10),
    _Pmc1008mpCfgReservedPortn_Type()
)
pmc1008mpCfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgReservedPortn.setStatus("deprecated")


class _Pmc1008mpCfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLinePhotodiodeModePortn_Object = MibTableColumn
pmc1008mpCfgLinePhotodiodeModePortn = _Pmc1008mpCfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 11),
    _Pmc1008mpCfgLinePhotodiodeModePortn_Type()
)
pmc1008mpCfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLinePhotodiodeModePortn.setStatus("current")


class _Pmc1008mpCfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLinePhotodiodeValuePortn_Object = MibTableColumn
pmc1008mpCfgLinePhotodiodeValuePortn = _Pmc1008mpCfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 2, 4, 1, 12),
    _Pmc1008mpCfgLinePhotodiodeValuePortn_Type()
)
pmc1008mpCfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLinePhotodiodeValuePortn.setStatus("current")
_Pmc1008mpCfgOther_ObjectIdentity = ObjectIdentity
pmc1008mpCfgOther = _Pmc1008mpCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 3)
)
_Pmc1008mptablemoduleOther_ObjectIdentity = ObjectIdentity
pmc1008mptablemoduleOther = _Pmc1008mptablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 3, 1)
)


class _Pmc1008mpCfgmode_Type(Unsigned32):
    """Custom type pmc1008mpCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgmode_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgmode_Object = MibScalar
pmc1008mpCfgmode = _Pmc1008mpCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 3, 1, 2),
    _Pmc1008mpCfgmode_Type()
)
pmc1008mpCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgmode.setStatus("current")
_Pmc1008mpCfgLabels_ObjectIdentity = ObjectIdentity
pmc1008mpCfgLabels = _Pmc1008mpCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 4)
)
_Pmc1008mpCfgLabelclientTable_Object = MibTable
pmc1008mpCfgLabelclientTable = _Pmc1008mpCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgLabelclientTable.setStatus("current")
_Pmc1008mpCfgLabelclientEntry_Object = MibTableRow
pmc1008mpCfgLabelclientEntry = _Pmc1008mpCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 4, 1, 1)
)
pmc1008mpCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgLabelclientEntry.setStatus("current")


class _Pmc1008mpCfgLabelclientIndex_Type(Integer32):
    """Custom type pmc1008mpCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmc1008mpCfgLabelclientIndex_Object = MibTableColumn
pmc1008mpCfgLabelclientIndex = _Pmc1008mpCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 4, 1, 1, 1),
    _Pmc1008mpCfgLabelclientIndex_Type()
)
pmc1008mpCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgLabelclientIndex.setStatus("current")


class _Pmc1008mpCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmc1008mpCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmc1008mpCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmc1008mpCfgLabelclientPortn_Object = MibTableColumn
pmc1008mpCfgLabelclientPortn = _Pmc1008mpCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 4, 1, 1, 3),
    _Pmc1008mpCfgLabelclientPortn_Type()
)
pmc1008mpCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLabelclientPortn.setStatus("current")
_Pmc1008mpCfgLabellineTable_Object = MibTable
pmc1008mpCfgLabellineTable = _Pmc1008mpCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgLabellineTable.setStatus("current")
_Pmc1008mpCfgLabellineEntry_Object = MibTableRow
pmc1008mpCfgLabellineEntry = _Pmc1008mpCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 4, 2, 1)
)
pmc1008mpCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgLabellineEntry.setStatus("current")


class _Pmc1008mpCfgLabellineIndex_Type(Integer32):
    """Custom type pmc1008mpCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgLabellineIndex_Type.__name__ = "Integer32"
_Pmc1008mpCfgLabellineIndex_Object = MibTableColumn
pmc1008mpCfgLabellineIndex = _Pmc1008mpCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 4, 2, 1, 1),
    _Pmc1008mpCfgLabellineIndex_Type()
)
pmc1008mpCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgLabellineIndex.setStatus("current")


class _Pmc1008mpCfgLabellinePortn_Type(DisplayString):
    """Custom type pmc1008mpCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmc1008mpCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmc1008mpCfgLabellinePortn_Object = MibTableColumn
pmc1008mpCfgLabellinePortn = _Pmc1008mpCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 4, 2, 1, 3),
    _Pmc1008mpCfgLabellinePortn_Type()
)
pmc1008mpCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLabellinePortn.setStatus("current")
_Pmc1008mpCfgStartuptimeslotsline1_ObjectIdentity = ObjectIdentity
pmc1008mpCfgStartuptimeslotsline1 = _Pmc1008mpCfgStartuptimeslotsline1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 5)
)
_Pmc1008mpCfgTimeslotsportsline1Table_Object = MibTable
pmc1008mpCfgTimeslotsportsline1Table = _Pmc1008mpCfgTimeslotsportsline1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotsportsline1Table.setStatus("current")
_Pmc1008mpCfgTimeslotsportsline1Entry_Object = MibTableRow
pmc1008mpCfgTimeslotsportsline1Entry = _Pmc1008mpCfgTimeslotsportsline1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 5, 1, 1)
)
pmc1008mpCfgTimeslotsportsline1Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgTimeslotsportsline1Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotsportsline1Entry.setStatus("current")


class _Pmc1008mpCfgTimeslotsportsline1Index_Type(Integer32):
    """Custom type pmc1008mpCfgTimeslotsportsline1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgTimeslotsportsline1Index_Type.__name__ = "Integer32"
_Pmc1008mpCfgTimeslotsportsline1Index_Object = MibTableColumn
pmc1008mpCfgTimeslotsportsline1Index = _Pmc1008mpCfgTimeslotsportsline1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 5, 1, 1, 1),
    _Pmc1008mpCfgTimeslotsportsline1Index_Type()
)
pmc1008mpCfgTimeslotsportsline1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotsportsline1Index.setStatus("current")


class _Pmc1008mpCfgLine1Timeslotb2PortPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine1Timeslotb2PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine1Timeslotb2PortPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine1Timeslotb2PortPortn_Object = MibTableColumn
pmc1008mpCfgLine1Timeslotb2PortPortn = _Pmc1008mpCfgLine1Timeslotb2PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 5, 1, 1, 3),
    _Pmc1008mpCfgLine1Timeslotb2PortPortn_Type()
)
pmc1008mpCfgLine1Timeslotb2PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine1Timeslotb2PortPortn.setStatus("current")


class _Pmc1008mpCfgLine1Timeslotb1PortPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine1Timeslotb1PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine1Timeslotb1PortPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine1Timeslotb1PortPortn_Object = MibTableColumn
pmc1008mpCfgLine1Timeslotb1PortPortn = _Pmc1008mpCfgLine1Timeslotb1PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 5, 1, 1, 4),
    _Pmc1008mpCfgLine1Timeslotb1PortPortn_Type()
)
pmc1008mpCfgLine1Timeslotb1PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine1Timeslotb1PortPortn.setStatus("current")


class _Pmc1008mpCfgLine1ProtocolPortPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine1ProtocolPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine1ProtocolPortPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine1ProtocolPortPortn_Object = MibTableColumn
pmc1008mpCfgLine1ProtocolPortPortn = _Pmc1008mpCfgLine1ProtocolPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 5, 1, 1, 5),
    _Pmc1008mpCfgLine1ProtocolPortPortn_Type()
)
pmc1008mpCfgLine1ProtocolPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine1ProtocolPortPortn.setStatus("current")
_Pmc1008mpCfgStartuptimeslotsline2_ObjectIdentity = ObjectIdentity
pmc1008mpCfgStartuptimeslotsline2 = _Pmc1008mpCfgStartuptimeslotsline2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 6)
)
_Pmc1008mpCfgTimeslotsportsline2Table_Object = MibTable
pmc1008mpCfgTimeslotsportsline2Table = _Pmc1008mpCfgTimeslotsportsline2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotsportsline2Table.setStatus("current")
_Pmc1008mpCfgTimeslotsportsline2Entry_Object = MibTableRow
pmc1008mpCfgTimeslotsportsline2Entry = _Pmc1008mpCfgTimeslotsportsline2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 6, 1, 1)
)
pmc1008mpCfgTimeslotsportsline2Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgTimeslotsportsline2Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotsportsline2Entry.setStatus("current")


class _Pmc1008mpCfgTimeslotsportsline2Index_Type(Integer32):
    """Custom type pmc1008mpCfgTimeslotsportsline2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgTimeslotsportsline2Index_Type.__name__ = "Integer32"
_Pmc1008mpCfgTimeslotsportsline2Index_Object = MibTableColumn
pmc1008mpCfgTimeslotsportsline2Index = _Pmc1008mpCfgTimeslotsportsline2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 6, 1, 1, 1),
    _Pmc1008mpCfgTimeslotsportsline2Index_Type()
)
pmc1008mpCfgTimeslotsportsline2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotsportsline2Index.setStatus("current")


class _Pmc1008mpCfgLine2Timeslotb2PortPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine2Timeslotb2PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine2Timeslotb2PortPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine2Timeslotb2PortPortn_Object = MibTableColumn
pmc1008mpCfgLine2Timeslotb2PortPortn = _Pmc1008mpCfgLine2Timeslotb2PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 6, 1, 1, 3),
    _Pmc1008mpCfgLine2Timeslotb2PortPortn_Type()
)
pmc1008mpCfgLine2Timeslotb2PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine2Timeslotb2PortPortn.setStatus("current")


class _Pmc1008mpCfgLine2Timeslotb1PortPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine2Timeslotb1PortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine2Timeslotb1PortPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine2Timeslotb1PortPortn_Object = MibTableColumn
pmc1008mpCfgLine2Timeslotb1PortPortn = _Pmc1008mpCfgLine2Timeslotb1PortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 6, 1, 1, 4),
    _Pmc1008mpCfgLine2Timeslotb1PortPortn_Type()
)
pmc1008mpCfgLine2Timeslotb1PortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine2Timeslotb1PortPortn.setStatus("current")


class _Pmc1008mpCfgLine2ProtocolPortPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine2ProtocolPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine2ProtocolPortPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine2ProtocolPortPortn_Object = MibTableColumn
pmc1008mpCfgLine2ProtocolPortPortn = _Pmc1008mpCfgLine2ProtocolPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 6, 1, 1, 5),
    _Pmc1008mpCfgLine2ProtocolPortPortn_Type()
)
pmc1008mpCfgLine2ProtocolPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine2ProtocolPortPortn.setStatus("current")
_Pmc1008mpCfgStartuptimeslotspassthroughline1_ObjectIdentity = ObjectIdentity
pmc1008mpCfgStartuptimeslotspassthroughline1 = _Pmc1008mpCfgStartuptimeslotspassthroughline1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 7)
)
_Pmc1008mpCfgTimeslotspassthroughline1Table_Object = MibTable
pmc1008mpCfgTimeslotspassthroughline1Table = _Pmc1008mpCfgTimeslotspassthroughline1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 7, 1)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotspassthroughline1Table.setStatus("current")
_Pmc1008mpCfgTimeslotspassthroughline1Entry_Object = MibTableRow
pmc1008mpCfgTimeslotspassthroughline1Entry = _Pmc1008mpCfgTimeslotspassthroughline1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 7, 1, 1)
)
pmc1008mpCfgTimeslotspassthroughline1Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgTimeslotspassthroughline1Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotspassthroughline1Entry.setStatus("current")


class _Pmc1008mpCfgTimeslotspassthroughline1Index_Type(Integer32):
    """Custom type pmc1008mpCfgTimeslotspassthroughline1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgTimeslotspassthroughline1Index_Type.__name__ = "Integer32"
_Pmc1008mpCfgTimeslotspassthroughline1Index_Object = MibTableColumn
pmc1008mpCfgTimeslotspassthroughline1Index = _Pmc1008mpCfgTimeslotspassthroughline1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 7, 1, 1, 1),
    _Pmc1008mpCfgTimeslotspassthroughline1Index_Type()
)
pmc1008mpCfgTimeslotspassthroughline1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotspassthroughline1Index.setStatus("current")


class _Pmc1008mpCfgLine1Timeslotb2PassthroughPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine1Timeslotb2PassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine1Timeslotb2PassthroughPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine1Timeslotb2PassthroughPortn_Object = MibTableColumn
pmc1008mpCfgLine1Timeslotb2PassthroughPortn = _Pmc1008mpCfgLine1Timeslotb2PassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 7, 1, 1, 3),
    _Pmc1008mpCfgLine1Timeslotb2PassthroughPortn_Type()
)
pmc1008mpCfgLine1Timeslotb2PassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine1Timeslotb2PassthroughPortn.setStatus("current")


class _Pmc1008mpCfgLine1Timeslotb1PassthroughPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine1Timeslotb1PassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine1Timeslotb1PassthroughPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine1Timeslotb1PassthroughPortn_Object = MibTableColumn
pmc1008mpCfgLine1Timeslotb1PassthroughPortn = _Pmc1008mpCfgLine1Timeslotb1PassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 7, 1, 1, 4),
    _Pmc1008mpCfgLine1Timeslotb1PassthroughPortn_Type()
)
pmc1008mpCfgLine1Timeslotb1PassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine1Timeslotb1PassthroughPortn.setStatus("current")


class _Pmc1008mpCfgLine1ProtocolPassthroughPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine1ProtocolPassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine1ProtocolPassthroughPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine1ProtocolPassthroughPortn_Object = MibTableColumn
pmc1008mpCfgLine1ProtocolPassthroughPortn = _Pmc1008mpCfgLine1ProtocolPassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 7, 1, 1, 5),
    _Pmc1008mpCfgLine1ProtocolPassthroughPortn_Type()
)
pmc1008mpCfgLine1ProtocolPassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine1ProtocolPassthroughPortn.setStatus("current")
_Pmc1008mpCfgStartuptimeslotspassthroughline2_ObjectIdentity = ObjectIdentity
pmc1008mpCfgStartuptimeslotspassthroughline2 = _Pmc1008mpCfgStartuptimeslotspassthroughline2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 8)
)
_Pmc1008mpCfgTimeslotspassthroughline2Table_Object = MibTable
pmc1008mpCfgTimeslotspassthroughline2Table = _Pmc1008mpCfgTimeslotspassthroughline2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 8, 1)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotspassthroughline2Table.setStatus("current")
_Pmc1008mpCfgTimeslotspassthroughline2Entry_Object = MibTableRow
pmc1008mpCfgTimeslotspassthroughline2Entry = _Pmc1008mpCfgTimeslotspassthroughline2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 8, 1, 1)
)
pmc1008mpCfgTimeslotspassthroughline2Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgTimeslotspassthroughline2Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotspassthroughline2Entry.setStatus("current")


class _Pmc1008mpCfgTimeslotspassthroughline2Index_Type(Integer32):
    """Custom type pmc1008mpCfgTimeslotspassthroughline2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgTimeslotspassthroughline2Index_Type.__name__ = "Integer32"
_Pmc1008mpCfgTimeslotspassthroughline2Index_Object = MibTableColumn
pmc1008mpCfgTimeslotspassthroughline2Index = _Pmc1008mpCfgTimeslotspassthroughline2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 8, 1, 1, 1),
    _Pmc1008mpCfgTimeslotspassthroughline2Index_Type()
)
pmc1008mpCfgTimeslotspassthroughline2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgTimeslotspassthroughline2Index.setStatus("current")


class _Pmc1008mpCfgLine2Timeslotb2PassthroughPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine2Timeslotb2PassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine2Timeslotb2PassthroughPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine2Timeslotb2PassthroughPortn_Object = MibTableColumn
pmc1008mpCfgLine2Timeslotb2PassthroughPortn = _Pmc1008mpCfgLine2Timeslotb2PassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 8, 1, 1, 3),
    _Pmc1008mpCfgLine2Timeslotb2PassthroughPortn_Type()
)
pmc1008mpCfgLine2Timeslotb2PassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine2Timeslotb2PassthroughPortn.setStatus("current")


class _Pmc1008mpCfgLine2Timeslotb1PassthroughPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine2Timeslotb1PassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine2Timeslotb1PassthroughPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine2Timeslotb1PassthroughPortn_Object = MibTableColumn
pmc1008mpCfgLine2Timeslotb1PassthroughPortn = _Pmc1008mpCfgLine2Timeslotb1PassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 8, 1, 1, 4),
    _Pmc1008mpCfgLine2Timeslotb1PassthroughPortn_Type()
)
pmc1008mpCfgLine2Timeslotb1PassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine2Timeslotb1PassthroughPortn.setStatus("current")


class _Pmc1008mpCfgLine2ProtocolPassthroughPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLine2ProtocolPassthroughPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLine2ProtocolPassthroughPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLine2ProtocolPassthroughPortn_Object = MibTableColumn
pmc1008mpCfgLine2ProtocolPassthroughPortn = _Pmc1008mpCfgLine2ProtocolPassthroughPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 8, 1, 1, 5),
    _Pmc1008mpCfgLine2ProtocolPassthroughPortn_Type()
)
pmc1008mpCfgLine2ProtocolPassthroughPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgLine2ProtocolPassthroughPortn.setStatus("current")
_Pmc1008mpCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pmc1008mpCfgStartuptablefive = _Pmc1008mpCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 9)
)
_Pmc1008mpCfgOtxtlhcapabilitiesTable_Object = MibTable
pmc1008mpCfgOtxtlhcapabilitiesTable = _Pmc1008mpCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 9, 1)
)
if mibBuilder.loadTexts:
    pmc1008mpCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pmc1008mpCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pmc1008mpCfgOtxtlhcapabilitiesEntry = _Pmc1008mpCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 9, 1, 1)
)
pmc1008mpCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pmc1008mpCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pmc1008mpCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pmc1008mpCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pmc1008mpCfgOtxtlhcapabilitiesIndex = _Pmc1008mpCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 9, 1, 1, 1),
    _Pmc1008mpCfgOtxtlhcapabilitiesIndex_Type()
)
pmc1008mpCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pmc1008mpCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgComponentTypePortn_Object = MibTableColumn
pmc1008mpCfgComponentTypePortn = _Pmc1008mpCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 9, 1, 1, 3),
    _Pmc1008mpCfgComponentTypePortn_Type()
)
pmc1008mpCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgComponentTypePortn.setStatus("current")


class _Pmc1008mpCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgMiscellaneousPortn_Object = MibTableColumn
pmc1008mpCfgMiscellaneousPortn = _Pmc1008mpCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 9, 1, 1, 4),
    _Pmc1008mpCfgMiscellaneousPortn_Type()
)
pmc1008mpCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgMiscellaneousPortn.setStatus("current")


class _Pmc1008mpCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgFirstChannelPortn_Object = MibTableColumn
pmc1008mpCfgFirstChannelPortn = _Pmc1008mpCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 9, 1, 1, 5),
    _Pmc1008mpCfgFirstChannelPortn_Type()
)
pmc1008mpCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgFirstChannelPortn.setStatus("current")


class _Pmc1008mpCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgLastChannelPortn_Object = MibTableColumn
pmc1008mpCfgLastChannelPortn = _Pmc1008mpCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 9, 1, 1, 6),
    _Pmc1008mpCfgLastChannelPortn_Type()
)
pmc1008mpCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgLastChannelPortn.setStatus("current")


class _Pmc1008mpCfgGridPortn_Type(Unsigned32):
    """Custom type pmc1008mpCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1008mpCfgGridPortn_Type.__name__ = "Unsigned32"
_Pmc1008mpCfgGridPortn_Object = MibTableColumn
pmc1008mpCfgGridPortn = _Pmc1008mpCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 9, 1, 1, 7),
    _Pmc1008mpCfgGridPortn_Type()
)
pmc1008mpCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpCfgGridPortn.setStatus("current")
_Pmc1008mpCfgWriteConfiguration_Type = EkiOnOff
_Pmc1008mpCfgWriteConfiguration_Object = MibScalar
pmc1008mpCfgWriteConfiguration = _Pmc1008mpCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 9, 257),
    _Pmc1008mpCfgWriteConfiguration_Type()
)
pmc1008mpCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpCfgWriteConfiguration.setStatus("current")
_Pmc1008mptraps_ObjectIdentity = ObjectIdentity
pmc1008mptraps = _Pmc1008mptraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10)
)


class _Pmc1008mptrapPortNumber_Type(Integer32):
    """Custom type pmc1008mptrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmc1008mptrapPortNumber_Type.__name__ = "Integer32"
_Pmc1008mptrapPortNumber_Object = MibScalar
pmc1008mptrapPortNumber = _Pmc1008mptrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 2),
    _Pmc1008mptrapPortNumber_Type()
)
pmc1008mptrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mptrapPortNumber.setStatus("current")


class _Pmc1008mptrapLineNumber_Type(Integer32):
    """Custom type pmc1008mptrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmc1008mptrapLineNumber_Type.__name__ = "Integer32"
_Pmc1008mptrapLineNumber_Object = MibScalar
pmc1008mptrapLineNumber = _Pmc1008mptrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 3),
    _Pmc1008mptrapLineNumber_Type()
)
pmc1008mptrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mptrapLineNumber.setStatus("current")


class _Pmc1008mptrapBoardNumber_Type(Integer32):
    """Custom type pmc1008mptrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmc1008mptrapBoardNumber_Type.__name__ = "Integer32"
_Pmc1008mptrapBoardNumber_Object = MibScalar
pmc1008mptrapBoardNumber = _Pmc1008mptrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 4),
    _Pmc1008mptrapBoardNumber_Type()
)
pmc1008mptrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mptrapBoardNumber.setStatus("current")
_Pmc1008mpMonitoring_ObjectIdentity = ObjectIdentity
pmc1008mpMonitoring = _Pmc1008mpMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11)
)
_Pmc1008mpMonOther_ObjectIdentity = ObjectIdentity
pmc1008mpMonOther = _Pmc1008mpMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1)
)
_Pmc1008mpMonSync_ObjectIdentity = ObjectIdentity
pmc1008mpMonSync = _Pmc1008mpMonSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 1)
)
_Pmc1008mpPerfEnable_Type = EkiOnOff
_Pmc1008mpPerfEnable_Object = MibScalar
pmc1008mpPerfEnable = _Pmc1008mpPerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 1, 257),
    _Pmc1008mpPerfEnable_Type()
)
pmc1008mpPerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpPerfEnable.setStatus("current")
_Pmc1008mpPerf15minSync_Type = EkiOnOff
_Pmc1008mpPerf15minSync_Object = MibScalar
pmc1008mpPerf15minSync = _Pmc1008mpPerf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 1, 259),
    _Pmc1008mpPerf15minSync_Type()
)
pmc1008mpPerf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpPerf15minSync.setStatus("current")
_Pmc1008mpPerf24hSync_Type = EkiOnOff
_Pmc1008mpPerf24hSync_Object = MibScalar
pmc1008mpPerf24hSync = _Pmc1008mpPerf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 1, 260),
    _Pmc1008mpPerf24hSync_Type()
)
pmc1008mpPerf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpPerf24hSync.setStatus("current")
_Pmc1008mpMonTimeStamp_ObjectIdentity = ObjectIdentity
pmc1008mpMonTimeStamp = _Pmc1008mpMonTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 2)
)
_Pmc1008mpPerf15MinShort_Type = EkiOnOff
_Pmc1008mpPerf15MinShort_Object = MibScalar
pmc1008mpPerf15MinShort = _Pmc1008mpPerf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 2, 1),
    _Pmc1008mpPerf15MinShort_Type()
)
pmc1008mpPerf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpPerf15MinShort.setStatus("current")
_Pmc1008mpPerf15MinLong_Type = EkiOnOff
_Pmc1008mpPerf15MinLong_Object = MibScalar
pmc1008mpPerf15MinLong = _Pmc1008mpPerf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 2, 2),
    _Pmc1008mpPerf15MinLong_Type()
)
pmc1008mpPerf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpPerf15MinLong.setStatus("current")
_Pmc1008mpPerf24HoursShort_Type = Counter32
_Pmc1008mpPerf24HoursShort_Object = MibScalar
pmc1008mpPerf24HoursShort = _Pmc1008mpPerf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 2, 5),
    _Pmc1008mpPerf24HoursShort_Type()
)
pmc1008mpPerf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpPerf24HoursShort.setStatus("current")
_Pmc1008mpPerf24HoursLong_Type = Counter32
_Pmc1008mpPerf24HoursLong_Object = MibScalar
pmc1008mpPerf24HoursLong = _Pmc1008mpPerf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 2, 6),
    _Pmc1008mpPerf24HoursLong_Type()
)
pmc1008mpPerf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpPerf24HoursLong.setStatus("current")
_Pmc1008mpPerfCurrent15MinElapsedTime_Type = Counter32
_Pmc1008mpPerfCurrent15MinElapsedTime_Object = MibScalar
pmc1008mpPerfCurrent15MinElapsedTime = _Pmc1008mpPerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 2, 7),
    _Pmc1008mpPerfCurrent15MinElapsedTime_Type()
)
pmc1008mpPerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpPerfCurrent15MinElapsedTime.setStatus("current")
_Pmc1008mpPerfCurrent24HoursElapsedTime_Type = Counter32
_Pmc1008mpPerfCurrent24HoursElapsedTime_Object = MibScalar
pmc1008mpPerfCurrent24HoursElapsedTime = _Pmc1008mpPerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 2, 8),
    _Pmc1008mpPerfCurrent24HoursElapsedTime_Type()
)
pmc1008mpPerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpPerfCurrent24HoursElapsedTime.setStatus("current")
_Pmc1008mpMonRmon_ObjectIdentity = ObjectIdentity
pmc1008mpMonRmon = _Pmc1008mpMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 3)
)
_Pmc1008mpMonCountersReset_Type = EkiOnOff
_Pmc1008mpMonCountersReset_Object = MibScalar
pmc1008mpMonCountersReset = _Pmc1008mpMonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 3, 359),
    _Pmc1008mpMonCountersReset_Type()
)
pmc1008mpMonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpMonCountersReset.setStatus("current")
_Pmc1008mpMonCountersStop_Type = EkiOnOff
_Pmc1008mpMonCountersStop_Object = MibScalar
pmc1008mpMonCountersStop = _Pmc1008mpMonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 1, 3, 360),
    _Pmc1008mpMonCountersStop_Type()
)
pmc1008mpMonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1008mpMonCountersStop.setStatus("current")
_Pmc1008mpMonClient_ObjectIdentity = ObjectIdentity
pmc1008mpMonClient = _Pmc1008mpMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2)
)
_Pmc1008mpMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pmc1008mpMonClientRmonCounter = _Pmc1008mpMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4)
)
_Pmc1008mpMonupRmonByteCntTable_Object = MibTable
pmc1008mpMonupRmonByteCntTable = _Pmc1008mpMonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonByteCntTable.setStatus("current")
_Pmc1008mpMonupRmonByteCntEntry_Object = MibTableRow
pmc1008mpMonupRmonByteCntEntry = _Pmc1008mpMonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 16, 1)
)
pmc1008mpMonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonByteCntEntry.setStatus("current")


class _Pmc1008mpMonupRmonByteCntIndex_Type(Integer32):
    """Custom type pmc1008mpMonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpMonupRmonByteCntIndex_Object = MibTableColumn
pmc1008mpMonupRmonByteCntIndex = _Pmc1008mpMonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 16, 1, 1),
    _Pmc1008mpMonupRmonByteCntIndex_Type()
)
pmc1008mpMonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonByteCntIndex.setStatus("current")
_Pmc1008mpMonupRmonByteCntValuePortn_Type = Counter64
_Pmc1008mpMonupRmonByteCntValuePortn_Object = MibTableColumn
pmc1008mpMonupRmonByteCntValuePortn = _Pmc1008mpMonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 16, 1, 2),
    _Pmc1008mpMonupRmonByteCntValuePortn_Type()
)
pmc1008mpMonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonByteCntValuePortn.setStatus("current")
_Pmc1008mpMonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonByteCntErrorPortn_Object = MibTableColumn
pmc1008mpMonupRmonByteCntErrorPortn = _Pmc1008mpMonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 16, 1, 3),
    _Pmc1008mpMonupRmonByteCntErrorPortn_Type()
)
pmc1008mpMonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonByteCntErrorPortn.setStatus("current")
_Pmc1008mpMonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonByteCntOverloadPortn_Object = MibTableColumn
pmc1008mpMonupRmonByteCntOverloadPortn = _Pmc1008mpMonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 16, 1, 4),
    _Pmc1008mpMonupRmonByteCntOverloadPortn_Type()
)
pmc1008mpMonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonByteCntOverloadPortn.setStatus("current")
_Pmc1008mpMonupRmonCrcErrorCntTable_Object = MibTable
pmc1008mpMonupRmonCrcErrorCntTable = _Pmc1008mpMonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 24)
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonCrcErrorCntTable.setStatus("current")
_Pmc1008mpMonupRmonCrcErrorCntEntry_Object = MibTableRow
pmc1008mpMonupRmonCrcErrorCntEntry = _Pmc1008mpMonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 24, 1)
)
pmc1008mpMonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonCrcErrorCntEntry.setStatus("current")


class _Pmc1008mpMonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pmc1008mpMonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpMonupRmonCrcErrorCntIndex_Object = MibTableColumn
pmc1008mpMonupRmonCrcErrorCntIndex = _Pmc1008mpMonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 24, 1, 1),
    _Pmc1008mpMonupRmonCrcErrorCntIndex_Type()
)
pmc1008mpMonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonCrcErrorCntIndex.setStatus("current")
_Pmc1008mpMonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pmc1008mpMonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pmc1008mpMonupRmonCrcErrorCntValuePortn = _Pmc1008mpMonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 24, 1, 2),
    _Pmc1008mpMonupRmonCrcErrorCntValuePortn_Type()
)
pmc1008mpMonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pmc1008mpMonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pmc1008mpMonupRmonCrcErrorCntErrorPortn = _Pmc1008mpMonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 24, 1, 3),
    _Pmc1008mpMonupRmonCrcErrorCntErrorPortn_Type()
)
pmc1008mpMonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pmc1008mpMonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pmc1008mpMonupRmonCrcErrorCntOverloadPortn = _Pmc1008mpMonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 24, 1, 4),
    _Pmc1008mpMonupRmonCrcErrorCntOverloadPortn_Type()
)
pmc1008mpMonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pmc1008mpMonupRmonPacketsCntTable_Object = MibTable
pmc1008mpMonupRmonPacketsCntTable = _Pmc1008mpMonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonPacketsCntTable.setStatus("current")
_Pmc1008mpMonupRmonPacketsCntEntry_Object = MibTableRow
pmc1008mpMonupRmonPacketsCntEntry = _Pmc1008mpMonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 32, 1)
)
pmc1008mpMonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonPacketsCntEntry.setStatus("current")


class _Pmc1008mpMonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pmc1008mpMonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpMonupRmonPacketsCntIndex_Object = MibTableColumn
pmc1008mpMonupRmonPacketsCntIndex = _Pmc1008mpMonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 32, 1, 1),
    _Pmc1008mpMonupRmonPacketsCntIndex_Type()
)
pmc1008mpMonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonPacketsCntIndex.setStatus("current")
_Pmc1008mpMonupRmonPacketsCntValuePortn_Type = Counter64
_Pmc1008mpMonupRmonPacketsCntValuePortn_Object = MibTableColumn
pmc1008mpMonupRmonPacketsCntValuePortn = _Pmc1008mpMonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 32, 1, 2),
    _Pmc1008mpMonupRmonPacketsCntValuePortn_Type()
)
pmc1008mpMonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonPacketsCntValuePortn.setStatus("current")
_Pmc1008mpMonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pmc1008mpMonupRmonPacketsCntErrorPortn = _Pmc1008mpMonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 32, 1, 3),
    _Pmc1008mpMonupRmonPacketsCntErrorPortn_Type()
)
pmc1008mpMonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonPacketsCntErrorPortn.setStatus("current")
_Pmc1008mpMonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pmc1008mpMonupRmonPacketsCntOverloadPortn = _Pmc1008mpMonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 32, 1, 4),
    _Pmc1008mpMonupRmonPacketsCntOverloadPortn_Type()
)
pmc1008mpMonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pmc1008mpMonupRmonBroadcastCntTable_Object = MibTable
pmc1008mpMonupRmonBroadcastCntTable = _Pmc1008mpMonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 40)
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonBroadcastCntTable.setStatus("current")
_Pmc1008mpMonupRmonBroadcastCntEntry_Object = MibTableRow
pmc1008mpMonupRmonBroadcastCntEntry = _Pmc1008mpMonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 40, 1)
)
pmc1008mpMonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonBroadcastCntEntry.setStatus("current")


class _Pmc1008mpMonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pmc1008mpMonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpMonupRmonBroadcastCntIndex_Object = MibTableColumn
pmc1008mpMonupRmonBroadcastCntIndex = _Pmc1008mpMonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 40, 1, 1),
    _Pmc1008mpMonupRmonBroadcastCntIndex_Type()
)
pmc1008mpMonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonBroadcastCntIndex.setStatus("current")
_Pmc1008mpMonupRmonBroadcastCntValuePortn_Type = Counter64
_Pmc1008mpMonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pmc1008mpMonupRmonBroadcastCntValuePortn = _Pmc1008mpMonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 40, 1, 2),
    _Pmc1008mpMonupRmonBroadcastCntValuePortn_Type()
)
pmc1008mpMonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonBroadcastCntValuePortn.setStatus("current")
_Pmc1008mpMonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pmc1008mpMonupRmonBroadcastCntErrorPortn = _Pmc1008mpMonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 40, 1, 3),
    _Pmc1008mpMonupRmonBroadcastCntErrorPortn_Type()
)
pmc1008mpMonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pmc1008mpMonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pmc1008mpMonupRmonBroadcastCntOverloadPortn = _Pmc1008mpMonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 40, 1, 4),
    _Pmc1008mpMonupRmonBroadcastCntOverloadPortn_Type()
)
pmc1008mpMonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pmc1008mpMonupRmonMulticastCntTable_Object = MibTable
pmc1008mpMonupRmonMulticastCntTable = _Pmc1008mpMonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonMulticastCntTable.setStatus("current")
_Pmc1008mpMonupRmonMulticastCntEntry_Object = MibTableRow
pmc1008mpMonupRmonMulticastCntEntry = _Pmc1008mpMonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 48, 1)
)
pmc1008mpMonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpMonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonMulticastCntEntry.setStatus("current")


class _Pmc1008mpMonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pmc1008mpMonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpMonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pmc1008mpMonupRmonMulticastCntIndex_Object = MibTableColumn
pmc1008mpMonupRmonMulticastCntIndex = _Pmc1008mpMonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 48, 1, 1),
    _Pmc1008mpMonupRmonMulticastCntIndex_Type()
)
pmc1008mpMonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonMulticastCntIndex.setStatus("current")
_Pmc1008mpMonupRmonMulticastCntValuePortn_Type = Counter64
_Pmc1008mpMonupRmonMulticastCntValuePortn_Object = MibTableColumn
pmc1008mpMonupRmonMulticastCntValuePortn = _Pmc1008mpMonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 48, 1, 2),
    _Pmc1008mpMonupRmonMulticastCntValuePortn_Type()
)
pmc1008mpMonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonMulticastCntValuePortn.setStatus("current")
_Pmc1008mpMonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pmc1008mpMonupRmonMulticastCntErrorPortn = _Pmc1008mpMonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 48, 1, 3),
    _Pmc1008mpMonupRmonMulticastCntErrorPortn_Type()
)
pmc1008mpMonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonMulticastCntErrorPortn.setStatus("current")
_Pmc1008mpMonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pmc1008mpMonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pmc1008mpMonupRmonMulticastCntOverloadPortn = _Pmc1008mpMonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 4, 48, 1, 4),
    _Pmc1008mpMonupRmonMulticastCntOverloadPortn_Type()
)
pmc1008mpMonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpMonupRmonMulticastCntOverloadPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatTable_Object = MibTable
pmc1008mpPerfTelecomClientCurrent15StatTable = _Pmc1008mpPerfTelecomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatTable.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatEntry_Object = MibTableRow
pmc1008mpPerfTelecomClientCurrent15StatEntry = _Pmc1008mpPerfTelecomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1)
)
pmc1008mpPerfTelecomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfTelecomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatEntry.setStatus("current")


class _Pmc1008mpPerfTelecomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pmc1008mpPerfTelecomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfTelecomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pmc1008mpPerfTelecomClientCurrent15StatIndex_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatIndex = _Pmc1008mpPerfTelecomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 1),
    _Pmc1008mpPerfTelecomClientCurrent15StatIndex_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatIndex.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent15StatInvCvPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatInvCvPortn = _Pmc1008mpPerfTelecomClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 2),
    _Pmc1008mpPerfTelecomClientCurrent15StatInvCvPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatInvCvPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent15StatCvValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatCvValuePortn = _Pmc1008mpPerfTelecomClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 3),
    _Pmc1008mpPerfTelecomClientCurrent15StatCvValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatCvValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent15StatInvEsPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatInvEsPortn = _Pmc1008mpPerfTelecomClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 4),
    _Pmc1008mpPerfTelecomClientCurrent15StatInvEsPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatInvEsPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent15StatEsValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatEsValuePortn = _Pmc1008mpPerfTelecomClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 5),
    _Pmc1008mpPerfTelecomClientCurrent15StatEsValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatEsValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent15StatInvSesPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatInvSesPortn = _Pmc1008mpPerfTelecomClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 6),
    _Pmc1008mpPerfTelecomClientCurrent15StatInvSesPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatInvSesPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent15StatSesValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatSesValuePortn = _Pmc1008mpPerfTelecomClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 7),
    _Pmc1008mpPerfTelecomClientCurrent15StatSesValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatSesValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatInvSefsPortn = _Pmc1008mpPerfTelecomClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 8),
    _Pmc1008mpPerfTelecomClientCurrent15StatInvSefsPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatInvSefsPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatSefsValuePortn = _Pmc1008mpPerfTelecomClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 9),
    _Pmc1008mpPerfTelecomClientCurrent15StatSefsValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatSefsValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent15StatInvUasPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatInvUasPortn = _Pmc1008mpPerfTelecomClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 10),
    _Pmc1008mpPerfTelecomClientCurrent15StatInvUasPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatInvUasPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent15StatUasValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent15StatUasValuePortn = _Pmc1008mpPerfTelecomClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 16, 1, 11),
    _Pmc1008mpPerfTelecomClientCurrent15StatUasValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent15StatUasValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryPort1Table_Object = MibTable
pmc1008mpPerfTelecomClientPast15StatHistoryPort1Table = _Pmc1008mpPerfTelecomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryPort1Table.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pmc1008mpPerfTelecomClientPast15StatHistoryPort1Entry = _Pmc1008mpPerfTelecomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1)
)
pmc1008mpPerfTelecomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index = _Pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 1),
    _Pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistoryInvCvPort1 = _Pmc1008mpPerfTelecomClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 2),
    _Pmc1008mpPerfTelecomClientPast15StatHistoryInvCvPort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistoryCvValuePort1 = _Pmc1008mpPerfTelecomClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 3),
    _Pmc1008mpPerfTelecomClientPast15StatHistoryCvValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistoryInvEsPort1 = _Pmc1008mpPerfTelecomClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 4),
    _Pmc1008mpPerfTelecomClientPast15StatHistoryInvEsPort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistoryEsValuePort1 = _Pmc1008mpPerfTelecomClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 5),
    _Pmc1008mpPerfTelecomClientPast15StatHistoryEsValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistoryInvSesPort1 = _Pmc1008mpPerfTelecomClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 6),
    _Pmc1008mpPerfTelecomClientPast15StatHistoryInvSesPort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistorySesValuePort1 = _Pmc1008mpPerfTelecomClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 7),
    _Pmc1008mpPerfTelecomClientPast15StatHistorySesValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistorySesValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistoryInvSefsPort1 = _Pmc1008mpPerfTelecomClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 8),
    _Pmc1008mpPerfTelecomClientPast15StatHistoryInvSefsPort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistorySefsValuePort1 = _Pmc1008mpPerfTelecomClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 9),
    _Pmc1008mpPerfTelecomClientPast15StatHistorySefsValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistoryInvUasPort1 = _Pmc1008mpPerfTelecomClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 10),
    _Pmc1008mpPerfTelecomClientPast15StatHistoryInvUasPort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast15StatHistoryUasValuePort1 = _Pmc1008mpPerfTelecomClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 24, 1, 11),
    _Pmc1008mpPerfTelecomClientPast15StatHistoryUasValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatTable_Object = MibTable
pmc1008mpPerfTelecomClientCurrent24StatTable = _Pmc1008mpPerfTelecomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatTable.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatEntry_Object = MibTableRow
pmc1008mpPerfTelecomClientCurrent24StatEntry = _Pmc1008mpPerfTelecomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1)
)
pmc1008mpPerfTelecomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfTelecomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatEntry.setStatus("current")


class _Pmc1008mpPerfTelecomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pmc1008mpPerfTelecomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfTelecomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pmc1008mpPerfTelecomClientCurrent24StatIndex_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatIndex = _Pmc1008mpPerfTelecomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 1),
    _Pmc1008mpPerfTelecomClientCurrent24StatIndex_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatIndex.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent24StatInvCvPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatInvCvPortn = _Pmc1008mpPerfTelecomClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 2),
    _Pmc1008mpPerfTelecomClientCurrent24StatInvCvPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatInvCvPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent24StatCvValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatCvValuePortn = _Pmc1008mpPerfTelecomClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 3),
    _Pmc1008mpPerfTelecomClientCurrent24StatCvValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatCvValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent24StatInvEsPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatInvEsPortn = _Pmc1008mpPerfTelecomClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 4),
    _Pmc1008mpPerfTelecomClientCurrent24StatInvEsPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatInvEsPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent24StatEsValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatEsValuePortn = _Pmc1008mpPerfTelecomClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 5),
    _Pmc1008mpPerfTelecomClientCurrent24StatEsValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatEsValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent24StatInvSesPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatInvSesPortn = _Pmc1008mpPerfTelecomClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 6),
    _Pmc1008mpPerfTelecomClientCurrent24StatInvSesPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatInvSesPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent24StatSesValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatSesValuePortn = _Pmc1008mpPerfTelecomClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 7),
    _Pmc1008mpPerfTelecomClientCurrent24StatSesValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatSesValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatInvSefsPortn = _Pmc1008mpPerfTelecomClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 8),
    _Pmc1008mpPerfTelecomClientCurrent24StatInvSefsPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatInvSefsPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatSefsValuePortn = _Pmc1008mpPerfTelecomClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 9),
    _Pmc1008mpPerfTelecomClientCurrent24StatSefsValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatSefsValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientCurrent24StatInvUasPortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatInvUasPortn = _Pmc1008mpPerfTelecomClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 10),
    _Pmc1008mpPerfTelecomClientCurrent24StatInvUasPortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatInvUasPortn.setStatus("current")
_Pmc1008mpPerfTelecomClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomClientCurrent24StatUasValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomClientCurrent24StatUasValuePortn = _Pmc1008mpPerfTelecomClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 32, 1, 11),
    _Pmc1008mpPerfTelecomClientCurrent24StatUasValuePortn_Type()
)
pmc1008mpPerfTelecomClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientCurrent24StatUasValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryPort1Table_Object = MibTable
pmc1008mpPerfTelecomClientPast24StatHistoryPort1Table = _Pmc1008mpPerfTelecomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryPort1Table.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pmc1008mpPerfTelecomClientPast24StatHistoryPort1Entry = _Pmc1008mpPerfTelecomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1)
)
pmc1008mpPerfTelecomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index = _Pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 1),
    _Pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistoryInvCvPort1 = _Pmc1008mpPerfTelecomClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 2),
    _Pmc1008mpPerfTelecomClientPast24StatHistoryInvCvPort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistoryCvValuePort1 = _Pmc1008mpPerfTelecomClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 3),
    _Pmc1008mpPerfTelecomClientPast24StatHistoryCvValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistoryInvEsPort1 = _Pmc1008mpPerfTelecomClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 4),
    _Pmc1008mpPerfTelecomClientPast24StatHistoryInvEsPort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistoryEsValuePort1 = _Pmc1008mpPerfTelecomClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 5),
    _Pmc1008mpPerfTelecomClientPast24StatHistoryEsValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistoryInvSesPort1 = _Pmc1008mpPerfTelecomClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 6),
    _Pmc1008mpPerfTelecomClientPast24StatHistoryInvSesPort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistorySesValuePort1 = _Pmc1008mpPerfTelecomClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 7),
    _Pmc1008mpPerfTelecomClientPast24StatHistorySesValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistorySesValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistoryInvSefsPort1 = _Pmc1008mpPerfTelecomClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 8),
    _Pmc1008mpPerfTelecomClientPast24StatHistoryInvSefsPort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistorySefsValuePort1 = _Pmc1008mpPerfTelecomClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 9),
    _Pmc1008mpPerfTelecomClientPast24StatHistorySefsValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistoryInvUasPort1 = _Pmc1008mpPerfTelecomClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 10),
    _Pmc1008mpPerfTelecomClientPast24StatHistoryInvUasPort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pmc1008mpPerfTelecomClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomClientPast24StatHistoryUasValuePort1 = _Pmc1008mpPerfTelecomClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 40, 1, 11),
    _Pmc1008mpPerfTelecomClientPast24StatHistoryUasValuePort1_Type()
)
pmc1008mpPerfTelecomClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pmc1008mpPerfDatacomClientCurrent15StatTable_Object = MibTable
pmc1008mpPerfDatacomClientCurrent15StatTable = _Pmc1008mpPerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientCurrent15StatTable.setStatus("current")
_Pmc1008mpPerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pmc1008mpPerfDatacomClientCurrent15StatEntry = _Pmc1008mpPerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1)
)
pmc1008mpPerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pmc1008mpPerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pmc1008mpPerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pmc1008mpPerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pmc1008mpPerfDatacomClientCurrent15StatIndex = _Pmc1008mpPerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 1),
    _Pmc1008mpPerfDatacomClientCurrent15StatIndex_Type()
)
pmc1008mpPerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientCurrent15StatIndex.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInBytesCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatInBytesCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInBytesCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatInBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 2),
    _Pmc1008mpperfdatacomclientCurrent15StatInBytesCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInBytesCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInBytesCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatInBytesCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInBytesCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatInBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 3),
    _Pmc1008mpperfdatacomclientCurrent15StatInBytesCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInBytesCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInCrcCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 4),
    _Pmc1008mpperfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInCrcCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 5),
    _Pmc1008mpperfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 8),
    _Pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 9),
    _Pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInMulticastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatInMulticastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInMulticastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatInMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 10),
    _Pmc1008mpperfdatacomclientCurrent15StatInMulticastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInMulticastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInMulticastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatInMulticastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInMulticastCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatInMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 11),
    _Pmc1008mpperfdatacomclientCurrent15StatInMulticastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInMulticastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInUnicastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatInUnicastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInUnicastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatInUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 20),
    _Pmc1008mpperfdatacomclientCurrent15StatInUnicastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInUnicastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInUnicastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatInUnicastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInUnicastCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatInUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 21),
    _Pmc1008mpperfdatacomclientCurrent15StatInUnicastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInUnicastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 22),
    _Pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 23),
    _Pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutBytesCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatOutBytesCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutBytesCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 26),
    _Pmc1008mpperfdatacomclientCurrent15StatOutBytesCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutBytesCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutBytesCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatOutBytesCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutBytesCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 27),
    _Pmc1008mpperfdatacomclientCurrent15StatOutBytesCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutBytesCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 32),
    _Pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 33),
    _Pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 34),
    _Pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 35),
    _Pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 42),
    _Pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 43),
    _Pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 44),
    _Pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountPortn = _Pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 256, 1, 45),
    _Pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountPortn.setStatus("current")
_Pmc1008mpPerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pmc1008mpPerfDatacomClientPast15StatHistoryPort1Table = _Pmc1008mpPerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pmc1008mpPerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pmc1008mpPerfDatacomClientPast15StatHistoryPort1Entry = _Pmc1008mpPerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1)
)
pmc1008mpPerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index = _Pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 1),
    _Pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInBytesCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatInBytesCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInBytesCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatInBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 2),
    _Pmc1008mpperfdatacomclientPast15StatInBytesCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInBytesCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInBytesCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatInBytesCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInBytesCountPort1 = _Pmc1008mpperfdatacomclientPast15StatInBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 3),
    _Pmc1008mpperfdatacomclientPast15StatInBytesCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInBytesCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInCrcCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 4),
    _Pmc1008mpperfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInCrcCountPort1 = _Pmc1008mpperfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 5),
    _Pmc1008mpperfdatacomclientPast15StatInCrcCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInBroadcastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatInBroadcastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInBroadcastCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatInBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 8),
    _Pmc1008mpperfdatacomclientPast15StatInBroadcastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInBroadcastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInBroadcastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatInBroadcastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInBroadcastCountPort1 = _Pmc1008mpperfdatacomclientPast15StatInBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 9),
    _Pmc1008mpperfdatacomclientPast15StatInBroadcastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInBroadcastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInMulticastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatInMulticastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInMulticastCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatInMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 10),
    _Pmc1008mpperfdatacomclientPast15StatInMulticastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInMulticastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInMulticastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatInMulticastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInMulticastCountPort1 = _Pmc1008mpperfdatacomclientPast15StatInMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 11),
    _Pmc1008mpperfdatacomclientPast15StatInMulticastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInMulticastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInUnicastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatInUnicastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInUnicastCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatInUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 20),
    _Pmc1008mpperfdatacomclientPast15StatInUnicastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInUnicastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInUnicastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatInUnicastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInUnicastCountPort1 = _Pmc1008mpperfdatacomclientPast15StatInUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 21),
    _Pmc1008mpperfdatacomclientPast15StatInUnicastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInUnicastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInNonunicastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatInNonunicastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInNonunicastCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatInNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 22),
    _Pmc1008mpperfdatacomclientPast15StatInNonunicastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInNonunicastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatInNonunicastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatInNonunicastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatInNonunicastCountPort1 = _Pmc1008mpperfdatacomclientPast15StatInNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 23),
    _Pmc1008mpperfdatacomclientPast15StatInNonunicastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatInNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatInNonunicastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutBytesCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatOutBytesCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutBytesCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatOutBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 26),
    _Pmc1008mpperfdatacomclientPast15StatOutBytesCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutBytesCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutBytesCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatOutBytesCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutBytesCountPort1 = _Pmc1008mpperfdatacomclientPast15StatOutBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 27),
    _Pmc1008mpperfdatacomclientPast15StatOutBytesCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutBytesCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutBroadcastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatOutBroadcastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutBroadcastCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatOutBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 32),
    _Pmc1008mpperfdatacomclientPast15StatOutBroadcastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutBroadcastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutBroadcastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatOutBroadcastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutBroadcastCountPort1 = _Pmc1008mpperfdatacomclientPast15StatOutBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 33),
    _Pmc1008mpperfdatacomclientPast15StatOutBroadcastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutBroadcastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutMulticastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatOutMulticastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutMulticastCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatOutMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 34),
    _Pmc1008mpperfdatacomclientPast15StatOutMulticastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutMulticastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutMulticastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatOutMulticastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutMulticastCountPort1 = _Pmc1008mpperfdatacomclientPast15StatOutMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 35),
    _Pmc1008mpperfdatacomclientPast15StatOutMulticastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutMulticastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutUnicastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatOutUnicastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutUnicastCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatOutUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 42),
    _Pmc1008mpperfdatacomclientPast15StatOutUnicastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutUnicastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutUnicastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatOutUnicastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutUnicastCountPort1 = _Pmc1008mpperfdatacomclientPast15StatOutUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 43),
    _Pmc1008mpperfdatacomclientPast15StatOutUnicastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutUnicastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutNonunicastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast15StatOutNonunicastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutNonunicastCountInvPort1 = _Pmc1008mpperfdatacomclientPast15StatOutNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 44),
    _Pmc1008mpperfdatacomclientPast15StatOutNonunicastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutNonunicastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast15StatOutNonunicastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast15StatOutNonunicastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast15StatOutNonunicastCountPort1 = _Pmc1008mpperfdatacomclientPast15StatOutNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 264, 1, 45),
    _Pmc1008mpperfdatacomclientPast15StatOutNonunicastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast15StatOutNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast15StatOutNonunicastCountPort1.setStatus("current")
_Pmc1008mpPerfDatacomClientCurrent24StatTable_Object = MibTable
pmc1008mpPerfDatacomClientCurrent24StatTable = _Pmc1008mpPerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientCurrent24StatTable.setStatus("current")
_Pmc1008mpPerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pmc1008mpPerfDatacomClientCurrent24StatEntry = _Pmc1008mpPerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1)
)
pmc1008mpPerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pmc1008mpPerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pmc1008mpPerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pmc1008mpPerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pmc1008mpPerfDatacomClientCurrent24StatIndex = _Pmc1008mpPerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 1),
    _Pmc1008mpPerfDatacomClientCurrent24StatIndex_Type()
)
pmc1008mpPerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientCurrent24StatIndex.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInBytesCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatInBytesCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInBytesCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatInBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 2),
    _Pmc1008mpperfdatacomclientCurrent24StatInBytesCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInBytesCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInBytesCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatInBytesCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInBytesCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatInBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 3),
    _Pmc1008mpperfdatacomclientCurrent24StatInBytesCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInBytesCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInCrcCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 4),
    _Pmc1008mpperfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInCrcCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 5),
    _Pmc1008mpperfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 8),
    _Pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 9),
    _Pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInMulticastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatInMulticastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInMulticastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatInMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 10),
    _Pmc1008mpperfdatacomclientCurrent24StatInMulticastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInMulticastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInMulticastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatInMulticastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInMulticastCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatInMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 11),
    _Pmc1008mpperfdatacomclientCurrent24StatInMulticastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInMulticastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInUnicastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatInUnicastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInUnicastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatInUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 20),
    _Pmc1008mpperfdatacomclientCurrent24StatInUnicastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInUnicastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInUnicastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatInUnicastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInUnicastCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatInUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 21),
    _Pmc1008mpperfdatacomclientCurrent24StatInUnicastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInUnicastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 22),
    _Pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 23),
    _Pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutBytesCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatOutBytesCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutBytesCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 26),
    _Pmc1008mpperfdatacomclientCurrent24StatOutBytesCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutBytesCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutBytesCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatOutBytesCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutBytesCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 27),
    _Pmc1008mpperfdatacomclientCurrent24StatOutBytesCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutBytesCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 32),
    _Pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 33),
    _Pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 34),
    _Pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 35),
    _Pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 42),
    _Pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 43),
    _Pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type = EkiOnOff
_Pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountInvPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 44),
    _Pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setStatus("current")
_Pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountPortn_Type = Counter64
_Pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountPortn_Object = MibTableColumn
pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountPortn = _Pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 272, 1, 45),
    _Pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountPortn_Type()
)
pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountPortn.setStatus("current")
_Pmc1008mpPerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pmc1008mpPerfDatacomClientPast24StatHistoryPort1Table = _Pmc1008mpPerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pmc1008mpPerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pmc1008mpPerfDatacomClientPast24StatHistoryPort1Entry = _Pmc1008mpPerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1)
)
pmc1008mpPerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index = _Pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 1),
    _Pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInBytesCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatInBytesCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInBytesCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatInBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 2),
    _Pmc1008mpperfdatacomclientPast24StatInBytesCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInBytesCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInBytesCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatInBytesCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInBytesCountPort1 = _Pmc1008mpperfdatacomclientPast24StatInBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 3),
    _Pmc1008mpperfdatacomclientPast24StatInBytesCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInBytesCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInCrcCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 4),
    _Pmc1008mpperfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInCrcCountPort1 = _Pmc1008mpperfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 5),
    _Pmc1008mpperfdatacomclientPast24StatInCrcCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInBroadcastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatInBroadcastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInBroadcastCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatInBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 8),
    _Pmc1008mpperfdatacomclientPast24StatInBroadcastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInBroadcastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInBroadcastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatInBroadcastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInBroadcastCountPort1 = _Pmc1008mpperfdatacomclientPast24StatInBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 9),
    _Pmc1008mpperfdatacomclientPast24StatInBroadcastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInBroadcastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInMulticastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatInMulticastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInMulticastCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatInMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 10),
    _Pmc1008mpperfdatacomclientPast24StatInMulticastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInMulticastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInMulticastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatInMulticastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInMulticastCountPort1 = _Pmc1008mpperfdatacomclientPast24StatInMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 11),
    _Pmc1008mpperfdatacomclientPast24StatInMulticastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInMulticastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInUnicastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatInUnicastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInUnicastCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatInUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 20),
    _Pmc1008mpperfdatacomclientPast24StatInUnicastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInUnicastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInUnicastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatInUnicastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInUnicastCountPort1 = _Pmc1008mpperfdatacomclientPast24StatInUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 21),
    _Pmc1008mpperfdatacomclientPast24StatInUnicastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInUnicastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInNonunicastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatInNonunicastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInNonunicastCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatInNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 22),
    _Pmc1008mpperfdatacomclientPast24StatInNonunicastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInNonunicastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatInNonunicastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatInNonunicastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatInNonunicastCountPort1 = _Pmc1008mpperfdatacomclientPast24StatInNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 23),
    _Pmc1008mpperfdatacomclientPast24StatInNonunicastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatInNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatInNonunicastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutBytesCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatOutBytesCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutBytesCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatOutBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 26),
    _Pmc1008mpperfdatacomclientPast24StatOutBytesCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutBytesCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutBytesCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatOutBytesCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutBytesCountPort1 = _Pmc1008mpperfdatacomclientPast24StatOutBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 27),
    _Pmc1008mpperfdatacomclientPast24StatOutBytesCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutBytesCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutBroadcastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatOutBroadcastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutBroadcastCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatOutBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 32),
    _Pmc1008mpperfdatacomclientPast24StatOutBroadcastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutBroadcastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutBroadcastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatOutBroadcastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutBroadcastCountPort1 = _Pmc1008mpperfdatacomclientPast24StatOutBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 33),
    _Pmc1008mpperfdatacomclientPast24StatOutBroadcastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutBroadcastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutMulticastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatOutMulticastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutMulticastCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatOutMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 34),
    _Pmc1008mpperfdatacomclientPast24StatOutMulticastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutMulticastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutMulticastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatOutMulticastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutMulticastCountPort1 = _Pmc1008mpperfdatacomclientPast24StatOutMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 35),
    _Pmc1008mpperfdatacomclientPast24StatOutMulticastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutMulticastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutUnicastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatOutUnicastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutUnicastCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatOutUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 42),
    _Pmc1008mpperfdatacomclientPast24StatOutUnicastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutUnicastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutUnicastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatOutUnicastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutUnicastCountPort1 = _Pmc1008mpperfdatacomclientPast24StatOutUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 43),
    _Pmc1008mpperfdatacomclientPast24StatOutUnicastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutUnicastCountPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutNonunicastCountInvPort1_Type = EkiOnOff
_Pmc1008mpperfdatacomclientPast24StatOutNonunicastCountInvPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutNonunicastCountInvPort1 = _Pmc1008mpperfdatacomclientPast24StatOutNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 44),
    _Pmc1008mpperfdatacomclientPast24StatOutNonunicastCountInvPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutNonunicastCountInvPort1.setStatus("current")
_Pmc1008mpperfdatacomclientPast24StatOutNonunicastCountPort1_Type = Counter64
_Pmc1008mpperfdatacomclientPast24StatOutNonunicastCountPort1_Object = MibTableColumn
pmc1008mpperfdatacomclientPast24StatOutNonunicastCountPort1 = _Pmc1008mpperfdatacomclientPast24StatOutNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 2, 280, 1, 45),
    _Pmc1008mpperfdatacomclientPast24StatOutNonunicastCountPort1_Type()
)
pmc1008mpperfdatacomclientPast24StatOutNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpperfdatacomclientPast24StatOutNonunicastCountPort1.setStatus("current")
_Pmc1008mpMonLine_ObjectIdentity = ObjectIdentity
pmc1008mpMonLine = _Pmc1008mpMonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3)
)
_Pmc1008mpPerfTelecomLineCurrent15StatTable_Object = MibTable
pmc1008mpPerfTelecomLineCurrent15StatTable = _Pmc1008mpPerfTelecomLineCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatTable.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatEntry_Object = MibTableRow
pmc1008mpPerfTelecomLineCurrent15StatEntry = _Pmc1008mpPerfTelecomLineCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1)
)
pmc1008mpPerfTelecomLineCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfTelecomLineCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatEntry.setStatus("current")


class _Pmc1008mpPerfTelecomLineCurrent15StatIndex_Type(Integer32):
    """Custom type pmc1008mpPerfTelecomLineCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfTelecomLineCurrent15StatIndex_Type.__name__ = "Integer32"
_Pmc1008mpPerfTelecomLineCurrent15StatIndex_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatIndex = _Pmc1008mpPerfTelecomLineCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 1),
    _Pmc1008mpPerfTelecomLineCurrent15StatIndex_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatIndex.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatInvCvPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent15StatInvCvPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatInvCvPortn = _Pmc1008mpPerfTelecomLineCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 2),
    _Pmc1008mpPerfTelecomLineCurrent15StatInvCvPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatInvCvPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatCvValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent15StatCvValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatCvValuePortn = _Pmc1008mpPerfTelecomLineCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 3),
    _Pmc1008mpPerfTelecomLineCurrent15StatCvValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatCvValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatInvEsPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent15StatInvEsPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatInvEsPortn = _Pmc1008mpPerfTelecomLineCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 4),
    _Pmc1008mpPerfTelecomLineCurrent15StatInvEsPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatInvEsPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatEsValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent15StatEsValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatEsValuePortn = _Pmc1008mpPerfTelecomLineCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 5),
    _Pmc1008mpPerfTelecomLineCurrent15StatEsValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatEsValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatInvSesPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent15StatInvSesPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatInvSesPortn = _Pmc1008mpPerfTelecomLineCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 6),
    _Pmc1008mpPerfTelecomLineCurrent15StatInvSesPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatInvSesPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatSesValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent15StatSesValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatSesValuePortn = _Pmc1008mpPerfTelecomLineCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 7),
    _Pmc1008mpPerfTelecomLineCurrent15StatSesValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatSesValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent15StatInvSefsPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatInvSefsPortn = _Pmc1008mpPerfTelecomLineCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 8),
    _Pmc1008mpPerfTelecomLineCurrent15StatInvSefsPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatInvSefsPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatSefsValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent15StatSefsValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatSefsValuePortn = _Pmc1008mpPerfTelecomLineCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 9),
    _Pmc1008mpPerfTelecomLineCurrent15StatSefsValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatSefsValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatInvUasPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent15StatInvUasPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatInvUasPortn = _Pmc1008mpPerfTelecomLineCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 10),
    _Pmc1008mpPerfTelecomLineCurrent15StatInvUasPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatInvUasPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent15StatUasValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent15StatUasValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent15StatUasValuePortn = _Pmc1008mpPerfTelecomLineCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 128, 1, 11),
    _Pmc1008mpPerfTelecomLineCurrent15StatUasValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent15StatUasValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryPort1Table_Object = MibTable
pmc1008mpPerfTelecomLinePast15StatHistoryPort1Table = _Pmc1008mpPerfTelecomLinePast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryPort1Table.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryPort1Entry_Object = MibTableRow
pmc1008mpPerfTelecomLinePast15StatHistoryPort1Entry = _Pmc1008mpPerfTelecomLinePast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1)
)
pmc1008mpPerfTelecomLinePast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryPort1Entry.setStatus("current")


class _Pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index = _Pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 1),
    _Pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvCvPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistoryInvCvPort1 = _Pmc1008mpPerfTelecomLinePast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 2),
    _Pmc1008mpPerfTelecomLinePast15StatHistoryInvCvPort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryInvCvPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryCvValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast15StatHistoryCvValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistoryCvValuePort1 = _Pmc1008mpPerfTelecomLinePast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 3),
    _Pmc1008mpPerfTelecomLinePast15StatHistoryCvValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryCvValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvEsPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistoryInvEsPort1 = _Pmc1008mpPerfTelecomLinePast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 4),
    _Pmc1008mpPerfTelecomLinePast15StatHistoryInvEsPort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryInvEsPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryEsValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast15StatHistoryEsValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistoryEsValuePort1 = _Pmc1008mpPerfTelecomLinePast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 5),
    _Pmc1008mpPerfTelecomLinePast15StatHistoryEsValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryEsValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvSesPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistoryInvSesPort1 = _Pmc1008mpPerfTelecomLinePast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 6),
    _Pmc1008mpPerfTelecomLinePast15StatHistoryInvSesPort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryInvSesPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistorySesValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast15StatHistorySesValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistorySesValuePort1 = _Pmc1008mpPerfTelecomLinePast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 7),
    _Pmc1008mpPerfTelecomLinePast15StatHistorySesValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistorySesValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvSefsPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistoryInvSefsPort1 = _Pmc1008mpPerfTelecomLinePast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 8),
    _Pmc1008mpPerfTelecomLinePast15StatHistoryInvSefsPort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryInvSefsPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistorySefsValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast15StatHistorySefsValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistorySefsValuePort1 = _Pmc1008mpPerfTelecomLinePast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 9),
    _Pmc1008mpPerfTelecomLinePast15StatHistorySefsValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistorySefsValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast15StatHistoryInvUasPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistoryInvUasPort1 = _Pmc1008mpPerfTelecomLinePast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 10),
    _Pmc1008mpPerfTelecomLinePast15StatHistoryInvUasPort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryInvUasPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast15StatHistoryUasValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast15StatHistoryUasValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast15StatHistoryUasValuePort1 = _Pmc1008mpPerfTelecomLinePast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 129, 1, 11),
    _Pmc1008mpPerfTelecomLinePast15StatHistoryUasValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast15StatHistoryUasValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatTable_Object = MibTable
pmc1008mpPerfTelecomLineCurrent24StatTable = _Pmc1008mpPerfTelecomLineCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatTable.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatEntry_Object = MibTableRow
pmc1008mpPerfTelecomLineCurrent24StatEntry = _Pmc1008mpPerfTelecomLineCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1)
)
pmc1008mpPerfTelecomLineCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfTelecomLineCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatEntry.setStatus("current")


class _Pmc1008mpPerfTelecomLineCurrent24StatIndex_Type(Integer32):
    """Custom type pmc1008mpPerfTelecomLineCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfTelecomLineCurrent24StatIndex_Type.__name__ = "Integer32"
_Pmc1008mpPerfTelecomLineCurrent24StatIndex_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatIndex = _Pmc1008mpPerfTelecomLineCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 1),
    _Pmc1008mpPerfTelecomLineCurrent24StatIndex_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatIndex.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatInvCvPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent24StatInvCvPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatInvCvPortn = _Pmc1008mpPerfTelecomLineCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 2),
    _Pmc1008mpPerfTelecomLineCurrent24StatInvCvPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatInvCvPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatCvValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent24StatCvValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatCvValuePortn = _Pmc1008mpPerfTelecomLineCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 3),
    _Pmc1008mpPerfTelecomLineCurrent24StatCvValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatCvValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatInvEsPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent24StatInvEsPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatInvEsPortn = _Pmc1008mpPerfTelecomLineCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 4),
    _Pmc1008mpPerfTelecomLineCurrent24StatInvEsPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatInvEsPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatEsValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent24StatEsValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatEsValuePortn = _Pmc1008mpPerfTelecomLineCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 5),
    _Pmc1008mpPerfTelecomLineCurrent24StatEsValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatEsValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatInvSesPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent24StatInvSesPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatInvSesPortn = _Pmc1008mpPerfTelecomLineCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 6),
    _Pmc1008mpPerfTelecomLineCurrent24StatInvSesPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatInvSesPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatSesValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent24StatSesValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatSesValuePortn = _Pmc1008mpPerfTelecomLineCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 7),
    _Pmc1008mpPerfTelecomLineCurrent24StatSesValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatSesValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent24StatInvSefsPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatInvSefsPortn = _Pmc1008mpPerfTelecomLineCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 8),
    _Pmc1008mpPerfTelecomLineCurrent24StatInvSefsPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatInvSefsPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatSefsValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent24StatSefsValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatSefsValuePortn = _Pmc1008mpPerfTelecomLineCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 9),
    _Pmc1008mpPerfTelecomLineCurrent24StatSefsValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatSefsValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatInvUasPortn_Type = EkiOnOff
_Pmc1008mpPerfTelecomLineCurrent24StatInvUasPortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatInvUasPortn = _Pmc1008mpPerfTelecomLineCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 10),
    _Pmc1008mpPerfTelecomLineCurrent24StatInvUasPortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatInvUasPortn.setStatus("current")
_Pmc1008mpPerfTelecomLineCurrent24StatUasValuePortn_Type = Unsigned32
_Pmc1008mpPerfTelecomLineCurrent24StatUasValuePortn_Object = MibTableColumn
pmc1008mpPerfTelecomLineCurrent24StatUasValuePortn = _Pmc1008mpPerfTelecomLineCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 130, 1, 11),
    _Pmc1008mpPerfTelecomLineCurrent24StatUasValuePortn_Type()
)
pmc1008mpPerfTelecomLineCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLineCurrent24StatUasValuePortn.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryPort1Table_Object = MibTable
pmc1008mpPerfTelecomLinePast24StatHistoryPort1Table = _Pmc1008mpPerfTelecomLinePast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131)
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryPort1Table.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryPort1Entry_Object = MibTableRow
pmc1008mpPerfTelecomLinePast24StatHistoryPort1Entry = _Pmc1008mpPerfTelecomLinePast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1)
)
pmc1008mpPerfTelecomLinePast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pmc1008MP-MIB", "pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryPort1Entry.setStatus("current")


class _Pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index = _Pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 1),
    _Pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvCvPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistoryInvCvPort1 = _Pmc1008mpPerfTelecomLinePast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 2),
    _Pmc1008mpPerfTelecomLinePast24StatHistoryInvCvPort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryInvCvPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryCvValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast24StatHistoryCvValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistoryCvValuePort1 = _Pmc1008mpPerfTelecomLinePast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 3),
    _Pmc1008mpPerfTelecomLinePast24StatHistoryCvValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryCvValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvEsPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistoryInvEsPort1 = _Pmc1008mpPerfTelecomLinePast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 4),
    _Pmc1008mpPerfTelecomLinePast24StatHistoryInvEsPort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryInvEsPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryEsValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast24StatHistoryEsValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistoryEsValuePort1 = _Pmc1008mpPerfTelecomLinePast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 5),
    _Pmc1008mpPerfTelecomLinePast24StatHistoryEsValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryEsValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvSesPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistoryInvSesPort1 = _Pmc1008mpPerfTelecomLinePast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 6),
    _Pmc1008mpPerfTelecomLinePast24StatHistoryInvSesPort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryInvSesPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistorySesValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast24StatHistorySesValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistorySesValuePort1 = _Pmc1008mpPerfTelecomLinePast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 7),
    _Pmc1008mpPerfTelecomLinePast24StatHistorySesValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistorySesValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvSefsPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistoryInvSefsPort1 = _Pmc1008mpPerfTelecomLinePast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 8),
    _Pmc1008mpPerfTelecomLinePast24StatHistoryInvSefsPort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryInvSefsPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistorySefsValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast24StatHistorySefsValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistorySefsValuePort1 = _Pmc1008mpPerfTelecomLinePast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 9),
    _Pmc1008mpPerfTelecomLinePast24StatHistorySefsValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistorySefsValuePort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc1008mpPerfTelecomLinePast24StatHistoryInvUasPort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistoryInvUasPort1 = _Pmc1008mpPerfTelecomLinePast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 10),
    _Pmc1008mpPerfTelecomLinePast24StatHistoryInvUasPort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryInvUasPort1.setStatus("current")
_Pmc1008mpPerfTelecomLinePast24StatHistoryUasValuePort1_Type = Unsigned32
_Pmc1008mpPerfTelecomLinePast24StatHistoryUasValuePort1_Object = MibTableColumn
pmc1008mpPerfTelecomLinePast24StatHistoryUasValuePort1 = _Pmc1008mpPerfTelecomLinePast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 47, 11, 3, 131, 1, 11),
    _Pmc1008mpPerfTelecomLinePast24StatHistoryUasValuePort1_Type()
)
pmc1008mpPerfTelecomLinePast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1008mpPerfTelecomLinePast24StatHistoryUasValuePort1.setStatus("current")

# Managed Objects groups


# Notification objects

pmc1008mpLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 30)
)
pmc1008mpLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmLineDdmWarningPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapLineNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmc1008mpLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 31)
)
pmc1008mpLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmLineDdmWarningPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapLineNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmc1008mpLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 32)
)
pmc1008mpLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmLineDdmAlmPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapLineNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmc1008mpLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 33)
)
pmc1008mpLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmLineDdmAlmPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapLineNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmc1008mpLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 34)
)
pmc1008mpLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmLineFailPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmLineHwFailPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapLineNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpLineTrapCritGoesOn.setStatus(
        "current"
    )

pmc1008mpLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 35)
)
pmc1008mpLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmLineFailPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmLineHwFailPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapLineNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpLineTrapCritGoesOff.setStatus(
        "current"
    )

pmc1008mpClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 40)
)
pmc1008mpClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapPortNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmc1008mpClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 41)
)
pmc1008mpClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapPortNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmc1008mpClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 42)
)
pmc1008mpClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapPortNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmc1008mpClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 43)
)
pmc1008mpClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapPortNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmc1008mpClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 44)
)
pmc1008mpClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmFailAccPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmHwFailAccPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapPortNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpClientTrapCritGoesOn.setStatus(
        "current"
    )

pmc1008mpClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 45)
)
pmc1008mpClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmFailAccPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmHwFailAccPortn"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapPortNumber"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpClientTrapCritGoesOff.setStatus(
        "current"
    )

pmc1008mpPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 50)
)
pmc1008mpPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmDefFuseB"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmDefFuseA"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmc1008mpPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 47, 10, 51)
)
pmc1008mpPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmDefFuseB"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mpAlmDefFuseA"),
        ("EKINOPS-Pmc1008MP-MIB", "pmc1008mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1008mpPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmc1008MP-MIB",
    **{"Pmc1008mpModeTimeSlot": Pmc1008mpModeTimeSlot,
       "Pmc1008mpModeAddDropA": Pmc1008mpModeAddDropA,
       "Pmc1008mpModeAddDrop": Pmc1008mpModeAddDrop,
       "Pmc1008mpProtectionTimeSlot": Pmc1008mpProtectionTimeSlot,
       "Pmc1008mpProtectionStartUp": Pmc1008mpProtectionStartUp,
       "Pmc1008mpDccMode": Pmc1008mpDccMode,
       "Pmc1008mpOtxMode": Pmc1008mpOtxMode,
       "Pmc1008mpOtxGrid": Pmc1008mpOtxGrid,
       "Pmc1008mpAdjustValue": Pmc1008mpAdjustValue,
       "Pmc1008mpOtxChannel": Pmc1008mpOtxChannel,
       "modulePmc1008mp": modulePmc1008mp,
       "pmc1008mpalarms": pmc1008mpalarms,
       "pmc1008mpAlmOther": pmc1008mpAlmOther,
       "pmc1008mpAlmOtherNurg": pmc1008mpAlmOtherNurg,
       "pmc1008mpAlmsynthAlm2": pmc1008mpAlmsynthAlm2,
       "pmc1008mpAlmConfTableSave": pmc1008mpAlmConfTableSave,
       "pmc1008mpAlmInvUpload": pmc1008mpAlmInvUpload,
       "pmc1008mpAlmConfTableLoad": pmc1008mpAlmConfTableLoad,
       "pmc1008mpAlmCorrelatOff": pmc1008mpAlmCorrelatOff,
       "pmc1008mpAlmOtherUrg": pmc1008mpAlmOtherUrg,
       "pmc1008mpAlmmodInitFailLevel2": pmc1008mpAlmmodInitFailLevel2,
       "pmc1008mpAlmLedFail": pmc1008mpAlmLedFail,
       "pmc1008mpAlmNextColdBootForced": pmc1008mpAlmNextColdBootForced,
       "pmc1008mpAlmBootUndone": pmc1008mpAlmBootUndone,
       "pmc1008mpAlmResetHwInitFail": pmc1008mpAlmResetHwInitFail,
       "pmc1008mpAlmSwInitFail": pmc1008mpAlmSwInitFail,
       "pmc1008mpAlmmodInitFailLevel3": pmc1008mpAlmmodInitFailLevel3,
       "pmc1008mpAlmGwIdentFail": pmc1008mpAlmGwIdentFail,
       "pmc1008mpAlmObmTypeReadFail": pmc1008mpAlmObmTypeReadFail,
       "pmc1008mpAlmInitModuleFail": pmc1008mpAlmInitModuleFail,
       "pmc1008mpAlmXfp1InitFail": pmc1008mpAlmXfp1InitFail,
       "pmc1008mpAlmXfp2InitFail": pmc1008mpAlmXfp2InitFail,
       "pmc1008mpAlmLine1InitFail": pmc1008mpAlmLine1InitFail,
       "pmc1008mpAlmLine2InitFail": pmc1008mpAlmLine2InitFail,
       "pmc1008mpAlmClient1InitFail": pmc1008mpAlmClient1InitFail,
       "pmc1008mpAlmClient2InitFail": pmc1008mpAlmClient2InitFail,
       "pmc1008mpAlmClient3InitFail": pmc1008mpAlmClient3InitFail,
       "pmc1008mpAlmClient4InitFail": pmc1008mpAlmClient4InitFail,
       "pmc1008mpAlmClient5InitFail": pmc1008mpAlmClient5InitFail,
       "pmc1008mpAlmClient6InitFail": pmc1008mpAlmClient6InitFail,
       "pmc1008mpAlmClient7InitFail": pmc1008mpAlmClient7InitFail,
       "pmc1008mpAlmClient8InitFail": pmc1008mpAlmClient8InitFail,
       "pmc1008mpAlmadddropTsClientRxProt": pmc1008mpAlmadddropTsClientRxProt,
       "pmc1008mpAlmAdddropClient1West": pmc1008mpAlmAdddropClient1West,
       "pmc1008mpAlmAdddropClient2West": pmc1008mpAlmAdddropClient2West,
       "pmc1008mpAlmAdddropClient3West": pmc1008mpAlmAdddropClient3West,
       "pmc1008mpAlmAdddropClient4West": pmc1008mpAlmAdddropClient4West,
       "pmc1008mpAlmAdddropClient5West": pmc1008mpAlmAdddropClient5West,
       "pmc1008mpAlmAdddropClient6West": pmc1008mpAlmAdddropClient6West,
       "pmc1008mpAlmAdddropClient7West": pmc1008mpAlmAdddropClient7West,
       "pmc1008mpAlmAdddropClient8West": pmc1008mpAlmAdddropClient8West,
       "pmc1008mpAlmAdddropClient1East": pmc1008mpAlmAdddropClient1East,
       "pmc1008mpAlmAdddropClient2East": pmc1008mpAlmAdddropClient2East,
       "pmc1008mpAlmAdddropClient3East": pmc1008mpAlmAdddropClient3East,
       "pmc1008mpAlmAdddropClient4East": pmc1008mpAlmAdddropClient4East,
       "pmc1008mpAlmAdddropClient5East": pmc1008mpAlmAdddropClient5East,
       "pmc1008mpAlmAdddropClient6East": pmc1008mpAlmAdddropClient6East,
       "pmc1008mpAlmAdddropClient7East": pmc1008mpAlmAdddropClient7East,
       "pmc1008mpAlmAdddropClient8East": pmc1008mpAlmAdddropClient8East,
       "pmc1008mpAlmOtherCrit": pmc1008mpAlmOtherCrit,
       "pmc1008mpAlmsynthAlm0": pmc1008mpAlmsynthAlm0,
       "pmc1008mpAlmModGlobFail": pmc1008mpAlmModGlobFail,
       "pmc1008mpAlmDefFuseA": pmc1008mpAlmDefFuseA,
       "pmc1008mpAlmDefFuseB": pmc1008mpAlmDefFuseB,
       "pmc1008mpAlmClient": pmc1008mpAlmClient,
       "pmc1008mpAlmClientNurg": pmc1008mpAlmClientNurg,
       "pmc1008mpAlmsfpWarnDdmTable": pmc1008mpAlmsfpWarnDdmTable,
       "pmc1008mpAlmsfpWarnDdmEntry": pmc1008mpAlmsfpWarnDdmEntry,
       "pmc1008mpAlmsfpWarnDdmIndex": pmc1008mpAlmsfpWarnDdmIndex,
       "pmc1008mpAlmTxPwLowWngPortn": pmc1008mpAlmTxPwLowWngPortn,
       "pmc1008mpAlmTxPwrHighWngPortn": pmc1008mpAlmTxPwrHighWngPortn,
       "pmc1008mpAlmTxBiasLowWngPortn": pmc1008mpAlmTxBiasLowWngPortn,
       "pmc1008mpAlmTxBiasHighWngPortn": pmc1008mpAlmTxBiasHighWngPortn,
       "pmc1008mpAlmVccLowWngPortn": pmc1008mpAlmVccLowWngPortn,
       "pmc1008mpAlmVccHighWngPortn": pmc1008mpAlmVccHighWngPortn,
       "pmc1008mpAlmTempLowWngPortn": pmc1008mpAlmTempLowWngPortn,
       "pmc1008mpAlmTempHighWngPortn": pmc1008mpAlmTempHighWngPortn,
       "pmc1008mpAlmRxPwrLowWngPortn": pmc1008mpAlmRxPwrLowWngPortn,
       "pmc1008mpAlmRxPwrHighWngPortn": pmc1008mpAlmRxPwrHighWngPortn,
       "pmc1008mpAlmClientUrg": pmc1008mpAlmClientUrg,
       "pmc1008mpAlmsfpAlmDdmTable": pmc1008mpAlmsfpAlmDdmTable,
       "pmc1008mpAlmsfpAlmDdmEntry": pmc1008mpAlmsfpAlmDdmEntry,
       "pmc1008mpAlmsfpAlmDdmIndex": pmc1008mpAlmsfpAlmDdmIndex,
       "pmc1008mpAlmTxPwrLowAlaPortn": pmc1008mpAlmTxPwrLowAlaPortn,
       "pmc1008mpAlmTxPwrHighAlaPortn": pmc1008mpAlmTxPwrHighAlaPortn,
       "pmc1008mpAlmTxBiasLowAlaPortn": pmc1008mpAlmTxBiasLowAlaPortn,
       "pmc1008mpAlmTxBiasHighAlaPortn": pmc1008mpAlmTxBiasHighAlaPortn,
       "pmc1008mpAlmVccLowAlaPortn": pmc1008mpAlmVccLowAlaPortn,
       "pmc1008mpAlmVccHighAlaPortn": pmc1008mpAlmVccHighAlaPortn,
       "pmc1008mpAlmTempLowAlaPortn": pmc1008mpAlmTempLowAlaPortn,
       "pmc1008mpAlmTempHighAlaPortn": pmc1008mpAlmTempHighAlaPortn,
       "pmc1008mpAlmRxPwrLowAlaPortn": pmc1008mpAlmRxPwrLowAlaPortn,
       "pmc1008mpAlmRxPwrHighAlaPortn": pmc1008mpAlmRxPwrHighAlaPortn,
       "pmc1008mpAlmClientCrit": pmc1008mpAlmClientCrit,
       "pmc1008mpAlmsynthAlmPortTable": pmc1008mpAlmsynthAlmPortTable,
       "pmc1008mpAlmsynthAlmPortEntry": pmc1008mpAlmsynthAlmPortEntry,
       "pmc1008mpAlmsynthAlmPortIndex": pmc1008mpAlmsynthAlmPortIndex,
       "pmc1008mpAlmSfpAbsentPortn": pmc1008mpAlmSfpAbsentPortn,
       "pmc1008mpAlmDdmAbsentPortn": pmc1008mpAlmDdmAbsentPortn,
       "pmc1008mpAlmHwFailAccPortn": pmc1008mpAlmHwFailAccPortn,
       "pmc1008mpAlmDwLsdPortn": pmc1008mpAlmDwLsdPortn,
       "pmc1008mpAlmClientLocalOosPortn": pmc1008mpAlmClientLocalOosPortn,
       "pmc1008mpAlmClientRemoteOosPortn": pmc1008mpAlmClientRemoteOosPortn,
       "pmc1008mpAlmDwCaisPortn": pmc1008mpAlmDwCaisPortn,
       "pmc1008mpAlmSfpDdmWarningPortn": pmc1008mpAlmSfpDdmWarningPortn,
       "pmc1008mpAlmSfpDdmAlmPortn": pmc1008mpAlmSfpDdmAlmPortn,
       "pmc1008mpAlmFailAccPortn": pmc1008mpAlmFailAccPortn,
       "pmc1008mpAlmClientActivePortn": pmc1008mpAlmClientActivePortn,
       "pmc1008mpAlmUpCsfPortn": pmc1008mpAlmUpCsfPortn,
       "pmc1008mpAlmaccessioAlmTable": pmc1008mpAlmaccessioAlmTable,
       "pmc1008mpAlmaccessioAlmEntry": pmc1008mpAlmaccessioAlmEntry,
       "pmc1008mpAlmaccessioAlmIndex": pmc1008mpAlmaccessioAlmIndex,
       "pmc1008mpAlmDwLasFailPortn": pmc1008mpAlmDwLasFailPortn,
       "pmc1008mpAlmUpLosPortn": pmc1008mpAlmUpLosPortn,
       "pmc1008mpAlmmapperDeAlmTable": pmc1008mpAlmmapperDeAlmTable,
       "pmc1008mpAlmmapperDeAlmEntry": pmc1008mpAlmmapperDeAlmEntry,
       "pmc1008mpAlmmapperDeAlmIndex": pmc1008mpAlmmapperDeAlmIndex,
       "pmc1008mpAlmUpAccOosPortn": pmc1008mpAlmUpAccOosPortn,
       "pmc1008mpAlmUpBufferOvlPortn": pmc1008mpAlmUpBufferOvlPortn,
       "pmc1008mpAlmDwCsfDetPortn": pmc1008mpAlmDwCsfDetPortn,
       "pmc1008mpAlmDwBufferOvlPortn": pmc1008mpAlmDwBufferOvlPortn,
       "pmc1008mpAlmLine": pmc1008mpAlmLine,
       "pmc1008mpAlmLineNurg": pmc1008mpAlmLineNurg,
       "pmc1008mpAlmlineXfp1WarningsTable": pmc1008mpAlmlineXfp1WarningsTable,
       "pmc1008mpAlmlineXfp1WarningsEntry": pmc1008mpAlmlineXfp1WarningsEntry,
       "pmc1008mpAlmlineXfp1WarningsIndex": pmc1008mpAlmlineXfp1WarningsIndex,
       "pmc1008mpAlmTxPowerLowWarningPortn": pmc1008mpAlmTxPowerLowWarningPortn,
       "pmc1008mpAlmTxPowerHighWarningPortn": pmc1008mpAlmTxPowerHighWarningPortn,
       "pmc1008mpAlmTxBiasLowWarningPortn": pmc1008mpAlmTxBiasLowWarningPortn,
       "pmc1008mpAlmTxBiasHighWarningPortn": pmc1008mpAlmTxBiasHighWarningPortn,
       "pmc1008mpAlmTempLowWarningPortn": pmc1008mpAlmTempLowWarningPortn,
       "pmc1008mpAlmTempHighWarningPortn": pmc1008mpAlmTempHighWarningPortn,
       "pmc1008mpAlmRxPowerLowWarningPortn": pmc1008mpAlmRxPowerLowWarningPortn,
       "pmc1008mpAlmRxPowerHighWarningPortn": pmc1008mpAlmRxPowerHighWarningPortn,
       "pmc1008mpAlmlineOtx1TlhWarningsTable": pmc1008mpAlmlineOtx1TlhWarningsTable,
       "pmc1008mpAlmlineOtx1TlhWarningsEntry": pmc1008mpAlmlineOtx1TlhWarningsEntry,
       "pmc1008mpAlmlineOtx1TlhWarningsIndex": pmc1008mpAlmlineOtx1TlhWarningsIndex,
       "pmc1008mpAlmLineModulatorAgingHighWarningPortn": pmc1008mpAlmLineModulatorAgingHighWarningPortn,
       "pmc1008mpAlmLineAgingHighWarningPortn": pmc1008mpAlmLineAgingHighWarningPortn,
       "pmc1008mpAlmLineFreqDevHighWarningPortn": pmc1008mpAlmLineFreqDevHighWarningPortn,
       "pmc1008mpAlmLineLaserTempHighWarningPortn": pmc1008mpAlmLineLaserTempHighWarningPortn,
       "pmc1008mpAlmLineUrg": pmc1008mpAlmLineUrg,
       "pmc1008mpAlmdfrmBerTable": pmc1008mpAlmdfrmBerTable,
       "pmc1008mpAlmdfrmBerEntry": pmc1008mpAlmdfrmBerEntry,
       "pmc1008mpAlmdfrmBerIndex": pmc1008mpAlmdfrmBerIndex,
       "pmc1008mpAlmLineSignalDegradePortn": pmc1008mpAlmLineSignalDegradePortn,
       "pmc1008mpAlmLineSignalFailPortn": pmc1008mpAlmLineSignalFailPortn,
       "pmc1008mpAlmLineDegradePortn": pmc1008mpAlmLineDegradePortn,
       "pmc1008mpAlmlineXfp1AlarmTable": pmc1008mpAlmlineXfp1AlarmTable,
       "pmc1008mpAlmlineXfp1AlarmEntry": pmc1008mpAlmlineXfp1AlarmEntry,
       "pmc1008mpAlmlineXfp1AlarmIndex": pmc1008mpAlmlineXfp1AlarmIndex,
       "pmc1008mpAlmTxPowerLowAlarmPortn": pmc1008mpAlmTxPowerLowAlarmPortn,
       "pmc1008mpAlmTxPowerHighAlarmPortn": pmc1008mpAlmTxPowerHighAlarmPortn,
       "pmc1008mpAlmTxBiasLowAlarmPortn": pmc1008mpAlmTxBiasLowAlarmPortn,
       "pmc1008mpAlmTxBiasHighAlarmPortn": pmc1008mpAlmTxBiasHighAlarmPortn,
       "pmc1008mpAlmTempLowAlarmPortn": pmc1008mpAlmTempLowAlarmPortn,
       "pmc1008mpAlmTempHighAlarmPortn": pmc1008mpAlmTempHighAlarmPortn,
       "pmc1008mpAlmRxPowerLowAlarmPortn": pmc1008mpAlmRxPowerLowAlarmPortn,
       "pmc1008mpAlmRxPowerHighAlarmPortn": pmc1008mpAlmRxPowerHighAlarmPortn,
       "pmc1008mpAlmlineXfp1SupplyAlarmTable": pmc1008mpAlmlineXfp1SupplyAlarmTable,
       "pmc1008mpAlmlineXfp1SupplyAlarmEntry": pmc1008mpAlmlineXfp1SupplyAlarmEntry,
       "pmc1008mpAlmlineXfp1SupplyAlarmIndex": pmc1008mpAlmlineXfp1SupplyAlarmIndex,
       "pmc1008mpAlmVee5LowAlarmPortn": pmc1008mpAlmVee5LowAlarmPortn,
       "pmc1008mpAlmVee5HighAlarmPortn": pmc1008mpAlmVee5HighAlarmPortn,
       "pmc1008mpAlmVcc2LowAlarmPortn": pmc1008mpAlmVcc2LowAlarmPortn,
       "pmc1008mpAlmVcc2HighAlarmPortn": pmc1008mpAlmVcc2HighAlarmPortn,
       "pmc1008mpAlmVcc3LowAlarmPortn": pmc1008mpAlmVcc3LowAlarmPortn,
       "pmc1008mpAlmVcc3HighAlarmPortn": pmc1008mpAlmVcc3HighAlarmPortn,
       "pmc1008mpAlmVcc5LowAlarmPortn": pmc1008mpAlmVcc5LowAlarmPortn,
       "pmc1008mpAlmVcc5HighAlarmPortn": pmc1008mpAlmVcc5HighAlarmPortn,
       "pmc1008mpAlmVee5LowWarningPortn": pmc1008mpAlmVee5LowWarningPortn,
       "pmc1008mpAlmVee5HighWarningPortn": pmc1008mpAlmVee5HighWarningPortn,
       "pmc1008mpAlmVcc2LowWarningPortn": pmc1008mpAlmVcc2LowWarningPortn,
       "pmc1008mpAlmVcc2HighWarningPortn": pmc1008mpAlmVcc2HighWarningPortn,
       "pmc1008mpAlmVcc3LowWarningPortn": pmc1008mpAlmVcc3LowWarningPortn,
       "pmc1008mpAlmVcc3HighWarningPortn": pmc1008mpAlmVcc3HighWarningPortn,
       "pmc1008mpAlmVcc5LowWarningPortn": pmc1008mpAlmVcc5LowWarningPortn,
       "pmc1008mpAlmVcc5HighWarningPortn": pmc1008mpAlmVcc5HighWarningPortn,
       "pmc1008mpAlmlineOtx1TlhAlarmsTable": pmc1008mpAlmlineOtx1TlhAlarmsTable,
       "pmc1008mpAlmlineOtx1TlhAlarmsEntry": pmc1008mpAlmlineOtx1TlhAlarmsEntry,
       "pmc1008mpAlmlineOtx1TlhAlarmsIndex": pmc1008mpAlmlineOtx1TlhAlarmsIndex,
       "pmc1008mpAlmLineModulatorAgingHighAlaPortn": pmc1008mpAlmLineModulatorAgingHighAlaPortn,
       "pmc1008mpAlmLineAgingHighAlaPortn": pmc1008mpAlmLineAgingHighAlaPortn,
       "pmc1008mpAlmLineCdrNotReadyPortn": pmc1008mpAlmLineCdrNotReadyPortn,
       "pmc1008mpAlmLineFreqDevHighAlaPortn": pmc1008mpAlmLineFreqDevHighAlaPortn,
       "pmc1008mpAlmLineLaserTempHighAlaPortn": pmc1008mpAlmLineLaserTempHighAlaPortn,
       "pmc1008mpAlmLineCrit": pmc1008mpAlmLineCrit,
       "pmc1008mpAlmsynthAlmLineTable": pmc1008mpAlmsynthAlmLineTable,
       "pmc1008mpAlmsynthAlmLineEntry": pmc1008mpAlmsynthAlmLineEntry,
       "pmc1008mpAlmsynthAlmLineIndex": pmc1008mpAlmsynthAlmLineIndex,
       "pmc1008mpAlmXfpAbsentPortn": pmc1008mpAlmXfpAbsentPortn,
       "pmc1008mpAlmXfpInitNotComplPortn": pmc1008mpAlmXfpInitNotComplPortn,
       "pmc1008mpAlmLineHwFailPortn": pmc1008mpAlmLineHwFailPortn,
       "pmc1008mpAlmXfpTxOffPortn": pmc1008mpAlmXfpTxOffPortn,
       "pmc1008mpAlmLineLocalOosPortn": pmc1008mpAlmLineLocalOosPortn,
       "pmc1008mpAlmUpRdiInsPortn": pmc1008mpAlmUpRdiInsPortn,
       "pmc1008mpAlmLineDdmWarningPortn": pmc1008mpAlmLineDdmWarningPortn,
       "pmc1008mpAlmLineDdmAlmPortn": pmc1008mpAlmLineDdmAlmPortn,
       "pmc1008mpAlmLineFailPortn": pmc1008mpAlmLineFailPortn,
       "pmc1008mpAlmLineActivePortn": pmc1008mpAlmLineActivePortn,
       "pmc1008mpAlmdfrmAlmTable": pmc1008mpAlmdfrmAlmTable,
       "pmc1008mpAlmdfrmAlmEntry": pmc1008mpAlmdfrmAlmEntry,
       "pmc1008mpAlmdfrmAlmIndex": pmc1008mpAlmdfrmAlmIndex,
       "pmc1008mpAlmDwAisDetPortn": pmc1008mpAlmDwAisDetPortn,
       "pmc1008mpAlmDwRdiDetPortn": pmc1008mpAlmDwRdiDetPortn,
       "pmc1008mpAlmDwOofPortn": pmc1008mpAlmDwOofPortn,
       "pmc1008mpAlmDwLofPortn": pmc1008mpAlmDwLofPortn,
       "pmc1008mpAlmlineSyncAlarmsTable": pmc1008mpAlmlineSyncAlarmsTable,
       "pmc1008mpAlmlineSyncAlarmsEntry": pmc1008mpAlmlineSyncAlarmsEntry,
       "pmc1008mpAlmlineSyncAlarmsIndex": pmc1008mpAlmlineSyncAlarmsIndex,
       "pmc1008mpAlmDwLockerrPortn": pmc1008mpAlmDwLockerrPortn,
       "pmc1008mpAlmUpLockerrPortn": pmc1008mpAlmUpLockerrPortn,
       "pmc1008mpAlmDwLosPortn": pmc1008mpAlmDwLosPortn,
       "pmc1008mpAlmlineXfp1AlarmsTable": pmc1008mpAlmlineXfp1AlarmsTable,
       "pmc1008mpAlmlineXfp1AlarmsEntry": pmc1008mpAlmlineXfp1AlarmsEntry,
       "pmc1008mpAlmlineXfp1AlarmsIndex": pmc1008mpAlmlineXfp1AlarmsIndex,
       "pmc1008mpAlmModNrPortn": pmc1008mpAlmModNrPortn,
       "pmc1008mpAlmRxCdrNotLockedPortn": pmc1008mpAlmRxCdrNotLockedPortn,
       "pmc1008mpAlmRxNrPortn": pmc1008mpAlmRxNrPortn,
       "pmc1008mpAlmTxCdrNotLockedPortn": pmc1008mpAlmTxCdrNotLockedPortn,
       "pmc1008mpAlmTxFaultPortn": pmc1008mpAlmTxFaultPortn,
       "pmc1008mpAlmTxNrPortn": pmc1008mpAlmTxNrPortn,
       "pmc1008mpAlmChannelNotAcquiredPortn": pmc1008mpAlmChannelNotAcquiredPortn,
       "pmc1008mpAlmWavelengthUnlockedPortn": pmc1008mpAlmWavelengthUnlockedPortn,
       "pmc1008mpAlmTecFaultPortn": pmc1008mpAlmTecFaultPortn,
       "pmc1008mpAlmApdSupplyFaultPortn": pmc1008mpAlmApdSupplyFaultPortn,
       "pmc1008mpmeasures": pmc1008mpmeasures,
       "pmc1008mpMesrOther": pmc1008mpMesrOther,
       "pmc1008mpMesrsynth0": pmc1008mpMesrsynth0,
       "pmc1008mpMesrsynth1": pmc1008mpMesrsynth1,
       "pmc1008mpMesrClient": pmc1008mpMesrClient,
       "pmc1008mpMesrtempMeasTable": pmc1008mpMesrtempMeasTable,
       "pmc1008mpMesrtempMeasEntry": pmc1008mpMesrtempMeasEntry,
       "pmc1008mpMesrtempMeasIndex": pmc1008mpMesrtempMeasIndex,
       "pmc1008mpMesrtempMeasPortn": pmc1008mpMesrtempMeasPortn,
       "pmc1008mpMesrvoltMeasTable": pmc1008mpMesrvoltMeasTable,
       "pmc1008mpMesrvoltMeasEntry": pmc1008mpMesrvoltMeasEntry,
       "pmc1008mpMesrvoltMeasIndex": pmc1008mpMesrvoltMeasIndex,
       "pmc1008mpMesrvoltMeasPortn": pmc1008mpMesrvoltMeasPortn,
       "pmc1008mpMesrbiasMeasTable": pmc1008mpMesrbiasMeasTable,
       "pmc1008mpMesrbiasMeasEntry": pmc1008mpMesrbiasMeasEntry,
       "pmc1008mpMesrbiasMeasIndex": pmc1008mpMesrbiasMeasIndex,
       "pmc1008mpMesrbiasMeasPortn": pmc1008mpMesrbiasMeasPortn,
       "pmc1008mpMesrtxpwrMeasTable": pmc1008mpMesrtxpwrMeasTable,
       "pmc1008mpMesrtxpwrMeasEntry": pmc1008mpMesrtxpwrMeasEntry,
       "pmc1008mpMesrtxpwrMeasIndex": pmc1008mpMesrtxpwrMeasIndex,
       "pmc1008mpMesrtxpwrMeasPortn": pmc1008mpMesrtxpwrMeasPortn,
       "pmc1008mpMesrrxpwrMeasTable": pmc1008mpMesrrxpwrMeasTable,
       "pmc1008mpMesrrxpwrMeasEntry": pmc1008mpMesrrxpwrMeasEntry,
       "pmc1008mpMesrrxpwrMeasIndex": pmc1008mpMesrrxpwrMeasIndex,
       "pmc1008mpMesrrxpwrMeasPortn": pmc1008mpMesrrxpwrMeasPortn,
       "pmc1008mpMesrLine": pmc1008mpMesrLine,
       "pmc1008mpMesrxfp1LxModTempMeasTable": pmc1008mpMesrxfp1LxModTempMeasTable,
       "pmc1008mpMesrxfp1LxModTempMeasEntry": pmc1008mpMesrxfp1LxModTempMeasEntry,
       "pmc1008mpMesrxfp1LxModTempMeasIndex": pmc1008mpMesrxfp1LxModTempMeasIndex,
       "pmc1008mpMesrxfp1LxModTempMeasPortn": pmc1008mpMesrxfp1LxModTempMeasPortn,
       "pmc1008mpMesrxfp1ReservedTable": pmc1008mpMesrxfp1ReservedTable,
       "pmc1008mpMesrxfp1ReservedEntry": pmc1008mpMesrxfp1ReservedEntry,
       "pmc1008mpMesrxfp1ReservedIndex": pmc1008mpMesrxfp1ReservedIndex,
       "pmc1008mpMesrxfp1ReservedPortn": pmc1008mpMesrxfp1ReservedPortn,
       "pmc1008mpMesrxfp1LoBiasCurrentMeasTable": pmc1008mpMesrxfp1LoBiasCurrentMeasTable,
       "pmc1008mpMesrxfp1LoBiasCurrentMeasEntry": pmc1008mpMesrxfp1LoBiasCurrentMeasEntry,
       "pmc1008mpMesrxfp1LoBiasCurrentMeasIndex": pmc1008mpMesrxfp1LoBiasCurrentMeasIndex,
       "pmc1008mpMesrxfp1LoBiasCurrentMeasPortn": pmc1008mpMesrxfp1LoBiasCurrentMeasPortn,
       "pmc1008mpMesrxfp1LoTxPowerMeasTable": pmc1008mpMesrxfp1LoTxPowerMeasTable,
       "pmc1008mpMesrxfp1LoTxPowerMeasEntry": pmc1008mpMesrxfp1LoTxPowerMeasEntry,
       "pmc1008mpMesrxfp1LoTxPowerMeasIndex": pmc1008mpMesrxfp1LoTxPowerMeasIndex,
       "pmc1008mpMesrxfp1LoTxPowerMeasPortn": pmc1008mpMesrxfp1LoTxPowerMeasPortn,
       "pmc1008mpMesrxfp1LiRxPowerMeasTable": pmc1008mpMesrxfp1LiRxPowerMeasTable,
       "pmc1008mpMesrxfp1LiRxPowerMeasEntry": pmc1008mpMesrxfp1LiRxPowerMeasEntry,
       "pmc1008mpMesrxfp1LiRxPowerMeasIndex": pmc1008mpMesrxfp1LiRxPowerMeasIndex,
       "pmc1008mpMesrxfp1LiRxPowerMeasPortn": pmc1008mpMesrxfp1LiRxPowerMeasPortn,
       "pmc1008mpMesrxfp1LxAux1MeasTable": pmc1008mpMesrxfp1LxAux1MeasTable,
       "pmc1008mpMesrxfp1LxAux1MeasEntry": pmc1008mpMesrxfp1LxAux1MeasEntry,
       "pmc1008mpMesrxfp1LxAux1MeasIndex": pmc1008mpMesrxfp1LxAux1MeasIndex,
       "pmc1008mpMesrxfp1LxAux1MeasPortn": pmc1008mpMesrxfp1LxAux1MeasPortn,
       "pmc1008mpMesrxfp1LxAux2MeasTable": pmc1008mpMesrxfp1LxAux2MeasTable,
       "pmc1008mpMesrxfp1LxAux2MeasEntry": pmc1008mpMesrxfp1LxAux2MeasEntry,
       "pmc1008mpMesrxfp1LxAux2MeasIndex": pmc1008mpMesrxfp1LxAux2MeasIndex,
       "pmc1008mpMesrxfp1LxAux2MeasPortn": pmc1008mpMesrxfp1LxAux2MeasPortn,
       "pmc1008mpMesrotx1AgingTable": pmc1008mpMesrotx1AgingTable,
       "pmc1008mpMesrotx1AgingEntry": pmc1008mpMesrotx1AgingEntry,
       "pmc1008mpMesrotx1AgingIndex": pmc1008mpMesrotx1AgingIndex,
       "pmc1008mpMesrotx1AgingPortn": pmc1008mpMesrotx1AgingPortn,
       "pmc1008mpMesrotx1LaserTemperatureTable": pmc1008mpMesrotx1LaserTemperatureTable,
       "pmc1008mpMesrotx1LaserTemperatureEntry": pmc1008mpMesrotx1LaserTemperatureEntry,
       "pmc1008mpMesrotx1LaserTemperatureIndex": pmc1008mpMesrotx1LaserTemperatureIndex,
       "pmc1008mpMesrotx1LaserTemperaturePortn": pmc1008mpMesrotx1LaserTemperaturePortn,
       "pmc1008mpMesrotx1FreqDeviationTable": pmc1008mpMesrotx1FreqDeviationTable,
       "pmc1008mpMesrotx1FreqDeviationEntry": pmc1008mpMesrotx1FreqDeviationEntry,
       "pmc1008mpMesrotx1FreqDeviationIndex": pmc1008mpMesrotx1FreqDeviationIndex,
       "pmc1008mpMesrotx1FreqDeviationPortn": pmc1008mpMesrotx1FreqDeviationPortn,
       "pmc1008mpMesrotx1LaserWvlengthTable": pmc1008mpMesrotx1LaserWvlengthTable,
       "pmc1008mpMesrotx1LaserWvlengthEntry": pmc1008mpMesrotx1LaserWvlengthEntry,
       "pmc1008mpMesrotx1LaserWvlengthIndex": pmc1008mpMesrotx1LaserWvlengthIndex,
       "pmc1008mpMesrotx1LaserWvlengthPortn": pmc1008mpMesrotx1LaserWvlengthPortn,
       "pmc1008mpcounters": pmc1008mpcounters,
       "pmc1008mpCntOther": pmc1008mpCntOther,
       "pmc1008mpCntClient": pmc1008mpCntClient,
       "pmc1008mpCntupRaRemCntTable": pmc1008mpCntupRaRemCntTable,
       "pmc1008mpCntupRaRemCntEntry": pmc1008mpCntupRaRemCntEntry,
       "pmc1008mpCntupRaRemCntIndex": pmc1008mpCntupRaRemCntIndex,
       "pmc1008mpCntupRaRemCntValuePortn": pmc1008mpCntupRaRemCntValuePortn,
       "pmc1008mpCntupRaRemCntErrorPortn": pmc1008mpCntupRaRemCntErrorPortn,
       "pmc1008mpCntupRaRemCntOverloadPortn": pmc1008mpCntupRaRemCntOverloadPortn,
       "pmc1008mpCntupRaInsCntTable": pmc1008mpCntupRaInsCntTable,
       "pmc1008mpCntupRaInsCntEntry": pmc1008mpCntupRaInsCntEntry,
       "pmc1008mpCntupRaInsCntIndex": pmc1008mpCntupRaInsCntIndex,
       "pmc1008mpCntupRaInsCntValuePortn": pmc1008mpCntupRaInsCntValuePortn,
       "pmc1008mpCntupRaInsCntErrorPortn": pmc1008mpCntupRaInsCntErrorPortn,
       "pmc1008mpCntupRaInsCntOverloadPortn": pmc1008mpCntupRaInsCntOverloadPortn,
       "pmc1008mpCntupRdErrCntTable": pmc1008mpCntupRdErrCntTable,
       "pmc1008mpCntupRdErrCntEntry": pmc1008mpCntupRdErrCntEntry,
       "pmc1008mpCntupRdErrCntIndex": pmc1008mpCntupRdErrCntIndex,
       "pmc1008mpCntupRdErrCntValuePortn": pmc1008mpCntupRdErrCntValuePortn,
       "pmc1008mpCntupRdErrCntErrorPortn": pmc1008mpCntupRdErrCntErrorPortn,
       "pmc1008mpCntupRdErrCntOverloadPortn": pmc1008mpCntupRdErrCntOverloadPortn,
       "pmc1008mpCntupTimCntTable": pmc1008mpCntupTimCntTable,
       "pmc1008mpCntupTimCntEntry": pmc1008mpCntupTimCntEntry,
       "pmc1008mpCntupTimCntIndex": pmc1008mpCntupTimCntIndex,
       "pmc1008mpCntupTimCntValuePortn": pmc1008mpCntupTimCntValuePortn,
       "pmc1008mpCntupTimCntErrorPortn": pmc1008mpCntupTimCntErrorPortn,
       "pmc1008mpCntupTimCntOverloadPortn": pmc1008mpCntupTimCntOverloadPortn,
       "pmc1008mpCntupCvErrCntTable": pmc1008mpCntupCvErrCntTable,
       "pmc1008mpCntupCvErrCntEntry": pmc1008mpCntupCvErrCntEntry,
       "pmc1008mpCntupCvErrCntIndex": pmc1008mpCntupCvErrCntIndex,
       "pmc1008mpCntupCvErrCntValuePortn": pmc1008mpCntupCvErrCntValuePortn,
       "pmc1008mpCntupCvErrCntErrorPortn": pmc1008mpCntupCvErrCntErrorPortn,
       "pmc1008mpCntupCvErrCntOverloadPortn": pmc1008mpCntupCvErrCntOverloadPortn,
       "pmc1008mpCntdwCbipCntTable": pmc1008mpCntdwCbipCntTable,
       "pmc1008mpCntdwCbipCntEntry": pmc1008mpCntdwCbipCntEntry,
       "pmc1008mpCntdwCbipCntIndex": pmc1008mpCntdwCbipCntIndex,
       "pmc1008mpCntdwCbipCntValuePortn": pmc1008mpCntdwCbipCntValuePortn,
       "pmc1008mpCntdwCbipCntErrorPortn": pmc1008mpCntdwCbipCntErrorPortn,
       "pmc1008mpCntdwCbipCntOverloadPortn": pmc1008mpCntdwCbipCntOverloadPortn,
       "pmc1008mpCntdwTimCntTable": pmc1008mpCntdwTimCntTable,
       "pmc1008mpCntdwTimCntEntry": pmc1008mpCntdwTimCntEntry,
       "pmc1008mpCntdwTimCntIndex": pmc1008mpCntdwTimCntIndex,
       "pmc1008mpCntdwTimCntValuePortn": pmc1008mpCntdwTimCntValuePortn,
       "pmc1008mpCntdwTimCntErrorPortn": pmc1008mpCntdwTimCntErrorPortn,
       "pmc1008mpCntdwTimCntOverloadPortn": pmc1008mpCntdwTimCntOverloadPortn,
       "pmc1008mpCntLine": pmc1008mpCntLine,
       "pmc1008mpCntdfrmB1ErrCntTable": pmc1008mpCntdfrmB1ErrCntTable,
       "pmc1008mpCntdfrmB1ErrCntEntry": pmc1008mpCntdfrmB1ErrCntEntry,
       "pmc1008mpCntdfrmB1ErrCntIndex": pmc1008mpCntdfrmB1ErrCntIndex,
       "pmc1008mpCntdfrmB1ErrCntValuePortn": pmc1008mpCntdfrmB1ErrCntValuePortn,
       "pmc1008mpCntdfrmB1ErrCntErrorPortn": pmc1008mpCntdfrmB1ErrCntErrorPortn,
       "pmc1008mpCntdfrmB1ErrCntOverloadPortn": pmc1008mpCntdfrmB1ErrCntOverloadPortn,
       "pmc1008mpCntdfrmTimCntTable": pmc1008mpCntdfrmTimCntTable,
       "pmc1008mpCntdfrmTimCntEntry": pmc1008mpCntdfrmTimCntEntry,
       "pmc1008mpCntdfrmTimCntIndex": pmc1008mpCntdfrmTimCntIndex,
       "pmc1008mpCntdfrmTimCntValuePortn": pmc1008mpCntdfrmTimCntValuePortn,
       "pmc1008mpCntdfrmTimCntErrorPortn": pmc1008mpCntdfrmTimCntErrorPortn,
       "pmc1008mpCntdfrmTimCntOverloadPortn": pmc1008mpCntdfrmTimCntOverloadPortn,
       "pmc1008mpCntdfrmPrimLineErrCntTable": pmc1008mpCntdfrmPrimLineErrCntTable,
       "pmc1008mpCntdfrmPrimLineErrCntEntry": pmc1008mpCntdfrmPrimLineErrCntEntry,
       "pmc1008mpCntdfrmPrimLineErrCntIndex": pmc1008mpCntdfrmPrimLineErrCntIndex,
       "pmc1008mpCntdfrmPrimLineErrCntValuePortn": pmc1008mpCntdfrmPrimLineErrCntValuePortn,
       "pmc1008mpCntdfrmPrimLineErrCntErrorPortn": pmc1008mpCntdfrmPrimLineErrCntErrorPortn,
       "pmc1008mpCntdfrmPrimLineErrCntOverloadPortn": pmc1008mpCntdfrmPrimLineErrCntOverloadPortn,
       "pmc1008mpCntCountersReset": pmc1008mpCntCountersReset,
       "pmc1008mpCntCountersStop": pmc1008mpCntCountersStop,
       "pmc1008mpcontrolsWrite": pmc1008mpcontrolsWrite,
       "pmc1008mpCtrlOther": pmc1008mpCtrlOther,
       "pmc1008mpCtrlconfMgnt1": pmc1008mpCtrlconfMgnt1,
       "pmc1008mpCtrlConf1Load1": pmc1008mpCtrlConf1Load1,
       "pmc1008mpCtrlConf2Load1": pmc1008mpCtrlConf2Load1,
       "pmc1008mpCtrlConf2Flash1": pmc1008mpCtrlConf2Flash1,
       "pmc1008mpCtrlConf2Clear1": pmc1008mpCtrlConf2Clear1,
       "pmc1008mpCtrlsynth4": pmc1008mpCtrlsynth4,
       "pmc1008mpCtrlCorrelatOn": pmc1008mpCtrlCorrelatOn,
       "pmc1008mpCtrlCorrelatOff": pmc1008mpCtrlCorrelatOff,
       "pmc1008mpCtrlswMgnt": pmc1008mpCtrlswMgnt,
       "pmc1008mpCtrlColdReset": pmc1008mpCtrlColdReset,
       "pmc1008mpCtrlWarmReset": pmc1008mpCtrlWarmReset,
       "pmc1008mpCtrlLoadSwBank1": pmc1008mpCtrlLoadSwBank1,
       "pmc1008mpCtrlLoadSwBank2": pmc1008mpCtrlLoadSwBank2,
       "pmc1008mpCtrlgwMgnt": pmc1008mpCtrlgwMgnt,
       "pmc1008mpCtrlCurrentGwReset": pmc1008mpCtrlCurrentGwReset,
       "pmc1008mpCtrlLoadGwBank1": pmc1008mpCtrlLoadGwBank1,
       "pmc1008mpCtrlLoadGwBank2": pmc1008mpCtrlLoadGwBank2,
       "pmc1008mpCtrlLoadGwBank3": pmc1008mpCtrlLoadGwBank3,
       "pmc1008mpCtrlLoadGwBank4": pmc1008mpCtrlLoadGwBank4,
       "pmc1008mpCtrlledTest": pmc1008mpCtrlledTest,
       "pmc1008mpCtrlGreenLed": pmc1008mpCtrlGreenLed,
       "pmc1008mpCtrlRedLed": pmc1008mpCtrlRedLed,
       "pmc1008mpCtrlLedOff": pmc1008mpCtrlLedOff,
       "pmc1008mpCtrlmoduleOosMode": pmc1008mpCtrlmoduleOosMode,
       "pmc1008mpCtrlModuleOosMode": pmc1008mpCtrlModuleOosMode,
       "pmc1008mpCtrlmoduleDccMgnt": pmc1008mpCtrlmoduleDccMgnt,
       "pmc1008mpCtrlmaintenanceMode": pmc1008mpCtrlmaintenanceMode,
       "pmc1008mpCtrlMaintenanceMode": pmc1008mpCtrlMaintenanceMode,
       "pmc1008mpCtrlClient": pmc1008mpCtrlClient,
       "pmc1008mpCtrlaccessLoopTable": pmc1008mpCtrlaccessLoopTable,
       "pmc1008mpCtrlaccessLoopEntry": pmc1008mpCtrlaccessLoopEntry,
       "pmc1008mpCtrlaccessLoopIndex": pmc1008mpCtrlaccessLoopIndex,
       "pmc1008mpCtrlaccessLoopPortn": pmc1008mpCtrlaccessLoopPortn,
       "pmc1008mpCtrlportOosModeTable": pmc1008mpCtrlportOosModeTable,
       "pmc1008mpCtrlportOosModeEntry": pmc1008mpCtrlportOosModeEntry,
       "pmc1008mpCtrlportOosModeIndex": pmc1008mpCtrlportOosModeIndex,
       "pmc1008mpCtrlportOosModePortn": pmc1008mpCtrlportOosModePortn,
       "pmc1008mpCtrlsfpOnCtrlTable": pmc1008mpCtrlsfpOnCtrlTable,
       "pmc1008mpCtrlsfpOnCtrlEntry": pmc1008mpCtrlsfpOnCtrlEntry,
       "pmc1008mpCtrlsfpOnCtrlIndex": pmc1008mpCtrlsfpOnCtrlIndex,
       "pmc1008mpCtrlsfpOnCtrlPortn": pmc1008mpCtrlsfpOnCtrlPortn,
       "pmc1008mpCtrlsfpOffCtrlTable": pmc1008mpCtrlsfpOffCtrlTable,
       "pmc1008mpCtrlsfpOffCtrlEntry": pmc1008mpCtrlsfpOffCtrlEntry,
       "pmc1008mpCtrlsfpOffCtrlIndex": pmc1008mpCtrlsfpOffCtrlIndex,
       "pmc1008mpCtrlsfpOffCtrlPortn": pmc1008mpCtrlsfpOffCtrlPortn,
       "pmc1008mpCtrlcsfUpInsTable": pmc1008mpCtrlcsfUpInsTable,
       "pmc1008mpCtrlcsfUpInsEntry": pmc1008mpCtrlcsfUpInsEntry,
       "pmc1008mpCtrlcsfUpInsIndex": pmc1008mpCtrlcsfUpInsIndex,
       "pmc1008mpCtrlcsfUpInsPortn": pmc1008mpCtrlcsfUpInsPortn,
       "pmc1008mpCtrlcaisDwInsTable": pmc1008mpCtrlcaisDwInsTable,
       "pmc1008mpCtrlcaisDwInsEntry": pmc1008mpCtrlcaisDwInsEntry,
       "pmc1008mpCtrlcaisDwInsIndex": pmc1008mpCtrlcaisDwInsIndex,
       "pmc1008mpCtrlcaisDwInsPortn": pmc1008mpCtrlcaisDwInsPortn,
       "pmc1008mpCtrlclientAccessTermLoopTable": pmc1008mpCtrlclientAccessTermLoopTable,
       "pmc1008mpCtrlclientAccessTermLoopEntry": pmc1008mpCtrlclientAccessTermLoopEntry,
       "pmc1008mpCtrlclientAccessTermLoopIndex": pmc1008mpCtrlclientAccessTermLoopIndex,
       "pmc1008mpCtrlclientAccessTermLoopPortn": pmc1008mpCtrlclientAccessTermLoopPortn,
       "pmc1008mpCtrlprotocolTable": pmc1008mpCtrlprotocolTable,
       "pmc1008mpCtrlprotocolEntry": pmc1008mpCtrlprotocolEntry,
       "pmc1008mpCtrlprotocolIndex": pmc1008mpCtrlprotocolIndex,
       "pmc1008mpCtrlprotocolPortn": pmc1008mpCtrlprotocolPortn,
       "pmc1008mpCtrladddropTsClientARxProtectTable": pmc1008mpCtrladddropTsClientARxProtectTable,
       "pmc1008mpCtrladddropTsClientARxProtectEntry": pmc1008mpCtrladddropTsClientARxProtectEntry,
       "pmc1008mpCtrladddropTsClientARxProtectIndex": pmc1008mpCtrladddropTsClientARxProtectIndex,
       "pmc1008mpCtrladddropTsClientARxProtectPortn": pmc1008mpCtrladddropTsClientARxProtectPortn,
       "pmc1008mpCtrladddropTsPairModeTable": pmc1008mpCtrladddropTsPairModeTable,
       "pmc1008mpCtrladddropTsPairModeEntry": pmc1008mpCtrladddropTsPairModeEntry,
       "pmc1008mpCtrladddropTsPairModeIndex": pmc1008mpCtrladddropTsPairModeIndex,
       "pmc1008mpCtrladddropTsPairModePortn": pmc1008mpCtrladddropTsPairModePortn,
       "pmc1008mpCtrlclientResetAllCountTable": pmc1008mpCtrlclientResetAllCountTable,
       "pmc1008mpCtrlclientResetAllCountEntry": pmc1008mpCtrlclientResetAllCountEntry,
       "pmc1008mpCtrlclientResetAllCountIndex": pmc1008mpCtrlclientResetAllCountIndex,
       "pmc1008mpCtrlclientResetAllCountsPortn": pmc1008mpCtrlclientResetAllCountsPortn,
       "pmc1008mpCtrlLine": pmc1008mpCtrlLine,
       "pmc1008mpCtrlcommAccessLoop": pmc1008mpCtrlcommAccessLoop,
       "pmc1008mpCtrlCommAccessloop": pmc1008mpCtrlCommAccessloop,
       "pmc1008mpCtrllineLoop": pmc1008mpCtrllineLoop,
       "pmc1008mpCtrlLineLoop": pmc1008mpCtrlLineLoop,
       "pmc1008mpCtrlmsAis": pmc1008mpCtrlmsAis,
       "pmc1008mpCtrlMsAis": pmc1008mpCtrlMsAis,
       "pmc1008mpCtrlfecDisableTable": pmc1008mpCtrlfecDisableTable,
       "pmc1008mpCtrlfecDisableEntry": pmc1008mpCtrlfecDisableEntry,
       "pmc1008mpCtrlfecDisableIndex": pmc1008mpCtrlfecDisableIndex,
       "pmc1008mpCtrlfecDisablePortn": pmc1008mpCtrlfecDisablePortn,
       "pmc1008mpCtrllineOosModeTable": pmc1008mpCtrllineOosModeTable,
       "pmc1008mpCtrllineOosModeEntry": pmc1008mpCtrllineOosModeEntry,
       "pmc1008mpCtrllineOosModeIndex": pmc1008mpCtrllineOosModeIndex,
       "pmc1008mpCtrllineOosModePortn": pmc1008mpCtrllineOosModePortn,
       "pmc1008mpCtrlxfpOnoffTable": pmc1008mpCtrlxfpOnoffTable,
       "pmc1008mpCtrlxfpOnoffEntry": pmc1008mpCtrlxfpOnoffEntry,
       "pmc1008mpCtrlxfpOnoffIndex": pmc1008mpCtrlxfpOnoffIndex,
       "pmc1008mpCtrlxfpOnoffPortn": pmc1008mpCtrlxfpOnoffPortn,
       "pmc1008mpCtrlxfpLineLoopTable": pmc1008mpCtrlxfpLineLoopTable,
       "pmc1008mpCtrlxfpLineLoopEntry": pmc1008mpCtrlxfpLineLoopEntry,
       "pmc1008mpCtrlxfpLineLoopIndex": pmc1008mpCtrlxfpLineLoopIndex,
       "pmc1008mpCtrlxfpLineLoopPortn": pmc1008mpCtrlxfpLineLoopPortn,
       "pmc1008mpCtrlxfpXfiLoopTable": pmc1008mpCtrlxfpXfiLoopTable,
       "pmc1008mpCtrlxfpXfiLoopEntry": pmc1008mpCtrlxfpXfiLoopEntry,
       "pmc1008mpCtrlxfpXfiLoopIndex": pmc1008mpCtrlxfpXfiLoopIndex,
       "pmc1008mpCtrlxfpXfiLoopPortn": pmc1008mpCtrlxfpXfiLoopPortn,
       "pmc1008mpCtrllineTunableChannelTable": pmc1008mpCtrllineTunableChannelTable,
       "pmc1008mpCtrllineTunableChannelEntry": pmc1008mpCtrllineTunableChannelEntry,
       "pmc1008mpCtrllineTunableChannelIndex": pmc1008mpCtrllineTunableChannelIndex,
       "pmc1008mpCtrllineTunableChannelPortn": pmc1008mpCtrllineTunableChannelPortn,
       "pmc1008mpCtrllinePhotodiodeModeTable": pmc1008mpCtrllinePhotodiodeModeTable,
       "pmc1008mpCtrllinePhotodiodeModeEntry": pmc1008mpCtrllinePhotodiodeModeEntry,
       "pmc1008mpCtrllinePhotodiodeModeIndex": pmc1008mpCtrllinePhotodiodeModeIndex,
       "pmc1008mpCtrllinePhotodiodeModePortn": pmc1008mpCtrllinePhotodiodeModePortn,
       "pmc1008mpCtrllinePhotodiodeValueTable": pmc1008mpCtrllinePhotodiodeValueTable,
       "pmc1008mpCtrllinePhotodiodeValueEntry": pmc1008mpCtrllinePhotodiodeValueEntry,
       "pmc1008mpCtrllinePhotodiodeValueIndex": pmc1008mpCtrllinePhotodiodeValueIndex,
       "pmc1008mpCtrllinePhotodiodeValuePortn": pmc1008mpCtrllinePhotodiodeValuePortn,
       "pmc1008mpCtrllinePowerLaserTable": pmc1008mpCtrllinePowerLaserTable,
       "pmc1008mpCtrllinePowerLaserEntry": pmc1008mpCtrllinePowerLaserEntry,
       "pmc1008mpCtrllinePowerLaserIndex": pmc1008mpCtrllinePowerLaserIndex,
       "pmc1008mpCtrllinePowerLaserPortn": pmc1008mpCtrllinePowerLaserPortn,
       "pmc1008mpCtrlotxVlhResetTable": pmc1008mpCtrlotxVlhResetTable,
       "pmc1008mpCtrlotxVlhResetEntry": pmc1008mpCtrlotxVlhResetEntry,
       "pmc1008mpCtrlotxVlhResetIndex": pmc1008mpCtrlotxVlhResetIndex,
       "pmc1008mpCtrlOtxVlhResetPortn": pmc1008mpCtrlOtxVlhResetPortn,
       "pmc1008mpCtrllineAccessLoopTable": pmc1008mpCtrllineAccessLoopTable,
       "pmc1008mpCtrllineAccessLoopEntry": pmc1008mpCtrllineAccessLoopEntry,
       "pmc1008mpCtrllineAccessLoopIndex": pmc1008mpCtrllineAccessLoopIndex,
       "pmc1008mpCtrllineAccessLoopPortn": pmc1008mpCtrllineAccessLoopPortn,
       "pmc1008mpCtrllineLoopTransceiverTable": pmc1008mpCtrllineLoopTransceiverTable,
       "pmc1008mpCtrllineLoopTransceiverEntry": pmc1008mpCtrllineLoopTransceiverEntry,
       "pmc1008mpCtrllineLoopTransceiverIndex": pmc1008mpCtrllineLoopTransceiverIndex,
       "pmc1008mpCtrllineLoopTransceiverPortn": pmc1008mpCtrllineLoopTransceiverPortn,
       "pmc1008mpCtrllineResetAllCountTable": pmc1008mpCtrllineResetAllCountTable,
       "pmc1008mpCtrllineResetAllCountEntry": pmc1008mpCtrllineResetAllCountEntry,
       "pmc1008mpCtrllineResetAllCountIndex": pmc1008mpCtrllineResetAllCountIndex,
       "pmc1008mpCtrllineResetAllCountsPortn": pmc1008mpCtrllineResetAllCountsPortn,
       "pmc1008mpri": pmc1008mpri,
       "pmc1008mpriTable": pmc1008mpriTable,
       "pmc1008mpRinvSfpTable": pmc1008mpRinvSfpTable,
       "pmc1008mpRinvSfpEntry": pmc1008mpRinvSfpEntry,
       "pmc1008mpRinvSfpIndex": pmc1008mpRinvSfpIndex,
       "pmc1008mpRinvsfp": pmc1008mpRinvsfp,
       "pmc1008mpRinvLineTable": pmc1008mpRinvLineTable,
       "pmc1008mpRinvLineEntry": pmc1008mpRinvLineEntry,
       "pmc1008mpRinvLineIndex": pmc1008mpRinvLineIndex,
       "pmc1008mpRinvxfpLine": pmc1008mpRinvxfpLine,
       "pmc1008mpRinvReloadInventory": pmc1008mpRinvReloadInventory,
       "pmc1008mpRinvHwPlatform": pmc1008mpRinvHwPlatform,
       "pmc1008mpRinvModulePlatform": pmc1008mpRinvModulePlatform,
       "pmc1008mpRinvSwPlatform": pmc1008mpRinvSwPlatform,
       "pmc1008mpRinvGwPlatform": pmc1008mpRinvGwPlatform,
       "pmc1008mpdownload": pmc1008mpdownload,
       "pmc1008mpDwlOther": pmc1008mpDwlOther,
       "pmc1008mpDwlrestartProcess": pmc1008mpDwlrestartProcess,
       "pmc1008mpDwlWarmRestartProcessed": pmc1008mpDwlWarmRestartProcessed,
       "pmc1008mpDwlColdRestartProcessed": pmc1008mpDwlColdRestartProcessed,
       "pmc1008mpDwlswBanksUsed": pmc1008mpDwlswBanksUsed,
       "pmc1008mpDwlSwBank1Used": pmc1008mpDwlSwBank1Used,
       "pmc1008mpDwlSwBank2Used": pmc1008mpDwlSwBank2Used,
       "pmc1008mpDwlSwBank1Notempty": pmc1008mpDwlSwBank1Notempty,
       "pmc1008mpDwlSwBank2Notempty": pmc1008mpDwlSwBank2Notempty,
       "pmc1008mpDwlgwBanksUsed": pmc1008mpDwlgwBanksUsed,
       "pmc1008mpDwlGwBank1Used": pmc1008mpDwlGwBank1Used,
       "pmc1008mpDwlGwBank2Used": pmc1008mpDwlGwBank2Used,
       "pmc1008mpDwlGwBank3Used": pmc1008mpDwlGwBank3Used,
       "pmc1008mpDwlGwBank4Used": pmc1008mpDwlGwBank4Used,
       "pmc1008mpDwlGwBank1Notempty": pmc1008mpDwlGwBank1Notempty,
       "pmc1008mpDwlGwBank2Notempty": pmc1008mpDwlGwBank2Notempty,
       "pmc1008mpDwlGwBank3Notempty": pmc1008mpDwlGwBank3Notempty,
       "pmc1008mpDwlGwBank4Notempty": pmc1008mpDwlGwBank4Notempty,
       "pmc1008mpDwlClient": pmc1008mpDwlClient,
       "pmc1008mpDwlLine": pmc1008mpDwlLine,
       "pmc1008mpConfig": pmc1008mpConfig,
       "pmc1008mpCfgAccessCAisCsf": pmc1008mpCfgAccessCAisCsf,
       "pmc1008mpCfgClientcaiscsfTable": pmc1008mpCfgClientcaiscsfTable,
       "pmc1008mpCfgClientcaiscsfEntry": pmc1008mpCfgClientcaiscsfEntry,
       "pmc1008mpCfgClientcaiscsfIndex": pmc1008mpCfgClientcaiscsfIndex,
       "pmc1008mpCfgCAisModePortn": pmc1008mpCfgCAisModePortn,
       "pmc1008mpCfgUpAccessioAlmPortn": pmc1008mpCfgUpAccessioAlmPortn,
       "pmc1008mpCfgUpMapperDeAlmPortn": pmc1008mpCfgUpMapperDeAlmPortn,
       "pmc1008mpCfgDownAccessioAlmPortn": pmc1008mpCfgDownAccessioAlmPortn,
       "pmc1008mpCfgDownMapperDeAlmPortn": pmc1008mpCfgDownMapperDeAlmPortn,
       "pmc1008mpCfgDownDfrmAlmPortn": pmc1008mpCfgDownDfrmAlmPortn,
       "pmc1008mpCfgDownLineSyncAlarmsPortn": pmc1008mpCfgDownLineSyncAlarmsPortn,
       "pmc1008mpCfgStartup": pmc1008mpCfgStartup,
       "pmc1008mpCfgClientStartupTable": pmc1008mpCfgClientStartupTable,
       "pmc1008mpCfgClientStartupEntry": pmc1008mpCfgClientStartupEntry,
       "pmc1008mpCfgClientStartupIndex": pmc1008mpCfgClientStartupIndex,
       "pmc1008mpCfgSystConfPortPortn": pmc1008mpCfgSystConfPortPortn,
       "pmc1008mpCfgNetConfPortPortn": pmc1008mpCfgNetConfPortPortn,
       "pmc1008mpCfgAdddropConfPortPortn": pmc1008mpCfgAdddropConfPortPortn,
       "pmc1008mptablelineStartup": pmc1008mptablelineStartup,
       "pmc1008mpCfgsystConfLine1": pmc1008mpCfgsystConfLine1,
       "pmc1008mpCfglineOptions1": pmc1008mpCfglineOptions1,
       "pmc1008mpCfgsystConfLine2": pmc1008mpCfgsystConfLine2,
       "pmc1008mpCfglineSelection": pmc1008mpCfglineSelection,
       "pmc1008mpCfglineOptions2": pmc1008mpCfglineOptions2,
       "pmc1008mpCfgXfpTable": pmc1008mpCfgXfpTable,
       "pmc1008mpCfgXfpEntry": pmc1008mpCfgXfpEntry,
       "pmc1008mpCfgXfpIndex": pmc1008mpCfgXfpIndex,
       "pmc1008mpCfgSystConfXfpPortn": pmc1008mpCfgSystConfXfpPortn,
       "pmc1008mpCfgDataRateConfXfpPortn": pmc1008mpCfgDataRateConfXfpPortn,
       "pmc1008mpCfgOtxtlhTable": pmc1008mpCfgOtxtlhTable,
       "pmc1008mpCfgOtxtlhEntry": pmc1008mpCfgOtxtlhEntry,
       "pmc1008mpCfgOtxtlhIndex": pmc1008mpCfgOtxtlhIndex,
       "pmc1008mpCfgLineOtxMiscPortn": pmc1008mpCfgLineOtxMiscPortn,
       "pmc1008mpCfgLineDitherRatePortn": pmc1008mpCfgLineDitherRatePortn,
       "pmc1008mpCfgLineDitherFhzPortn": pmc1008mpCfgLineDitherFhzPortn,
       "pmc1008mpCfgLinePwrLaserPortn": pmc1008mpCfgLinePwrLaserPortn,
       "pmc1008mpCfgLineFCurrentPortn": pmc1008mpCfgLineFCurrentPortn,
       "pmc1008mpCfgLineGridCurrentPortn": pmc1008mpCfgLineGridCurrentPortn,
       "pmc1008mpCfgFPortn": pmc1008mpCfgFPortn,
       "pmc1008mpCfgReservedPortn": pmc1008mpCfgReservedPortn,
       "pmc1008mpCfgLinePhotodiodeModePortn": pmc1008mpCfgLinePhotodiodeModePortn,
       "pmc1008mpCfgLinePhotodiodeValuePortn": pmc1008mpCfgLinePhotodiodeValuePortn,
       "pmc1008mpCfgOther": pmc1008mpCfgOther,
       "pmc1008mptablemoduleOther": pmc1008mptablemoduleOther,
       "pmc1008mpCfgmode": pmc1008mpCfgmode,
       "pmc1008mpCfgLabels": pmc1008mpCfgLabels,
       "pmc1008mpCfgLabelclientTable": pmc1008mpCfgLabelclientTable,
       "pmc1008mpCfgLabelclientEntry": pmc1008mpCfgLabelclientEntry,
       "pmc1008mpCfgLabelclientIndex": pmc1008mpCfgLabelclientIndex,
       "pmc1008mpCfgLabelclientPortn": pmc1008mpCfgLabelclientPortn,
       "pmc1008mpCfgLabellineTable": pmc1008mpCfgLabellineTable,
       "pmc1008mpCfgLabellineEntry": pmc1008mpCfgLabellineEntry,
       "pmc1008mpCfgLabellineIndex": pmc1008mpCfgLabellineIndex,
       "pmc1008mpCfgLabellinePortn": pmc1008mpCfgLabellinePortn,
       "pmc1008mpCfgStartuptimeslotsline1": pmc1008mpCfgStartuptimeslotsline1,
       "pmc1008mpCfgTimeslotsportsline1Table": pmc1008mpCfgTimeslotsportsline1Table,
       "pmc1008mpCfgTimeslotsportsline1Entry": pmc1008mpCfgTimeslotsportsline1Entry,
       "pmc1008mpCfgTimeslotsportsline1Index": pmc1008mpCfgTimeslotsportsline1Index,
       "pmc1008mpCfgLine1Timeslotb2PortPortn": pmc1008mpCfgLine1Timeslotb2PortPortn,
       "pmc1008mpCfgLine1Timeslotb1PortPortn": pmc1008mpCfgLine1Timeslotb1PortPortn,
       "pmc1008mpCfgLine1ProtocolPortPortn": pmc1008mpCfgLine1ProtocolPortPortn,
       "pmc1008mpCfgStartuptimeslotsline2": pmc1008mpCfgStartuptimeslotsline2,
       "pmc1008mpCfgTimeslotsportsline2Table": pmc1008mpCfgTimeslotsportsline2Table,
       "pmc1008mpCfgTimeslotsportsline2Entry": pmc1008mpCfgTimeslotsportsline2Entry,
       "pmc1008mpCfgTimeslotsportsline2Index": pmc1008mpCfgTimeslotsportsline2Index,
       "pmc1008mpCfgLine2Timeslotb2PortPortn": pmc1008mpCfgLine2Timeslotb2PortPortn,
       "pmc1008mpCfgLine2Timeslotb1PortPortn": pmc1008mpCfgLine2Timeslotb1PortPortn,
       "pmc1008mpCfgLine2ProtocolPortPortn": pmc1008mpCfgLine2ProtocolPortPortn,
       "pmc1008mpCfgStartuptimeslotspassthroughline1": pmc1008mpCfgStartuptimeslotspassthroughline1,
       "pmc1008mpCfgTimeslotspassthroughline1Table": pmc1008mpCfgTimeslotspassthroughline1Table,
       "pmc1008mpCfgTimeslotspassthroughline1Entry": pmc1008mpCfgTimeslotspassthroughline1Entry,
       "pmc1008mpCfgTimeslotspassthroughline1Index": pmc1008mpCfgTimeslotspassthroughline1Index,
       "pmc1008mpCfgLine1Timeslotb2PassthroughPortn": pmc1008mpCfgLine1Timeslotb2PassthroughPortn,
       "pmc1008mpCfgLine1Timeslotb1PassthroughPortn": pmc1008mpCfgLine1Timeslotb1PassthroughPortn,
       "pmc1008mpCfgLine1ProtocolPassthroughPortn": pmc1008mpCfgLine1ProtocolPassthroughPortn,
       "pmc1008mpCfgStartuptimeslotspassthroughline2": pmc1008mpCfgStartuptimeslotspassthroughline2,
       "pmc1008mpCfgTimeslotspassthroughline2Table": pmc1008mpCfgTimeslotspassthroughline2Table,
       "pmc1008mpCfgTimeslotspassthroughline2Entry": pmc1008mpCfgTimeslotspassthroughline2Entry,
       "pmc1008mpCfgTimeslotspassthroughline2Index": pmc1008mpCfgTimeslotspassthroughline2Index,
       "pmc1008mpCfgLine2Timeslotb2PassthroughPortn": pmc1008mpCfgLine2Timeslotb2PassthroughPortn,
       "pmc1008mpCfgLine2Timeslotb1PassthroughPortn": pmc1008mpCfgLine2Timeslotb1PassthroughPortn,
       "pmc1008mpCfgLine2ProtocolPassthroughPortn": pmc1008mpCfgLine2ProtocolPassthroughPortn,
       "pmc1008mpCfgStartuptablefive": pmc1008mpCfgStartuptablefive,
       "pmc1008mpCfgOtxtlhcapabilitiesTable": pmc1008mpCfgOtxtlhcapabilitiesTable,
       "pmc1008mpCfgOtxtlhcapabilitiesEntry": pmc1008mpCfgOtxtlhcapabilitiesEntry,
       "pmc1008mpCfgOtxtlhcapabilitiesIndex": pmc1008mpCfgOtxtlhcapabilitiesIndex,
       "pmc1008mpCfgComponentTypePortn": pmc1008mpCfgComponentTypePortn,
       "pmc1008mpCfgMiscellaneousPortn": pmc1008mpCfgMiscellaneousPortn,
       "pmc1008mpCfgFirstChannelPortn": pmc1008mpCfgFirstChannelPortn,
       "pmc1008mpCfgLastChannelPortn": pmc1008mpCfgLastChannelPortn,
       "pmc1008mpCfgGridPortn": pmc1008mpCfgGridPortn,
       "pmc1008mpCfgWriteConfiguration": pmc1008mpCfgWriteConfiguration,
       "pmc1008mptraps": pmc1008mptraps,
       "pmc1008mptrapPortNumber": pmc1008mptrapPortNumber,
       "pmc1008mptrapLineNumber": pmc1008mptrapLineNumber,
       "pmc1008mptrapBoardNumber": pmc1008mptrapBoardNumber,
       "pmc1008mpLineTrapNotUrgentGoesOn": pmc1008mpLineTrapNotUrgentGoesOn,
       "pmc1008mpLineTrapNotUrgentGoesOff": pmc1008mpLineTrapNotUrgentGoesOff,
       "pmc1008mpLineTrapUrgentGoesOn": pmc1008mpLineTrapUrgentGoesOn,
       "pmc1008mpLineTrapUrgentGoesOff": pmc1008mpLineTrapUrgentGoesOff,
       "pmc1008mpLineTrapCritGoesOn": pmc1008mpLineTrapCritGoesOn,
       "pmc1008mpLineTrapCritGoesOff": pmc1008mpLineTrapCritGoesOff,
       "pmc1008mpClientTrapNotUrgentGoesOn": pmc1008mpClientTrapNotUrgentGoesOn,
       "pmc1008mpClientTrapNotUrgentGoesOff": pmc1008mpClientTrapNotUrgentGoesOff,
       "pmc1008mpClientTrapUrgentGoesOn": pmc1008mpClientTrapUrgentGoesOn,
       "pmc1008mpClientTrapUrgentGoesOff": pmc1008mpClientTrapUrgentGoesOff,
       "pmc1008mpClientTrapCritGoesOn": pmc1008mpClientTrapCritGoesOn,
       "pmc1008mpClientTrapCritGoesOff": pmc1008mpClientTrapCritGoesOff,
       "pmc1008mpPowerTrapUrgentGoesOn": pmc1008mpPowerTrapUrgentGoesOn,
       "pmc1008mpPowerTrapUrgentGoesOff": pmc1008mpPowerTrapUrgentGoesOff,
       "pmc1008mpMonitoring": pmc1008mpMonitoring,
       "pmc1008mpMonOther": pmc1008mpMonOther,
       "pmc1008mpMonSync": pmc1008mpMonSync,
       "pmc1008mpPerfEnable": pmc1008mpPerfEnable,
       "pmc1008mpPerf15minSync": pmc1008mpPerf15minSync,
       "pmc1008mpPerf24hSync": pmc1008mpPerf24hSync,
       "pmc1008mpMonTimeStamp": pmc1008mpMonTimeStamp,
       "pmc1008mpPerf15MinShort": pmc1008mpPerf15MinShort,
       "pmc1008mpPerf15MinLong": pmc1008mpPerf15MinLong,
       "pmc1008mpPerf24HoursShort": pmc1008mpPerf24HoursShort,
       "pmc1008mpPerf24HoursLong": pmc1008mpPerf24HoursLong,
       "pmc1008mpPerfCurrent15MinElapsedTime": pmc1008mpPerfCurrent15MinElapsedTime,
       "pmc1008mpPerfCurrent24HoursElapsedTime": pmc1008mpPerfCurrent24HoursElapsedTime,
       "pmc1008mpMonRmon": pmc1008mpMonRmon,
       "pmc1008mpMonCountersReset": pmc1008mpMonCountersReset,
       "pmc1008mpMonCountersStop": pmc1008mpMonCountersStop,
       "pmc1008mpMonClient": pmc1008mpMonClient,
       "pmc1008mpMonClientRmonCounter": pmc1008mpMonClientRmonCounter,
       "pmc1008mpMonupRmonByteCntTable": pmc1008mpMonupRmonByteCntTable,
       "pmc1008mpMonupRmonByteCntEntry": pmc1008mpMonupRmonByteCntEntry,
       "pmc1008mpMonupRmonByteCntIndex": pmc1008mpMonupRmonByteCntIndex,
       "pmc1008mpMonupRmonByteCntValuePortn": pmc1008mpMonupRmonByteCntValuePortn,
       "pmc1008mpMonupRmonByteCntErrorPortn": pmc1008mpMonupRmonByteCntErrorPortn,
       "pmc1008mpMonupRmonByteCntOverloadPortn": pmc1008mpMonupRmonByteCntOverloadPortn,
       "pmc1008mpMonupRmonCrcErrorCntTable": pmc1008mpMonupRmonCrcErrorCntTable,
       "pmc1008mpMonupRmonCrcErrorCntEntry": pmc1008mpMonupRmonCrcErrorCntEntry,
       "pmc1008mpMonupRmonCrcErrorCntIndex": pmc1008mpMonupRmonCrcErrorCntIndex,
       "pmc1008mpMonupRmonCrcErrorCntValuePortn": pmc1008mpMonupRmonCrcErrorCntValuePortn,
       "pmc1008mpMonupRmonCrcErrorCntErrorPortn": pmc1008mpMonupRmonCrcErrorCntErrorPortn,
       "pmc1008mpMonupRmonCrcErrorCntOverloadPortn": pmc1008mpMonupRmonCrcErrorCntOverloadPortn,
       "pmc1008mpMonupRmonPacketsCntTable": pmc1008mpMonupRmonPacketsCntTable,
       "pmc1008mpMonupRmonPacketsCntEntry": pmc1008mpMonupRmonPacketsCntEntry,
       "pmc1008mpMonupRmonPacketsCntIndex": pmc1008mpMonupRmonPacketsCntIndex,
       "pmc1008mpMonupRmonPacketsCntValuePortn": pmc1008mpMonupRmonPacketsCntValuePortn,
       "pmc1008mpMonupRmonPacketsCntErrorPortn": pmc1008mpMonupRmonPacketsCntErrorPortn,
       "pmc1008mpMonupRmonPacketsCntOverloadPortn": pmc1008mpMonupRmonPacketsCntOverloadPortn,
       "pmc1008mpMonupRmonBroadcastCntTable": pmc1008mpMonupRmonBroadcastCntTable,
       "pmc1008mpMonupRmonBroadcastCntEntry": pmc1008mpMonupRmonBroadcastCntEntry,
       "pmc1008mpMonupRmonBroadcastCntIndex": pmc1008mpMonupRmonBroadcastCntIndex,
       "pmc1008mpMonupRmonBroadcastCntValuePortn": pmc1008mpMonupRmonBroadcastCntValuePortn,
       "pmc1008mpMonupRmonBroadcastCntErrorPortn": pmc1008mpMonupRmonBroadcastCntErrorPortn,
       "pmc1008mpMonupRmonBroadcastCntOverloadPortn": pmc1008mpMonupRmonBroadcastCntOverloadPortn,
       "pmc1008mpMonupRmonMulticastCntTable": pmc1008mpMonupRmonMulticastCntTable,
       "pmc1008mpMonupRmonMulticastCntEntry": pmc1008mpMonupRmonMulticastCntEntry,
       "pmc1008mpMonupRmonMulticastCntIndex": pmc1008mpMonupRmonMulticastCntIndex,
       "pmc1008mpMonupRmonMulticastCntValuePortn": pmc1008mpMonupRmonMulticastCntValuePortn,
       "pmc1008mpMonupRmonMulticastCntErrorPortn": pmc1008mpMonupRmonMulticastCntErrorPortn,
       "pmc1008mpMonupRmonMulticastCntOverloadPortn": pmc1008mpMonupRmonMulticastCntOverloadPortn,
       "pmc1008mpPerfTelecomClientCurrent15StatTable": pmc1008mpPerfTelecomClientCurrent15StatTable,
       "pmc1008mpPerfTelecomClientCurrent15StatEntry": pmc1008mpPerfTelecomClientCurrent15StatEntry,
       "pmc1008mpPerfTelecomClientCurrent15StatIndex": pmc1008mpPerfTelecomClientCurrent15StatIndex,
       "pmc1008mpPerfTelecomClientCurrent15StatInvCvPortn": pmc1008mpPerfTelecomClientCurrent15StatInvCvPortn,
       "pmc1008mpPerfTelecomClientCurrent15StatCvValuePortn": pmc1008mpPerfTelecomClientCurrent15StatCvValuePortn,
       "pmc1008mpPerfTelecomClientCurrent15StatInvEsPortn": pmc1008mpPerfTelecomClientCurrent15StatInvEsPortn,
       "pmc1008mpPerfTelecomClientCurrent15StatEsValuePortn": pmc1008mpPerfTelecomClientCurrent15StatEsValuePortn,
       "pmc1008mpPerfTelecomClientCurrent15StatInvSesPortn": pmc1008mpPerfTelecomClientCurrent15StatInvSesPortn,
       "pmc1008mpPerfTelecomClientCurrent15StatSesValuePortn": pmc1008mpPerfTelecomClientCurrent15StatSesValuePortn,
       "pmc1008mpPerfTelecomClientCurrent15StatInvSefsPortn": pmc1008mpPerfTelecomClientCurrent15StatInvSefsPortn,
       "pmc1008mpPerfTelecomClientCurrent15StatSefsValuePortn": pmc1008mpPerfTelecomClientCurrent15StatSefsValuePortn,
       "pmc1008mpPerfTelecomClientCurrent15StatInvUasPortn": pmc1008mpPerfTelecomClientCurrent15StatInvUasPortn,
       "pmc1008mpPerfTelecomClientCurrent15StatUasValuePortn": pmc1008mpPerfTelecomClientCurrent15StatUasValuePortn,
       "pmc1008mpPerfTelecomClientPast15StatHistoryPort1Table": pmc1008mpPerfTelecomClientPast15StatHistoryPort1Table,
       "pmc1008mpPerfTelecomClientPast15StatHistoryPort1Entry": pmc1008mpPerfTelecomClientPast15StatHistoryPort1Entry,
       "pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index": pmc1008mpPerfTelecomClientPast15StatHistoryPort1Index,
       "pmc1008mpPerfTelecomClientPast15StatHistoryInvCvPort1": pmc1008mpPerfTelecomClientPast15StatHistoryInvCvPort1,
       "pmc1008mpPerfTelecomClientPast15StatHistoryCvValuePort1": pmc1008mpPerfTelecomClientPast15StatHistoryCvValuePort1,
       "pmc1008mpPerfTelecomClientPast15StatHistoryInvEsPort1": pmc1008mpPerfTelecomClientPast15StatHistoryInvEsPort1,
       "pmc1008mpPerfTelecomClientPast15StatHistoryEsValuePort1": pmc1008mpPerfTelecomClientPast15StatHistoryEsValuePort1,
       "pmc1008mpPerfTelecomClientPast15StatHistoryInvSesPort1": pmc1008mpPerfTelecomClientPast15StatHistoryInvSesPort1,
       "pmc1008mpPerfTelecomClientPast15StatHistorySesValuePort1": pmc1008mpPerfTelecomClientPast15StatHistorySesValuePort1,
       "pmc1008mpPerfTelecomClientPast15StatHistoryInvSefsPort1": pmc1008mpPerfTelecomClientPast15StatHistoryInvSefsPort1,
       "pmc1008mpPerfTelecomClientPast15StatHistorySefsValuePort1": pmc1008mpPerfTelecomClientPast15StatHistorySefsValuePort1,
       "pmc1008mpPerfTelecomClientPast15StatHistoryInvUasPort1": pmc1008mpPerfTelecomClientPast15StatHistoryInvUasPort1,
       "pmc1008mpPerfTelecomClientPast15StatHistoryUasValuePort1": pmc1008mpPerfTelecomClientPast15StatHistoryUasValuePort1,
       "pmc1008mpPerfTelecomClientCurrent24StatTable": pmc1008mpPerfTelecomClientCurrent24StatTable,
       "pmc1008mpPerfTelecomClientCurrent24StatEntry": pmc1008mpPerfTelecomClientCurrent24StatEntry,
       "pmc1008mpPerfTelecomClientCurrent24StatIndex": pmc1008mpPerfTelecomClientCurrent24StatIndex,
       "pmc1008mpPerfTelecomClientCurrent24StatInvCvPortn": pmc1008mpPerfTelecomClientCurrent24StatInvCvPortn,
       "pmc1008mpPerfTelecomClientCurrent24StatCvValuePortn": pmc1008mpPerfTelecomClientCurrent24StatCvValuePortn,
       "pmc1008mpPerfTelecomClientCurrent24StatInvEsPortn": pmc1008mpPerfTelecomClientCurrent24StatInvEsPortn,
       "pmc1008mpPerfTelecomClientCurrent24StatEsValuePortn": pmc1008mpPerfTelecomClientCurrent24StatEsValuePortn,
       "pmc1008mpPerfTelecomClientCurrent24StatInvSesPortn": pmc1008mpPerfTelecomClientCurrent24StatInvSesPortn,
       "pmc1008mpPerfTelecomClientCurrent24StatSesValuePortn": pmc1008mpPerfTelecomClientCurrent24StatSesValuePortn,
       "pmc1008mpPerfTelecomClientCurrent24StatInvSefsPortn": pmc1008mpPerfTelecomClientCurrent24StatInvSefsPortn,
       "pmc1008mpPerfTelecomClientCurrent24StatSefsValuePortn": pmc1008mpPerfTelecomClientCurrent24StatSefsValuePortn,
       "pmc1008mpPerfTelecomClientCurrent24StatInvUasPortn": pmc1008mpPerfTelecomClientCurrent24StatInvUasPortn,
       "pmc1008mpPerfTelecomClientCurrent24StatUasValuePortn": pmc1008mpPerfTelecomClientCurrent24StatUasValuePortn,
       "pmc1008mpPerfTelecomClientPast24StatHistoryPort1Table": pmc1008mpPerfTelecomClientPast24StatHistoryPort1Table,
       "pmc1008mpPerfTelecomClientPast24StatHistoryPort1Entry": pmc1008mpPerfTelecomClientPast24StatHistoryPort1Entry,
       "pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index": pmc1008mpPerfTelecomClientPast24StatHistoryPort1Index,
       "pmc1008mpPerfTelecomClientPast24StatHistoryInvCvPort1": pmc1008mpPerfTelecomClientPast24StatHistoryInvCvPort1,
       "pmc1008mpPerfTelecomClientPast24StatHistoryCvValuePort1": pmc1008mpPerfTelecomClientPast24StatHistoryCvValuePort1,
       "pmc1008mpPerfTelecomClientPast24StatHistoryInvEsPort1": pmc1008mpPerfTelecomClientPast24StatHistoryInvEsPort1,
       "pmc1008mpPerfTelecomClientPast24StatHistoryEsValuePort1": pmc1008mpPerfTelecomClientPast24StatHistoryEsValuePort1,
       "pmc1008mpPerfTelecomClientPast24StatHistoryInvSesPort1": pmc1008mpPerfTelecomClientPast24StatHistoryInvSesPort1,
       "pmc1008mpPerfTelecomClientPast24StatHistorySesValuePort1": pmc1008mpPerfTelecomClientPast24StatHistorySesValuePort1,
       "pmc1008mpPerfTelecomClientPast24StatHistoryInvSefsPort1": pmc1008mpPerfTelecomClientPast24StatHistoryInvSefsPort1,
       "pmc1008mpPerfTelecomClientPast24StatHistorySefsValuePort1": pmc1008mpPerfTelecomClientPast24StatHistorySefsValuePort1,
       "pmc1008mpPerfTelecomClientPast24StatHistoryInvUasPort1": pmc1008mpPerfTelecomClientPast24StatHistoryInvUasPort1,
       "pmc1008mpPerfTelecomClientPast24StatHistoryUasValuePort1": pmc1008mpPerfTelecomClientPast24StatHistoryUasValuePort1,
       "pmc1008mpPerfDatacomClientCurrent15StatTable": pmc1008mpPerfDatacomClientCurrent15StatTable,
       "pmc1008mpPerfDatacomClientCurrent15StatEntry": pmc1008mpPerfDatacomClientCurrent15StatEntry,
       "pmc1008mpPerfDatacomClientCurrent15StatIndex": pmc1008mpPerfDatacomClientCurrent15StatIndex,
       "pmc1008mpperfdatacomclientCurrent15StatInBytesCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatInBytesCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInBytesCountPortn": pmc1008mpperfdatacomclientCurrent15StatInBytesCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInCrcCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatInCrcCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInCrcCountPortn": pmc1008mpperfdatacomclientCurrent15StatInCrcCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountPortn": pmc1008mpperfdatacomclientCurrent15StatInBroadcastCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInMulticastCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatInMulticastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInMulticastCountPortn": pmc1008mpperfdatacomclientCurrent15StatInMulticastCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInUnicastCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatInUnicastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInUnicastCountPortn": pmc1008mpperfdatacomclientCurrent15StatInUnicastCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountPortn": pmc1008mpperfdatacomclientCurrent15StatInNonunicastCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutBytesCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatOutBytesCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutBytesCountPortn": pmc1008mpperfdatacomclientCurrent15StatOutBytesCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountPortn": pmc1008mpperfdatacomclientCurrent15StatOutBroadcastCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountPortn": pmc1008mpperfdatacomclientCurrent15StatOutMulticastCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountPortn": pmc1008mpperfdatacomclientCurrent15StatOutUnicastCountPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountInvPortn": pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountPortn": pmc1008mpperfdatacomclientCurrent15StatOutNonunicastCountPortn,
       "pmc1008mpPerfDatacomClientPast15StatHistoryPort1Table": pmc1008mpPerfDatacomClientPast15StatHistoryPort1Table,
       "pmc1008mpPerfDatacomClientPast15StatHistoryPort1Entry": pmc1008mpPerfDatacomClientPast15StatHistoryPort1Entry,
       "pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index": pmc1008mpPerfDatacomClientPast15StatHistoryPort1Index,
       "pmc1008mpperfdatacomclientPast15StatInBytesCountInvPort1": pmc1008mpperfdatacomclientPast15StatInBytesCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatInBytesCountPort1": pmc1008mpperfdatacomclientPast15StatInBytesCountPort1,
       "pmc1008mpperfdatacomclientPast15StatInCrcCountInvPort1": pmc1008mpperfdatacomclientPast15StatInCrcCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatInCrcCountPort1": pmc1008mpperfdatacomclientPast15StatInCrcCountPort1,
       "pmc1008mpperfdatacomclientPast15StatInBroadcastCountInvPort1": pmc1008mpperfdatacomclientPast15StatInBroadcastCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatInBroadcastCountPort1": pmc1008mpperfdatacomclientPast15StatInBroadcastCountPort1,
       "pmc1008mpperfdatacomclientPast15StatInMulticastCountInvPort1": pmc1008mpperfdatacomclientPast15StatInMulticastCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatInMulticastCountPort1": pmc1008mpperfdatacomclientPast15StatInMulticastCountPort1,
       "pmc1008mpperfdatacomclientPast15StatInUnicastCountInvPort1": pmc1008mpperfdatacomclientPast15StatInUnicastCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatInUnicastCountPort1": pmc1008mpperfdatacomclientPast15StatInUnicastCountPort1,
       "pmc1008mpperfdatacomclientPast15StatInNonunicastCountInvPort1": pmc1008mpperfdatacomclientPast15StatInNonunicastCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatInNonunicastCountPort1": pmc1008mpperfdatacomclientPast15StatInNonunicastCountPort1,
       "pmc1008mpperfdatacomclientPast15StatOutBytesCountInvPort1": pmc1008mpperfdatacomclientPast15StatOutBytesCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatOutBytesCountPort1": pmc1008mpperfdatacomclientPast15StatOutBytesCountPort1,
       "pmc1008mpperfdatacomclientPast15StatOutBroadcastCountInvPort1": pmc1008mpperfdatacomclientPast15StatOutBroadcastCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatOutBroadcastCountPort1": pmc1008mpperfdatacomclientPast15StatOutBroadcastCountPort1,
       "pmc1008mpperfdatacomclientPast15StatOutMulticastCountInvPort1": pmc1008mpperfdatacomclientPast15StatOutMulticastCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatOutMulticastCountPort1": pmc1008mpperfdatacomclientPast15StatOutMulticastCountPort1,
       "pmc1008mpperfdatacomclientPast15StatOutUnicastCountInvPort1": pmc1008mpperfdatacomclientPast15StatOutUnicastCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatOutUnicastCountPort1": pmc1008mpperfdatacomclientPast15StatOutUnicastCountPort1,
       "pmc1008mpperfdatacomclientPast15StatOutNonunicastCountInvPort1": pmc1008mpperfdatacomclientPast15StatOutNonunicastCountInvPort1,
       "pmc1008mpperfdatacomclientPast15StatOutNonunicastCountPort1": pmc1008mpperfdatacomclientPast15StatOutNonunicastCountPort1,
       "pmc1008mpPerfDatacomClientCurrent24StatTable": pmc1008mpPerfDatacomClientCurrent24StatTable,
       "pmc1008mpPerfDatacomClientCurrent24StatEntry": pmc1008mpPerfDatacomClientCurrent24StatEntry,
       "pmc1008mpPerfDatacomClientCurrent24StatIndex": pmc1008mpPerfDatacomClientCurrent24StatIndex,
       "pmc1008mpperfdatacomclientCurrent24StatInBytesCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatInBytesCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInBytesCountPortn": pmc1008mpperfdatacomclientCurrent24StatInBytesCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInCrcCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatInCrcCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInCrcCountPortn": pmc1008mpperfdatacomclientCurrent24StatInCrcCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountPortn": pmc1008mpperfdatacomclientCurrent24StatInBroadcastCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInMulticastCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatInMulticastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInMulticastCountPortn": pmc1008mpperfdatacomclientCurrent24StatInMulticastCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInUnicastCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatInUnicastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInUnicastCountPortn": pmc1008mpperfdatacomclientCurrent24StatInUnicastCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountPortn": pmc1008mpperfdatacomclientCurrent24StatInNonunicastCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutBytesCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatOutBytesCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutBytesCountPortn": pmc1008mpperfdatacomclientCurrent24StatOutBytesCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountPortn": pmc1008mpperfdatacomclientCurrent24StatOutBroadcastCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountPortn": pmc1008mpperfdatacomclientCurrent24StatOutMulticastCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountPortn": pmc1008mpperfdatacomclientCurrent24StatOutUnicastCountPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountInvPortn": pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountInvPortn,
       "pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountPortn": pmc1008mpperfdatacomclientCurrent24StatOutNonunicastCountPortn,
       "pmc1008mpPerfDatacomClientPast24StatHistoryPort1Table": pmc1008mpPerfDatacomClientPast24StatHistoryPort1Table,
       "pmc1008mpPerfDatacomClientPast24StatHistoryPort1Entry": pmc1008mpPerfDatacomClientPast24StatHistoryPort1Entry,
       "pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index": pmc1008mpPerfDatacomClientPast24StatHistoryPort1Index,
       "pmc1008mpperfdatacomclientPast24StatInBytesCountInvPort1": pmc1008mpperfdatacomclientPast24StatInBytesCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatInBytesCountPort1": pmc1008mpperfdatacomclientPast24StatInBytesCountPort1,
       "pmc1008mpperfdatacomclientPast24StatInCrcCountInvPort1": pmc1008mpperfdatacomclientPast24StatInCrcCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatInCrcCountPort1": pmc1008mpperfdatacomclientPast24StatInCrcCountPort1,
       "pmc1008mpperfdatacomclientPast24StatInBroadcastCountInvPort1": pmc1008mpperfdatacomclientPast24StatInBroadcastCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatInBroadcastCountPort1": pmc1008mpperfdatacomclientPast24StatInBroadcastCountPort1,
       "pmc1008mpperfdatacomclientPast24StatInMulticastCountInvPort1": pmc1008mpperfdatacomclientPast24StatInMulticastCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatInMulticastCountPort1": pmc1008mpperfdatacomclientPast24StatInMulticastCountPort1,
       "pmc1008mpperfdatacomclientPast24StatInUnicastCountInvPort1": pmc1008mpperfdatacomclientPast24StatInUnicastCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatInUnicastCountPort1": pmc1008mpperfdatacomclientPast24StatInUnicastCountPort1,
       "pmc1008mpperfdatacomclientPast24StatInNonunicastCountInvPort1": pmc1008mpperfdatacomclientPast24StatInNonunicastCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatInNonunicastCountPort1": pmc1008mpperfdatacomclientPast24StatInNonunicastCountPort1,
       "pmc1008mpperfdatacomclientPast24StatOutBytesCountInvPort1": pmc1008mpperfdatacomclientPast24StatOutBytesCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatOutBytesCountPort1": pmc1008mpperfdatacomclientPast24StatOutBytesCountPort1,
       "pmc1008mpperfdatacomclientPast24StatOutBroadcastCountInvPort1": pmc1008mpperfdatacomclientPast24StatOutBroadcastCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatOutBroadcastCountPort1": pmc1008mpperfdatacomclientPast24StatOutBroadcastCountPort1,
       "pmc1008mpperfdatacomclientPast24StatOutMulticastCountInvPort1": pmc1008mpperfdatacomclientPast24StatOutMulticastCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatOutMulticastCountPort1": pmc1008mpperfdatacomclientPast24StatOutMulticastCountPort1,
       "pmc1008mpperfdatacomclientPast24StatOutUnicastCountInvPort1": pmc1008mpperfdatacomclientPast24StatOutUnicastCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatOutUnicastCountPort1": pmc1008mpperfdatacomclientPast24StatOutUnicastCountPort1,
       "pmc1008mpperfdatacomclientPast24StatOutNonunicastCountInvPort1": pmc1008mpperfdatacomclientPast24StatOutNonunicastCountInvPort1,
       "pmc1008mpperfdatacomclientPast24StatOutNonunicastCountPort1": pmc1008mpperfdatacomclientPast24StatOutNonunicastCountPort1,
       "pmc1008mpMonLine": pmc1008mpMonLine,
       "pmc1008mpPerfTelecomLineCurrent15StatTable": pmc1008mpPerfTelecomLineCurrent15StatTable,
       "pmc1008mpPerfTelecomLineCurrent15StatEntry": pmc1008mpPerfTelecomLineCurrent15StatEntry,
       "pmc1008mpPerfTelecomLineCurrent15StatIndex": pmc1008mpPerfTelecomLineCurrent15StatIndex,
       "pmc1008mpPerfTelecomLineCurrent15StatInvCvPortn": pmc1008mpPerfTelecomLineCurrent15StatInvCvPortn,
       "pmc1008mpPerfTelecomLineCurrent15StatCvValuePortn": pmc1008mpPerfTelecomLineCurrent15StatCvValuePortn,
       "pmc1008mpPerfTelecomLineCurrent15StatInvEsPortn": pmc1008mpPerfTelecomLineCurrent15StatInvEsPortn,
       "pmc1008mpPerfTelecomLineCurrent15StatEsValuePortn": pmc1008mpPerfTelecomLineCurrent15StatEsValuePortn,
       "pmc1008mpPerfTelecomLineCurrent15StatInvSesPortn": pmc1008mpPerfTelecomLineCurrent15StatInvSesPortn,
       "pmc1008mpPerfTelecomLineCurrent15StatSesValuePortn": pmc1008mpPerfTelecomLineCurrent15StatSesValuePortn,
       "pmc1008mpPerfTelecomLineCurrent15StatInvSefsPortn": pmc1008mpPerfTelecomLineCurrent15StatInvSefsPortn,
       "pmc1008mpPerfTelecomLineCurrent15StatSefsValuePortn": pmc1008mpPerfTelecomLineCurrent15StatSefsValuePortn,
       "pmc1008mpPerfTelecomLineCurrent15StatInvUasPortn": pmc1008mpPerfTelecomLineCurrent15StatInvUasPortn,
       "pmc1008mpPerfTelecomLineCurrent15StatUasValuePortn": pmc1008mpPerfTelecomLineCurrent15StatUasValuePortn,
       "pmc1008mpPerfTelecomLinePast15StatHistoryPort1Table": pmc1008mpPerfTelecomLinePast15StatHistoryPort1Table,
       "pmc1008mpPerfTelecomLinePast15StatHistoryPort1Entry": pmc1008mpPerfTelecomLinePast15StatHistoryPort1Entry,
       "pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index": pmc1008mpPerfTelecomLinePast15StatHistoryPort1Index,
       "pmc1008mpPerfTelecomLinePast15StatHistoryInvCvPort1": pmc1008mpPerfTelecomLinePast15StatHistoryInvCvPort1,
       "pmc1008mpPerfTelecomLinePast15StatHistoryCvValuePort1": pmc1008mpPerfTelecomLinePast15StatHistoryCvValuePort1,
       "pmc1008mpPerfTelecomLinePast15StatHistoryInvEsPort1": pmc1008mpPerfTelecomLinePast15StatHistoryInvEsPort1,
       "pmc1008mpPerfTelecomLinePast15StatHistoryEsValuePort1": pmc1008mpPerfTelecomLinePast15StatHistoryEsValuePort1,
       "pmc1008mpPerfTelecomLinePast15StatHistoryInvSesPort1": pmc1008mpPerfTelecomLinePast15StatHistoryInvSesPort1,
       "pmc1008mpPerfTelecomLinePast15StatHistorySesValuePort1": pmc1008mpPerfTelecomLinePast15StatHistorySesValuePort1,
       "pmc1008mpPerfTelecomLinePast15StatHistoryInvSefsPort1": pmc1008mpPerfTelecomLinePast15StatHistoryInvSefsPort1,
       "pmc1008mpPerfTelecomLinePast15StatHistorySefsValuePort1": pmc1008mpPerfTelecomLinePast15StatHistorySefsValuePort1,
       "pmc1008mpPerfTelecomLinePast15StatHistoryInvUasPort1": pmc1008mpPerfTelecomLinePast15StatHistoryInvUasPort1,
       "pmc1008mpPerfTelecomLinePast15StatHistoryUasValuePort1": pmc1008mpPerfTelecomLinePast15StatHistoryUasValuePort1,
       "pmc1008mpPerfTelecomLineCurrent24StatTable": pmc1008mpPerfTelecomLineCurrent24StatTable,
       "pmc1008mpPerfTelecomLineCurrent24StatEntry": pmc1008mpPerfTelecomLineCurrent24StatEntry,
       "pmc1008mpPerfTelecomLineCurrent24StatIndex": pmc1008mpPerfTelecomLineCurrent24StatIndex,
       "pmc1008mpPerfTelecomLineCurrent24StatInvCvPortn": pmc1008mpPerfTelecomLineCurrent24StatInvCvPortn,
       "pmc1008mpPerfTelecomLineCurrent24StatCvValuePortn": pmc1008mpPerfTelecomLineCurrent24StatCvValuePortn,
       "pmc1008mpPerfTelecomLineCurrent24StatInvEsPortn": pmc1008mpPerfTelecomLineCurrent24StatInvEsPortn,
       "pmc1008mpPerfTelecomLineCurrent24StatEsValuePortn": pmc1008mpPerfTelecomLineCurrent24StatEsValuePortn,
       "pmc1008mpPerfTelecomLineCurrent24StatInvSesPortn": pmc1008mpPerfTelecomLineCurrent24StatInvSesPortn,
       "pmc1008mpPerfTelecomLineCurrent24StatSesValuePortn": pmc1008mpPerfTelecomLineCurrent24StatSesValuePortn,
       "pmc1008mpPerfTelecomLineCurrent24StatInvSefsPortn": pmc1008mpPerfTelecomLineCurrent24StatInvSefsPortn,
       "pmc1008mpPerfTelecomLineCurrent24StatSefsValuePortn": pmc1008mpPerfTelecomLineCurrent24StatSefsValuePortn,
       "pmc1008mpPerfTelecomLineCurrent24StatInvUasPortn": pmc1008mpPerfTelecomLineCurrent24StatInvUasPortn,
       "pmc1008mpPerfTelecomLineCurrent24StatUasValuePortn": pmc1008mpPerfTelecomLineCurrent24StatUasValuePortn,
       "pmc1008mpPerfTelecomLinePast24StatHistoryPort1Table": pmc1008mpPerfTelecomLinePast24StatHistoryPort1Table,
       "pmc1008mpPerfTelecomLinePast24StatHistoryPort1Entry": pmc1008mpPerfTelecomLinePast24StatHistoryPort1Entry,
       "pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index": pmc1008mpPerfTelecomLinePast24StatHistoryPort1Index,
       "pmc1008mpPerfTelecomLinePast24StatHistoryInvCvPort1": pmc1008mpPerfTelecomLinePast24StatHistoryInvCvPort1,
       "pmc1008mpPerfTelecomLinePast24StatHistoryCvValuePort1": pmc1008mpPerfTelecomLinePast24StatHistoryCvValuePort1,
       "pmc1008mpPerfTelecomLinePast24StatHistoryInvEsPort1": pmc1008mpPerfTelecomLinePast24StatHistoryInvEsPort1,
       "pmc1008mpPerfTelecomLinePast24StatHistoryEsValuePort1": pmc1008mpPerfTelecomLinePast24StatHistoryEsValuePort1,
       "pmc1008mpPerfTelecomLinePast24StatHistoryInvSesPort1": pmc1008mpPerfTelecomLinePast24StatHistoryInvSesPort1,
       "pmc1008mpPerfTelecomLinePast24StatHistorySesValuePort1": pmc1008mpPerfTelecomLinePast24StatHistorySesValuePort1,
       "pmc1008mpPerfTelecomLinePast24StatHistoryInvSefsPort1": pmc1008mpPerfTelecomLinePast24StatHistoryInvSefsPort1,
       "pmc1008mpPerfTelecomLinePast24StatHistorySefsValuePort1": pmc1008mpPerfTelecomLinePast24StatHistorySefsValuePort1,
       "pmc1008mpPerfTelecomLinePast24StatHistoryInvUasPort1": pmc1008mpPerfTelecomLinePast24StatHistoryInvUasPort1,
       "pmc1008mpPerfTelecomLinePast24StatHistoryUasValuePort1": pmc1008mpPerfTelecomLinePast24StatHistoryUasValuePort1}
)
