# SNMP MIB module (EKINOPS-Pm1008DCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1008DCP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:47 2025
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

modulePm1008dcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27)
)
if mibBuilder.loadTexts:
    modulePm1008dcp.setRevisions(
        ("2008-03-11 00:00",
         "2008-04-08 00:00",
         "2008-05-22 00:00",
         "2008-05-30 00:00",
         "2008-12-03 00:00",
         "2008-12-04 00:00",
         "2009-06-24 00:00",
         "2010-02-09 00:00",
         "2010-02-17 00:00",
         "2010-03-18 00:00",
         "2010-11-10 00:00",
         "2012-07-02 00:00",
         "2013-04-02 00:00",
         "2014-03-25 00:00",
         "2015-01-14 00:00",
         "2015-01-14 00:00",
         "2016-05-19 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1008dcpModeTimeSlot(TextualConvention, Integer32):
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



class Pm1008dcpModeAddDropA(TextualConvention, Integer32):
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



class Pm1008dcpModeAddDrop(TextualConvention, Integer32):
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



class Pm1008dcpProtectionTimeSlot(TextualConvention, Integer32):
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



class Pm1008dcpProtectionStartUp(TextualConvention, Integer32):
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



class Pm1008dcpDccMode(TextualConvention, Integer32):
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



class Pm1008dcpOtxMode(TextualConvention, Integer32):
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



class Pm1008dcpOtxGrid(TextualConvention, Integer32):
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



class Pm1008dcpAdjustValue(TextualConvention, Integer32):
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



class Pm1008dcpOtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm1008dcpalarms_ObjectIdentity = ObjectIdentity
pm1008dcpalarms = _Pm1008dcpalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2)
)
_Pm1008dcpAlmOther_ObjectIdentity = ObjectIdentity
pm1008dcpAlmOther = _Pm1008dcpAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1)
)
_Pm1008dcpAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1008dcpAlmOtherNurg = _Pm1008dcpAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 1)
)
_Pm1008dcpAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm1008dcpAlmsynthAlm2 = _Pm1008dcpAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 1, 2)
)
_Pm1008dcpAlmConfTableSave_Type = EkiOnOff
_Pm1008dcpAlmConfTableSave_Object = MibScalar
pm1008dcpAlmConfTableSave = _Pm1008dcpAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 1, 2, 1),
    _Pm1008dcpAlmConfTableSave_Type()
)
pm1008dcpAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmConfTableSave.setStatus("current")
_Pm1008dcpAlmInvUpload_Type = EkiOnOff
_Pm1008dcpAlmInvUpload_Object = MibScalar
pm1008dcpAlmInvUpload = _Pm1008dcpAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 1, 2, 2),
    _Pm1008dcpAlmInvUpload_Type()
)
pm1008dcpAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmInvUpload.setStatus("current")
_Pm1008dcpAlmConfTableLoad_Type = EkiOnOff
_Pm1008dcpAlmConfTableLoad_Object = MibScalar
pm1008dcpAlmConfTableLoad = _Pm1008dcpAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 1, 2, 3),
    _Pm1008dcpAlmConfTableLoad_Type()
)
pm1008dcpAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmConfTableLoad.setStatus("current")
_Pm1008dcpAlmCorrelatOff_Type = EkiOnOff
_Pm1008dcpAlmCorrelatOff_Object = MibScalar
pm1008dcpAlmCorrelatOff = _Pm1008dcpAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 1, 2, 4),
    _Pm1008dcpAlmCorrelatOff_Type()
)
pm1008dcpAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmCorrelatOff.setStatus("current")
_Pm1008dcpAlmMaintenanceOn_Type = EkiOnOff
_Pm1008dcpAlmMaintenanceOn_Object = MibScalar
pm1008dcpAlmMaintenanceOn = _Pm1008dcpAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 1, 2, 5),
    _Pm1008dcpAlmMaintenanceOn_Type()
)
pm1008dcpAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmMaintenanceOn.setStatus("current")
_Pm1008dcpAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1008dcpAlmOtherUrg = _Pm1008dcpAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2)
)
_Pm1008dcpAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm1008dcpAlmmodInitFailLevel2 = _Pm1008dcpAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 194)
)
_Pm1008dcpAlmLedFail_Type = EkiOnOff
_Pm1008dcpAlmLedFail_Object = MibScalar
pm1008dcpAlmLedFail = _Pm1008dcpAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 194, 1),
    _Pm1008dcpAlmLedFail_Type()
)
pm1008dcpAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLedFail.setStatus("current")
_Pm1008dcpAlmNextColdBootForced_Type = EkiOnOff
_Pm1008dcpAlmNextColdBootForced_Object = MibScalar
pm1008dcpAlmNextColdBootForced = _Pm1008dcpAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 194, 2),
    _Pm1008dcpAlmNextColdBootForced_Type()
)
pm1008dcpAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmNextColdBootForced.setStatus("current")
_Pm1008dcpAlmBootUndone_Type = EkiOnOff
_Pm1008dcpAlmBootUndone_Object = MibScalar
pm1008dcpAlmBootUndone = _Pm1008dcpAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 194, 3),
    _Pm1008dcpAlmBootUndone_Type()
)
pm1008dcpAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmBootUndone.setStatus("current")
_Pm1008dcpAlmResetHwInitFail_Type = EkiOnOff
_Pm1008dcpAlmResetHwInitFail_Object = MibScalar
pm1008dcpAlmResetHwInitFail = _Pm1008dcpAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 194, 4),
    _Pm1008dcpAlmResetHwInitFail_Type()
)
pm1008dcpAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmResetHwInitFail.setStatus("current")
_Pm1008dcpAlmSwInitFail_Type = EkiOnOff
_Pm1008dcpAlmSwInitFail_Object = MibScalar
pm1008dcpAlmSwInitFail = _Pm1008dcpAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 194, 5),
    _Pm1008dcpAlmSwInitFail_Type()
)
pm1008dcpAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmSwInitFail.setStatus("current")
_Pm1008dcpAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm1008dcpAlmmodInitFailLevel3 = _Pm1008dcpAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195)
)
_Pm1008dcpAlmGwIdentFail_Type = EkiOnOff
_Pm1008dcpAlmGwIdentFail_Object = MibScalar
pm1008dcpAlmGwIdentFail = _Pm1008dcpAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 1),
    _Pm1008dcpAlmGwIdentFail_Type()
)
pm1008dcpAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmGwIdentFail.setStatus("current")
_Pm1008dcpAlmObmTypeReadFail_Type = EkiOnOff
_Pm1008dcpAlmObmTypeReadFail_Object = MibScalar
pm1008dcpAlmObmTypeReadFail = _Pm1008dcpAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 2),
    _Pm1008dcpAlmObmTypeReadFail_Type()
)
pm1008dcpAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmObmTypeReadFail.setStatus("current")
_Pm1008dcpAlmInitModuleFail_Type = EkiOnOff
_Pm1008dcpAlmInitModuleFail_Object = MibScalar
pm1008dcpAlmInitModuleFail = _Pm1008dcpAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 3),
    _Pm1008dcpAlmInitModuleFail_Type()
)
pm1008dcpAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmInitModuleFail.setStatus("current")
_Pm1008dcpAlmXfp1InitFail_Type = EkiOnOff
_Pm1008dcpAlmXfp1InitFail_Object = MibScalar
pm1008dcpAlmXfp1InitFail = _Pm1008dcpAlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 5),
    _Pm1008dcpAlmXfp1InitFail_Type()
)
pm1008dcpAlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmXfp1InitFail.setStatus("current")
_Pm1008dcpAlmXfp2InitFail_Type = EkiOnOff
_Pm1008dcpAlmXfp2InitFail_Object = MibScalar
pm1008dcpAlmXfp2InitFail = _Pm1008dcpAlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 6),
    _Pm1008dcpAlmXfp2InitFail_Type()
)
pm1008dcpAlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmXfp2InitFail.setStatus("current")
_Pm1008dcpAlmLine1InitFail_Type = EkiOnOff
_Pm1008dcpAlmLine1InitFail_Object = MibScalar
pm1008dcpAlmLine1InitFail = _Pm1008dcpAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 7),
    _Pm1008dcpAlmLine1InitFail_Type()
)
pm1008dcpAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLine1InitFail.setStatus("current")
_Pm1008dcpAlmLine2InitFail_Type = EkiOnOff
_Pm1008dcpAlmLine2InitFail_Object = MibScalar
pm1008dcpAlmLine2InitFail = _Pm1008dcpAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 8),
    _Pm1008dcpAlmLine2InitFail_Type()
)
pm1008dcpAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLine2InitFail.setStatus("current")
_Pm1008dcpAlmClient1InitFail_Type = EkiOnOff
_Pm1008dcpAlmClient1InitFail_Object = MibScalar
pm1008dcpAlmClient1InitFail = _Pm1008dcpAlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 9),
    _Pm1008dcpAlmClient1InitFail_Type()
)
pm1008dcpAlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClient1InitFail.setStatus("current")
_Pm1008dcpAlmClient2InitFail_Type = EkiOnOff
_Pm1008dcpAlmClient2InitFail_Object = MibScalar
pm1008dcpAlmClient2InitFail = _Pm1008dcpAlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 10),
    _Pm1008dcpAlmClient2InitFail_Type()
)
pm1008dcpAlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClient2InitFail.setStatus("current")
_Pm1008dcpAlmClient3InitFail_Type = EkiOnOff
_Pm1008dcpAlmClient3InitFail_Object = MibScalar
pm1008dcpAlmClient3InitFail = _Pm1008dcpAlmClient3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 11),
    _Pm1008dcpAlmClient3InitFail_Type()
)
pm1008dcpAlmClient3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClient3InitFail.setStatus("current")
_Pm1008dcpAlmClient4InitFail_Type = EkiOnOff
_Pm1008dcpAlmClient4InitFail_Object = MibScalar
pm1008dcpAlmClient4InitFail = _Pm1008dcpAlmClient4InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 12),
    _Pm1008dcpAlmClient4InitFail_Type()
)
pm1008dcpAlmClient4InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClient4InitFail.setStatus("current")
_Pm1008dcpAlmClient5InitFail_Type = EkiOnOff
_Pm1008dcpAlmClient5InitFail_Object = MibScalar
pm1008dcpAlmClient5InitFail = _Pm1008dcpAlmClient5InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 13),
    _Pm1008dcpAlmClient5InitFail_Type()
)
pm1008dcpAlmClient5InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClient5InitFail.setStatus("current")
_Pm1008dcpAlmClient6InitFail_Type = EkiOnOff
_Pm1008dcpAlmClient6InitFail_Object = MibScalar
pm1008dcpAlmClient6InitFail = _Pm1008dcpAlmClient6InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 14),
    _Pm1008dcpAlmClient6InitFail_Type()
)
pm1008dcpAlmClient6InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClient6InitFail.setStatus("current")
_Pm1008dcpAlmClient7InitFail_Type = EkiOnOff
_Pm1008dcpAlmClient7InitFail_Object = MibScalar
pm1008dcpAlmClient7InitFail = _Pm1008dcpAlmClient7InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 15),
    _Pm1008dcpAlmClient7InitFail_Type()
)
pm1008dcpAlmClient7InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClient7InitFail.setStatus("current")
_Pm1008dcpAlmClient8InitFail_Type = EkiOnOff
_Pm1008dcpAlmClient8InitFail_Object = MibScalar
pm1008dcpAlmClient8InitFail = _Pm1008dcpAlmClient8InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 195, 16),
    _Pm1008dcpAlmClient8InitFail_Type()
)
pm1008dcpAlmClient8InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClient8InitFail.setStatus("current")
_Pm1008dcpAlmadddropTsClientRxProt_ObjectIdentity = ObjectIdentity
pm1008dcpAlmadddropTsClientRxProt = _Pm1008dcpAlmadddropTsClientRxProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198)
)
_Pm1008dcpAlmAdddropClient1West_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient1West_Object = MibScalar
pm1008dcpAlmAdddropClient1West = _Pm1008dcpAlmAdddropClient1West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 1),
    _Pm1008dcpAlmAdddropClient1West_Type()
)
pm1008dcpAlmAdddropClient1West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient1West.setStatus("current")
_Pm1008dcpAlmAdddropClient2West_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient2West_Object = MibScalar
pm1008dcpAlmAdddropClient2West = _Pm1008dcpAlmAdddropClient2West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 2),
    _Pm1008dcpAlmAdddropClient2West_Type()
)
pm1008dcpAlmAdddropClient2West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient2West.setStatus("current")
_Pm1008dcpAlmAdddropClient3West_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient3West_Object = MibScalar
pm1008dcpAlmAdddropClient3West = _Pm1008dcpAlmAdddropClient3West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 3),
    _Pm1008dcpAlmAdddropClient3West_Type()
)
pm1008dcpAlmAdddropClient3West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient3West.setStatus("current")
_Pm1008dcpAlmAdddropClient4West_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient4West_Object = MibScalar
pm1008dcpAlmAdddropClient4West = _Pm1008dcpAlmAdddropClient4West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 4),
    _Pm1008dcpAlmAdddropClient4West_Type()
)
pm1008dcpAlmAdddropClient4West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient4West.setStatus("current")
_Pm1008dcpAlmAdddropClient5West_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient5West_Object = MibScalar
pm1008dcpAlmAdddropClient5West = _Pm1008dcpAlmAdddropClient5West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 5),
    _Pm1008dcpAlmAdddropClient5West_Type()
)
pm1008dcpAlmAdddropClient5West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient5West.setStatus("current")
_Pm1008dcpAlmAdddropClient6West_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient6West_Object = MibScalar
pm1008dcpAlmAdddropClient6West = _Pm1008dcpAlmAdddropClient6West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 6),
    _Pm1008dcpAlmAdddropClient6West_Type()
)
pm1008dcpAlmAdddropClient6West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient6West.setStatus("current")
_Pm1008dcpAlmAdddropClient7West_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient7West_Object = MibScalar
pm1008dcpAlmAdddropClient7West = _Pm1008dcpAlmAdddropClient7West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 7),
    _Pm1008dcpAlmAdddropClient7West_Type()
)
pm1008dcpAlmAdddropClient7West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient7West.setStatus("current")
_Pm1008dcpAlmAdddropClient8West_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient8West_Object = MibScalar
pm1008dcpAlmAdddropClient8West = _Pm1008dcpAlmAdddropClient8West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 8),
    _Pm1008dcpAlmAdddropClient8West_Type()
)
pm1008dcpAlmAdddropClient8West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient8West.setStatus("current")
_Pm1008dcpAlmAdddropClient1East_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient1East_Object = MibScalar
pm1008dcpAlmAdddropClient1East = _Pm1008dcpAlmAdddropClient1East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 9),
    _Pm1008dcpAlmAdddropClient1East_Type()
)
pm1008dcpAlmAdddropClient1East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient1East.setStatus("current")
_Pm1008dcpAlmAdddropClient2East_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient2East_Object = MibScalar
pm1008dcpAlmAdddropClient2East = _Pm1008dcpAlmAdddropClient2East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 10),
    _Pm1008dcpAlmAdddropClient2East_Type()
)
pm1008dcpAlmAdddropClient2East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient2East.setStatus("current")
_Pm1008dcpAlmAdddropClient3East_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient3East_Object = MibScalar
pm1008dcpAlmAdddropClient3East = _Pm1008dcpAlmAdddropClient3East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 11),
    _Pm1008dcpAlmAdddropClient3East_Type()
)
pm1008dcpAlmAdddropClient3East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient3East.setStatus("current")
_Pm1008dcpAlmAdddropClient4East_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient4East_Object = MibScalar
pm1008dcpAlmAdddropClient4East = _Pm1008dcpAlmAdddropClient4East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 12),
    _Pm1008dcpAlmAdddropClient4East_Type()
)
pm1008dcpAlmAdddropClient4East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient4East.setStatus("current")
_Pm1008dcpAlmAdddropClient5East_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient5East_Object = MibScalar
pm1008dcpAlmAdddropClient5East = _Pm1008dcpAlmAdddropClient5East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 13),
    _Pm1008dcpAlmAdddropClient5East_Type()
)
pm1008dcpAlmAdddropClient5East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient5East.setStatus("current")
_Pm1008dcpAlmAdddropClient6East_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient6East_Object = MibScalar
pm1008dcpAlmAdddropClient6East = _Pm1008dcpAlmAdddropClient6East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 14),
    _Pm1008dcpAlmAdddropClient6East_Type()
)
pm1008dcpAlmAdddropClient6East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient6East.setStatus("current")
_Pm1008dcpAlmAdddropClient7East_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient7East_Object = MibScalar
pm1008dcpAlmAdddropClient7East = _Pm1008dcpAlmAdddropClient7East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 15),
    _Pm1008dcpAlmAdddropClient7East_Type()
)
pm1008dcpAlmAdddropClient7East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient7East.setStatus("current")
_Pm1008dcpAlmAdddropClient8East_Type = EkiOnOff
_Pm1008dcpAlmAdddropClient8East_Object = MibScalar
pm1008dcpAlmAdddropClient8East = _Pm1008dcpAlmAdddropClient8East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 2, 198, 16),
    _Pm1008dcpAlmAdddropClient8East_Type()
)
pm1008dcpAlmAdddropClient8East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmAdddropClient8East.setStatus("current")
_Pm1008dcpAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1008dcpAlmOtherCrit = _Pm1008dcpAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 3)
)
_Pm1008dcpAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1008dcpAlmsynthAlm0 = _Pm1008dcpAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 3, 0)
)
_Pm1008dcpAlmModGlobFail_Type = EkiOnOff
_Pm1008dcpAlmModGlobFail_Object = MibScalar
pm1008dcpAlmModGlobFail = _Pm1008dcpAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 3, 0, 9),
    _Pm1008dcpAlmModGlobFail_Type()
)
pm1008dcpAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmModGlobFail.setStatus("current")
_Pm1008dcpAlmDefFuseA_Type = EkiOnOff
_Pm1008dcpAlmDefFuseA_Object = MibScalar
pm1008dcpAlmDefFuseA = _Pm1008dcpAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 3, 0, 15),
    _Pm1008dcpAlmDefFuseA_Type()
)
pm1008dcpAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDefFuseA.setStatus("current")
_Pm1008dcpAlmDefFuseB_Type = EkiOnOff
_Pm1008dcpAlmDefFuseB_Object = MibScalar
pm1008dcpAlmDefFuseB = _Pm1008dcpAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 1, 3, 0, 16),
    _Pm1008dcpAlmDefFuseB_Type()
)
pm1008dcpAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDefFuseB.setStatus("current")
_Pm1008dcpAlmClient_ObjectIdentity = ObjectIdentity
pm1008dcpAlmClient = _Pm1008dcpAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2)
)
_Pm1008dcpAlmClientNurg_ObjectIdentity = ObjectIdentity
pm1008dcpAlmClientNurg = _Pm1008dcpAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1)
)
_Pm1008dcpAlmsfpWarnDdmTable_Object = MibTable
pm1008dcpAlmsfpWarnDdmTable = _Pm1008dcpAlmsfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmsfpWarnDdmTable.setStatus("current")
_Pm1008dcpAlmsfpWarnDdmEntry_Object = MibTableRow
pm1008dcpAlmsfpWarnDdmEntry = _Pm1008dcpAlmsfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1)
)
pm1008dcpAlmsfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmsfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmsfpWarnDdmEntry.setStatus("current")


class _Pm1008dcpAlmsfpWarnDdmIndex_Type(Integer32):
    """Custom type pm1008dcpAlmsfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmsfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmsfpWarnDdmIndex_Object = MibTableColumn
pm1008dcpAlmsfpWarnDdmIndex = _Pm1008dcpAlmsfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 1),
    _Pm1008dcpAlmsfpWarnDdmIndex_Type()
)
pm1008dcpAlmsfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmsfpWarnDdmIndex.setStatus("current")
_Pm1008dcpAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm1008dcpAlmTxPwLowWngPortn_Object = MibTableColumn
pm1008dcpAlmTxPwLowWngPortn = _Pm1008dcpAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 2),
    _Pm1008dcpAlmTxPwLowWngPortn_Type()
)
pm1008dcpAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxPwLowWngPortn.setStatus("current")
_Pm1008dcpAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm1008dcpAlmTxPwrHighWngPortn_Object = MibTableColumn
pm1008dcpAlmTxPwrHighWngPortn = _Pm1008dcpAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 3),
    _Pm1008dcpAlmTxPwrHighWngPortn_Type()
)
pm1008dcpAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxPwrHighWngPortn.setStatus("current")
_Pm1008dcpAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm1008dcpAlmTxBiasLowWngPortn_Object = MibTableColumn
pm1008dcpAlmTxBiasLowWngPortn = _Pm1008dcpAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 4),
    _Pm1008dcpAlmTxBiasLowWngPortn_Type()
)
pm1008dcpAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxBiasLowWngPortn.setStatus("current")
_Pm1008dcpAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm1008dcpAlmTxBiasHighWngPortn_Object = MibTableColumn
pm1008dcpAlmTxBiasHighWngPortn = _Pm1008dcpAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 5),
    _Pm1008dcpAlmTxBiasHighWngPortn_Type()
)
pm1008dcpAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxBiasHighWngPortn.setStatus("current")
_Pm1008dcpAlmVccLowWngPortn_Type = EkiOnOff
_Pm1008dcpAlmVccLowWngPortn_Object = MibTableColumn
pm1008dcpAlmVccLowWngPortn = _Pm1008dcpAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 6),
    _Pm1008dcpAlmVccLowWngPortn_Type()
)
pm1008dcpAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVccLowWngPortn.setStatus("current")
_Pm1008dcpAlmVccHighWngPortn_Type = EkiOnOff
_Pm1008dcpAlmVccHighWngPortn_Object = MibTableColumn
pm1008dcpAlmVccHighWngPortn = _Pm1008dcpAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 7),
    _Pm1008dcpAlmVccHighWngPortn_Type()
)
pm1008dcpAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVccHighWngPortn.setStatus("current")
_Pm1008dcpAlmTempLowWngPortn_Type = EkiOnOff
_Pm1008dcpAlmTempLowWngPortn_Object = MibTableColumn
pm1008dcpAlmTempLowWngPortn = _Pm1008dcpAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 8),
    _Pm1008dcpAlmTempLowWngPortn_Type()
)
pm1008dcpAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTempLowWngPortn.setStatus("current")
_Pm1008dcpAlmTempHighWngPortn_Type = EkiOnOff
_Pm1008dcpAlmTempHighWngPortn_Object = MibTableColumn
pm1008dcpAlmTempHighWngPortn = _Pm1008dcpAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 9),
    _Pm1008dcpAlmTempHighWngPortn_Type()
)
pm1008dcpAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTempHighWngPortn.setStatus("current")
_Pm1008dcpAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm1008dcpAlmRxPwrLowWngPortn_Object = MibTableColumn
pm1008dcpAlmRxPwrLowWngPortn = _Pm1008dcpAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 16),
    _Pm1008dcpAlmRxPwrLowWngPortn_Type()
)
pm1008dcpAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxPwrLowWngPortn.setStatus("current")
_Pm1008dcpAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm1008dcpAlmRxPwrHighWngPortn_Object = MibTableColumn
pm1008dcpAlmRxPwrHighWngPortn = _Pm1008dcpAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 1, 48, 1, 17),
    _Pm1008dcpAlmRxPwrHighWngPortn_Type()
)
pm1008dcpAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxPwrHighWngPortn.setStatus("current")
_Pm1008dcpAlmClientUrg_ObjectIdentity = ObjectIdentity
pm1008dcpAlmClientUrg = _Pm1008dcpAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2)
)
_Pm1008dcpAlmsfpAlmDdmTable_Object = MibTable
pm1008dcpAlmsfpAlmDdmTable = _Pm1008dcpAlmsfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmsfpAlmDdmTable.setStatus("current")
_Pm1008dcpAlmsfpAlmDdmEntry_Object = MibTableRow
pm1008dcpAlmsfpAlmDdmEntry = _Pm1008dcpAlmsfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1)
)
pm1008dcpAlmsfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmsfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmsfpAlmDdmEntry.setStatus("current")


class _Pm1008dcpAlmsfpAlmDdmIndex_Type(Integer32):
    """Custom type pm1008dcpAlmsfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmsfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmsfpAlmDdmIndex_Object = MibTableColumn
pm1008dcpAlmsfpAlmDdmIndex = _Pm1008dcpAlmsfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 1),
    _Pm1008dcpAlmsfpAlmDdmIndex_Type()
)
pm1008dcpAlmsfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmsfpAlmDdmIndex.setStatus("current")
_Pm1008dcpAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm1008dcpAlmTxPwrLowAlaPortn = _Pm1008dcpAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 2),
    _Pm1008dcpAlmTxPwrLowAlaPortn_Type()
)
pm1008dcpAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxPwrLowAlaPortn.setStatus("current")
_Pm1008dcpAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm1008dcpAlmTxPwrHighAlaPortn = _Pm1008dcpAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 3),
    _Pm1008dcpAlmTxPwrHighAlaPortn_Type()
)
pm1008dcpAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxPwrHighAlaPortn.setStatus("current")
_Pm1008dcpAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm1008dcpAlmTxBiasLowAlaPortn = _Pm1008dcpAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 4),
    _Pm1008dcpAlmTxBiasLowAlaPortn_Type()
)
pm1008dcpAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxBiasLowAlaPortn.setStatus("current")
_Pm1008dcpAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm1008dcpAlmTxBiasHighAlaPortn = _Pm1008dcpAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 5),
    _Pm1008dcpAlmTxBiasHighAlaPortn_Type()
)
pm1008dcpAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxBiasHighAlaPortn.setStatus("current")
_Pm1008dcpAlmVccLowAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmVccLowAlaPortn_Object = MibTableColumn
pm1008dcpAlmVccLowAlaPortn = _Pm1008dcpAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 6),
    _Pm1008dcpAlmVccLowAlaPortn_Type()
)
pm1008dcpAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVccLowAlaPortn.setStatus("current")
_Pm1008dcpAlmVccHighAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmVccHighAlaPortn_Object = MibTableColumn
pm1008dcpAlmVccHighAlaPortn = _Pm1008dcpAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 7),
    _Pm1008dcpAlmVccHighAlaPortn_Type()
)
pm1008dcpAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVccHighAlaPortn.setStatus("current")
_Pm1008dcpAlmTempLowAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmTempLowAlaPortn_Object = MibTableColumn
pm1008dcpAlmTempLowAlaPortn = _Pm1008dcpAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 8),
    _Pm1008dcpAlmTempLowAlaPortn_Type()
)
pm1008dcpAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTempLowAlaPortn.setStatus("current")
_Pm1008dcpAlmTempHighAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmTempHighAlaPortn_Object = MibTableColumn
pm1008dcpAlmTempHighAlaPortn = _Pm1008dcpAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 9),
    _Pm1008dcpAlmTempHighAlaPortn_Type()
)
pm1008dcpAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTempHighAlaPortn.setStatus("current")
_Pm1008dcpAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm1008dcpAlmRxPwrLowAlaPortn = _Pm1008dcpAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 16),
    _Pm1008dcpAlmRxPwrLowAlaPortn_Type()
)
pm1008dcpAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxPwrLowAlaPortn.setStatus("current")
_Pm1008dcpAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm1008dcpAlmRxPwrHighAlaPortn = _Pm1008dcpAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 2, 32, 1, 17),
    _Pm1008dcpAlmRxPwrHighAlaPortn_Type()
)
pm1008dcpAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxPwrHighAlaPortn.setStatus("current")
_Pm1008dcpAlmClientCrit_ObjectIdentity = ObjectIdentity
pm1008dcpAlmClientCrit = _Pm1008dcpAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3)
)
_Pm1008dcpAlmsynthAlmPortTable_Object = MibTable
pm1008dcpAlmsynthAlmPortTable = _Pm1008dcpAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmsynthAlmPortTable.setStatus("current")
_Pm1008dcpAlmsynthAlmPortEntry_Object = MibTableRow
pm1008dcpAlmsynthAlmPortEntry = _Pm1008dcpAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1)
)
pm1008dcpAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmsynthAlmPortEntry.setStatus("current")


class _Pm1008dcpAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm1008dcpAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmsynthAlmPortIndex_Object = MibTableColumn
pm1008dcpAlmsynthAlmPortIndex = _Pm1008dcpAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 1),
    _Pm1008dcpAlmsynthAlmPortIndex_Type()
)
pm1008dcpAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmsynthAlmPortIndex.setStatus("current")
_Pm1008dcpAlmSfpAbsentPortn_Type = EkiOnOff
_Pm1008dcpAlmSfpAbsentPortn_Object = MibTableColumn
pm1008dcpAlmSfpAbsentPortn = _Pm1008dcpAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 2),
    _Pm1008dcpAlmSfpAbsentPortn_Type()
)
pm1008dcpAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmSfpAbsentPortn.setStatus("current")
_Pm1008dcpAlmDdmAbsentPortn_Type = EkiOnOff
_Pm1008dcpAlmDdmAbsentPortn_Object = MibTableColumn
pm1008dcpAlmDdmAbsentPortn = _Pm1008dcpAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 3),
    _Pm1008dcpAlmDdmAbsentPortn_Type()
)
pm1008dcpAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDdmAbsentPortn.setStatus("current")
_Pm1008dcpAlmHwFailAccPortn_Type = EkiOnOff
_Pm1008dcpAlmHwFailAccPortn_Object = MibTableColumn
pm1008dcpAlmHwFailAccPortn = _Pm1008dcpAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 5),
    _Pm1008dcpAlmHwFailAccPortn_Type()
)
pm1008dcpAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmHwFailAccPortn.setStatus("current")
_Pm1008dcpAlmDwLsdPortn_Type = EkiOnOff
_Pm1008dcpAlmDwLsdPortn_Object = MibTableColumn
pm1008dcpAlmDwLsdPortn = _Pm1008dcpAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 6),
    _Pm1008dcpAlmDwLsdPortn_Type()
)
pm1008dcpAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwLsdPortn.setStatus("current")
_Pm1008dcpAlmClientLocalOosPortn_Type = EkiOnOff
_Pm1008dcpAlmClientLocalOosPortn_Object = MibTableColumn
pm1008dcpAlmClientLocalOosPortn = _Pm1008dcpAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 7),
    _Pm1008dcpAlmClientLocalOosPortn_Type()
)
pm1008dcpAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClientLocalOosPortn.setStatus("current")
_Pm1008dcpAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm1008dcpAlmClientRemoteOosPortn_Object = MibTableColumn
pm1008dcpAlmClientRemoteOosPortn = _Pm1008dcpAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 8),
    _Pm1008dcpAlmClientRemoteOosPortn_Type()
)
pm1008dcpAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClientRemoteOosPortn.setStatus("current")
_Pm1008dcpAlmDwCaisPortn_Type = EkiOnOff
_Pm1008dcpAlmDwCaisPortn_Object = MibTableColumn
pm1008dcpAlmDwCaisPortn = _Pm1008dcpAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 9),
    _Pm1008dcpAlmDwCaisPortn_Type()
)
pm1008dcpAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwCaisPortn.setStatus("current")
_Pm1008dcpAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmSfpDdmWarningPortn_Object = MibTableColumn
pm1008dcpAlmSfpDdmWarningPortn = _Pm1008dcpAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 10),
    _Pm1008dcpAlmSfpDdmWarningPortn_Type()
)
pm1008dcpAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmSfpDdmWarningPortn.setStatus("current")
_Pm1008dcpAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm1008dcpAlmSfpDdmAlmPortn_Object = MibTableColumn
pm1008dcpAlmSfpDdmAlmPortn = _Pm1008dcpAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 11),
    _Pm1008dcpAlmSfpDdmAlmPortn_Type()
)
pm1008dcpAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmSfpDdmAlmPortn.setStatus("current")
_Pm1008dcpAlmFailAccPortn_Type = EkiOnOff
_Pm1008dcpAlmFailAccPortn_Object = MibTableColumn
pm1008dcpAlmFailAccPortn = _Pm1008dcpAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 13),
    _Pm1008dcpAlmFailAccPortn_Type()
)
pm1008dcpAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmFailAccPortn.setStatus("current")
_Pm1008dcpAlmClientActivePortn_Type = EkiOnOff
_Pm1008dcpAlmClientActivePortn_Object = MibTableColumn
pm1008dcpAlmClientActivePortn = _Pm1008dcpAlmClientActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 16),
    _Pm1008dcpAlmClientActivePortn_Type()
)
pm1008dcpAlmClientActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmClientActivePortn.setStatus("current")
_Pm1008dcpAlmUpCsfPortn_Type = EkiOnOff
_Pm1008dcpAlmUpCsfPortn_Object = MibTableColumn
pm1008dcpAlmUpCsfPortn = _Pm1008dcpAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 8, 1, 17),
    _Pm1008dcpAlmUpCsfPortn_Type()
)
pm1008dcpAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmUpCsfPortn.setStatus("current")
_Pm1008dcpAlmaccessioAlmTable_Object = MibTable
pm1008dcpAlmaccessioAlmTable = _Pm1008dcpAlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmaccessioAlmTable.setStatus("current")
_Pm1008dcpAlmaccessioAlmEntry_Object = MibTableRow
pm1008dcpAlmaccessioAlmEntry = _Pm1008dcpAlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 16, 1)
)
pm1008dcpAlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmaccessioAlmEntry.setStatus("current")


class _Pm1008dcpAlmaccessioAlmIndex_Type(Integer32):
    """Custom type pm1008dcpAlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmaccessioAlmIndex_Object = MibTableColumn
pm1008dcpAlmaccessioAlmIndex = _Pm1008dcpAlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 16, 1, 1),
    _Pm1008dcpAlmaccessioAlmIndex_Type()
)
pm1008dcpAlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmaccessioAlmIndex.setStatus("current")
_Pm1008dcpAlmDwLasFailPortn_Type = EkiOnOff
_Pm1008dcpAlmDwLasFailPortn_Object = MibTableColumn
pm1008dcpAlmDwLasFailPortn = _Pm1008dcpAlmDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 16, 1, 2),
    _Pm1008dcpAlmDwLasFailPortn_Type()
)
pm1008dcpAlmDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwLasFailPortn.setStatus("current")
_Pm1008dcpAlmUpLosPortn_Type = EkiOnOff
_Pm1008dcpAlmUpLosPortn_Object = MibTableColumn
pm1008dcpAlmUpLosPortn = _Pm1008dcpAlmUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 16, 1, 5),
    _Pm1008dcpAlmUpLosPortn_Type()
)
pm1008dcpAlmUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmUpLosPortn.setStatus("current")
_Pm1008dcpAlmmapperDeAlmTable_Object = MibTable
pm1008dcpAlmmapperDeAlmTable = _Pm1008dcpAlmmapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmmapperDeAlmTable.setStatus("current")
_Pm1008dcpAlmmapperDeAlmEntry_Object = MibTableRow
pm1008dcpAlmmapperDeAlmEntry = _Pm1008dcpAlmmapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 72, 1)
)
pm1008dcpAlmmapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmmapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmmapperDeAlmEntry.setStatus("current")


class _Pm1008dcpAlmmapperDeAlmIndex_Type(Integer32):
    """Custom type pm1008dcpAlmmapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmmapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmmapperDeAlmIndex_Object = MibTableColumn
pm1008dcpAlmmapperDeAlmIndex = _Pm1008dcpAlmmapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 72, 1, 1),
    _Pm1008dcpAlmmapperDeAlmIndex_Type()
)
pm1008dcpAlmmapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmmapperDeAlmIndex.setStatus("current")
_Pm1008dcpAlmUpAccOosPortn_Type = EkiOnOff
_Pm1008dcpAlmUpAccOosPortn_Object = MibTableColumn
pm1008dcpAlmUpAccOosPortn = _Pm1008dcpAlmUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 72, 1, 2),
    _Pm1008dcpAlmUpAccOosPortn_Type()
)
pm1008dcpAlmUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmUpAccOosPortn.setStatus("current")
_Pm1008dcpAlmUpBufferOvlPortn_Type = EkiOnOff
_Pm1008dcpAlmUpBufferOvlPortn_Object = MibTableColumn
pm1008dcpAlmUpBufferOvlPortn = _Pm1008dcpAlmUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 72, 1, 11),
    _Pm1008dcpAlmUpBufferOvlPortn_Type()
)
pm1008dcpAlmUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmUpBufferOvlPortn.setStatus("current")
_Pm1008dcpAlmDwCsfDetPortn_Type = EkiOnOff
_Pm1008dcpAlmDwCsfDetPortn_Object = MibTableColumn
pm1008dcpAlmDwCsfDetPortn = _Pm1008dcpAlmDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 72, 1, 12),
    _Pm1008dcpAlmDwCsfDetPortn_Type()
)
pm1008dcpAlmDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwCsfDetPortn.setStatus("current")
_Pm1008dcpAlmDwBufferOvlPortn_Type = EkiOnOff
_Pm1008dcpAlmDwBufferOvlPortn_Object = MibTableColumn
pm1008dcpAlmDwBufferOvlPortn = _Pm1008dcpAlmDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 2, 3, 72, 1, 15),
    _Pm1008dcpAlmDwBufferOvlPortn_Type()
)
pm1008dcpAlmDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwBufferOvlPortn.setStatus("current")
_Pm1008dcpAlmLine_ObjectIdentity = ObjectIdentity
pm1008dcpAlmLine = _Pm1008dcpAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3)
)
_Pm1008dcpAlmLineNurg_ObjectIdentity = ObjectIdentity
pm1008dcpAlmLineNurg = _Pm1008dcpAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1)
)
_Pm1008dcpAlmlineXfp1WarningsTable_Object = MibTable
pm1008dcpAlmlineXfp1WarningsTable = _Pm1008dcpAlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1WarningsTable.setStatus("current")
_Pm1008dcpAlmlineXfp1WarningsEntry_Object = MibTableRow
pm1008dcpAlmlineXfp1WarningsEntry = _Pm1008dcpAlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1)
)
pm1008dcpAlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1WarningsEntry.setStatus("current")


class _Pm1008dcpAlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pm1008dcpAlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmlineXfp1WarningsIndex_Object = MibTableColumn
pm1008dcpAlmlineXfp1WarningsIndex = _Pm1008dcpAlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1, 1),
    _Pm1008dcpAlmlineXfp1WarningsIndex_Type()
)
pm1008dcpAlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1WarningsIndex.setStatus("current")
_Pm1008dcpAlmTxPowerLowWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmTxPowerLowWarningPortn_Object = MibTableColumn
pm1008dcpAlmTxPowerLowWarningPortn = _Pm1008dcpAlmTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1, 2),
    _Pm1008dcpAlmTxPowerLowWarningPortn_Type()
)
pm1008dcpAlmTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxPowerLowWarningPortn.setStatus("current")
_Pm1008dcpAlmTxPowerHighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmTxPowerHighWarningPortn_Object = MibTableColumn
pm1008dcpAlmTxPowerHighWarningPortn = _Pm1008dcpAlmTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1, 3),
    _Pm1008dcpAlmTxPowerHighWarningPortn_Type()
)
pm1008dcpAlmTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxPowerHighWarningPortn.setStatus("current")
_Pm1008dcpAlmTxBiasLowWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmTxBiasLowWarningPortn_Object = MibTableColumn
pm1008dcpAlmTxBiasLowWarningPortn = _Pm1008dcpAlmTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1, 4),
    _Pm1008dcpAlmTxBiasLowWarningPortn_Type()
)
pm1008dcpAlmTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxBiasLowWarningPortn.setStatus("current")
_Pm1008dcpAlmTxBiasHighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmTxBiasHighWarningPortn_Object = MibTableColumn
pm1008dcpAlmTxBiasHighWarningPortn = _Pm1008dcpAlmTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1, 5),
    _Pm1008dcpAlmTxBiasHighWarningPortn_Type()
)
pm1008dcpAlmTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxBiasHighWarningPortn.setStatus("current")
_Pm1008dcpAlmTempLowWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmTempLowWarningPortn_Object = MibTableColumn
pm1008dcpAlmTempLowWarningPortn = _Pm1008dcpAlmTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1, 8),
    _Pm1008dcpAlmTempLowWarningPortn_Type()
)
pm1008dcpAlmTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTempLowWarningPortn.setStatus("current")
_Pm1008dcpAlmTempHighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmTempHighWarningPortn_Object = MibTableColumn
pm1008dcpAlmTempHighWarningPortn = _Pm1008dcpAlmTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1, 9),
    _Pm1008dcpAlmTempHighWarningPortn_Type()
)
pm1008dcpAlmTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTempHighWarningPortn.setStatus("current")
_Pm1008dcpAlmRxPowerLowWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmRxPowerLowWarningPortn_Object = MibTableColumn
pm1008dcpAlmRxPowerLowWarningPortn = _Pm1008dcpAlmRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1, 16),
    _Pm1008dcpAlmRxPowerLowWarningPortn_Type()
)
pm1008dcpAlmRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxPowerLowWarningPortn.setStatus("current")
_Pm1008dcpAlmRxPowerHighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmRxPowerHighWarningPortn_Object = MibTableColumn
pm1008dcpAlmRxPowerHighWarningPortn = _Pm1008dcpAlmRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 209, 1, 17),
    _Pm1008dcpAlmRxPowerHighWarningPortn_Type()
)
pm1008dcpAlmRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxPowerHighWarningPortn.setStatus("current")
_Pm1008dcpAlmlineOtx1TlhWarningsTable_Object = MibTable
pm1008dcpAlmlineOtx1TlhWarningsTable = _Pm1008dcpAlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineOtx1TlhWarningsTable.setStatus("current")
_Pm1008dcpAlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pm1008dcpAlmlineOtx1TlhWarningsEntry = _Pm1008dcpAlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 225, 1)
)
pm1008dcpAlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pm1008dcpAlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pm1008dcpAlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pm1008dcpAlmlineOtx1TlhWarningsIndex = _Pm1008dcpAlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 225, 1, 1),
    _Pm1008dcpAlmlineOtx1TlhWarningsIndex_Type()
)
pm1008dcpAlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pm1008dcpAlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pm1008dcpAlmLineModulatorAgingHighWarningPortn = _Pm1008dcpAlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 225, 1, 6),
    _Pm1008dcpAlmLineModulatorAgingHighWarningPortn_Type()
)
pm1008dcpAlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pm1008dcpAlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmLineAgingHighWarningPortn_Object = MibTableColumn
pm1008dcpAlmLineAgingHighWarningPortn = _Pm1008dcpAlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 225, 1, 7),
    _Pm1008dcpAlmLineAgingHighWarningPortn_Type()
)
pm1008dcpAlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineAgingHighWarningPortn.setStatus("current")
_Pm1008dcpAlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pm1008dcpAlmLineFreqDevHighWarningPortn = _Pm1008dcpAlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 225, 1, 13),
    _Pm1008dcpAlmLineFreqDevHighWarningPortn_Type()
)
pm1008dcpAlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineFreqDevHighWarningPortn.setStatus("current")
_Pm1008dcpAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm1008dcpAlmLineLaserTempHighWarningPortn = _Pm1008dcpAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 1, 225, 1, 15),
    _Pm1008dcpAlmLineLaserTempHighWarningPortn_Type()
)
pm1008dcpAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm1008dcpAlmLineUrg_ObjectIdentity = ObjectIdentity
pm1008dcpAlmLineUrg = _Pm1008dcpAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2)
)
_Pm1008dcpAlmdfrmBerTable_Object = MibTable
pm1008dcpAlmdfrmBerTable = _Pm1008dcpAlmdfrmBerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 129)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmdfrmBerTable.setStatus("current")
_Pm1008dcpAlmdfrmBerEntry_Object = MibTableRow
pm1008dcpAlmdfrmBerEntry = _Pm1008dcpAlmdfrmBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 129, 1)
)
pm1008dcpAlmdfrmBerEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmdfrmBerIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmdfrmBerEntry.setStatus("current")


class _Pm1008dcpAlmdfrmBerIndex_Type(Integer32):
    """Custom type pm1008dcpAlmdfrmBerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmdfrmBerIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmdfrmBerIndex_Object = MibTableColumn
pm1008dcpAlmdfrmBerIndex = _Pm1008dcpAlmdfrmBerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 129, 1, 1),
    _Pm1008dcpAlmdfrmBerIndex_Type()
)
pm1008dcpAlmdfrmBerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmdfrmBerIndex.setStatus("current")
_Pm1008dcpAlmLineSignalDegradePortn_Type = EkiOnOff
_Pm1008dcpAlmLineSignalDegradePortn_Object = MibTableColumn
pm1008dcpAlmLineSignalDegradePortn = _Pm1008dcpAlmLineSignalDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 129, 1, 2),
    _Pm1008dcpAlmLineSignalDegradePortn_Type()
)
pm1008dcpAlmLineSignalDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineSignalDegradePortn.setStatus("current")
_Pm1008dcpAlmLineSignalFailPortn_Type = EkiOnOff
_Pm1008dcpAlmLineSignalFailPortn_Object = MibTableColumn
pm1008dcpAlmLineSignalFailPortn = _Pm1008dcpAlmLineSignalFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 129, 1, 3),
    _Pm1008dcpAlmLineSignalFailPortn_Type()
)
pm1008dcpAlmLineSignalFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineSignalFailPortn.setStatus("current")
_Pm1008dcpAlmLineDegradePortn_Type = EkiOnOff
_Pm1008dcpAlmLineDegradePortn_Object = MibTableColumn
pm1008dcpAlmLineDegradePortn = _Pm1008dcpAlmLineDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 129, 1, 6),
    _Pm1008dcpAlmLineDegradePortn_Type()
)
pm1008dcpAlmLineDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineDegradePortn.setStatus("current")
_Pm1008dcpAlmlineXfp1AlarmTable_Object = MibTable
pm1008dcpAlmlineXfp1AlarmTable = _Pm1008dcpAlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1AlarmTable.setStatus("current")
_Pm1008dcpAlmlineXfp1AlarmEntry_Object = MibTableRow
pm1008dcpAlmlineXfp1AlarmEntry = _Pm1008dcpAlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1)
)
pm1008dcpAlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1AlarmEntry.setStatus("current")


class _Pm1008dcpAlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pm1008dcpAlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmlineXfp1AlarmIndex_Object = MibTableColumn
pm1008dcpAlmlineXfp1AlarmIndex = _Pm1008dcpAlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1, 1),
    _Pm1008dcpAlmlineXfp1AlarmIndex_Type()
)
pm1008dcpAlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1AlarmIndex.setStatus("current")
_Pm1008dcpAlmTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmTxPowerLowAlarmPortn_Object = MibTableColumn
pm1008dcpAlmTxPowerLowAlarmPortn = _Pm1008dcpAlmTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1, 2),
    _Pm1008dcpAlmTxPowerLowAlarmPortn_Type()
)
pm1008dcpAlmTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxPowerLowAlarmPortn.setStatus("current")
_Pm1008dcpAlmTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmTxPowerHighAlarmPortn_Object = MibTableColumn
pm1008dcpAlmTxPowerHighAlarmPortn = _Pm1008dcpAlmTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1, 3),
    _Pm1008dcpAlmTxPowerHighAlarmPortn_Type()
)
pm1008dcpAlmTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxPowerHighAlarmPortn.setStatus("current")
_Pm1008dcpAlmTxBiasLowAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmTxBiasLowAlarmPortn_Object = MibTableColumn
pm1008dcpAlmTxBiasLowAlarmPortn = _Pm1008dcpAlmTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1, 4),
    _Pm1008dcpAlmTxBiasLowAlarmPortn_Type()
)
pm1008dcpAlmTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxBiasLowAlarmPortn.setStatus("current")
_Pm1008dcpAlmTxBiasHighAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmTxBiasHighAlarmPortn_Object = MibTableColumn
pm1008dcpAlmTxBiasHighAlarmPortn = _Pm1008dcpAlmTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1, 5),
    _Pm1008dcpAlmTxBiasHighAlarmPortn_Type()
)
pm1008dcpAlmTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxBiasHighAlarmPortn.setStatus("current")
_Pm1008dcpAlmTempLowAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmTempLowAlarmPortn_Object = MibTableColumn
pm1008dcpAlmTempLowAlarmPortn = _Pm1008dcpAlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1, 8),
    _Pm1008dcpAlmTempLowAlarmPortn_Type()
)
pm1008dcpAlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTempLowAlarmPortn.setStatus("current")
_Pm1008dcpAlmTempHighAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmTempHighAlarmPortn_Object = MibTableColumn
pm1008dcpAlmTempHighAlarmPortn = _Pm1008dcpAlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1, 9),
    _Pm1008dcpAlmTempHighAlarmPortn_Type()
)
pm1008dcpAlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTempHighAlarmPortn.setStatus("current")
_Pm1008dcpAlmRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmRxPowerLowAlarmPortn_Object = MibTableColumn
pm1008dcpAlmRxPowerLowAlarmPortn = _Pm1008dcpAlmRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1, 16),
    _Pm1008dcpAlmRxPowerLowAlarmPortn_Type()
)
pm1008dcpAlmRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxPowerLowAlarmPortn.setStatus("current")
_Pm1008dcpAlmRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmRxPowerHighAlarmPortn_Object = MibTableColumn
pm1008dcpAlmRxPowerHighAlarmPortn = _Pm1008dcpAlmRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 208, 1, 17),
    _Pm1008dcpAlmRxPowerHighAlarmPortn_Type()
)
pm1008dcpAlmRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxPowerHighAlarmPortn.setStatus("current")
_Pm1008dcpAlmlineXfp1SupplyAlarmTable_Object = MibTable
pm1008dcpAlmlineXfp1SupplyAlarmTable = _Pm1008dcpAlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pm1008dcpAlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pm1008dcpAlmlineXfp1SupplyAlarmEntry = _Pm1008dcpAlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1)
)
pm1008dcpAlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pm1008dcpAlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pm1008dcpAlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pm1008dcpAlmlineXfp1SupplyAlarmIndex = _Pm1008dcpAlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 1),
    _Pm1008dcpAlmlineXfp1SupplyAlarmIndex_Type()
)
pm1008dcpAlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pm1008dcpAlmVee5LowAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmVee5LowAlarmPortn_Object = MibTableColumn
pm1008dcpAlmVee5LowAlarmPortn = _Pm1008dcpAlmVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 2),
    _Pm1008dcpAlmVee5LowAlarmPortn_Type()
)
pm1008dcpAlmVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVee5LowAlarmPortn.setStatus("current")
_Pm1008dcpAlmVee5HighAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmVee5HighAlarmPortn_Object = MibTableColumn
pm1008dcpAlmVee5HighAlarmPortn = _Pm1008dcpAlmVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 3),
    _Pm1008dcpAlmVee5HighAlarmPortn_Type()
)
pm1008dcpAlmVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVee5HighAlarmPortn.setStatus("current")
_Pm1008dcpAlmVcc2LowAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc2LowAlarmPortn_Object = MibTableColumn
pm1008dcpAlmVcc2LowAlarmPortn = _Pm1008dcpAlmVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 4),
    _Pm1008dcpAlmVcc2LowAlarmPortn_Type()
)
pm1008dcpAlmVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc2LowAlarmPortn.setStatus("current")
_Pm1008dcpAlmVcc2HighAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc2HighAlarmPortn_Object = MibTableColumn
pm1008dcpAlmVcc2HighAlarmPortn = _Pm1008dcpAlmVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 5),
    _Pm1008dcpAlmVcc2HighAlarmPortn_Type()
)
pm1008dcpAlmVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc2HighAlarmPortn.setStatus("current")
_Pm1008dcpAlmVcc3LowAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc3LowAlarmPortn_Object = MibTableColumn
pm1008dcpAlmVcc3LowAlarmPortn = _Pm1008dcpAlmVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 6),
    _Pm1008dcpAlmVcc3LowAlarmPortn_Type()
)
pm1008dcpAlmVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc3LowAlarmPortn.setStatus("current")
_Pm1008dcpAlmVcc3HighAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc3HighAlarmPortn_Object = MibTableColumn
pm1008dcpAlmVcc3HighAlarmPortn = _Pm1008dcpAlmVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 7),
    _Pm1008dcpAlmVcc3HighAlarmPortn_Type()
)
pm1008dcpAlmVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc3HighAlarmPortn.setStatus("current")
_Pm1008dcpAlmVcc5LowAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc5LowAlarmPortn_Object = MibTableColumn
pm1008dcpAlmVcc5LowAlarmPortn = _Pm1008dcpAlmVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 8),
    _Pm1008dcpAlmVcc5LowAlarmPortn_Type()
)
pm1008dcpAlmVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc5LowAlarmPortn.setStatus("current")
_Pm1008dcpAlmVcc5HighAlarmPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc5HighAlarmPortn_Object = MibTableColumn
pm1008dcpAlmVcc5HighAlarmPortn = _Pm1008dcpAlmVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 9),
    _Pm1008dcpAlmVcc5HighAlarmPortn_Type()
)
pm1008dcpAlmVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc5HighAlarmPortn.setStatus("current")
_Pm1008dcpAlmVee5LowWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmVee5LowWarningPortn_Object = MibTableColumn
pm1008dcpAlmVee5LowWarningPortn = _Pm1008dcpAlmVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 10),
    _Pm1008dcpAlmVee5LowWarningPortn_Type()
)
pm1008dcpAlmVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVee5LowWarningPortn.setStatus("current")
_Pm1008dcpAlmVee5HighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmVee5HighWarningPortn_Object = MibTableColumn
pm1008dcpAlmVee5HighWarningPortn = _Pm1008dcpAlmVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 11),
    _Pm1008dcpAlmVee5HighWarningPortn_Type()
)
pm1008dcpAlmVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVee5HighWarningPortn.setStatus("current")
_Pm1008dcpAlmVcc2LowWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc2LowWarningPortn_Object = MibTableColumn
pm1008dcpAlmVcc2LowWarningPortn = _Pm1008dcpAlmVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 12),
    _Pm1008dcpAlmVcc2LowWarningPortn_Type()
)
pm1008dcpAlmVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc2LowWarningPortn.setStatus("current")
_Pm1008dcpAlmVcc2HighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc2HighWarningPortn_Object = MibTableColumn
pm1008dcpAlmVcc2HighWarningPortn = _Pm1008dcpAlmVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 13),
    _Pm1008dcpAlmVcc2HighWarningPortn_Type()
)
pm1008dcpAlmVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc2HighWarningPortn.setStatus("current")
_Pm1008dcpAlmVcc3LowWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc3LowWarningPortn_Object = MibTableColumn
pm1008dcpAlmVcc3LowWarningPortn = _Pm1008dcpAlmVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 14),
    _Pm1008dcpAlmVcc3LowWarningPortn_Type()
)
pm1008dcpAlmVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc3LowWarningPortn.setStatus("current")
_Pm1008dcpAlmVcc3HighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc3HighWarningPortn_Object = MibTableColumn
pm1008dcpAlmVcc3HighWarningPortn = _Pm1008dcpAlmVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 15),
    _Pm1008dcpAlmVcc3HighWarningPortn_Type()
)
pm1008dcpAlmVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc3HighWarningPortn.setStatus("current")
_Pm1008dcpAlmVcc5LowWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc5LowWarningPortn_Object = MibTableColumn
pm1008dcpAlmVcc5LowWarningPortn = _Pm1008dcpAlmVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 16),
    _Pm1008dcpAlmVcc5LowWarningPortn_Type()
)
pm1008dcpAlmVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc5LowWarningPortn.setStatus("current")
_Pm1008dcpAlmVcc5HighWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmVcc5HighWarningPortn_Object = MibTableColumn
pm1008dcpAlmVcc5HighWarningPortn = _Pm1008dcpAlmVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 212, 1, 17),
    _Pm1008dcpAlmVcc5HighWarningPortn_Type()
)
pm1008dcpAlmVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmVcc5HighWarningPortn.setStatus("current")
_Pm1008dcpAlmlineOtx1TlhAlarmsTable_Object = MibTable
pm1008dcpAlmlineOtx1TlhAlarmsTable = _Pm1008dcpAlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pm1008dcpAlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pm1008dcpAlmlineOtx1TlhAlarmsEntry = _Pm1008dcpAlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 224, 1)
)
pm1008dcpAlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pm1008dcpAlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pm1008dcpAlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pm1008dcpAlmlineOtx1TlhAlarmsIndex = _Pm1008dcpAlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 224, 1, 1),
    _Pm1008dcpAlmlineOtx1TlhAlarmsIndex_Type()
)
pm1008dcpAlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pm1008dcpAlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pm1008dcpAlmLineModulatorAgingHighAlaPortn = _Pm1008dcpAlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 224, 1, 6),
    _Pm1008dcpAlmLineModulatorAgingHighAlaPortn_Type()
)
pm1008dcpAlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pm1008dcpAlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmLineAgingHighAlaPortn_Object = MibTableColumn
pm1008dcpAlmLineAgingHighAlaPortn = _Pm1008dcpAlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 224, 1, 7),
    _Pm1008dcpAlmLineAgingHighAlaPortn_Type()
)
pm1008dcpAlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineAgingHighAlaPortn.setStatus("current")
_Pm1008dcpAlmLineCdrNotReadyPortn_Type = EkiOnOff
_Pm1008dcpAlmLineCdrNotReadyPortn_Object = MibTableColumn
pm1008dcpAlmLineCdrNotReadyPortn = _Pm1008dcpAlmLineCdrNotReadyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 224, 1, 10),
    _Pm1008dcpAlmLineCdrNotReadyPortn_Type()
)
pm1008dcpAlmLineCdrNotReadyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineCdrNotReadyPortn.setStatus("current")
_Pm1008dcpAlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pm1008dcpAlmLineFreqDevHighAlaPortn = _Pm1008dcpAlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 224, 1, 13),
    _Pm1008dcpAlmLineFreqDevHighAlaPortn_Type()
)
pm1008dcpAlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineFreqDevHighAlaPortn.setStatus("current")
_Pm1008dcpAlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pm1008dcpAlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pm1008dcpAlmLineLaserTempHighAlaPortn = _Pm1008dcpAlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 2, 224, 1, 15),
    _Pm1008dcpAlmLineLaserTempHighAlaPortn_Type()
)
pm1008dcpAlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineLaserTempHighAlaPortn.setStatus("current")
_Pm1008dcpAlmLineCrit_ObjectIdentity = ObjectIdentity
pm1008dcpAlmLineCrit = _Pm1008dcpAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3)
)
_Pm1008dcpAlmsynthAlmLineTable_Object = MibTable
pm1008dcpAlmsynthAlmLineTable = _Pm1008dcpAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmsynthAlmLineTable.setStatus("current")
_Pm1008dcpAlmsynthAlmLineEntry_Object = MibTableRow
pm1008dcpAlmsynthAlmLineEntry = _Pm1008dcpAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1)
)
pm1008dcpAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmsynthAlmLineEntry.setStatus("current")


class _Pm1008dcpAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm1008dcpAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmsynthAlmLineIndex_Object = MibTableColumn
pm1008dcpAlmsynthAlmLineIndex = _Pm1008dcpAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 1),
    _Pm1008dcpAlmsynthAlmLineIndex_Type()
)
pm1008dcpAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmsynthAlmLineIndex.setStatus("current")
_Pm1008dcpAlmXfpAbsentPortn_Type = EkiOnOff
_Pm1008dcpAlmXfpAbsentPortn_Object = MibTableColumn
pm1008dcpAlmXfpAbsentPortn = _Pm1008dcpAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 2),
    _Pm1008dcpAlmXfpAbsentPortn_Type()
)
pm1008dcpAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmXfpAbsentPortn.setStatus("current")
_Pm1008dcpAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm1008dcpAlmXfpInitNotComplPortn_Object = MibTableColumn
pm1008dcpAlmXfpInitNotComplPortn = _Pm1008dcpAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 3),
    _Pm1008dcpAlmXfpInitNotComplPortn_Type()
)
pm1008dcpAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmXfpInitNotComplPortn.setStatus("current")
_Pm1008dcpAlmLineHwFailPortn_Type = EkiOnOff
_Pm1008dcpAlmLineHwFailPortn_Object = MibTableColumn
pm1008dcpAlmLineHwFailPortn = _Pm1008dcpAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 5),
    _Pm1008dcpAlmLineHwFailPortn_Type()
)
pm1008dcpAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineHwFailPortn.setStatus("current")
_Pm1008dcpAlmXfpTxOffPortn_Type = EkiOnOff
_Pm1008dcpAlmXfpTxOffPortn_Object = MibTableColumn
pm1008dcpAlmXfpTxOffPortn = _Pm1008dcpAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 6),
    _Pm1008dcpAlmXfpTxOffPortn_Type()
)
pm1008dcpAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmXfpTxOffPortn.setStatus("current")
_Pm1008dcpAlmLineLocalOosPortn_Type = EkiOnOff
_Pm1008dcpAlmLineLocalOosPortn_Object = MibTableColumn
pm1008dcpAlmLineLocalOosPortn = _Pm1008dcpAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 7),
    _Pm1008dcpAlmLineLocalOosPortn_Type()
)
pm1008dcpAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineLocalOosPortn.setStatus("current")
_Pm1008dcpAlmUpRdiInsPortn_Type = EkiOnOff
_Pm1008dcpAlmUpRdiInsPortn_Object = MibTableColumn
pm1008dcpAlmUpRdiInsPortn = _Pm1008dcpAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 9),
    _Pm1008dcpAlmUpRdiInsPortn_Type()
)
pm1008dcpAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmUpRdiInsPortn.setStatus("current")
_Pm1008dcpAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm1008dcpAlmLineDdmWarningPortn_Object = MibTableColumn
pm1008dcpAlmLineDdmWarningPortn = _Pm1008dcpAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 10),
    _Pm1008dcpAlmLineDdmWarningPortn_Type()
)
pm1008dcpAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineDdmWarningPortn.setStatus("current")
_Pm1008dcpAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm1008dcpAlmLineDdmAlmPortn_Object = MibTableColumn
pm1008dcpAlmLineDdmAlmPortn = _Pm1008dcpAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 11),
    _Pm1008dcpAlmLineDdmAlmPortn_Type()
)
pm1008dcpAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineDdmAlmPortn.setStatus("current")
_Pm1008dcpAlmLineFailPortn_Type = EkiOnOff
_Pm1008dcpAlmLineFailPortn_Object = MibTableColumn
pm1008dcpAlmLineFailPortn = _Pm1008dcpAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 7, 1, 13),
    _Pm1008dcpAlmLineFailPortn_Type()
)
pm1008dcpAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmLineFailPortn.setStatus("current")
_Pm1008dcpAlmdfrmAlmTable_Object = MibTable
pm1008dcpAlmdfrmAlmTable = _Pm1008dcpAlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmdfrmAlmTable.setStatus("current")
_Pm1008dcpAlmdfrmAlmEntry_Object = MibTableRow
pm1008dcpAlmdfrmAlmEntry = _Pm1008dcpAlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 128, 1)
)
pm1008dcpAlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmdfrmAlmEntry.setStatus("current")


class _Pm1008dcpAlmdfrmAlmIndex_Type(Integer32):
    """Custom type pm1008dcpAlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmdfrmAlmIndex_Object = MibTableColumn
pm1008dcpAlmdfrmAlmIndex = _Pm1008dcpAlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 128, 1, 1),
    _Pm1008dcpAlmdfrmAlmIndex_Type()
)
pm1008dcpAlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmdfrmAlmIndex.setStatus("current")
_Pm1008dcpAlmDwAisDetPortn_Type = EkiOnOff
_Pm1008dcpAlmDwAisDetPortn_Object = MibTableColumn
pm1008dcpAlmDwAisDetPortn = _Pm1008dcpAlmDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 128, 1, 2),
    _Pm1008dcpAlmDwAisDetPortn_Type()
)
pm1008dcpAlmDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwAisDetPortn.setStatus("current")
_Pm1008dcpAlmDwRdiDetPortn_Type = EkiOnOff
_Pm1008dcpAlmDwRdiDetPortn_Object = MibTableColumn
pm1008dcpAlmDwRdiDetPortn = _Pm1008dcpAlmDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 128, 1, 3),
    _Pm1008dcpAlmDwRdiDetPortn_Type()
)
pm1008dcpAlmDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwRdiDetPortn.setStatus("current")
_Pm1008dcpAlmDwOofPortn_Type = EkiOnOff
_Pm1008dcpAlmDwOofPortn_Object = MibTableColumn
pm1008dcpAlmDwOofPortn = _Pm1008dcpAlmDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 128, 1, 4),
    _Pm1008dcpAlmDwOofPortn_Type()
)
pm1008dcpAlmDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwOofPortn.setStatus("current")
_Pm1008dcpAlmDwLofPortn_Type = EkiOnOff
_Pm1008dcpAlmDwLofPortn_Object = MibTableColumn
pm1008dcpAlmDwLofPortn = _Pm1008dcpAlmDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 128, 1, 5),
    _Pm1008dcpAlmDwLofPortn_Type()
)
pm1008dcpAlmDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwLofPortn.setStatus("current")
_Pm1008dcpAlmlineSyncAlarmsTable_Object = MibTable
pm1008dcpAlmlineSyncAlarmsTable = _Pm1008dcpAlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineSyncAlarmsTable.setStatus("current")
_Pm1008dcpAlmlineSyncAlarmsEntry_Object = MibTableRow
pm1008dcpAlmlineSyncAlarmsEntry = _Pm1008dcpAlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 133, 1)
)
pm1008dcpAlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineSyncAlarmsEntry.setStatus("current")


class _Pm1008dcpAlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pm1008dcpAlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmlineSyncAlarmsIndex_Object = MibTableColumn
pm1008dcpAlmlineSyncAlarmsIndex = _Pm1008dcpAlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 133, 1, 1),
    _Pm1008dcpAlmlineSyncAlarmsIndex_Type()
)
pm1008dcpAlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmlineSyncAlarmsIndex.setStatus("current")
_Pm1008dcpAlmDwLockerrPortn_Type = EkiOnOff
_Pm1008dcpAlmDwLockerrPortn_Object = MibTableColumn
pm1008dcpAlmDwLockerrPortn = _Pm1008dcpAlmDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 133, 1, 13),
    _Pm1008dcpAlmDwLockerrPortn_Type()
)
pm1008dcpAlmDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwLockerrPortn.setStatus("current")
_Pm1008dcpAlmUpLockerrPortn_Type = EkiOnOff
_Pm1008dcpAlmUpLockerrPortn_Object = MibTableColumn
pm1008dcpAlmUpLockerrPortn = _Pm1008dcpAlmUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 133, 1, 14),
    _Pm1008dcpAlmUpLockerrPortn_Type()
)
pm1008dcpAlmUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmUpLockerrPortn.setStatus("current")
_Pm1008dcpAlmDwLosPortn_Type = EkiOnOff
_Pm1008dcpAlmDwLosPortn_Object = MibTableColumn
pm1008dcpAlmDwLosPortn = _Pm1008dcpAlmDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 133, 1, 17),
    _Pm1008dcpAlmDwLosPortn_Type()
)
pm1008dcpAlmDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmDwLosPortn.setStatus("current")
_Pm1008dcpAlmlineXfp1AlarmsTable_Object = MibTable
pm1008dcpAlmlineXfp1AlarmsTable = _Pm1008dcpAlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1AlarmsTable.setStatus("current")
_Pm1008dcpAlmlineXfp1AlarmsEntry_Object = MibTableRow
pm1008dcpAlmlineXfp1AlarmsEntry = _Pm1008dcpAlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1)
)
pm1008dcpAlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1AlarmsEntry.setStatus("current")


class _Pm1008dcpAlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pm1008dcpAlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpAlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pm1008dcpAlmlineXfp1AlarmsIndex_Object = MibTableColumn
pm1008dcpAlmlineXfp1AlarmsIndex = _Pm1008dcpAlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 1),
    _Pm1008dcpAlmlineXfp1AlarmsIndex_Type()
)
pm1008dcpAlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmlineXfp1AlarmsIndex.setStatus("current")
_Pm1008dcpAlmModNrPortn_Type = EkiOnOff
_Pm1008dcpAlmModNrPortn_Object = MibTableColumn
pm1008dcpAlmModNrPortn = _Pm1008dcpAlmModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 3),
    _Pm1008dcpAlmModNrPortn_Type()
)
pm1008dcpAlmModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmModNrPortn.setStatus("current")
_Pm1008dcpAlmRxCdrNotLockedPortn_Type = EkiOnOff
_Pm1008dcpAlmRxCdrNotLockedPortn_Object = MibTableColumn
pm1008dcpAlmRxCdrNotLockedPortn = _Pm1008dcpAlmRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 4),
    _Pm1008dcpAlmRxCdrNotLockedPortn_Type()
)
pm1008dcpAlmRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxCdrNotLockedPortn.setStatus("current")
_Pm1008dcpAlmRxNrPortn_Type = EkiOnOff
_Pm1008dcpAlmRxNrPortn_Object = MibTableColumn
pm1008dcpAlmRxNrPortn = _Pm1008dcpAlmRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 6),
    _Pm1008dcpAlmRxNrPortn_Type()
)
pm1008dcpAlmRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmRxNrPortn.setStatus("current")
_Pm1008dcpAlmTxCdrNotLockedPortn_Type = EkiOnOff
_Pm1008dcpAlmTxCdrNotLockedPortn_Object = MibTableColumn
pm1008dcpAlmTxCdrNotLockedPortn = _Pm1008dcpAlmTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 7),
    _Pm1008dcpAlmTxCdrNotLockedPortn_Type()
)
pm1008dcpAlmTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxCdrNotLockedPortn.setStatus("current")
_Pm1008dcpAlmTxFaultPortn_Type = EkiOnOff
_Pm1008dcpAlmTxFaultPortn_Object = MibTableColumn
pm1008dcpAlmTxFaultPortn = _Pm1008dcpAlmTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 8),
    _Pm1008dcpAlmTxFaultPortn_Type()
)
pm1008dcpAlmTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxFaultPortn.setStatus("current")
_Pm1008dcpAlmTxNrPortn_Type = EkiOnOff
_Pm1008dcpAlmTxNrPortn_Object = MibTableColumn
pm1008dcpAlmTxNrPortn = _Pm1008dcpAlmTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 9),
    _Pm1008dcpAlmTxNrPortn_Type()
)
pm1008dcpAlmTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTxNrPortn.setStatus("current")
_Pm1008dcpAlmChannelNotAcquiredPortn_Type = EkiOnOff
_Pm1008dcpAlmChannelNotAcquiredPortn_Object = MibTableColumn
pm1008dcpAlmChannelNotAcquiredPortn = _Pm1008dcpAlmChannelNotAcquiredPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 11),
    _Pm1008dcpAlmChannelNotAcquiredPortn_Type()
)
pm1008dcpAlmChannelNotAcquiredPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmChannelNotAcquiredPortn.setStatus("current")
_Pm1008dcpAlmWavelengthUnlockedPortn_Type = EkiOnOff
_Pm1008dcpAlmWavelengthUnlockedPortn_Object = MibTableColumn
pm1008dcpAlmWavelengthUnlockedPortn = _Pm1008dcpAlmWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 15),
    _Pm1008dcpAlmWavelengthUnlockedPortn_Type()
)
pm1008dcpAlmWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmWavelengthUnlockedPortn.setStatus("current")
_Pm1008dcpAlmTecFaultPortn_Type = EkiOnOff
_Pm1008dcpAlmTecFaultPortn_Object = MibTableColumn
pm1008dcpAlmTecFaultPortn = _Pm1008dcpAlmTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 16),
    _Pm1008dcpAlmTecFaultPortn_Type()
)
pm1008dcpAlmTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmTecFaultPortn.setStatus("current")
_Pm1008dcpAlmApdSupplyFaultPortn_Type = EkiOnOff
_Pm1008dcpAlmApdSupplyFaultPortn_Object = MibTableColumn
pm1008dcpAlmApdSupplyFaultPortn = _Pm1008dcpAlmApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 2, 3, 3, 211, 1, 17),
    _Pm1008dcpAlmApdSupplyFaultPortn_Type()
)
pm1008dcpAlmApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpAlmApdSupplyFaultPortn.setStatus("current")
_Pm1008dcpmeasures_ObjectIdentity = ObjectIdentity
pm1008dcpmeasures = _Pm1008dcpmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3)
)
_Pm1008dcpMesrOther_ObjectIdentity = ObjectIdentity
pm1008dcpMesrOther = _Pm1008dcpMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 1)
)
_Pm1008dcpMesrsynth0_Type = EkiMeasureType
_Pm1008dcpMesrsynth0_Object = MibScalar
pm1008dcpMesrsynth0 = _Pm1008dcpMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 1, 0),
    _Pm1008dcpMesrsynth0_Type()
)
pm1008dcpMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrsynth0.setStatus("deprecated")
_Pm1008dcpMesrsynth1_Type = EkiMeasureType
_Pm1008dcpMesrsynth1_Object = MibScalar
pm1008dcpMesrsynth1 = _Pm1008dcpMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 1, 1),
    _Pm1008dcpMesrsynth1_Type()
)
pm1008dcpMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrsynth1.setStatus("deprecated")
_Pm1008dcpMesrClient_ObjectIdentity = ObjectIdentity
pm1008dcpMesrClient = _Pm1008dcpMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2)
)
_Pm1008dcpMesrtempMeasTable_Object = MibTable
pm1008dcpMesrtempMeasTable = _Pm1008dcpMesrtempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrtempMeasTable.setStatus("current")
_Pm1008dcpMesrtempMeasEntry_Object = MibTableRow
pm1008dcpMesrtempMeasEntry = _Pm1008dcpMesrtempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 16, 1)
)
pm1008dcpMesrtempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrtempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrtempMeasEntry.setStatus("current")


class _Pm1008dcpMesrtempMeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrtempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrtempMeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrtempMeasIndex_Object = MibTableColumn
pm1008dcpMesrtempMeasIndex = _Pm1008dcpMesrtempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 16, 1, 1),
    _Pm1008dcpMesrtempMeasIndex_Type()
)
pm1008dcpMesrtempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrtempMeasIndex.setStatus("current")


class _Pm1008dcpMesrtempMeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrtempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrtempMeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrtempMeasPortn_Object = MibTableColumn
pm1008dcpMesrtempMeasPortn = _Pm1008dcpMesrtempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 16, 1, 2),
    _Pm1008dcpMesrtempMeasPortn_Type()
)
pm1008dcpMesrtempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrtempMeasPortn.setStatus("current")
_Pm1008dcpMesrvoltMeasTable_Object = MibTable
pm1008dcpMesrvoltMeasTable = _Pm1008dcpMesrvoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrvoltMeasTable.setStatus("current")
_Pm1008dcpMesrvoltMeasEntry_Object = MibTableRow
pm1008dcpMesrvoltMeasEntry = _Pm1008dcpMesrvoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 24, 1)
)
pm1008dcpMesrvoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrvoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrvoltMeasEntry.setStatus("current")


class _Pm1008dcpMesrvoltMeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrvoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrvoltMeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrvoltMeasIndex_Object = MibTableColumn
pm1008dcpMesrvoltMeasIndex = _Pm1008dcpMesrvoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 24, 1, 1),
    _Pm1008dcpMesrvoltMeasIndex_Type()
)
pm1008dcpMesrvoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrvoltMeasIndex.setStatus("current")


class _Pm1008dcpMesrvoltMeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrvoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrvoltMeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrvoltMeasPortn_Object = MibTableColumn
pm1008dcpMesrvoltMeasPortn = _Pm1008dcpMesrvoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 24, 1, 2),
    _Pm1008dcpMesrvoltMeasPortn_Type()
)
pm1008dcpMesrvoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrvoltMeasPortn.setStatus("current")
_Pm1008dcpMesrbiasMeasTable_Object = MibTable
pm1008dcpMesrbiasMeasTable = _Pm1008dcpMesrbiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrbiasMeasTable.setStatus("current")
_Pm1008dcpMesrbiasMeasEntry_Object = MibTableRow
pm1008dcpMesrbiasMeasEntry = _Pm1008dcpMesrbiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 32, 1)
)
pm1008dcpMesrbiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrbiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrbiasMeasEntry.setStatus("current")


class _Pm1008dcpMesrbiasMeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrbiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrbiasMeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrbiasMeasIndex_Object = MibTableColumn
pm1008dcpMesrbiasMeasIndex = _Pm1008dcpMesrbiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 32, 1, 1),
    _Pm1008dcpMesrbiasMeasIndex_Type()
)
pm1008dcpMesrbiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrbiasMeasIndex.setStatus("current")


class _Pm1008dcpMesrbiasMeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrbiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrbiasMeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrbiasMeasPortn_Object = MibTableColumn
pm1008dcpMesrbiasMeasPortn = _Pm1008dcpMesrbiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 32, 1, 2),
    _Pm1008dcpMesrbiasMeasPortn_Type()
)
pm1008dcpMesrbiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrbiasMeasPortn.setStatus("current")
_Pm1008dcpMesrtxpwrMeasTable_Object = MibTable
pm1008dcpMesrtxpwrMeasTable = _Pm1008dcpMesrtxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrtxpwrMeasTable.setStatus("current")
_Pm1008dcpMesrtxpwrMeasEntry_Object = MibTableRow
pm1008dcpMesrtxpwrMeasEntry = _Pm1008dcpMesrtxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 40, 1)
)
pm1008dcpMesrtxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrtxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrtxpwrMeasEntry.setStatus("current")


class _Pm1008dcpMesrtxpwrMeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrtxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrtxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrtxpwrMeasIndex_Object = MibTableColumn
pm1008dcpMesrtxpwrMeasIndex = _Pm1008dcpMesrtxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 40, 1, 1),
    _Pm1008dcpMesrtxpwrMeasIndex_Type()
)
pm1008dcpMesrtxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrtxpwrMeasIndex.setStatus("current")


class _Pm1008dcpMesrtxpwrMeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrtxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrtxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrtxpwrMeasPortn_Object = MibTableColumn
pm1008dcpMesrtxpwrMeasPortn = _Pm1008dcpMesrtxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 40, 1, 2),
    _Pm1008dcpMesrtxpwrMeasPortn_Type()
)
pm1008dcpMesrtxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrtxpwrMeasPortn.setStatus("current")
_Pm1008dcpMesrrxpwrMeasTable_Object = MibTable
pm1008dcpMesrrxpwrMeasTable = _Pm1008dcpMesrrxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrrxpwrMeasTable.setStatus("current")
_Pm1008dcpMesrrxpwrMeasEntry_Object = MibTableRow
pm1008dcpMesrrxpwrMeasEntry = _Pm1008dcpMesrrxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 48, 1)
)
pm1008dcpMesrrxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrrxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrrxpwrMeasEntry.setStatus("current")


class _Pm1008dcpMesrrxpwrMeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrrxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrrxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrrxpwrMeasIndex_Object = MibTableColumn
pm1008dcpMesrrxpwrMeasIndex = _Pm1008dcpMesrrxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 48, 1, 1),
    _Pm1008dcpMesrrxpwrMeasIndex_Type()
)
pm1008dcpMesrrxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrrxpwrMeasIndex.setStatus("current")


class _Pm1008dcpMesrrxpwrMeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrrxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrrxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrrxpwrMeasPortn_Object = MibTableColumn
pm1008dcpMesrrxpwrMeasPortn = _Pm1008dcpMesrrxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 2, 48, 1, 2),
    _Pm1008dcpMesrrxpwrMeasPortn_Type()
)
pm1008dcpMesrrxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrrxpwrMeasPortn.setStatus("current")
_Pm1008dcpMesrLine_ObjectIdentity = ObjectIdentity
pm1008dcpMesrLine = _Pm1008dcpMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3)
)
_Pm1008dcpMesrxfp1LxModTempMeasTable_Object = MibTable
pm1008dcpMesrxfp1LxModTempMeasTable = _Pm1008dcpMesrxfp1LxModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxModTempMeasTable.setStatus("current")
_Pm1008dcpMesrxfp1LxModTempMeasEntry_Object = MibTableRow
pm1008dcpMesrxfp1LxModTempMeasEntry = _Pm1008dcpMesrxfp1LxModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 208, 1)
)
pm1008dcpMesrxfp1LxModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrxfp1LxModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxModTempMeasEntry.setStatus("current")


class _Pm1008dcpMesrxfp1LxModTempMeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LxModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrxfp1LxModTempMeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LxModTempMeasIndex_Object = MibTableColumn
pm1008dcpMesrxfp1LxModTempMeasIndex = _Pm1008dcpMesrxfp1LxModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 208, 1, 1),
    _Pm1008dcpMesrxfp1LxModTempMeasIndex_Type()
)
pm1008dcpMesrxfp1LxModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxModTempMeasIndex.setStatus("current")


class _Pm1008dcpMesrxfp1LxModTempMeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LxModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrxfp1LxModTempMeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LxModTempMeasPortn_Object = MibTableColumn
pm1008dcpMesrxfp1LxModTempMeasPortn = _Pm1008dcpMesrxfp1LxModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 208, 1, 2),
    _Pm1008dcpMesrxfp1LxModTempMeasPortn_Type()
)
pm1008dcpMesrxfp1LxModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxModTempMeasPortn.setStatus("current")
_Pm1008dcpMesrxfp1ReservedTable_Object = MibTable
pm1008dcpMesrxfp1ReservedTable = _Pm1008dcpMesrxfp1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1ReservedTable.setStatus("deprecated")
_Pm1008dcpMesrxfp1ReservedEntry_Object = MibTableRow
pm1008dcpMesrxfp1ReservedEntry = _Pm1008dcpMesrxfp1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 209, 1)
)
pm1008dcpMesrxfp1ReservedEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrxfp1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1ReservedEntry.setStatus("deprecated")


class _Pm1008dcpMesrxfp1ReservedIndex_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrxfp1ReservedIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1ReservedIndex_Object = MibTableColumn
pm1008dcpMesrxfp1ReservedIndex = _Pm1008dcpMesrxfp1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 209, 1, 1),
    _Pm1008dcpMesrxfp1ReservedIndex_Type()
)
pm1008dcpMesrxfp1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1ReservedIndex.setStatus("deprecated")


class _Pm1008dcpMesrxfp1ReservedPortn_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrxfp1ReservedPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1ReservedPortn_Object = MibTableColumn
pm1008dcpMesrxfp1ReservedPortn = _Pm1008dcpMesrxfp1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 209, 1, 2),
    _Pm1008dcpMesrxfp1ReservedPortn_Type()
)
pm1008dcpMesrxfp1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1ReservedPortn.setStatus("deprecated")
_Pm1008dcpMesrxfp1LoBiasCurrentMeasTable_Object = MibTable
pm1008dcpMesrxfp1LoBiasCurrentMeasTable = _Pm1008dcpMesrxfp1LoBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LoBiasCurrentMeasTable.setStatus("current")
_Pm1008dcpMesrxfp1LoBiasCurrentMeasEntry_Object = MibTableRow
pm1008dcpMesrxfp1LoBiasCurrentMeasEntry = _Pm1008dcpMesrxfp1LoBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 210, 1)
)
pm1008dcpMesrxfp1LoBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrxfp1LoBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LoBiasCurrentMeasEntry.setStatus("current")


class _Pm1008dcpMesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LoBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrxfp1LoBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LoBiasCurrentMeasIndex_Object = MibTableColumn
pm1008dcpMesrxfp1LoBiasCurrentMeasIndex = _Pm1008dcpMesrxfp1LoBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 210, 1, 1),
    _Pm1008dcpMesrxfp1LoBiasCurrentMeasIndex_Type()
)
pm1008dcpMesrxfp1LoBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LoBiasCurrentMeasIndex.setStatus("current")


class _Pm1008dcpMesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LoBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrxfp1LoBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LoBiasCurrentMeasPortn_Object = MibTableColumn
pm1008dcpMesrxfp1LoBiasCurrentMeasPortn = _Pm1008dcpMesrxfp1LoBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 210, 1, 2),
    _Pm1008dcpMesrxfp1LoBiasCurrentMeasPortn_Type()
)
pm1008dcpMesrxfp1LoBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LoBiasCurrentMeasPortn.setStatus("current")
_Pm1008dcpMesrxfp1LoTxPowerMeasTable_Object = MibTable
pm1008dcpMesrxfp1LoTxPowerMeasTable = _Pm1008dcpMesrxfp1LoTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LoTxPowerMeasTable.setStatus("current")
_Pm1008dcpMesrxfp1LoTxPowerMeasEntry_Object = MibTableRow
pm1008dcpMesrxfp1LoTxPowerMeasEntry = _Pm1008dcpMesrxfp1LoTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 211, 1)
)
pm1008dcpMesrxfp1LoTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrxfp1LoTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LoTxPowerMeasEntry.setStatus("current")


class _Pm1008dcpMesrxfp1LoTxPowerMeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LoTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrxfp1LoTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LoTxPowerMeasIndex_Object = MibTableColumn
pm1008dcpMesrxfp1LoTxPowerMeasIndex = _Pm1008dcpMesrxfp1LoTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 211, 1, 1),
    _Pm1008dcpMesrxfp1LoTxPowerMeasIndex_Type()
)
pm1008dcpMesrxfp1LoTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LoTxPowerMeasIndex.setStatus("current")


class _Pm1008dcpMesrxfp1LoTxPowerMeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LoTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrxfp1LoTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LoTxPowerMeasPortn_Object = MibTableColumn
pm1008dcpMesrxfp1LoTxPowerMeasPortn = _Pm1008dcpMesrxfp1LoTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 211, 1, 2),
    _Pm1008dcpMesrxfp1LoTxPowerMeasPortn_Type()
)
pm1008dcpMesrxfp1LoTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LoTxPowerMeasPortn.setStatus("current")
_Pm1008dcpMesrxfp1LiRxPowerMeasTable_Object = MibTable
pm1008dcpMesrxfp1LiRxPowerMeasTable = _Pm1008dcpMesrxfp1LiRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LiRxPowerMeasTable.setStatus("current")
_Pm1008dcpMesrxfp1LiRxPowerMeasEntry_Object = MibTableRow
pm1008dcpMesrxfp1LiRxPowerMeasEntry = _Pm1008dcpMesrxfp1LiRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 212, 1)
)
pm1008dcpMesrxfp1LiRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrxfp1LiRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LiRxPowerMeasEntry.setStatus("current")


class _Pm1008dcpMesrxfp1LiRxPowerMeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LiRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrxfp1LiRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LiRxPowerMeasIndex_Object = MibTableColumn
pm1008dcpMesrxfp1LiRxPowerMeasIndex = _Pm1008dcpMesrxfp1LiRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 212, 1, 1),
    _Pm1008dcpMesrxfp1LiRxPowerMeasIndex_Type()
)
pm1008dcpMesrxfp1LiRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LiRxPowerMeasIndex.setStatus("current")


class _Pm1008dcpMesrxfp1LiRxPowerMeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LiRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrxfp1LiRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LiRxPowerMeasPortn_Object = MibTableColumn
pm1008dcpMesrxfp1LiRxPowerMeasPortn = _Pm1008dcpMesrxfp1LiRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 212, 1, 2),
    _Pm1008dcpMesrxfp1LiRxPowerMeasPortn_Type()
)
pm1008dcpMesrxfp1LiRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LiRxPowerMeasPortn.setStatus("current")
_Pm1008dcpMesrxfp1LxAux1MeasTable_Object = MibTable
pm1008dcpMesrxfp1LxAux1MeasTable = _Pm1008dcpMesrxfp1LxAux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxAux1MeasTable.setStatus("deprecated")
_Pm1008dcpMesrxfp1LxAux1MeasEntry_Object = MibTableRow
pm1008dcpMesrxfp1LxAux1MeasEntry = _Pm1008dcpMesrxfp1LxAux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 213, 1)
)
pm1008dcpMesrxfp1LxAux1MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrxfp1LxAux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxAux1MeasEntry.setStatus("deprecated")


class _Pm1008dcpMesrxfp1LxAux1MeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LxAux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrxfp1LxAux1MeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LxAux1MeasIndex_Object = MibTableColumn
pm1008dcpMesrxfp1LxAux1MeasIndex = _Pm1008dcpMesrxfp1LxAux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 213, 1, 1),
    _Pm1008dcpMesrxfp1LxAux1MeasIndex_Type()
)
pm1008dcpMesrxfp1LxAux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxAux1MeasIndex.setStatus("deprecated")


class _Pm1008dcpMesrxfp1LxAux1MeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LxAux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrxfp1LxAux1MeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LxAux1MeasPortn_Object = MibTableColumn
pm1008dcpMesrxfp1LxAux1MeasPortn = _Pm1008dcpMesrxfp1LxAux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 213, 1, 2),
    _Pm1008dcpMesrxfp1LxAux1MeasPortn_Type()
)
pm1008dcpMesrxfp1LxAux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxAux1MeasPortn.setStatus("deprecated")
_Pm1008dcpMesrxfp1LxAux2MeasTable_Object = MibTable
pm1008dcpMesrxfp1LxAux2MeasTable = _Pm1008dcpMesrxfp1LxAux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxAux2MeasTable.setStatus("deprecated")
_Pm1008dcpMesrxfp1LxAux2MeasEntry_Object = MibTableRow
pm1008dcpMesrxfp1LxAux2MeasEntry = _Pm1008dcpMesrxfp1LxAux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 214, 1)
)
pm1008dcpMesrxfp1LxAux2MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrxfp1LxAux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxAux2MeasEntry.setStatus("deprecated")


class _Pm1008dcpMesrxfp1LxAux2MeasIndex_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LxAux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrxfp1LxAux2MeasIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LxAux2MeasIndex_Object = MibTableColumn
pm1008dcpMesrxfp1LxAux2MeasIndex = _Pm1008dcpMesrxfp1LxAux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 214, 1, 1),
    _Pm1008dcpMesrxfp1LxAux2MeasIndex_Type()
)
pm1008dcpMesrxfp1LxAux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxAux2MeasIndex.setStatus("deprecated")


class _Pm1008dcpMesrxfp1LxAux2MeasPortn_Type(Integer32):
    """Custom type pm1008dcpMesrxfp1LxAux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrxfp1LxAux2MeasPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrxfp1LxAux2MeasPortn_Object = MibTableColumn
pm1008dcpMesrxfp1LxAux2MeasPortn = _Pm1008dcpMesrxfp1LxAux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 214, 1, 2),
    _Pm1008dcpMesrxfp1LxAux2MeasPortn_Type()
)
pm1008dcpMesrxfp1LxAux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrxfp1LxAux2MeasPortn.setStatus("deprecated")
_Pm1008dcpMesrotx1AgingTable_Object = MibTable
pm1008dcpMesrotx1AgingTable = _Pm1008dcpMesrotx1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1AgingTable.setStatus("current")
_Pm1008dcpMesrotx1AgingEntry_Object = MibTableRow
pm1008dcpMesrotx1AgingEntry = _Pm1008dcpMesrotx1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 224, 1)
)
pm1008dcpMesrotx1AgingEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrotx1AgingIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1AgingEntry.setStatus("current")


class _Pm1008dcpMesrotx1AgingIndex_Type(Integer32):
    """Custom type pm1008dcpMesrotx1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrotx1AgingIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrotx1AgingIndex_Object = MibTableColumn
pm1008dcpMesrotx1AgingIndex = _Pm1008dcpMesrotx1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 224, 1, 1),
    _Pm1008dcpMesrotx1AgingIndex_Type()
)
pm1008dcpMesrotx1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1AgingIndex.setStatus("current")


class _Pm1008dcpMesrotx1AgingPortn_Type(Integer32):
    """Custom type pm1008dcpMesrotx1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrotx1AgingPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrotx1AgingPortn_Object = MibTableColumn
pm1008dcpMesrotx1AgingPortn = _Pm1008dcpMesrotx1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 224, 1, 2),
    _Pm1008dcpMesrotx1AgingPortn_Type()
)
pm1008dcpMesrotx1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1AgingPortn.setStatus("current")
_Pm1008dcpMesrotx1LaserTemperatureTable_Object = MibTable
pm1008dcpMesrotx1LaserTemperatureTable = _Pm1008dcpMesrotx1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1LaserTemperatureTable.setStatus("deprecated")
_Pm1008dcpMesrotx1LaserTemperatureEntry_Object = MibTableRow
pm1008dcpMesrotx1LaserTemperatureEntry = _Pm1008dcpMesrotx1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 225, 1)
)
pm1008dcpMesrotx1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrotx1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1LaserTemperatureEntry.setStatus("deprecated")


class _Pm1008dcpMesrotx1LaserTemperatureIndex_Type(Integer32):
    """Custom type pm1008dcpMesrotx1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrotx1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrotx1LaserTemperatureIndex_Object = MibTableColumn
pm1008dcpMesrotx1LaserTemperatureIndex = _Pm1008dcpMesrotx1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 225, 1, 1),
    _Pm1008dcpMesrotx1LaserTemperatureIndex_Type()
)
pm1008dcpMesrotx1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1LaserTemperatureIndex.setStatus("deprecated")


class _Pm1008dcpMesrotx1LaserTemperaturePortn_Type(Integer32):
    """Custom type pm1008dcpMesrotx1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrotx1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrotx1LaserTemperaturePortn_Object = MibTableColumn
pm1008dcpMesrotx1LaserTemperaturePortn = _Pm1008dcpMesrotx1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 225, 1, 2),
    _Pm1008dcpMesrotx1LaserTemperaturePortn_Type()
)
pm1008dcpMesrotx1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1LaserTemperaturePortn.setStatus("deprecated")
_Pm1008dcpMesrotx1FreqDeviationTable_Object = MibTable
pm1008dcpMesrotx1FreqDeviationTable = _Pm1008dcpMesrotx1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1FreqDeviationTable.setStatus("current")
_Pm1008dcpMesrotx1FreqDeviationEntry_Object = MibTableRow
pm1008dcpMesrotx1FreqDeviationEntry = _Pm1008dcpMesrotx1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 226, 1)
)
pm1008dcpMesrotx1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrotx1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1FreqDeviationEntry.setStatus("current")


class _Pm1008dcpMesrotx1FreqDeviationIndex_Type(Integer32):
    """Custom type pm1008dcpMesrotx1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrotx1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrotx1FreqDeviationIndex_Object = MibTableColumn
pm1008dcpMesrotx1FreqDeviationIndex = _Pm1008dcpMesrotx1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 226, 1, 1),
    _Pm1008dcpMesrotx1FreqDeviationIndex_Type()
)
pm1008dcpMesrotx1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1FreqDeviationIndex.setStatus("current")


class _Pm1008dcpMesrotx1FreqDeviationPortn_Type(Integer32):
    """Custom type pm1008dcpMesrotx1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrotx1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrotx1FreqDeviationPortn_Object = MibTableColumn
pm1008dcpMesrotx1FreqDeviationPortn = _Pm1008dcpMesrotx1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 226, 1, 2),
    _Pm1008dcpMesrotx1FreqDeviationPortn_Type()
)
pm1008dcpMesrotx1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1FreqDeviationPortn.setStatus("current")
_Pm1008dcpMesrotx1LaserWvlengthTable_Object = MibTable
pm1008dcpMesrotx1LaserWvlengthTable = _Pm1008dcpMesrotx1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1LaserWvlengthTable.setStatus("current")
_Pm1008dcpMesrotx1LaserWvlengthEntry_Object = MibTableRow
pm1008dcpMesrotx1LaserWvlengthEntry = _Pm1008dcpMesrotx1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 227, 1)
)
pm1008dcpMesrotx1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMesrotx1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1LaserWvlengthEntry.setStatus("current")


class _Pm1008dcpMesrotx1LaserWvlengthIndex_Type(Integer32):
    """Custom type pm1008dcpMesrotx1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMesrotx1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pm1008dcpMesrotx1LaserWvlengthIndex_Object = MibTableColumn
pm1008dcpMesrotx1LaserWvlengthIndex = _Pm1008dcpMesrotx1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 227, 1, 1),
    _Pm1008dcpMesrotx1LaserWvlengthIndex_Type()
)
pm1008dcpMesrotx1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1LaserWvlengthIndex.setStatus("current")


class _Pm1008dcpMesrotx1LaserWvlengthPortn_Type(Integer32):
    """Custom type pm1008dcpMesrotx1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008dcpMesrotx1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pm1008dcpMesrotx1LaserWvlengthPortn_Object = MibTableColumn
pm1008dcpMesrotx1LaserWvlengthPortn = _Pm1008dcpMesrotx1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 3, 3, 227, 1, 2),
    _Pm1008dcpMesrotx1LaserWvlengthPortn_Type()
)
pm1008dcpMesrotx1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMesrotx1LaserWvlengthPortn.setStatus("current")
_Pm1008dcpcounters_ObjectIdentity = ObjectIdentity
pm1008dcpcounters = _Pm1008dcpcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4)
)
_Pm1008dcpCntOther_ObjectIdentity = ObjectIdentity
pm1008dcpCntOther = _Pm1008dcpCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 1)
)
_Pm1008dcpCntClient_ObjectIdentity = ObjectIdentity
pm1008dcpCntClient = _Pm1008dcpCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2)
)
_Pm1008dcpCntupRaRemCntTable_Object = MibTable
pm1008dcpCntupRaRemCntTable = _Pm1008dcpCntupRaRemCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm1008dcpCntupRaRemCntTable.setStatus("current")
_Pm1008dcpCntupRaRemCntEntry_Object = MibTableRow
pm1008dcpCntupRaRemCntEntry = _Pm1008dcpCntupRaRemCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 16, 1)
)
pm1008dcpCntupRaRemCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntupRaRemCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntupRaRemCntEntry.setStatus("current")


class _Pm1008dcpCntupRaRemCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntupRaRemCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntupRaRemCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntupRaRemCntIndex_Object = MibTableColumn
pm1008dcpCntupRaRemCntIndex = _Pm1008dcpCntupRaRemCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 16, 1, 1),
    _Pm1008dcpCntupRaRemCntIndex_Type()
)
pm1008dcpCntupRaRemCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRaRemCntIndex.setStatus("current")
_Pm1008dcpCntupRaRemCntValuePortn_Type = Counter32
_Pm1008dcpCntupRaRemCntValuePortn_Object = MibTableColumn
pm1008dcpCntupRaRemCntValuePortn = _Pm1008dcpCntupRaRemCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 16, 1, 2),
    _Pm1008dcpCntupRaRemCntValuePortn_Type()
)
pm1008dcpCntupRaRemCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRaRemCntValuePortn.setStatus("current")
_Pm1008dcpCntupRaRemCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntupRaRemCntErrorPortn_Object = MibTableColumn
pm1008dcpCntupRaRemCntErrorPortn = _Pm1008dcpCntupRaRemCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 16, 1, 3),
    _Pm1008dcpCntupRaRemCntErrorPortn_Type()
)
pm1008dcpCntupRaRemCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRaRemCntErrorPortn.setStatus("current")
_Pm1008dcpCntupRaRemCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntupRaRemCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntupRaRemCntOverloadPortn = _Pm1008dcpCntupRaRemCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 16, 1, 4),
    _Pm1008dcpCntupRaRemCntOverloadPortn_Type()
)
pm1008dcpCntupRaRemCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRaRemCntOverloadPortn.setStatus("current")
_Pm1008dcpCntupRaInsCntTable_Object = MibTable
pm1008dcpCntupRaInsCntTable = _Pm1008dcpCntupRaInsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 24)
)
if mibBuilder.loadTexts:
    pm1008dcpCntupRaInsCntTable.setStatus("current")
_Pm1008dcpCntupRaInsCntEntry_Object = MibTableRow
pm1008dcpCntupRaInsCntEntry = _Pm1008dcpCntupRaInsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 24, 1)
)
pm1008dcpCntupRaInsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntupRaInsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntupRaInsCntEntry.setStatus("current")


class _Pm1008dcpCntupRaInsCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntupRaInsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntupRaInsCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntupRaInsCntIndex_Object = MibTableColumn
pm1008dcpCntupRaInsCntIndex = _Pm1008dcpCntupRaInsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 24, 1, 1),
    _Pm1008dcpCntupRaInsCntIndex_Type()
)
pm1008dcpCntupRaInsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRaInsCntIndex.setStatus("current")
_Pm1008dcpCntupRaInsCntValuePortn_Type = Counter32
_Pm1008dcpCntupRaInsCntValuePortn_Object = MibTableColumn
pm1008dcpCntupRaInsCntValuePortn = _Pm1008dcpCntupRaInsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 24, 1, 2),
    _Pm1008dcpCntupRaInsCntValuePortn_Type()
)
pm1008dcpCntupRaInsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRaInsCntValuePortn.setStatus("current")
_Pm1008dcpCntupRaInsCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntupRaInsCntErrorPortn_Object = MibTableColumn
pm1008dcpCntupRaInsCntErrorPortn = _Pm1008dcpCntupRaInsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 24, 1, 3),
    _Pm1008dcpCntupRaInsCntErrorPortn_Type()
)
pm1008dcpCntupRaInsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRaInsCntErrorPortn.setStatus("current")
_Pm1008dcpCntupRaInsCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntupRaInsCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntupRaInsCntOverloadPortn = _Pm1008dcpCntupRaInsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 24, 1, 4),
    _Pm1008dcpCntupRaInsCntOverloadPortn_Type()
)
pm1008dcpCntupRaInsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRaInsCntOverloadPortn.setStatus("current")
_Pm1008dcpCntupRdErrCntTable_Object = MibTable
pm1008dcpCntupRdErrCntTable = _Pm1008dcpCntupRdErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm1008dcpCntupRdErrCntTable.setStatus("current")
_Pm1008dcpCntupRdErrCntEntry_Object = MibTableRow
pm1008dcpCntupRdErrCntEntry = _Pm1008dcpCntupRdErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 32, 1)
)
pm1008dcpCntupRdErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntupRdErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntupRdErrCntEntry.setStatus("current")


class _Pm1008dcpCntupRdErrCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntupRdErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntupRdErrCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntupRdErrCntIndex_Object = MibTableColumn
pm1008dcpCntupRdErrCntIndex = _Pm1008dcpCntupRdErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 32, 1, 1),
    _Pm1008dcpCntupRdErrCntIndex_Type()
)
pm1008dcpCntupRdErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRdErrCntIndex.setStatus("current")
_Pm1008dcpCntupRdErrCntValuePortn_Type = Counter32
_Pm1008dcpCntupRdErrCntValuePortn_Object = MibTableColumn
pm1008dcpCntupRdErrCntValuePortn = _Pm1008dcpCntupRdErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 32, 1, 2),
    _Pm1008dcpCntupRdErrCntValuePortn_Type()
)
pm1008dcpCntupRdErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRdErrCntValuePortn.setStatus("current")
_Pm1008dcpCntupRdErrCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntupRdErrCntErrorPortn_Object = MibTableColumn
pm1008dcpCntupRdErrCntErrorPortn = _Pm1008dcpCntupRdErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 32, 1, 3),
    _Pm1008dcpCntupRdErrCntErrorPortn_Type()
)
pm1008dcpCntupRdErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRdErrCntErrorPortn.setStatus("current")
_Pm1008dcpCntupRdErrCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntupRdErrCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntupRdErrCntOverloadPortn = _Pm1008dcpCntupRdErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 32, 1, 4),
    _Pm1008dcpCntupRdErrCntOverloadPortn_Type()
)
pm1008dcpCntupRdErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupRdErrCntOverloadPortn.setStatus("current")
_Pm1008dcpCntupTimCntTable_Object = MibTable
pm1008dcpCntupTimCntTable = _Pm1008dcpCntupTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 40)
)
if mibBuilder.loadTexts:
    pm1008dcpCntupTimCntTable.setStatus("current")
_Pm1008dcpCntupTimCntEntry_Object = MibTableRow
pm1008dcpCntupTimCntEntry = _Pm1008dcpCntupTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 40, 1)
)
pm1008dcpCntupTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntupTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntupTimCntEntry.setStatus("current")


class _Pm1008dcpCntupTimCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntupTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntupTimCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntupTimCntIndex_Object = MibTableColumn
pm1008dcpCntupTimCntIndex = _Pm1008dcpCntupTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 40, 1, 1),
    _Pm1008dcpCntupTimCntIndex_Type()
)
pm1008dcpCntupTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupTimCntIndex.setStatus("current")
_Pm1008dcpCntupTimCntValuePortn_Type = Counter32
_Pm1008dcpCntupTimCntValuePortn_Object = MibTableColumn
pm1008dcpCntupTimCntValuePortn = _Pm1008dcpCntupTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 40, 1, 2),
    _Pm1008dcpCntupTimCntValuePortn_Type()
)
pm1008dcpCntupTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupTimCntValuePortn.setStatus("current")
_Pm1008dcpCntupTimCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntupTimCntErrorPortn_Object = MibTableColumn
pm1008dcpCntupTimCntErrorPortn = _Pm1008dcpCntupTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 40, 1, 3),
    _Pm1008dcpCntupTimCntErrorPortn_Type()
)
pm1008dcpCntupTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupTimCntErrorPortn.setStatus("current")
_Pm1008dcpCntupTimCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntupTimCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntupTimCntOverloadPortn = _Pm1008dcpCntupTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 40, 1, 4),
    _Pm1008dcpCntupTimCntOverloadPortn_Type()
)
pm1008dcpCntupTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupTimCntOverloadPortn.setStatus("current")
_Pm1008dcpCntupCvErrCntTable_Object = MibTable
pm1008dcpCntupCvErrCntTable = _Pm1008dcpCntupCvErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 48)
)
if mibBuilder.loadTexts:
    pm1008dcpCntupCvErrCntTable.setStatus("current")
_Pm1008dcpCntupCvErrCntEntry_Object = MibTableRow
pm1008dcpCntupCvErrCntEntry = _Pm1008dcpCntupCvErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 48, 1)
)
pm1008dcpCntupCvErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntupCvErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntupCvErrCntEntry.setStatus("current")


class _Pm1008dcpCntupCvErrCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntupCvErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntupCvErrCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntupCvErrCntIndex_Object = MibTableColumn
pm1008dcpCntupCvErrCntIndex = _Pm1008dcpCntupCvErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 48, 1, 1),
    _Pm1008dcpCntupCvErrCntIndex_Type()
)
pm1008dcpCntupCvErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupCvErrCntIndex.setStatus("current")
_Pm1008dcpCntupCvErrCntValuePortn_Type = Counter32
_Pm1008dcpCntupCvErrCntValuePortn_Object = MibTableColumn
pm1008dcpCntupCvErrCntValuePortn = _Pm1008dcpCntupCvErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 48, 1, 2),
    _Pm1008dcpCntupCvErrCntValuePortn_Type()
)
pm1008dcpCntupCvErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupCvErrCntValuePortn.setStatus("current")
_Pm1008dcpCntupCvErrCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntupCvErrCntErrorPortn_Object = MibTableColumn
pm1008dcpCntupCvErrCntErrorPortn = _Pm1008dcpCntupCvErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 48, 1, 3),
    _Pm1008dcpCntupCvErrCntErrorPortn_Type()
)
pm1008dcpCntupCvErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupCvErrCntErrorPortn.setStatus("current")
_Pm1008dcpCntupCvErrCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntupCvErrCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntupCvErrCntOverloadPortn = _Pm1008dcpCntupCvErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 48, 1, 4),
    _Pm1008dcpCntupCvErrCntOverloadPortn_Type()
)
pm1008dcpCntupCvErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntupCvErrCntOverloadPortn.setStatus("current")
_Pm1008dcpCntdwCbipCntTable_Object = MibTable
pm1008dcpCntdwCbipCntTable = _Pm1008dcpCntdwCbipCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 64)
)
if mibBuilder.loadTexts:
    pm1008dcpCntdwCbipCntTable.setStatus("current")
_Pm1008dcpCntdwCbipCntEntry_Object = MibTableRow
pm1008dcpCntdwCbipCntEntry = _Pm1008dcpCntdwCbipCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 64, 1)
)
pm1008dcpCntdwCbipCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntdwCbipCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntdwCbipCntEntry.setStatus("current")


class _Pm1008dcpCntdwCbipCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntdwCbipCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntdwCbipCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntdwCbipCntIndex_Object = MibTableColumn
pm1008dcpCntdwCbipCntIndex = _Pm1008dcpCntdwCbipCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 64, 1, 1),
    _Pm1008dcpCntdwCbipCntIndex_Type()
)
pm1008dcpCntdwCbipCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdwCbipCntIndex.setStatus("current")
_Pm1008dcpCntdwCbipCntValuePortn_Type = Counter32
_Pm1008dcpCntdwCbipCntValuePortn_Object = MibTableColumn
pm1008dcpCntdwCbipCntValuePortn = _Pm1008dcpCntdwCbipCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 64, 1, 2),
    _Pm1008dcpCntdwCbipCntValuePortn_Type()
)
pm1008dcpCntdwCbipCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdwCbipCntValuePortn.setStatus("current")
_Pm1008dcpCntdwCbipCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntdwCbipCntErrorPortn_Object = MibTableColumn
pm1008dcpCntdwCbipCntErrorPortn = _Pm1008dcpCntdwCbipCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 64, 1, 3),
    _Pm1008dcpCntdwCbipCntErrorPortn_Type()
)
pm1008dcpCntdwCbipCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdwCbipCntErrorPortn.setStatus("current")
_Pm1008dcpCntdwCbipCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntdwCbipCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntdwCbipCntOverloadPortn = _Pm1008dcpCntdwCbipCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 64, 1, 4),
    _Pm1008dcpCntdwCbipCntOverloadPortn_Type()
)
pm1008dcpCntdwCbipCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdwCbipCntOverloadPortn.setStatus("current")
_Pm1008dcpCntdwTimCntTable_Object = MibTable
pm1008dcpCntdwTimCntTable = _Pm1008dcpCntdwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 72)
)
if mibBuilder.loadTexts:
    pm1008dcpCntdwTimCntTable.setStatus("current")
_Pm1008dcpCntdwTimCntEntry_Object = MibTableRow
pm1008dcpCntdwTimCntEntry = _Pm1008dcpCntdwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 72, 1)
)
pm1008dcpCntdwTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntdwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntdwTimCntEntry.setStatus("current")


class _Pm1008dcpCntdwTimCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntdwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntdwTimCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntdwTimCntIndex_Object = MibTableColumn
pm1008dcpCntdwTimCntIndex = _Pm1008dcpCntdwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 72, 1, 1),
    _Pm1008dcpCntdwTimCntIndex_Type()
)
pm1008dcpCntdwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdwTimCntIndex.setStatus("current")
_Pm1008dcpCntdwTimCntValuePortn_Type = Counter32
_Pm1008dcpCntdwTimCntValuePortn_Object = MibTableColumn
pm1008dcpCntdwTimCntValuePortn = _Pm1008dcpCntdwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 72, 1, 2),
    _Pm1008dcpCntdwTimCntValuePortn_Type()
)
pm1008dcpCntdwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdwTimCntValuePortn.setStatus("current")
_Pm1008dcpCntdwTimCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntdwTimCntErrorPortn_Object = MibTableColumn
pm1008dcpCntdwTimCntErrorPortn = _Pm1008dcpCntdwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 72, 1, 3),
    _Pm1008dcpCntdwTimCntErrorPortn_Type()
)
pm1008dcpCntdwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdwTimCntErrorPortn.setStatus("current")
_Pm1008dcpCntdwTimCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntdwTimCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntdwTimCntOverloadPortn = _Pm1008dcpCntdwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 2, 72, 1, 4),
    _Pm1008dcpCntdwTimCntOverloadPortn_Type()
)
pm1008dcpCntdwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdwTimCntOverloadPortn.setStatus("current")
_Pm1008dcpCntLine_ObjectIdentity = ObjectIdentity
pm1008dcpCntLine = _Pm1008dcpCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3)
)
_Pm1008dcpCntdfrmB1ErrCntTable_Object = MibTable
pm1008dcpCntdfrmB1ErrCntTable = _Pm1008dcpCntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmB1ErrCntTable.setStatus("current")
_Pm1008dcpCntdfrmB1ErrCntEntry_Object = MibTableRow
pm1008dcpCntdfrmB1ErrCntEntry = _Pm1008dcpCntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 152, 1)
)
pm1008dcpCntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmB1ErrCntEntry.setStatus("current")


class _Pm1008dcpCntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntdfrmB1ErrCntIndex_Object = MibTableColumn
pm1008dcpCntdfrmB1ErrCntIndex = _Pm1008dcpCntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 152, 1, 1),
    _Pm1008dcpCntdfrmB1ErrCntIndex_Type()
)
pm1008dcpCntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmB1ErrCntIndex.setStatus("current")
_Pm1008dcpCntdfrmB1ErrCntValuePortn_Type = Counter32
_Pm1008dcpCntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pm1008dcpCntdfrmB1ErrCntValuePortn = _Pm1008dcpCntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 152, 1, 2),
    _Pm1008dcpCntdfrmB1ErrCntValuePortn_Type()
)
pm1008dcpCntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmB1ErrCntValuePortn.setStatus("current")
_Pm1008dcpCntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm1008dcpCntdfrmB1ErrCntErrorPortn = _Pm1008dcpCntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 152, 1, 3),
    _Pm1008dcpCntdfrmB1ErrCntErrorPortn_Type()
)
pm1008dcpCntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pm1008dcpCntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntdfrmB1ErrCntOverloadPortn = _Pm1008dcpCntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 152, 1, 4),
    _Pm1008dcpCntdfrmB1ErrCntOverloadPortn_Type()
)
pm1008dcpCntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm1008dcpCntdfrmTimCntTable_Object = MibTable
pm1008dcpCntdfrmTimCntTable = _Pm1008dcpCntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmTimCntTable.setStatus("current")
_Pm1008dcpCntdfrmTimCntEntry_Object = MibTableRow
pm1008dcpCntdfrmTimCntEntry = _Pm1008dcpCntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 153, 1)
)
pm1008dcpCntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmTimCntEntry.setStatus("current")


class _Pm1008dcpCntdfrmTimCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntdfrmTimCntIndex_Object = MibTableColumn
pm1008dcpCntdfrmTimCntIndex = _Pm1008dcpCntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 153, 1, 1),
    _Pm1008dcpCntdfrmTimCntIndex_Type()
)
pm1008dcpCntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmTimCntIndex.setStatus("current")
_Pm1008dcpCntdfrmTimCntValuePortn_Type = Counter32
_Pm1008dcpCntdfrmTimCntValuePortn_Object = MibTableColumn
pm1008dcpCntdfrmTimCntValuePortn = _Pm1008dcpCntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 153, 1, 2),
    _Pm1008dcpCntdfrmTimCntValuePortn_Type()
)
pm1008dcpCntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmTimCntValuePortn.setStatus("current")
_Pm1008dcpCntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntdfrmTimCntErrorPortn_Object = MibTableColumn
pm1008dcpCntdfrmTimCntErrorPortn = _Pm1008dcpCntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 153, 1, 3),
    _Pm1008dcpCntdfrmTimCntErrorPortn_Type()
)
pm1008dcpCntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmTimCntErrorPortn.setStatus("current")
_Pm1008dcpCntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntdfrmTimCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntdfrmTimCntOverloadPortn = _Pm1008dcpCntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 153, 1, 4),
    _Pm1008dcpCntdfrmTimCntOverloadPortn_Type()
)
pm1008dcpCntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmTimCntOverloadPortn.setStatus("current")
_Pm1008dcpCntdfrmPrimLineErrCntTable_Object = MibTable
pm1008dcpCntdfrmPrimLineErrCntTable = _Pm1008dcpCntdfrmPrimLineErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 154)
)
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmPrimLineErrCntTable.setStatus("current")
_Pm1008dcpCntdfrmPrimLineErrCntEntry_Object = MibTableRow
pm1008dcpCntdfrmPrimLineErrCntEntry = _Pm1008dcpCntdfrmPrimLineErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 154, 1)
)
pm1008dcpCntdfrmPrimLineErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCntdfrmPrimLineErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmPrimLineErrCntEntry.setStatus("current")


class _Pm1008dcpCntdfrmPrimLineErrCntIndex_Type(Integer32):
    """Custom type pm1008dcpCntdfrmPrimLineErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCntdfrmPrimLineErrCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpCntdfrmPrimLineErrCntIndex_Object = MibTableColumn
pm1008dcpCntdfrmPrimLineErrCntIndex = _Pm1008dcpCntdfrmPrimLineErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 154, 1, 1),
    _Pm1008dcpCntdfrmPrimLineErrCntIndex_Type()
)
pm1008dcpCntdfrmPrimLineErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmPrimLineErrCntIndex.setStatus("current")
_Pm1008dcpCntdfrmPrimLineErrCntValuePortn_Type = Counter32
_Pm1008dcpCntdfrmPrimLineErrCntValuePortn_Object = MibTableColumn
pm1008dcpCntdfrmPrimLineErrCntValuePortn = _Pm1008dcpCntdfrmPrimLineErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 154, 1, 2),
    _Pm1008dcpCntdfrmPrimLineErrCntValuePortn_Type()
)
pm1008dcpCntdfrmPrimLineErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmPrimLineErrCntValuePortn.setStatus("current")
_Pm1008dcpCntdfrmPrimLineErrCntErrorPortn_Type = EkiOnOff
_Pm1008dcpCntdfrmPrimLineErrCntErrorPortn_Object = MibTableColumn
pm1008dcpCntdfrmPrimLineErrCntErrorPortn = _Pm1008dcpCntdfrmPrimLineErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 154, 1, 3),
    _Pm1008dcpCntdfrmPrimLineErrCntErrorPortn_Type()
)
pm1008dcpCntdfrmPrimLineErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmPrimLineErrCntErrorPortn.setStatus("current")
_Pm1008dcpCntdfrmPrimLineErrCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpCntdfrmPrimLineErrCntOverloadPortn_Object = MibTableColumn
pm1008dcpCntdfrmPrimLineErrCntOverloadPortn = _Pm1008dcpCntdfrmPrimLineErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 3, 154, 1, 4),
    _Pm1008dcpCntdfrmPrimLineErrCntOverloadPortn_Type()
)
pm1008dcpCntdfrmPrimLineErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCntdfrmPrimLineErrCntOverloadPortn.setStatus("current")
_Pm1008dcpCntCountersReset_Type = EkiOnOff
_Pm1008dcpCntCountersReset_Object = MibScalar
pm1008dcpCntCountersReset = _Pm1008dcpCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 259),
    _Pm1008dcpCntCountersReset_Type()
)
pm1008dcpCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCntCountersReset.setStatus("current")
_Pm1008dcpCntCountersStop_Type = EkiOnOff
_Pm1008dcpCntCountersStop_Object = MibScalar
pm1008dcpCntCountersStop = _Pm1008dcpCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 4, 260),
    _Pm1008dcpCntCountersStop_Type()
)
pm1008dcpCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCntCountersStop.setStatus("current")
_Pm1008dcpcontrolsWrite_ObjectIdentity = ObjectIdentity
pm1008dcpcontrolsWrite = _Pm1008dcpcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6)
)
_Pm1008dcpCtrlOther_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlOther = _Pm1008dcpCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1)
)
_Pm1008dcpCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlconfMgnt1 = _Pm1008dcpCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 1)
)
_Pm1008dcpCtrlConf1Load1_Type = EkiOnOff
_Pm1008dcpCtrlConf1Load1_Object = MibScalar
pm1008dcpCtrlConf1Load1 = _Pm1008dcpCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 1, 1),
    _Pm1008dcpCtrlConf1Load1_Type()
)
pm1008dcpCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlConf1Load1.setStatus("current")
_Pm1008dcpCtrlConf2Load1_Type = EkiOnOff
_Pm1008dcpCtrlConf2Load1_Object = MibScalar
pm1008dcpCtrlConf2Load1 = _Pm1008dcpCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 1, 2),
    _Pm1008dcpCtrlConf2Load1_Type()
)
pm1008dcpCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlConf2Load1.setStatus("current")
_Pm1008dcpCtrlConf2Flash1_Type = EkiOnOff
_Pm1008dcpCtrlConf2Flash1_Object = MibScalar
pm1008dcpCtrlConf2Flash1 = _Pm1008dcpCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 1, 10),
    _Pm1008dcpCtrlConf2Flash1_Type()
)
pm1008dcpCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlConf2Flash1.setStatus("current")
_Pm1008dcpCtrlConf2Clear1_Type = EkiOnOff
_Pm1008dcpCtrlConf2Clear1_Object = MibScalar
pm1008dcpCtrlConf2Clear1 = _Pm1008dcpCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 1, 14),
    _Pm1008dcpCtrlConf2Clear1_Type()
)
pm1008dcpCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlConf2Clear1.setStatus("current")
_Pm1008dcpCtrlsynth4_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlsynth4 = _Pm1008dcpCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 4)
)
_Pm1008dcpCtrlCorrelatOn_Type = EkiOnOff
_Pm1008dcpCtrlCorrelatOn_Object = MibScalar
pm1008dcpCtrlCorrelatOn = _Pm1008dcpCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 4, 1),
    _Pm1008dcpCtrlCorrelatOn_Type()
)
pm1008dcpCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlCorrelatOn.setStatus("current")
_Pm1008dcpCtrlCorrelatOff_Type = EkiOnOff
_Pm1008dcpCtrlCorrelatOff_Object = MibScalar
pm1008dcpCtrlCorrelatOff = _Pm1008dcpCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 4, 2),
    _Pm1008dcpCtrlCorrelatOff_Type()
)
pm1008dcpCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlCorrelatOff.setStatus("current")
_Pm1008dcpCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlswMgnt = _Pm1008dcpCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 5)
)
_Pm1008dcpCtrlColdReset_Type = EkiOnOff
_Pm1008dcpCtrlColdReset_Object = MibScalar
pm1008dcpCtrlColdReset = _Pm1008dcpCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 5, 2),
    _Pm1008dcpCtrlColdReset_Type()
)
pm1008dcpCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlColdReset.setStatus("current")
_Pm1008dcpCtrlWarmReset_Type = EkiOnOff
_Pm1008dcpCtrlWarmReset_Object = MibScalar
pm1008dcpCtrlWarmReset = _Pm1008dcpCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 5, 3),
    _Pm1008dcpCtrlWarmReset_Type()
)
pm1008dcpCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlWarmReset.setStatus("current")
_Pm1008dcpCtrlLoadSwBank1_Type = EkiOnOff
_Pm1008dcpCtrlLoadSwBank1_Object = MibScalar
pm1008dcpCtrlLoadSwBank1 = _Pm1008dcpCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 5, 5),
    _Pm1008dcpCtrlLoadSwBank1_Type()
)
pm1008dcpCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlLoadSwBank1.setStatus("current")
_Pm1008dcpCtrlLoadSwBank2_Type = EkiOnOff
_Pm1008dcpCtrlLoadSwBank2_Object = MibScalar
pm1008dcpCtrlLoadSwBank2 = _Pm1008dcpCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 5, 6),
    _Pm1008dcpCtrlLoadSwBank2_Type()
)
pm1008dcpCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlLoadSwBank2.setStatus("current")
_Pm1008dcpCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlgwMgnt = _Pm1008dcpCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 6)
)
_Pm1008dcpCtrlCurrentGwReset_Type = EkiOnOff
_Pm1008dcpCtrlCurrentGwReset_Object = MibScalar
pm1008dcpCtrlCurrentGwReset = _Pm1008dcpCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 6, 1),
    _Pm1008dcpCtrlCurrentGwReset_Type()
)
pm1008dcpCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlCurrentGwReset.setStatus("current")
_Pm1008dcpCtrlLoadGwBank1_Type = EkiOnOff
_Pm1008dcpCtrlLoadGwBank1_Object = MibScalar
pm1008dcpCtrlLoadGwBank1 = _Pm1008dcpCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 6, 5),
    _Pm1008dcpCtrlLoadGwBank1_Type()
)
pm1008dcpCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlLoadGwBank1.setStatus("current")
_Pm1008dcpCtrlLoadGwBank2_Type = EkiOnOff
_Pm1008dcpCtrlLoadGwBank2_Object = MibScalar
pm1008dcpCtrlLoadGwBank2 = _Pm1008dcpCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 6, 6),
    _Pm1008dcpCtrlLoadGwBank2_Type()
)
pm1008dcpCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlLoadGwBank2.setStatus("current")
_Pm1008dcpCtrlLoadGwBank3_Type = EkiOnOff
_Pm1008dcpCtrlLoadGwBank3_Object = MibScalar
pm1008dcpCtrlLoadGwBank3 = _Pm1008dcpCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 6, 7),
    _Pm1008dcpCtrlLoadGwBank3_Type()
)
pm1008dcpCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlLoadGwBank3.setStatus("current")
_Pm1008dcpCtrlLoadGwBank4_Type = EkiOnOff
_Pm1008dcpCtrlLoadGwBank4_Object = MibScalar
pm1008dcpCtrlLoadGwBank4 = _Pm1008dcpCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 6, 8),
    _Pm1008dcpCtrlLoadGwBank4_Type()
)
pm1008dcpCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlLoadGwBank4.setStatus("current")
_Pm1008dcpCtrlledTest_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlledTest = _Pm1008dcpCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 192)
)
_Pm1008dcpCtrlGreenLed_Type = EkiOnOff
_Pm1008dcpCtrlGreenLed_Object = MibScalar
pm1008dcpCtrlGreenLed = _Pm1008dcpCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 192, 1),
    _Pm1008dcpCtrlGreenLed_Type()
)
pm1008dcpCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlGreenLed.setStatus("current")
_Pm1008dcpCtrlRedLed_Type = EkiOnOff
_Pm1008dcpCtrlRedLed_Object = MibScalar
pm1008dcpCtrlRedLed = _Pm1008dcpCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 192, 2),
    _Pm1008dcpCtrlRedLed_Type()
)
pm1008dcpCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlRedLed.setStatus("current")
_Pm1008dcpCtrlLedOff_Type = EkiOnOff
_Pm1008dcpCtrlLedOff_Object = MibScalar
pm1008dcpCtrlLedOff = _Pm1008dcpCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 192, 3),
    _Pm1008dcpCtrlLedOff_Type()
)
pm1008dcpCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlLedOff.setStatus("current")
_Pm1008dcpCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlmoduleOosMode = _Pm1008dcpCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 193)
)
_Pm1008dcpCtrlModuleOosMode_Type = EkiOnOff
_Pm1008dcpCtrlModuleOosMode_Object = MibScalar
pm1008dcpCtrlModuleOosMode = _Pm1008dcpCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 193, 1),
    _Pm1008dcpCtrlModuleOosMode_Type()
)
pm1008dcpCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlModuleOosMode.setStatus("current")
_Pm1008dcpCtrlmoduleDccMgnt_Type = Pm1008dcpDccMode
_Pm1008dcpCtrlmoduleDccMgnt_Object = MibScalar
pm1008dcpCtrlmoduleDccMgnt = _Pm1008dcpCtrlmoduleDccMgnt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 196),
    _Pm1008dcpCtrlmoduleDccMgnt_Type()
)
pm1008dcpCtrlmoduleDccMgnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlmoduleDccMgnt.setStatus("current")
_Pm1008dcpCtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlmaintenanceMode = _Pm1008dcpCtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 197)
)
_Pm1008dcpCtrlMaintenanceMode_Type = EkiOnOff
_Pm1008dcpCtrlMaintenanceMode_Object = MibScalar
pm1008dcpCtrlMaintenanceMode = _Pm1008dcpCtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 1, 197, 1),
    _Pm1008dcpCtrlMaintenanceMode_Type()
)
pm1008dcpCtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlMaintenanceMode.setStatus("current")
_Pm1008dcpCtrlClient_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlClient = _Pm1008dcpCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2)
)
_Pm1008dcpCtrlaccessLoopTable_Object = MibTable
pm1008dcpCtrlaccessLoopTable = _Pm1008dcpCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlaccessLoopTable.setStatus("current")
_Pm1008dcpCtrlaccessLoopEntry_Object = MibTableRow
pm1008dcpCtrlaccessLoopEntry = _Pm1008dcpCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 16, 1)
)
pm1008dcpCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlaccessLoopEntry.setStatus("current")


class _Pm1008dcpCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlaccessLoopIndex_Object = MibTableColumn
pm1008dcpCtrlaccessLoopIndex = _Pm1008dcpCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 16, 1, 1),
    _Pm1008dcpCtrlaccessLoopIndex_Type()
)
pm1008dcpCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlaccessLoopIndex.setStatus("current")
_Pm1008dcpCtrlaccessLoopPortn_Type = EkiState
_Pm1008dcpCtrlaccessLoopPortn_Object = MibTableColumn
pm1008dcpCtrlaccessLoopPortn = _Pm1008dcpCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 16, 1, 2),
    _Pm1008dcpCtrlaccessLoopPortn_Type()
)
pm1008dcpCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlaccessLoopPortn.setStatus("current")
_Pm1008dcpCtrlportOosModeTable_Object = MibTable
pm1008dcpCtrlportOosModeTable = _Pm1008dcpCtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlportOosModeTable.setStatus("current")
_Pm1008dcpCtrlportOosModeEntry_Object = MibTableRow
pm1008dcpCtrlportOosModeEntry = _Pm1008dcpCtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 18, 1)
)
pm1008dcpCtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlportOosModeEntry.setStatus("current")


class _Pm1008dcpCtrlportOosModeIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlportOosModeIndex_Object = MibTableColumn
pm1008dcpCtrlportOosModeIndex = _Pm1008dcpCtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 18, 1, 1),
    _Pm1008dcpCtrlportOosModeIndex_Type()
)
pm1008dcpCtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlportOosModeIndex.setStatus("current")
_Pm1008dcpCtrlportOosModePortn_Type = EkiState
_Pm1008dcpCtrlportOosModePortn_Object = MibTableColumn
pm1008dcpCtrlportOosModePortn = _Pm1008dcpCtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 18, 1, 2),
    _Pm1008dcpCtrlportOosModePortn_Type()
)
pm1008dcpCtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlportOosModePortn.setStatus("current")
_Pm1008dcpCtrlsfpOnCtrlTable_Object = MibTable
pm1008dcpCtrlsfpOnCtrlTable = _Pm1008dcpCtrlsfpOnCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 19)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlsfpOnCtrlTable.setStatus("current")
_Pm1008dcpCtrlsfpOnCtrlEntry_Object = MibTableRow
pm1008dcpCtrlsfpOnCtrlEntry = _Pm1008dcpCtrlsfpOnCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 19, 1)
)
pm1008dcpCtrlsfpOnCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlsfpOnCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlsfpOnCtrlEntry.setStatus("current")


class _Pm1008dcpCtrlsfpOnCtrlIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlsfpOnCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlsfpOnCtrlIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlsfpOnCtrlIndex_Object = MibTableColumn
pm1008dcpCtrlsfpOnCtrlIndex = _Pm1008dcpCtrlsfpOnCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 19, 1, 1),
    _Pm1008dcpCtrlsfpOnCtrlIndex_Type()
)
pm1008dcpCtrlsfpOnCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlsfpOnCtrlIndex.setStatus("current")
_Pm1008dcpCtrlsfpOnCtrlPortn_Type = EkiState
_Pm1008dcpCtrlsfpOnCtrlPortn_Object = MibTableColumn
pm1008dcpCtrlsfpOnCtrlPortn = _Pm1008dcpCtrlsfpOnCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 19, 1, 2),
    _Pm1008dcpCtrlsfpOnCtrlPortn_Type()
)
pm1008dcpCtrlsfpOnCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlsfpOnCtrlPortn.setStatus("current")
_Pm1008dcpCtrlsfpOffCtrlTable_Object = MibTable
pm1008dcpCtrlsfpOffCtrlTable = _Pm1008dcpCtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlsfpOffCtrlTable.setStatus("current")
_Pm1008dcpCtrlsfpOffCtrlEntry_Object = MibTableRow
pm1008dcpCtrlsfpOffCtrlEntry = _Pm1008dcpCtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 20, 1)
)
pm1008dcpCtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlsfpOffCtrlEntry.setStatus("current")


class _Pm1008dcpCtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlsfpOffCtrlIndex_Object = MibTableColumn
pm1008dcpCtrlsfpOffCtrlIndex = _Pm1008dcpCtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 20, 1, 1),
    _Pm1008dcpCtrlsfpOffCtrlIndex_Type()
)
pm1008dcpCtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlsfpOffCtrlIndex.setStatus("current")
_Pm1008dcpCtrlsfpOffCtrlPortn_Type = EkiState
_Pm1008dcpCtrlsfpOffCtrlPortn_Object = MibTableColumn
pm1008dcpCtrlsfpOffCtrlPortn = _Pm1008dcpCtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 20, 1, 2),
    _Pm1008dcpCtrlsfpOffCtrlPortn_Type()
)
pm1008dcpCtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlsfpOffCtrlPortn.setStatus("current")
_Pm1008dcpCtrlcsfUpInsTable_Object = MibTable
pm1008dcpCtrlcsfUpInsTable = _Pm1008dcpCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlcsfUpInsTable.setStatus("current")
_Pm1008dcpCtrlcsfUpInsEntry_Object = MibTableRow
pm1008dcpCtrlcsfUpInsEntry = _Pm1008dcpCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 21, 1)
)
pm1008dcpCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlcsfUpInsEntry.setStatus("current")


class _Pm1008dcpCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlcsfUpInsIndex_Object = MibTableColumn
pm1008dcpCtrlcsfUpInsIndex = _Pm1008dcpCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 21, 1, 1),
    _Pm1008dcpCtrlcsfUpInsIndex_Type()
)
pm1008dcpCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlcsfUpInsIndex.setStatus("current")
_Pm1008dcpCtrlcsfUpInsPortn_Type = EkiState
_Pm1008dcpCtrlcsfUpInsPortn_Object = MibTableColumn
pm1008dcpCtrlcsfUpInsPortn = _Pm1008dcpCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 21, 1, 2),
    _Pm1008dcpCtrlcsfUpInsPortn_Type()
)
pm1008dcpCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlcsfUpInsPortn.setStatus("current")
_Pm1008dcpCtrlcaisDwInsTable_Object = MibTable
pm1008dcpCtrlcaisDwInsTable = _Pm1008dcpCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlcaisDwInsTable.setStatus("current")
_Pm1008dcpCtrlcaisDwInsEntry_Object = MibTableRow
pm1008dcpCtrlcaisDwInsEntry = _Pm1008dcpCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 22, 1)
)
pm1008dcpCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlcaisDwInsEntry.setStatus("current")


class _Pm1008dcpCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlcaisDwInsIndex_Object = MibTableColumn
pm1008dcpCtrlcaisDwInsIndex = _Pm1008dcpCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 22, 1, 1),
    _Pm1008dcpCtrlcaisDwInsIndex_Type()
)
pm1008dcpCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlcaisDwInsIndex.setStatus("current")
_Pm1008dcpCtrlcaisDwInsPortn_Type = EkiState
_Pm1008dcpCtrlcaisDwInsPortn_Object = MibTableColumn
pm1008dcpCtrlcaisDwInsPortn = _Pm1008dcpCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 22, 1, 2),
    _Pm1008dcpCtrlcaisDwInsPortn_Type()
)
pm1008dcpCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlcaisDwInsPortn.setStatus("current")
_Pm1008dcpCtrlclientAccessTermLoopTable_Object = MibTable
pm1008dcpCtrlclientAccessTermLoopTable = _Pm1008dcpCtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlclientAccessTermLoopTable.setStatus("current")
_Pm1008dcpCtrlclientAccessTermLoopEntry_Object = MibTableRow
pm1008dcpCtrlclientAccessTermLoopEntry = _Pm1008dcpCtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 26, 1)
)
pm1008dcpCtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm1008dcpCtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm1008dcpCtrlclientAccessTermLoopIndex = _Pm1008dcpCtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 26, 1, 1),
    _Pm1008dcpCtrlclientAccessTermLoopIndex_Type()
)
pm1008dcpCtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlclientAccessTermLoopIndex.setStatus("current")
_Pm1008dcpCtrlclientAccessTermLoopPortn_Type = EkiState
_Pm1008dcpCtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm1008dcpCtrlclientAccessTermLoopPortn = _Pm1008dcpCtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 26, 1, 2),
    _Pm1008dcpCtrlclientAccessTermLoopPortn_Type()
)
pm1008dcpCtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlclientAccessTermLoopPortn.setStatus("current")
_Pm1008dcpCtrlprotocolTable_Object = MibTable
pm1008dcpCtrlprotocolTable = _Pm1008dcpCtrlprotocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 48)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlprotocolTable.setStatus("current")
_Pm1008dcpCtrlprotocolEntry_Object = MibTableRow
pm1008dcpCtrlprotocolEntry = _Pm1008dcpCtrlprotocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 48, 1)
)
pm1008dcpCtrlprotocolEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlprotocolIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlprotocolEntry.setStatus("current")


class _Pm1008dcpCtrlprotocolIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlprotocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlprotocolIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlprotocolIndex_Object = MibTableColumn
pm1008dcpCtrlprotocolIndex = _Pm1008dcpCtrlprotocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 48, 1, 1),
    _Pm1008dcpCtrlprotocolIndex_Type()
)
pm1008dcpCtrlprotocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlprotocolIndex.setStatus("current")
_Pm1008dcpCtrlprotocolPortn_Type = EkiProtocol
_Pm1008dcpCtrlprotocolPortn_Object = MibTableColumn
pm1008dcpCtrlprotocolPortn = _Pm1008dcpCtrlprotocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 48, 1, 2),
    _Pm1008dcpCtrlprotocolPortn_Type()
)
pm1008dcpCtrlprotocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlprotocolPortn.setStatus("current")
_Pm1008dcpCtrladddropTsClientARxProtectTable_Object = MibTable
pm1008dcpCtrladddropTsClientARxProtectTable = _Pm1008dcpCtrladddropTsClientARxProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 128)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrladddropTsClientARxProtectTable.setStatus("current")
_Pm1008dcpCtrladddropTsClientARxProtectEntry_Object = MibTableRow
pm1008dcpCtrladddropTsClientARxProtectEntry = _Pm1008dcpCtrladddropTsClientARxProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 128, 1)
)
pm1008dcpCtrladddropTsClientARxProtectEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrladddropTsClientARxProtectIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrladddropTsClientARxProtectEntry.setStatus("current")


class _Pm1008dcpCtrladddropTsClientARxProtectIndex_Type(Integer32):
    """Custom type pm1008dcpCtrladddropTsClientARxProtectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrladddropTsClientARxProtectIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrladddropTsClientARxProtectIndex_Object = MibTableColumn
pm1008dcpCtrladddropTsClientARxProtectIndex = _Pm1008dcpCtrladddropTsClientARxProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 128, 1, 1),
    _Pm1008dcpCtrladddropTsClientARxProtectIndex_Type()
)
pm1008dcpCtrladddropTsClientARxProtectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrladddropTsClientARxProtectIndex.setStatus("current")
_Pm1008dcpCtrladddropTsClientARxProtectPortn_Type = Pm1008dcpProtectionTimeSlot
_Pm1008dcpCtrladddropTsClientARxProtectPortn_Object = MibTableColumn
pm1008dcpCtrladddropTsClientARxProtectPortn = _Pm1008dcpCtrladddropTsClientARxProtectPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 128, 1, 2),
    _Pm1008dcpCtrladddropTsClientARxProtectPortn_Type()
)
pm1008dcpCtrladddropTsClientARxProtectPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrladddropTsClientARxProtectPortn.setStatus("current")
_Pm1008dcpCtrladddropTsPairModeTable_Object = MibTable
pm1008dcpCtrladddropTsPairModeTable = _Pm1008dcpCtrladddropTsPairModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 136)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrladddropTsPairModeTable.setStatus("current")
_Pm1008dcpCtrladddropTsPairModeEntry_Object = MibTableRow
pm1008dcpCtrladddropTsPairModeEntry = _Pm1008dcpCtrladddropTsPairModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 136, 1)
)
pm1008dcpCtrladddropTsPairModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrladddropTsPairModeIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrladddropTsPairModeEntry.setStatus("current")


class _Pm1008dcpCtrladddropTsPairModeIndex_Type(Integer32):
    """Custom type pm1008dcpCtrladddropTsPairModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrladddropTsPairModeIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrladddropTsPairModeIndex_Object = MibTableColumn
pm1008dcpCtrladddropTsPairModeIndex = _Pm1008dcpCtrladddropTsPairModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 136, 1, 1),
    _Pm1008dcpCtrladddropTsPairModeIndex_Type()
)
pm1008dcpCtrladddropTsPairModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrladddropTsPairModeIndex.setStatus("current")
_Pm1008dcpCtrladddropTsPairModePortn_Type = Pm1008dcpModeTimeSlot
_Pm1008dcpCtrladddropTsPairModePortn_Object = MibTableColumn
pm1008dcpCtrladddropTsPairModePortn = _Pm1008dcpCtrladddropTsPairModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 2, 136, 1, 2),
    _Pm1008dcpCtrladddropTsPairModePortn_Type()
)
pm1008dcpCtrladddropTsPairModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrladddropTsPairModePortn.setStatus("current")
_Pm1008dcpCtrlLine_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlLine = _Pm1008dcpCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3)
)
_Pm1008dcpCtrlcommAccessLoop_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlcommAccessLoop = _Pm1008dcpCtrlcommAccessLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 64)
)
_Pm1008dcpCtrlCommAccessloop_Type = EkiOnOff
_Pm1008dcpCtrlCommAccessloop_Object = MibScalar
pm1008dcpCtrlCommAccessloop = _Pm1008dcpCtrlCommAccessloop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 64, 1),
    _Pm1008dcpCtrlCommAccessloop_Type()
)
pm1008dcpCtrlCommAccessloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlCommAccessloop.setStatus("deprecated")
_Pm1008dcpCtrllineLoop_ObjectIdentity = ObjectIdentity
pm1008dcpCtrllineLoop = _Pm1008dcpCtrllineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 66)
)
_Pm1008dcpCtrlLineLoop_Type = EkiOnOff
_Pm1008dcpCtrlLineLoop_Object = MibScalar
pm1008dcpCtrlLineLoop = _Pm1008dcpCtrlLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 66, 1),
    _Pm1008dcpCtrlLineLoop_Type()
)
pm1008dcpCtrlLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlLineLoop.setStatus("deprecated")
_Pm1008dcpCtrlmsAis_ObjectIdentity = ObjectIdentity
pm1008dcpCtrlmsAis = _Pm1008dcpCtrlmsAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 67)
)
_Pm1008dcpCtrlMsAis_Type = EkiOnOff
_Pm1008dcpCtrlMsAis_Object = MibScalar
pm1008dcpCtrlMsAis = _Pm1008dcpCtrlMsAis_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 67, 1),
    _Pm1008dcpCtrlMsAis_Type()
)
pm1008dcpCtrlMsAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlMsAis.setStatus("current")
_Pm1008dcpCtrlfecDisableTable_Object = MibTable
pm1008dcpCtrlfecDisableTable = _Pm1008dcpCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlfecDisableTable.setStatus("current")
_Pm1008dcpCtrlfecDisableEntry_Object = MibTableRow
pm1008dcpCtrlfecDisableEntry = _Pm1008dcpCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 69, 1)
)
pm1008dcpCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlfecDisableEntry.setStatus("current")


class _Pm1008dcpCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlfecDisableIndex_Object = MibTableColumn
pm1008dcpCtrlfecDisableIndex = _Pm1008dcpCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 69, 1, 1),
    _Pm1008dcpCtrlfecDisableIndex_Type()
)
pm1008dcpCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlfecDisableIndex.setStatus("current")
_Pm1008dcpCtrlfecDisablePortn_Type = EkiState
_Pm1008dcpCtrlfecDisablePortn_Object = MibTableColumn
pm1008dcpCtrlfecDisablePortn = _Pm1008dcpCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 69, 1, 2),
    _Pm1008dcpCtrlfecDisablePortn_Type()
)
pm1008dcpCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlfecDisablePortn.setStatus("current")
_Pm1008dcpCtrllineOosModeTable_Object = MibTable
pm1008dcpCtrllineOosModeTable = _Pm1008dcpCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllineOosModeTable.setStatus("current")
_Pm1008dcpCtrllineOosModeEntry_Object = MibTableRow
pm1008dcpCtrllineOosModeEntry = _Pm1008dcpCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 74, 1)
)
pm1008dcpCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllineOosModeEntry.setStatus("current")


class _Pm1008dcpCtrllineOosModeIndex_Type(Integer32):
    """Custom type pm1008dcpCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrllineOosModeIndex_Object = MibTableColumn
pm1008dcpCtrllineOosModeIndex = _Pm1008dcpCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 74, 1, 1),
    _Pm1008dcpCtrllineOosModeIndex_Type()
)
pm1008dcpCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrllineOosModeIndex.setStatus("current")
_Pm1008dcpCtrllineOosModePortn_Type = EkiState
_Pm1008dcpCtrllineOosModePortn_Object = MibTableColumn
pm1008dcpCtrllineOosModePortn = _Pm1008dcpCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 74, 1, 2),
    _Pm1008dcpCtrllineOosModePortn_Type()
)
pm1008dcpCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrllineOosModePortn.setStatus("current")
_Pm1008dcpCtrlxfpOnoffTable_Object = MibTable
pm1008dcpCtrlxfpOnoffTable = _Pm1008dcpCtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpOnoffTable.setStatus("current")
_Pm1008dcpCtrlxfpOnoffEntry_Object = MibTableRow
pm1008dcpCtrlxfpOnoffEntry = _Pm1008dcpCtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 208, 1)
)
pm1008dcpCtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpOnoffEntry.setStatus("current")


class _Pm1008dcpCtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlxfpOnoffIndex_Object = MibTableColumn
pm1008dcpCtrlxfpOnoffIndex = _Pm1008dcpCtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 208, 1, 1),
    _Pm1008dcpCtrlxfpOnoffIndex_Type()
)
pm1008dcpCtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpOnoffIndex.setStatus("current")
_Pm1008dcpCtrlxfpOnoffPortn_Type = EkiState
_Pm1008dcpCtrlxfpOnoffPortn_Object = MibTableColumn
pm1008dcpCtrlxfpOnoffPortn = _Pm1008dcpCtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 208, 1, 2),
    _Pm1008dcpCtrlxfpOnoffPortn_Type()
)
pm1008dcpCtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpOnoffPortn.setStatus("current")
_Pm1008dcpCtrlxfpLineLoopTable_Object = MibTable
pm1008dcpCtrlxfpLineLoopTable = _Pm1008dcpCtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpLineLoopTable.setStatus("current")
_Pm1008dcpCtrlxfpLineLoopEntry_Object = MibTableRow
pm1008dcpCtrlxfpLineLoopEntry = _Pm1008dcpCtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 209, 1)
)
pm1008dcpCtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpLineLoopEntry.setStatus("current")


class _Pm1008dcpCtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlxfpLineLoopIndex_Object = MibTableColumn
pm1008dcpCtrlxfpLineLoopIndex = _Pm1008dcpCtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 209, 1, 1),
    _Pm1008dcpCtrlxfpLineLoopIndex_Type()
)
pm1008dcpCtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpLineLoopIndex.setStatus("current")
_Pm1008dcpCtrlxfpLineLoopPortn_Type = EkiState
_Pm1008dcpCtrlxfpLineLoopPortn_Object = MibTableColumn
pm1008dcpCtrlxfpLineLoopPortn = _Pm1008dcpCtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 209, 1, 2),
    _Pm1008dcpCtrlxfpLineLoopPortn_Type()
)
pm1008dcpCtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpLineLoopPortn.setStatus("current")
_Pm1008dcpCtrlxfpXfiLoopTable_Object = MibTable
pm1008dcpCtrlxfpXfiLoopTable = _Pm1008dcpCtrlxfpXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpXfiLoopTable.setStatus("current")
_Pm1008dcpCtrlxfpXfiLoopEntry_Object = MibTableRow
pm1008dcpCtrlxfpXfiLoopEntry = _Pm1008dcpCtrlxfpXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 210, 1)
)
pm1008dcpCtrlxfpXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlxfpXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpXfiLoopEntry.setStatus("current")


class _Pm1008dcpCtrlxfpXfiLoopIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlxfpXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlxfpXfiLoopIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlxfpXfiLoopIndex_Object = MibTableColumn
pm1008dcpCtrlxfpXfiLoopIndex = _Pm1008dcpCtrlxfpXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 210, 1, 1),
    _Pm1008dcpCtrlxfpXfiLoopIndex_Type()
)
pm1008dcpCtrlxfpXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpXfiLoopIndex.setStatus("current")
_Pm1008dcpCtrlxfpXfiLoopPortn_Type = EkiState
_Pm1008dcpCtrlxfpXfiLoopPortn_Object = MibTableColumn
pm1008dcpCtrlxfpXfiLoopPortn = _Pm1008dcpCtrlxfpXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 210, 1, 2),
    _Pm1008dcpCtrlxfpXfiLoopPortn_Type()
)
pm1008dcpCtrlxfpXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlxfpXfiLoopPortn.setStatus("current")
_Pm1008dcpCtrllineTunableChannelTable_Object = MibTable
pm1008dcpCtrllineTunableChannelTable = _Pm1008dcpCtrllineTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllineTunableChannelTable.setStatus("current")
_Pm1008dcpCtrllineTunableChannelEntry_Object = MibTableRow
pm1008dcpCtrllineTunableChannelEntry = _Pm1008dcpCtrllineTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 212, 1)
)
pm1008dcpCtrllineTunableChannelEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrllineTunableChannelIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllineTunableChannelEntry.setStatus("current")


class _Pm1008dcpCtrllineTunableChannelIndex_Type(Integer32):
    """Custom type pm1008dcpCtrllineTunableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrllineTunableChannelIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrllineTunableChannelIndex_Object = MibTableColumn
pm1008dcpCtrllineTunableChannelIndex = _Pm1008dcpCtrllineTunableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 212, 1, 1),
    _Pm1008dcpCtrllineTunableChannelIndex_Type()
)
pm1008dcpCtrllineTunableChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrllineTunableChannelIndex.setStatus("current")
_Pm1008dcpCtrllineTunableChannelPortn_Type = Pm1008dcpOtxChannel
_Pm1008dcpCtrllineTunableChannelPortn_Object = MibTableColumn
pm1008dcpCtrllineTunableChannelPortn = _Pm1008dcpCtrllineTunableChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 212, 1, 2),
    _Pm1008dcpCtrllineTunableChannelPortn_Type()
)
pm1008dcpCtrllineTunableChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrllineTunableChannelPortn.setStatus("current")
_Pm1008dcpCtrllinePhotodiodeModeTable_Object = MibTable
pm1008dcpCtrllinePhotodiodeModeTable = _Pm1008dcpCtrllinePhotodiodeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 213)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePhotodiodeModeTable.setStatus("current")
_Pm1008dcpCtrllinePhotodiodeModeEntry_Object = MibTableRow
pm1008dcpCtrllinePhotodiodeModeEntry = _Pm1008dcpCtrllinePhotodiodeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 213, 1)
)
pm1008dcpCtrllinePhotodiodeModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrllinePhotodiodeModeIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePhotodiodeModeEntry.setStatus("current")


class _Pm1008dcpCtrllinePhotodiodeModeIndex_Type(Integer32):
    """Custom type pm1008dcpCtrllinePhotodiodeModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrllinePhotodiodeModeIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrllinePhotodiodeModeIndex_Object = MibTableColumn
pm1008dcpCtrllinePhotodiodeModeIndex = _Pm1008dcpCtrllinePhotodiodeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 213, 1, 1),
    _Pm1008dcpCtrllinePhotodiodeModeIndex_Type()
)
pm1008dcpCtrllinePhotodiodeModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePhotodiodeModeIndex.setStatus("current")
_Pm1008dcpCtrllinePhotodiodeModePortn_Type = Pm1008dcpOtxMode
_Pm1008dcpCtrllinePhotodiodeModePortn_Object = MibTableColumn
pm1008dcpCtrllinePhotodiodeModePortn = _Pm1008dcpCtrllinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 213, 1, 2),
    _Pm1008dcpCtrllinePhotodiodeModePortn_Type()
)
pm1008dcpCtrllinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePhotodiodeModePortn.setStatus("current")
_Pm1008dcpCtrllinePhotodiodeValueTable_Object = MibTable
pm1008dcpCtrllinePhotodiodeValueTable = _Pm1008dcpCtrllinePhotodiodeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 214)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePhotodiodeValueTable.setStatus("current")
_Pm1008dcpCtrllinePhotodiodeValueEntry_Object = MibTableRow
pm1008dcpCtrllinePhotodiodeValueEntry = _Pm1008dcpCtrllinePhotodiodeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 214, 1)
)
pm1008dcpCtrllinePhotodiodeValueEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrllinePhotodiodeValueIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePhotodiodeValueEntry.setStatus("current")


class _Pm1008dcpCtrllinePhotodiodeValueIndex_Type(Integer32):
    """Custom type pm1008dcpCtrllinePhotodiodeValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrllinePhotodiodeValueIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrllinePhotodiodeValueIndex_Object = MibTableColumn
pm1008dcpCtrllinePhotodiodeValueIndex = _Pm1008dcpCtrllinePhotodiodeValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 214, 1, 1),
    _Pm1008dcpCtrllinePhotodiodeValueIndex_Type()
)
pm1008dcpCtrllinePhotodiodeValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePhotodiodeValueIndex.setStatus("current")
_Pm1008dcpCtrllinePhotodiodeValuePortn_Type = Pm1008dcpAdjustValue
_Pm1008dcpCtrllinePhotodiodeValuePortn_Object = MibTableColumn
pm1008dcpCtrllinePhotodiodeValuePortn = _Pm1008dcpCtrllinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 214, 1, 2),
    _Pm1008dcpCtrllinePhotodiodeValuePortn_Type()
)
pm1008dcpCtrllinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePhotodiodeValuePortn.setStatus("current")
_Pm1008dcpCtrllinePowerLaserTable_Object = MibTable
pm1008dcpCtrllinePowerLaserTable = _Pm1008dcpCtrllinePowerLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 215)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePowerLaserTable.setStatus("current")
_Pm1008dcpCtrllinePowerLaserEntry_Object = MibTableRow
pm1008dcpCtrllinePowerLaserEntry = _Pm1008dcpCtrllinePowerLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 215, 1)
)
pm1008dcpCtrllinePowerLaserEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrllinePowerLaserIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePowerLaserEntry.setStatus("current")


class _Pm1008dcpCtrllinePowerLaserIndex_Type(Integer32):
    """Custom type pm1008dcpCtrllinePowerLaserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrllinePowerLaserIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrllinePowerLaserIndex_Object = MibTableColumn
pm1008dcpCtrllinePowerLaserIndex = _Pm1008dcpCtrllinePowerLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 215, 1, 1),
    _Pm1008dcpCtrllinePowerLaserIndex_Type()
)
pm1008dcpCtrllinePowerLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePowerLaserIndex.setStatus("current")


class _Pm1008dcpCtrllinePowerLaserPortn_Type(Integer32):
    """Custom type pm1008dcpCtrllinePowerLaserPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1008dcpCtrllinePowerLaserPortn_Type.__name__ = "Integer32"
_Pm1008dcpCtrllinePowerLaserPortn_Object = MibTableColumn
pm1008dcpCtrllinePowerLaserPortn = _Pm1008dcpCtrllinePowerLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 215, 1, 2),
    _Pm1008dcpCtrllinePowerLaserPortn_Type()
)
pm1008dcpCtrllinePowerLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrllinePowerLaserPortn.setStatus("current")
_Pm1008dcpCtrlotxVlhResetTable_Object = MibTable
pm1008dcpCtrlotxVlhResetTable = _Pm1008dcpCtrlotxVlhResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 216)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlotxVlhResetTable.setStatus("current")
_Pm1008dcpCtrlotxVlhResetEntry_Object = MibTableRow
pm1008dcpCtrlotxVlhResetEntry = _Pm1008dcpCtrlotxVlhResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 216, 1)
)
pm1008dcpCtrlotxVlhResetEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrlotxVlhResetIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrlotxVlhResetEntry.setStatus("current")


class _Pm1008dcpCtrlotxVlhResetIndex_Type(Integer32):
    """Custom type pm1008dcpCtrlotxVlhResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrlotxVlhResetIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrlotxVlhResetIndex_Object = MibTableColumn
pm1008dcpCtrlotxVlhResetIndex = _Pm1008dcpCtrlotxVlhResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 216, 1, 1),
    _Pm1008dcpCtrlotxVlhResetIndex_Type()
)
pm1008dcpCtrlotxVlhResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrlotxVlhResetIndex.setStatus("current")
_Pm1008dcpCtrlOtxVlhResetPortn_Type = EkiOnOff
_Pm1008dcpCtrlOtxVlhResetPortn_Object = MibTableColumn
pm1008dcpCtrlOtxVlhResetPortn = _Pm1008dcpCtrlOtxVlhResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 216, 1, 2),
    _Pm1008dcpCtrlOtxVlhResetPortn_Type()
)
pm1008dcpCtrlOtxVlhResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrlOtxVlhResetPortn.setStatus("current")
_Pm1008dcpCtrllineAccessLoopTable_Object = MibTable
pm1008dcpCtrllineAccessLoopTable = _Pm1008dcpCtrllineAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 217)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllineAccessLoopTable.setStatus("current")
_Pm1008dcpCtrllineAccessLoopEntry_Object = MibTableRow
pm1008dcpCtrllineAccessLoopEntry = _Pm1008dcpCtrllineAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 217, 1)
)
pm1008dcpCtrllineAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrllineAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllineAccessLoopEntry.setStatus("current")


class _Pm1008dcpCtrllineAccessLoopIndex_Type(Integer32):
    """Custom type pm1008dcpCtrllineAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrllineAccessLoopIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrllineAccessLoopIndex_Object = MibTableColumn
pm1008dcpCtrllineAccessLoopIndex = _Pm1008dcpCtrllineAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 217, 1, 1),
    _Pm1008dcpCtrllineAccessLoopIndex_Type()
)
pm1008dcpCtrllineAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrllineAccessLoopIndex.setStatus("current")
_Pm1008dcpCtrllineAccessLoopPortn_Type = EkiState
_Pm1008dcpCtrllineAccessLoopPortn_Object = MibTableColumn
pm1008dcpCtrllineAccessLoopPortn = _Pm1008dcpCtrllineAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 217, 1, 2),
    _Pm1008dcpCtrllineAccessLoopPortn_Type()
)
pm1008dcpCtrllineAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrllineAccessLoopPortn.setStatus("current")
_Pm1008dcpCtrllineLoopTransceiverTable_Object = MibTable
pm1008dcpCtrllineLoopTransceiverTable = _Pm1008dcpCtrllineLoopTransceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 218)
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllineLoopTransceiverTable.setStatus("current")
_Pm1008dcpCtrllineLoopTransceiverEntry_Object = MibTableRow
pm1008dcpCtrllineLoopTransceiverEntry = _Pm1008dcpCtrllineLoopTransceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 218, 1)
)
pm1008dcpCtrllineLoopTransceiverEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCtrllineLoopTransceiverIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCtrllineLoopTransceiverEntry.setStatus("current")


class _Pm1008dcpCtrllineLoopTransceiverIndex_Type(Integer32):
    """Custom type pm1008dcpCtrllineLoopTransceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCtrllineLoopTransceiverIndex_Type.__name__ = "Integer32"
_Pm1008dcpCtrllineLoopTransceiverIndex_Object = MibTableColumn
pm1008dcpCtrllineLoopTransceiverIndex = _Pm1008dcpCtrllineLoopTransceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 218, 1, 1),
    _Pm1008dcpCtrllineLoopTransceiverIndex_Type()
)
pm1008dcpCtrllineLoopTransceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCtrllineLoopTransceiverIndex.setStatus("current")
_Pm1008dcpCtrllineLoopTransceiverPortn_Type = EkiState
_Pm1008dcpCtrllineLoopTransceiverPortn_Object = MibTableColumn
pm1008dcpCtrllineLoopTransceiverPortn = _Pm1008dcpCtrllineLoopTransceiverPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 6, 3, 218, 1, 2),
    _Pm1008dcpCtrllineLoopTransceiverPortn_Type()
)
pm1008dcpCtrllineLoopTransceiverPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCtrllineLoopTransceiverPortn.setStatus("current")
_Pm1008dcpri_ObjectIdentity = ObjectIdentity
pm1008dcpri = _Pm1008dcpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7)
)
_Pm1008dcpriTable_ObjectIdentity = ObjectIdentity
pm1008dcpriTable = _Pm1008dcpriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 1)
)
_Pm1008dcpRinvSfpTable_Object = MibTable
pm1008dcpRinvSfpTable = _Pm1008dcpRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm1008dcpRinvSfpTable.setStatus("current")
_Pm1008dcpRinvSfpEntry_Object = MibTableRow
pm1008dcpRinvSfpEntry = _Pm1008dcpRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 1, 1, 1)
)
pm1008dcpRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpRinvSfpEntry.setStatus("current")


class _Pm1008dcpRinvSfpIndex_Type(Integer32):
    """Custom type pm1008dcpRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1008dcpRinvSfpIndex_Type.__name__ = "Integer32"
_Pm1008dcpRinvSfpIndex_Object = MibTableColumn
pm1008dcpRinvSfpIndex = _Pm1008dcpRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 1, 1, 1, 1),
    _Pm1008dcpRinvSfpIndex_Type()
)
pm1008dcpRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpRinvSfpIndex.setStatus("current")
_Pm1008dcpRinvsfp_Type = DisplayString
_Pm1008dcpRinvsfp_Object = MibTableColumn
pm1008dcpRinvsfp = _Pm1008dcpRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 1, 1, 1, 2),
    _Pm1008dcpRinvsfp_Type()
)
pm1008dcpRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpRinvsfp.setStatus("current")
_Pm1008dcpRinvLineTable_Object = MibTable
pm1008dcpRinvLineTable = _Pm1008dcpRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm1008dcpRinvLineTable.setStatus("current")
_Pm1008dcpRinvLineEntry_Object = MibTableRow
pm1008dcpRinvLineEntry = _Pm1008dcpRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 1, 2, 1)
)
pm1008dcpRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpRinvLineEntry.setStatus("current")


class _Pm1008dcpRinvLineIndex_Type(Integer32):
    """Custom type pm1008dcpRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1008dcpRinvLineIndex_Type.__name__ = "Integer32"
_Pm1008dcpRinvLineIndex_Object = MibTableColumn
pm1008dcpRinvLineIndex = _Pm1008dcpRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 1, 2, 1, 1),
    _Pm1008dcpRinvLineIndex_Type()
)
pm1008dcpRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpRinvLineIndex.setStatus("current")
_Pm1008dcpRinvxfpLine_Type = DisplayString
_Pm1008dcpRinvxfpLine_Object = MibTableColumn
pm1008dcpRinvxfpLine = _Pm1008dcpRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 1, 2, 1, 2),
    _Pm1008dcpRinvxfpLine_Type()
)
pm1008dcpRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpRinvxfpLine.setStatus("current")
_Pm1008dcpRinvReloadInventory_Type = EkiOnOff
_Pm1008dcpRinvReloadInventory_Object = MibScalar
pm1008dcpRinvReloadInventory = _Pm1008dcpRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 2),
    _Pm1008dcpRinvReloadInventory_Type()
)
pm1008dcpRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpRinvReloadInventory.setStatus("current")
_Pm1008dcpRinvHwPlatform_Type = DisplayString
_Pm1008dcpRinvHwPlatform_Object = MibScalar
pm1008dcpRinvHwPlatform = _Pm1008dcpRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 3),
    _Pm1008dcpRinvHwPlatform_Type()
)
pm1008dcpRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpRinvHwPlatform.setStatus("current")
_Pm1008dcpRinvModulePlatform_Type = DisplayString
_Pm1008dcpRinvModulePlatform_Object = MibScalar
pm1008dcpRinvModulePlatform = _Pm1008dcpRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 4),
    _Pm1008dcpRinvModulePlatform_Type()
)
pm1008dcpRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpRinvModulePlatform.setStatus("current")
_Pm1008dcpRinvSwPlatform_Type = DisplayString
_Pm1008dcpRinvSwPlatform_Object = MibScalar
pm1008dcpRinvSwPlatform = _Pm1008dcpRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 5),
    _Pm1008dcpRinvSwPlatform_Type()
)
pm1008dcpRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpRinvSwPlatform.setStatus("current")
_Pm1008dcpRinvGwPlatform_Type = DisplayString
_Pm1008dcpRinvGwPlatform_Object = MibScalar
pm1008dcpRinvGwPlatform = _Pm1008dcpRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 7, 6),
    _Pm1008dcpRinvGwPlatform_Type()
)
pm1008dcpRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpRinvGwPlatform.setStatus("current")
_Pm1008dcpdownload_ObjectIdentity = ObjectIdentity
pm1008dcpdownload = _Pm1008dcpdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8)
)
_Pm1008dcpDwlOther_ObjectIdentity = ObjectIdentity
pm1008dcpDwlOther = _Pm1008dcpDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1)
)
_Pm1008dcpDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm1008dcpDwlrestartProcess = _Pm1008dcpDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 0)
)
_Pm1008dcpDwlWarmRestartProcessed_Type = EkiOnOff
_Pm1008dcpDwlWarmRestartProcessed_Object = MibScalar
pm1008dcpDwlWarmRestartProcessed = _Pm1008dcpDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 0, 1),
    _Pm1008dcpDwlWarmRestartProcessed_Type()
)
pm1008dcpDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlWarmRestartProcessed.setStatus("current")
_Pm1008dcpDwlColdRestartProcessed_Type = EkiOnOff
_Pm1008dcpDwlColdRestartProcessed_Object = MibScalar
pm1008dcpDwlColdRestartProcessed = _Pm1008dcpDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 0, 2),
    _Pm1008dcpDwlColdRestartProcessed_Type()
)
pm1008dcpDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlColdRestartProcessed.setStatus("current")
_Pm1008dcpDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm1008dcpDwlswBanksUsed = _Pm1008dcpDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 1)
)
_Pm1008dcpDwlSwBank1Used_Type = EkiOnOff
_Pm1008dcpDwlSwBank1Used_Object = MibScalar
pm1008dcpDwlSwBank1Used = _Pm1008dcpDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 1, 1),
    _Pm1008dcpDwlSwBank1Used_Type()
)
pm1008dcpDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlSwBank1Used.setStatus("current")
_Pm1008dcpDwlSwBank2Used_Type = EkiOnOff
_Pm1008dcpDwlSwBank2Used_Object = MibScalar
pm1008dcpDwlSwBank2Used = _Pm1008dcpDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 1, 2),
    _Pm1008dcpDwlSwBank2Used_Type()
)
pm1008dcpDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlSwBank2Used.setStatus("current")
_Pm1008dcpDwlSwBank1Notempty_Type = EkiOnOff
_Pm1008dcpDwlSwBank1Notempty_Object = MibScalar
pm1008dcpDwlSwBank1Notempty = _Pm1008dcpDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 1, 5),
    _Pm1008dcpDwlSwBank1Notempty_Type()
)
pm1008dcpDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlSwBank1Notempty.setStatus("current")
_Pm1008dcpDwlSwBank2Notempty_Type = EkiOnOff
_Pm1008dcpDwlSwBank2Notempty_Object = MibScalar
pm1008dcpDwlSwBank2Notempty = _Pm1008dcpDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 1, 6),
    _Pm1008dcpDwlSwBank2Notempty_Type()
)
pm1008dcpDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlSwBank2Notempty.setStatus("current")
_Pm1008dcpDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm1008dcpDwlgwBanksUsed = _Pm1008dcpDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 2)
)
_Pm1008dcpDwlGwBank1Used_Type = EkiOnOff
_Pm1008dcpDwlGwBank1Used_Object = MibScalar
pm1008dcpDwlGwBank1Used = _Pm1008dcpDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 2, 1),
    _Pm1008dcpDwlGwBank1Used_Type()
)
pm1008dcpDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlGwBank1Used.setStatus("current")
_Pm1008dcpDwlGwBank2Used_Type = EkiOnOff
_Pm1008dcpDwlGwBank2Used_Object = MibScalar
pm1008dcpDwlGwBank2Used = _Pm1008dcpDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 2, 2),
    _Pm1008dcpDwlGwBank2Used_Type()
)
pm1008dcpDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlGwBank2Used.setStatus("current")
_Pm1008dcpDwlGwBank3Used_Type = EkiOnOff
_Pm1008dcpDwlGwBank3Used_Object = MibScalar
pm1008dcpDwlGwBank3Used = _Pm1008dcpDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 2, 3),
    _Pm1008dcpDwlGwBank3Used_Type()
)
pm1008dcpDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlGwBank3Used.setStatus("current")
_Pm1008dcpDwlGwBank4Used_Type = EkiOnOff
_Pm1008dcpDwlGwBank4Used_Object = MibScalar
pm1008dcpDwlGwBank4Used = _Pm1008dcpDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 2, 4),
    _Pm1008dcpDwlGwBank4Used_Type()
)
pm1008dcpDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlGwBank4Used.setStatus("current")
_Pm1008dcpDwlGwBank1Notempty_Type = EkiOnOff
_Pm1008dcpDwlGwBank1Notempty_Object = MibScalar
pm1008dcpDwlGwBank1Notempty = _Pm1008dcpDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 2, 5),
    _Pm1008dcpDwlGwBank1Notempty_Type()
)
pm1008dcpDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlGwBank1Notempty.setStatus("current")
_Pm1008dcpDwlGwBank2Notempty_Type = EkiOnOff
_Pm1008dcpDwlGwBank2Notempty_Object = MibScalar
pm1008dcpDwlGwBank2Notempty = _Pm1008dcpDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 2, 6),
    _Pm1008dcpDwlGwBank2Notempty_Type()
)
pm1008dcpDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlGwBank2Notempty.setStatus("current")
_Pm1008dcpDwlGwBank3Notempty_Type = EkiOnOff
_Pm1008dcpDwlGwBank3Notempty_Object = MibScalar
pm1008dcpDwlGwBank3Notempty = _Pm1008dcpDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 2, 7),
    _Pm1008dcpDwlGwBank3Notempty_Type()
)
pm1008dcpDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlGwBank3Notempty.setStatus("current")
_Pm1008dcpDwlGwBank4Notempty_Type = EkiOnOff
_Pm1008dcpDwlGwBank4Notempty_Object = MibScalar
pm1008dcpDwlGwBank4Notempty = _Pm1008dcpDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 1, 2, 8),
    _Pm1008dcpDwlGwBank4Notempty_Type()
)
pm1008dcpDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpDwlGwBank4Notempty.setStatus("current")
_Pm1008dcpDwlClient_ObjectIdentity = ObjectIdentity
pm1008dcpDwlClient = _Pm1008dcpDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 2)
)
_Pm1008dcpDwlLine_ObjectIdentity = ObjectIdentity
pm1008dcpDwlLine = _Pm1008dcpDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 8, 3)
)
_Pm1008dcpConfig_ObjectIdentity = ObjectIdentity
pm1008dcpConfig = _Pm1008dcpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9)
)
_Pm1008dcpCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm1008dcpCfgAccessCAisCsf = _Pm1008dcpCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1)
)
_Pm1008dcpCfgClientcaiscsfTable_Object = MibTable
pm1008dcpCfgClientcaiscsfTable = _Pm1008dcpCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm1008dcpCfgClientcaiscsfTable.setStatus("current")
_Pm1008dcpCfgClientcaiscsfEntry_Object = MibTableRow
pm1008dcpCfgClientcaiscsfEntry = _Pm1008dcpCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1, 1)
)
pm1008dcpCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCfgClientcaiscsfEntry.setStatus("current")


class _Pm1008dcpCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm1008dcpCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm1008dcpCfgClientcaiscsfIndex_Object = MibTableColumn
pm1008dcpCfgClientcaiscsfIndex = _Pm1008dcpCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1, 1, 1),
    _Pm1008dcpCfgClientcaiscsfIndex_Type()
)
pm1008dcpCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgClientcaiscsfIndex.setStatus("current")


class _Pm1008dcpCfgCAisModePortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgCAisModePortn_Object = MibTableColumn
pm1008dcpCfgCAisModePortn = _Pm1008dcpCfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1, 1, 3),
    _Pm1008dcpCfgCAisModePortn_Type()
)
pm1008dcpCfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgCAisModePortn.setStatus("current")


class _Pm1008dcpCfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgUpAccessioAlmPortn_Object = MibTableColumn
pm1008dcpCfgUpAccessioAlmPortn = _Pm1008dcpCfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1, 1, 9),
    _Pm1008dcpCfgUpAccessioAlmPortn_Type()
)
pm1008dcpCfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgUpAccessioAlmPortn.setStatus("current")


class _Pm1008dcpCfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgUpMapperDeAlmPortn_Object = MibTableColumn
pm1008dcpCfgUpMapperDeAlmPortn = _Pm1008dcpCfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1, 1, 10),
    _Pm1008dcpCfgUpMapperDeAlmPortn_Type()
)
pm1008dcpCfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgUpMapperDeAlmPortn.setStatus("current")


class _Pm1008dcpCfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgDownAccessioAlmPortn_Object = MibTableColumn
pm1008dcpCfgDownAccessioAlmPortn = _Pm1008dcpCfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1, 1, 17),
    _Pm1008dcpCfgDownAccessioAlmPortn_Type()
)
pm1008dcpCfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgDownAccessioAlmPortn.setStatus("current")


class _Pm1008dcpCfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgDownMapperDeAlmPortn_Object = MibTableColumn
pm1008dcpCfgDownMapperDeAlmPortn = _Pm1008dcpCfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1, 1, 18),
    _Pm1008dcpCfgDownMapperDeAlmPortn_Type()
)
pm1008dcpCfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgDownMapperDeAlmPortn.setStatus("current")


class _Pm1008dcpCfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgDownDfrmAlmPortn_Object = MibTableColumn
pm1008dcpCfgDownDfrmAlmPortn = _Pm1008dcpCfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1, 1, 19),
    _Pm1008dcpCfgDownDfrmAlmPortn_Type()
)
pm1008dcpCfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgDownDfrmAlmPortn.setStatus("current")


class _Pm1008dcpCfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pm1008dcpCfgDownLineSyncAlarmsPortn = _Pm1008dcpCfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 1, 1, 1, 20),
    _Pm1008dcpCfgDownLineSyncAlarmsPortn_Type()
)
pm1008dcpCfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgDownLineSyncAlarmsPortn.setStatus("deprecated")
_Pm1008dcpCfgStartup_ObjectIdentity = ObjectIdentity
pm1008dcpCfgStartup = _Pm1008dcpCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2)
)
_Pm1008dcpCfgClientStartupTable_Object = MibTable
pm1008dcpCfgClientStartupTable = _Pm1008dcpCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm1008dcpCfgClientStartupTable.setStatus("current")
_Pm1008dcpCfgClientStartupEntry_Object = MibTableRow
pm1008dcpCfgClientStartupEntry = _Pm1008dcpCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 1, 1)
)
pm1008dcpCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCfgClientStartupEntry.setStatus("current")


class _Pm1008dcpCfgClientStartupIndex_Type(Integer32):
    """Custom type pm1008dcpCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm1008dcpCfgClientStartupIndex_Object = MibTableColumn
pm1008dcpCfgClientStartupIndex = _Pm1008dcpCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 1, 1, 1),
    _Pm1008dcpCfgClientStartupIndex_Type()
)
pm1008dcpCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgClientStartupIndex.setStatus("current")


class _Pm1008dcpCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgSystConfPortPortn_Object = MibTableColumn
pm1008dcpCfgSystConfPortPortn = _Pm1008dcpCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 1, 1, 3),
    _Pm1008dcpCfgSystConfPortPortn_Type()
)
pm1008dcpCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgSystConfPortPortn.setStatus("current")


class _Pm1008dcpCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgNetConfPortPortn_Object = MibTableColumn
pm1008dcpCfgNetConfPortPortn = _Pm1008dcpCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 1, 1, 4),
    _Pm1008dcpCfgNetConfPortPortn_Type()
)
pm1008dcpCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgNetConfPortPortn.setStatus("current")


class _Pm1008dcpCfgAdddropConfPortPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgAdddropConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgAdddropConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgAdddropConfPortPortn_Object = MibTableColumn
pm1008dcpCfgAdddropConfPortPortn = _Pm1008dcpCfgAdddropConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 1, 1, 5),
    _Pm1008dcpCfgAdddropConfPortPortn_Type()
)
pm1008dcpCfgAdddropConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgAdddropConfPortPortn.setStatus("deprecated")
_Pm1008dcptablelineStartup_ObjectIdentity = ObjectIdentity
pm1008dcptablelineStartup = _Pm1008dcptablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 2)
)


class _Pm1008dcpCfgsystConfLine1_Type(Unsigned32):
    """Custom type pm1008dcpCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgsystConfLine1_Object = MibScalar
pm1008dcpCfgsystConfLine1 = _Pm1008dcpCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 2, 2),
    _Pm1008dcpCfgsystConfLine1_Type()
)
pm1008dcpCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgsystConfLine1.setStatus("current")


class _Pm1008dcpCfglineOptions1_Type(Unsigned32):
    """Custom type pm1008dcpCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfglineOptions1_Type.__name__ = "Unsigned32"
_Pm1008dcpCfglineOptions1_Object = MibScalar
pm1008dcpCfglineOptions1 = _Pm1008dcpCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 2, 5),
    _Pm1008dcpCfglineOptions1_Type()
)
pm1008dcpCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfglineOptions1.setStatus("current")


class _Pm1008dcpCfgsystConfLine2_Type(Unsigned32):
    """Custom type pm1008dcpCfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgsystConfLine2_Object = MibScalar
pm1008dcpCfgsystConfLine2 = _Pm1008dcpCfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 2, 6),
    _Pm1008dcpCfgsystConfLine2_Type()
)
pm1008dcpCfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgsystConfLine2.setStatus("current")


class _Pm1008dcpCfglineSelection_Type(Unsigned32):
    """Custom type pm1008dcpCfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfglineSelection_Type.__name__ = "Unsigned32"
_Pm1008dcpCfglineSelection_Object = MibScalar
pm1008dcpCfglineSelection = _Pm1008dcpCfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 2, 7),
    _Pm1008dcpCfglineSelection_Type()
)
pm1008dcpCfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfglineSelection.setStatus("current")


class _Pm1008dcpCfglineOptions2_Type(Unsigned32):
    """Custom type pm1008dcpCfglineOptions2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfglineOptions2_Type.__name__ = "Unsigned32"
_Pm1008dcpCfglineOptions2_Object = MibScalar
pm1008dcpCfglineOptions2 = _Pm1008dcpCfglineOptions2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 2, 9),
    _Pm1008dcpCfglineOptions2_Type()
)
pm1008dcpCfglineOptions2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfglineOptions2.setStatus("deprecated")
_Pm1008dcpCfgXfpTable_Object = MibTable
pm1008dcpCfgXfpTable = _Pm1008dcpCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm1008dcpCfgXfpTable.setStatus("current")
_Pm1008dcpCfgXfpEntry_Object = MibTableRow
pm1008dcpCfgXfpEntry = _Pm1008dcpCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 3, 1)
)
pm1008dcpCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCfgXfpEntry.setStatus("current")


class _Pm1008dcpCfgXfpIndex_Type(Integer32):
    """Custom type pm1008dcpCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCfgXfpIndex_Type.__name__ = "Integer32"
_Pm1008dcpCfgXfpIndex_Object = MibTableColumn
pm1008dcpCfgXfpIndex = _Pm1008dcpCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 3, 1, 1),
    _Pm1008dcpCfgXfpIndex_Type()
)
pm1008dcpCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgXfpIndex.setStatus("current")


class _Pm1008dcpCfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgSystConfXfpPortn_Object = MibTableColumn
pm1008dcpCfgSystConfXfpPortn = _Pm1008dcpCfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 3, 1, 3),
    _Pm1008dcpCfgSystConfXfpPortn_Type()
)
pm1008dcpCfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgSystConfXfpPortn.setStatus("current")


class _Pm1008dcpCfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgDataRateConfXfpPortn_Object = MibTableColumn
pm1008dcpCfgDataRateConfXfpPortn = _Pm1008dcpCfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 3, 1, 4),
    _Pm1008dcpCfgDataRateConfXfpPortn_Type()
)
pm1008dcpCfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgDataRateConfXfpPortn.setStatus("deprecated")
_Pm1008dcpCfgOtxtlhTable_Object = MibTable
pm1008dcpCfgOtxtlhTable = _Pm1008dcpCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4)
)
if mibBuilder.loadTexts:
    pm1008dcpCfgOtxtlhTable.setStatus("current")
_Pm1008dcpCfgOtxtlhEntry_Object = MibTableRow
pm1008dcpCfgOtxtlhEntry = _Pm1008dcpCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1)
)
pm1008dcpCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCfgOtxtlhEntry.setStatus("current")


class _Pm1008dcpCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm1008dcpCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm1008dcpCfgOtxtlhIndex_Object = MibTableColumn
pm1008dcpCfgOtxtlhIndex = _Pm1008dcpCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 1),
    _Pm1008dcpCfgOtxtlhIndex_Type()
)
pm1008dcpCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgOtxtlhIndex.setStatus("current")


class _Pm1008dcpCfgNuPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgNuPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgNuPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgNuPortn_Object = MibTableColumn
pm1008dcpCfgNuPortn = _Pm1008dcpCfgNuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 3),
    _Pm1008dcpCfgNuPortn_Type()
)
pm1008dcpCfgNuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgNuPortn.setStatus("deprecated")


class _Pm1008dcpCfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgLineDitherRatePortn_Object = MibTableColumn
pm1008dcpCfgLineDitherRatePortn = _Pm1008dcpCfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 4),
    _Pm1008dcpCfgLineDitherRatePortn_Type()
)
pm1008dcpCfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgLineDitherRatePortn.setStatus("current")


class _Pm1008dcpCfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgLineDitherFhzPortn_Object = MibTableColumn
pm1008dcpCfgLineDitherFhzPortn = _Pm1008dcpCfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 5),
    _Pm1008dcpCfgLineDitherFhzPortn_Type()
)
pm1008dcpCfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgLineDitherFhzPortn.setStatus("current")


class _Pm1008dcpCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgLinePwrLaserPortn_Object = MibTableColumn
pm1008dcpCfgLinePwrLaserPortn = _Pm1008dcpCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 6),
    _Pm1008dcpCfgLinePwrLaserPortn_Type()
)
pm1008dcpCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgLinePwrLaserPortn.setStatus("current")


class _Pm1008dcpCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgLineFCurrentPortn_Object = MibTableColumn
pm1008dcpCfgLineFCurrentPortn = _Pm1008dcpCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 7),
    _Pm1008dcpCfgLineFCurrentPortn_Type()
)
pm1008dcpCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgLineFCurrentPortn.setStatus("current")


class _Pm1008dcpCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgLineGridCurrentPortn_Object = MibTableColumn
pm1008dcpCfgLineGridCurrentPortn = _Pm1008dcpCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 8),
    _Pm1008dcpCfgLineGridCurrentPortn_Type()
)
pm1008dcpCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgLineGridCurrentPortn.setStatus("current")


class _Pm1008dcpCfgFPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgFPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgFPortn_Object = MibTableColumn
pm1008dcpCfgFPortn = _Pm1008dcpCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 9),
    _Pm1008dcpCfgFPortn_Type()
)
pm1008dcpCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgFPortn.setStatus("current")


class _Pm1008dcpCfgReservedPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgReservedPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgReservedPortn_Object = MibTableColumn
pm1008dcpCfgReservedPortn = _Pm1008dcpCfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 10),
    _Pm1008dcpCfgReservedPortn_Type()
)
pm1008dcpCfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgReservedPortn.setStatus("deprecated")


class _Pm1008dcpCfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgLinePhotodiodeModePortn_Object = MibTableColumn
pm1008dcpCfgLinePhotodiodeModePortn = _Pm1008dcpCfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 11),
    _Pm1008dcpCfgLinePhotodiodeModePortn_Type()
)
pm1008dcpCfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgLinePhotodiodeModePortn.setStatus("current")


class _Pm1008dcpCfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgLinePhotodiodeValuePortn_Object = MibTableColumn
pm1008dcpCfgLinePhotodiodeValuePortn = _Pm1008dcpCfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 2, 4, 1, 12),
    _Pm1008dcpCfgLinePhotodiodeValuePortn_Type()
)
pm1008dcpCfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgLinePhotodiodeValuePortn.setStatus("current")
_Pm1008dcpCfgOther_ObjectIdentity = ObjectIdentity
pm1008dcpCfgOther = _Pm1008dcpCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 3)
)
_Pm1008dcptablemoduleOther_ObjectIdentity = ObjectIdentity
pm1008dcptablemoduleOther = _Pm1008dcptablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 3, 1)
)


class _Pm1008dcpCfgmode_Type(Unsigned32):
    """Custom type pm1008dcpCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgmode_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgmode_Object = MibScalar
pm1008dcpCfgmode = _Pm1008dcpCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 3, 1, 2),
    _Pm1008dcpCfgmode_Type()
)
pm1008dcpCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgmode.setStatus("current")


class _Pm1008dcpCfgadddropTsPairMode1_Type(Unsigned32):
    """Custom type pm1008dcpCfgadddropTsPairMode1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgadddropTsPairMode1_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgadddropTsPairMode1_Object = MibScalar
pm1008dcpCfgadddropTsPairMode1 = _Pm1008dcpCfgadddropTsPairMode1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 3, 1, 3),
    _Pm1008dcpCfgadddropTsPairMode1_Type()
)
pm1008dcpCfgadddropTsPairMode1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgadddropTsPairMode1.setStatus("current")


class _Pm1008dcpCfgadddropTsPairMode2_Type(Unsigned32):
    """Custom type pm1008dcpCfgadddropTsPairMode2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgadddropTsPairMode2_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgadddropTsPairMode2_Object = MibScalar
pm1008dcpCfgadddropTsPairMode2 = _Pm1008dcpCfgadddropTsPairMode2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 3, 1, 4),
    _Pm1008dcpCfgadddropTsPairMode2_Type()
)
pm1008dcpCfgadddropTsPairMode2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgadddropTsPairMode2.setStatus("current")


class _Pm1008dcpCfgadddropTsPairMode3_Type(Unsigned32):
    """Custom type pm1008dcpCfgadddropTsPairMode3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgadddropTsPairMode3_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgadddropTsPairMode3_Object = MibScalar
pm1008dcpCfgadddropTsPairMode3 = _Pm1008dcpCfgadddropTsPairMode3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 3, 1, 5),
    _Pm1008dcpCfgadddropTsPairMode3_Type()
)
pm1008dcpCfgadddropTsPairMode3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgadddropTsPairMode3.setStatus("current")


class _Pm1008dcpCfgadddropTsPairMode4_Type(Unsigned32):
    """Custom type pm1008dcpCfgadddropTsPairMode4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgadddropTsPairMode4_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgadddropTsPairMode4_Object = MibScalar
pm1008dcpCfgadddropTsPairMode4 = _Pm1008dcpCfgadddropTsPairMode4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 3, 1, 6),
    _Pm1008dcpCfgadddropTsPairMode4_Type()
)
pm1008dcpCfgadddropTsPairMode4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgadddropTsPairMode4.setStatus("current")
_Pm1008dcpCfgLabels_ObjectIdentity = ObjectIdentity
pm1008dcpCfgLabels = _Pm1008dcpCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 4)
)
_Pm1008dcpCfgLabelclientTable_Object = MibTable
pm1008dcpCfgLabelclientTable = _Pm1008dcpCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm1008dcpCfgLabelclientTable.setStatus("current")
_Pm1008dcpCfgLabelclientEntry_Object = MibTableRow
pm1008dcpCfgLabelclientEntry = _Pm1008dcpCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 4, 1, 1)
)
pm1008dcpCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCfgLabelclientEntry.setStatus("current")


class _Pm1008dcpCfgLabelclientIndex_Type(Integer32):
    """Custom type pm1008dcpCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1008dcpCfgLabelclientIndex_Object = MibTableColumn
pm1008dcpCfgLabelclientIndex = _Pm1008dcpCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 4, 1, 1, 1),
    _Pm1008dcpCfgLabelclientIndex_Type()
)
pm1008dcpCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgLabelclientIndex.setStatus("current")


class _Pm1008dcpCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1008dcpCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1008dcpCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1008dcpCfgLabelclientPortn_Object = MibTableColumn
pm1008dcpCfgLabelclientPortn = _Pm1008dcpCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 4, 1, 1, 3),
    _Pm1008dcpCfgLabelclientPortn_Type()
)
pm1008dcpCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgLabelclientPortn.setStatus("current")
_Pm1008dcpCfgLabellineTable_Object = MibTable
pm1008dcpCfgLabellineTable = _Pm1008dcpCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pm1008dcpCfgLabellineTable.setStatus("current")
_Pm1008dcpCfgLabellineEntry_Object = MibTableRow
pm1008dcpCfgLabellineEntry = _Pm1008dcpCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 4, 2, 1)
)
pm1008dcpCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCfgLabellineEntry.setStatus("current")


class _Pm1008dcpCfgLabellineIndex_Type(Integer32):
    """Custom type pm1008dcpCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1008dcpCfgLabellineIndex_Object = MibTableColumn
pm1008dcpCfgLabellineIndex = _Pm1008dcpCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 4, 2, 1, 1),
    _Pm1008dcpCfgLabellineIndex_Type()
)
pm1008dcpCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgLabellineIndex.setStatus("current")


class _Pm1008dcpCfgLabellinePortn_Type(DisplayString):
    """Custom type pm1008dcpCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1008dcpCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1008dcpCfgLabellinePortn_Object = MibTableColumn
pm1008dcpCfgLabellinePortn = _Pm1008dcpCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 4, 2, 1, 3),
    _Pm1008dcpCfgLabellinePortn_Type()
)
pm1008dcpCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgLabellinePortn.setStatus("current")
_Pm1008dcpCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm1008dcpCfgStartuptablefive = _Pm1008dcpCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 5)
)
_Pm1008dcpCfgOtxtlhcapabilitiesTable_Object = MibTable
pm1008dcpCfgOtxtlhcapabilitiesTable = _Pm1008dcpCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pm1008dcpCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm1008dcpCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm1008dcpCfgOtxtlhcapabilitiesEntry = _Pm1008dcpCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 5, 1, 1)
)
pm1008dcpCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm1008dcpCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm1008dcpCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm1008dcpCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm1008dcpCfgOtxtlhcapabilitiesIndex = _Pm1008dcpCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 5, 1, 1, 1),
    _Pm1008dcpCfgOtxtlhcapabilitiesIndex_Type()
)
pm1008dcpCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm1008dcpCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgComponentTypePortn_Object = MibTableColumn
pm1008dcpCfgComponentTypePortn = _Pm1008dcpCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 5, 1, 1, 3),
    _Pm1008dcpCfgComponentTypePortn_Type()
)
pm1008dcpCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgComponentTypePortn.setStatus("current")


class _Pm1008dcpCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgMiscellaneousPortn_Object = MibTableColumn
pm1008dcpCfgMiscellaneousPortn = _Pm1008dcpCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 5, 1, 1, 4),
    _Pm1008dcpCfgMiscellaneousPortn_Type()
)
pm1008dcpCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgMiscellaneousPortn.setStatus("current")


class _Pm1008dcpCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgFirstChannelPortn_Object = MibTableColumn
pm1008dcpCfgFirstChannelPortn = _Pm1008dcpCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 5, 1, 1, 5),
    _Pm1008dcpCfgFirstChannelPortn_Type()
)
pm1008dcpCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgFirstChannelPortn.setStatus("current")


class _Pm1008dcpCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgLastChannelPortn_Object = MibTableColumn
pm1008dcpCfgLastChannelPortn = _Pm1008dcpCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 5, 1, 1, 6),
    _Pm1008dcpCfgLastChannelPortn_Type()
)
pm1008dcpCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgLastChannelPortn.setStatus("current")


class _Pm1008dcpCfgGridPortn_Type(Unsigned32):
    """Custom type pm1008dcpCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008dcpCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm1008dcpCfgGridPortn_Object = MibTableColumn
pm1008dcpCfgGridPortn = _Pm1008dcpCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 5, 1, 1, 7),
    _Pm1008dcpCfgGridPortn_Type()
)
pm1008dcpCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpCfgGridPortn.setStatus("current")
_Pm1008dcpCfgWriteConfiguration_Type = EkiOnOff
_Pm1008dcpCfgWriteConfiguration_Object = MibScalar
pm1008dcpCfgWriteConfiguration = _Pm1008dcpCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 9, 257),
    _Pm1008dcpCfgWriteConfiguration_Type()
)
pm1008dcpCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpCfgWriteConfiguration.setStatus("current")
_Pm1008dcptraps_ObjectIdentity = ObjectIdentity
pm1008dcptraps = _Pm1008dcptraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10)
)


class _Pm1008dcptrapPortNumber_Type(Integer32):
    """Custom type pm1008dcptrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1008dcptrapPortNumber_Type.__name__ = "Integer32"
_Pm1008dcptrapPortNumber_Object = MibScalar
pm1008dcptrapPortNumber = _Pm1008dcptrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 2),
    _Pm1008dcptrapPortNumber_Type()
)
pm1008dcptrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcptrapPortNumber.setStatus("current")


class _Pm1008dcptrapLineNumber_Type(Integer32):
    """Custom type pm1008dcptrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1008dcptrapLineNumber_Type.__name__ = "Integer32"
_Pm1008dcptrapLineNumber_Object = MibScalar
pm1008dcptrapLineNumber = _Pm1008dcptrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 3),
    _Pm1008dcptrapLineNumber_Type()
)
pm1008dcptrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcptrapLineNumber.setStatus("current")


class _Pm1008dcptrapBoardNumber_Type(Integer32):
    """Custom type pm1008dcptrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1008dcptrapBoardNumber_Type.__name__ = "Integer32"
_Pm1008dcptrapBoardNumber_Object = MibScalar
pm1008dcptrapBoardNumber = _Pm1008dcptrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 4),
    _Pm1008dcptrapBoardNumber_Type()
)
pm1008dcptrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcptrapBoardNumber.setStatus("current")
_Pm1008dcpMonitoring_ObjectIdentity = ObjectIdentity
pm1008dcpMonitoring = _Pm1008dcpMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11)
)
_Pm1008dcpMonOther_ObjectIdentity = ObjectIdentity
pm1008dcpMonOther = _Pm1008dcpMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 1)
)
_Pm1008dcpMonRmon_ObjectIdentity = ObjectIdentity
pm1008dcpMonRmon = _Pm1008dcpMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 1, 3)
)
_Pm1008dcpMonCountersReset_Type = EkiOnOff
_Pm1008dcpMonCountersReset_Object = MibScalar
pm1008dcpMonCountersReset = _Pm1008dcpMonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 1, 3, 359),
    _Pm1008dcpMonCountersReset_Type()
)
pm1008dcpMonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpMonCountersReset.setStatus("current")
_Pm1008dcpMonCountersStop_Type = EkiOnOff
_Pm1008dcpMonCountersStop_Object = MibScalar
pm1008dcpMonCountersStop = _Pm1008dcpMonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 1, 3, 360),
    _Pm1008dcpMonCountersStop_Type()
)
pm1008dcpMonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008dcpMonCountersStop.setStatus("current")
_Pm1008dcpMonClient_ObjectIdentity = ObjectIdentity
pm1008dcpMonClient = _Pm1008dcpMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2)
)
_Pm1008dcpMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm1008dcpMonClientRmonCounter = _Pm1008dcpMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4)
)
_Pm1008dcpMonupRmonByteCntTable_Object = MibTable
pm1008dcpMonupRmonByteCntTable = _Pm1008dcpMonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonByteCntTable.setStatus("current")
_Pm1008dcpMonupRmonByteCntEntry_Object = MibTableRow
pm1008dcpMonupRmonByteCntEntry = _Pm1008dcpMonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 16, 1)
)
pm1008dcpMonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonByteCntEntry.setStatus("current")


class _Pm1008dcpMonupRmonByteCntIndex_Type(Integer32):
    """Custom type pm1008dcpMonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpMonupRmonByteCntIndex_Object = MibTableColumn
pm1008dcpMonupRmonByteCntIndex = _Pm1008dcpMonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 16, 1, 1),
    _Pm1008dcpMonupRmonByteCntIndex_Type()
)
pm1008dcpMonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonByteCntIndex.setStatus("current")
_Pm1008dcpMonupRmonByteCntValuePortn_Type = Counter64
_Pm1008dcpMonupRmonByteCntValuePortn_Object = MibTableColumn
pm1008dcpMonupRmonByteCntValuePortn = _Pm1008dcpMonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 16, 1, 2),
    _Pm1008dcpMonupRmonByteCntValuePortn_Type()
)
pm1008dcpMonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonByteCntValuePortn.setStatus("current")
_Pm1008dcpMonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonByteCntErrorPortn_Object = MibTableColumn
pm1008dcpMonupRmonByteCntErrorPortn = _Pm1008dcpMonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 16, 1, 3),
    _Pm1008dcpMonupRmonByteCntErrorPortn_Type()
)
pm1008dcpMonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonByteCntErrorPortn.setStatus("current")
_Pm1008dcpMonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonByteCntOverloadPortn_Object = MibTableColumn
pm1008dcpMonupRmonByteCntOverloadPortn = _Pm1008dcpMonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 16, 1, 4),
    _Pm1008dcpMonupRmonByteCntOverloadPortn_Type()
)
pm1008dcpMonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonByteCntOverloadPortn.setStatus("current")
_Pm1008dcpMonupRmonCrcErrorCntTable_Object = MibTable
pm1008dcpMonupRmonCrcErrorCntTable = _Pm1008dcpMonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 24)
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonCrcErrorCntTable.setStatus("current")
_Pm1008dcpMonupRmonCrcErrorCntEntry_Object = MibTableRow
pm1008dcpMonupRmonCrcErrorCntEntry = _Pm1008dcpMonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 24, 1)
)
pm1008dcpMonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonCrcErrorCntEntry.setStatus("current")


class _Pm1008dcpMonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1008dcpMonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpMonupRmonCrcErrorCntIndex_Object = MibTableColumn
pm1008dcpMonupRmonCrcErrorCntIndex = _Pm1008dcpMonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 24, 1, 1),
    _Pm1008dcpMonupRmonCrcErrorCntIndex_Type()
)
pm1008dcpMonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonCrcErrorCntIndex.setStatus("current")
_Pm1008dcpMonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1008dcpMonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1008dcpMonupRmonCrcErrorCntValuePortn = _Pm1008dcpMonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 24, 1, 2),
    _Pm1008dcpMonupRmonCrcErrorCntValuePortn_Type()
)
pm1008dcpMonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1008dcpMonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1008dcpMonupRmonCrcErrorCntErrorPortn = _Pm1008dcpMonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 24, 1, 3),
    _Pm1008dcpMonupRmonCrcErrorCntErrorPortn_Type()
)
pm1008dcpMonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1008dcpMonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1008dcpMonupRmonCrcErrorCntOverloadPortn = _Pm1008dcpMonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 24, 1, 4),
    _Pm1008dcpMonupRmonCrcErrorCntOverloadPortn_Type()
)
pm1008dcpMonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1008dcpMonupRmonPacketsCntTable_Object = MibTable
pm1008dcpMonupRmonPacketsCntTable = _Pm1008dcpMonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonPacketsCntTable.setStatus("current")
_Pm1008dcpMonupRmonPacketsCntEntry_Object = MibTableRow
pm1008dcpMonupRmonPacketsCntEntry = _Pm1008dcpMonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 32, 1)
)
pm1008dcpMonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonPacketsCntEntry.setStatus("current")


class _Pm1008dcpMonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1008dcpMonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpMonupRmonPacketsCntIndex_Object = MibTableColumn
pm1008dcpMonupRmonPacketsCntIndex = _Pm1008dcpMonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 32, 1, 1),
    _Pm1008dcpMonupRmonPacketsCntIndex_Type()
)
pm1008dcpMonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonPacketsCntIndex.setStatus("current")
_Pm1008dcpMonupRmonPacketsCntValuePortn_Type = Counter64
_Pm1008dcpMonupRmonPacketsCntValuePortn_Object = MibTableColumn
pm1008dcpMonupRmonPacketsCntValuePortn = _Pm1008dcpMonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 32, 1, 2),
    _Pm1008dcpMonupRmonPacketsCntValuePortn_Type()
)
pm1008dcpMonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonPacketsCntValuePortn.setStatus("current")
_Pm1008dcpMonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1008dcpMonupRmonPacketsCntErrorPortn = _Pm1008dcpMonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 32, 1, 3),
    _Pm1008dcpMonupRmonPacketsCntErrorPortn_Type()
)
pm1008dcpMonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonPacketsCntErrorPortn.setStatus("current")
_Pm1008dcpMonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1008dcpMonupRmonPacketsCntOverloadPortn = _Pm1008dcpMonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 32, 1, 4),
    _Pm1008dcpMonupRmonPacketsCntOverloadPortn_Type()
)
pm1008dcpMonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1008dcpMonupRmonBroadcastCntTable_Object = MibTable
pm1008dcpMonupRmonBroadcastCntTable = _Pm1008dcpMonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 40)
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonBroadcastCntTable.setStatus("current")
_Pm1008dcpMonupRmonBroadcastCntEntry_Object = MibTableRow
pm1008dcpMonupRmonBroadcastCntEntry = _Pm1008dcpMonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 40, 1)
)
pm1008dcpMonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonBroadcastCntEntry.setStatus("current")


class _Pm1008dcpMonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pm1008dcpMonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpMonupRmonBroadcastCntIndex_Object = MibTableColumn
pm1008dcpMonupRmonBroadcastCntIndex = _Pm1008dcpMonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 40, 1, 1),
    _Pm1008dcpMonupRmonBroadcastCntIndex_Type()
)
pm1008dcpMonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonBroadcastCntIndex.setStatus("current")
_Pm1008dcpMonupRmonBroadcastCntValuePortn_Type = Counter64
_Pm1008dcpMonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pm1008dcpMonupRmonBroadcastCntValuePortn = _Pm1008dcpMonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 40, 1, 2),
    _Pm1008dcpMonupRmonBroadcastCntValuePortn_Type()
)
pm1008dcpMonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonBroadcastCntValuePortn.setStatus("current")
_Pm1008dcpMonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pm1008dcpMonupRmonBroadcastCntErrorPortn = _Pm1008dcpMonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 40, 1, 3),
    _Pm1008dcpMonupRmonBroadcastCntErrorPortn_Type()
)
pm1008dcpMonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pm1008dcpMonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pm1008dcpMonupRmonBroadcastCntOverloadPortn = _Pm1008dcpMonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 40, 1, 4),
    _Pm1008dcpMonupRmonBroadcastCntOverloadPortn_Type()
)
pm1008dcpMonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pm1008dcpMonupRmonMulticastCntTable_Object = MibTable
pm1008dcpMonupRmonMulticastCntTable = _Pm1008dcpMonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonMulticastCntTable.setStatus("current")
_Pm1008dcpMonupRmonMulticastCntEntry_Object = MibTableRow
pm1008dcpMonupRmonMulticastCntEntry = _Pm1008dcpMonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 48, 1)
)
pm1008dcpMonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008DCP-MIB", "pm1008dcpMonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonMulticastCntEntry.setStatus("current")


class _Pm1008dcpMonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pm1008dcpMonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008dcpMonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pm1008dcpMonupRmonMulticastCntIndex_Object = MibTableColumn
pm1008dcpMonupRmonMulticastCntIndex = _Pm1008dcpMonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 48, 1, 1),
    _Pm1008dcpMonupRmonMulticastCntIndex_Type()
)
pm1008dcpMonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonMulticastCntIndex.setStatus("current")
_Pm1008dcpMonupRmonMulticastCntValuePortn_Type = Counter64
_Pm1008dcpMonupRmonMulticastCntValuePortn_Object = MibTableColumn
pm1008dcpMonupRmonMulticastCntValuePortn = _Pm1008dcpMonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 48, 1, 2),
    _Pm1008dcpMonupRmonMulticastCntValuePortn_Type()
)
pm1008dcpMonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonMulticastCntValuePortn.setStatus("current")
_Pm1008dcpMonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pm1008dcpMonupRmonMulticastCntErrorPortn = _Pm1008dcpMonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 48, 1, 3),
    _Pm1008dcpMonupRmonMulticastCntErrorPortn_Type()
)
pm1008dcpMonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonMulticastCntErrorPortn.setStatus("current")
_Pm1008dcpMonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pm1008dcpMonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pm1008dcpMonupRmonMulticastCntOverloadPortn = _Pm1008dcpMonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 27, 11, 2, 4, 48, 1, 4),
    _Pm1008dcpMonupRmonMulticastCntOverloadPortn_Type()
)
pm1008dcpMonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008dcpMonupRmonMulticastCntOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

pm1008dcpLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 30)
)
pm1008dcpLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapLineNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1008dcpLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 31)
)
pm1008dcpLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapLineNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1008dcpLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 32)
)
pm1008dcpLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapLineNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1008dcpLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 33)
)
pm1008dcpLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapLineNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1008dcpLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 34)
)
pm1008dcpLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmLineFailPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmLineHwFailPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapLineNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpLineTrapCritGoesOn.setStatus(
        "current"
    )

pm1008dcpLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 35)
)
pm1008dcpLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmLineFailPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmLineHwFailPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapLineNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpLineTrapCritGoesOff.setStatus(
        "current"
    )

pm1008dcpClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 40)
)
pm1008dcpClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapPortNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1008dcpClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 41)
)
pm1008dcpClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapPortNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1008dcpClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 42)
)
pm1008dcpClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapPortNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1008dcpClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 43)
)
pm1008dcpClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapPortNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1008dcpClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 44)
)
pm1008dcpClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmFailAccPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmHwFailAccPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapPortNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpClientTrapCritGoesOn.setStatus(
        "current"
    )

pm1008dcpClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 45)
)
pm1008dcpClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmFailAccPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmHwFailAccPortn"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapPortNumber"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpClientTrapCritGoesOff.setStatus(
        "current"
    )

pm1008dcpPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 50)
)
pm1008dcpPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmDefFuseB"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmDefFuseA"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1008dcpPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 27, 10, 51)
)
pm1008dcpPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmDefFuseB"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcpAlmDefFuseA"),
        ("EKINOPS-Pm1008DCP-MIB", "pm1008dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008dcpPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1008DCP-MIB",
    **{"Pm1008dcpModeTimeSlot": Pm1008dcpModeTimeSlot,
       "Pm1008dcpModeAddDropA": Pm1008dcpModeAddDropA,
       "Pm1008dcpModeAddDrop": Pm1008dcpModeAddDrop,
       "Pm1008dcpProtectionTimeSlot": Pm1008dcpProtectionTimeSlot,
       "Pm1008dcpProtectionStartUp": Pm1008dcpProtectionStartUp,
       "Pm1008dcpDccMode": Pm1008dcpDccMode,
       "Pm1008dcpOtxMode": Pm1008dcpOtxMode,
       "Pm1008dcpOtxGrid": Pm1008dcpOtxGrid,
       "Pm1008dcpAdjustValue": Pm1008dcpAdjustValue,
       "Pm1008dcpOtxChannel": Pm1008dcpOtxChannel,
       "modulePm1008dcp": modulePm1008dcp,
       "pm1008dcpalarms": pm1008dcpalarms,
       "pm1008dcpAlmOther": pm1008dcpAlmOther,
       "pm1008dcpAlmOtherNurg": pm1008dcpAlmOtherNurg,
       "pm1008dcpAlmsynthAlm2": pm1008dcpAlmsynthAlm2,
       "pm1008dcpAlmConfTableSave": pm1008dcpAlmConfTableSave,
       "pm1008dcpAlmInvUpload": pm1008dcpAlmInvUpload,
       "pm1008dcpAlmConfTableLoad": pm1008dcpAlmConfTableLoad,
       "pm1008dcpAlmCorrelatOff": pm1008dcpAlmCorrelatOff,
       "pm1008dcpAlmMaintenanceOn": pm1008dcpAlmMaintenanceOn,
       "pm1008dcpAlmOtherUrg": pm1008dcpAlmOtherUrg,
       "pm1008dcpAlmmodInitFailLevel2": pm1008dcpAlmmodInitFailLevel2,
       "pm1008dcpAlmLedFail": pm1008dcpAlmLedFail,
       "pm1008dcpAlmNextColdBootForced": pm1008dcpAlmNextColdBootForced,
       "pm1008dcpAlmBootUndone": pm1008dcpAlmBootUndone,
       "pm1008dcpAlmResetHwInitFail": pm1008dcpAlmResetHwInitFail,
       "pm1008dcpAlmSwInitFail": pm1008dcpAlmSwInitFail,
       "pm1008dcpAlmmodInitFailLevel3": pm1008dcpAlmmodInitFailLevel3,
       "pm1008dcpAlmGwIdentFail": pm1008dcpAlmGwIdentFail,
       "pm1008dcpAlmObmTypeReadFail": pm1008dcpAlmObmTypeReadFail,
       "pm1008dcpAlmInitModuleFail": pm1008dcpAlmInitModuleFail,
       "pm1008dcpAlmXfp1InitFail": pm1008dcpAlmXfp1InitFail,
       "pm1008dcpAlmXfp2InitFail": pm1008dcpAlmXfp2InitFail,
       "pm1008dcpAlmLine1InitFail": pm1008dcpAlmLine1InitFail,
       "pm1008dcpAlmLine2InitFail": pm1008dcpAlmLine2InitFail,
       "pm1008dcpAlmClient1InitFail": pm1008dcpAlmClient1InitFail,
       "pm1008dcpAlmClient2InitFail": pm1008dcpAlmClient2InitFail,
       "pm1008dcpAlmClient3InitFail": pm1008dcpAlmClient3InitFail,
       "pm1008dcpAlmClient4InitFail": pm1008dcpAlmClient4InitFail,
       "pm1008dcpAlmClient5InitFail": pm1008dcpAlmClient5InitFail,
       "pm1008dcpAlmClient6InitFail": pm1008dcpAlmClient6InitFail,
       "pm1008dcpAlmClient7InitFail": pm1008dcpAlmClient7InitFail,
       "pm1008dcpAlmClient8InitFail": pm1008dcpAlmClient8InitFail,
       "pm1008dcpAlmadddropTsClientRxProt": pm1008dcpAlmadddropTsClientRxProt,
       "pm1008dcpAlmAdddropClient1West": pm1008dcpAlmAdddropClient1West,
       "pm1008dcpAlmAdddropClient2West": pm1008dcpAlmAdddropClient2West,
       "pm1008dcpAlmAdddropClient3West": pm1008dcpAlmAdddropClient3West,
       "pm1008dcpAlmAdddropClient4West": pm1008dcpAlmAdddropClient4West,
       "pm1008dcpAlmAdddropClient5West": pm1008dcpAlmAdddropClient5West,
       "pm1008dcpAlmAdddropClient6West": pm1008dcpAlmAdddropClient6West,
       "pm1008dcpAlmAdddropClient7West": pm1008dcpAlmAdddropClient7West,
       "pm1008dcpAlmAdddropClient8West": pm1008dcpAlmAdddropClient8West,
       "pm1008dcpAlmAdddropClient1East": pm1008dcpAlmAdddropClient1East,
       "pm1008dcpAlmAdddropClient2East": pm1008dcpAlmAdddropClient2East,
       "pm1008dcpAlmAdddropClient3East": pm1008dcpAlmAdddropClient3East,
       "pm1008dcpAlmAdddropClient4East": pm1008dcpAlmAdddropClient4East,
       "pm1008dcpAlmAdddropClient5East": pm1008dcpAlmAdddropClient5East,
       "pm1008dcpAlmAdddropClient6East": pm1008dcpAlmAdddropClient6East,
       "pm1008dcpAlmAdddropClient7East": pm1008dcpAlmAdddropClient7East,
       "pm1008dcpAlmAdddropClient8East": pm1008dcpAlmAdddropClient8East,
       "pm1008dcpAlmOtherCrit": pm1008dcpAlmOtherCrit,
       "pm1008dcpAlmsynthAlm0": pm1008dcpAlmsynthAlm0,
       "pm1008dcpAlmModGlobFail": pm1008dcpAlmModGlobFail,
       "pm1008dcpAlmDefFuseA": pm1008dcpAlmDefFuseA,
       "pm1008dcpAlmDefFuseB": pm1008dcpAlmDefFuseB,
       "pm1008dcpAlmClient": pm1008dcpAlmClient,
       "pm1008dcpAlmClientNurg": pm1008dcpAlmClientNurg,
       "pm1008dcpAlmsfpWarnDdmTable": pm1008dcpAlmsfpWarnDdmTable,
       "pm1008dcpAlmsfpWarnDdmEntry": pm1008dcpAlmsfpWarnDdmEntry,
       "pm1008dcpAlmsfpWarnDdmIndex": pm1008dcpAlmsfpWarnDdmIndex,
       "pm1008dcpAlmTxPwLowWngPortn": pm1008dcpAlmTxPwLowWngPortn,
       "pm1008dcpAlmTxPwrHighWngPortn": pm1008dcpAlmTxPwrHighWngPortn,
       "pm1008dcpAlmTxBiasLowWngPortn": pm1008dcpAlmTxBiasLowWngPortn,
       "pm1008dcpAlmTxBiasHighWngPortn": pm1008dcpAlmTxBiasHighWngPortn,
       "pm1008dcpAlmVccLowWngPortn": pm1008dcpAlmVccLowWngPortn,
       "pm1008dcpAlmVccHighWngPortn": pm1008dcpAlmVccHighWngPortn,
       "pm1008dcpAlmTempLowWngPortn": pm1008dcpAlmTempLowWngPortn,
       "pm1008dcpAlmTempHighWngPortn": pm1008dcpAlmTempHighWngPortn,
       "pm1008dcpAlmRxPwrLowWngPortn": pm1008dcpAlmRxPwrLowWngPortn,
       "pm1008dcpAlmRxPwrHighWngPortn": pm1008dcpAlmRxPwrHighWngPortn,
       "pm1008dcpAlmClientUrg": pm1008dcpAlmClientUrg,
       "pm1008dcpAlmsfpAlmDdmTable": pm1008dcpAlmsfpAlmDdmTable,
       "pm1008dcpAlmsfpAlmDdmEntry": pm1008dcpAlmsfpAlmDdmEntry,
       "pm1008dcpAlmsfpAlmDdmIndex": pm1008dcpAlmsfpAlmDdmIndex,
       "pm1008dcpAlmTxPwrLowAlaPortn": pm1008dcpAlmTxPwrLowAlaPortn,
       "pm1008dcpAlmTxPwrHighAlaPortn": pm1008dcpAlmTxPwrHighAlaPortn,
       "pm1008dcpAlmTxBiasLowAlaPortn": pm1008dcpAlmTxBiasLowAlaPortn,
       "pm1008dcpAlmTxBiasHighAlaPortn": pm1008dcpAlmTxBiasHighAlaPortn,
       "pm1008dcpAlmVccLowAlaPortn": pm1008dcpAlmVccLowAlaPortn,
       "pm1008dcpAlmVccHighAlaPortn": pm1008dcpAlmVccHighAlaPortn,
       "pm1008dcpAlmTempLowAlaPortn": pm1008dcpAlmTempLowAlaPortn,
       "pm1008dcpAlmTempHighAlaPortn": pm1008dcpAlmTempHighAlaPortn,
       "pm1008dcpAlmRxPwrLowAlaPortn": pm1008dcpAlmRxPwrLowAlaPortn,
       "pm1008dcpAlmRxPwrHighAlaPortn": pm1008dcpAlmRxPwrHighAlaPortn,
       "pm1008dcpAlmClientCrit": pm1008dcpAlmClientCrit,
       "pm1008dcpAlmsynthAlmPortTable": pm1008dcpAlmsynthAlmPortTable,
       "pm1008dcpAlmsynthAlmPortEntry": pm1008dcpAlmsynthAlmPortEntry,
       "pm1008dcpAlmsynthAlmPortIndex": pm1008dcpAlmsynthAlmPortIndex,
       "pm1008dcpAlmSfpAbsentPortn": pm1008dcpAlmSfpAbsentPortn,
       "pm1008dcpAlmDdmAbsentPortn": pm1008dcpAlmDdmAbsentPortn,
       "pm1008dcpAlmHwFailAccPortn": pm1008dcpAlmHwFailAccPortn,
       "pm1008dcpAlmDwLsdPortn": pm1008dcpAlmDwLsdPortn,
       "pm1008dcpAlmClientLocalOosPortn": pm1008dcpAlmClientLocalOosPortn,
       "pm1008dcpAlmClientRemoteOosPortn": pm1008dcpAlmClientRemoteOosPortn,
       "pm1008dcpAlmDwCaisPortn": pm1008dcpAlmDwCaisPortn,
       "pm1008dcpAlmSfpDdmWarningPortn": pm1008dcpAlmSfpDdmWarningPortn,
       "pm1008dcpAlmSfpDdmAlmPortn": pm1008dcpAlmSfpDdmAlmPortn,
       "pm1008dcpAlmFailAccPortn": pm1008dcpAlmFailAccPortn,
       "pm1008dcpAlmClientActivePortn": pm1008dcpAlmClientActivePortn,
       "pm1008dcpAlmUpCsfPortn": pm1008dcpAlmUpCsfPortn,
       "pm1008dcpAlmaccessioAlmTable": pm1008dcpAlmaccessioAlmTable,
       "pm1008dcpAlmaccessioAlmEntry": pm1008dcpAlmaccessioAlmEntry,
       "pm1008dcpAlmaccessioAlmIndex": pm1008dcpAlmaccessioAlmIndex,
       "pm1008dcpAlmDwLasFailPortn": pm1008dcpAlmDwLasFailPortn,
       "pm1008dcpAlmUpLosPortn": pm1008dcpAlmUpLosPortn,
       "pm1008dcpAlmmapperDeAlmTable": pm1008dcpAlmmapperDeAlmTable,
       "pm1008dcpAlmmapperDeAlmEntry": pm1008dcpAlmmapperDeAlmEntry,
       "pm1008dcpAlmmapperDeAlmIndex": pm1008dcpAlmmapperDeAlmIndex,
       "pm1008dcpAlmUpAccOosPortn": pm1008dcpAlmUpAccOosPortn,
       "pm1008dcpAlmUpBufferOvlPortn": pm1008dcpAlmUpBufferOvlPortn,
       "pm1008dcpAlmDwCsfDetPortn": pm1008dcpAlmDwCsfDetPortn,
       "pm1008dcpAlmDwBufferOvlPortn": pm1008dcpAlmDwBufferOvlPortn,
       "pm1008dcpAlmLine": pm1008dcpAlmLine,
       "pm1008dcpAlmLineNurg": pm1008dcpAlmLineNurg,
       "pm1008dcpAlmlineXfp1WarningsTable": pm1008dcpAlmlineXfp1WarningsTable,
       "pm1008dcpAlmlineXfp1WarningsEntry": pm1008dcpAlmlineXfp1WarningsEntry,
       "pm1008dcpAlmlineXfp1WarningsIndex": pm1008dcpAlmlineXfp1WarningsIndex,
       "pm1008dcpAlmTxPowerLowWarningPortn": pm1008dcpAlmTxPowerLowWarningPortn,
       "pm1008dcpAlmTxPowerHighWarningPortn": pm1008dcpAlmTxPowerHighWarningPortn,
       "pm1008dcpAlmTxBiasLowWarningPortn": pm1008dcpAlmTxBiasLowWarningPortn,
       "pm1008dcpAlmTxBiasHighWarningPortn": pm1008dcpAlmTxBiasHighWarningPortn,
       "pm1008dcpAlmTempLowWarningPortn": pm1008dcpAlmTempLowWarningPortn,
       "pm1008dcpAlmTempHighWarningPortn": pm1008dcpAlmTempHighWarningPortn,
       "pm1008dcpAlmRxPowerLowWarningPortn": pm1008dcpAlmRxPowerLowWarningPortn,
       "pm1008dcpAlmRxPowerHighWarningPortn": pm1008dcpAlmRxPowerHighWarningPortn,
       "pm1008dcpAlmlineOtx1TlhWarningsTable": pm1008dcpAlmlineOtx1TlhWarningsTable,
       "pm1008dcpAlmlineOtx1TlhWarningsEntry": pm1008dcpAlmlineOtx1TlhWarningsEntry,
       "pm1008dcpAlmlineOtx1TlhWarningsIndex": pm1008dcpAlmlineOtx1TlhWarningsIndex,
       "pm1008dcpAlmLineModulatorAgingHighWarningPortn": pm1008dcpAlmLineModulatorAgingHighWarningPortn,
       "pm1008dcpAlmLineAgingHighWarningPortn": pm1008dcpAlmLineAgingHighWarningPortn,
       "pm1008dcpAlmLineFreqDevHighWarningPortn": pm1008dcpAlmLineFreqDevHighWarningPortn,
       "pm1008dcpAlmLineLaserTempHighWarningPortn": pm1008dcpAlmLineLaserTempHighWarningPortn,
       "pm1008dcpAlmLineUrg": pm1008dcpAlmLineUrg,
       "pm1008dcpAlmdfrmBerTable": pm1008dcpAlmdfrmBerTable,
       "pm1008dcpAlmdfrmBerEntry": pm1008dcpAlmdfrmBerEntry,
       "pm1008dcpAlmdfrmBerIndex": pm1008dcpAlmdfrmBerIndex,
       "pm1008dcpAlmLineSignalDegradePortn": pm1008dcpAlmLineSignalDegradePortn,
       "pm1008dcpAlmLineSignalFailPortn": pm1008dcpAlmLineSignalFailPortn,
       "pm1008dcpAlmLineDegradePortn": pm1008dcpAlmLineDegradePortn,
       "pm1008dcpAlmlineXfp1AlarmTable": pm1008dcpAlmlineXfp1AlarmTable,
       "pm1008dcpAlmlineXfp1AlarmEntry": pm1008dcpAlmlineXfp1AlarmEntry,
       "pm1008dcpAlmlineXfp1AlarmIndex": pm1008dcpAlmlineXfp1AlarmIndex,
       "pm1008dcpAlmTxPowerLowAlarmPortn": pm1008dcpAlmTxPowerLowAlarmPortn,
       "pm1008dcpAlmTxPowerHighAlarmPortn": pm1008dcpAlmTxPowerHighAlarmPortn,
       "pm1008dcpAlmTxBiasLowAlarmPortn": pm1008dcpAlmTxBiasLowAlarmPortn,
       "pm1008dcpAlmTxBiasHighAlarmPortn": pm1008dcpAlmTxBiasHighAlarmPortn,
       "pm1008dcpAlmTempLowAlarmPortn": pm1008dcpAlmTempLowAlarmPortn,
       "pm1008dcpAlmTempHighAlarmPortn": pm1008dcpAlmTempHighAlarmPortn,
       "pm1008dcpAlmRxPowerLowAlarmPortn": pm1008dcpAlmRxPowerLowAlarmPortn,
       "pm1008dcpAlmRxPowerHighAlarmPortn": pm1008dcpAlmRxPowerHighAlarmPortn,
       "pm1008dcpAlmlineXfp1SupplyAlarmTable": pm1008dcpAlmlineXfp1SupplyAlarmTable,
       "pm1008dcpAlmlineXfp1SupplyAlarmEntry": pm1008dcpAlmlineXfp1SupplyAlarmEntry,
       "pm1008dcpAlmlineXfp1SupplyAlarmIndex": pm1008dcpAlmlineXfp1SupplyAlarmIndex,
       "pm1008dcpAlmVee5LowAlarmPortn": pm1008dcpAlmVee5LowAlarmPortn,
       "pm1008dcpAlmVee5HighAlarmPortn": pm1008dcpAlmVee5HighAlarmPortn,
       "pm1008dcpAlmVcc2LowAlarmPortn": pm1008dcpAlmVcc2LowAlarmPortn,
       "pm1008dcpAlmVcc2HighAlarmPortn": pm1008dcpAlmVcc2HighAlarmPortn,
       "pm1008dcpAlmVcc3LowAlarmPortn": pm1008dcpAlmVcc3LowAlarmPortn,
       "pm1008dcpAlmVcc3HighAlarmPortn": pm1008dcpAlmVcc3HighAlarmPortn,
       "pm1008dcpAlmVcc5LowAlarmPortn": pm1008dcpAlmVcc5LowAlarmPortn,
       "pm1008dcpAlmVcc5HighAlarmPortn": pm1008dcpAlmVcc5HighAlarmPortn,
       "pm1008dcpAlmVee5LowWarningPortn": pm1008dcpAlmVee5LowWarningPortn,
       "pm1008dcpAlmVee5HighWarningPortn": pm1008dcpAlmVee5HighWarningPortn,
       "pm1008dcpAlmVcc2LowWarningPortn": pm1008dcpAlmVcc2LowWarningPortn,
       "pm1008dcpAlmVcc2HighWarningPortn": pm1008dcpAlmVcc2HighWarningPortn,
       "pm1008dcpAlmVcc3LowWarningPortn": pm1008dcpAlmVcc3LowWarningPortn,
       "pm1008dcpAlmVcc3HighWarningPortn": pm1008dcpAlmVcc3HighWarningPortn,
       "pm1008dcpAlmVcc5LowWarningPortn": pm1008dcpAlmVcc5LowWarningPortn,
       "pm1008dcpAlmVcc5HighWarningPortn": pm1008dcpAlmVcc5HighWarningPortn,
       "pm1008dcpAlmlineOtx1TlhAlarmsTable": pm1008dcpAlmlineOtx1TlhAlarmsTable,
       "pm1008dcpAlmlineOtx1TlhAlarmsEntry": pm1008dcpAlmlineOtx1TlhAlarmsEntry,
       "pm1008dcpAlmlineOtx1TlhAlarmsIndex": pm1008dcpAlmlineOtx1TlhAlarmsIndex,
       "pm1008dcpAlmLineModulatorAgingHighAlaPortn": pm1008dcpAlmLineModulatorAgingHighAlaPortn,
       "pm1008dcpAlmLineAgingHighAlaPortn": pm1008dcpAlmLineAgingHighAlaPortn,
       "pm1008dcpAlmLineCdrNotReadyPortn": pm1008dcpAlmLineCdrNotReadyPortn,
       "pm1008dcpAlmLineFreqDevHighAlaPortn": pm1008dcpAlmLineFreqDevHighAlaPortn,
       "pm1008dcpAlmLineLaserTempHighAlaPortn": pm1008dcpAlmLineLaserTempHighAlaPortn,
       "pm1008dcpAlmLineCrit": pm1008dcpAlmLineCrit,
       "pm1008dcpAlmsynthAlmLineTable": pm1008dcpAlmsynthAlmLineTable,
       "pm1008dcpAlmsynthAlmLineEntry": pm1008dcpAlmsynthAlmLineEntry,
       "pm1008dcpAlmsynthAlmLineIndex": pm1008dcpAlmsynthAlmLineIndex,
       "pm1008dcpAlmXfpAbsentPortn": pm1008dcpAlmXfpAbsentPortn,
       "pm1008dcpAlmXfpInitNotComplPortn": pm1008dcpAlmXfpInitNotComplPortn,
       "pm1008dcpAlmLineHwFailPortn": pm1008dcpAlmLineHwFailPortn,
       "pm1008dcpAlmXfpTxOffPortn": pm1008dcpAlmXfpTxOffPortn,
       "pm1008dcpAlmLineLocalOosPortn": pm1008dcpAlmLineLocalOosPortn,
       "pm1008dcpAlmUpRdiInsPortn": pm1008dcpAlmUpRdiInsPortn,
       "pm1008dcpAlmLineDdmWarningPortn": pm1008dcpAlmLineDdmWarningPortn,
       "pm1008dcpAlmLineDdmAlmPortn": pm1008dcpAlmLineDdmAlmPortn,
       "pm1008dcpAlmLineFailPortn": pm1008dcpAlmLineFailPortn,
       "pm1008dcpAlmdfrmAlmTable": pm1008dcpAlmdfrmAlmTable,
       "pm1008dcpAlmdfrmAlmEntry": pm1008dcpAlmdfrmAlmEntry,
       "pm1008dcpAlmdfrmAlmIndex": pm1008dcpAlmdfrmAlmIndex,
       "pm1008dcpAlmDwAisDetPortn": pm1008dcpAlmDwAisDetPortn,
       "pm1008dcpAlmDwRdiDetPortn": pm1008dcpAlmDwRdiDetPortn,
       "pm1008dcpAlmDwOofPortn": pm1008dcpAlmDwOofPortn,
       "pm1008dcpAlmDwLofPortn": pm1008dcpAlmDwLofPortn,
       "pm1008dcpAlmlineSyncAlarmsTable": pm1008dcpAlmlineSyncAlarmsTable,
       "pm1008dcpAlmlineSyncAlarmsEntry": pm1008dcpAlmlineSyncAlarmsEntry,
       "pm1008dcpAlmlineSyncAlarmsIndex": pm1008dcpAlmlineSyncAlarmsIndex,
       "pm1008dcpAlmDwLockerrPortn": pm1008dcpAlmDwLockerrPortn,
       "pm1008dcpAlmUpLockerrPortn": pm1008dcpAlmUpLockerrPortn,
       "pm1008dcpAlmDwLosPortn": pm1008dcpAlmDwLosPortn,
       "pm1008dcpAlmlineXfp1AlarmsTable": pm1008dcpAlmlineXfp1AlarmsTable,
       "pm1008dcpAlmlineXfp1AlarmsEntry": pm1008dcpAlmlineXfp1AlarmsEntry,
       "pm1008dcpAlmlineXfp1AlarmsIndex": pm1008dcpAlmlineXfp1AlarmsIndex,
       "pm1008dcpAlmModNrPortn": pm1008dcpAlmModNrPortn,
       "pm1008dcpAlmRxCdrNotLockedPortn": pm1008dcpAlmRxCdrNotLockedPortn,
       "pm1008dcpAlmRxNrPortn": pm1008dcpAlmRxNrPortn,
       "pm1008dcpAlmTxCdrNotLockedPortn": pm1008dcpAlmTxCdrNotLockedPortn,
       "pm1008dcpAlmTxFaultPortn": pm1008dcpAlmTxFaultPortn,
       "pm1008dcpAlmTxNrPortn": pm1008dcpAlmTxNrPortn,
       "pm1008dcpAlmChannelNotAcquiredPortn": pm1008dcpAlmChannelNotAcquiredPortn,
       "pm1008dcpAlmWavelengthUnlockedPortn": pm1008dcpAlmWavelengthUnlockedPortn,
       "pm1008dcpAlmTecFaultPortn": pm1008dcpAlmTecFaultPortn,
       "pm1008dcpAlmApdSupplyFaultPortn": pm1008dcpAlmApdSupplyFaultPortn,
       "pm1008dcpmeasures": pm1008dcpmeasures,
       "pm1008dcpMesrOther": pm1008dcpMesrOther,
       "pm1008dcpMesrsynth0": pm1008dcpMesrsynth0,
       "pm1008dcpMesrsynth1": pm1008dcpMesrsynth1,
       "pm1008dcpMesrClient": pm1008dcpMesrClient,
       "pm1008dcpMesrtempMeasTable": pm1008dcpMesrtempMeasTable,
       "pm1008dcpMesrtempMeasEntry": pm1008dcpMesrtempMeasEntry,
       "pm1008dcpMesrtempMeasIndex": pm1008dcpMesrtempMeasIndex,
       "pm1008dcpMesrtempMeasPortn": pm1008dcpMesrtempMeasPortn,
       "pm1008dcpMesrvoltMeasTable": pm1008dcpMesrvoltMeasTable,
       "pm1008dcpMesrvoltMeasEntry": pm1008dcpMesrvoltMeasEntry,
       "pm1008dcpMesrvoltMeasIndex": pm1008dcpMesrvoltMeasIndex,
       "pm1008dcpMesrvoltMeasPortn": pm1008dcpMesrvoltMeasPortn,
       "pm1008dcpMesrbiasMeasTable": pm1008dcpMesrbiasMeasTable,
       "pm1008dcpMesrbiasMeasEntry": pm1008dcpMesrbiasMeasEntry,
       "pm1008dcpMesrbiasMeasIndex": pm1008dcpMesrbiasMeasIndex,
       "pm1008dcpMesrbiasMeasPortn": pm1008dcpMesrbiasMeasPortn,
       "pm1008dcpMesrtxpwrMeasTable": pm1008dcpMesrtxpwrMeasTable,
       "pm1008dcpMesrtxpwrMeasEntry": pm1008dcpMesrtxpwrMeasEntry,
       "pm1008dcpMesrtxpwrMeasIndex": pm1008dcpMesrtxpwrMeasIndex,
       "pm1008dcpMesrtxpwrMeasPortn": pm1008dcpMesrtxpwrMeasPortn,
       "pm1008dcpMesrrxpwrMeasTable": pm1008dcpMesrrxpwrMeasTable,
       "pm1008dcpMesrrxpwrMeasEntry": pm1008dcpMesrrxpwrMeasEntry,
       "pm1008dcpMesrrxpwrMeasIndex": pm1008dcpMesrrxpwrMeasIndex,
       "pm1008dcpMesrrxpwrMeasPortn": pm1008dcpMesrrxpwrMeasPortn,
       "pm1008dcpMesrLine": pm1008dcpMesrLine,
       "pm1008dcpMesrxfp1LxModTempMeasTable": pm1008dcpMesrxfp1LxModTempMeasTable,
       "pm1008dcpMesrxfp1LxModTempMeasEntry": pm1008dcpMesrxfp1LxModTempMeasEntry,
       "pm1008dcpMesrxfp1LxModTempMeasIndex": pm1008dcpMesrxfp1LxModTempMeasIndex,
       "pm1008dcpMesrxfp1LxModTempMeasPortn": pm1008dcpMesrxfp1LxModTempMeasPortn,
       "pm1008dcpMesrxfp1ReservedTable": pm1008dcpMesrxfp1ReservedTable,
       "pm1008dcpMesrxfp1ReservedEntry": pm1008dcpMesrxfp1ReservedEntry,
       "pm1008dcpMesrxfp1ReservedIndex": pm1008dcpMesrxfp1ReservedIndex,
       "pm1008dcpMesrxfp1ReservedPortn": pm1008dcpMesrxfp1ReservedPortn,
       "pm1008dcpMesrxfp1LoBiasCurrentMeasTable": pm1008dcpMesrxfp1LoBiasCurrentMeasTable,
       "pm1008dcpMesrxfp1LoBiasCurrentMeasEntry": pm1008dcpMesrxfp1LoBiasCurrentMeasEntry,
       "pm1008dcpMesrxfp1LoBiasCurrentMeasIndex": pm1008dcpMesrxfp1LoBiasCurrentMeasIndex,
       "pm1008dcpMesrxfp1LoBiasCurrentMeasPortn": pm1008dcpMesrxfp1LoBiasCurrentMeasPortn,
       "pm1008dcpMesrxfp1LoTxPowerMeasTable": pm1008dcpMesrxfp1LoTxPowerMeasTable,
       "pm1008dcpMesrxfp1LoTxPowerMeasEntry": pm1008dcpMesrxfp1LoTxPowerMeasEntry,
       "pm1008dcpMesrxfp1LoTxPowerMeasIndex": pm1008dcpMesrxfp1LoTxPowerMeasIndex,
       "pm1008dcpMesrxfp1LoTxPowerMeasPortn": pm1008dcpMesrxfp1LoTxPowerMeasPortn,
       "pm1008dcpMesrxfp1LiRxPowerMeasTable": pm1008dcpMesrxfp1LiRxPowerMeasTable,
       "pm1008dcpMesrxfp1LiRxPowerMeasEntry": pm1008dcpMesrxfp1LiRxPowerMeasEntry,
       "pm1008dcpMesrxfp1LiRxPowerMeasIndex": pm1008dcpMesrxfp1LiRxPowerMeasIndex,
       "pm1008dcpMesrxfp1LiRxPowerMeasPortn": pm1008dcpMesrxfp1LiRxPowerMeasPortn,
       "pm1008dcpMesrxfp1LxAux1MeasTable": pm1008dcpMesrxfp1LxAux1MeasTable,
       "pm1008dcpMesrxfp1LxAux1MeasEntry": pm1008dcpMesrxfp1LxAux1MeasEntry,
       "pm1008dcpMesrxfp1LxAux1MeasIndex": pm1008dcpMesrxfp1LxAux1MeasIndex,
       "pm1008dcpMesrxfp1LxAux1MeasPortn": pm1008dcpMesrxfp1LxAux1MeasPortn,
       "pm1008dcpMesrxfp1LxAux2MeasTable": pm1008dcpMesrxfp1LxAux2MeasTable,
       "pm1008dcpMesrxfp1LxAux2MeasEntry": pm1008dcpMesrxfp1LxAux2MeasEntry,
       "pm1008dcpMesrxfp1LxAux2MeasIndex": pm1008dcpMesrxfp1LxAux2MeasIndex,
       "pm1008dcpMesrxfp1LxAux2MeasPortn": pm1008dcpMesrxfp1LxAux2MeasPortn,
       "pm1008dcpMesrotx1AgingTable": pm1008dcpMesrotx1AgingTable,
       "pm1008dcpMesrotx1AgingEntry": pm1008dcpMesrotx1AgingEntry,
       "pm1008dcpMesrotx1AgingIndex": pm1008dcpMesrotx1AgingIndex,
       "pm1008dcpMesrotx1AgingPortn": pm1008dcpMesrotx1AgingPortn,
       "pm1008dcpMesrotx1LaserTemperatureTable": pm1008dcpMesrotx1LaserTemperatureTable,
       "pm1008dcpMesrotx1LaserTemperatureEntry": pm1008dcpMesrotx1LaserTemperatureEntry,
       "pm1008dcpMesrotx1LaserTemperatureIndex": pm1008dcpMesrotx1LaserTemperatureIndex,
       "pm1008dcpMesrotx1LaserTemperaturePortn": pm1008dcpMesrotx1LaserTemperaturePortn,
       "pm1008dcpMesrotx1FreqDeviationTable": pm1008dcpMesrotx1FreqDeviationTable,
       "pm1008dcpMesrotx1FreqDeviationEntry": pm1008dcpMesrotx1FreqDeviationEntry,
       "pm1008dcpMesrotx1FreqDeviationIndex": pm1008dcpMesrotx1FreqDeviationIndex,
       "pm1008dcpMesrotx1FreqDeviationPortn": pm1008dcpMesrotx1FreqDeviationPortn,
       "pm1008dcpMesrotx1LaserWvlengthTable": pm1008dcpMesrotx1LaserWvlengthTable,
       "pm1008dcpMesrotx1LaserWvlengthEntry": pm1008dcpMesrotx1LaserWvlengthEntry,
       "pm1008dcpMesrotx1LaserWvlengthIndex": pm1008dcpMesrotx1LaserWvlengthIndex,
       "pm1008dcpMesrotx1LaserWvlengthPortn": pm1008dcpMesrotx1LaserWvlengthPortn,
       "pm1008dcpcounters": pm1008dcpcounters,
       "pm1008dcpCntOther": pm1008dcpCntOther,
       "pm1008dcpCntClient": pm1008dcpCntClient,
       "pm1008dcpCntupRaRemCntTable": pm1008dcpCntupRaRemCntTable,
       "pm1008dcpCntupRaRemCntEntry": pm1008dcpCntupRaRemCntEntry,
       "pm1008dcpCntupRaRemCntIndex": pm1008dcpCntupRaRemCntIndex,
       "pm1008dcpCntupRaRemCntValuePortn": pm1008dcpCntupRaRemCntValuePortn,
       "pm1008dcpCntupRaRemCntErrorPortn": pm1008dcpCntupRaRemCntErrorPortn,
       "pm1008dcpCntupRaRemCntOverloadPortn": pm1008dcpCntupRaRemCntOverloadPortn,
       "pm1008dcpCntupRaInsCntTable": pm1008dcpCntupRaInsCntTable,
       "pm1008dcpCntupRaInsCntEntry": pm1008dcpCntupRaInsCntEntry,
       "pm1008dcpCntupRaInsCntIndex": pm1008dcpCntupRaInsCntIndex,
       "pm1008dcpCntupRaInsCntValuePortn": pm1008dcpCntupRaInsCntValuePortn,
       "pm1008dcpCntupRaInsCntErrorPortn": pm1008dcpCntupRaInsCntErrorPortn,
       "pm1008dcpCntupRaInsCntOverloadPortn": pm1008dcpCntupRaInsCntOverloadPortn,
       "pm1008dcpCntupRdErrCntTable": pm1008dcpCntupRdErrCntTable,
       "pm1008dcpCntupRdErrCntEntry": pm1008dcpCntupRdErrCntEntry,
       "pm1008dcpCntupRdErrCntIndex": pm1008dcpCntupRdErrCntIndex,
       "pm1008dcpCntupRdErrCntValuePortn": pm1008dcpCntupRdErrCntValuePortn,
       "pm1008dcpCntupRdErrCntErrorPortn": pm1008dcpCntupRdErrCntErrorPortn,
       "pm1008dcpCntupRdErrCntOverloadPortn": pm1008dcpCntupRdErrCntOverloadPortn,
       "pm1008dcpCntupTimCntTable": pm1008dcpCntupTimCntTable,
       "pm1008dcpCntupTimCntEntry": pm1008dcpCntupTimCntEntry,
       "pm1008dcpCntupTimCntIndex": pm1008dcpCntupTimCntIndex,
       "pm1008dcpCntupTimCntValuePortn": pm1008dcpCntupTimCntValuePortn,
       "pm1008dcpCntupTimCntErrorPortn": pm1008dcpCntupTimCntErrorPortn,
       "pm1008dcpCntupTimCntOverloadPortn": pm1008dcpCntupTimCntOverloadPortn,
       "pm1008dcpCntupCvErrCntTable": pm1008dcpCntupCvErrCntTable,
       "pm1008dcpCntupCvErrCntEntry": pm1008dcpCntupCvErrCntEntry,
       "pm1008dcpCntupCvErrCntIndex": pm1008dcpCntupCvErrCntIndex,
       "pm1008dcpCntupCvErrCntValuePortn": pm1008dcpCntupCvErrCntValuePortn,
       "pm1008dcpCntupCvErrCntErrorPortn": pm1008dcpCntupCvErrCntErrorPortn,
       "pm1008dcpCntupCvErrCntOverloadPortn": pm1008dcpCntupCvErrCntOverloadPortn,
       "pm1008dcpCntdwCbipCntTable": pm1008dcpCntdwCbipCntTable,
       "pm1008dcpCntdwCbipCntEntry": pm1008dcpCntdwCbipCntEntry,
       "pm1008dcpCntdwCbipCntIndex": pm1008dcpCntdwCbipCntIndex,
       "pm1008dcpCntdwCbipCntValuePortn": pm1008dcpCntdwCbipCntValuePortn,
       "pm1008dcpCntdwCbipCntErrorPortn": pm1008dcpCntdwCbipCntErrorPortn,
       "pm1008dcpCntdwCbipCntOverloadPortn": pm1008dcpCntdwCbipCntOverloadPortn,
       "pm1008dcpCntdwTimCntTable": pm1008dcpCntdwTimCntTable,
       "pm1008dcpCntdwTimCntEntry": pm1008dcpCntdwTimCntEntry,
       "pm1008dcpCntdwTimCntIndex": pm1008dcpCntdwTimCntIndex,
       "pm1008dcpCntdwTimCntValuePortn": pm1008dcpCntdwTimCntValuePortn,
       "pm1008dcpCntdwTimCntErrorPortn": pm1008dcpCntdwTimCntErrorPortn,
       "pm1008dcpCntdwTimCntOverloadPortn": pm1008dcpCntdwTimCntOverloadPortn,
       "pm1008dcpCntLine": pm1008dcpCntLine,
       "pm1008dcpCntdfrmB1ErrCntTable": pm1008dcpCntdfrmB1ErrCntTable,
       "pm1008dcpCntdfrmB1ErrCntEntry": pm1008dcpCntdfrmB1ErrCntEntry,
       "pm1008dcpCntdfrmB1ErrCntIndex": pm1008dcpCntdfrmB1ErrCntIndex,
       "pm1008dcpCntdfrmB1ErrCntValuePortn": pm1008dcpCntdfrmB1ErrCntValuePortn,
       "pm1008dcpCntdfrmB1ErrCntErrorPortn": pm1008dcpCntdfrmB1ErrCntErrorPortn,
       "pm1008dcpCntdfrmB1ErrCntOverloadPortn": pm1008dcpCntdfrmB1ErrCntOverloadPortn,
       "pm1008dcpCntdfrmTimCntTable": pm1008dcpCntdfrmTimCntTable,
       "pm1008dcpCntdfrmTimCntEntry": pm1008dcpCntdfrmTimCntEntry,
       "pm1008dcpCntdfrmTimCntIndex": pm1008dcpCntdfrmTimCntIndex,
       "pm1008dcpCntdfrmTimCntValuePortn": pm1008dcpCntdfrmTimCntValuePortn,
       "pm1008dcpCntdfrmTimCntErrorPortn": pm1008dcpCntdfrmTimCntErrorPortn,
       "pm1008dcpCntdfrmTimCntOverloadPortn": pm1008dcpCntdfrmTimCntOverloadPortn,
       "pm1008dcpCntdfrmPrimLineErrCntTable": pm1008dcpCntdfrmPrimLineErrCntTable,
       "pm1008dcpCntdfrmPrimLineErrCntEntry": pm1008dcpCntdfrmPrimLineErrCntEntry,
       "pm1008dcpCntdfrmPrimLineErrCntIndex": pm1008dcpCntdfrmPrimLineErrCntIndex,
       "pm1008dcpCntdfrmPrimLineErrCntValuePortn": pm1008dcpCntdfrmPrimLineErrCntValuePortn,
       "pm1008dcpCntdfrmPrimLineErrCntErrorPortn": pm1008dcpCntdfrmPrimLineErrCntErrorPortn,
       "pm1008dcpCntdfrmPrimLineErrCntOverloadPortn": pm1008dcpCntdfrmPrimLineErrCntOverloadPortn,
       "pm1008dcpCntCountersReset": pm1008dcpCntCountersReset,
       "pm1008dcpCntCountersStop": pm1008dcpCntCountersStop,
       "pm1008dcpcontrolsWrite": pm1008dcpcontrolsWrite,
       "pm1008dcpCtrlOther": pm1008dcpCtrlOther,
       "pm1008dcpCtrlconfMgnt1": pm1008dcpCtrlconfMgnt1,
       "pm1008dcpCtrlConf1Load1": pm1008dcpCtrlConf1Load1,
       "pm1008dcpCtrlConf2Load1": pm1008dcpCtrlConf2Load1,
       "pm1008dcpCtrlConf2Flash1": pm1008dcpCtrlConf2Flash1,
       "pm1008dcpCtrlConf2Clear1": pm1008dcpCtrlConf2Clear1,
       "pm1008dcpCtrlsynth4": pm1008dcpCtrlsynth4,
       "pm1008dcpCtrlCorrelatOn": pm1008dcpCtrlCorrelatOn,
       "pm1008dcpCtrlCorrelatOff": pm1008dcpCtrlCorrelatOff,
       "pm1008dcpCtrlswMgnt": pm1008dcpCtrlswMgnt,
       "pm1008dcpCtrlColdReset": pm1008dcpCtrlColdReset,
       "pm1008dcpCtrlWarmReset": pm1008dcpCtrlWarmReset,
       "pm1008dcpCtrlLoadSwBank1": pm1008dcpCtrlLoadSwBank1,
       "pm1008dcpCtrlLoadSwBank2": pm1008dcpCtrlLoadSwBank2,
       "pm1008dcpCtrlgwMgnt": pm1008dcpCtrlgwMgnt,
       "pm1008dcpCtrlCurrentGwReset": pm1008dcpCtrlCurrentGwReset,
       "pm1008dcpCtrlLoadGwBank1": pm1008dcpCtrlLoadGwBank1,
       "pm1008dcpCtrlLoadGwBank2": pm1008dcpCtrlLoadGwBank2,
       "pm1008dcpCtrlLoadGwBank3": pm1008dcpCtrlLoadGwBank3,
       "pm1008dcpCtrlLoadGwBank4": pm1008dcpCtrlLoadGwBank4,
       "pm1008dcpCtrlledTest": pm1008dcpCtrlledTest,
       "pm1008dcpCtrlGreenLed": pm1008dcpCtrlGreenLed,
       "pm1008dcpCtrlRedLed": pm1008dcpCtrlRedLed,
       "pm1008dcpCtrlLedOff": pm1008dcpCtrlLedOff,
       "pm1008dcpCtrlmoduleOosMode": pm1008dcpCtrlmoduleOosMode,
       "pm1008dcpCtrlModuleOosMode": pm1008dcpCtrlModuleOosMode,
       "pm1008dcpCtrlmoduleDccMgnt": pm1008dcpCtrlmoduleDccMgnt,
       "pm1008dcpCtrlmaintenanceMode": pm1008dcpCtrlmaintenanceMode,
       "pm1008dcpCtrlMaintenanceMode": pm1008dcpCtrlMaintenanceMode,
       "pm1008dcpCtrlClient": pm1008dcpCtrlClient,
       "pm1008dcpCtrlaccessLoopTable": pm1008dcpCtrlaccessLoopTable,
       "pm1008dcpCtrlaccessLoopEntry": pm1008dcpCtrlaccessLoopEntry,
       "pm1008dcpCtrlaccessLoopIndex": pm1008dcpCtrlaccessLoopIndex,
       "pm1008dcpCtrlaccessLoopPortn": pm1008dcpCtrlaccessLoopPortn,
       "pm1008dcpCtrlportOosModeTable": pm1008dcpCtrlportOosModeTable,
       "pm1008dcpCtrlportOosModeEntry": pm1008dcpCtrlportOosModeEntry,
       "pm1008dcpCtrlportOosModeIndex": pm1008dcpCtrlportOosModeIndex,
       "pm1008dcpCtrlportOosModePortn": pm1008dcpCtrlportOosModePortn,
       "pm1008dcpCtrlsfpOnCtrlTable": pm1008dcpCtrlsfpOnCtrlTable,
       "pm1008dcpCtrlsfpOnCtrlEntry": pm1008dcpCtrlsfpOnCtrlEntry,
       "pm1008dcpCtrlsfpOnCtrlIndex": pm1008dcpCtrlsfpOnCtrlIndex,
       "pm1008dcpCtrlsfpOnCtrlPortn": pm1008dcpCtrlsfpOnCtrlPortn,
       "pm1008dcpCtrlsfpOffCtrlTable": pm1008dcpCtrlsfpOffCtrlTable,
       "pm1008dcpCtrlsfpOffCtrlEntry": pm1008dcpCtrlsfpOffCtrlEntry,
       "pm1008dcpCtrlsfpOffCtrlIndex": pm1008dcpCtrlsfpOffCtrlIndex,
       "pm1008dcpCtrlsfpOffCtrlPortn": pm1008dcpCtrlsfpOffCtrlPortn,
       "pm1008dcpCtrlcsfUpInsTable": pm1008dcpCtrlcsfUpInsTable,
       "pm1008dcpCtrlcsfUpInsEntry": pm1008dcpCtrlcsfUpInsEntry,
       "pm1008dcpCtrlcsfUpInsIndex": pm1008dcpCtrlcsfUpInsIndex,
       "pm1008dcpCtrlcsfUpInsPortn": pm1008dcpCtrlcsfUpInsPortn,
       "pm1008dcpCtrlcaisDwInsTable": pm1008dcpCtrlcaisDwInsTable,
       "pm1008dcpCtrlcaisDwInsEntry": pm1008dcpCtrlcaisDwInsEntry,
       "pm1008dcpCtrlcaisDwInsIndex": pm1008dcpCtrlcaisDwInsIndex,
       "pm1008dcpCtrlcaisDwInsPortn": pm1008dcpCtrlcaisDwInsPortn,
       "pm1008dcpCtrlclientAccessTermLoopTable": pm1008dcpCtrlclientAccessTermLoopTable,
       "pm1008dcpCtrlclientAccessTermLoopEntry": pm1008dcpCtrlclientAccessTermLoopEntry,
       "pm1008dcpCtrlclientAccessTermLoopIndex": pm1008dcpCtrlclientAccessTermLoopIndex,
       "pm1008dcpCtrlclientAccessTermLoopPortn": pm1008dcpCtrlclientAccessTermLoopPortn,
       "pm1008dcpCtrlprotocolTable": pm1008dcpCtrlprotocolTable,
       "pm1008dcpCtrlprotocolEntry": pm1008dcpCtrlprotocolEntry,
       "pm1008dcpCtrlprotocolIndex": pm1008dcpCtrlprotocolIndex,
       "pm1008dcpCtrlprotocolPortn": pm1008dcpCtrlprotocolPortn,
       "pm1008dcpCtrladddropTsClientARxProtectTable": pm1008dcpCtrladddropTsClientARxProtectTable,
       "pm1008dcpCtrladddropTsClientARxProtectEntry": pm1008dcpCtrladddropTsClientARxProtectEntry,
       "pm1008dcpCtrladddropTsClientARxProtectIndex": pm1008dcpCtrladddropTsClientARxProtectIndex,
       "pm1008dcpCtrladddropTsClientARxProtectPortn": pm1008dcpCtrladddropTsClientARxProtectPortn,
       "pm1008dcpCtrladddropTsPairModeTable": pm1008dcpCtrladddropTsPairModeTable,
       "pm1008dcpCtrladddropTsPairModeEntry": pm1008dcpCtrladddropTsPairModeEntry,
       "pm1008dcpCtrladddropTsPairModeIndex": pm1008dcpCtrladddropTsPairModeIndex,
       "pm1008dcpCtrladddropTsPairModePortn": pm1008dcpCtrladddropTsPairModePortn,
       "pm1008dcpCtrlLine": pm1008dcpCtrlLine,
       "pm1008dcpCtrlcommAccessLoop": pm1008dcpCtrlcommAccessLoop,
       "pm1008dcpCtrlCommAccessloop": pm1008dcpCtrlCommAccessloop,
       "pm1008dcpCtrllineLoop": pm1008dcpCtrllineLoop,
       "pm1008dcpCtrlLineLoop": pm1008dcpCtrlLineLoop,
       "pm1008dcpCtrlmsAis": pm1008dcpCtrlmsAis,
       "pm1008dcpCtrlMsAis": pm1008dcpCtrlMsAis,
       "pm1008dcpCtrlfecDisableTable": pm1008dcpCtrlfecDisableTable,
       "pm1008dcpCtrlfecDisableEntry": pm1008dcpCtrlfecDisableEntry,
       "pm1008dcpCtrlfecDisableIndex": pm1008dcpCtrlfecDisableIndex,
       "pm1008dcpCtrlfecDisablePortn": pm1008dcpCtrlfecDisablePortn,
       "pm1008dcpCtrllineOosModeTable": pm1008dcpCtrllineOosModeTable,
       "pm1008dcpCtrllineOosModeEntry": pm1008dcpCtrllineOosModeEntry,
       "pm1008dcpCtrllineOosModeIndex": pm1008dcpCtrllineOosModeIndex,
       "pm1008dcpCtrllineOosModePortn": pm1008dcpCtrllineOosModePortn,
       "pm1008dcpCtrlxfpOnoffTable": pm1008dcpCtrlxfpOnoffTable,
       "pm1008dcpCtrlxfpOnoffEntry": pm1008dcpCtrlxfpOnoffEntry,
       "pm1008dcpCtrlxfpOnoffIndex": pm1008dcpCtrlxfpOnoffIndex,
       "pm1008dcpCtrlxfpOnoffPortn": pm1008dcpCtrlxfpOnoffPortn,
       "pm1008dcpCtrlxfpLineLoopTable": pm1008dcpCtrlxfpLineLoopTable,
       "pm1008dcpCtrlxfpLineLoopEntry": pm1008dcpCtrlxfpLineLoopEntry,
       "pm1008dcpCtrlxfpLineLoopIndex": pm1008dcpCtrlxfpLineLoopIndex,
       "pm1008dcpCtrlxfpLineLoopPortn": pm1008dcpCtrlxfpLineLoopPortn,
       "pm1008dcpCtrlxfpXfiLoopTable": pm1008dcpCtrlxfpXfiLoopTable,
       "pm1008dcpCtrlxfpXfiLoopEntry": pm1008dcpCtrlxfpXfiLoopEntry,
       "pm1008dcpCtrlxfpXfiLoopIndex": pm1008dcpCtrlxfpXfiLoopIndex,
       "pm1008dcpCtrlxfpXfiLoopPortn": pm1008dcpCtrlxfpXfiLoopPortn,
       "pm1008dcpCtrllineTunableChannelTable": pm1008dcpCtrllineTunableChannelTable,
       "pm1008dcpCtrllineTunableChannelEntry": pm1008dcpCtrllineTunableChannelEntry,
       "pm1008dcpCtrllineTunableChannelIndex": pm1008dcpCtrllineTunableChannelIndex,
       "pm1008dcpCtrllineTunableChannelPortn": pm1008dcpCtrllineTunableChannelPortn,
       "pm1008dcpCtrllinePhotodiodeModeTable": pm1008dcpCtrllinePhotodiodeModeTable,
       "pm1008dcpCtrllinePhotodiodeModeEntry": pm1008dcpCtrllinePhotodiodeModeEntry,
       "pm1008dcpCtrllinePhotodiodeModeIndex": pm1008dcpCtrllinePhotodiodeModeIndex,
       "pm1008dcpCtrllinePhotodiodeModePortn": pm1008dcpCtrllinePhotodiodeModePortn,
       "pm1008dcpCtrllinePhotodiodeValueTable": pm1008dcpCtrllinePhotodiodeValueTable,
       "pm1008dcpCtrllinePhotodiodeValueEntry": pm1008dcpCtrllinePhotodiodeValueEntry,
       "pm1008dcpCtrllinePhotodiodeValueIndex": pm1008dcpCtrllinePhotodiodeValueIndex,
       "pm1008dcpCtrllinePhotodiodeValuePortn": pm1008dcpCtrllinePhotodiodeValuePortn,
       "pm1008dcpCtrllinePowerLaserTable": pm1008dcpCtrllinePowerLaserTable,
       "pm1008dcpCtrllinePowerLaserEntry": pm1008dcpCtrllinePowerLaserEntry,
       "pm1008dcpCtrllinePowerLaserIndex": pm1008dcpCtrllinePowerLaserIndex,
       "pm1008dcpCtrllinePowerLaserPortn": pm1008dcpCtrllinePowerLaserPortn,
       "pm1008dcpCtrlotxVlhResetTable": pm1008dcpCtrlotxVlhResetTable,
       "pm1008dcpCtrlotxVlhResetEntry": pm1008dcpCtrlotxVlhResetEntry,
       "pm1008dcpCtrlotxVlhResetIndex": pm1008dcpCtrlotxVlhResetIndex,
       "pm1008dcpCtrlOtxVlhResetPortn": pm1008dcpCtrlOtxVlhResetPortn,
       "pm1008dcpCtrllineAccessLoopTable": pm1008dcpCtrllineAccessLoopTable,
       "pm1008dcpCtrllineAccessLoopEntry": pm1008dcpCtrllineAccessLoopEntry,
       "pm1008dcpCtrllineAccessLoopIndex": pm1008dcpCtrllineAccessLoopIndex,
       "pm1008dcpCtrllineAccessLoopPortn": pm1008dcpCtrllineAccessLoopPortn,
       "pm1008dcpCtrllineLoopTransceiverTable": pm1008dcpCtrllineLoopTransceiverTable,
       "pm1008dcpCtrllineLoopTransceiverEntry": pm1008dcpCtrllineLoopTransceiverEntry,
       "pm1008dcpCtrllineLoopTransceiverIndex": pm1008dcpCtrllineLoopTransceiverIndex,
       "pm1008dcpCtrllineLoopTransceiverPortn": pm1008dcpCtrllineLoopTransceiverPortn,
       "pm1008dcpri": pm1008dcpri,
       "pm1008dcpriTable": pm1008dcpriTable,
       "pm1008dcpRinvSfpTable": pm1008dcpRinvSfpTable,
       "pm1008dcpRinvSfpEntry": pm1008dcpRinvSfpEntry,
       "pm1008dcpRinvSfpIndex": pm1008dcpRinvSfpIndex,
       "pm1008dcpRinvsfp": pm1008dcpRinvsfp,
       "pm1008dcpRinvLineTable": pm1008dcpRinvLineTable,
       "pm1008dcpRinvLineEntry": pm1008dcpRinvLineEntry,
       "pm1008dcpRinvLineIndex": pm1008dcpRinvLineIndex,
       "pm1008dcpRinvxfpLine": pm1008dcpRinvxfpLine,
       "pm1008dcpRinvReloadInventory": pm1008dcpRinvReloadInventory,
       "pm1008dcpRinvHwPlatform": pm1008dcpRinvHwPlatform,
       "pm1008dcpRinvModulePlatform": pm1008dcpRinvModulePlatform,
       "pm1008dcpRinvSwPlatform": pm1008dcpRinvSwPlatform,
       "pm1008dcpRinvGwPlatform": pm1008dcpRinvGwPlatform,
       "pm1008dcpdownload": pm1008dcpdownload,
       "pm1008dcpDwlOther": pm1008dcpDwlOther,
       "pm1008dcpDwlrestartProcess": pm1008dcpDwlrestartProcess,
       "pm1008dcpDwlWarmRestartProcessed": pm1008dcpDwlWarmRestartProcessed,
       "pm1008dcpDwlColdRestartProcessed": pm1008dcpDwlColdRestartProcessed,
       "pm1008dcpDwlswBanksUsed": pm1008dcpDwlswBanksUsed,
       "pm1008dcpDwlSwBank1Used": pm1008dcpDwlSwBank1Used,
       "pm1008dcpDwlSwBank2Used": pm1008dcpDwlSwBank2Used,
       "pm1008dcpDwlSwBank1Notempty": pm1008dcpDwlSwBank1Notempty,
       "pm1008dcpDwlSwBank2Notempty": pm1008dcpDwlSwBank2Notempty,
       "pm1008dcpDwlgwBanksUsed": pm1008dcpDwlgwBanksUsed,
       "pm1008dcpDwlGwBank1Used": pm1008dcpDwlGwBank1Used,
       "pm1008dcpDwlGwBank2Used": pm1008dcpDwlGwBank2Used,
       "pm1008dcpDwlGwBank3Used": pm1008dcpDwlGwBank3Used,
       "pm1008dcpDwlGwBank4Used": pm1008dcpDwlGwBank4Used,
       "pm1008dcpDwlGwBank1Notempty": pm1008dcpDwlGwBank1Notempty,
       "pm1008dcpDwlGwBank2Notempty": pm1008dcpDwlGwBank2Notempty,
       "pm1008dcpDwlGwBank3Notempty": pm1008dcpDwlGwBank3Notempty,
       "pm1008dcpDwlGwBank4Notempty": pm1008dcpDwlGwBank4Notempty,
       "pm1008dcpDwlClient": pm1008dcpDwlClient,
       "pm1008dcpDwlLine": pm1008dcpDwlLine,
       "pm1008dcpConfig": pm1008dcpConfig,
       "pm1008dcpCfgAccessCAisCsf": pm1008dcpCfgAccessCAisCsf,
       "pm1008dcpCfgClientcaiscsfTable": pm1008dcpCfgClientcaiscsfTable,
       "pm1008dcpCfgClientcaiscsfEntry": pm1008dcpCfgClientcaiscsfEntry,
       "pm1008dcpCfgClientcaiscsfIndex": pm1008dcpCfgClientcaiscsfIndex,
       "pm1008dcpCfgCAisModePortn": pm1008dcpCfgCAisModePortn,
       "pm1008dcpCfgUpAccessioAlmPortn": pm1008dcpCfgUpAccessioAlmPortn,
       "pm1008dcpCfgUpMapperDeAlmPortn": pm1008dcpCfgUpMapperDeAlmPortn,
       "pm1008dcpCfgDownAccessioAlmPortn": pm1008dcpCfgDownAccessioAlmPortn,
       "pm1008dcpCfgDownMapperDeAlmPortn": pm1008dcpCfgDownMapperDeAlmPortn,
       "pm1008dcpCfgDownDfrmAlmPortn": pm1008dcpCfgDownDfrmAlmPortn,
       "pm1008dcpCfgDownLineSyncAlarmsPortn": pm1008dcpCfgDownLineSyncAlarmsPortn,
       "pm1008dcpCfgStartup": pm1008dcpCfgStartup,
       "pm1008dcpCfgClientStartupTable": pm1008dcpCfgClientStartupTable,
       "pm1008dcpCfgClientStartupEntry": pm1008dcpCfgClientStartupEntry,
       "pm1008dcpCfgClientStartupIndex": pm1008dcpCfgClientStartupIndex,
       "pm1008dcpCfgSystConfPortPortn": pm1008dcpCfgSystConfPortPortn,
       "pm1008dcpCfgNetConfPortPortn": pm1008dcpCfgNetConfPortPortn,
       "pm1008dcpCfgAdddropConfPortPortn": pm1008dcpCfgAdddropConfPortPortn,
       "pm1008dcptablelineStartup": pm1008dcptablelineStartup,
       "pm1008dcpCfgsystConfLine1": pm1008dcpCfgsystConfLine1,
       "pm1008dcpCfglineOptions1": pm1008dcpCfglineOptions1,
       "pm1008dcpCfgsystConfLine2": pm1008dcpCfgsystConfLine2,
       "pm1008dcpCfglineSelection": pm1008dcpCfglineSelection,
       "pm1008dcpCfglineOptions2": pm1008dcpCfglineOptions2,
       "pm1008dcpCfgXfpTable": pm1008dcpCfgXfpTable,
       "pm1008dcpCfgXfpEntry": pm1008dcpCfgXfpEntry,
       "pm1008dcpCfgXfpIndex": pm1008dcpCfgXfpIndex,
       "pm1008dcpCfgSystConfXfpPortn": pm1008dcpCfgSystConfXfpPortn,
       "pm1008dcpCfgDataRateConfXfpPortn": pm1008dcpCfgDataRateConfXfpPortn,
       "pm1008dcpCfgOtxtlhTable": pm1008dcpCfgOtxtlhTable,
       "pm1008dcpCfgOtxtlhEntry": pm1008dcpCfgOtxtlhEntry,
       "pm1008dcpCfgOtxtlhIndex": pm1008dcpCfgOtxtlhIndex,
       "pm1008dcpCfgNuPortn": pm1008dcpCfgNuPortn,
       "pm1008dcpCfgLineDitherRatePortn": pm1008dcpCfgLineDitherRatePortn,
       "pm1008dcpCfgLineDitherFhzPortn": pm1008dcpCfgLineDitherFhzPortn,
       "pm1008dcpCfgLinePwrLaserPortn": pm1008dcpCfgLinePwrLaserPortn,
       "pm1008dcpCfgLineFCurrentPortn": pm1008dcpCfgLineFCurrentPortn,
       "pm1008dcpCfgLineGridCurrentPortn": pm1008dcpCfgLineGridCurrentPortn,
       "pm1008dcpCfgFPortn": pm1008dcpCfgFPortn,
       "pm1008dcpCfgReservedPortn": pm1008dcpCfgReservedPortn,
       "pm1008dcpCfgLinePhotodiodeModePortn": pm1008dcpCfgLinePhotodiodeModePortn,
       "pm1008dcpCfgLinePhotodiodeValuePortn": pm1008dcpCfgLinePhotodiodeValuePortn,
       "pm1008dcpCfgOther": pm1008dcpCfgOther,
       "pm1008dcptablemoduleOther": pm1008dcptablemoduleOther,
       "pm1008dcpCfgmode": pm1008dcpCfgmode,
       "pm1008dcpCfgadddropTsPairMode1": pm1008dcpCfgadddropTsPairMode1,
       "pm1008dcpCfgadddropTsPairMode2": pm1008dcpCfgadddropTsPairMode2,
       "pm1008dcpCfgadddropTsPairMode3": pm1008dcpCfgadddropTsPairMode3,
       "pm1008dcpCfgadddropTsPairMode4": pm1008dcpCfgadddropTsPairMode4,
       "pm1008dcpCfgLabels": pm1008dcpCfgLabels,
       "pm1008dcpCfgLabelclientTable": pm1008dcpCfgLabelclientTable,
       "pm1008dcpCfgLabelclientEntry": pm1008dcpCfgLabelclientEntry,
       "pm1008dcpCfgLabelclientIndex": pm1008dcpCfgLabelclientIndex,
       "pm1008dcpCfgLabelclientPortn": pm1008dcpCfgLabelclientPortn,
       "pm1008dcpCfgLabellineTable": pm1008dcpCfgLabellineTable,
       "pm1008dcpCfgLabellineEntry": pm1008dcpCfgLabellineEntry,
       "pm1008dcpCfgLabellineIndex": pm1008dcpCfgLabellineIndex,
       "pm1008dcpCfgLabellinePortn": pm1008dcpCfgLabellinePortn,
       "pm1008dcpCfgStartuptablefive": pm1008dcpCfgStartuptablefive,
       "pm1008dcpCfgOtxtlhcapabilitiesTable": pm1008dcpCfgOtxtlhcapabilitiesTable,
       "pm1008dcpCfgOtxtlhcapabilitiesEntry": pm1008dcpCfgOtxtlhcapabilitiesEntry,
       "pm1008dcpCfgOtxtlhcapabilitiesIndex": pm1008dcpCfgOtxtlhcapabilitiesIndex,
       "pm1008dcpCfgComponentTypePortn": pm1008dcpCfgComponentTypePortn,
       "pm1008dcpCfgMiscellaneousPortn": pm1008dcpCfgMiscellaneousPortn,
       "pm1008dcpCfgFirstChannelPortn": pm1008dcpCfgFirstChannelPortn,
       "pm1008dcpCfgLastChannelPortn": pm1008dcpCfgLastChannelPortn,
       "pm1008dcpCfgGridPortn": pm1008dcpCfgGridPortn,
       "pm1008dcpCfgWriteConfiguration": pm1008dcpCfgWriteConfiguration,
       "pm1008dcptraps": pm1008dcptraps,
       "pm1008dcptrapPortNumber": pm1008dcptrapPortNumber,
       "pm1008dcptrapLineNumber": pm1008dcptrapLineNumber,
       "pm1008dcptrapBoardNumber": pm1008dcptrapBoardNumber,
       "pm1008dcpLineTrapNotUrgentGoesOn": pm1008dcpLineTrapNotUrgentGoesOn,
       "pm1008dcpLineTrapNotUrgentGoesOff": pm1008dcpLineTrapNotUrgentGoesOff,
       "pm1008dcpLineTrapUrgentGoesOn": pm1008dcpLineTrapUrgentGoesOn,
       "pm1008dcpLineTrapUrgentGoesOff": pm1008dcpLineTrapUrgentGoesOff,
       "pm1008dcpLineTrapCritGoesOn": pm1008dcpLineTrapCritGoesOn,
       "pm1008dcpLineTrapCritGoesOff": pm1008dcpLineTrapCritGoesOff,
       "pm1008dcpClientTrapNotUrgentGoesOn": pm1008dcpClientTrapNotUrgentGoesOn,
       "pm1008dcpClientTrapNotUrgentGoesOff": pm1008dcpClientTrapNotUrgentGoesOff,
       "pm1008dcpClientTrapUrgentGoesOn": pm1008dcpClientTrapUrgentGoesOn,
       "pm1008dcpClientTrapUrgentGoesOff": pm1008dcpClientTrapUrgentGoesOff,
       "pm1008dcpClientTrapCritGoesOn": pm1008dcpClientTrapCritGoesOn,
       "pm1008dcpClientTrapCritGoesOff": pm1008dcpClientTrapCritGoesOff,
       "pm1008dcpPowerTrapUrgentGoesOn": pm1008dcpPowerTrapUrgentGoesOn,
       "pm1008dcpPowerTrapUrgentGoesOff": pm1008dcpPowerTrapUrgentGoesOff,
       "pm1008dcpMonitoring": pm1008dcpMonitoring,
       "pm1008dcpMonOther": pm1008dcpMonOther,
       "pm1008dcpMonRmon": pm1008dcpMonRmon,
       "pm1008dcpMonCountersReset": pm1008dcpMonCountersReset,
       "pm1008dcpMonCountersStop": pm1008dcpMonCountersStop,
       "pm1008dcpMonClient": pm1008dcpMonClient,
       "pm1008dcpMonClientRmonCounter": pm1008dcpMonClientRmonCounter,
       "pm1008dcpMonupRmonByteCntTable": pm1008dcpMonupRmonByteCntTable,
       "pm1008dcpMonupRmonByteCntEntry": pm1008dcpMonupRmonByteCntEntry,
       "pm1008dcpMonupRmonByteCntIndex": pm1008dcpMonupRmonByteCntIndex,
       "pm1008dcpMonupRmonByteCntValuePortn": pm1008dcpMonupRmonByteCntValuePortn,
       "pm1008dcpMonupRmonByteCntErrorPortn": pm1008dcpMonupRmonByteCntErrorPortn,
       "pm1008dcpMonupRmonByteCntOverloadPortn": pm1008dcpMonupRmonByteCntOverloadPortn,
       "pm1008dcpMonupRmonCrcErrorCntTable": pm1008dcpMonupRmonCrcErrorCntTable,
       "pm1008dcpMonupRmonCrcErrorCntEntry": pm1008dcpMonupRmonCrcErrorCntEntry,
       "pm1008dcpMonupRmonCrcErrorCntIndex": pm1008dcpMonupRmonCrcErrorCntIndex,
       "pm1008dcpMonupRmonCrcErrorCntValuePortn": pm1008dcpMonupRmonCrcErrorCntValuePortn,
       "pm1008dcpMonupRmonCrcErrorCntErrorPortn": pm1008dcpMonupRmonCrcErrorCntErrorPortn,
       "pm1008dcpMonupRmonCrcErrorCntOverloadPortn": pm1008dcpMonupRmonCrcErrorCntOverloadPortn,
       "pm1008dcpMonupRmonPacketsCntTable": pm1008dcpMonupRmonPacketsCntTable,
       "pm1008dcpMonupRmonPacketsCntEntry": pm1008dcpMonupRmonPacketsCntEntry,
       "pm1008dcpMonupRmonPacketsCntIndex": pm1008dcpMonupRmonPacketsCntIndex,
       "pm1008dcpMonupRmonPacketsCntValuePortn": pm1008dcpMonupRmonPacketsCntValuePortn,
       "pm1008dcpMonupRmonPacketsCntErrorPortn": pm1008dcpMonupRmonPacketsCntErrorPortn,
       "pm1008dcpMonupRmonPacketsCntOverloadPortn": pm1008dcpMonupRmonPacketsCntOverloadPortn,
       "pm1008dcpMonupRmonBroadcastCntTable": pm1008dcpMonupRmonBroadcastCntTable,
       "pm1008dcpMonupRmonBroadcastCntEntry": pm1008dcpMonupRmonBroadcastCntEntry,
       "pm1008dcpMonupRmonBroadcastCntIndex": pm1008dcpMonupRmonBroadcastCntIndex,
       "pm1008dcpMonupRmonBroadcastCntValuePortn": pm1008dcpMonupRmonBroadcastCntValuePortn,
       "pm1008dcpMonupRmonBroadcastCntErrorPortn": pm1008dcpMonupRmonBroadcastCntErrorPortn,
       "pm1008dcpMonupRmonBroadcastCntOverloadPortn": pm1008dcpMonupRmonBroadcastCntOverloadPortn,
       "pm1008dcpMonupRmonMulticastCntTable": pm1008dcpMonupRmonMulticastCntTable,
       "pm1008dcpMonupRmonMulticastCntEntry": pm1008dcpMonupRmonMulticastCntEntry,
       "pm1008dcpMonupRmonMulticastCntIndex": pm1008dcpMonupRmonMulticastCntIndex,
       "pm1008dcpMonupRmonMulticastCntValuePortn": pm1008dcpMonupRmonMulticastCntValuePortn,
       "pm1008dcpMonupRmonMulticastCntErrorPortn": pm1008dcpMonupRmonMulticastCntErrorPortn,
       "pm1008dcpMonupRmonMulticastCntOverloadPortn": pm1008dcpMonupRmonMulticastCntOverloadPortn}
)
