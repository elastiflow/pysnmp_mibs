# SNMP MIB module (EKINOPS-Pm1004dcp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1004dcp-MIB.mib
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

modulePm1004dcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37)
)
if mibBuilder.loadTexts:
    modulePm1004dcp.setRevisions(
        ("2009-11-10 00:00",
         "2009-02-17 00:00",
         "2009-02-17 00:00",
         "2009-04-07 00:00",
         "2009-09-30 00:00",
         "2010-02-15 00:00",
         "2011-07-25 00:00",
         "2012-07-03 00:00",
         "2013-04-03 00:00",
         "2014-03-27 00:00",
         "2014-12-22 00:00",
         "2016-05-19 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1004dcpModeTimeSlot(TextualConvention, Integer32):
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



class Pm1004dcpModeAddDropA(TextualConvention, Integer32):
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



class Pm1004dcpModeAddDrop(TextualConvention, Integer32):
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



class Pm1004dcpProtectionTimeSlot(TextualConvention, Integer32):
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



class Pm1004dcpProtectionStartUp(TextualConvention, Integer32):
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



class Pm1004dcpDccMode(TextualConvention, Integer32):
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



class Pm1004dcpOtxMode(TextualConvention, Integer32):
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



class Pm1004dcpOtxGrid(TextualConvention, Integer32):
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



class Pm1004dcpAdjustValue(TextualConvention, Integer32):
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



class Pm1004dcpOtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm1004dcpalarms_ObjectIdentity = ObjectIdentity
pm1004dcpalarms = _Pm1004dcpalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2)
)
_Pm1004dcpAlmOther_ObjectIdentity = ObjectIdentity
pm1004dcpAlmOther = _Pm1004dcpAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1)
)
_Pm1004dcpAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1004dcpAlmOtherNurg = _Pm1004dcpAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 1)
)
_Pm1004dcpAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm1004dcpAlmsynthAlm2 = _Pm1004dcpAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 1, 2)
)
_Pm1004dcpAlmConfTableSave_Type = EkiOnOff
_Pm1004dcpAlmConfTableSave_Object = MibScalar
pm1004dcpAlmConfTableSave = _Pm1004dcpAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 1, 2, 1),
    _Pm1004dcpAlmConfTableSave_Type()
)
pm1004dcpAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmConfTableSave.setStatus("current")
_Pm1004dcpAlmInvUpload_Type = EkiOnOff
_Pm1004dcpAlmInvUpload_Object = MibScalar
pm1004dcpAlmInvUpload = _Pm1004dcpAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 1, 2, 2),
    _Pm1004dcpAlmInvUpload_Type()
)
pm1004dcpAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmInvUpload.setStatus("current")
_Pm1004dcpAlmConfTableLoad_Type = EkiOnOff
_Pm1004dcpAlmConfTableLoad_Object = MibScalar
pm1004dcpAlmConfTableLoad = _Pm1004dcpAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 1, 2, 3),
    _Pm1004dcpAlmConfTableLoad_Type()
)
pm1004dcpAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmConfTableLoad.setStatus("current")
_Pm1004dcpAlmCorrelatOff_Type = EkiOnOff
_Pm1004dcpAlmCorrelatOff_Object = MibScalar
pm1004dcpAlmCorrelatOff = _Pm1004dcpAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 1, 2, 4),
    _Pm1004dcpAlmCorrelatOff_Type()
)
pm1004dcpAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmCorrelatOff.setStatus("current")
_Pm1004dcpAlmMaintenanceOn_Type = EkiOnOff
_Pm1004dcpAlmMaintenanceOn_Object = MibScalar
pm1004dcpAlmMaintenanceOn = _Pm1004dcpAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 1, 2, 5),
    _Pm1004dcpAlmMaintenanceOn_Type()
)
pm1004dcpAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmMaintenanceOn.setStatus("current")
_Pm1004dcpAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1004dcpAlmOtherUrg = _Pm1004dcpAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2)
)
_Pm1004dcpAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm1004dcpAlmmodInitFailLevel2 = _Pm1004dcpAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 194)
)
_Pm1004dcpAlmLedFail_Type = EkiOnOff
_Pm1004dcpAlmLedFail_Object = MibScalar
pm1004dcpAlmLedFail = _Pm1004dcpAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 194, 1),
    _Pm1004dcpAlmLedFail_Type()
)
pm1004dcpAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLedFail.setStatus("current")
_Pm1004dcpAlmNextColdBootForced_Type = EkiOnOff
_Pm1004dcpAlmNextColdBootForced_Object = MibScalar
pm1004dcpAlmNextColdBootForced = _Pm1004dcpAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 194, 2),
    _Pm1004dcpAlmNextColdBootForced_Type()
)
pm1004dcpAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmNextColdBootForced.setStatus("current")
_Pm1004dcpAlmBootUndone_Type = EkiOnOff
_Pm1004dcpAlmBootUndone_Object = MibScalar
pm1004dcpAlmBootUndone = _Pm1004dcpAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 194, 3),
    _Pm1004dcpAlmBootUndone_Type()
)
pm1004dcpAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmBootUndone.setStatus("current")
_Pm1004dcpAlmResetHwInitFail_Type = EkiOnOff
_Pm1004dcpAlmResetHwInitFail_Object = MibScalar
pm1004dcpAlmResetHwInitFail = _Pm1004dcpAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 194, 4),
    _Pm1004dcpAlmResetHwInitFail_Type()
)
pm1004dcpAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmResetHwInitFail.setStatus("current")
_Pm1004dcpAlmSwInitFail_Type = EkiOnOff
_Pm1004dcpAlmSwInitFail_Object = MibScalar
pm1004dcpAlmSwInitFail = _Pm1004dcpAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 194, 5),
    _Pm1004dcpAlmSwInitFail_Type()
)
pm1004dcpAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmSwInitFail.setStatus("current")
_Pm1004dcpAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm1004dcpAlmmodInitFailLevel3 = _Pm1004dcpAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195)
)
_Pm1004dcpAlmGwIdentFail_Type = EkiOnOff
_Pm1004dcpAlmGwIdentFail_Object = MibScalar
pm1004dcpAlmGwIdentFail = _Pm1004dcpAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 1),
    _Pm1004dcpAlmGwIdentFail_Type()
)
pm1004dcpAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmGwIdentFail.setStatus("current")
_Pm1004dcpAlmObmTypeReadFail_Type = EkiOnOff
_Pm1004dcpAlmObmTypeReadFail_Object = MibScalar
pm1004dcpAlmObmTypeReadFail = _Pm1004dcpAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 2),
    _Pm1004dcpAlmObmTypeReadFail_Type()
)
pm1004dcpAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmObmTypeReadFail.setStatus("current")
_Pm1004dcpAlmInitModuleFail_Type = EkiOnOff
_Pm1004dcpAlmInitModuleFail_Object = MibScalar
pm1004dcpAlmInitModuleFail = _Pm1004dcpAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 3),
    _Pm1004dcpAlmInitModuleFail_Type()
)
pm1004dcpAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmInitModuleFail.setStatus("current")
_Pm1004dcpAlmXfp1InitFail_Type = EkiOnOff
_Pm1004dcpAlmXfp1InitFail_Object = MibScalar
pm1004dcpAlmXfp1InitFail = _Pm1004dcpAlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 5),
    _Pm1004dcpAlmXfp1InitFail_Type()
)
pm1004dcpAlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmXfp1InitFail.setStatus("current")
_Pm1004dcpAlmXfp2InitFail_Type = EkiOnOff
_Pm1004dcpAlmXfp2InitFail_Object = MibScalar
pm1004dcpAlmXfp2InitFail = _Pm1004dcpAlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 6),
    _Pm1004dcpAlmXfp2InitFail_Type()
)
pm1004dcpAlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmXfp2InitFail.setStatus("current")
_Pm1004dcpAlmLine1InitFail_Type = EkiOnOff
_Pm1004dcpAlmLine1InitFail_Object = MibScalar
pm1004dcpAlmLine1InitFail = _Pm1004dcpAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 7),
    _Pm1004dcpAlmLine1InitFail_Type()
)
pm1004dcpAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLine1InitFail.setStatus("current")
_Pm1004dcpAlmLine2InitFail_Type = EkiOnOff
_Pm1004dcpAlmLine2InitFail_Object = MibScalar
pm1004dcpAlmLine2InitFail = _Pm1004dcpAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 8),
    _Pm1004dcpAlmLine2InitFail_Type()
)
pm1004dcpAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLine2InitFail.setStatus("current")
_Pm1004dcpAlmClient1InitFail_Type = EkiOnOff
_Pm1004dcpAlmClient1InitFail_Object = MibScalar
pm1004dcpAlmClient1InitFail = _Pm1004dcpAlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 9),
    _Pm1004dcpAlmClient1InitFail_Type()
)
pm1004dcpAlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClient1InitFail.setStatus("current")
_Pm1004dcpAlmClient2InitFail_Type = EkiOnOff
_Pm1004dcpAlmClient2InitFail_Object = MibScalar
pm1004dcpAlmClient2InitFail = _Pm1004dcpAlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 10),
    _Pm1004dcpAlmClient2InitFail_Type()
)
pm1004dcpAlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClient2InitFail.setStatus("current")
_Pm1004dcpAlmClient3InitFail_Type = EkiOnOff
_Pm1004dcpAlmClient3InitFail_Object = MibScalar
pm1004dcpAlmClient3InitFail = _Pm1004dcpAlmClient3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 11),
    _Pm1004dcpAlmClient3InitFail_Type()
)
pm1004dcpAlmClient3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClient3InitFail.setStatus("current")
_Pm1004dcpAlmClient4InitFail_Type = EkiOnOff
_Pm1004dcpAlmClient4InitFail_Object = MibScalar
pm1004dcpAlmClient4InitFail = _Pm1004dcpAlmClient4InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 195, 12),
    _Pm1004dcpAlmClient4InitFail_Type()
)
pm1004dcpAlmClient4InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClient4InitFail.setStatus("current")
_Pm1004dcpAlmadddropTsClientRxProt_ObjectIdentity = ObjectIdentity
pm1004dcpAlmadddropTsClientRxProt = _Pm1004dcpAlmadddropTsClientRxProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 198)
)
_Pm1004dcpAlmAdddropClient1West_Type = EkiOnOff
_Pm1004dcpAlmAdddropClient1West_Object = MibScalar
pm1004dcpAlmAdddropClient1West = _Pm1004dcpAlmAdddropClient1West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 198, 1),
    _Pm1004dcpAlmAdddropClient1West_Type()
)
pm1004dcpAlmAdddropClient1West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmAdddropClient1West.setStatus("current")
_Pm1004dcpAlmAdddropClient2West_Type = EkiOnOff
_Pm1004dcpAlmAdddropClient2West_Object = MibScalar
pm1004dcpAlmAdddropClient2West = _Pm1004dcpAlmAdddropClient2West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 198, 2),
    _Pm1004dcpAlmAdddropClient2West_Type()
)
pm1004dcpAlmAdddropClient2West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmAdddropClient2West.setStatus("current")
_Pm1004dcpAlmAdddropClient3West_Type = EkiOnOff
_Pm1004dcpAlmAdddropClient3West_Object = MibScalar
pm1004dcpAlmAdddropClient3West = _Pm1004dcpAlmAdddropClient3West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 198, 3),
    _Pm1004dcpAlmAdddropClient3West_Type()
)
pm1004dcpAlmAdddropClient3West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmAdddropClient3West.setStatus("current")
_Pm1004dcpAlmAdddropClient4West_Type = EkiOnOff
_Pm1004dcpAlmAdddropClient4West_Object = MibScalar
pm1004dcpAlmAdddropClient4West = _Pm1004dcpAlmAdddropClient4West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 198, 4),
    _Pm1004dcpAlmAdddropClient4West_Type()
)
pm1004dcpAlmAdddropClient4West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmAdddropClient4West.setStatus("current")
_Pm1004dcpAlmAdddropClient1East_Type = EkiOnOff
_Pm1004dcpAlmAdddropClient1East_Object = MibScalar
pm1004dcpAlmAdddropClient1East = _Pm1004dcpAlmAdddropClient1East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 198, 9),
    _Pm1004dcpAlmAdddropClient1East_Type()
)
pm1004dcpAlmAdddropClient1East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmAdddropClient1East.setStatus("current")
_Pm1004dcpAlmAdddropClient2East_Type = EkiOnOff
_Pm1004dcpAlmAdddropClient2East_Object = MibScalar
pm1004dcpAlmAdddropClient2East = _Pm1004dcpAlmAdddropClient2East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 198, 10),
    _Pm1004dcpAlmAdddropClient2East_Type()
)
pm1004dcpAlmAdddropClient2East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmAdddropClient2East.setStatus("current")
_Pm1004dcpAlmAdddropClient3East_Type = EkiOnOff
_Pm1004dcpAlmAdddropClient3East_Object = MibScalar
pm1004dcpAlmAdddropClient3East = _Pm1004dcpAlmAdddropClient3East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 198, 11),
    _Pm1004dcpAlmAdddropClient3East_Type()
)
pm1004dcpAlmAdddropClient3East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmAdddropClient3East.setStatus("current")
_Pm1004dcpAlmAdddropClient4East_Type = EkiOnOff
_Pm1004dcpAlmAdddropClient4East_Object = MibScalar
pm1004dcpAlmAdddropClient4East = _Pm1004dcpAlmAdddropClient4East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 2, 198, 12),
    _Pm1004dcpAlmAdddropClient4East_Type()
)
pm1004dcpAlmAdddropClient4East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmAdddropClient4East.setStatus("current")
_Pm1004dcpAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1004dcpAlmOtherCrit = _Pm1004dcpAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 3)
)
_Pm1004dcpAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1004dcpAlmsynthAlm0 = _Pm1004dcpAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 3, 0)
)
_Pm1004dcpAlmModGlobFail_Type = EkiOnOff
_Pm1004dcpAlmModGlobFail_Object = MibScalar
pm1004dcpAlmModGlobFail = _Pm1004dcpAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 3, 0, 9),
    _Pm1004dcpAlmModGlobFail_Type()
)
pm1004dcpAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmModGlobFail.setStatus("current")
_Pm1004dcpAlmDefFuseA_Type = EkiOnOff
_Pm1004dcpAlmDefFuseA_Object = MibScalar
pm1004dcpAlmDefFuseA = _Pm1004dcpAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 3, 0, 15),
    _Pm1004dcpAlmDefFuseA_Type()
)
pm1004dcpAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDefFuseA.setStatus("current")
_Pm1004dcpAlmDefFuseB_Type = EkiOnOff
_Pm1004dcpAlmDefFuseB_Object = MibScalar
pm1004dcpAlmDefFuseB = _Pm1004dcpAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 1, 3, 0, 16),
    _Pm1004dcpAlmDefFuseB_Type()
)
pm1004dcpAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDefFuseB.setStatus("current")
_Pm1004dcpAlmClient_ObjectIdentity = ObjectIdentity
pm1004dcpAlmClient = _Pm1004dcpAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2)
)
_Pm1004dcpAlmClientNurg_ObjectIdentity = ObjectIdentity
pm1004dcpAlmClientNurg = _Pm1004dcpAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1)
)
_Pm1004dcpAlmsfpWarnDdmTable_Object = MibTable
pm1004dcpAlmsfpWarnDdmTable = _Pm1004dcpAlmsfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmsfpWarnDdmTable.setStatus("current")
_Pm1004dcpAlmsfpWarnDdmEntry_Object = MibTableRow
pm1004dcpAlmsfpWarnDdmEntry = _Pm1004dcpAlmsfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1)
)
pm1004dcpAlmsfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmsfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmsfpWarnDdmEntry.setStatus("current")


class _Pm1004dcpAlmsfpWarnDdmIndex_Type(Integer32):
    """Custom type pm1004dcpAlmsfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmsfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmsfpWarnDdmIndex_Object = MibTableColumn
pm1004dcpAlmsfpWarnDdmIndex = _Pm1004dcpAlmsfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 1),
    _Pm1004dcpAlmsfpWarnDdmIndex_Type()
)
pm1004dcpAlmsfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmsfpWarnDdmIndex.setStatus("current")
_Pm1004dcpAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm1004dcpAlmTxPwLowWngPortn_Object = MibTableColumn
pm1004dcpAlmTxPwLowWngPortn = _Pm1004dcpAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 2),
    _Pm1004dcpAlmTxPwLowWngPortn_Type()
)
pm1004dcpAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxPwLowWngPortn.setStatus("current")
_Pm1004dcpAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm1004dcpAlmTxPwrHighWngPortn_Object = MibTableColumn
pm1004dcpAlmTxPwrHighWngPortn = _Pm1004dcpAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 3),
    _Pm1004dcpAlmTxPwrHighWngPortn_Type()
)
pm1004dcpAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxPwrHighWngPortn.setStatus("current")
_Pm1004dcpAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm1004dcpAlmTxBiasLowWngPortn_Object = MibTableColumn
pm1004dcpAlmTxBiasLowWngPortn = _Pm1004dcpAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 4),
    _Pm1004dcpAlmTxBiasLowWngPortn_Type()
)
pm1004dcpAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxBiasLowWngPortn.setStatus("current")
_Pm1004dcpAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm1004dcpAlmTxBiasHighWngPortn_Object = MibTableColumn
pm1004dcpAlmTxBiasHighWngPortn = _Pm1004dcpAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 5),
    _Pm1004dcpAlmTxBiasHighWngPortn_Type()
)
pm1004dcpAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxBiasHighWngPortn.setStatus("current")
_Pm1004dcpAlmVccLowWngPortn_Type = EkiOnOff
_Pm1004dcpAlmVccLowWngPortn_Object = MibTableColumn
pm1004dcpAlmVccLowWngPortn = _Pm1004dcpAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 6),
    _Pm1004dcpAlmVccLowWngPortn_Type()
)
pm1004dcpAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVccLowWngPortn.setStatus("current")
_Pm1004dcpAlmVccHighWngPortn_Type = EkiOnOff
_Pm1004dcpAlmVccHighWngPortn_Object = MibTableColumn
pm1004dcpAlmVccHighWngPortn = _Pm1004dcpAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 7),
    _Pm1004dcpAlmVccHighWngPortn_Type()
)
pm1004dcpAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVccHighWngPortn.setStatus("current")
_Pm1004dcpAlmTempLowWngPortn_Type = EkiOnOff
_Pm1004dcpAlmTempLowWngPortn_Object = MibTableColumn
pm1004dcpAlmTempLowWngPortn = _Pm1004dcpAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 8),
    _Pm1004dcpAlmTempLowWngPortn_Type()
)
pm1004dcpAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTempLowWngPortn.setStatus("current")
_Pm1004dcpAlmTempHighWngPortn_Type = EkiOnOff
_Pm1004dcpAlmTempHighWngPortn_Object = MibTableColumn
pm1004dcpAlmTempHighWngPortn = _Pm1004dcpAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 9),
    _Pm1004dcpAlmTempHighWngPortn_Type()
)
pm1004dcpAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTempHighWngPortn.setStatus("current")
_Pm1004dcpAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm1004dcpAlmRxPwrLowWngPortn_Object = MibTableColumn
pm1004dcpAlmRxPwrLowWngPortn = _Pm1004dcpAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 16),
    _Pm1004dcpAlmRxPwrLowWngPortn_Type()
)
pm1004dcpAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxPwrLowWngPortn.setStatus("current")
_Pm1004dcpAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm1004dcpAlmRxPwrHighWngPortn_Object = MibTableColumn
pm1004dcpAlmRxPwrHighWngPortn = _Pm1004dcpAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 48, 1, 17),
    _Pm1004dcpAlmRxPwrHighWngPortn_Type()
)
pm1004dcpAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxPwrHighWngPortn.setStatus("current")
_Pm1004dcpAlmk1K2ClientTable_Object = MibTable
pm1004dcpAlmk1K2ClientTable = _Pm1004dcpAlmk1K2ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 96)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmk1K2ClientTable.setStatus("current")
_Pm1004dcpAlmk1K2ClientEntry_Object = MibTableRow
pm1004dcpAlmk1K2ClientEntry = _Pm1004dcpAlmk1K2ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 96, 1)
)
pm1004dcpAlmk1K2ClientEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmk1K2ClientIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmk1K2ClientEntry.setStatus("current")


class _Pm1004dcpAlmk1K2ClientIndex_Type(Integer32):
    """Custom type pm1004dcpAlmk1K2ClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmk1K2ClientIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmk1K2ClientIndex_Object = MibTableColumn
pm1004dcpAlmk1K2ClientIndex = _Pm1004dcpAlmk1K2ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 96, 1, 1),
    _Pm1004dcpAlmk1K2ClientIndex_Type()
)
pm1004dcpAlmk1K2ClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmk1K2ClientIndex.setStatus("current")


class _Pm1004dcpAlmk1K2ClientPortn_Type(Integer32):
    """Custom type pm1004dcpAlmk1K2ClientPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpAlmk1K2ClientPortn_Type.__name__ = "Integer32"
_Pm1004dcpAlmk1K2ClientPortn_Object = MibTableColumn
pm1004dcpAlmk1K2ClientPortn = _Pm1004dcpAlmk1K2ClientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 1, 96, 1, 2),
    _Pm1004dcpAlmk1K2ClientPortn_Type()
)
pm1004dcpAlmk1K2ClientPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmk1K2ClientPortn.setStatus("current")
_Pm1004dcpAlmClientUrg_ObjectIdentity = ObjectIdentity
pm1004dcpAlmClientUrg = _Pm1004dcpAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2)
)
_Pm1004dcpAlmsfpAlmDdmTable_Object = MibTable
pm1004dcpAlmsfpAlmDdmTable = _Pm1004dcpAlmsfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmsfpAlmDdmTable.setStatus("current")
_Pm1004dcpAlmsfpAlmDdmEntry_Object = MibTableRow
pm1004dcpAlmsfpAlmDdmEntry = _Pm1004dcpAlmsfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1)
)
pm1004dcpAlmsfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmsfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmsfpAlmDdmEntry.setStatus("current")


class _Pm1004dcpAlmsfpAlmDdmIndex_Type(Integer32):
    """Custom type pm1004dcpAlmsfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmsfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmsfpAlmDdmIndex_Object = MibTableColumn
pm1004dcpAlmsfpAlmDdmIndex = _Pm1004dcpAlmsfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 1),
    _Pm1004dcpAlmsfpAlmDdmIndex_Type()
)
pm1004dcpAlmsfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmsfpAlmDdmIndex.setStatus("current")
_Pm1004dcpAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm1004dcpAlmTxPwrLowAlaPortn = _Pm1004dcpAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 2),
    _Pm1004dcpAlmTxPwrLowAlaPortn_Type()
)
pm1004dcpAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxPwrLowAlaPortn.setStatus("current")
_Pm1004dcpAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm1004dcpAlmTxPwrHighAlaPortn = _Pm1004dcpAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 3),
    _Pm1004dcpAlmTxPwrHighAlaPortn_Type()
)
pm1004dcpAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxPwrHighAlaPortn.setStatus("current")
_Pm1004dcpAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm1004dcpAlmTxBiasLowAlaPortn = _Pm1004dcpAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 4),
    _Pm1004dcpAlmTxBiasLowAlaPortn_Type()
)
pm1004dcpAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxBiasLowAlaPortn.setStatus("current")
_Pm1004dcpAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm1004dcpAlmTxBiasHighAlaPortn = _Pm1004dcpAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 5),
    _Pm1004dcpAlmTxBiasHighAlaPortn_Type()
)
pm1004dcpAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxBiasHighAlaPortn.setStatus("current")
_Pm1004dcpAlmVccLowAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmVccLowAlaPortn_Object = MibTableColumn
pm1004dcpAlmVccLowAlaPortn = _Pm1004dcpAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 6),
    _Pm1004dcpAlmVccLowAlaPortn_Type()
)
pm1004dcpAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVccLowAlaPortn.setStatus("current")
_Pm1004dcpAlmVccHighAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmVccHighAlaPortn_Object = MibTableColumn
pm1004dcpAlmVccHighAlaPortn = _Pm1004dcpAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 7),
    _Pm1004dcpAlmVccHighAlaPortn_Type()
)
pm1004dcpAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVccHighAlaPortn.setStatus("current")
_Pm1004dcpAlmTempLowAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmTempLowAlaPortn_Object = MibTableColumn
pm1004dcpAlmTempLowAlaPortn = _Pm1004dcpAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 8),
    _Pm1004dcpAlmTempLowAlaPortn_Type()
)
pm1004dcpAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTempLowAlaPortn.setStatus("current")
_Pm1004dcpAlmTempHighAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmTempHighAlaPortn_Object = MibTableColumn
pm1004dcpAlmTempHighAlaPortn = _Pm1004dcpAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 9),
    _Pm1004dcpAlmTempHighAlaPortn_Type()
)
pm1004dcpAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTempHighAlaPortn.setStatus("current")
_Pm1004dcpAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm1004dcpAlmRxPwrLowAlaPortn = _Pm1004dcpAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 16),
    _Pm1004dcpAlmRxPwrLowAlaPortn_Type()
)
pm1004dcpAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxPwrLowAlaPortn.setStatus("current")
_Pm1004dcpAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm1004dcpAlmRxPwrHighAlaPortn = _Pm1004dcpAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 2, 32, 1, 17),
    _Pm1004dcpAlmRxPwrHighAlaPortn_Type()
)
pm1004dcpAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxPwrHighAlaPortn.setStatus("current")
_Pm1004dcpAlmClientCrit_ObjectIdentity = ObjectIdentity
pm1004dcpAlmClientCrit = _Pm1004dcpAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3)
)
_Pm1004dcpAlmsynthAlmPortTable_Object = MibTable
pm1004dcpAlmsynthAlmPortTable = _Pm1004dcpAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmsynthAlmPortTable.setStatus("current")
_Pm1004dcpAlmsynthAlmPortEntry_Object = MibTableRow
pm1004dcpAlmsynthAlmPortEntry = _Pm1004dcpAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1)
)
pm1004dcpAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmsynthAlmPortEntry.setStatus("current")


class _Pm1004dcpAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm1004dcpAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmsynthAlmPortIndex_Object = MibTableColumn
pm1004dcpAlmsynthAlmPortIndex = _Pm1004dcpAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 1),
    _Pm1004dcpAlmsynthAlmPortIndex_Type()
)
pm1004dcpAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmsynthAlmPortIndex.setStatus("current")
_Pm1004dcpAlmSfpAbsentPortn_Type = EkiOnOff
_Pm1004dcpAlmSfpAbsentPortn_Object = MibTableColumn
pm1004dcpAlmSfpAbsentPortn = _Pm1004dcpAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 2),
    _Pm1004dcpAlmSfpAbsentPortn_Type()
)
pm1004dcpAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmSfpAbsentPortn.setStatus("current")
_Pm1004dcpAlmDdmAbsentPortn_Type = EkiOnOff
_Pm1004dcpAlmDdmAbsentPortn_Object = MibTableColumn
pm1004dcpAlmDdmAbsentPortn = _Pm1004dcpAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 3),
    _Pm1004dcpAlmDdmAbsentPortn_Type()
)
pm1004dcpAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDdmAbsentPortn.setStatus("current")
_Pm1004dcpAlmHwFailAccPortn_Type = EkiOnOff
_Pm1004dcpAlmHwFailAccPortn_Object = MibTableColumn
pm1004dcpAlmHwFailAccPortn = _Pm1004dcpAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 5),
    _Pm1004dcpAlmHwFailAccPortn_Type()
)
pm1004dcpAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmHwFailAccPortn.setStatus("current")
_Pm1004dcpAlmDwLsdPortn_Type = EkiOnOff
_Pm1004dcpAlmDwLsdPortn_Object = MibTableColumn
pm1004dcpAlmDwLsdPortn = _Pm1004dcpAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 6),
    _Pm1004dcpAlmDwLsdPortn_Type()
)
pm1004dcpAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwLsdPortn.setStatus("current")
_Pm1004dcpAlmClientLocalOosPortn_Type = EkiOnOff
_Pm1004dcpAlmClientLocalOosPortn_Object = MibTableColumn
pm1004dcpAlmClientLocalOosPortn = _Pm1004dcpAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 7),
    _Pm1004dcpAlmClientLocalOosPortn_Type()
)
pm1004dcpAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClientLocalOosPortn.setStatus("current")
_Pm1004dcpAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm1004dcpAlmClientRemoteOosPortn_Object = MibTableColumn
pm1004dcpAlmClientRemoteOosPortn = _Pm1004dcpAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 8),
    _Pm1004dcpAlmClientRemoteOosPortn_Type()
)
pm1004dcpAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClientRemoteOosPortn.setStatus("current")
_Pm1004dcpAlmDwCaisPortn_Type = EkiOnOff
_Pm1004dcpAlmDwCaisPortn_Object = MibTableColumn
pm1004dcpAlmDwCaisPortn = _Pm1004dcpAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 9),
    _Pm1004dcpAlmDwCaisPortn_Type()
)
pm1004dcpAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwCaisPortn.setStatus("current")
_Pm1004dcpAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmSfpDdmWarningPortn_Object = MibTableColumn
pm1004dcpAlmSfpDdmWarningPortn = _Pm1004dcpAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 10),
    _Pm1004dcpAlmSfpDdmWarningPortn_Type()
)
pm1004dcpAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmSfpDdmWarningPortn.setStatus("current")
_Pm1004dcpAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm1004dcpAlmSfpDdmAlmPortn_Object = MibTableColumn
pm1004dcpAlmSfpDdmAlmPortn = _Pm1004dcpAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 11),
    _Pm1004dcpAlmSfpDdmAlmPortn_Type()
)
pm1004dcpAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmSfpDdmAlmPortn.setStatus("current")
_Pm1004dcpAlmFailAccPortn_Type = EkiOnOff
_Pm1004dcpAlmFailAccPortn_Object = MibTableColumn
pm1004dcpAlmFailAccPortn = _Pm1004dcpAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 13),
    _Pm1004dcpAlmFailAccPortn_Type()
)
pm1004dcpAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmFailAccPortn.setStatus("current")
_Pm1004dcpAlmClientActivePortn_Type = EkiOnOff
_Pm1004dcpAlmClientActivePortn_Object = MibTableColumn
pm1004dcpAlmClientActivePortn = _Pm1004dcpAlmClientActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 16),
    _Pm1004dcpAlmClientActivePortn_Type()
)
pm1004dcpAlmClientActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClientActivePortn.setStatus("current")
_Pm1004dcpAlmUpCsfPortn_Type = EkiOnOff
_Pm1004dcpAlmUpCsfPortn_Object = MibTableColumn
pm1004dcpAlmUpCsfPortn = _Pm1004dcpAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 8, 1, 17),
    _Pm1004dcpAlmUpCsfPortn_Type()
)
pm1004dcpAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmUpCsfPortn.setStatus("current")
_Pm1004dcpAlmaccessioAlmTable_Object = MibTable
pm1004dcpAlmaccessioAlmTable = _Pm1004dcpAlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmaccessioAlmTable.setStatus("current")
_Pm1004dcpAlmaccessioAlmEntry_Object = MibTableRow
pm1004dcpAlmaccessioAlmEntry = _Pm1004dcpAlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 16, 1)
)
pm1004dcpAlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmaccessioAlmEntry.setStatus("current")


class _Pm1004dcpAlmaccessioAlmIndex_Type(Integer32):
    """Custom type pm1004dcpAlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmaccessioAlmIndex_Object = MibTableColumn
pm1004dcpAlmaccessioAlmIndex = _Pm1004dcpAlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 16, 1, 1),
    _Pm1004dcpAlmaccessioAlmIndex_Type()
)
pm1004dcpAlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmaccessioAlmIndex.setStatus("current")
_Pm1004dcpAlmDwLasFailPortn_Type = EkiOnOff
_Pm1004dcpAlmDwLasFailPortn_Object = MibTableColumn
pm1004dcpAlmDwLasFailPortn = _Pm1004dcpAlmDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 16, 1, 2),
    _Pm1004dcpAlmDwLasFailPortn_Type()
)
pm1004dcpAlmDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwLasFailPortn.setStatus("current")
_Pm1004dcpAlmUpLosPortn_Type = EkiOnOff
_Pm1004dcpAlmUpLosPortn_Object = MibTableColumn
pm1004dcpAlmUpLosPortn = _Pm1004dcpAlmUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 16, 1, 5),
    _Pm1004dcpAlmUpLosPortn_Type()
)
pm1004dcpAlmUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmUpLosPortn.setStatus("current")
_Pm1004dcpAlmmapperDeAlmTable_Object = MibTable
pm1004dcpAlmmapperDeAlmTable = _Pm1004dcpAlmmapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmmapperDeAlmTable.setStatus("current")
_Pm1004dcpAlmmapperDeAlmEntry_Object = MibTableRow
pm1004dcpAlmmapperDeAlmEntry = _Pm1004dcpAlmmapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 72, 1)
)
pm1004dcpAlmmapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmmapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmmapperDeAlmEntry.setStatus("current")


class _Pm1004dcpAlmmapperDeAlmIndex_Type(Integer32):
    """Custom type pm1004dcpAlmmapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmmapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmmapperDeAlmIndex_Object = MibTableColumn
pm1004dcpAlmmapperDeAlmIndex = _Pm1004dcpAlmmapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 72, 1, 1),
    _Pm1004dcpAlmmapperDeAlmIndex_Type()
)
pm1004dcpAlmmapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmmapperDeAlmIndex.setStatus("current")
_Pm1004dcpAlmUpAccOosPortn_Type = EkiOnOff
_Pm1004dcpAlmUpAccOosPortn_Object = MibTableColumn
pm1004dcpAlmUpAccOosPortn = _Pm1004dcpAlmUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 72, 1, 2),
    _Pm1004dcpAlmUpAccOosPortn_Type()
)
pm1004dcpAlmUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmUpAccOosPortn.setStatus("current")
_Pm1004dcpAlmUpBufferOvlPortn_Type = EkiOnOff
_Pm1004dcpAlmUpBufferOvlPortn_Object = MibTableColumn
pm1004dcpAlmUpBufferOvlPortn = _Pm1004dcpAlmUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 72, 1, 11),
    _Pm1004dcpAlmUpBufferOvlPortn_Type()
)
pm1004dcpAlmUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmUpBufferOvlPortn.setStatus("current")
_Pm1004dcpAlmDwCsfDetPortn_Type = EkiOnOff
_Pm1004dcpAlmDwCsfDetPortn_Object = MibTableColumn
pm1004dcpAlmDwCsfDetPortn = _Pm1004dcpAlmDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 72, 1, 12),
    _Pm1004dcpAlmDwCsfDetPortn_Type()
)
pm1004dcpAlmDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwCsfDetPortn.setStatus("current")
_Pm1004dcpAlmDwBufferOvlPortn_Type = EkiOnOff
_Pm1004dcpAlmDwBufferOvlPortn_Object = MibTableColumn
pm1004dcpAlmDwBufferOvlPortn = _Pm1004dcpAlmDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 72, 1, 15),
    _Pm1004dcpAlmDwBufferOvlPortn_Type()
)
pm1004dcpAlmDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwBufferOvlPortn.setStatus("current")
_Pm1004dcpAlmaccessioSdhAlarmTable_Object = MibTable
pm1004dcpAlmaccessioSdhAlarmTable = _Pm1004dcpAlmaccessioSdhAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 104)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmaccessioSdhAlarmTable.setStatus("current")
_Pm1004dcpAlmaccessioSdhAlarmEntry_Object = MibTableRow
pm1004dcpAlmaccessioSdhAlarmEntry = _Pm1004dcpAlmaccessioSdhAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 104, 1)
)
pm1004dcpAlmaccessioSdhAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmaccessioSdhAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmaccessioSdhAlarmEntry.setStatus("current")


class _Pm1004dcpAlmaccessioSdhAlarmIndex_Type(Integer32):
    """Custom type pm1004dcpAlmaccessioSdhAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmaccessioSdhAlarmIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmaccessioSdhAlarmIndex_Object = MibTableColumn
pm1004dcpAlmaccessioSdhAlarmIndex = _Pm1004dcpAlmaccessioSdhAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 104, 1, 1),
    _Pm1004dcpAlmaccessioSdhAlarmIndex_Type()
)
pm1004dcpAlmaccessioSdhAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmaccessioSdhAlarmIndex.setStatus("current")
_Pm1004dcpAlmFifoErrPortn_Type = EkiOnOff
_Pm1004dcpAlmFifoErrPortn_Object = MibTableColumn
pm1004dcpAlmFifoErrPortn = _Pm1004dcpAlmFifoErrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 104, 1, 3),
    _Pm1004dcpAlmFifoErrPortn_Type()
)
pm1004dcpAlmFifoErrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmFifoErrPortn.setStatus("current")
_Pm1004dcpAlmRxLossOfLockPortn_Type = EkiOnOff
_Pm1004dcpAlmRxLossOfLockPortn_Object = MibTableColumn
pm1004dcpAlmRxLossOfLockPortn = _Pm1004dcpAlmRxLossOfLockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 104, 1, 4),
    _Pm1004dcpAlmRxLossOfLockPortn_Type()
)
pm1004dcpAlmRxLossOfLockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxLossOfLockPortn.setStatus("current")
_Pm1004dcpAlmTxLossOfLockPortn_Type = EkiOnOff
_Pm1004dcpAlmTxLossOfLockPortn_Object = MibTableColumn
pm1004dcpAlmTxLossOfLockPortn = _Pm1004dcpAlmTxLossOfLockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 104, 1, 5),
    _Pm1004dcpAlmTxLossOfLockPortn_Type()
)
pm1004dcpAlmTxLossOfLockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxLossOfLockPortn.setStatus("current")
_Pm1004dcpAlmClientAisDetPortn_Type = EkiOnOff
_Pm1004dcpAlmClientAisDetPortn_Object = MibTableColumn
pm1004dcpAlmClientAisDetPortn = _Pm1004dcpAlmClientAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 104, 1, 6),
    _Pm1004dcpAlmClientAisDetPortn_Type()
)
pm1004dcpAlmClientAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClientAisDetPortn.setStatus("current")
_Pm1004dcpAlmClientRdiDetPortn_Type = EkiOnOff
_Pm1004dcpAlmClientRdiDetPortn_Object = MibTableColumn
pm1004dcpAlmClientRdiDetPortn = _Pm1004dcpAlmClientRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 104, 1, 7),
    _Pm1004dcpAlmClientRdiDetPortn_Type()
)
pm1004dcpAlmClientRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClientRdiDetPortn.setStatus("current")
_Pm1004dcpAlmClientOofPortn_Type = EkiOnOff
_Pm1004dcpAlmClientOofPortn_Object = MibTableColumn
pm1004dcpAlmClientOofPortn = _Pm1004dcpAlmClientOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 2, 3, 104, 1, 8),
    _Pm1004dcpAlmClientOofPortn_Type()
)
pm1004dcpAlmClientOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmClientOofPortn.setStatus("current")
_Pm1004dcpAlmLine_ObjectIdentity = ObjectIdentity
pm1004dcpAlmLine = _Pm1004dcpAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3)
)
_Pm1004dcpAlmLineNurg_ObjectIdentity = ObjectIdentity
pm1004dcpAlmLineNurg = _Pm1004dcpAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1)
)
_Pm1004dcpAlmlineXfp1WarningsTable_Object = MibTable
pm1004dcpAlmlineXfp1WarningsTable = _Pm1004dcpAlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1WarningsTable.setStatus("current")
_Pm1004dcpAlmlineXfp1WarningsEntry_Object = MibTableRow
pm1004dcpAlmlineXfp1WarningsEntry = _Pm1004dcpAlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1)
)
pm1004dcpAlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1WarningsEntry.setStatus("current")


class _Pm1004dcpAlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pm1004dcpAlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmlineXfp1WarningsIndex_Object = MibTableColumn
pm1004dcpAlmlineXfp1WarningsIndex = _Pm1004dcpAlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1, 1),
    _Pm1004dcpAlmlineXfp1WarningsIndex_Type()
)
pm1004dcpAlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1WarningsIndex.setStatus("current")
_Pm1004dcpAlmTxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmTxPowerLowWarningPortn_Object = MibTableColumn
pm1004dcpAlmTxPowerLowWarningPortn = _Pm1004dcpAlmTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1, 2),
    _Pm1004dcpAlmTxPowerLowWarningPortn_Type()
)
pm1004dcpAlmTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxPowerLowWarningPortn.setStatus("current")
_Pm1004dcpAlmTxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmTxPowerHighWarningPortn_Object = MibTableColumn
pm1004dcpAlmTxPowerHighWarningPortn = _Pm1004dcpAlmTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1, 3),
    _Pm1004dcpAlmTxPowerHighWarningPortn_Type()
)
pm1004dcpAlmTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxPowerHighWarningPortn.setStatus("current")
_Pm1004dcpAlmTxBiasLowWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmTxBiasLowWarningPortn_Object = MibTableColumn
pm1004dcpAlmTxBiasLowWarningPortn = _Pm1004dcpAlmTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1, 4),
    _Pm1004dcpAlmTxBiasLowWarningPortn_Type()
)
pm1004dcpAlmTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxBiasLowWarningPortn.setStatus("current")
_Pm1004dcpAlmTxBiasHighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmTxBiasHighWarningPortn_Object = MibTableColumn
pm1004dcpAlmTxBiasHighWarningPortn = _Pm1004dcpAlmTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1, 5),
    _Pm1004dcpAlmTxBiasHighWarningPortn_Type()
)
pm1004dcpAlmTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxBiasHighWarningPortn.setStatus("current")
_Pm1004dcpAlmTempLowWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmTempLowWarningPortn_Object = MibTableColumn
pm1004dcpAlmTempLowWarningPortn = _Pm1004dcpAlmTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1, 8),
    _Pm1004dcpAlmTempLowWarningPortn_Type()
)
pm1004dcpAlmTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTempLowWarningPortn.setStatus("current")
_Pm1004dcpAlmTempHighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmTempHighWarningPortn_Object = MibTableColumn
pm1004dcpAlmTempHighWarningPortn = _Pm1004dcpAlmTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1, 9),
    _Pm1004dcpAlmTempHighWarningPortn_Type()
)
pm1004dcpAlmTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTempHighWarningPortn.setStatus("current")
_Pm1004dcpAlmRxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmRxPowerLowWarningPortn_Object = MibTableColumn
pm1004dcpAlmRxPowerLowWarningPortn = _Pm1004dcpAlmRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1, 16),
    _Pm1004dcpAlmRxPowerLowWarningPortn_Type()
)
pm1004dcpAlmRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxPowerLowWarningPortn.setStatus("current")
_Pm1004dcpAlmRxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmRxPowerHighWarningPortn_Object = MibTableColumn
pm1004dcpAlmRxPowerHighWarningPortn = _Pm1004dcpAlmRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 209, 1, 17),
    _Pm1004dcpAlmRxPowerHighWarningPortn_Type()
)
pm1004dcpAlmRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxPowerHighWarningPortn.setStatus("current")
_Pm1004dcpAlmlineOtx1TlhWarningsTable_Object = MibTable
pm1004dcpAlmlineOtx1TlhWarningsTable = _Pm1004dcpAlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineOtx1TlhWarningsTable.setStatus("current")
_Pm1004dcpAlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pm1004dcpAlmlineOtx1TlhWarningsEntry = _Pm1004dcpAlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 225, 1)
)
pm1004dcpAlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pm1004dcpAlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pm1004dcpAlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pm1004dcpAlmlineOtx1TlhWarningsIndex = _Pm1004dcpAlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 225, 1, 1),
    _Pm1004dcpAlmlineOtx1TlhWarningsIndex_Type()
)
pm1004dcpAlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pm1004dcpAlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pm1004dcpAlmLineModulatorAgingHighWarningPortn = _Pm1004dcpAlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 225, 1, 6),
    _Pm1004dcpAlmLineModulatorAgingHighWarningPortn_Type()
)
pm1004dcpAlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pm1004dcpAlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmLineAgingHighWarningPortn_Object = MibTableColumn
pm1004dcpAlmLineAgingHighWarningPortn = _Pm1004dcpAlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 225, 1, 7),
    _Pm1004dcpAlmLineAgingHighWarningPortn_Type()
)
pm1004dcpAlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineAgingHighWarningPortn.setStatus("current")
_Pm1004dcpAlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pm1004dcpAlmLineFreqDevHighWarningPortn = _Pm1004dcpAlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 225, 1, 13),
    _Pm1004dcpAlmLineFreqDevHighWarningPortn_Type()
)
pm1004dcpAlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineFreqDevHighWarningPortn.setStatus("current")
_Pm1004dcpAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm1004dcpAlmLineLaserTempHighWarningPortn = _Pm1004dcpAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 1, 225, 1, 15),
    _Pm1004dcpAlmLineLaserTempHighWarningPortn_Type()
)
pm1004dcpAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm1004dcpAlmLineUrg_ObjectIdentity = ObjectIdentity
pm1004dcpAlmLineUrg = _Pm1004dcpAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2)
)
_Pm1004dcpAlmdfrmBerTable_Object = MibTable
pm1004dcpAlmdfrmBerTable = _Pm1004dcpAlmdfrmBerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 129)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmdfrmBerTable.setStatus("current")
_Pm1004dcpAlmdfrmBerEntry_Object = MibTableRow
pm1004dcpAlmdfrmBerEntry = _Pm1004dcpAlmdfrmBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 129, 1)
)
pm1004dcpAlmdfrmBerEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmdfrmBerIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmdfrmBerEntry.setStatus("current")


class _Pm1004dcpAlmdfrmBerIndex_Type(Integer32):
    """Custom type pm1004dcpAlmdfrmBerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmdfrmBerIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmdfrmBerIndex_Object = MibTableColumn
pm1004dcpAlmdfrmBerIndex = _Pm1004dcpAlmdfrmBerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 129, 1, 1),
    _Pm1004dcpAlmdfrmBerIndex_Type()
)
pm1004dcpAlmdfrmBerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmdfrmBerIndex.setStatus("current")
_Pm1004dcpAlmLineSignalDegradePortn_Type = EkiOnOff
_Pm1004dcpAlmLineSignalDegradePortn_Object = MibTableColumn
pm1004dcpAlmLineSignalDegradePortn = _Pm1004dcpAlmLineSignalDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 129, 1, 2),
    _Pm1004dcpAlmLineSignalDegradePortn_Type()
)
pm1004dcpAlmLineSignalDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineSignalDegradePortn.setStatus("current")
_Pm1004dcpAlmLineSignalFailPortn_Type = EkiOnOff
_Pm1004dcpAlmLineSignalFailPortn_Object = MibTableColumn
pm1004dcpAlmLineSignalFailPortn = _Pm1004dcpAlmLineSignalFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 129, 1, 3),
    _Pm1004dcpAlmLineSignalFailPortn_Type()
)
pm1004dcpAlmLineSignalFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineSignalFailPortn.setStatus("current")
_Pm1004dcpAlmLineDegradePortn_Type = EkiOnOff
_Pm1004dcpAlmLineDegradePortn_Object = MibTableColumn
pm1004dcpAlmLineDegradePortn = _Pm1004dcpAlmLineDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 129, 1, 6),
    _Pm1004dcpAlmLineDegradePortn_Type()
)
pm1004dcpAlmLineDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineDegradePortn.setStatus("current")
_Pm1004dcpAlmlineXfp1AlarmTable_Object = MibTable
pm1004dcpAlmlineXfp1AlarmTable = _Pm1004dcpAlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1AlarmTable.setStatus("current")
_Pm1004dcpAlmlineXfp1AlarmEntry_Object = MibTableRow
pm1004dcpAlmlineXfp1AlarmEntry = _Pm1004dcpAlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1)
)
pm1004dcpAlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1AlarmEntry.setStatus("current")


class _Pm1004dcpAlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pm1004dcpAlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmlineXfp1AlarmIndex_Object = MibTableColumn
pm1004dcpAlmlineXfp1AlarmIndex = _Pm1004dcpAlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1, 1),
    _Pm1004dcpAlmlineXfp1AlarmIndex_Type()
)
pm1004dcpAlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1AlarmIndex.setStatus("current")
_Pm1004dcpAlmTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmTxPowerLowAlarmPortn_Object = MibTableColumn
pm1004dcpAlmTxPowerLowAlarmPortn = _Pm1004dcpAlmTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1, 2),
    _Pm1004dcpAlmTxPowerLowAlarmPortn_Type()
)
pm1004dcpAlmTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxPowerLowAlarmPortn.setStatus("current")
_Pm1004dcpAlmTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmTxPowerHighAlarmPortn_Object = MibTableColumn
pm1004dcpAlmTxPowerHighAlarmPortn = _Pm1004dcpAlmTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1, 3),
    _Pm1004dcpAlmTxPowerHighAlarmPortn_Type()
)
pm1004dcpAlmTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxPowerHighAlarmPortn.setStatus("current")
_Pm1004dcpAlmTxBiasLowAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmTxBiasLowAlarmPortn_Object = MibTableColumn
pm1004dcpAlmTxBiasLowAlarmPortn = _Pm1004dcpAlmTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1, 4),
    _Pm1004dcpAlmTxBiasLowAlarmPortn_Type()
)
pm1004dcpAlmTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxBiasLowAlarmPortn.setStatus("current")
_Pm1004dcpAlmTxBiasHighAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmTxBiasHighAlarmPortn_Object = MibTableColumn
pm1004dcpAlmTxBiasHighAlarmPortn = _Pm1004dcpAlmTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1, 5),
    _Pm1004dcpAlmTxBiasHighAlarmPortn_Type()
)
pm1004dcpAlmTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxBiasHighAlarmPortn.setStatus("current")
_Pm1004dcpAlmTempLowAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmTempLowAlarmPortn_Object = MibTableColumn
pm1004dcpAlmTempLowAlarmPortn = _Pm1004dcpAlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1, 8),
    _Pm1004dcpAlmTempLowAlarmPortn_Type()
)
pm1004dcpAlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTempLowAlarmPortn.setStatus("current")
_Pm1004dcpAlmTempHighAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmTempHighAlarmPortn_Object = MibTableColumn
pm1004dcpAlmTempHighAlarmPortn = _Pm1004dcpAlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1, 9),
    _Pm1004dcpAlmTempHighAlarmPortn_Type()
)
pm1004dcpAlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTempHighAlarmPortn.setStatus("current")
_Pm1004dcpAlmRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmRxPowerLowAlarmPortn_Object = MibTableColumn
pm1004dcpAlmRxPowerLowAlarmPortn = _Pm1004dcpAlmRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1, 16),
    _Pm1004dcpAlmRxPowerLowAlarmPortn_Type()
)
pm1004dcpAlmRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxPowerLowAlarmPortn.setStatus("current")
_Pm1004dcpAlmRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmRxPowerHighAlarmPortn_Object = MibTableColumn
pm1004dcpAlmRxPowerHighAlarmPortn = _Pm1004dcpAlmRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 208, 1, 17),
    _Pm1004dcpAlmRxPowerHighAlarmPortn_Type()
)
pm1004dcpAlmRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxPowerHighAlarmPortn.setStatus("current")
_Pm1004dcpAlmlineXfp1SupplyAlarmTable_Object = MibTable
pm1004dcpAlmlineXfp1SupplyAlarmTable = _Pm1004dcpAlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pm1004dcpAlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pm1004dcpAlmlineXfp1SupplyAlarmEntry = _Pm1004dcpAlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1)
)
pm1004dcpAlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pm1004dcpAlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pm1004dcpAlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pm1004dcpAlmlineXfp1SupplyAlarmIndex = _Pm1004dcpAlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 1),
    _Pm1004dcpAlmlineXfp1SupplyAlarmIndex_Type()
)
pm1004dcpAlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pm1004dcpAlmVee5LowAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmVee5LowAlarmPortn_Object = MibTableColumn
pm1004dcpAlmVee5LowAlarmPortn = _Pm1004dcpAlmVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 2),
    _Pm1004dcpAlmVee5LowAlarmPortn_Type()
)
pm1004dcpAlmVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVee5LowAlarmPortn.setStatus("current")
_Pm1004dcpAlmVee5HighAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmVee5HighAlarmPortn_Object = MibTableColumn
pm1004dcpAlmVee5HighAlarmPortn = _Pm1004dcpAlmVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 3),
    _Pm1004dcpAlmVee5HighAlarmPortn_Type()
)
pm1004dcpAlmVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVee5HighAlarmPortn.setStatus("current")
_Pm1004dcpAlmVcc2LowAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc2LowAlarmPortn_Object = MibTableColumn
pm1004dcpAlmVcc2LowAlarmPortn = _Pm1004dcpAlmVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 4),
    _Pm1004dcpAlmVcc2LowAlarmPortn_Type()
)
pm1004dcpAlmVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc2LowAlarmPortn.setStatus("current")
_Pm1004dcpAlmVcc2HighAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc2HighAlarmPortn_Object = MibTableColumn
pm1004dcpAlmVcc2HighAlarmPortn = _Pm1004dcpAlmVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 5),
    _Pm1004dcpAlmVcc2HighAlarmPortn_Type()
)
pm1004dcpAlmVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc2HighAlarmPortn.setStatus("current")
_Pm1004dcpAlmVcc3LowAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc3LowAlarmPortn_Object = MibTableColumn
pm1004dcpAlmVcc3LowAlarmPortn = _Pm1004dcpAlmVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 6),
    _Pm1004dcpAlmVcc3LowAlarmPortn_Type()
)
pm1004dcpAlmVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc3LowAlarmPortn.setStatus("current")
_Pm1004dcpAlmVcc3HighAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc3HighAlarmPortn_Object = MibTableColumn
pm1004dcpAlmVcc3HighAlarmPortn = _Pm1004dcpAlmVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 7),
    _Pm1004dcpAlmVcc3HighAlarmPortn_Type()
)
pm1004dcpAlmVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc3HighAlarmPortn.setStatus("current")
_Pm1004dcpAlmVcc5LowAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc5LowAlarmPortn_Object = MibTableColumn
pm1004dcpAlmVcc5LowAlarmPortn = _Pm1004dcpAlmVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 8),
    _Pm1004dcpAlmVcc5LowAlarmPortn_Type()
)
pm1004dcpAlmVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc5LowAlarmPortn.setStatus("current")
_Pm1004dcpAlmVcc5HighAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc5HighAlarmPortn_Object = MibTableColumn
pm1004dcpAlmVcc5HighAlarmPortn = _Pm1004dcpAlmVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 9),
    _Pm1004dcpAlmVcc5HighAlarmPortn_Type()
)
pm1004dcpAlmVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc5HighAlarmPortn.setStatus("current")
_Pm1004dcpAlmVee5LowWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmVee5LowWarningPortn_Object = MibTableColumn
pm1004dcpAlmVee5LowWarningPortn = _Pm1004dcpAlmVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 10),
    _Pm1004dcpAlmVee5LowWarningPortn_Type()
)
pm1004dcpAlmVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVee5LowWarningPortn.setStatus("current")
_Pm1004dcpAlmVee5HighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmVee5HighWarningPortn_Object = MibTableColumn
pm1004dcpAlmVee5HighWarningPortn = _Pm1004dcpAlmVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 11),
    _Pm1004dcpAlmVee5HighWarningPortn_Type()
)
pm1004dcpAlmVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVee5HighWarningPortn.setStatus("current")
_Pm1004dcpAlmVcc2LowWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc2LowWarningPortn_Object = MibTableColumn
pm1004dcpAlmVcc2LowWarningPortn = _Pm1004dcpAlmVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 12),
    _Pm1004dcpAlmVcc2LowWarningPortn_Type()
)
pm1004dcpAlmVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc2LowWarningPortn.setStatus("current")
_Pm1004dcpAlmVcc2HighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc2HighWarningPortn_Object = MibTableColumn
pm1004dcpAlmVcc2HighWarningPortn = _Pm1004dcpAlmVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 13),
    _Pm1004dcpAlmVcc2HighWarningPortn_Type()
)
pm1004dcpAlmVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc2HighWarningPortn.setStatus("current")
_Pm1004dcpAlmVcc3LowWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc3LowWarningPortn_Object = MibTableColumn
pm1004dcpAlmVcc3LowWarningPortn = _Pm1004dcpAlmVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 14),
    _Pm1004dcpAlmVcc3LowWarningPortn_Type()
)
pm1004dcpAlmVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc3LowWarningPortn.setStatus("current")
_Pm1004dcpAlmVcc3HighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc3HighWarningPortn_Object = MibTableColumn
pm1004dcpAlmVcc3HighWarningPortn = _Pm1004dcpAlmVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 15),
    _Pm1004dcpAlmVcc3HighWarningPortn_Type()
)
pm1004dcpAlmVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc3HighWarningPortn.setStatus("current")
_Pm1004dcpAlmVcc5LowWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc5LowWarningPortn_Object = MibTableColumn
pm1004dcpAlmVcc5LowWarningPortn = _Pm1004dcpAlmVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 16),
    _Pm1004dcpAlmVcc5LowWarningPortn_Type()
)
pm1004dcpAlmVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc5LowWarningPortn.setStatus("current")
_Pm1004dcpAlmVcc5HighWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmVcc5HighWarningPortn_Object = MibTableColumn
pm1004dcpAlmVcc5HighWarningPortn = _Pm1004dcpAlmVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 212, 1, 17),
    _Pm1004dcpAlmVcc5HighWarningPortn_Type()
)
pm1004dcpAlmVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmVcc5HighWarningPortn.setStatus("current")
_Pm1004dcpAlmlineOtx1TlhAlarmsTable_Object = MibTable
pm1004dcpAlmlineOtx1TlhAlarmsTable = _Pm1004dcpAlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pm1004dcpAlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pm1004dcpAlmlineOtx1TlhAlarmsEntry = _Pm1004dcpAlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 224, 1)
)
pm1004dcpAlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pm1004dcpAlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pm1004dcpAlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pm1004dcpAlmlineOtx1TlhAlarmsIndex = _Pm1004dcpAlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 224, 1, 1),
    _Pm1004dcpAlmlineOtx1TlhAlarmsIndex_Type()
)
pm1004dcpAlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pm1004dcpAlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pm1004dcpAlmLineModulatorAgingHighAlaPortn = _Pm1004dcpAlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 224, 1, 6),
    _Pm1004dcpAlmLineModulatorAgingHighAlaPortn_Type()
)
pm1004dcpAlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pm1004dcpAlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmLineAgingHighAlaPortn_Object = MibTableColumn
pm1004dcpAlmLineAgingHighAlaPortn = _Pm1004dcpAlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 224, 1, 7),
    _Pm1004dcpAlmLineAgingHighAlaPortn_Type()
)
pm1004dcpAlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineAgingHighAlaPortn.setStatus("current")
_Pm1004dcpAlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pm1004dcpAlmLineFreqDevHighAlaPortn = _Pm1004dcpAlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 224, 1, 13),
    _Pm1004dcpAlmLineFreqDevHighAlaPortn_Type()
)
pm1004dcpAlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineFreqDevHighAlaPortn.setStatus("current")
_Pm1004dcpAlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pm1004dcpAlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pm1004dcpAlmLineLaserTempHighAlaPortn = _Pm1004dcpAlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 2, 224, 1, 15),
    _Pm1004dcpAlmLineLaserTempHighAlaPortn_Type()
)
pm1004dcpAlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineLaserTempHighAlaPortn.setStatus("current")
_Pm1004dcpAlmLineCrit_ObjectIdentity = ObjectIdentity
pm1004dcpAlmLineCrit = _Pm1004dcpAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3)
)
_Pm1004dcpAlmsynthAlmLineTable_Object = MibTable
pm1004dcpAlmsynthAlmLineTable = _Pm1004dcpAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmsynthAlmLineTable.setStatus("current")
_Pm1004dcpAlmsynthAlmLineEntry_Object = MibTableRow
pm1004dcpAlmsynthAlmLineEntry = _Pm1004dcpAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1)
)
pm1004dcpAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmsynthAlmLineEntry.setStatus("current")


class _Pm1004dcpAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm1004dcpAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmsynthAlmLineIndex_Object = MibTableColumn
pm1004dcpAlmsynthAlmLineIndex = _Pm1004dcpAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 1),
    _Pm1004dcpAlmsynthAlmLineIndex_Type()
)
pm1004dcpAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmsynthAlmLineIndex.setStatus("current")
_Pm1004dcpAlmXfpAbsentPortn_Type = EkiOnOff
_Pm1004dcpAlmXfpAbsentPortn_Object = MibTableColumn
pm1004dcpAlmXfpAbsentPortn = _Pm1004dcpAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 2),
    _Pm1004dcpAlmXfpAbsentPortn_Type()
)
pm1004dcpAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmXfpAbsentPortn.setStatus("current")
_Pm1004dcpAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm1004dcpAlmXfpInitNotComplPortn_Object = MibTableColumn
pm1004dcpAlmXfpInitNotComplPortn = _Pm1004dcpAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 3),
    _Pm1004dcpAlmXfpInitNotComplPortn_Type()
)
pm1004dcpAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmXfpInitNotComplPortn.setStatus("current")
_Pm1004dcpAlmLineHwFailPortn_Type = EkiOnOff
_Pm1004dcpAlmLineHwFailPortn_Object = MibTableColumn
pm1004dcpAlmLineHwFailPortn = _Pm1004dcpAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 5),
    _Pm1004dcpAlmLineHwFailPortn_Type()
)
pm1004dcpAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineHwFailPortn.setStatus("current")
_Pm1004dcpAlmXfpTxOffPortn_Type = EkiOnOff
_Pm1004dcpAlmXfpTxOffPortn_Object = MibTableColumn
pm1004dcpAlmXfpTxOffPortn = _Pm1004dcpAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 6),
    _Pm1004dcpAlmXfpTxOffPortn_Type()
)
pm1004dcpAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmXfpTxOffPortn.setStatus("current")
_Pm1004dcpAlmLineLocalOosPortn_Type = EkiOnOff
_Pm1004dcpAlmLineLocalOosPortn_Object = MibTableColumn
pm1004dcpAlmLineLocalOosPortn = _Pm1004dcpAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 7),
    _Pm1004dcpAlmLineLocalOosPortn_Type()
)
pm1004dcpAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineLocalOosPortn.setStatus("current")
_Pm1004dcpAlmUpRdiInsPortn_Type = EkiOnOff
_Pm1004dcpAlmUpRdiInsPortn_Object = MibTableColumn
pm1004dcpAlmUpRdiInsPortn = _Pm1004dcpAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 9),
    _Pm1004dcpAlmUpRdiInsPortn_Type()
)
pm1004dcpAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmUpRdiInsPortn.setStatus("current")
_Pm1004dcpAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm1004dcpAlmLineDdmWarningPortn_Object = MibTableColumn
pm1004dcpAlmLineDdmWarningPortn = _Pm1004dcpAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 10),
    _Pm1004dcpAlmLineDdmWarningPortn_Type()
)
pm1004dcpAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineDdmWarningPortn.setStatus("current")
_Pm1004dcpAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm1004dcpAlmLineDdmAlmPortn_Object = MibTableColumn
pm1004dcpAlmLineDdmAlmPortn = _Pm1004dcpAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 11),
    _Pm1004dcpAlmLineDdmAlmPortn_Type()
)
pm1004dcpAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineDdmAlmPortn.setStatus("current")
_Pm1004dcpAlmLineFailPortn_Type = EkiOnOff
_Pm1004dcpAlmLineFailPortn_Object = MibTableColumn
pm1004dcpAlmLineFailPortn = _Pm1004dcpAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 7, 1, 13),
    _Pm1004dcpAlmLineFailPortn_Type()
)
pm1004dcpAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmLineFailPortn.setStatus("current")
_Pm1004dcpAlmdfrmAlmTable_Object = MibTable
pm1004dcpAlmdfrmAlmTable = _Pm1004dcpAlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmdfrmAlmTable.setStatus("current")
_Pm1004dcpAlmdfrmAlmEntry_Object = MibTableRow
pm1004dcpAlmdfrmAlmEntry = _Pm1004dcpAlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 128, 1)
)
pm1004dcpAlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmdfrmAlmEntry.setStatus("current")


class _Pm1004dcpAlmdfrmAlmIndex_Type(Integer32):
    """Custom type pm1004dcpAlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmdfrmAlmIndex_Object = MibTableColumn
pm1004dcpAlmdfrmAlmIndex = _Pm1004dcpAlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 128, 1, 1),
    _Pm1004dcpAlmdfrmAlmIndex_Type()
)
pm1004dcpAlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmdfrmAlmIndex.setStatus("current")
_Pm1004dcpAlmDwAisDetPortn_Type = EkiOnOff
_Pm1004dcpAlmDwAisDetPortn_Object = MibTableColumn
pm1004dcpAlmDwAisDetPortn = _Pm1004dcpAlmDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 128, 1, 2),
    _Pm1004dcpAlmDwAisDetPortn_Type()
)
pm1004dcpAlmDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwAisDetPortn.setStatus("current")
_Pm1004dcpAlmDwRdiDetPortn_Type = EkiOnOff
_Pm1004dcpAlmDwRdiDetPortn_Object = MibTableColumn
pm1004dcpAlmDwRdiDetPortn = _Pm1004dcpAlmDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 128, 1, 3),
    _Pm1004dcpAlmDwRdiDetPortn_Type()
)
pm1004dcpAlmDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwRdiDetPortn.setStatus("current")
_Pm1004dcpAlmDwOofPortn_Type = EkiOnOff
_Pm1004dcpAlmDwOofPortn_Object = MibTableColumn
pm1004dcpAlmDwOofPortn = _Pm1004dcpAlmDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 128, 1, 4),
    _Pm1004dcpAlmDwOofPortn_Type()
)
pm1004dcpAlmDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwOofPortn.setStatus("current")
_Pm1004dcpAlmDwLofPortn_Type = EkiOnOff
_Pm1004dcpAlmDwLofPortn_Object = MibTableColumn
pm1004dcpAlmDwLofPortn = _Pm1004dcpAlmDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 128, 1, 5),
    _Pm1004dcpAlmDwLofPortn_Type()
)
pm1004dcpAlmDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwLofPortn.setStatus("current")
_Pm1004dcpAlmlineSyncAlarmsTable_Object = MibTable
pm1004dcpAlmlineSyncAlarmsTable = _Pm1004dcpAlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineSyncAlarmsTable.setStatus("current")
_Pm1004dcpAlmlineSyncAlarmsEntry_Object = MibTableRow
pm1004dcpAlmlineSyncAlarmsEntry = _Pm1004dcpAlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 133, 1)
)
pm1004dcpAlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineSyncAlarmsEntry.setStatus("current")


class _Pm1004dcpAlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pm1004dcpAlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmlineSyncAlarmsIndex_Object = MibTableColumn
pm1004dcpAlmlineSyncAlarmsIndex = _Pm1004dcpAlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 133, 1, 1),
    _Pm1004dcpAlmlineSyncAlarmsIndex_Type()
)
pm1004dcpAlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmlineSyncAlarmsIndex.setStatus("current")
_Pm1004dcpAlmDwLockerrPortn_Type = EkiOnOff
_Pm1004dcpAlmDwLockerrPortn_Object = MibTableColumn
pm1004dcpAlmDwLockerrPortn = _Pm1004dcpAlmDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 133, 1, 13),
    _Pm1004dcpAlmDwLockerrPortn_Type()
)
pm1004dcpAlmDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwLockerrPortn.setStatus("current")
_Pm1004dcpAlmUpLockerrPortn_Type = EkiOnOff
_Pm1004dcpAlmUpLockerrPortn_Object = MibTableColumn
pm1004dcpAlmUpLockerrPortn = _Pm1004dcpAlmUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 133, 1, 14),
    _Pm1004dcpAlmUpLockerrPortn_Type()
)
pm1004dcpAlmUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmUpLockerrPortn.setStatus("current")
_Pm1004dcpAlmDwLosPortn_Type = EkiOnOff
_Pm1004dcpAlmDwLosPortn_Object = MibTableColumn
pm1004dcpAlmDwLosPortn = _Pm1004dcpAlmDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 133, 1, 17),
    _Pm1004dcpAlmDwLosPortn_Type()
)
pm1004dcpAlmDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmDwLosPortn.setStatus("current")
_Pm1004dcpAlmlineXfp1AlarmsTable_Object = MibTable
pm1004dcpAlmlineXfp1AlarmsTable = _Pm1004dcpAlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1AlarmsTable.setStatus("current")
_Pm1004dcpAlmlineXfp1AlarmsEntry_Object = MibTableRow
pm1004dcpAlmlineXfp1AlarmsEntry = _Pm1004dcpAlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1)
)
pm1004dcpAlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1AlarmsEntry.setStatus("current")


class _Pm1004dcpAlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pm1004dcpAlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmlineXfp1AlarmsIndex_Object = MibTableColumn
pm1004dcpAlmlineXfp1AlarmsIndex = _Pm1004dcpAlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 1),
    _Pm1004dcpAlmlineXfp1AlarmsIndex_Type()
)
pm1004dcpAlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmlineXfp1AlarmsIndex.setStatus("current")
_Pm1004dcpAlmModNrPortn_Type = EkiOnOff
_Pm1004dcpAlmModNrPortn_Object = MibTableColumn
pm1004dcpAlmModNrPortn = _Pm1004dcpAlmModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 3),
    _Pm1004dcpAlmModNrPortn_Type()
)
pm1004dcpAlmModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmModNrPortn.setStatus("current")
_Pm1004dcpAlmRxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004dcpAlmRxCdrNotLockedPortn_Object = MibTableColumn
pm1004dcpAlmRxCdrNotLockedPortn = _Pm1004dcpAlmRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 4),
    _Pm1004dcpAlmRxCdrNotLockedPortn_Type()
)
pm1004dcpAlmRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxCdrNotLockedPortn.setStatus("current")
_Pm1004dcpAlmRxNrPortn_Type = EkiOnOff
_Pm1004dcpAlmRxNrPortn_Object = MibTableColumn
pm1004dcpAlmRxNrPortn = _Pm1004dcpAlmRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 6),
    _Pm1004dcpAlmRxNrPortn_Type()
)
pm1004dcpAlmRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmRxNrPortn.setStatus("current")
_Pm1004dcpAlmTxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004dcpAlmTxCdrNotLockedPortn_Object = MibTableColumn
pm1004dcpAlmTxCdrNotLockedPortn = _Pm1004dcpAlmTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 7),
    _Pm1004dcpAlmTxCdrNotLockedPortn_Type()
)
pm1004dcpAlmTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxCdrNotLockedPortn.setStatus("current")
_Pm1004dcpAlmTxFaultPortn_Type = EkiOnOff
_Pm1004dcpAlmTxFaultPortn_Object = MibTableColumn
pm1004dcpAlmTxFaultPortn = _Pm1004dcpAlmTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 8),
    _Pm1004dcpAlmTxFaultPortn_Type()
)
pm1004dcpAlmTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxFaultPortn.setStatus("current")
_Pm1004dcpAlmTxNrPortn_Type = EkiOnOff
_Pm1004dcpAlmTxNrPortn_Object = MibTableColumn
pm1004dcpAlmTxNrPortn = _Pm1004dcpAlmTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 9),
    _Pm1004dcpAlmTxNrPortn_Type()
)
pm1004dcpAlmTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTxNrPortn.setStatus("current")
_Pm1004dcpAlmWavelengthUnlockedPortn_Type = EkiOnOff
_Pm1004dcpAlmWavelengthUnlockedPortn_Object = MibTableColumn
pm1004dcpAlmWavelengthUnlockedPortn = _Pm1004dcpAlmWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 15),
    _Pm1004dcpAlmWavelengthUnlockedPortn_Type()
)
pm1004dcpAlmWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmWavelengthUnlockedPortn.setStatus("current")
_Pm1004dcpAlmTecFaultPortn_Type = EkiOnOff
_Pm1004dcpAlmTecFaultPortn_Object = MibTableColumn
pm1004dcpAlmTecFaultPortn = _Pm1004dcpAlmTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 16),
    _Pm1004dcpAlmTecFaultPortn_Type()
)
pm1004dcpAlmTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmTecFaultPortn.setStatus("current")
_Pm1004dcpAlmApdSupplyFaultPortn_Type = EkiOnOff
_Pm1004dcpAlmApdSupplyFaultPortn_Object = MibTableColumn
pm1004dcpAlmApdSupplyFaultPortn = _Pm1004dcpAlmApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 2, 3, 3, 211, 1, 17),
    _Pm1004dcpAlmApdSupplyFaultPortn_Type()
)
pm1004dcpAlmApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmApdSupplyFaultPortn.setStatus("current")
_Pm1004dcpmeasures_ObjectIdentity = ObjectIdentity
pm1004dcpmeasures = _Pm1004dcpmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3)
)
_Pm1004dcpMesrOther_ObjectIdentity = ObjectIdentity
pm1004dcpMesrOther = _Pm1004dcpMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 1)
)
_Pm1004dcpMesrsynth0_Type = EkiMeasureType
_Pm1004dcpMesrsynth0_Object = MibScalar
pm1004dcpMesrsynth0 = _Pm1004dcpMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 1, 0),
    _Pm1004dcpMesrsynth0_Type()
)
pm1004dcpMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrsynth0.setStatus("deprecated")
_Pm1004dcpMesrsynth1_Type = EkiMeasureType
_Pm1004dcpMesrsynth1_Object = MibScalar
pm1004dcpMesrsynth1 = _Pm1004dcpMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 1, 1),
    _Pm1004dcpMesrsynth1_Type()
)
pm1004dcpMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrsynth1.setStatus("deprecated")
_Pm1004dcpMesrClient_ObjectIdentity = ObjectIdentity
pm1004dcpMesrClient = _Pm1004dcpMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2)
)
_Pm1004dcpMesrtempMeasTable_Object = MibTable
pm1004dcpMesrtempMeasTable = _Pm1004dcpMesrtempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrtempMeasTable.setStatus("current")
_Pm1004dcpMesrtempMeasEntry_Object = MibTableRow
pm1004dcpMesrtempMeasEntry = _Pm1004dcpMesrtempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 16, 1)
)
pm1004dcpMesrtempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrtempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrtempMeasEntry.setStatus("current")


class _Pm1004dcpMesrtempMeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrtempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrtempMeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrtempMeasIndex_Object = MibTableColumn
pm1004dcpMesrtempMeasIndex = _Pm1004dcpMesrtempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 16, 1, 1),
    _Pm1004dcpMesrtempMeasIndex_Type()
)
pm1004dcpMesrtempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrtempMeasIndex.setStatus("current")


class _Pm1004dcpMesrtempMeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrtempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrtempMeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrtempMeasPortn_Object = MibTableColumn
pm1004dcpMesrtempMeasPortn = _Pm1004dcpMesrtempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 16, 1, 2),
    _Pm1004dcpMesrtempMeasPortn_Type()
)
pm1004dcpMesrtempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrtempMeasPortn.setStatus("current")
_Pm1004dcpMesrvoltMeasTable_Object = MibTable
pm1004dcpMesrvoltMeasTable = _Pm1004dcpMesrvoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrvoltMeasTable.setStatus("current")
_Pm1004dcpMesrvoltMeasEntry_Object = MibTableRow
pm1004dcpMesrvoltMeasEntry = _Pm1004dcpMesrvoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 24, 1)
)
pm1004dcpMesrvoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrvoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrvoltMeasEntry.setStatus("current")


class _Pm1004dcpMesrvoltMeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrvoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrvoltMeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrvoltMeasIndex_Object = MibTableColumn
pm1004dcpMesrvoltMeasIndex = _Pm1004dcpMesrvoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 24, 1, 1),
    _Pm1004dcpMesrvoltMeasIndex_Type()
)
pm1004dcpMesrvoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrvoltMeasIndex.setStatus("current")


class _Pm1004dcpMesrvoltMeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrvoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrvoltMeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrvoltMeasPortn_Object = MibTableColumn
pm1004dcpMesrvoltMeasPortn = _Pm1004dcpMesrvoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 24, 1, 2),
    _Pm1004dcpMesrvoltMeasPortn_Type()
)
pm1004dcpMesrvoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrvoltMeasPortn.setStatus("current")
_Pm1004dcpMesrbiasMeasTable_Object = MibTable
pm1004dcpMesrbiasMeasTable = _Pm1004dcpMesrbiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrbiasMeasTable.setStatus("current")
_Pm1004dcpMesrbiasMeasEntry_Object = MibTableRow
pm1004dcpMesrbiasMeasEntry = _Pm1004dcpMesrbiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 32, 1)
)
pm1004dcpMesrbiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrbiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrbiasMeasEntry.setStatus("current")


class _Pm1004dcpMesrbiasMeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrbiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrbiasMeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrbiasMeasIndex_Object = MibTableColumn
pm1004dcpMesrbiasMeasIndex = _Pm1004dcpMesrbiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 32, 1, 1),
    _Pm1004dcpMesrbiasMeasIndex_Type()
)
pm1004dcpMesrbiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrbiasMeasIndex.setStatus("current")


class _Pm1004dcpMesrbiasMeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrbiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrbiasMeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrbiasMeasPortn_Object = MibTableColumn
pm1004dcpMesrbiasMeasPortn = _Pm1004dcpMesrbiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 32, 1, 2),
    _Pm1004dcpMesrbiasMeasPortn_Type()
)
pm1004dcpMesrbiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrbiasMeasPortn.setStatus("current")
_Pm1004dcpMesrtxpwrMeasTable_Object = MibTable
pm1004dcpMesrtxpwrMeasTable = _Pm1004dcpMesrtxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrtxpwrMeasTable.setStatus("current")
_Pm1004dcpMesrtxpwrMeasEntry_Object = MibTableRow
pm1004dcpMesrtxpwrMeasEntry = _Pm1004dcpMesrtxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 40, 1)
)
pm1004dcpMesrtxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrtxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrtxpwrMeasEntry.setStatus("current")


class _Pm1004dcpMesrtxpwrMeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrtxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrtxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrtxpwrMeasIndex_Object = MibTableColumn
pm1004dcpMesrtxpwrMeasIndex = _Pm1004dcpMesrtxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 40, 1, 1),
    _Pm1004dcpMesrtxpwrMeasIndex_Type()
)
pm1004dcpMesrtxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrtxpwrMeasIndex.setStatus("current")


class _Pm1004dcpMesrtxpwrMeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrtxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrtxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrtxpwrMeasPortn_Object = MibTableColumn
pm1004dcpMesrtxpwrMeasPortn = _Pm1004dcpMesrtxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 40, 1, 2),
    _Pm1004dcpMesrtxpwrMeasPortn_Type()
)
pm1004dcpMesrtxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrtxpwrMeasPortn.setStatus("current")
_Pm1004dcpMesrrxpwrMeasTable_Object = MibTable
pm1004dcpMesrrxpwrMeasTable = _Pm1004dcpMesrrxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrrxpwrMeasTable.setStatus("current")
_Pm1004dcpMesrrxpwrMeasEntry_Object = MibTableRow
pm1004dcpMesrrxpwrMeasEntry = _Pm1004dcpMesrrxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 48, 1)
)
pm1004dcpMesrrxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrrxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrrxpwrMeasEntry.setStatus("current")


class _Pm1004dcpMesrrxpwrMeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrrxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrrxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrrxpwrMeasIndex_Object = MibTableColumn
pm1004dcpMesrrxpwrMeasIndex = _Pm1004dcpMesrrxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 48, 1, 1),
    _Pm1004dcpMesrrxpwrMeasIndex_Type()
)
pm1004dcpMesrrxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrrxpwrMeasIndex.setStatus("current")


class _Pm1004dcpMesrrxpwrMeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrrxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrrxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrrxpwrMeasPortn_Object = MibTableColumn
pm1004dcpMesrrxpwrMeasPortn = _Pm1004dcpMesrrxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 2, 48, 1, 2),
    _Pm1004dcpMesrrxpwrMeasPortn_Type()
)
pm1004dcpMesrrxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrrxpwrMeasPortn.setStatus("current")
_Pm1004dcpMesrLine_ObjectIdentity = ObjectIdentity
pm1004dcpMesrLine = _Pm1004dcpMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3)
)
_Pm1004dcpMesrxfp1LxModTempMeasTable_Object = MibTable
pm1004dcpMesrxfp1LxModTempMeasTable = _Pm1004dcpMesrxfp1LxModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxModTempMeasTable.setStatus("current")
_Pm1004dcpMesrxfp1LxModTempMeasEntry_Object = MibTableRow
pm1004dcpMesrxfp1LxModTempMeasEntry = _Pm1004dcpMesrxfp1LxModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 208, 1)
)
pm1004dcpMesrxfp1LxModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrxfp1LxModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxModTempMeasEntry.setStatus("current")


class _Pm1004dcpMesrxfp1LxModTempMeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LxModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrxfp1LxModTempMeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LxModTempMeasIndex_Object = MibTableColumn
pm1004dcpMesrxfp1LxModTempMeasIndex = _Pm1004dcpMesrxfp1LxModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 208, 1, 1),
    _Pm1004dcpMesrxfp1LxModTempMeasIndex_Type()
)
pm1004dcpMesrxfp1LxModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxModTempMeasIndex.setStatus("current")


class _Pm1004dcpMesrxfp1LxModTempMeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LxModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrxfp1LxModTempMeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LxModTempMeasPortn_Object = MibTableColumn
pm1004dcpMesrxfp1LxModTempMeasPortn = _Pm1004dcpMesrxfp1LxModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 208, 1, 2),
    _Pm1004dcpMesrxfp1LxModTempMeasPortn_Type()
)
pm1004dcpMesrxfp1LxModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxModTempMeasPortn.setStatus("current")
_Pm1004dcpMesrxfp1ReservedTable_Object = MibTable
pm1004dcpMesrxfp1ReservedTable = _Pm1004dcpMesrxfp1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1ReservedTable.setStatus("deprecated")
_Pm1004dcpMesrxfp1ReservedEntry_Object = MibTableRow
pm1004dcpMesrxfp1ReservedEntry = _Pm1004dcpMesrxfp1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 209, 1)
)
pm1004dcpMesrxfp1ReservedEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrxfp1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1ReservedEntry.setStatus("deprecated")


class _Pm1004dcpMesrxfp1ReservedIndex_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrxfp1ReservedIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1ReservedIndex_Object = MibTableColumn
pm1004dcpMesrxfp1ReservedIndex = _Pm1004dcpMesrxfp1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 209, 1, 1),
    _Pm1004dcpMesrxfp1ReservedIndex_Type()
)
pm1004dcpMesrxfp1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1ReservedIndex.setStatus("deprecated")


class _Pm1004dcpMesrxfp1ReservedPortn_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrxfp1ReservedPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1ReservedPortn_Object = MibTableColumn
pm1004dcpMesrxfp1ReservedPortn = _Pm1004dcpMesrxfp1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 209, 1, 2),
    _Pm1004dcpMesrxfp1ReservedPortn_Type()
)
pm1004dcpMesrxfp1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1ReservedPortn.setStatus("deprecated")
_Pm1004dcpMesrxfp1LoBiasCurrentMeasTable_Object = MibTable
pm1004dcpMesrxfp1LoBiasCurrentMeasTable = _Pm1004dcpMesrxfp1LoBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LoBiasCurrentMeasTable.setStatus("current")
_Pm1004dcpMesrxfp1LoBiasCurrentMeasEntry_Object = MibTableRow
pm1004dcpMesrxfp1LoBiasCurrentMeasEntry = _Pm1004dcpMesrxfp1LoBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 210, 1)
)
pm1004dcpMesrxfp1LoBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrxfp1LoBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LoBiasCurrentMeasEntry.setStatus("current")


class _Pm1004dcpMesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LoBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrxfp1LoBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LoBiasCurrentMeasIndex_Object = MibTableColumn
pm1004dcpMesrxfp1LoBiasCurrentMeasIndex = _Pm1004dcpMesrxfp1LoBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 210, 1, 1),
    _Pm1004dcpMesrxfp1LoBiasCurrentMeasIndex_Type()
)
pm1004dcpMesrxfp1LoBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LoBiasCurrentMeasIndex.setStatus("current")


class _Pm1004dcpMesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LoBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrxfp1LoBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LoBiasCurrentMeasPortn_Object = MibTableColumn
pm1004dcpMesrxfp1LoBiasCurrentMeasPortn = _Pm1004dcpMesrxfp1LoBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 210, 1, 2),
    _Pm1004dcpMesrxfp1LoBiasCurrentMeasPortn_Type()
)
pm1004dcpMesrxfp1LoBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LoBiasCurrentMeasPortn.setStatus("current")
_Pm1004dcpMesrxfp1LoTxPowerMeasTable_Object = MibTable
pm1004dcpMesrxfp1LoTxPowerMeasTable = _Pm1004dcpMesrxfp1LoTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LoTxPowerMeasTable.setStatus("current")
_Pm1004dcpMesrxfp1LoTxPowerMeasEntry_Object = MibTableRow
pm1004dcpMesrxfp1LoTxPowerMeasEntry = _Pm1004dcpMesrxfp1LoTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 211, 1)
)
pm1004dcpMesrxfp1LoTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrxfp1LoTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LoTxPowerMeasEntry.setStatus("current")


class _Pm1004dcpMesrxfp1LoTxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LoTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrxfp1LoTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LoTxPowerMeasIndex_Object = MibTableColumn
pm1004dcpMesrxfp1LoTxPowerMeasIndex = _Pm1004dcpMesrxfp1LoTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 211, 1, 1),
    _Pm1004dcpMesrxfp1LoTxPowerMeasIndex_Type()
)
pm1004dcpMesrxfp1LoTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LoTxPowerMeasIndex.setStatus("current")


class _Pm1004dcpMesrxfp1LoTxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LoTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrxfp1LoTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LoTxPowerMeasPortn_Object = MibTableColumn
pm1004dcpMesrxfp1LoTxPowerMeasPortn = _Pm1004dcpMesrxfp1LoTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 211, 1, 2),
    _Pm1004dcpMesrxfp1LoTxPowerMeasPortn_Type()
)
pm1004dcpMesrxfp1LoTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LoTxPowerMeasPortn.setStatus("current")
_Pm1004dcpMesrxfp1LiRxPowerMeasTable_Object = MibTable
pm1004dcpMesrxfp1LiRxPowerMeasTable = _Pm1004dcpMesrxfp1LiRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LiRxPowerMeasTable.setStatus("current")
_Pm1004dcpMesrxfp1LiRxPowerMeasEntry_Object = MibTableRow
pm1004dcpMesrxfp1LiRxPowerMeasEntry = _Pm1004dcpMesrxfp1LiRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 212, 1)
)
pm1004dcpMesrxfp1LiRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrxfp1LiRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LiRxPowerMeasEntry.setStatus("current")


class _Pm1004dcpMesrxfp1LiRxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LiRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrxfp1LiRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LiRxPowerMeasIndex_Object = MibTableColumn
pm1004dcpMesrxfp1LiRxPowerMeasIndex = _Pm1004dcpMesrxfp1LiRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 212, 1, 1),
    _Pm1004dcpMesrxfp1LiRxPowerMeasIndex_Type()
)
pm1004dcpMesrxfp1LiRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LiRxPowerMeasIndex.setStatus("current")


class _Pm1004dcpMesrxfp1LiRxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LiRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrxfp1LiRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LiRxPowerMeasPortn_Object = MibTableColumn
pm1004dcpMesrxfp1LiRxPowerMeasPortn = _Pm1004dcpMesrxfp1LiRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 212, 1, 2),
    _Pm1004dcpMesrxfp1LiRxPowerMeasPortn_Type()
)
pm1004dcpMesrxfp1LiRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LiRxPowerMeasPortn.setStatus("current")
_Pm1004dcpMesrxfp1LxAux1MeasTable_Object = MibTable
pm1004dcpMesrxfp1LxAux1MeasTable = _Pm1004dcpMesrxfp1LxAux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxAux1MeasTable.setStatus("deprecated")
_Pm1004dcpMesrxfp1LxAux1MeasEntry_Object = MibTableRow
pm1004dcpMesrxfp1LxAux1MeasEntry = _Pm1004dcpMesrxfp1LxAux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 213, 1)
)
pm1004dcpMesrxfp1LxAux1MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrxfp1LxAux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxAux1MeasEntry.setStatus("deprecated")


class _Pm1004dcpMesrxfp1LxAux1MeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LxAux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrxfp1LxAux1MeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LxAux1MeasIndex_Object = MibTableColumn
pm1004dcpMesrxfp1LxAux1MeasIndex = _Pm1004dcpMesrxfp1LxAux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 213, 1, 1),
    _Pm1004dcpMesrxfp1LxAux1MeasIndex_Type()
)
pm1004dcpMesrxfp1LxAux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxAux1MeasIndex.setStatus("deprecated")


class _Pm1004dcpMesrxfp1LxAux1MeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LxAux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrxfp1LxAux1MeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LxAux1MeasPortn_Object = MibTableColumn
pm1004dcpMesrxfp1LxAux1MeasPortn = _Pm1004dcpMesrxfp1LxAux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 213, 1, 2),
    _Pm1004dcpMesrxfp1LxAux1MeasPortn_Type()
)
pm1004dcpMesrxfp1LxAux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxAux1MeasPortn.setStatus("deprecated")
_Pm1004dcpMesrxfp1LxAux2MeasTable_Object = MibTable
pm1004dcpMesrxfp1LxAux2MeasTable = _Pm1004dcpMesrxfp1LxAux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxAux2MeasTable.setStatus("deprecated")
_Pm1004dcpMesrxfp1LxAux2MeasEntry_Object = MibTableRow
pm1004dcpMesrxfp1LxAux2MeasEntry = _Pm1004dcpMesrxfp1LxAux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 214, 1)
)
pm1004dcpMesrxfp1LxAux2MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrxfp1LxAux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxAux2MeasEntry.setStatus("deprecated")


class _Pm1004dcpMesrxfp1LxAux2MeasIndex_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LxAux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrxfp1LxAux2MeasIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LxAux2MeasIndex_Object = MibTableColumn
pm1004dcpMesrxfp1LxAux2MeasIndex = _Pm1004dcpMesrxfp1LxAux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 214, 1, 1),
    _Pm1004dcpMesrxfp1LxAux2MeasIndex_Type()
)
pm1004dcpMesrxfp1LxAux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxAux2MeasIndex.setStatus("deprecated")


class _Pm1004dcpMesrxfp1LxAux2MeasPortn_Type(Integer32):
    """Custom type pm1004dcpMesrxfp1LxAux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrxfp1LxAux2MeasPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrxfp1LxAux2MeasPortn_Object = MibTableColumn
pm1004dcpMesrxfp1LxAux2MeasPortn = _Pm1004dcpMesrxfp1LxAux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 214, 1, 2),
    _Pm1004dcpMesrxfp1LxAux2MeasPortn_Type()
)
pm1004dcpMesrxfp1LxAux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrxfp1LxAux2MeasPortn.setStatus("deprecated")
_Pm1004dcpMesrotx1AgingTable_Object = MibTable
pm1004dcpMesrotx1AgingTable = _Pm1004dcpMesrotx1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1AgingTable.setStatus("current")
_Pm1004dcpMesrotx1AgingEntry_Object = MibTableRow
pm1004dcpMesrotx1AgingEntry = _Pm1004dcpMesrotx1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 224, 1)
)
pm1004dcpMesrotx1AgingEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrotx1AgingIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1AgingEntry.setStatus("current")


class _Pm1004dcpMesrotx1AgingIndex_Type(Integer32):
    """Custom type pm1004dcpMesrotx1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrotx1AgingIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrotx1AgingIndex_Object = MibTableColumn
pm1004dcpMesrotx1AgingIndex = _Pm1004dcpMesrotx1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 224, 1, 1),
    _Pm1004dcpMesrotx1AgingIndex_Type()
)
pm1004dcpMesrotx1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1AgingIndex.setStatus("current")


class _Pm1004dcpMesrotx1AgingPortn_Type(Integer32):
    """Custom type pm1004dcpMesrotx1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrotx1AgingPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrotx1AgingPortn_Object = MibTableColumn
pm1004dcpMesrotx1AgingPortn = _Pm1004dcpMesrotx1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 224, 1, 2),
    _Pm1004dcpMesrotx1AgingPortn_Type()
)
pm1004dcpMesrotx1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1AgingPortn.setStatus("current")
_Pm1004dcpMesrotx1LaserTemperatureTable_Object = MibTable
pm1004dcpMesrotx1LaserTemperatureTable = _Pm1004dcpMesrotx1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1LaserTemperatureTable.setStatus("deprecated")
_Pm1004dcpMesrotx1LaserTemperatureEntry_Object = MibTableRow
pm1004dcpMesrotx1LaserTemperatureEntry = _Pm1004dcpMesrotx1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 225, 1)
)
pm1004dcpMesrotx1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrotx1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1LaserTemperatureEntry.setStatus("deprecated")


class _Pm1004dcpMesrotx1LaserTemperatureIndex_Type(Integer32):
    """Custom type pm1004dcpMesrotx1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrotx1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrotx1LaserTemperatureIndex_Object = MibTableColumn
pm1004dcpMesrotx1LaserTemperatureIndex = _Pm1004dcpMesrotx1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 225, 1, 1),
    _Pm1004dcpMesrotx1LaserTemperatureIndex_Type()
)
pm1004dcpMesrotx1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1LaserTemperatureIndex.setStatus("deprecated")


class _Pm1004dcpMesrotx1LaserTemperaturePortn_Type(Integer32):
    """Custom type pm1004dcpMesrotx1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrotx1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrotx1LaserTemperaturePortn_Object = MibTableColumn
pm1004dcpMesrotx1LaserTemperaturePortn = _Pm1004dcpMesrotx1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 225, 1, 2),
    _Pm1004dcpMesrotx1LaserTemperaturePortn_Type()
)
pm1004dcpMesrotx1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1LaserTemperaturePortn.setStatus("deprecated")
_Pm1004dcpMesrotx1FreqDeviationTable_Object = MibTable
pm1004dcpMesrotx1FreqDeviationTable = _Pm1004dcpMesrotx1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1FreqDeviationTable.setStatus("current")
_Pm1004dcpMesrotx1FreqDeviationEntry_Object = MibTableRow
pm1004dcpMesrotx1FreqDeviationEntry = _Pm1004dcpMesrotx1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 226, 1)
)
pm1004dcpMesrotx1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrotx1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1FreqDeviationEntry.setStatus("current")


class _Pm1004dcpMesrotx1FreqDeviationIndex_Type(Integer32):
    """Custom type pm1004dcpMesrotx1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrotx1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrotx1FreqDeviationIndex_Object = MibTableColumn
pm1004dcpMesrotx1FreqDeviationIndex = _Pm1004dcpMesrotx1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 226, 1, 1),
    _Pm1004dcpMesrotx1FreqDeviationIndex_Type()
)
pm1004dcpMesrotx1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1FreqDeviationIndex.setStatus("current")


class _Pm1004dcpMesrotx1FreqDeviationPortn_Type(Integer32):
    """Custom type pm1004dcpMesrotx1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrotx1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrotx1FreqDeviationPortn_Object = MibTableColumn
pm1004dcpMesrotx1FreqDeviationPortn = _Pm1004dcpMesrotx1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 226, 1, 2),
    _Pm1004dcpMesrotx1FreqDeviationPortn_Type()
)
pm1004dcpMesrotx1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1FreqDeviationPortn.setStatus("current")
_Pm1004dcpMesrotx1LaserWvlengthTable_Object = MibTable
pm1004dcpMesrotx1LaserWvlengthTable = _Pm1004dcpMesrotx1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1LaserWvlengthTable.setStatus("current")
_Pm1004dcpMesrotx1LaserWvlengthEntry_Object = MibTableRow
pm1004dcpMesrotx1LaserWvlengthEntry = _Pm1004dcpMesrotx1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 227, 1)
)
pm1004dcpMesrotx1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpMesrotx1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1LaserWvlengthEntry.setStatus("current")


class _Pm1004dcpMesrotx1LaserWvlengthIndex_Type(Integer32):
    """Custom type pm1004dcpMesrotx1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpMesrotx1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pm1004dcpMesrotx1LaserWvlengthIndex_Object = MibTableColumn
pm1004dcpMesrotx1LaserWvlengthIndex = _Pm1004dcpMesrotx1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 227, 1, 1),
    _Pm1004dcpMesrotx1LaserWvlengthIndex_Type()
)
pm1004dcpMesrotx1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1LaserWvlengthIndex.setStatus("current")


class _Pm1004dcpMesrotx1LaserWvlengthPortn_Type(Integer32):
    """Custom type pm1004dcpMesrotx1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004dcpMesrotx1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pm1004dcpMesrotx1LaserWvlengthPortn_Object = MibTableColumn
pm1004dcpMesrotx1LaserWvlengthPortn = _Pm1004dcpMesrotx1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 3, 3, 227, 1, 2),
    _Pm1004dcpMesrotx1LaserWvlengthPortn_Type()
)
pm1004dcpMesrotx1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpMesrotx1LaserWvlengthPortn.setStatus("current")
_Pm1004dcpcounters_ObjectIdentity = ObjectIdentity
pm1004dcpcounters = _Pm1004dcpcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4)
)
_Pm1004dcpCntOther_ObjectIdentity = ObjectIdentity
pm1004dcpCntOther = _Pm1004dcpCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 1)
)
_Pm1004dcpCntClient_ObjectIdentity = ObjectIdentity
pm1004dcpCntClient = _Pm1004dcpCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2)
)
_Pm1004dcpCntupRaRemCntTable_Object = MibTable
pm1004dcpCntupRaRemCntTable = _Pm1004dcpCntupRaRemCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004dcpCntupRaRemCntTable.setStatus("current")
_Pm1004dcpCntupRaRemCntEntry_Object = MibTableRow
pm1004dcpCntupRaRemCntEntry = _Pm1004dcpCntupRaRemCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 16, 1)
)
pm1004dcpCntupRaRemCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntupRaRemCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntupRaRemCntEntry.setStatus("current")


class _Pm1004dcpCntupRaRemCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntupRaRemCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntupRaRemCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntupRaRemCntIndex_Object = MibTableColumn
pm1004dcpCntupRaRemCntIndex = _Pm1004dcpCntupRaRemCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 16, 1, 1),
    _Pm1004dcpCntupRaRemCntIndex_Type()
)
pm1004dcpCntupRaRemCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRaRemCntIndex.setStatus("current")
_Pm1004dcpCntupRaRemCntValuePortn_Type = Counter32
_Pm1004dcpCntupRaRemCntValuePortn_Object = MibTableColumn
pm1004dcpCntupRaRemCntValuePortn = _Pm1004dcpCntupRaRemCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 16, 1, 2),
    _Pm1004dcpCntupRaRemCntValuePortn_Type()
)
pm1004dcpCntupRaRemCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRaRemCntValuePortn.setStatus("current")
_Pm1004dcpCntupRaRemCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntupRaRemCntErrorPortn_Object = MibTableColumn
pm1004dcpCntupRaRemCntErrorPortn = _Pm1004dcpCntupRaRemCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 16, 1, 3),
    _Pm1004dcpCntupRaRemCntErrorPortn_Type()
)
pm1004dcpCntupRaRemCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRaRemCntErrorPortn.setStatus("current")
_Pm1004dcpCntupRaRemCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntupRaRemCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntupRaRemCntOverloadPortn = _Pm1004dcpCntupRaRemCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 16, 1, 4),
    _Pm1004dcpCntupRaRemCntOverloadPortn_Type()
)
pm1004dcpCntupRaRemCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRaRemCntOverloadPortn.setStatus("current")
_Pm1004dcpCntupRaInsCntTable_Object = MibTable
pm1004dcpCntupRaInsCntTable = _Pm1004dcpCntupRaInsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 24)
)
if mibBuilder.loadTexts:
    pm1004dcpCntupRaInsCntTable.setStatus("current")
_Pm1004dcpCntupRaInsCntEntry_Object = MibTableRow
pm1004dcpCntupRaInsCntEntry = _Pm1004dcpCntupRaInsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 24, 1)
)
pm1004dcpCntupRaInsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntupRaInsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntupRaInsCntEntry.setStatus("current")


class _Pm1004dcpCntupRaInsCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntupRaInsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntupRaInsCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntupRaInsCntIndex_Object = MibTableColumn
pm1004dcpCntupRaInsCntIndex = _Pm1004dcpCntupRaInsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 24, 1, 1),
    _Pm1004dcpCntupRaInsCntIndex_Type()
)
pm1004dcpCntupRaInsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRaInsCntIndex.setStatus("current")
_Pm1004dcpCntupRaInsCntValuePortn_Type = Counter32
_Pm1004dcpCntupRaInsCntValuePortn_Object = MibTableColumn
pm1004dcpCntupRaInsCntValuePortn = _Pm1004dcpCntupRaInsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 24, 1, 2),
    _Pm1004dcpCntupRaInsCntValuePortn_Type()
)
pm1004dcpCntupRaInsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRaInsCntValuePortn.setStatus("current")
_Pm1004dcpCntupRaInsCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntupRaInsCntErrorPortn_Object = MibTableColumn
pm1004dcpCntupRaInsCntErrorPortn = _Pm1004dcpCntupRaInsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 24, 1, 3),
    _Pm1004dcpCntupRaInsCntErrorPortn_Type()
)
pm1004dcpCntupRaInsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRaInsCntErrorPortn.setStatus("current")
_Pm1004dcpCntupRaInsCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntupRaInsCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntupRaInsCntOverloadPortn = _Pm1004dcpCntupRaInsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 24, 1, 4),
    _Pm1004dcpCntupRaInsCntOverloadPortn_Type()
)
pm1004dcpCntupRaInsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRaInsCntOverloadPortn.setStatus("current")
_Pm1004dcpCntupRdErrCntTable_Object = MibTable
pm1004dcpCntupRdErrCntTable = _Pm1004dcpCntupRdErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004dcpCntupRdErrCntTable.setStatus("current")
_Pm1004dcpCntupRdErrCntEntry_Object = MibTableRow
pm1004dcpCntupRdErrCntEntry = _Pm1004dcpCntupRdErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 32, 1)
)
pm1004dcpCntupRdErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntupRdErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntupRdErrCntEntry.setStatus("current")


class _Pm1004dcpCntupRdErrCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntupRdErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntupRdErrCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntupRdErrCntIndex_Object = MibTableColumn
pm1004dcpCntupRdErrCntIndex = _Pm1004dcpCntupRdErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 32, 1, 1),
    _Pm1004dcpCntupRdErrCntIndex_Type()
)
pm1004dcpCntupRdErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRdErrCntIndex.setStatus("current")
_Pm1004dcpCntupRdErrCntValuePortn_Type = Counter32
_Pm1004dcpCntupRdErrCntValuePortn_Object = MibTableColumn
pm1004dcpCntupRdErrCntValuePortn = _Pm1004dcpCntupRdErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 32, 1, 2),
    _Pm1004dcpCntupRdErrCntValuePortn_Type()
)
pm1004dcpCntupRdErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRdErrCntValuePortn.setStatus("current")
_Pm1004dcpCntupRdErrCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntupRdErrCntErrorPortn_Object = MibTableColumn
pm1004dcpCntupRdErrCntErrorPortn = _Pm1004dcpCntupRdErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 32, 1, 3),
    _Pm1004dcpCntupRdErrCntErrorPortn_Type()
)
pm1004dcpCntupRdErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRdErrCntErrorPortn.setStatus("current")
_Pm1004dcpCntupRdErrCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntupRdErrCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntupRdErrCntOverloadPortn = _Pm1004dcpCntupRdErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 32, 1, 4),
    _Pm1004dcpCntupRdErrCntOverloadPortn_Type()
)
pm1004dcpCntupRdErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupRdErrCntOverloadPortn.setStatus("current")
_Pm1004dcpCntupTimCntTable_Object = MibTable
pm1004dcpCntupTimCntTable = _Pm1004dcpCntupTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 40)
)
if mibBuilder.loadTexts:
    pm1004dcpCntupTimCntTable.setStatus("current")
_Pm1004dcpCntupTimCntEntry_Object = MibTableRow
pm1004dcpCntupTimCntEntry = _Pm1004dcpCntupTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 40, 1)
)
pm1004dcpCntupTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntupTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntupTimCntEntry.setStatus("current")


class _Pm1004dcpCntupTimCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntupTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntupTimCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntupTimCntIndex_Object = MibTableColumn
pm1004dcpCntupTimCntIndex = _Pm1004dcpCntupTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 40, 1, 1),
    _Pm1004dcpCntupTimCntIndex_Type()
)
pm1004dcpCntupTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupTimCntIndex.setStatus("current")
_Pm1004dcpCntupTimCntValuePortn_Type = Counter32
_Pm1004dcpCntupTimCntValuePortn_Object = MibTableColumn
pm1004dcpCntupTimCntValuePortn = _Pm1004dcpCntupTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 40, 1, 2),
    _Pm1004dcpCntupTimCntValuePortn_Type()
)
pm1004dcpCntupTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupTimCntValuePortn.setStatus("current")
_Pm1004dcpCntupTimCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntupTimCntErrorPortn_Object = MibTableColumn
pm1004dcpCntupTimCntErrorPortn = _Pm1004dcpCntupTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 40, 1, 3),
    _Pm1004dcpCntupTimCntErrorPortn_Type()
)
pm1004dcpCntupTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupTimCntErrorPortn.setStatus("current")
_Pm1004dcpCntupTimCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntupTimCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntupTimCntOverloadPortn = _Pm1004dcpCntupTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 40, 1, 4),
    _Pm1004dcpCntupTimCntOverloadPortn_Type()
)
pm1004dcpCntupTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupTimCntOverloadPortn.setStatus("current")
_Pm1004dcpCntupCvErrCntTable_Object = MibTable
pm1004dcpCntupCvErrCntTable = _Pm1004dcpCntupCvErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 48)
)
if mibBuilder.loadTexts:
    pm1004dcpCntupCvErrCntTable.setStatus("current")
_Pm1004dcpCntupCvErrCntEntry_Object = MibTableRow
pm1004dcpCntupCvErrCntEntry = _Pm1004dcpCntupCvErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 48, 1)
)
pm1004dcpCntupCvErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntupCvErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntupCvErrCntEntry.setStatus("current")


class _Pm1004dcpCntupCvErrCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntupCvErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntupCvErrCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntupCvErrCntIndex_Object = MibTableColumn
pm1004dcpCntupCvErrCntIndex = _Pm1004dcpCntupCvErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 48, 1, 1),
    _Pm1004dcpCntupCvErrCntIndex_Type()
)
pm1004dcpCntupCvErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupCvErrCntIndex.setStatus("current")
_Pm1004dcpCntupCvErrCntValuePortn_Type = Counter32
_Pm1004dcpCntupCvErrCntValuePortn_Object = MibTableColumn
pm1004dcpCntupCvErrCntValuePortn = _Pm1004dcpCntupCvErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 48, 1, 2),
    _Pm1004dcpCntupCvErrCntValuePortn_Type()
)
pm1004dcpCntupCvErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupCvErrCntValuePortn.setStatus("current")
_Pm1004dcpCntupCvErrCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntupCvErrCntErrorPortn_Object = MibTableColumn
pm1004dcpCntupCvErrCntErrorPortn = _Pm1004dcpCntupCvErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 48, 1, 3),
    _Pm1004dcpCntupCvErrCntErrorPortn_Type()
)
pm1004dcpCntupCvErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupCvErrCntErrorPortn.setStatus("current")
_Pm1004dcpCntupCvErrCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntupCvErrCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntupCvErrCntOverloadPortn = _Pm1004dcpCntupCvErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 48, 1, 4),
    _Pm1004dcpCntupCvErrCntOverloadPortn_Type()
)
pm1004dcpCntupCvErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntupCvErrCntOverloadPortn.setStatus("current")
_Pm1004dcpCntdwCbipCntTable_Object = MibTable
pm1004dcpCntdwCbipCntTable = _Pm1004dcpCntdwCbipCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 64)
)
if mibBuilder.loadTexts:
    pm1004dcpCntdwCbipCntTable.setStatus("current")
_Pm1004dcpCntdwCbipCntEntry_Object = MibTableRow
pm1004dcpCntdwCbipCntEntry = _Pm1004dcpCntdwCbipCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 64, 1)
)
pm1004dcpCntdwCbipCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntdwCbipCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntdwCbipCntEntry.setStatus("current")


class _Pm1004dcpCntdwCbipCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntdwCbipCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntdwCbipCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntdwCbipCntIndex_Object = MibTableColumn
pm1004dcpCntdwCbipCntIndex = _Pm1004dcpCntdwCbipCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 64, 1, 1),
    _Pm1004dcpCntdwCbipCntIndex_Type()
)
pm1004dcpCntdwCbipCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdwCbipCntIndex.setStatus("current")
_Pm1004dcpCntdwCbipCntValuePortn_Type = Counter32
_Pm1004dcpCntdwCbipCntValuePortn_Object = MibTableColumn
pm1004dcpCntdwCbipCntValuePortn = _Pm1004dcpCntdwCbipCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 64, 1, 2),
    _Pm1004dcpCntdwCbipCntValuePortn_Type()
)
pm1004dcpCntdwCbipCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdwCbipCntValuePortn.setStatus("current")
_Pm1004dcpCntdwCbipCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntdwCbipCntErrorPortn_Object = MibTableColumn
pm1004dcpCntdwCbipCntErrorPortn = _Pm1004dcpCntdwCbipCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 64, 1, 3),
    _Pm1004dcpCntdwCbipCntErrorPortn_Type()
)
pm1004dcpCntdwCbipCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdwCbipCntErrorPortn.setStatus("current")
_Pm1004dcpCntdwCbipCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntdwCbipCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntdwCbipCntOverloadPortn = _Pm1004dcpCntdwCbipCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 64, 1, 4),
    _Pm1004dcpCntdwCbipCntOverloadPortn_Type()
)
pm1004dcpCntdwCbipCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdwCbipCntOverloadPortn.setStatus("current")
_Pm1004dcpCntdwTimCntTable_Object = MibTable
pm1004dcpCntdwTimCntTable = _Pm1004dcpCntdwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 72)
)
if mibBuilder.loadTexts:
    pm1004dcpCntdwTimCntTable.setStatus("current")
_Pm1004dcpCntdwTimCntEntry_Object = MibTableRow
pm1004dcpCntdwTimCntEntry = _Pm1004dcpCntdwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 72, 1)
)
pm1004dcpCntdwTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntdwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntdwTimCntEntry.setStatus("current")


class _Pm1004dcpCntdwTimCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntdwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntdwTimCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntdwTimCntIndex_Object = MibTableColumn
pm1004dcpCntdwTimCntIndex = _Pm1004dcpCntdwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 72, 1, 1),
    _Pm1004dcpCntdwTimCntIndex_Type()
)
pm1004dcpCntdwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdwTimCntIndex.setStatus("current")
_Pm1004dcpCntdwTimCntValuePortn_Type = Counter32
_Pm1004dcpCntdwTimCntValuePortn_Object = MibTableColumn
pm1004dcpCntdwTimCntValuePortn = _Pm1004dcpCntdwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 72, 1, 2),
    _Pm1004dcpCntdwTimCntValuePortn_Type()
)
pm1004dcpCntdwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdwTimCntValuePortn.setStatus("current")
_Pm1004dcpCntdwTimCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntdwTimCntErrorPortn_Object = MibTableColumn
pm1004dcpCntdwTimCntErrorPortn = _Pm1004dcpCntdwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 72, 1, 3),
    _Pm1004dcpCntdwTimCntErrorPortn_Type()
)
pm1004dcpCntdwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdwTimCntErrorPortn.setStatus("current")
_Pm1004dcpCntdwTimCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntdwTimCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntdwTimCntOverloadPortn = _Pm1004dcpCntdwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 2, 72, 1, 4),
    _Pm1004dcpCntdwTimCntOverloadPortn_Type()
)
pm1004dcpCntdwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdwTimCntOverloadPortn.setStatus("current")
_Pm1004dcpCntLine_ObjectIdentity = ObjectIdentity
pm1004dcpCntLine = _Pm1004dcpCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3)
)
_Pm1004dcpCntdfrmB1ErrCntTable_Object = MibTable
pm1004dcpCntdfrmB1ErrCntTable = _Pm1004dcpCntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmB1ErrCntTable.setStatus("current")
_Pm1004dcpCntdfrmB1ErrCntEntry_Object = MibTableRow
pm1004dcpCntdfrmB1ErrCntEntry = _Pm1004dcpCntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 152, 1)
)
pm1004dcpCntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmB1ErrCntEntry.setStatus("current")


class _Pm1004dcpCntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntdfrmB1ErrCntIndex_Object = MibTableColumn
pm1004dcpCntdfrmB1ErrCntIndex = _Pm1004dcpCntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 152, 1, 1),
    _Pm1004dcpCntdfrmB1ErrCntIndex_Type()
)
pm1004dcpCntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmB1ErrCntIndex.setStatus("current")
_Pm1004dcpCntdfrmB1ErrCntValuePortn_Type = Counter32
_Pm1004dcpCntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pm1004dcpCntdfrmB1ErrCntValuePortn = _Pm1004dcpCntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 152, 1, 2),
    _Pm1004dcpCntdfrmB1ErrCntValuePortn_Type()
)
pm1004dcpCntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmB1ErrCntValuePortn.setStatus("current")
_Pm1004dcpCntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm1004dcpCntdfrmB1ErrCntErrorPortn = _Pm1004dcpCntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 152, 1, 3),
    _Pm1004dcpCntdfrmB1ErrCntErrorPortn_Type()
)
pm1004dcpCntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pm1004dcpCntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntdfrmB1ErrCntOverloadPortn = _Pm1004dcpCntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 152, 1, 4),
    _Pm1004dcpCntdfrmB1ErrCntOverloadPortn_Type()
)
pm1004dcpCntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm1004dcpCntdfrmTimCntTable_Object = MibTable
pm1004dcpCntdfrmTimCntTable = _Pm1004dcpCntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmTimCntTable.setStatus("current")
_Pm1004dcpCntdfrmTimCntEntry_Object = MibTableRow
pm1004dcpCntdfrmTimCntEntry = _Pm1004dcpCntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 153, 1)
)
pm1004dcpCntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmTimCntEntry.setStatus("current")


class _Pm1004dcpCntdfrmTimCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntdfrmTimCntIndex_Object = MibTableColumn
pm1004dcpCntdfrmTimCntIndex = _Pm1004dcpCntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 153, 1, 1),
    _Pm1004dcpCntdfrmTimCntIndex_Type()
)
pm1004dcpCntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmTimCntIndex.setStatus("current")
_Pm1004dcpCntdfrmTimCntValuePortn_Type = Counter32
_Pm1004dcpCntdfrmTimCntValuePortn_Object = MibTableColumn
pm1004dcpCntdfrmTimCntValuePortn = _Pm1004dcpCntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 153, 1, 2),
    _Pm1004dcpCntdfrmTimCntValuePortn_Type()
)
pm1004dcpCntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmTimCntValuePortn.setStatus("current")
_Pm1004dcpCntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntdfrmTimCntErrorPortn_Object = MibTableColumn
pm1004dcpCntdfrmTimCntErrorPortn = _Pm1004dcpCntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 153, 1, 3),
    _Pm1004dcpCntdfrmTimCntErrorPortn_Type()
)
pm1004dcpCntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmTimCntErrorPortn.setStatus("current")
_Pm1004dcpCntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntdfrmTimCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntdfrmTimCntOverloadPortn = _Pm1004dcpCntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 153, 1, 4),
    _Pm1004dcpCntdfrmTimCntOverloadPortn_Type()
)
pm1004dcpCntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmTimCntOverloadPortn.setStatus("current")
_Pm1004dcpCntdfrmPrimLineErrCntTable_Object = MibTable
pm1004dcpCntdfrmPrimLineErrCntTable = _Pm1004dcpCntdfrmPrimLineErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 154)
)
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmPrimLineErrCntTable.setStatus("current")
_Pm1004dcpCntdfrmPrimLineErrCntEntry_Object = MibTableRow
pm1004dcpCntdfrmPrimLineErrCntEntry = _Pm1004dcpCntdfrmPrimLineErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 154, 1)
)
pm1004dcpCntdfrmPrimLineErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCntdfrmPrimLineErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmPrimLineErrCntEntry.setStatus("current")


class _Pm1004dcpCntdfrmPrimLineErrCntIndex_Type(Integer32):
    """Custom type pm1004dcpCntdfrmPrimLineErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCntdfrmPrimLineErrCntIndex_Type.__name__ = "Integer32"
_Pm1004dcpCntdfrmPrimLineErrCntIndex_Object = MibTableColumn
pm1004dcpCntdfrmPrimLineErrCntIndex = _Pm1004dcpCntdfrmPrimLineErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 154, 1, 1),
    _Pm1004dcpCntdfrmPrimLineErrCntIndex_Type()
)
pm1004dcpCntdfrmPrimLineErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmPrimLineErrCntIndex.setStatus("current")
_Pm1004dcpCntdfrmPrimLineErrCntValuePortn_Type = Counter32
_Pm1004dcpCntdfrmPrimLineErrCntValuePortn_Object = MibTableColumn
pm1004dcpCntdfrmPrimLineErrCntValuePortn = _Pm1004dcpCntdfrmPrimLineErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 154, 1, 2),
    _Pm1004dcpCntdfrmPrimLineErrCntValuePortn_Type()
)
pm1004dcpCntdfrmPrimLineErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmPrimLineErrCntValuePortn.setStatus("current")
_Pm1004dcpCntdfrmPrimLineErrCntErrorPortn_Type = EkiOnOff
_Pm1004dcpCntdfrmPrimLineErrCntErrorPortn_Object = MibTableColumn
pm1004dcpCntdfrmPrimLineErrCntErrorPortn = _Pm1004dcpCntdfrmPrimLineErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 154, 1, 3),
    _Pm1004dcpCntdfrmPrimLineErrCntErrorPortn_Type()
)
pm1004dcpCntdfrmPrimLineErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmPrimLineErrCntErrorPortn.setStatus("current")
_Pm1004dcpCntdfrmPrimLineErrCntOverloadPortn_Type = EkiOnOff
_Pm1004dcpCntdfrmPrimLineErrCntOverloadPortn_Object = MibTableColumn
pm1004dcpCntdfrmPrimLineErrCntOverloadPortn = _Pm1004dcpCntdfrmPrimLineErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 3, 154, 1, 4),
    _Pm1004dcpCntdfrmPrimLineErrCntOverloadPortn_Type()
)
pm1004dcpCntdfrmPrimLineErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCntdfrmPrimLineErrCntOverloadPortn.setStatus("current")
_Pm1004dcpCntCountersReset_Type = EkiOnOff
_Pm1004dcpCntCountersReset_Object = MibScalar
pm1004dcpCntCountersReset = _Pm1004dcpCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 259),
    _Pm1004dcpCntCountersReset_Type()
)
pm1004dcpCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCntCountersReset.setStatus("current")
_Pm1004dcpCntCountersStop_Type = EkiOnOff
_Pm1004dcpCntCountersStop_Object = MibScalar
pm1004dcpCntCountersStop = _Pm1004dcpCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 4, 260),
    _Pm1004dcpCntCountersStop_Type()
)
pm1004dcpCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCntCountersStop.setStatus("current")
_Pm1004dcpcontrolsWrite_ObjectIdentity = ObjectIdentity
pm1004dcpcontrolsWrite = _Pm1004dcpcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6)
)
_Pm1004dcpCtrlOther_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlOther = _Pm1004dcpCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1)
)
_Pm1004dcpCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlconfMgnt1 = _Pm1004dcpCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 1)
)
_Pm1004dcpCtrlConf1Load1_Type = EkiOnOff
_Pm1004dcpCtrlConf1Load1_Object = MibScalar
pm1004dcpCtrlConf1Load1 = _Pm1004dcpCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 1, 1),
    _Pm1004dcpCtrlConf1Load1_Type()
)
pm1004dcpCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlConf1Load1.setStatus("current")
_Pm1004dcpCtrlConf2Load1_Type = EkiOnOff
_Pm1004dcpCtrlConf2Load1_Object = MibScalar
pm1004dcpCtrlConf2Load1 = _Pm1004dcpCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 1, 2),
    _Pm1004dcpCtrlConf2Load1_Type()
)
pm1004dcpCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlConf2Load1.setStatus("current")
_Pm1004dcpCtrlConf2Flash1_Type = EkiOnOff
_Pm1004dcpCtrlConf2Flash1_Object = MibScalar
pm1004dcpCtrlConf2Flash1 = _Pm1004dcpCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 1, 10),
    _Pm1004dcpCtrlConf2Flash1_Type()
)
pm1004dcpCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlConf2Flash1.setStatus("current")
_Pm1004dcpCtrlConf2Clear1_Type = EkiOnOff
_Pm1004dcpCtrlConf2Clear1_Object = MibScalar
pm1004dcpCtrlConf2Clear1 = _Pm1004dcpCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 1, 14),
    _Pm1004dcpCtrlConf2Clear1_Type()
)
pm1004dcpCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlConf2Clear1.setStatus("current")
_Pm1004dcpCtrlsynth4_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlsynth4 = _Pm1004dcpCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 4)
)
_Pm1004dcpCtrlCorrelatOn_Type = EkiOnOff
_Pm1004dcpCtrlCorrelatOn_Object = MibScalar
pm1004dcpCtrlCorrelatOn = _Pm1004dcpCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 4, 1),
    _Pm1004dcpCtrlCorrelatOn_Type()
)
pm1004dcpCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlCorrelatOn.setStatus("current")
_Pm1004dcpCtrlCorrelatOff_Type = EkiOnOff
_Pm1004dcpCtrlCorrelatOff_Object = MibScalar
pm1004dcpCtrlCorrelatOff = _Pm1004dcpCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 4, 2),
    _Pm1004dcpCtrlCorrelatOff_Type()
)
pm1004dcpCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlCorrelatOff.setStatus("current")
_Pm1004dcpCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlswMgnt = _Pm1004dcpCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 5)
)
_Pm1004dcpCtrlColdReset_Type = EkiOnOff
_Pm1004dcpCtrlColdReset_Object = MibScalar
pm1004dcpCtrlColdReset = _Pm1004dcpCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 5, 2),
    _Pm1004dcpCtrlColdReset_Type()
)
pm1004dcpCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlColdReset.setStatus("current")
_Pm1004dcpCtrlWarmReset_Type = EkiOnOff
_Pm1004dcpCtrlWarmReset_Object = MibScalar
pm1004dcpCtrlWarmReset = _Pm1004dcpCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 5, 3),
    _Pm1004dcpCtrlWarmReset_Type()
)
pm1004dcpCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlWarmReset.setStatus("current")
_Pm1004dcpCtrlLoadSwBank1_Type = EkiOnOff
_Pm1004dcpCtrlLoadSwBank1_Object = MibScalar
pm1004dcpCtrlLoadSwBank1 = _Pm1004dcpCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 5, 5),
    _Pm1004dcpCtrlLoadSwBank1_Type()
)
pm1004dcpCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlLoadSwBank1.setStatus("current")
_Pm1004dcpCtrlLoadSwBank2_Type = EkiOnOff
_Pm1004dcpCtrlLoadSwBank2_Object = MibScalar
pm1004dcpCtrlLoadSwBank2 = _Pm1004dcpCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 5, 6),
    _Pm1004dcpCtrlLoadSwBank2_Type()
)
pm1004dcpCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlLoadSwBank2.setStatus("current")
_Pm1004dcpCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlgwMgnt = _Pm1004dcpCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 6)
)
_Pm1004dcpCtrlCurrentGwReset_Type = EkiOnOff
_Pm1004dcpCtrlCurrentGwReset_Object = MibScalar
pm1004dcpCtrlCurrentGwReset = _Pm1004dcpCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 6, 1),
    _Pm1004dcpCtrlCurrentGwReset_Type()
)
pm1004dcpCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlCurrentGwReset.setStatus("current")
_Pm1004dcpCtrlLoadGwBank1_Type = EkiOnOff
_Pm1004dcpCtrlLoadGwBank1_Object = MibScalar
pm1004dcpCtrlLoadGwBank1 = _Pm1004dcpCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 6, 5),
    _Pm1004dcpCtrlLoadGwBank1_Type()
)
pm1004dcpCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlLoadGwBank1.setStatus("current")
_Pm1004dcpCtrlLoadGwBank2_Type = EkiOnOff
_Pm1004dcpCtrlLoadGwBank2_Object = MibScalar
pm1004dcpCtrlLoadGwBank2 = _Pm1004dcpCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 6, 6),
    _Pm1004dcpCtrlLoadGwBank2_Type()
)
pm1004dcpCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlLoadGwBank2.setStatus("current")
_Pm1004dcpCtrlLoadGwBank3_Type = EkiOnOff
_Pm1004dcpCtrlLoadGwBank3_Object = MibScalar
pm1004dcpCtrlLoadGwBank3 = _Pm1004dcpCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 6, 7),
    _Pm1004dcpCtrlLoadGwBank3_Type()
)
pm1004dcpCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlLoadGwBank3.setStatus("current")
_Pm1004dcpCtrlLoadGwBank4_Type = EkiOnOff
_Pm1004dcpCtrlLoadGwBank4_Object = MibScalar
pm1004dcpCtrlLoadGwBank4 = _Pm1004dcpCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 6, 8),
    _Pm1004dcpCtrlLoadGwBank4_Type()
)
pm1004dcpCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlLoadGwBank4.setStatus("current")
_Pm1004dcpCtrlledTest_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlledTest = _Pm1004dcpCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 192)
)
_Pm1004dcpCtrlGreenLed_Type = EkiOnOff
_Pm1004dcpCtrlGreenLed_Object = MibScalar
pm1004dcpCtrlGreenLed = _Pm1004dcpCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 192, 1),
    _Pm1004dcpCtrlGreenLed_Type()
)
pm1004dcpCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlGreenLed.setStatus("current")
_Pm1004dcpCtrlRedLed_Type = EkiOnOff
_Pm1004dcpCtrlRedLed_Object = MibScalar
pm1004dcpCtrlRedLed = _Pm1004dcpCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 192, 2),
    _Pm1004dcpCtrlRedLed_Type()
)
pm1004dcpCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlRedLed.setStatus("current")
_Pm1004dcpCtrlLedOff_Type = EkiOnOff
_Pm1004dcpCtrlLedOff_Object = MibScalar
pm1004dcpCtrlLedOff = _Pm1004dcpCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 192, 3),
    _Pm1004dcpCtrlLedOff_Type()
)
pm1004dcpCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlLedOff.setStatus("current")
_Pm1004dcpCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlmoduleOosMode = _Pm1004dcpCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 193)
)
_Pm1004dcpCtrlModuleOosMode_Type = EkiOnOff
_Pm1004dcpCtrlModuleOosMode_Object = MibScalar
pm1004dcpCtrlModuleOosMode = _Pm1004dcpCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 193, 1),
    _Pm1004dcpCtrlModuleOosMode_Type()
)
pm1004dcpCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlModuleOosMode.setStatus("current")
_Pm1004dcpCtrlmoduleDccMgnt_Type = Pm1004dcpDccMode
_Pm1004dcpCtrlmoduleDccMgnt_Object = MibScalar
pm1004dcpCtrlmoduleDccMgnt = _Pm1004dcpCtrlmoduleDccMgnt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 196),
    _Pm1004dcpCtrlmoduleDccMgnt_Type()
)
pm1004dcpCtrlmoduleDccMgnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlmoduleDccMgnt.setStatus("current")
_Pm1004dcpCtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlmaintenanceMode = _Pm1004dcpCtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 197)
)
_Pm1004dcpCtrlMaintenanceMode_Type = EkiOnOff
_Pm1004dcpCtrlMaintenanceMode_Object = MibScalar
pm1004dcpCtrlMaintenanceMode = _Pm1004dcpCtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 1, 197, 1),
    _Pm1004dcpCtrlMaintenanceMode_Type()
)
pm1004dcpCtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlMaintenanceMode.setStatus("current")
_Pm1004dcpCtrlClient_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlClient = _Pm1004dcpCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2)
)
_Pm1004dcpCtrlaccessLoopTable_Object = MibTable
pm1004dcpCtrlaccessLoopTable = _Pm1004dcpCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlaccessLoopTable.setStatus("current")
_Pm1004dcpCtrlaccessLoopEntry_Object = MibTableRow
pm1004dcpCtrlaccessLoopEntry = _Pm1004dcpCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 16, 1)
)
pm1004dcpCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlaccessLoopEntry.setStatus("current")


class _Pm1004dcpCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlaccessLoopIndex_Object = MibTableColumn
pm1004dcpCtrlaccessLoopIndex = _Pm1004dcpCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 16, 1, 1),
    _Pm1004dcpCtrlaccessLoopIndex_Type()
)
pm1004dcpCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlaccessLoopIndex.setStatus("current")
_Pm1004dcpCtrlaccessLoopPortn_Type = EkiState
_Pm1004dcpCtrlaccessLoopPortn_Object = MibTableColumn
pm1004dcpCtrlaccessLoopPortn = _Pm1004dcpCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 16, 1, 2),
    _Pm1004dcpCtrlaccessLoopPortn_Type()
)
pm1004dcpCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlaccessLoopPortn.setStatus("current")
_Pm1004dcpCtrlportOosModeTable_Object = MibTable
pm1004dcpCtrlportOosModeTable = _Pm1004dcpCtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlportOosModeTable.setStatus("current")
_Pm1004dcpCtrlportOosModeEntry_Object = MibTableRow
pm1004dcpCtrlportOosModeEntry = _Pm1004dcpCtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 18, 1)
)
pm1004dcpCtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlportOosModeEntry.setStatus("current")


class _Pm1004dcpCtrlportOosModeIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlportOosModeIndex_Object = MibTableColumn
pm1004dcpCtrlportOosModeIndex = _Pm1004dcpCtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 18, 1, 1),
    _Pm1004dcpCtrlportOosModeIndex_Type()
)
pm1004dcpCtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlportOosModeIndex.setStatus("current")
_Pm1004dcpCtrlportOosModePortn_Type = EkiState
_Pm1004dcpCtrlportOosModePortn_Object = MibTableColumn
pm1004dcpCtrlportOosModePortn = _Pm1004dcpCtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 18, 1, 2),
    _Pm1004dcpCtrlportOosModePortn_Type()
)
pm1004dcpCtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlportOosModePortn.setStatus("current")
_Pm1004dcpCtrlsfpOnCtrlTable_Object = MibTable
pm1004dcpCtrlsfpOnCtrlTable = _Pm1004dcpCtrlsfpOnCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 19)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlsfpOnCtrlTable.setStatus("current")
_Pm1004dcpCtrlsfpOnCtrlEntry_Object = MibTableRow
pm1004dcpCtrlsfpOnCtrlEntry = _Pm1004dcpCtrlsfpOnCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 19, 1)
)
pm1004dcpCtrlsfpOnCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlsfpOnCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlsfpOnCtrlEntry.setStatus("current")


class _Pm1004dcpCtrlsfpOnCtrlIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlsfpOnCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlsfpOnCtrlIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlsfpOnCtrlIndex_Object = MibTableColumn
pm1004dcpCtrlsfpOnCtrlIndex = _Pm1004dcpCtrlsfpOnCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 19, 1, 1),
    _Pm1004dcpCtrlsfpOnCtrlIndex_Type()
)
pm1004dcpCtrlsfpOnCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlsfpOnCtrlIndex.setStatus("current")
_Pm1004dcpCtrlsfpOnCtrlPortn_Type = EkiState
_Pm1004dcpCtrlsfpOnCtrlPortn_Object = MibTableColumn
pm1004dcpCtrlsfpOnCtrlPortn = _Pm1004dcpCtrlsfpOnCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 19, 1, 2),
    _Pm1004dcpCtrlsfpOnCtrlPortn_Type()
)
pm1004dcpCtrlsfpOnCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlsfpOnCtrlPortn.setStatus("current")
_Pm1004dcpCtrlsfpOffCtrlTable_Object = MibTable
pm1004dcpCtrlsfpOffCtrlTable = _Pm1004dcpCtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlsfpOffCtrlTable.setStatus("current")
_Pm1004dcpCtrlsfpOffCtrlEntry_Object = MibTableRow
pm1004dcpCtrlsfpOffCtrlEntry = _Pm1004dcpCtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 20, 1)
)
pm1004dcpCtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlsfpOffCtrlEntry.setStatus("current")


class _Pm1004dcpCtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlsfpOffCtrlIndex_Object = MibTableColumn
pm1004dcpCtrlsfpOffCtrlIndex = _Pm1004dcpCtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 20, 1, 1),
    _Pm1004dcpCtrlsfpOffCtrlIndex_Type()
)
pm1004dcpCtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlsfpOffCtrlIndex.setStatus("current")
_Pm1004dcpCtrlsfpOffCtrlPortn_Type = EkiState
_Pm1004dcpCtrlsfpOffCtrlPortn_Object = MibTableColumn
pm1004dcpCtrlsfpOffCtrlPortn = _Pm1004dcpCtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 20, 1, 2),
    _Pm1004dcpCtrlsfpOffCtrlPortn_Type()
)
pm1004dcpCtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlsfpOffCtrlPortn.setStatus("current")
_Pm1004dcpCtrlcsfUpInsTable_Object = MibTable
pm1004dcpCtrlcsfUpInsTable = _Pm1004dcpCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlcsfUpInsTable.setStatus("current")
_Pm1004dcpCtrlcsfUpInsEntry_Object = MibTableRow
pm1004dcpCtrlcsfUpInsEntry = _Pm1004dcpCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 21, 1)
)
pm1004dcpCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlcsfUpInsEntry.setStatus("current")


class _Pm1004dcpCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlcsfUpInsIndex_Object = MibTableColumn
pm1004dcpCtrlcsfUpInsIndex = _Pm1004dcpCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 21, 1, 1),
    _Pm1004dcpCtrlcsfUpInsIndex_Type()
)
pm1004dcpCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlcsfUpInsIndex.setStatus("current")
_Pm1004dcpCtrlcsfUpInsPortn_Type = EkiState
_Pm1004dcpCtrlcsfUpInsPortn_Object = MibTableColumn
pm1004dcpCtrlcsfUpInsPortn = _Pm1004dcpCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 21, 1, 2),
    _Pm1004dcpCtrlcsfUpInsPortn_Type()
)
pm1004dcpCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlcsfUpInsPortn.setStatus("current")
_Pm1004dcpCtrlcaisDwInsTable_Object = MibTable
pm1004dcpCtrlcaisDwInsTable = _Pm1004dcpCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlcaisDwInsTable.setStatus("current")
_Pm1004dcpCtrlcaisDwInsEntry_Object = MibTableRow
pm1004dcpCtrlcaisDwInsEntry = _Pm1004dcpCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 22, 1)
)
pm1004dcpCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlcaisDwInsEntry.setStatus("current")


class _Pm1004dcpCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlcaisDwInsIndex_Object = MibTableColumn
pm1004dcpCtrlcaisDwInsIndex = _Pm1004dcpCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 22, 1, 1),
    _Pm1004dcpCtrlcaisDwInsIndex_Type()
)
pm1004dcpCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlcaisDwInsIndex.setStatus("current")
_Pm1004dcpCtrlcaisDwInsPortn_Type = EkiState
_Pm1004dcpCtrlcaisDwInsPortn_Object = MibTableColumn
pm1004dcpCtrlcaisDwInsPortn = _Pm1004dcpCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 22, 1, 2),
    _Pm1004dcpCtrlcaisDwInsPortn_Type()
)
pm1004dcpCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlcaisDwInsPortn.setStatus("current")
_Pm1004dcpCtrlclientAccessTermLoopTable_Object = MibTable
pm1004dcpCtrlclientAccessTermLoopTable = _Pm1004dcpCtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlclientAccessTermLoopTable.setStatus("current")
_Pm1004dcpCtrlclientAccessTermLoopEntry_Object = MibTableRow
pm1004dcpCtrlclientAccessTermLoopEntry = _Pm1004dcpCtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 26, 1)
)
pm1004dcpCtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm1004dcpCtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm1004dcpCtrlclientAccessTermLoopIndex = _Pm1004dcpCtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 26, 1, 1),
    _Pm1004dcpCtrlclientAccessTermLoopIndex_Type()
)
pm1004dcpCtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlclientAccessTermLoopIndex.setStatus("current")
_Pm1004dcpCtrlclientAccessTermLoopPortn_Type = EkiState
_Pm1004dcpCtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm1004dcpCtrlclientAccessTermLoopPortn = _Pm1004dcpCtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 26, 1, 2),
    _Pm1004dcpCtrlclientAccessTermLoopPortn_Type()
)
pm1004dcpCtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlclientAccessTermLoopPortn.setStatus("current")
_Pm1004dcpCtrlresetCount15PortTable_Object = MibTable
pm1004dcpCtrlresetCount15PortTable = _Pm1004dcpCtrlresetCount15PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 35)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlresetCount15PortTable.setStatus("current")
_Pm1004dcpCtrlresetCount15PortEntry_Object = MibTableRow
pm1004dcpCtrlresetCount15PortEntry = _Pm1004dcpCtrlresetCount15PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 35, 1)
)
pm1004dcpCtrlresetCount15PortEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlresetCount15PortIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlresetCount15PortEntry.setStatus("current")


class _Pm1004dcpCtrlresetCount15PortIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlresetCount15PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlresetCount15PortIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlresetCount15PortIndex_Object = MibTableColumn
pm1004dcpCtrlresetCount15PortIndex = _Pm1004dcpCtrlresetCount15PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 35, 1, 1),
    _Pm1004dcpCtrlresetCount15PortIndex_Type()
)
pm1004dcpCtrlresetCount15PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlresetCount15PortIndex.setStatus("current")
_Pm1004dcpCtrlclientResetAllPerfCount15Portn_Type = EkiState
_Pm1004dcpCtrlclientResetAllPerfCount15Portn_Object = MibTableColumn
pm1004dcpCtrlclientResetAllPerfCount15Portn = _Pm1004dcpCtrlclientResetAllPerfCount15Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 35, 1, 2),
    _Pm1004dcpCtrlclientResetAllPerfCount15Portn_Type()
)
pm1004dcpCtrlclientResetAllPerfCount15Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlclientResetAllPerfCount15Portn.setStatus("current")
_Pm1004dcpCtrlresetCount24PortTable_Object = MibTable
pm1004dcpCtrlresetCount24PortTable = _Pm1004dcpCtrlresetCount24PortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 36)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlresetCount24PortTable.setStatus("current")
_Pm1004dcpCtrlresetCount24PortEntry_Object = MibTableRow
pm1004dcpCtrlresetCount24PortEntry = _Pm1004dcpCtrlresetCount24PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 36, 1)
)
pm1004dcpCtrlresetCount24PortEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlresetCount24PortIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlresetCount24PortEntry.setStatus("current")


class _Pm1004dcpCtrlresetCount24PortIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlresetCount24PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlresetCount24PortIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlresetCount24PortIndex_Object = MibTableColumn
pm1004dcpCtrlresetCount24PortIndex = _Pm1004dcpCtrlresetCount24PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 36, 1, 1),
    _Pm1004dcpCtrlresetCount24PortIndex_Type()
)
pm1004dcpCtrlresetCount24PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlresetCount24PortIndex.setStatus("current")
_Pm1004dcpCtrlclientResetAllPerfCount24Portn_Type = EkiState
_Pm1004dcpCtrlclientResetAllPerfCount24Portn_Object = MibTableColumn
pm1004dcpCtrlclientResetAllPerfCount24Portn = _Pm1004dcpCtrlclientResetAllPerfCount24Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 36, 1, 2),
    _Pm1004dcpCtrlclientResetAllPerfCount24Portn_Type()
)
pm1004dcpCtrlclientResetAllPerfCount24Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlclientResetAllPerfCount24Portn.setStatus("current")
_Pm1004dcpCtrladddropTsClientARxProtectTable_Object = MibTable
pm1004dcpCtrladddropTsClientARxProtectTable = _Pm1004dcpCtrladddropTsClientARxProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 128)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrladddropTsClientARxProtectTable.setStatus("current")
_Pm1004dcpCtrladddropTsClientARxProtectEntry_Object = MibTableRow
pm1004dcpCtrladddropTsClientARxProtectEntry = _Pm1004dcpCtrladddropTsClientARxProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 128, 1)
)
pm1004dcpCtrladddropTsClientARxProtectEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrladddropTsClientARxProtectIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrladddropTsClientARxProtectEntry.setStatus("current")


class _Pm1004dcpCtrladddropTsClientARxProtectIndex_Type(Integer32):
    """Custom type pm1004dcpCtrladddropTsClientARxProtectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrladddropTsClientARxProtectIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrladddropTsClientARxProtectIndex_Object = MibTableColumn
pm1004dcpCtrladddropTsClientARxProtectIndex = _Pm1004dcpCtrladddropTsClientARxProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 128, 1, 1),
    _Pm1004dcpCtrladddropTsClientARxProtectIndex_Type()
)
pm1004dcpCtrladddropTsClientARxProtectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrladddropTsClientARxProtectIndex.setStatus("current")
_Pm1004dcpCtrladddropTsClientARxProtectPortn_Type = Pm1004dcpProtectionTimeSlot
_Pm1004dcpCtrladddropTsClientARxProtectPortn_Object = MibTableColumn
pm1004dcpCtrladddropTsClientARxProtectPortn = _Pm1004dcpCtrladddropTsClientARxProtectPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 128, 1, 2),
    _Pm1004dcpCtrladddropTsClientARxProtectPortn_Type()
)
pm1004dcpCtrladddropTsClientARxProtectPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrladddropTsClientARxProtectPortn.setStatus("current")
_Pm1004dcpCtrladddropTsPairModeTable_Object = MibTable
pm1004dcpCtrladddropTsPairModeTable = _Pm1004dcpCtrladddropTsPairModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 136)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrladddropTsPairModeTable.setStatus("current")
_Pm1004dcpCtrladddropTsPairModeEntry_Object = MibTableRow
pm1004dcpCtrladddropTsPairModeEntry = _Pm1004dcpCtrladddropTsPairModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 136, 1)
)
pm1004dcpCtrladddropTsPairModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrladddropTsPairModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrladddropTsPairModeEntry.setStatus("current")


class _Pm1004dcpCtrladddropTsPairModeIndex_Type(Integer32):
    """Custom type pm1004dcpCtrladddropTsPairModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrladddropTsPairModeIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrladddropTsPairModeIndex_Object = MibTableColumn
pm1004dcpCtrladddropTsPairModeIndex = _Pm1004dcpCtrladddropTsPairModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 136, 1, 1),
    _Pm1004dcpCtrladddropTsPairModeIndex_Type()
)
pm1004dcpCtrladddropTsPairModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrladddropTsPairModeIndex.setStatus("current")
_Pm1004dcpCtrladddropTsPairModePortn_Type = Pm1004dcpModeTimeSlot
_Pm1004dcpCtrladddropTsPairModePortn_Object = MibTableColumn
pm1004dcpCtrladddropTsPairModePortn = _Pm1004dcpCtrladddropTsPairModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 2, 136, 1, 2),
    _Pm1004dcpCtrladddropTsPairModePortn_Type()
)
pm1004dcpCtrladddropTsPairModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrladddropTsPairModePortn.setStatus("current")
_Pm1004dcpCtrlLine_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlLine = _Pm1004dcpCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3)
)
_Pm1004dcpCtrlcommAccessLoop_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlcommAccessLoop = _Pm1004dcpCtrlcommAccessLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 64)
)
_Pm1004dcpCtrlCommAccessloop_Type = EkiOnOff
_Pm1004dcpCtrlCommAccessloop_Object = MibScalar
pm1004dcpCtrlCommAccessloop = _Pm1004dcpCtrlCommAccessloop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 64, 1),
    _Pm1004dcpCtrlCommAccessloop_Type()
)
pm1004dcpCtrlCommAccessloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlCommAccessloop.setStatus("deprecated")
_Pm1004dcpCtrllineLoop_ObjectIdentity = ObjectIdentity
pm1004dcpCtrllineLoop = _Pm1004dcpCtrllineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 66)
)
_Pm1004dcpCtrlLineLoop_Type = EkiOnOff
_Pm1004dcpCtrlLineLoop_Object = MibScalar
pm1004dcpCtrlLineLoop = _Pm1004dcpCtrlLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 66, 1),
    _Pm1004dcpCtrlLineLoop_Type()
)
pm1004dcpCtrlLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlLineLoop.setStatus("deprecated")
_Pm1004dcpCtrlmsAis_ObjectIdentity = ObjectIdentity
pm1004dcpCtrlmsAis = _Pm1004dcpCtrlmsAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 67)
)
_Pm1004dcpCtrlMsAis_Type = EkiOnOff
_Pm1004dcpCtrlMsAis_Object = MibScalar
pm1004dcpCtrlMsAis = _Pm1004dcpCtrlMsAis_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 67, 1),
    _Pm1004dcpCtrlMsAis_Type()
)
pm1004dcpCtrlMsAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlMsAis.setStatus("current")
_Pm1004dcpCtrlfecDisableTable_Object = MibTable
pm1004dcpCtrlfecDisableTable = _Pm1004dcpCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlfecDisableTable.setStatus("current")
_Pm1004dcpCtrlfecDisableEntry_Object = MibTableRow
pm1004dcpCtrlfecDisableEntry = _Pm1004dcpCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 69, 1)
)
pm1004dcpCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlfecDisableEntry.setStatus("current")


class _Pm1004dcpCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlfecDisableIndex_Object = MibTableColumn
pm1004dcpCtrlfecDisableIndex = _Pm1004dcpCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 69, 1, 1),
    _Pm1004dcpCtrlfecDisableIndex_Type()
)
pm1004dcpCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlfecDisableIndex.setStatus("current")
_Pm1004dcpCtrlfecDisablePortn_Type = EkiState
_Pm1004dcpCtrlfecDisablePortn_Object = MibTableColumn
pm1004dcpCtrlfecDisablePortn = _Pm1004dcpCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 69, 1, 2),
    _Pm1004dcpCtrlfecDisablePortn_Type()
)
pm1004dcpCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlfecDisablePortn.setStatus("current")
_Pm1004dcpCtrllineOosModeTable_Object = MibTable
pm1004dcpCtrllineOosModeTable = _Pm1004dcpCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllineOosModeTable.setStatus("current")
_Pm1004dcpCtrllineOosModeEntry_Object = MibTableRow
pm1004dcpCtrllineOosModeEntry = _Pm1004dcpCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 74, 1)
)
pm1004dcpCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllineOosModeEntry.setStatus("current")


class _Pm1004dcpCtrllineOosModeIndex_Type(Integer32):
    """Custom type pm1004dcpCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrllineOosModeIndex_Object = MibTableColumn
pm1004dcpCtrllineOosModeIndex = _Pm1004dcpCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 74, 1, 1),
    _Pm1004dcpCtrllineOosModeIndex_Type()
)
pm1004dcpCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrllineOosModeIndex.setStatus("current")
_Pm1004dcpCtrllineOosModePortn_Type = EkiState
_Pm1004dcpCtrllineOosModePortn_Object = MibTableColumn
pm1004dcpCtrllineOosModePortn = _Pm1004dcpCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 74, 1, 2),
    _Pm1004dcpCtrllineOosModePortn_Type()
)
pm1004dcpCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrllineOosModePortn.setStatus("current")
_Pm1004dcpCtrllineResetCount15LineTable_Object = MibTable
pm1004dcpCtrllineResetCount15LineTable = _Pm1004dcpCtrllineResetCount15LineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 86)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllineResetCount15LineTable.setStatus("current")
_Pm1004dcpCtrllineResetCount15LineEntry_Object = MibTableRow
pm1004dcpCtrllineResetCount15LineEntry = _Pm1004dcpCtrllineResetCount15LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 86, 1)
)
pm1004dcpCtrllineResetCount15LineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrllineResetCount15LineIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllineResetCount15LineEntry.setStatus("current")


class _Pm1004dcpCtrllineResetCount15LineIndex_Type(Integer32):
    """Custom type pm1004dcpCtrllineResetCount15LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrllineResetCount15LineIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrllineResetCount15LineIndex_Object = MibTableColumn
pm1004dcpCtrllineResetCount15LineIndex = _Pm1004dcpCtrllineResetCount15LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 86, 1, 1),
    _Pm1004dcpCtrllineResetCount15LineIndex_Type()
)
pm1004dcpCtrllineResetCount15LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrllineResetCount15LineIndex.setStatus("current")
_Pm1004dcpCtrlresetAllPerfCount15Portn_Type = EkiState
_Pm1004dcpCtrlresetAllPerfCount15Portn_Object = MibTableColumn
pm1004dcpCtrlresetAllPerfCount15Portn = _Pm1004dcpCtrlresetAllPerfCount15Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 86, 1, 2),
    _Pm1004dcpCtrlresetAllPerfCount15Portn_Type()
)
pm1004dcpCtrlresetAllPerfCount15Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlresetAllPerfCount15Portn.setStatus("current")
_Pm1004dcpCtrllineResetCount24LineTable_Object = MibTable
pm1004dcpCtrllineResetCount24LineTable = _Pm1004dcpCtrllineResetCount24LineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 87)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllineResetCount24LineTable.setStatus("current")
_Pm1004dcpCtrllineResetCount24LineEntry_Object = MibTableRow
pm1004dcpCtrllineResetCount24LineEntry = _Pm1004dcpCtrllineResetCount24LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 87, 1)
)
pm1004dcpCtrllineResetCount24LineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrllineResetCount24LineIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllineResetCount24LineEntry.setStatus("current")


class _Pm1004dcpCtrllineResetCount24LineIndex_Type(Integer32):
    """Custom type pm1004dcpCtrllineResetCount24LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrllineResetCount24LineIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrllineResetCount24LineIndex_Object = MibTableColumn
pm1004dcpCtrllineResetCount24LineIndex = _Pm1004dcpCtrllineResetCount24LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 87, 1, 1),
    _Pm1004dcpCtrllineResetCount24LineIndex_Type()
)
pm1004dcpCtrllineResetCount24LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrllineResetCount24LineIndex.setStatus("current")
_Pm1004dcpCtrlresetAllPerfCount24Portn_Type = EkiState
_Pm1004dcpCtrlresetAllPerfCount24Portn_Object = MibTableColumn
pm1004dcpCtrlresetAllPerfCount24Portn = _Pm1004dcpCtrlresetAllPerfCount24Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 87, 1, 2),
    _Pm1004dcpCtrlresetAllPerfCount24Portn_Type()
)
pm1004dcpCtrlresetAllPerfCount24Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlresetAllPerfCount24Portn.setStatus("current")
_Pm1004dcpCtrlxfpOnoffTable_Object = MibTable
pm1004dcpCtrlxfpOnoffTable = _Pm1004dcpCtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpOnoffTable.setStatus("current")
_Pm1004dcpCtrlxfpOnoffEntry_Object = MibTableRow
pm1004dcpCtrlxfpOnoffEntry = _Pm1004dcpCtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 208, 1)
)
pm1004dcpCtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpOnoffEntry.setStatus("current")


class _Pm1004dcpCtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlxfpOnoffIndex_Object = MibTableColumn
pm1004dcpCtrlxfpOnoffIndex = _Pm1004dcpCtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 208, 1, 1),
    _Pm1004dcpCtrlxfpOnoffIndex_Type()
)
pm1004dcpCtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpOnoffIndex.setStatus("current")
_Pm1004dcpCtrlxfpOnoffPortn_Type = EkiState
_Pm1004dcpCtrlxfpOnoffPortn_Object = MibTableColumn
pm1004dcpCtrlxfpOnoffPortn = _Pm1004dcpCtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 208, 1, 2),
    _Pm1004dcpCtrlxfpOnoffPortn_Type()
)
pm1004dcpCtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpOnoffPortn.setStatus("current")
_Pm1004dcpCtrlxfpLineLoopTable_Object = MibTable
pm1004dcpCtrlxfpLineLoopTable = _Pm1004dcpCtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpLineLoopTable.setStatus("current")
_Pm1004dcpCtrlxfpLineLoopEntry_Object = MibTableRow
pm1004dcpCtrlxfpLineLoopEntry = _Pm1004dcpCtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 209, 1)
)
pm1004dcpCtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpLineLoopEntry.setStatus("current")


class _Pm1004dcpCtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlxfpLineLoopIndex_Object = MibTableColumn
pm1004dcpCtrlxfpLineLoopIndex = _Pm1004dcpCtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 209, 1, 1),
    _Pm1004dcpCtrlxfpLineLoopIndex_Type()
)
pm1004dcpCtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpLineLoopIndex.setStatus("current")
_Pm1004dcpCtrlxfpLineLoopPortn_Type = EkiState
_Pm1004dcpCtrlxfpLineLoopPortn_Object = MibTableColumn
pm1004dcpCtrlxfpLineLoopPortn = _Pm1004dcpCtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 209, 1, 2),
    _Pm1004dcpCtrlxfpLineLoopPortn_Type()
)
pm1004dcpCtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpLineLoopPortn.setStatus("current")
_Pm1004dcpCtrlxfpXfiLoopTable_Object = MibTable
pm1004dcpCtrlxfpXfiLoopTable = _Pm1004dcpCtrlxfpXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpXfiLoopTable.setStatus("current")
_Pm1004dcpCtrlxfpXfiLoopEntry_Object = MibTableRow
pm1004dcpCtrlxfpXfiLoopEntry = _Pm1004dcpCtrlxfpXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 210, 1)
)
pm1004dcpCtrlxfpXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrlxfpXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpXfiLoopEntry.setStatus("current")


class _Pm1004dcpCtrlxfpXfiLoopIndex_Type(Integer32):
    """Custom type pm1004dcpCtrlxfpXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrlxfpXfiLoopIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrlxfpXfiLoopIndex_Object = MibTableColumn
pm1004dcpCtrlxfpXfiLoopIndex = _Pm1004dcpCtrlxfpXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 210, 1, 1),
    _Pm1004dcpCtrlxfpXfiLoopIndex_Type()
)
pm1004dcpCtrlxfpXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpXfiLoopIndex.setStatus("current")
_Pm1004dcpCtrlxfpXfiLoopPortn_Type = EkiState
_Pm1004dcpCtrlxfpXfiLoopPortn_Object = MibTableColumn
pm1004dcpCtrlxfpXfiLoopPortn = _Pm1004dcpCtrlxfpXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 210, 1, 2),
    _Pm1004dcpCtrlxfpXfiLoopPortn_Type()
)
pm1004dcpCtrlxfpXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrlxfpXfiLoopPortn.setStatus("current")
_Pm1004dcpCtrllineTunableChannelTable_Object = MibTable
pm1004dcpCtrllineTunableChannelTable = _Pm1004dcpCtrllineTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllineTunableChannelTable.setStatus("current")
_Pm1004dcpCtrllineTunableChannelEntry_Object = MibTableRow
pm1004dcpCtrllineTunableChannelEntry = _Pm1004dcpCtrllineTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 212, 1)
)
pm1004dcpCtrllineTunableChannelEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrllineTunableChannelIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllineTunableChannelEntry.setStatus("current")


class _Pm1004dcpCtrllineTunableChannelIndex_Type(Integer32):
    """Custom type pm1004dcpCtrllineTunableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrllineTunableChannelIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrllineTunableChannelIndex_Object = MibTableColumn
pm1004dcpCtrllineTunableChannelIndex = _Pm1004dcpCtrllineTunableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 212, 1, 1),
    _Pm1004dcpCtrllineTunableChannelIndex_Type()
)
pm1004dcpCtrllineTunableChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrllineTunableChannelIndex.setStatus("current")
_Pm1004dcpCtrllineTunableChannelPortn_Type = Pm1004dcpOtxChannel
_Pm1004dcpCtrllineTunableChannelPortn_Object = MibTableColumn
pm1004dcpCtrllineTunableChannelPortn = _Pm1004dcpCtrllineTunableChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 212, 1, 2),
    _Pm1004dcpCtrllineTunableChannelPortn_Type()
)
pm1004dcpCtrllineTunableChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrllineTunableChannelPortn.setStatus("current")
_Pm1004dcpCtrllinePhotodiodeModeTable_Object = MibTable
pm1004dcpCtrllinePhotodiodeModeTable = _Pm1004dcpCtrllinePhotodiodeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 213)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePhotodiodeModeTable.setStatus("current")
_Pm1004dcpCtrllinePhotodiodeModeEntry_Object = MibTableRow
pm1004dcpCtrllinePhotodiodeModeEntry = _Pm1004dcpCtrllinePhotodiodeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 213, 1)
)
pm1004dcpCtrllinePhotodiodeModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrllinePhotodiodeModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePhotodiodeModeEntry.setStatus("current")


class _Pm1004dcpCtrllinePhotodiodeModeIndex_Type(Integer32):
    """Custom type pm1004dcpCtrllinePhotodiodeModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrllinePhotodiodeModeIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrllinePhotodiodeModeIndex_Object = MibTableColumn
pm1004dcpCtrllinePhotodiodeModeIndex = _Pm1004dcpCtrllinePhotodiodeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 213, 1, 1),
    _Pm1004dcpCtrllinePhotodiodeModeIndex_Type()
)
pm1004dcpCtrllinePhotodiodeModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePhotodiodeModeIndex.setStatus("current")
_Pm1004dcpCtrllinePhotodiodeModePortn_Type = Pm1004dcpOtxMode
_Pm1004dcpCtrllinePhotodiodeModePortn_Object = MibTableColumn
pm1004dcpCtrllinePhotodiodeModePortn = _Pm1004dcpCtrllinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 213, 1, 2),
    _Pm1004dcpCtrllinePhotodiodeModePortn_Type()
)
pm1004dcpCtrllinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePhotodiodeModePortn.setStatus("current")
_Pm1004dcpCtrllinePhotodiodeValueTable_Object = MibTable
pm1004dcpCtrllinePhotodiodeValueTable = _Pm1004dcpCtrllinePhotodiodeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 214)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePhotodiodeValueTable.setStatus("current")
_Pm1004dcpCtrllinePhotodiodeValueEntry_Object = MibTableRow
pm1004dcpCtrllinePhotodiodeValueEntry = _Pm1004dcpCtrllinePhotodiodeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 214, 1)
)
pm1004dcpCtrllinePhotodiodeValueEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrllinePhotodiodeValueIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePhotodiodeValueEntry.setStatus("current")


class _Pm1004dcpCtrllinePhotodiodeValueIndex_Type(Integer32):
    """Custom type pm1004dcpCtrllinePhotodiodeValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrllinePhotodiodeValueIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrllinePhotodiodeValueIndex_Object = MibTableColumn
pm1004dcpCtrllinePhotodiodeValueIndex = _Pm1004dcpCtrllinePhotodiodeValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 214, 1, 1),
    _Pm1004dcpCtrllinePhotodiodeValueIndex_Type()
)
pm1004dcpCtrllinePhotodiodeValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePhotodiodeValueIndex.setStatus("current")
_Pm1004dcpCtrllinePhotodiodeValuePortn_Type = Pm1004dcpAdjustValue
_Pm1004dcpCtrllinePhotodiodeValuePortn_Object = MibTableColumn
pm1004dcpCtrllinePhotodiodeValuePortn = _Pm1004dcpCtrllinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 214, 1, 2),
    _Pm1004dcpCtrllinePhotodiodeValuePortn_Type()
)
pm1004dcpCtrllinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePhotodiodeValuePortn.setStatus("current")
_Pm1004dcpCtrllinePowerLaserTable_Object = MibTable
pm1004dcpCtrllinePowerLaserTable = _Pm1004dcpCtrllinePowerLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 215)
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePowerLaserTable.setStatus("current")
_Pm1004dcpCtrllinePowerLaserEntry_Object = MibTableRow
pm1004dcpCtrllinePowerLaserEntry = _Pm1004dcpCtrllinePowerLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 215, 1)
)
pm1004dcpCtrllinePowerLaserEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCtrllinePowerLaserIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePowerLaserEntry.setStatus("current")


class _Pm1004dcpCtrllinePowerLaserIndex_Type(Integer32):
    """Custom type pm1004dcpCtrllinePowerLaserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCtrllinePowerLaserIndex_Type.__name__ = "Integer32"
_Pm1004dcpCtrllinePowerLaserIndex_Object = MibTableColumn
pm1004dcpCtrllinePowerLaserIndex = _Pm1004dcpCtrllinePowerLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 215, 1, 1),
    _Pm1004dcpCtrllinePowerLaserIndex_Type()
)
pm1004dcpCtrllinePowerLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePowerLaserIndex.setStatus("current")


class _Pm1004dcpCtrllinePowerLaserPortn_Type(Integer32):
    """Custom type pm1004dcpCtrllinePowerLaserPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1004dcpCtrllinePowerLaserPortn_Type.__name__ = "Integer32"
_Pm1004dcpCtrllinePowerLaserPortn_Object = MibTableColumn
pm1004dcpCtrllinePowerLaserPortn = _Pm1004dcpCtrllinePowerLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 6, 3, 215, 1, 2),
    _Pm1004dcpCtrllinePowerLaserPortn_Type()
)
pm1004dcpCtrllinePowerLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCtrllinePowerLaserPortn.setStatus("current")
_Pm1004dcpri_ObjectIdentity = ObjectIdentity
pm1004dcpri = _Pm1004dcpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7)
)
_Pm1004dcpriTable_ObjectIdentity = ObjectIdentity
pm1004dcpriTable = _Pm1004dcpriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 1)
)
_Pm1004dcpRinvSfpTable_Object = MibTable
pm1004dcpRinvSfpTable = _Pm1004dcpRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004dcpRinvSfpTable.setStatus("current")
_Pm1004dcpRinvSfpEntry_Object = MibTableRow
pm1004dcpRinvSfpEntry = _Pm1004dcpRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 1, 1, 1)
)
pm1004dcpRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpRinvSfpEntry.setStatus("current")


class _Pm1004dcpRinvSfpIndex_Type(Integer32):
    """Custom type pm1004dcpRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004dcpRinvSfpIndex_Type.__name__ = "Integer32"
_Pm1004dcpRinvSfpIndex_Object = MibTableColumn
pm1004dcpRinvSfpIndex = _Pm1004dcpRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 1, 1, 1, 1),
    _Pm1004dcpRinvSfpIndex_Type()
)
pm1004dcpRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpRinvSfpIndex.setStatus("current")
_Pm1004dcpRinvsfp_Type = DisplayString
_Pm1004dcpRinvsfp_Object = MibTableColumn
pm1004dcpRinvsfp = _Pm1004dcpRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 1, 1, 1, 2),
    _Pm1004dcpRinvsfp_Type()
)
pm1004dcpRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpRinvsfp.setStatus("current")
_Pm1004dcpRinvLineTable_Object = MibTable
pm1004dcpRinvLineTable = _Pm1004dcpRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm1004dcpRinvLineTable.setStatus("current")
_Pm1004dcpRinvLineEntry_Object = MibTableRow
pm1004dcpRinvLineEntry = _Pm1004dcpRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 1, 2, 1)
)
pm1004dcpRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpRinvLineEntry.setStatus("current")


class _Pm1004dcpRinvLineIndex_Type(Integer32):
    """Custom type pm1004dcpRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004dcpRinvLineIndex_Type.__name__ = "Integer32"
_Pm1004dcpRinvLineIndex_Object = MibTableColumn
pm1004dcpRinvLineIndex = _Pm1004dcpRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 1, 2, 1, 1),
    _Pm1004dcpRinvLineIndex_Type()
)
pm1004dcpRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpRinvLineIndex.setStatus("current")
_Pm1004dcpRinvxfpLine_Type = DisplayString
_Pm1004dcpRinvxfpLine_Object = MibTableColumn
pm1004dcpRinvxfpLine = _Pm1004dcpRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 1, 2, 1, 2),
    _Pm1004dcpRinvxfpLine_Type()
)
pm1004dcpRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpRinvxfpLine.setStatus("current")
_Pm1004dcpRinvReloadInventory_Type = EkiOnOff
_Pm1004dcpRinvReloadInventory_Object = MibScalar
pm1004dcpRinvReloadInventory = _Pm1004dcpRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 2),
    _Pm1004dcpRinvReloadInventory_Type()
)
pm1004dcpRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpRinvReloadInventory.setStatus("current")
_Pm1004dcpRinvHwPlatform_Type = DisplayString
_Pm1004dcpRinvHwPlatform_Object = MibScalar
pm1004dcpRinvHwPlatform = _Pm1004dcpRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 3),
    _Pm1004dcpRinvHwPlatform_Type()
)
pm1004dcpRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpRinvHwPlatform.setStatus("current")
_Pm1004dcpRinvModulePlatform_Type = DisplayString
_Pm1004dcpRinvModulePlatform_Object = MibScalar
pm1004dcpRinvModulePlatform = _Pm1004dcpRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 4),
    _Pm1004dcpRinvModulePlatform_Type()
)
pm1004dcpRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpRinvModulePlatform.setStatus("current")
_Pm1004dcpRinvSwPlatform_Type = DisplayString
_Pm1004dcpRinvSwPlatform_Object = MibScalar
pm1004dcpRinvSwPlatform = _Pm1004dcpRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 5),
    _Pm1004dcpRinvSwPlatform_Type()
)
pm1004dcpRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpRinvSwPlatform.setStatus("current")
_Pm1004dcpRinvGwPlatform_Type = DisplayString
_Pm1004dcpRinvGwPlatform_Object = MibScalar
pm1004dcpRinvGwPlatform = _Pm1004dcpRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 7, 6),
    _Pm1004dcpRinvGwPlatform_Type()
)
pm1004dcpRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpRinvGwPlatform.setStatus("current")
_Pm1004dcpdownload_ObjectIdentity = ObjectIdentity
pm1004dcpdownload = _Pm1004dcpdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8)
)
_Pm1004dcpDwlOther_ObjectIdentity = ObjectIdentity
pm1004dcpDwlOther = _Pm1004dcpDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1)
)
_Pm1004dcpDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm1004dcpDwlrestartProcess = _Pm1004dcpDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 0)
)
_Pm1004dcpDwlWarmRestartProcessed_Type = EkiOnOff
_Pm1004dcpDwlWarmRestartProcessed_Object = MibScalar
pm1004dcpDwlWarmRestartProcessed = _Pm1004dcpDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 0, 1),
    _Pm1004dcpDwlWarmRestartProcessed_Type()
)
pm1004dcpDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlWarmRestartProcessed.setStatus("current")
_Pm1004dcpDwlColdRestartProcessed_Type = EkiOnOff
_Pm1004dcpDwlColdRestartProcessed_Object = MibScalar
pm1004dcpDwlColdRestartProcessed = _Pm1004dcpDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 0, 2),
    _Pm1004dcpDwlColdRestartProcessed_Type()
)
pm1004dcpDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlColdRestartProcessed.setStatus("current")
_Pm1004dcpDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm1004dcpDwlswBanksUsed = _Pm1004dcpDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 1)
)
_Pm1004dcpDwlSwBank1Used_Type = EkiOnOff
_Pm1004dcpDwlSwBank1Used_Object = MibScalar
pm1004dcpDwlSwBank1Used = _Pm1004dcpDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 1, 1),
    _Pm1004dcpDwlSwBank1Used_Type()
)
pm1004dcpDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlSwBank1Used.setStatus("current")
_Pm1004dcpDwlSwBank2Used_Type = EkiOnOff
_Pm1004dcpDwlSwBank2Used_Object = MibScalar
pm1004dcpDwlSwBank2Used = _Pm1004dcpDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 1, 2),
    _Pm1004dcpDwlSwBank2Used_Type()
)
pm1004dcpDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlSwBank2Used.setStatus("current")
_Pm1004dcpDwlSwBank1Notempty_Type = EkiOnOff
_Pm1004dcpDwlSwBank1Notempty_Object = MibScalar
pm1004dcpDwlSwBank1Notempty = _Pm1004dcpDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 1, 5),
    _Pm1004dcpDwlSwBank1Notempty_Type()
)
pm1004dcpDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlSwBank1Notempty.setStatus("current")
_Pm1004dcpDwlSwBank2Notempty_Type = EkiOnOff
_Pm1004dcpDwlSwBank2Notempty_Object = MibScalar
pm1004dcpDwlSwBank2Notempty = _Pm1004dcpDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 1, 6),
    _Pm1004dcpDwlSwBank2Notempty_Type()
)
pm1004dcpDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlSwBank2Notempty.setStatus("current")
_Pm1004dcpDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm1004dcpDwlgwBanksUsed = _Pm1004dcpDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 2)
)
_Pm1004dcpDwlGwBank1Used_Type = EkiOnOff
_Pm1004dcpDwlGwBank1Used_Object = MibScalar
pm1004dcpDwlGwBank1Used = _Pm1004dcpDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 2, 1),
    _Pm1004dcpDwlGwBank1Used_Type()
)
pm1004dcpDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlGwBank1Used.setStatus("current")
_Pm1004dcpDwlGwBank2Used_Type = EkiOnOff
_Pm1004dcpDwlGwBank2Used_Object = MibScalar
pm1004dcpDwlGwBank2Used = _Pm1004dcpDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 2, 2),
    _Pm1004dcpDwlGwBank2Used_Type()
)
pm1004dcpDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlGwBank2Used.setStatus("current")
_Pm1004dcpDwlGwBank3Used_Type = EkiOnOff
_Pm1004dcpDwlGwBank3Used_Object = MibScalar
pm1004dcpDwlGwBank3Used = _Pm1004dcpDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 2, 3),
    _Pm1004dcpDwlGwBank3Used_Type()
)
pm1004dcpDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlGwBank3Used.setStatus("current")
_Pm1004dcpDwlGwBank4Used_Type = EkiOnOff
_Pm1004dcpDwlGwBank4Used_Object = MibScalar
pm1004dcpDwlGwBank4Used = _Pm1004dcpDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 2, 4),
    _Pm1004dcpDwlGwBank4Used_Type()
)
pm1004dcpDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlGwBank4Used.setStatus("current")
_Pm1004dcpDwlGwBank1Notempty_Type = EkiOnOff
_Pm1004dcpDwlGwBank1Notempty_Object = MibScalar
pm1004dcpDwlGwBank1Notempty = _Pm1004dcpDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 2, 5),
    _Pm1004dcpDwlGwBank1Notempty_Type()
)
pm1004dcpDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlGwBank1Notempty.setStatus("current")
_Pm1004dcpDwlGwBank2Notempty_Type = EkiOnOff
_Pm1004dcpDwlGwBank2Notempty_Object = MibScalar
pm1004dcpDwlGwBank2Notempty = _Pm1004dcpDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 2, 6),
    _Pm1004dcpDwlGwBank2Notempty_Type()
)
pm1004dcpDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlGwBank2Notempty.setStatus("current")
_Pm1004dcpDwlGwBank3Notempty_Type = EkiOnOff
_Pm1004dcpDwlGwBank3Notempty_Object = MibScalar
pm1004dcpDwlGwBank3Notempty = _Pm1004dcpDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 2, 7),
    _Pm1004dcpDwlGwBank3Notempty_Type()
)
pm1004dcpDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlGwBank3Notempty.setStatus("current")
_Pm1004dcpDwlGwBank4Notempty_Type = EkiOnOff
_Pm1004dcpDwlGwBank4Notempty_Object = MibScalar
pm1004dcpDwlGwBank4Notempty = _Pm1004dcpDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 1, 2, 8),
    _Pm1004dcpDwlGwBank4Notempty_Type()
)
pm1004dcpDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpDwlGwBank4Notempty.setStatus("current")
_Pm1004dcpDwlClient_ObjectIdentity = ObjectIdentity
pm1004dcpDwlClient = _Pm1004dcpDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 2)
)
_Pm1004dcpDwlLine_ObjectIdentity = ObjectIdentity
pm1004dcpDwlLine = _Pm1004dcpDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 8, 3)
)
_Pm1004dcpConfig_ObjectIdentity = ObjectIdentity
pm1004dcpConfig = _Pm1004dcpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9)
)
_Pm1004dcpCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm1004dcpCfgAccessCAisCsf = _Pm1004dcpCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1)
)
_Pm1004dcpCfgClientcaiscsfTable_Object = MibTable
pm1004dcpCfgClientcaiscsfTable = _Pm1004dcpCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004dcpCfgClientcaiscsfTable.setStatus("current")
_Pm1004dcpCfgClientcaiscsfEntry_Object = MibTableRow
pm1004dcpCfgClientcaiscsfEntry = _Pm1004dcpCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1)
)
pm1004dcpCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCfgClientcaiscsfEntry.setStatus("current")


class _Pm1004dcpCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm1004dcpCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm1004dcpCfgClientcaiscsfIndex_Object = MibTableColumn
pm1004dcpCfgClientcaiscsfIndex = _Pm1004dcpCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 1),
    _Pm1004dcpCfgClientcaiscsfIndex_Type()
)
pm1004dcpCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCfgClientcaiscsfIndex.setStatus("current")


class _Pm1004dcpCfgCAisModePortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgCAisModePortn_Object = MibTableColumn
pm1004dcpCfgCAisModePortn = _Pm1004dcpCfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 3),
    _Pm1004dcpCfgCAisModePortn_Type()
)
pm1004dcpCfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgCAisModePortn.setStatus("current")


class _Pm1004dcpCfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgUpAccessioAlmPortn_Object = MibTableColumn
pm1004dcpCfgUpAccessioAlmPortn = _Pm1004dcpCfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 9),
    _Pm1004dcpCfgUpAccessioAlmPortn_Type()
)
pm1004dcpCfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgUpAccessioAlmPortn.setStatus("current")


class _Pm1004dcpCfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgUpMapperDeAlmPortn_Object = MibTableColumn
pm1004dcpCfgUpMapperDeAlmPortn = _Pm1004dcpCfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 10),
    _Pm1004dcpCfgUpMapperDeAlmPortn_Type()
)
pm1004dcpCfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgUpMapperDeAlmPortn.setStatus("current")


class _Pm1004dcpCfgUpAccessioSdhAlmPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgUpAccessioSdhAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgUpAccessioSdhAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgUpAccessioSdhAlmPortn_Object = MibTableColumn
pm1004dcpCfgUpAccessioSdhAlmPortn = _Pm1004dcpCfgUpAccessioSdhAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 11),
    _Pm1004dcpCfgUpAccessioSdhAlmPortn_Type()
)
pm1004dcpCfgUpAccessioSdhAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgUpAccessioSdhAlmPortn.setStatus("current")


class _Pm1004dcpCfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgDownAccessioAlmPortn_Object = MibTableColumn
pm1004dcpCfgDownAccessioAlmPortn = _Pm1004dcpCfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 17),
    _Pm1004dcpCfgDownAccessioAlmPortn_Type()
)
pm1004dcpCfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgDownAccessioAlmPortn.setStatus("current")


class _Pm1004dcpCfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgDownMapperDeAlmPortn_Object = MibTableColumn
pm1004dcpCfgDownMapperDeAlmPortn = _Pm1004dcpCfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 18),
    _Pm1004dcpCfgDownMapperDeAlmPortn_Type()
)
pm1004dcpCfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgDownMapperDeAlmPortn.setStatus("current")


class _Pm1004dcpCfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgDownDfrmAlmPortn_Object = MibTableColumn
pm1004dcpCfgDownDfrmAlmPortn = _Pm1004dcpCfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 19),
    _Pm1004dcpCfgDownDfrmAlmPortn_Type()
)
pm1004dcpCfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgDownDfrmAlmPortn.setStatus("current")


class _Pm1004dcpCfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pm1004dcpCfgDownLineSyncAlarmsPortn = _Pm1004dcpCfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 20),
    _Pm1004dcpCfgDownLineSyncAlarmsPortn_Type()
)
pm1004dcpCfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgDownLineSyncAlarmsPortn.setStatus("deprecated")


class _Pm1004dcpCfgDownAccessioSdhAlmPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgDownAccessioSdhAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgDownAccessioSdhAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgDownAccessioSdhAlmPortn_Object = MibTableColumn
pm1004dcpCfgDownAccessioSdhAlmPortn = _Pm1004dcpCfgDownAccessioSdhAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 1, 1, 1, 21),
    _Pm1004dcpCfgDownAccessioSdhAlmPortn_Type()
)
pm1004dcpCfgDownAccessioSdhAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgDownAccessioSdhAlmPortn.setStatus("current")
_Pm1004dcpCfgStartup_ObjectIdentity = ObjectIdentity
pm1004dcpCfgStartup = _Pm1004dcpCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2)
)
_Pm1004dcpCfgClientStartupTable_Object = MibTable
pm1004dcpCfgClientStartupTable = _Pm1004dcpCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm1004dcpCfgClientStartupTable.setStatus("current")
_Pm1004dcpCfgClientStartupEntry_Object = MibTableRow
pm1004dcpCfgClientStartupEntry = _Pm1004dcpCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 1, 1)
)
pm1004dcpCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCfgClientStartupEntry.setStatus("current")


class _Pm1004dcpCfgClientStartupIndex_Type(Integer32):
    """Custom type pm1004dcpCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm1004dcpCfgClientStartupIndex_Object = MibTableColumn
pm1004dcpCfgClientStartupIndex = _Pm1004dcpCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 1, 1, 1),
    _Pm1004dcpCfgClientStartupIndex_Type()
)
pm1004dcpCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCfgClientStartupIndex.setStatus("current")


class _Pm1004dcpCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgSystConfPortPortn_Object = MibTableColumn
pm1004dcpCfgSystConfPortPortn = _Pm1004dcpCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 1, 1, 3),
    _Pm1004dcpCfgSystConfPortPortn_Type()
)
pm1004dcpCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgSystConfPortPortn.setStatus("current")


class _Pm1004dcpCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgNetConfPortPortn_Object = MibTableColumn
pm1004dcpCfgNetConfPortPortn = _Pm1004dcpCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 1, 1, 4),
    _Pm1004dcpCfgNetConfPortPortn_Type()
)
pm1004dcpCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgNetConfPortPortn.setStatus("current")


class _Pm1004dcpCfgAdddropConfPortPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgAdddropConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgAdddropConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgAdddropConfPortPortn_Object = MibTableColumn
pm1004dcpCfgAdddropConfPortPortn = _Pm1004dcpCfgAdddropConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 1, 1, 5),
    _Pm1004dcpCfgAdddropConfPortPortn_Type()
)
pm1004dcpCfgAdddropConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgAdddropConfPortPortn.setStatus("deprecated")
_Pm1004dcptablelineStartup_ObjectIdentity = ObjectIdentity
pm1004dcptablelineStartup = _Pm1004dcptablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 2)
)


class _Pm1004dcpCfgsystConfLine1_Type(Unsigned32):
    """Custom type pm1004dcpCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgsystConfLine1_Object = MibScalar
pm1004dcpCfgsystConfLine1 = _Pm1004dcpCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 2, 2),
    _Pm1004dcpCfgsystConfLine1_Type()
)
pm1004dcpCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgsystConfLine1.setStatus("current")


class _Pm1004dcpCfglineOptions1_Type(Unsigned32):
    """Custom type pm1004dcpCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfglineOptions1_Type.__name__ = "Unsigned32"
_Pm1004dcpCfglineOptions1_Object = MibScalar
pm1004dcpCfglineOptions1 = _Pm1004dcpCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 2, 5),
    _Pm1004dcpCfglineOptions1_Type()
)
pm1004dcpCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfglineOptions1.setStatus("current")


class _Pm1004dcpCfgsystConfLine2_Type(Unsigned32):
    """Custom type pm1004dcpCfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgsystConfLine2_Object = MibScalar
pm1004dcpCfgsystConfLine2 = _Pm1004dcpCfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 2, 6),
    _Pm1004dcpCfgsystConfLine2_Type()
)
pm1004dcpCfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgsystConfLine2.setStatus("current")


class _Pm1004dcpCfglineSelection_Type(Unsigned32):
    """Custom type pm1004dcpCfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfglineSelection_Type.__name__ = "Unsigned32"
_Pm1004dcpCfglineSelection_Object = MibScalar
pm1004dcpCfglineSelection = _Pm1004dcpCfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 2, 7),
    _Pm1004dcpCfglineSelection_Type()
)
pm1004dcpCfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfglineSelection.setStatus("current")


class _Pm1004dcpCfglineOptions2_Type(Unsigned32):
    """Custom type pm1004dcpCfglineOptions2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfglineOptions2_Type.__name__ = "Unsigned32"
_Pm1004dcpCfglineOptions2_Object = MibScalar
pm1004dcpCfglineOptions2 = _Pm1004dcpCfglineOptions2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 2, 9),
    _Pm1004dcpCfglineOptions2_Type()
)
pm1004dcpCfglineOptions2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfglineOptions2.setStatus("deprecated")
_Pm1004dcpCfgXfpTable_Object = MibTable
pm1004dcpCfgXfpTable = _Pm1004dcpCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm1004dcpCfgXfpTable.setStatus("current")
_Pm1004dcpCfgXfpEntry_Object = MibTableRow
pm1004dcpCfgXfpEntry = _Pm1004dcpCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 3, 1)
)
pm1004dcpCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCfgXfpEntry.setStatus("current")


class _Pm1004dcpCfgXfpIndex_Type(Integer32):
    """Custom type pm1004dcpCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCfgXfpIndex_Type.__name__ = "Integer32"
_Pm1004dcpCfgXfpIndex_Object = MibTableColumn
pm1004dcpCfgXfpIndex = _Pm1004dcpCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 3, 1, 1),
    _Pm1004dcpCfgXfpIndex_Type()
)
pm1004dcpCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCfgXfpIndex.setStatus("current")


class _Pm1004dcpCfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgSystConfXfpPortn_Object = MibTableColumn
pm1004dcpCfgSystConfXfpPortn = _Pm1004dcpCfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 3, 1, 3),
    _Pm1004dcpCfgSystConfXfpPortn_Type()
)
pm1004dcpCfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgSystConfXfpPortn.setStatus("current")


class _Pm1004dcpCfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgDataRateConfXfpPortn_Object = MibTableColumn
pm1004dcpCfgDataRateConfXfpPortn = _Pm1004dcpCfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 2, 3, 1, 4),
    _Pm1004dcpCfgDataRateConfXfpPortn_Type()
)
pm1004dcpCfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgDataRateConfXfpPortn.setStatus("deprecated")
_Pm1004dcpCfgModPerfConfig_ObjectIdentity = ObjectIdentity
pm1004dcpCfgModPerfConfig = _Pm1004dcpCfgModPerfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 3)
)
_Pm1004dcptablemodPerfConfig_ObjectIdentity = ObjectIdentity
pm1004dcptablemodPerfConfig = _Pm1004dcptablemodPerfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 3, 1)
)


class _Pm1004dcpCfgperfMode_Type(Unsigned32):
    """Custom type pm1004dcpCfgperfMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgperfMode_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgperfMode_Object = MibScalar
pm1004dcpCfgperfMode = _Pm1004dcpCfgperfMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 3, 1, 2),
    _Pm1004dcpCfgperfMode_Type()
)
pm1004dcpCfgperfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgperfMode.setStatus("current")
_Pm1004dcpCfgJ0Client_ObjectIdentity = ObjectIdentity
pm1004dcpCfgJ0Client = _Pm1004dcpCfgJ0Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 4)
)
_Pm1004dcpCfgEmptyTable_Object = MibTable
pm1004dcpCfgEmptyTable = _Pm1004dcpCfgEmptyTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm1004dcpCfgEmptyTable.setStatus("current")
_Pm1004dcpCfgEmptyEntry_Object = MibTableRow
pm1004dcpCfgEmptyEntry = _Pm1004dcpCfgEmptyEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 4, 1, 1)
)
pm1004dcpCfgEmptyEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCfgEmptyIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCfgEmptyEntry.setStatus("current")


class _Pm1004dcpCfgEmptyIndex_Type(Integer32):
    """Custom type pm1004dcpCfgEmptyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCfgEmptyIndex_Type.__name__ = "Integer32"
_Pm1004dcpCfgEmptyIndex_Object = MibTableColumn
pm1004dcpCfgEmptyIndex = _Pm1004dcpCfgEmptyIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 4, 1, 1, 1),
    _Pm1004dcpCfgEmptyIndex_Type()
)
pm1004dcpCfgEmptyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCfgEmptyIndex.setStatus("current")


class _Pm1004dcpCfgClientExpectJ0SetupPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgClientExpectJ0SetupPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgClientExpectJ0SetupPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgClientExpectJ0SetupPortn_Object = MibTableColumn
pm1004dcpCfgClientExpectJ0SetupPortn = _Pm1004dcpCfgClientExpectJ0SetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 4, 1, 1, 3),
    _Pm1004dcpCfgClientExpectJ0SetupPortn_Type()
)
pm1004dcpCfgClientExpectJ0SetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgClientExpectJ0SetupPortn.setStatus("current")
_Pm1004dcpCfgLabels_ObjectIdentity = ObjectIdentity
pm1004dcpCfgLabels = _Pm1004dcpCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 5)
)
_Pm1004dcpCfgLabelclientTable_Object = MibTable
pm1004dcpCfgLabelclientTable = _Pm1004dcpCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pm1004dcpCfgLabelclientTable.setStatus("current")
_Pm1004dcpCfgLabelclientEntry_Object = MibTableRow
pm1004dcpCfgLabelclientEntry = _Pm1004dcpCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 5, 1, 1)
)
pm1004dcpCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCfgLabelclientEntry.setStatus("current")


class _Pm1004dcpCfgLabelclientIndex_Type(Integer32):
    """Custom type pm1004dcpCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1004dcpCfgLabelclientIndex_Object = MibTableColumn
pm1004dcpCfgLabelclientIndex = _Pm1004dcpCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 5, 1, 1, 1),
    _Pm1004dcpCfgLabelclientIndex_Type()
)
pm1004dcpCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCfgLabelclientIndex.setStatus("current")


class _Pm1004dcpCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1004dcpCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004dcpCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1004dcpCfgLabelclientPortn_Object = MibTableColumn
pm1004dcpCfgLabelclientPortn = _Pm1004dcpCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 5, 1, 1, 3),
    _Pm1004dcpCfgLabelclientPortn_Type()
)
pm1004dcpCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLabelclientPortn.setStatus("current")
_Pm1004dcpCfgLabellineTable_Object = MibTable
pm1004dcpCfgLabellineTable = _Pm1004dcpCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 5, 2)
)
if mibBuilder.loadTexts:
    pm1004dcpCfgLabellineTable.setStatus("current")
_Pm1004dcpCfgLabellineEntry_Object = MibTableRow
pm1004dcpCfgLabellineEntry = _Pm1004dcpCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 5, 2, 1)
)
pm1004dcpCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCfgLabellineEntry.setStatus("current")


class _Pm1004dcpCfgLabellineIndex_Type(Integer32):
    """Custom type pm1004dcpCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1004dcpCfgLabellineIndex_Object = MibTableColumn
pm1004dcpCfgLabellineIndex = _Pm1004dcpCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 5, 2, 1, 1),
    _Pm1004dcpCfgLabellineIndex_Type()
)
pm1004dcpCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCfgLabellineIndex.setStatus("current")


class _Pm1004dcpCfgLabellinePortn_Type(DisplayString):
    """Custom type pm1004dcpCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004dcpCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1004dcpCfgLabellinePortn_Object = MibTableColumn
pm1004dcpCfgLabellinePortn = _Pm1004dcpCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 5, 2, 1, 3),
    _Pm1004dcpCfgLabellinePortn_Type()
)
pm1004dcpCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLabellinePortn.setStatus("current")
_Pm1004dcpCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm1004dcpCfgStartuptlh = _Pm1004dcpCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6)
)
_Pm1004dcpCfgOtxtlhTable_Object = MibTable
pm1004dcpCfgOtxtlhTable = _Pm1004dcpCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm1004dcpCfgOtxtlhTable.setStatus("current")
_Pm1004dcpCfgOtxtlhEntry_Object = MibTableRow
pm1004dcpCfgOtxtlhEntry = _Pm1004dcpCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1)
)
pm1004dcpCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCfgOtxtlhEntry.setStatus("current")


class _Pm1004dcpCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm1004dcpCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm1004dcpCfgOtxtlhIndex_Object = MibTableColumn
pm1004dcpCfgOtxtlhIndex = _Pm1004dcpCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 1),
    _Pm1004dcpCfgOtxtlhIndex_Type()
)
pm1004dcpCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCfgOtxtlhIndex.setStatus("current")


class _Pm1004dcpCfgNuPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgNuPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgNuPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgNuPortn_Object = MibTableColumn
pm1004dcpCfgNuPortn = _Pm1004dcpCfgNuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 3),
    _Pm1004dcpCfgNuPortn_Type()
)
pm1004dcpCfgNuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgNuPortn.setStatus("deprecated")


class _Pm1004dcpCfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgLineDitherRatePortn_Object = MibTableColumn
pm1004dcpCfgLineDitherRatePortn = _Pm1004dcpCfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 4),
    _Pm1004dcpCfgLineDitherRatePortn_Type()
)
pm1004dcpCfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLineDitherRatePortn.setStatus("current")


class _Pm1004dcpCfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgLineDitherFhzPortn_Object = MibTableColumn
pm1004dcpCfgLineDitherFhzPortn = _Pm1004dcpCfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 5),
    _Pm1004dcpCfgLineDitherFhzPortn_Type()
)
pm1004dcpCfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLineDitherFhzPortn.setStatus("current")


class _Pm1004dcpCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgLinePwrLaserPortn_Object = MibTableColumn
pm1004dcpCfgLinePwrLaserPortn = _Pm1004dcpCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 6),
    _Pm1004dcpCfgLinePwrLaserPortn_Type()
)
pm1004dcpCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLinePwrLaserPortn.setStatus("current")


class _Pm1004dcpCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgLineFCurrentPortn_Object = MibTableColumn
pm1004dcpCfgLineFCurrentPortn = _Pm1004dcpCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 7),
    _Pm1004dcpCfgLineFCurrentPortn_Type()
)
pm1004dcpCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLineFCurrentPortn.setStatus("current")


class _Pm1004dcpCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgLineGridCurrentPortn_Object = MibTableColumn
pm1004dcpCfgLineGridCurrentPortn = _Pm1004dcpCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 8),
    _Pm1004dcpCfgLineGridCurrentPortn_Type()
)
pm1004dcpCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLineGridCurrentPortn.setStatus("current")


class _Pm1004dcpCfgFPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgFPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgFPortn_Object = MibTableColumn
pm1004dcpCfgFPortn = _Pm1004dcpCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 9),
    _Pm1004dcpCfgFPortn_Type()
)
pm1004dcpCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgFPortn.setStatus("current")


class _Pm1004dcpCfgReservedPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgReservedPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgReservedPortn_Object = MibTableColumn
pm1004dcpCfgReservedPortn = _Pm1004dcpCfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 10),
    _Pm1004dcpCfgReservedPortn_Type()
)
pm1004dcpCfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgReservedPortn.setStatus("deprecated")


class _Pm1004dcpCfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgLinePhotodiodeModePortn_Object = MibTableColumn
pm1004dcpCfgLinePhotodiodeModePortn = _Pm1004dcpCfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 11),
    _Pm1004dcpCfgLinePhotodiodeModePortn_Type()
)
pm1004dcpCfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLinePhotodiodeModePortn.setStatus("current")


class _Pm1004dcpCfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgLinePhotodiodeValuePortn_Object = MibTableColumn
pm1004dcpCfgLinePhotodiodeValuePortn = _Pm1004dcpCfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 6, 1, 1, 12),
    _Pm1004dcpCfgLinePhotodiodeValuePortn_Type()
)
pm1004dcpCfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLinePhotodiodeValuePortn.setStatus("current")
_Pm1004dcpCfgOther_ObjectIdentity = ObjectIdentity
pm1004dcpCfgOther = _Pm1004dcpCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 7)
)
_Pm1004dcptablemoduleOther_ObjectIdentity = ObjectIdentity
pm1004dcptablemoduleOther = _Pm1004dcptablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 7, 1)
)


class _Pm1004dcpCfgmode_Type(Unsigned32):
    """Custom type pm1004dcpCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgmode_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgmode_Object = MibScalar
pm1004dcpCfgmode = _Pm1004dcpCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 7, 1, 2),
    _Pm1004dcpCfgmode_Type()
)
pm1004dcpCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgmode.setStatus("current")


class _Pm1004dcpCfgadddropTsPairMode1_Type(Unsigned32):
    """Custom type pm1004dcpCfgadddropTsPairMode1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgadddropTsPairMode1_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgadddropTsPairMode1_Object = MibScalar
pm1004dcpCfgadddropTsPairMode1 = _Pm1004dcpCfgadddropTsPairMode1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 7, 1, 3),
    _Pm1004dcpCfgadddropTsPairMode1_Type()
)
pm1004dcpCfgadddropTsPairMode1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgadddropTsPairMode1.setStatus("current")


class _Pm1004dcpCfgadddropTsPairMode2_Type(Unsigned32):
    """Custom type pm1004dcpCfgadddropTsPairMode2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgadddropTsPairMode2_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgadddropTsPairMode2_Object = MibScalar
pm1004dcpCfgadddropTsPairMode2 = _Pm1004dcpCfgadddropTsPairMode2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 7, 1, 4),
    _Pm1004dcpCfgadddropTsPairMode2_Type()
)
pm1004dcpCfgadddropTsPairMode2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgadddropTsPairMode2.setStatus("current")


class _Pm1004dcpCfgadddropTsPairMode3_Type(Unsigned32):
    """Custom type pm1004dcpCfgadddropTsPairMode3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgadddropTsPairMode3_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgadddropTsPairMode3_Object = MibScalar
pm1004dcpCfgadddropTsPairMode3 = _Pm1004dcpCfgadddropTsPairMode3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 7, 1, 5),
    _Pm1004dcpCfgadddropTsPairMode3_Type()
)
pm1004dcpCfgadddropTsPairMode3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgadddropTsPairMode3.setStatus("current")


class _Pm1004dcpCfgadddropTsPairMode4_Type(Unsigned32):
    """Custom type pm1004dcpCfgadddropTsPairMode4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgadddropTsPairMode4_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgadddropTsPairMode4_Object = MibScalar
pm1004dcpCfgadddropTsPairMode4 = _Pm1004dcpCfgadddropTsPairMode4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 7, 1, 6),
    _Pm1004dcpCfgadddropTsPairMode4_Type()
)
pm1004dcpCfgadddropTsPairMode4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgadddropTsPairMode4.setStatus("current")
_Pm1004dcpCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm1004dcpCfgStartuptablefive = _Pm1004dcpCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 8)
)
_Pm1004dcpCfgOtxtlhcapabilitiesTable_Object = MibTable
pm1004dcpCfgOtxtlhcapabilitiesTable = _Pm1004dcpCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 8, 1)
)
if mibBuilder.loadTexts:
    pm1004dcpCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm1004dcpCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm1004dcpCfgOtxtlhcapabilitiesEntry = _Pm1004dcpCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 8, 1, 1)
)
pm1004dcpCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm1004dcpCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm1004dcpCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm1004dcpCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm1004dcpCfgOtxtlhcapabilitiesIndex = _Pm1004dcpCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 8, 1, 1, 1),
    _Pm1004dcpCfgOtxtlhcapabilitiesIndex_Type()
)
pm1004dcpCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm1004dcpCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgComponentTypePortn_Object = MibTableColumn
pm1004dcpCfgComponentTypePortn = _Pm1004dcpCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 8, 1, 1, 3),
    _Pm1004dcpCfgComponentTypePortn_Type()
)
pm1004dcpCfgComponentTypePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgComponentTypePortn.setStatus("current")


class _Pm1004dcpCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgMiscellaneousPortn_Object = MibTableColumn
pm1004dcpCfgMiscellaneousPortn = _Pm1004dcpCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 8, 1, 1, 4),
    _Pm1004dcpCfgMiscellaneousPortn_Type()
)
pm1004dcpCfgMiscellaneousPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgMiscellaneousPortn.setStatus("current")


class _Pm1004dcpCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgFirstChannelPortn_Object = MibTableColumn
pm1004dcpCfgFirstChannelPortn = _Pm1004dcpCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 8, 1, 1, 5),
    _Pm1004dcpCfgFirstChannelPortn_Type()
)
pm1004dcpCfgFirstChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgFirstChannelPortn.setStatus("current")


class _Pm1004dcpCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgLastChannelPortn_Object = MibTableColumn
pm1004dcpCfgLastChannelPortn = _Pm1004dcpCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 8, 1, 1, 6),
    _Pm1004dcpCfgLastChannelPortn_Type()
)
pm1004dcpCfgLastChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgLastChannelPortn.setStatus("current")


class _Pm1004dcpCfgGridPortn_Type(Unsigned32):
    """Custom type pm1004dcpCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004dcpCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm1004dcpCfgGridPortn_Object = MibTableColumn
pm1004dcpCfgGridPortn = _Pm1004dcpCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 8, 1, 1, 7),
    _Pm1004dcpCfgGridPortn_Type()
)
pm1004dcpCfgGridPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgGridPortn.setStatus("current")
_Pm1004dcpCfgWriteConfiguration_Type = EkiOnOff
_Pm1004dcpCfgWriteConfiguration_Object = MibScalar
pm1004dcpCfgWriteConfiguration = _Pm1004dcpCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 9, 257),
    _Pm1004dcpCfgWriteConfiguration_Type()
)
pm1004dcpCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpCfgWriteConfiguration.setStatus("current")
_Pm1004dcptraps_ObjectIdentity = ObjectIdentity
pm1004dcptraps = _Pm1004dcptraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10)
)


class _Pm1004dcptrapPortNumber_Type(Integer32):
    """Custom type pm1004dcptrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004dcptrapPortNumber_Type.__name__ = "Integer32"
_Pm1004dcptrapPortNumber_Object = MibScalar
pm1004dcptrapPortNumber = _Pm1004dcptrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 2),
    _Pm1004dcptrapPortNumber_Type()
)
pm1004dcptrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcptrapPortNumber.setStatus("current")


class _Pm1004dcptrapLineNumber_Type(Integer32):
    """Custom type pm1004dcptrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004dcptrapLineNumber_Type.__name__ = "Integer32"
_Pm1004dcptrapLineNumber_Object = MibScalar
pm1004dcptrapLineNumber = _Pm1004dcptrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 3),
    _Pm1004dcptrapLineNumber_Type()
)
pm1004dcptrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcptrapLineNumber.setStatus("current")


class _Pm1004dcptrapBoardNumber_Type(Integer32):
    """Custom type pm1004dcptrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004dcptrapBoardNumber_Type.__name__ = "Integer32"
_Pm1004dcptrapBoardNumber_Object = MibScalar
pm1004dcptrapBoardNumber = _Pm1004dcptrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 4),
    _Pm1004dcptrapBoardNumber_Type()
)
pm1004dcptrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcptrapBoardNumber.setStatus("current")
_Pm1004dcpMonitoring_ObjectIdentity = ObjectIdentity
pm1004dcpMonitoring = _Pm1004dcpMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11)
)
_Pm1004dcpMonOther_ObjectIdentity = ObjectIdentity
pm1004dcpMonOther = _Pm1004dcpMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1)
)
_Pm1004dcpMonSync_ObjectIdentity = ObjectIdentity
pm1004dcpMonSync = _Pm1004dcpMonSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 1)
)
_Pm1004dcpPerfEnable_Type = EkiOnOff
_Pm1004dcpPerfEnable_Object = MibScalar
pm1004dcpPerfEnable = _Pm1004dcpPerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 1, 257),
    _Pm1004dcpPerfEnable_Type()
)
pm1004dcpPerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpPerfEnable.setStatus("current")
_Pm1004dcpPerfSyncSource_Type = EkiSynchroMode
_Pm1004dcpPerfSyncSource_Object = MibScalar
pm1004dcpPerfSyncSource = _Pm1004dcpPerfSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 1, 258),
    _Pm1004dcpPerfSyncSource_Type()
)
pm1004dcpPerfSyncSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpPerfSyncSource.setStatus("current")
_Pm1004dcpPerf15minSync_Type = EkiOnOff
_Pm1004dcpPerf15minSync_Object = MibScalar
pm1004dcpPerf15minSync = _Pm1004dcpPerf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 1, 259),
    _Pm1004dcpPerf15minSync_Type()
)
pm1004dcpPerf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpPerf15minSync.setStatus("current")
_Pm1004dcpPerf24hSync_Type = EkiOnOff
_Pm1004dcpPerf24hSync_Object = MibScalar
pm1004dcpPerf24hSync = _Pm1004dcpPerf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 1, 260),
    _Pm1004dcpPerf24hSync_Type()
)
pm1004dcpPerf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpPerf24hSync.setStatus("current")
_Pm1004dcpMonTimeStamp_ObjectIdentity = ObjectIdentity
pm1004dcpMonTimeStamp = _Pm1004dcpMonTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 2)
)
_Pm1004dcpPerfCurrent15MinElapsedTime_Type = Counter32
_Pm1004dcpPerfCurrent15MinElapsedTime_Object = MibScalar
pm1004dcpPerfCurrent15MinElapsedTime = _Pm1004dcpPerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 2, 5),
    _Pm1004dcpPerfCurrent15MinElapsedTime_Type()
)
pm1004dcpPerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpPerfCurrent15MinElapsedTime.setStatus("current")
_Pm1004dcpPerfCurrent24HoursElapsedTime_Type = Counter32
_Pm1004dcpPerfCurrent24HoursElapsedTime_Object = MibScalar
pm1004dcpPerfCurrent24HoursElapsedTime = _Pm1004dcpPerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 2, 6),
    _Pm1004dcpPerfCurrent24HoursElapsedTime_Type()
)
pm1004dcpPerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpPerfCurrent24HoursElapsedTime.setStatus("current")
_Pm1004dcpPerfPast15MinElapsedTime_Type = Counter32
_Pm1004dcpPerfPast15MinElapsedTime_Object = MibScalar
pm1004dcpPerfPast15MinElapsedTime = _Pm1004dcpPerfPast15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 2, 7),
    _Pm1004dcpPerfPast15MinElapsedTime_Type()
)
pm1004dcpPerfPast15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpPerfPast15MinElapsedTime.setStatus("current")
_Pm1004dcpPerfPast24HoursElapsedTime_Type = Counter32
_Pm1004dcpPerfPast24HoursElapsedTime_Object = MibScalar
pm1004dcpPerfPast24HoursElapsedTime = _Pm1004dcpPerfPast24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 1, 2, 8),
    _Pm1004dcpPerfPast24HoursElapsedTime_Type()
)
pm1004dcpPerfPast24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004dcpPerfPast24HoursElapsedTime.setStatus("current")
_Pm1004dcpMonClient_ObjectIdentity = ObjectIdentity
pm1004dcpMonClient = _Pm1004dcpMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2)
)
_Pm1004dcpMonClientPerformance_ObjectIdentity = ObjectIdentity
pm1004dcpMonClientPerformance = _Pm1004dcpMonClientPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1)
)
_Pm1004dcpPerfUpCurrent15CntTable_Object = MibTable
pm1004dcpPerfUpCurrent15CntTable = _Pm1004dcpPerfUpCurrent15CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16)
)
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntTable.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntEntry_Object = MibTableRow
pm1004dcpPerfUpCurrent15CntEntry = _Pm1004dcpPerfUpCurrent15CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1)
)
pm1004dcpPerfUpCurrent15CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpPerfUpCurrent15CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntEntry.setStatus("current")


class _Pm1004dcpPerfUpCurrent15CntIndex_Type(Integer32):
    """Custom type pm1004dcpPerfUpCurrent15CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpPerfUpCurrent15CntIndex_Type.__name__ = "Integer32"
_Pm1004dcpPerfUpCurrent15CntIndex_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntIndex = _Pm1004dcpPerfUpCurrent15CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 1),
    _Pm1004dcpPerfUpCurrent15CntIndex_Type()
)
pm1004dcpPerfUpCurrent15CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntIndex.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntInvCvPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent15CntInvCvPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntInvCvPortn = _Pm1004dcpPerfUpCurrent15CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 2),
    _Pm1004dcpPerfUpCurrent15CntInvCvPortn_Type()
)
pm1004dcpPerfUpCurrent15CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntInvCvPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntCvValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent15CntCvValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntCvValuePortn = _Pm1004dcpPerfUpCurrent15CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 3),
    _Pm1004dcpPerfUpCurrent15CntCvValuePortn_Type()
)
pm1004dcpPerfUpCurrent15CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntCvValuePortn.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntInvEsPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent15CntInvEsPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntInvEsPortn = _Pm1004dcpPerfUpCurrent15CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 4),
    _Pm1004dcpPerfUpCurrent15CntInvEsPortn_Type()
)
pm1004dcpPerfUpCurrent15CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntInvEsPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntEsValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent15CntEsValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntEsValuePortn = _Pm1004dcpPerfUpCurrent15CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 5),
    _Pm1004dcpPerfUpCurrent15CntEsValuePortn_Type()
)
pm1004dcpPerfUpCurrent15CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntEsValuePortn.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntInvSesPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent15CntInvSesPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntInvSesPortn = _Pm1004dcpPerfUpCurrent15CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 6),
    _Pm1004dcpPerfUpCurrent15CntInvSesPortn_Type()
)
pm1004dcpPerfUpCurrent15CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntInvSesPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntSesValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent15CntSesValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntSesValuePortn = _Pm1004dcpPerfUpCurrent15CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 7),
    _Pm1004dcpPerfUpCurrent15CntSesValuePortn_Type()
)
pm1004dcpPerfUpCurrent15CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntSesValuePortn.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntInvSefsPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent15CntInvSefsPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntInvSefsPortn = _Pm1004dcpPerfUpCurrent15CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 8),
    _Pm1004dcpPerfUpCurrent15CntInvSefsPortn_Type()
)
pm1004dcpPerfUpCurrent15CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntInvSefsPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntSefsValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent15CntSefsValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntSefsValuePortn = _Pm1004dcpPerfUpCurrent15CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 9),
    _Pm1004dcpPerfUpCurrent15CntSefsValuePortn_Type()
)
pm1004dcpPerfUpCurrent15CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntSefsValuePortn.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntInvUasPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent15CntInvUasPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntInvUasPortn = _Pm1004dcpPerfUpCurrent15CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 10),
    _Pm1004dcpPerfUpCurrent15CntInvUasPortn_Type()
)
pm1004dcpPerfUpCurrent15CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntInvUasPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent15CntUasValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent15CntUasValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent15CntUasValuePortn = _Pm1004dcpPerfUpCurrent15CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 16, 1, 11),
    _Pm1004dcpPerfUpCurrent15CntUasValuePortn_Type()
)
pm1004dcpPerfUpCurrent15CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent15CntUasValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntTable_Object = MibTable
pm1004dcpPerfUpPast15CntTable = _Pm1004dcpPerfUpPast15CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24)
)
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntTable.setStatus("current")
_Pm1004dcpPerfUpPast15CntEntry_Object = MibTableRow
pm1004dcpPerfUpPast15CntEntry = _Pm1004dcpPerfUpPast15CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1)
)
pm1004dcpPerfUpPast15CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpPerfUpPast15CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntEntry.setStatus("current")


class _Pm1004dcpPerfUpPast15CntIndex_Type(Integer32):
    """Custom type pm1004dcpPerfUpPast15CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpPerfUpPast15CntIndex_Type.__name__ = "Integer32"
_Pm1004dcpPerfUpPast15CntIndex_Object = MibTableColumn
pm1004dcpPerfUpPast15CntIndex = _Pm1004dcpPerfUpPast15CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 1),
    _Pm1004dcpPerfUpPast15CntIndex_Type()
)
pm1004dcpPerfUpPast15CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntIndex.setStatus("current")
_Pm1004dcpPerfUpPast15CntInvCvPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast15CntInvCvPortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntInvCvPortn = _Pm1004dcpPerfUpPast15CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 2),
    _Pm1004dcpPerfUpPast15CntInvCvPortn_Type()
)
pm1004dcpPerfUpPast15CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntInvCvPortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntCvValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast15CntCvValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntCvValuePortn = _Pm1004dcpPerfUpPast15CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 3),
    _Pm1004dcpPerfUpPast15CntCvValuePortn_Type()
)
pm1004dcpPerfUpPast15CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntCvValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntInvEsPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast15CntInvEsPortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntInvEsPortn = _Pm1004dcpPerfUpPast15CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 4),
    _Pm1004dcpPerfUpPast15CntInvEsPortn_Type()
)
pm1004dcpPerfUpPast15CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntInvEsPortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntEsValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast15CntEsValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntEsValuePortn = _Pm1004dcpPerfUpPast15CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 5),
    _Pm1004dcpPerfUpPast15CntEsValuePortn_Type()
)
pm1004dcpPerfUpPast15CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntEsValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntInvSesPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast15CntInvSesPortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntInvSesPortn = _Pm1004dcpPerfUpPast15CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 6),
    _Pm1004dcpPerfUpPast15CntInvSesPortn_Type()
)
pm1004dcpPerfUpPast15CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntInvSesPortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntSesValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast15CntSesValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntSesValuePortn = _Pm1004dcpPerfUpPast15CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 7),
    _Pm1004dcpPerfUpPast15CntSesValuePortn_Type()
)
pm1004dcpPerfUpPast15CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntSesValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntInvSefsPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast15CntInvSefsPortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntInvSefsPortn = _Pm1004dcpPerfUpPast15CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 8),
    _Pm1004dcpPerfUpPast15CntInvSefsPortn_Type()
)
pm1004dcpPerfUpPast15CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntInvSefsPortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntSefsValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast15CntSefsValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntSefsValuePortn = _Pm1004dcpPerfUpPast15CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 9),
    _Pm1004dcpPerfUpPast15CntSefsValuePortn_Type()
)
pm1004dcpPerfUpPast15CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntSefsValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntInvUasPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast15CntInvUasPortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntInvUasPortn = _Pm1004dcpPerfUpPast15CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 10),
    _Pm1004dcpPerfUpPast15CntInvUasPortn_Type()
)
pm1004dcpPerfUpPast15CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntInvUasPortn.setStatus("current")
_Pm1004dcpPerfUpPast15CntUasValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast15CntUasValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast15CntUasValuePortn = _Pm1004dcpPerfUpPast15CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 24, 1, 11),
    _Pm1004dcpPerfUpPast15CntUasValuePortn_Type()
)
pm1004dcpPerfUpPast15CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast15CntUasValuePortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntTable_Object = MibTable
pm1004dcpPerfUpCurrent24CntTable = _Pm1004dcpPerfUpCurrent24CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32)
)
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntTable.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntEntry_Object = MibTableRow
pm1004dcpPerfUpCurrent24CntEntry = _Pm1004dcpPerfUpCurrent24CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1)
)
pm1004dcpPerfUpCurrent24CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpPerfUpCurrent24CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntEntry.setStatus("current")


class _Pm1004dcpPerfUpCurrent24CntIndex_Type(Integer32):
    """Custom type pm1004dcpPerfUpCurrent24CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpPerfUpCurrent24CntIndex_Type.__name__ = "Integer32"
_Pm1004dcpPerfUpCurrent24CntIndex_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntIndex = _Pm1004dcpPerfUpCurrent24CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 1),
    _Pm1004dcpPerfUpCurrent24CntIndex_Type()
)
pm1004dcpPerfUpCurrent24CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntIndex.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntInvCvPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent24CntInvCvPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntInvCvPortn = _Pm1004dcpPerfUpCurrent24CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 2),
    _Pm1004dcpPerfUpCurrent24CntInvCvPortn_Type()
)
pm1004dcpPerfUpCurrent24CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntInvCvPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntCvValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent24CntCvValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntCvValuePortn = _Pm1004dcpPerfUpCurrent24CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 3),
    _Pm1004dcpPerfUpCurrent24CntCvValuePortn_Type()
)
pm1004dcpPerfUpCurrent24CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntCvValuePortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntInvEsPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent24CntInvEsPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntInvEsPortn = _Pm1004dcpPerfUpCurrent24CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 4),
    _Pm1004dcpPerfUpCurrent24CntInvEsPortn_Type()
)
pm1004dcpPerfUpCurrent24CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntInvEsPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntEsValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent24CntEsValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntEsValuePortn = _Pm1004dcpPerfUpCurrent24CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 5),
    _Pm1004dcpPerfUpCurrent24CntEsValuePortn_Type()
)
pm1004dcpPerfUpCurrent24CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntEsValuePortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntInvSesPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent24CntInvSesPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntInvSesPortn = _Pm1004dcpPerfUpCurrent24CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 6),
    _Pm1004dcpPerfUpCurrent24CntInvSesPortn_Type()
)
pm1004dcpPerfUpCurrent24CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntInvSesPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntSesValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent24CntSesValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntSesValuePortn = _Pm1004dcpPerfUpCurrent24CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 7),
    _Pm1004dcpPerfUpCurrent24CntSesValuePortn_Type()
)
pm1004dcpPerfUpCurrent24CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntSesValuePortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntInvSefsPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent24CntInvSefsPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntInvSefsPortn = _Pm1004dcpPerfUpCurrent24CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 8),
    _Pm1004dcpPerfUpCurrent24CntInvSefsPortn_Type()
)
pm1004dcpPerfUpCurrent24CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntInvSefsPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntSefsValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent24CntSefsValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntSefsValuePortn = _Pm1004dcpPerfUpCurrent24CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 9),
    _Pm1004dcpPerfUpCurrent24CntSefsValuePortn_Type()
)
pm1004dcpPerfUpCurrent24CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntSefsValuePortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntInvUasPortn_Type = EkiOnOff
_Pm1004dcpPerfUpCurrent24CntInvUasPortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntInvUasPortn = _Pm1004dcpPerfUpCurrent24CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 10),
    _Pm1004dcpPerfUpCurrent24CntInvUasPortn_Type()
)
pm1004dcpPerfUpCurrent24CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntInvUasPortn.setStatus("current")
_Pm1004dcpPerfUpCurrent24CntUasValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpCurrent24CntUasValuePortn_Object = MibTableColumn
pm1004dcpPerfUpCurrent24CntUasValuePortn = _Pm1004dcpPerfUpCurrent24CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 32, 1, 11),
    _Pm1004dcpPerfUpCurrent24CntUasValuePortn_Type()
)
pm1004dcpPerfUpCurrent24CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpCurrent24CntUasValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntTable_Object = MibTable
pm1004dcpPerfUpPast24CntTable = _Pm1004dcpPerfUpPast24CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40)
)
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntTable.setStatus("current")
_Pm1004dcpPerfUpPast24CntEntry_Object = MibTableRow
pm1004dcpPerfUpPast24CntEntry = _Pm1004dcpPerfUpPast24CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1)
)
pm1004dcpPerfUpPast24CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpPerfUpPast24CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntEntry.setStatus("current")


class _Pm1004dcpPerfUpPast24CntIndex_Type(Integer32):
    """Custom type pm1004dcpPerfUpPast24CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpPerfUpPast24CntIndex_Type.__name__ = "Integer32"
_Pm1004dcpPerfUpPast24CntIndex_Object = MibTableColumn
pm1004dcpPerfUpPast24CntIndex = _Pm1004dcpPerfUpPast24CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 1),
    _Pm1004dcpPerfUpPast24CntIndex_Type()
)
pm1004dcpPerfUpPast24CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntIndex.setStatus("current")
_Pm1004dcpPerfUpPast24CntInvCvPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast24CntInvCvPortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntInvCvPortn = _Pm1004dcpPerfUpPast24CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 2),
    _Pm1004dcpPerfUpPast24CntInvCvPortn_Type()
)
pm1004dcpPerfUpPast24CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntInvCvPortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntCvValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast24CntCvValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntCvValuePortn = _Pm1004dcpPerfUpPast24CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 3),
    _Pm1004dcpPerfUpPast24CntCvValuePortn_Type()
)
pm1004dcpPerfUpPast24CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntCvValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntInvEsPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast24CntInvEsPortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntInvEsPortn = _Pm1004dcpPerfUpPast24CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 4),
    _Pm1004dcpPerfUpPast24CntInvEsPortn_Type()
)
pm1004dcpPerfUpPast24CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntInvEsPortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntEsValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast24CntEsValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntEsValuePortn = _Pm1004dcpPerfUpPast24CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 5),
    _Pm1004dcpPerfUpPast24CntEsValuePortn_Type()
)
pm1004dcpPerfUpPast24CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntEsValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntInvSesPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast24CntInvSesPortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntInvSesPortn = _Pm1004dcpPerfUpPast24CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 6),
    _Pm1004dcpPerfUpPast24CntInvSesPortn_Type()
)
pm1004dcpPerfUpPast24CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntInvSesPortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntSesValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast24CntSesValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntSesValuePortn = _Pm1004dcpPerfUpPast24CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 7),
    _Pm1004dcpPerfUpPast24CntSesValuePortn_Type()
)
pm1004dcpPerfUpPast24CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntSesValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntInvSefsPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast24CntInvSefsPortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntInvSefsPortn = _Pm1004dcpPerfUpPast24CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 8),
    _Pm1004dcpPerfUpPast24CntInvSefsPortn_Type()
)
pm1004dcpPerfUpPast24CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntInvSefsPortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntSefsValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast24CntSefsValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntSefsValuePortn = _Pm1004dcpPerfUpPast24CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 9),
    _Pm1004dcpPerfUpPast24CntSefsValuePortn_Type()
)
pm1004dcpPerfUpPast24CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntSefsValuePortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntInvUasPortn_Type = EkiOnOff
_Pm1004dcpPerfUpPast24CntInvUasPortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntInvUasPortn = _Pm1004dcpPerfUpPast24CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 10),
    _Pm1004dcpPerfUpPast24CntInvUasPortn_Type()
)
pm1004dcpPerfUpPast24CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntInvUasPortn.setStatus("current")
_Pm1004dcpPerfUpPast24CntUasValuePortn_Type = Unsigned32
_Pm1004dcpPerfUpPast24CntUasValuePortn_Object = MibTableColumn
pm1004dcpPerfUpPast24CntUasValuePortn = _Pm1004dcpPerfUpPast24CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 1, 40, 1, 11),
    _Pm1004dcpPerfUpPast24CntUasValuePortn_Type()
)
pm1004dcpPerfUpPast24CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfUpPast24CntUasValuePortn.setStatus("current")
_Pm1004dcpMonClientTraceIdentifier_ObjectIdentity = ObjectIdentity
pm1004dcpMonClientTraceIdentifier = _Pm1004dcpMonClientTraceIdentifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 2)
)
_Pm1004dcpAlmj0AlarmTable_Object = MibTable
pm1004dcpAlmj0AlarmTable = _Pm1004dcpAlmj0AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 2, 2112)
)
if mibBuilder.loadTexts:
    pm1004dcpAlmj0AlarmTable.setStatus("current")
_Pm1004dcpAlmj0AlarmEntry_Object = MibTableRow
pm1004dcpAlmj0AlarmEntry = _Pm1004dcpAlmj0AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 2, 2112, 1)
)
pm1004dcpAlmj0AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmj0AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpAlmj0AlarmEntry.setStatus("current")


class _Pm1004dcpAlmj0AlarmIndex_Type(Integer32):
    """Custom type pm1004dcpAlmj0AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpAlmj0AlarmIndex_Type.__name__ = "Integer32"
_Pm1004dcpAlmj0AlarmIndex_Object = MibTableColumn
pm1004dcpAlmj0AlarmIndex = _Pm1004dcpAlmj0AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 2, 2112, 1, 1),
    _Pm1004dcpAlmj0AlarmIndex_Type()
)
pm1004dcpAlmj0AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmj0AlarmIndex.setStatus("current")
_Pm1004dcpAlmJ0TimAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmJ0TimAlarmPortn_Object = MibTableColumn
pm1004dcpAlmJ0TimAlarmPortn = _Pm1004dcpAlmJ0TimAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 2, 2112, 1, 2),
    _Pm1004dcpAlmJ0TimAlarmPortn_Type()
)
pm1004dcpAlmJ0TimAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmJ0TimAlarmPortn.setStatus("current")
_Pm1004dcpAlmJ0TiiAlarmPortn_Type = EkiOnOff
_Pm1004dcpAlmJ0TiiAlarmPortn_Object = MibTableColumn
pm1004dcpAlmJ0TiiAlarmPortn = _Pm1004dcpAlmJ0TiiAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 2, 2112, 1, 3),
    _Pm1004dcpAlmJ0TiiAlarmPortn_Type()
)
pm1004dcpAlmJ0TiiAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmJ0TiiAlarmPortn.setStatus("current")
_Pm1004dcpAlmCrc7ErrorPortn_Type = EkiOnOff
_Pm1004dcpAlmCrc7ErrorPortn_Object = MibTableColumn
pm1004dcpAlmCrc7ErrorPortn = _Pm1004dcpAlmCrc7ErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 2, 2, 2112, 1, 4),
    _Pm1004dcpAlmCrc7ErrorPortn_Type()
)
pm1004dcpAlmCrc7ErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpAlmCrc7ErrorPortn.setStatus("current")
_Pm1004dcpMonLine_ObjectIdentity = ObjectIdentity
pm1004dcpMonLine = _Pm1004dcpMonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3)
)
_Pm1004dcpMonLinePerformance_ObjectIdentity = ObjectIdentity
pm1004dcpMonLinePerformance = _Pm1004dcpMonLinePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1)
)
_Pm1004dcpPerfLineCurrent15CntTable_Object = MibTable
pm1004dcpPerfLineCurrent15CntTable = _Pm1004dcpPerfLineCurrent15CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128)
)
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntTable.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntEntry_Object = MibTableRow
pm1004dcpPerfLineCurrent15CntEntry = _Pm1004dcpPerfLineCurrent15CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1)
)
pm1004dcpPerfLineCurrent15CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpPerfLineCurrent15CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntEntry.setStatus("current")


class _Pm1004dcpPerfLineCurrent15CntIndex_Type(Integer32):
    """Custom type pm1004dcpPerfLineCurrent15CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpPerfLineCurrent15CntIndex_Type.__name__ = "Integer32"
_Pm1004dcpPerfLineCurrent15CntIndex_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntIndex = _Pm1004dcpPerfLineCurrent15CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 1),
    _Pm1004dcpPerfLineCurrent15CntIndex_Type()
)
pm1004dcpPerfLineCurrent15CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntIndex.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntInvCvPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent15CntInvCvPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntInvCvPortn = _Pm1004dcpPerfLineCurrent15CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 2),
    _Pm1004dcpPerfLineCurrent15CntInvCvPortn_Type()
)
pm1004dcpPerfLineCurrent15CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntInvCvPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntCvValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent15CntCvValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntCvValuePortn = _Pm1004dcpPerfLineCurrent15CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 3),
    _Pm1004dcpPerfLineCurrent15CntCvValuePortn_Type()
)
pm1004dcpPerfLineCurrent15CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntCvValuePortn.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntInvEsPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent15CntInvEsPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntInvEsPortn = _Pm1004dcpPerfLineCurrent15CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 4),
    _Pm1004dcpPerfLineCurrent15CntInvEsPortn_Type()
)
pm1004dcpPerfLineCurrent15CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntInvEsPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntEsValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent15CntEsValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntEsValuePortn = _Pm1004dcpPerfLineCurrent15CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 5),
    _Pm1004dcpPerfLineCurrent15CntEsValuePortn_Type()
)
pm1004dcpPerfLineCurrent15CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntEsValuePortn.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntInvSesPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent15CntInvSesPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntInvSesPortn = _Pm1004dcpPerfLineCurrent15CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 6),
    _Pm1004dcpPerfLineCurrent15CntInvSesPortn_Type()
)
pm1004dcpPerfLineCurrent15CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntInvSesPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntSesValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent15CntSesValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntSesValuePortn = _Pm1004dcpPerfLineCurrent15CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 7),
    _Pm1004dcpPerfLineCurrent15CntSesValuePortn_Type()
)
pm1004dcpPerfLineCurrent15CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntSesValuePortn.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntInvSefsPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent15CntInvSefsPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntInvSefsPortn = _Pm1004dcpPerfLineCurrent15CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 8),
    _Pm1004dcpPerfLineCurrent15CntInvSefsPortn_Type()
)
pm1004dcpPerfLineCurrent15CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntInvSefsPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntSefsValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent15CntSefsValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntSefsValuePortn = _Pm1004dcpPerfLineCurrent15CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 9),
    _Pm1004dcpPerfLineCurrent15CntSefsValuePortn_Type()
)
pm1004dcpPerfLineCurrent15CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntSefsValuePortn.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntInvUasPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent15CntInvUasPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntInvUasPortn = _Pm1004dcpPerfLineCurrent15CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 10),
    _Pm1004dcpPerfLineCurrent15CntInvUasPortn_Type()
)
pm1004dcpPerfLineCurrent15CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntInvUasPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent15CntUasValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent15CntUasValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent15CntUasValuePortn = _Pm1004dcpPerfLineCurrent15CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 128, 1, 11),
    _Pm1004dcpPerfLineCurrent15CntUasValuePortn_Type()
)
pm1004dcpPerfLineCurrent15CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent15CntUasValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntTable_Object = MibTable
pm1004dcpPerfLinePast15CntTable = _Pm1004dcpPerfLinePast15CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129)
)
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntTable.setStatus("current")
_Pm1004dcpPerfLinePast15CntEntry_Object = MibTableRow
pm1004dcpPerfLinePast15CntEntry = _Pm1004dcpPerfLinePast15CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1)
)
pm1004dcpPerfLinePast15CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpPerfLinePast15CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntEntry.setStatus("current")


class _Pm1004dcpPerfLinePast15CntIndex_Type(Integer32):
    """Custom type pm1004dcpPerfLinePast15CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpPerfLinePast15CntIndex_Type.__name__ = "Integer32"
_Pm1004dcpPerfLinePast15CntIndex_Object = MibTableColumn
pm1004dcpPerfLinePast15CntIndex = _Pm1004dcpPerfLinePast15CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 1),
    _Pm1004dcpPerfLinePast15CntIndex_Type()
)
pm1004dcpPerfLinePast15CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntIndex.setStatus("current")
_Pm1004dcpPerfLinePast15CntInvCvPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast15CntInvCvPortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntInvCvPortn = _Pm1004dcpPerfLinePast15CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 2),
    _Pm1004dcpPerfLinePast15CntInvCvPortn_Type()
)
pm1004dcpPerfLinePast15CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntInvCvPortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntCvValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast15CntCvValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntCvValuePortn = _Pm1004dcpPerfLinePast15CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 3),
    _Pm1004dcpPerfLinePast15CntCvValuePortn_Type()
)
pm1004dcpPerfLinePast15CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntCvValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntInvEsPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast15CntInvEsPortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntInvEsPortn = _Pm1004dcpPerfLinePast15CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 4),
    _Pm1004dcpPerfLinePast15CntInvEsPortn_Type()
)
pm1004dcpPerfLinePast15CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntInvEsPortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntEsValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast15CntEsValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntEsValuePortn = _Pm1004dcpPerfLinePast15CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 5),
    _Pm1004dcpPerfLinePast15CntEsValuePortn_Type()
)
pm1004dcpPerfLinePast15CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntEsValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntInvSesPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast15CntInvSesPortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntInvSesPortn = _Pm1004dcpPerfLinePast15CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 6),
    _Pm1004dcpPerfLinePast15CntInvSesPortn_Type()
)
pm1004dcpPerfLinePast15CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntInvSesPortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntSesValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast15CntSesValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntSesValuePortn = _Pm1004dcpPerfLinePast15CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 7),
    _Pm1004dcpPerfLinePast15CntSesValuePortn_Type()
)
pm1004dcpPerfLinePast15CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntSesValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntInvSefsPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast15CntInvSefsPortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntInvSefsPortn = _Pm1004dcpPerfLinePast15CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 8),
    _Pm1004dcpPerfLinePast15CntInvSefsPortn_Type()
)
pm1004dcpPerfLinePast15CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntInvSefsPortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntSefsValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast15CntSefsValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntSefsValuePortn = _Pm1004dcpPerfLinePast15CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 9),
    _Pm1004dcpPerfLinePast15CntSefsValuePortn_Type()
)
pm1004dcpPerfLinePast15CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntSefsValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntInvUasPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast15CntInvUasPortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntInvUasPortn = _Pm1004dcpPerfLinePast15CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 10),
    _Pm1004dcpPerfLinePast15CntInvUasPortn_Type()
)
pm1004dcpPerfLinePast15CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntInvUasPortn.setStatus("current")
_Pm1004dcpPerfLinePast15CntUasValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast15CntUasValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast15CntUasValuePortn = _Pm1004dcpPerfLinePast15CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 129, 1, 11),
    _Pm1004dcpPerfLinePast15CntUasValuePortn_Type()
)
pm1004dcpPerfLinePast15CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast15CntUasValuePortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntTable_Object = MibTable
pm1004dcpPerfLineCurrent24CntTable = _Pm1004dcpPerfLineCurrent24CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130)
)
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntTable.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntEntry_Object = MibTableRow
pm1004dcpPerfLineCurrent24CntEntry = _Pm1004dcpPerfLineCurrent24CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1)
)
pm1004dcpPerfLineCurrent24CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpPerfLineCurrent24CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntEntry.setStatus("current")


class _Pm1004dcpPerfLineCurrent24CntIndex_Type(Integer32):
    """Custom type pm1004dcpPerfLineCurrent24CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpPerfLineCurrent24CntIndex_Type.__name__ = "Integer32"
_Pm1004dcpPerfLineCurrent24CntIndex_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntIndex = _Pm1004dcpPerfLineCurrent24CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 1),
    _Pm1004dcpPerfLineCurrent24CntIndex_Type()
)
pm1004dcpPerfLineCurrent24CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntIndex.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntInvCvPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent24CntInvCvPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntInvCvPortn = _Pm1004dcpPerfLineCurrent24CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 2),
    _Pm1004dcpPerfLineCurrent24CntInvCvPortn_Type()
)
pm1004dcpPerfLineCurrent24CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntInvCvPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntCvValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent24CntCvValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntCvValuePortn = _Pm1004dcpPerfLineCurrent24CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 3),
    _Pm1004dcpPerfLineCurrent24CntCvValuePortn_Type()
)
pm1004dcpPerfLineCurrent24CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntCvValuePortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntInvEsPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent24CntInvEsPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntInvEsPortn = _Pm1004dcpPerfLineCurrent24CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 4),
    _Pm1004dcpPerfLineCurrent24CntInvEsPortn_Type()
)
pm1004dcpPerfLineCurrent24CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntInvEsPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntEsValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent24CntEsValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntEsValuePortn = _Pm1004dcpPerfLineCurrent24CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 5),
    _Pm1004dcpPerfLineCurrent24CntEsValuePortn_Type()
)
pm1004dcpPerfLineCurrent24CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntEsValuePortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntInvSesPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent24CntInvSesPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntInvSesPortn = _Pm1004dcpPerfLineCurrent24CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 6),
    _Pm1004dcpPerfLineCurrent24CntInvSesPortn_Type()
)
pm1004dcpPerfLineCurrent24CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntInvSesPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntSesValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent24CntSesValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntSesValuePortn = _Pm1004dcpPerfLineCurrent24CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 7),
    _Pm1004dcpPerfLineCurrent24CntSesValuePortn_Type()
)
pm1004dcpPerfLineCurrent24CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntSesValuePortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntInvSefsPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent24CntInvSefsPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntInvSefsPortn = _Pm1004dcpPerfLineCurrent24CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 8),
    _Pm1004dcpPerfLineCurrent24CntInvSefsPortn_Type()
)
pm1004dcpPerfLineCurrent24CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntInvSefsPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntSefsValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent24CntSefsValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntSefsValuePortn = _Pm1004dcpPerfLineCurrent24CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 9),
    _Pm1004dcpPerfLineCurrent24CntSefsValuePortn_Type()
)
pm1004dcpPerfLineCurrent24CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntSefsValuePortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntInvUasPortn_Type = EkiOnOff
_Pm1004dcpPerfLineCurrent24CntInvUasPortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntInvUasPortn = _Pm1004dcpPerfLineCurrent24CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 10),
    _Pm1004dcpPerfLineCurrent24CntInvUasPortn_Type()
)
pm1004dcpPerfLineCurrent24CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntInvUasPortn.setStatus("current")
_Pm1004dcpPerfLineCurrent24CntUasValuePortn_Type = Unsigned32
_Pm1004dcpPerfLineCurrent24CntUasValuePortn_Object = MibTableColumn
pm1004dcpPerfLineCurrent24CntUasValuePortn = _Pm1004dcpPerfLineCurrent24CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 130, 1, 11),
    _Pm1004dcpPerfLineCurrent24CntUasValuePortn_Type()
)
pm1004dcpPerfLineCurrent24CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLineCurrent24CntUasValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntTable_Object = MibTable
pm1004dcpPerfLinePast24CntTable = _Pm1004dcpPerfLinePast24CntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131)
)
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntTable.setStatus("current")
_Pm1004dcpPerfLinePast24CntEntry_Object = MibTableRow
pm1004dcpPerfLinePast24CntEntry = _Pm1004dcpPerfLinePast24CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1)
)
pm1004dcpPerfLinePast24CntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004dcp-MIB", "pm1004dcpPerfLinePast24CntIndex"),
)
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntEntry.setStatus("current")


class _Pm1004dcpPerfLinePast24CntIndex_Type(Integer32):
    """Custom type pm1004dcpPerfLinePast24CntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004dcpPerfLinePast24CntIndex_Type.__name__ = "Integer32"
_Pm1004dcpPerfLinePast24CntIndex_Object = MibTableColumn
pm1004dcpPerfLinePast24CntIndex = _Pm1004dcpPerfLinePast24CntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 1),
    _Pm1004dcpPerfLinePast24CntIndex_Type()
)
pm1004dcpPerfLinePast24CntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntIndex.setStatus("current")
_Pm1004dcpPerfLinePast24CntInvCvPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast24CntInvCvPortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntInvCvPortn = _Pm1004dcpPerfLinePast24CntInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 2),
    _Pm1004dcpPerfLinePast24CntInvCvPortn_Type()
)
pm1004dcpPerfLinePast24CntInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntInvCvPortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntCvValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast24CntCvValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntCvValuePortn = _Pm1004dcpPerfLinePast24CntCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 3),
    _Pm1004dcpPerfLinePast24CntCvValuePortn_Type()
)
pm1004dcpPerfLinePast24CntCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntCvValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntInvEsPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast24CntInvEsPortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntInvEsPortn = _Pm1004dcpPerfLinePast24CntInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 4),
    _Pm1004dcpPerfLinePast24CntInvEsPortn_Type()
)
pm1004dcpPerfLinePast24CntInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntInvEsPortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntEsValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast24CntEsValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntEsValuePortn = _Pm1004dcpPerfLinePast24CntEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 5),
    _Pm1004dcpPerfLinePast24CntEsValuePortn_Type()
)
pm1004dcpPerfLinePast24CntEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntEsValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntInvSesPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast24CntInvSesPortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntInvSesPortn = _Pm1004dcpPerfLinePast24CntInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 6),
    _Pm1004dcpPerfLinePast24CntInvSesPortn_Type()
)
pm1004dcpPerfLinePast24CntInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntInvSesPortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntSesValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast24CntSesValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntSesValuePortn = _Pm1004dcpPerfLinePast24CntSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 7),
    _Pm1004dcpPerfLinePast24CntSesValuePortn_Type()
)
pm1004dcpPerfLinePast24CntSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntSesValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntInvSefsPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast24CntInvSefsPortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntInvSefsPortn = _Pm1004dcpPerfLinePast24CntInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 8),
    _Pm1004dcpPerfLinePast24CntInvSefsPortn_Type()
)
pm1004dcpPerfLinePast24CntInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntInvSefsPortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntSefsValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast24CntSefsValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntSefsValuePortn = _Pm1004dcpPerfLinePast24CntSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 9),
    _Pm1004dcpPerfLinePast24CntSefsValuePortn_Type()
)
pm1004dcpPerfLinePast24CntSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntSefsValuePortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntInvUasPortn_Type = EkiOnOff
_Pm1004dcpPerfLinePast24CntInvUasPortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntInvUasPortn = _Pm1004dcpPerfLinePast24CntInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 10),
    _Pm1004dcpPerfLinePast24CntInvUasPortn_Type()
)
pm1004dcpPerfLinePast24CntInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntInvUasPortn.setStatus("current")
_Pm1004dcpPerfLinePast24CntUasValuePortn_Type = Unsigned32
_Pm1004dcpPerfLinePast24CntUasValuePortn_Object = MibTableColumn
pm1004dcpPerfLinePast24CntUasValuePortn = _Pm1004dcpPerfLinePast24CntUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 1, 131, 1, 11),
    _Pm1004dcpPerfLinePast24CntUasValuePortn_Type()
)
pm1004dcpPerfLinePast24CntUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004dcpPerfLinePast24CntUasValuePortn.setStatus("current")
_Pm1004dcpMonLineTraceIdentifier_ObjectIdentity = ObjectIdentity
pm1004dcpMonLineTraceIdentifier = _Pm1004dcpMonLineTraceIdentifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 37, 11, 3, 2)
)

# Managed Objects groups


# Notification objects

pm1004dcpLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 30)
)
pm1004dcpLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapLineNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1004dcpLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 31)
)
pm1004dcpLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapLineNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1004dcpLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 32)
)
pm1004dcpLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapLineNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004dcpLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 33)
)
pm1004dcpLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapLineNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1004dcpLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 34)
)
pm1004dcpLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmLineFailPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapLineNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpLineTrapCritGoesOn.setStatus(
        "current"
    )

pm1004dcpLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 35)
)
pm1004dcpLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmLineFailPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapLineNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpLineTrapCritGoesOff.setStatus(
        "current"
    )

pm1004dcpClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 40)
)
pm1004dcpClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapPortNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1004dcpClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 41)
)
pm1004dcpClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapPortNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1004dcpClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 42)
)
pm1004dcpClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapPortNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004dcpClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 43)
)
pm1004dcpClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapPortNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1004dcpClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 44)
)
pm1004dcpClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmFailAccPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapPortNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpClientTrapCritGoesOn.setStatus(
        "current"
    )

pm1004dcpClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 45)
)
pm1004dcpClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmFailAccPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapPortNumber"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpClientTrapCritGoesOff.setStatus(
        "current"
    )

pm1004dcpPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 50)
)
pm1004dcpPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmDefFuseB"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmDefFuseA"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004dcpPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 37, 10, 51)
)
pm1004dcpPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmDefFuseB"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcpAlmDefFuseA"),
        ("EKINOPS-Pm1004dcp-MIB", "pm1004dcptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004dcpPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1004dcp-MIB",
    **{"Pm1004dcpModeTimeSlot": Pm1004dcpModeTimeSlot,
       "Pm1004dcpModeAddDropA": Pm1004dcpModeAddDropA,
       "Pm1004dcpModeAddDrop": Pm1004dcpModeAddDrop,
       "Pm1004dcpProtectionTimeSlot": Pm1004dcpProtectionTimeSlot,
       "Pm1004dcpProtectionStartUp": Pm1004dcpProtectionStartUp,
       "Pm1004dcpDccMode": Pm1004dcpDccMode,
       "Pm1004dcpOtxMode": Pm1004dcpOtxMode,
       "Pm1004dcpOtxGrid": Pm1004dcpOtxGrid,
       "Pm1004dcpAdjustValue": Pm1004dcpAdjustValue,
       "Pm1004dcpOtxChannel": Pm1004dcpOtxChannel,
       "modulePm1004dcp": modulePm1004dcp,
       "pm1004dcpalarms": pm1004dcpalarms,
       "pm1004dcpAlmOther": pm1004dcpAlmOther,
       "pm1004dcpAlmOtherNurg": pm1004dcpAlmOtherNurg,
       "pm1004dcpAlmsynthAlm2": pm1004dcpAlmsynthAlm2,
       "pm1004dcpAlmConfTableSave": pm1004dcpAlmConfTableSave,
       "pm1004dcpAlmInvUpload": pm1004dcpAlmInvUpload,
       "pm1004dcpAlmConfTableLoad": pm1004dcpAlmConfTableLoad,
       "pm1004dcpAlmCorrelatOff": pm1004dcpAlmCorrelatOff,
       "pm1004dcpAlmMaintenanceOn": pm1004dcpAlmMaintenanceOn,
       "pm1004dcpAlmOtherUrg": pm1004dcpAlmOtherUrg,
       "pm1004dcpAlmmodInitFailLevel2": pm1004dcpAlmmodInitFailLevel2,
       "pm1004dcpAlmLedFail": pm1004dcpAlmLedFail,
       "pm1004dcpAlmNextColdBootForced": pm1004dcpAlmNextColdBootForced,
       "pm1004dcpAlmBootUndone": pm1004dcpAlmBootUndone,
       "pm1004dcpAlmResetHwInitFail": pm1004dcpAlmResetHwInitFail,
       "pm1004dcpAlmSwInitFail": pm1004dcpAlmSwInitFail,
       "pm1004dcpAlmmodInitFailLevel3": pm1004dcpAlmmodInitFailLevel3,
       "pm1004dcpAlmGwIdentFail": pm1004dcpAlmGwIdentFail,
       "pm1004dcpAlmObmTypeReadFail": pm1004dcpAlmObmTypeReadFail,
       "pm1004dcpAlmInitModuleFail": pm1004dcpAlmInitModuleFail,
       "pm1004dcpAlmXfp1InitFail": pm1004dcpAlmXfp1InitFail,
       "pm1004dcpAlmXfp2InitFail": pm1004dcpAlmXfp2InitFail,
       "pm1004dcpAlmLine1InitFail": pm1004dcpAlmLine1InitFail,
       "pm1004dcpAlmLine2InitFail": pm1004dcpAlmLine2InitFail,
       "pm1004dcpAlmClient1InitFail": pm1004dcpAlmClient1InitFail,
       "pm1004dcpAlmClient2InitFail": pm1004dcpAlmClient2InitFail,
       "pm1004dcpAlmClient3InitFail": pm1004dcpAlmClient3InitFail,
       "pm1004dcpAlmClient4InitFail": pm1004dcpAlmClient4InitFail,
       "pm1004dcpAlmadddropTsClientRxProt": pm1004dcpAlmadddropTsClientRxProt,
       "pm1004dcpAlmAdddropClient1West": pm1004dcpAlmAdddropClient1West,
       "pm1004dcpAlmAdddropClient2West": pm1004dcpAlmAdddropClient2West,
       "pm1004dcpAlmAdddropClient3West": pm1004dcpAlmAdddropClient3West,
       "pm1004dcpAlmAdddropClient4West": pm1004dcpAlmAdddropClient4West,
       "pm1004dcpAlmAdddropClient1East": pm1004dcpAlmAdddropClient1East,
       "pm1004dcpAlmAdddropClient2East": pm1004dcpAlmAdddropClient2East,
       "pm1004dcpAlmAdddropClient3East": pm1004dcpAlmAdddropClient3East,
       "pm1004dcpAlmAdddropClient4East": pm1004dcpAlmAdddropClient4East,
       "pm1004dcpAlmOtherCrit": pm1004dcpAlmOtherCrit,
       "pm1004dcpAlmsynthAlm0": pm1004dcpAlmsynthAlm0,
       "pm1004dcpAlmModGlobFail": pm1004dcpAlmModGlobFail,
       "pm1004dcpAlmDefFuseA": pm1004dcpAlmDefFuseA,
       "pm1004dcpAlmDefFuseB": pm1004dcpAlmDefFuseB,
       "pm1004dcpAlmClient": pm1004dcpAlmClient,
       "pm1004dcpAlmClientNurg": pm1004dcpAlmClientNurg,
       "pm1004dcpAlmsfpWarnDdmTable": pm1004dcpAlmsfpWarnDdmTable,
       "pm1004dcpAlmsfpWarnDdmEntry": pm1004dcpAlmsfpWarnDdmEntry,
       "pm1004dcpAlmsfpWarnDdmIndex": pm1004dcpAlmsfpWarnDdmIndex,
       "pm1004dcpAlmTxPwLowWngPortn": pm1004dcpAlmTxPwLowWngPortn,
       "pm1004dcpAlmTxPwrHighWngPortn": pm1004dcpAlmTxPwrHighWngPortn,
       "pm1004dcpAlmTxBiasLowWngPortn": pm1004dcpAlmTxBiasLowWngPortn,
       "pm1004dcpAlmTxBiasHighWngPortn": pm1004dcpAlmTxBiasHighWngPortn,
       "pm1004dcpAlmVccLowWngPortn": pm1004dcpAlmVccLowWngPortn,
       "pm1004dcpAlmVccHighWngPortn": pm1004dcpAlmVccHighWngPortn,
       "pm1004dcpAlmTempLowWngPortn": pm1004dcpAlmTempLowWngPortn,
       "pm1004dcpAlmTempHighWngPortn": pm1004dcpAlmTempHighWngPortn,
       "pm1004dcpAlmRxPwrLowWngPortn": pm1004dcpAlmRxPwrLowWngPortn,
       "pm1004dcpAlmRxPwrHighWngPortn": pm1004dcpAlmRxPwrHighWngPortn,
       "pm1004dcpAlmk1K2ClientTable": pm1004dcpAlmk1K2ClientTable,
       "pm1004dcpAlmk1K2ClientEntry": pm1004dcpAlmk1K2ClientEntry,
       "pm1004dcpAlmk1K2ClientIndex": pm1004dcpAlmk1K2ClientIndex,
       "pm1004dcpAlmk1K2ClientPortn": pm1004dcpAlmk1K2ClientPortn,
       "pm1004dcpAlmClientUrg": pm1004dcpAlmClientUrg,
       "pm1004dcpAlmsfpAlmDdmTable": pm1004dcpAlmsfpAlmDdmTable,
       "pm1004dcpAlmsfpAlmDdmEntry": pm1004dcpAlmsfpAlmDdmEntry,
       "pm1004dcpAlmsfpAlmDdmIndex": pm1004dcpAlmsfpAlmDdmIndex,
       "pm1004dcpAlmTxPwrLowAlaPortn": pm1004dcpAlmTxPwrLowAlaPortn,
       "pm1004dcpAlmTxPwrHighAlaPortn": pm1004dcpAlmTxPwrHighAlaPortn,
       "pm1004dcpAlmTxBiasLowAlaPortn": pm1004dcpAlmTxBiasLowAlaPortn,
       "pm1004dcpAlmTxBiasHighAlaPortn": pm1004dcpAlmTxBiasHighAlaPortn,
       "pm1004dcpAlmVccLowAlaPortn": pm1004dcpAlmVccLowAlaPortn,
       "pm1004dcpAlmVccHighAlaPortn": pm1004dcpAlmVccHighAlaPortn,
       "pm1004dcpAlmTempLowAlaPortn": pm1004dcpAlmTempLowAlaPortn,
       "pm1004dcpAlmTempHighAlaPortn": pm1004dcpAlmTempHighAlaPortn,
       "pm1004dcpAlmRxPwrLowAlaPortn": pm1004dcpAlmRxPwrLowAlaPortn,
       "pm1004dcpAlmRxPwrHighAlaPortn": pm1004dcpAlmRxPwrHighAlaPortn,
       "pm1004dcpAlmClientCrit": pm1004dcpAlmClientCrit,
       "pm1004dcpAlmsynthAlmPortTable": pm1004dcpAlmsynthAlmPortTable,
       "pm1004dcpAlmsynthAlmPortEntry": pm1004dcpAlmsynthAlmPortEntry,
       "pm1004dcpAlmsynthAlmPortIndex": pm1004dcpAlmsynthAlmPortIndex,
       "pm1004dcpAlmSfpAbsentPortn": pm1004dcpAlmSfpAbsentPortn,
       "pm1004dcpAlmDdmAbsentPortn": pm1004dcpAlmDdmAbsentPortn,
       "pm1004dcpAlmHwFailAccPortn": pm1004dcpAlmHwFailAccPortn,
       "pm1004dcpAlmDwLsdPortn": pm1004dcpAlmDwLsdPortn,
       "pm1004dcpAlmClientLocalOosPortn": pm1004dcpAlmClientLocalOosPortn,
       "pm1004dcpAlmClientRemoteOosPortn": pm1004dcpAlmClientRemoteOosPortn,
       "pm1004dcpAlmDwCaisPortn": pm1004dcpAlmDwCaisPortn,
       "pm1004dcpAlmSfpDdmWarningPortn": pm1004dcpAlmSfpDdmWarningPortn,
       "pm1004dcpAlmSfpDdmAlmPortn": pm1004dcpAlmSfpDdmAlmPortn,
       "pm1004dcpAlmFailAccPortn": pm1004dcpAlmFailAccPortn,
       "pm1004dcpAlmClientActivePortn": pm1004dcpAlmClientActivePortn,
       "pm1004dcpAlmUpCsfPortn": pm1004dcpAlmUpCsfPortn,
       "pm1004dcpAlmaccessioAlmTable": pm1004dcpAlmaccessioAlmTable,
       "pm1004dcpAlmaccessioAlmEntry": pm1004dcpAlmaccessioAlmEntry,
       "pm1004dcpAlmaccessioAlmIndex": pm1004dcpAlmaccessioAlmIndex,
       "pm1004dcpAlmDwLasFailPortn": pm1004dcpAlmDwLasFailPortn,
       "pm1004dcpAlmUpLosPortn": pm1004dcpAlmUpLosPortn,
       "pm1004dcpAlmmapperDeAlmTable": pm1004dcpAlmmapperDeAlmTable,
       "pm1004dcpAlmmapperDeAlmEntry": pm1004dcpAlmmapperDeAlmEntry,
       "pm1004dcpAlmmapperDeAlmIndex": pm1004dcpAlmmapperDeAlmIndex,
       "pm1004dcpAlmUpAccOosPortn": pm1004dcpAlmUpAccOosPortn,
       "pm1004dcpAlmUpBufferOvlPortn": pm1004dcpAlmUpBufferOvlPortn,
       "pm1004dcpAlmDwCsfDetPortn": pm1004dcpAlmDwCsfDetPortn,
       "pm1004dcpAlmDwBufferOvlPortn": pm1004dcpAlmDwBufferOvlPortn,
       "pm1004dcpAlmaccessioSdhAlarmTable": pm1004dcpAlmaccessioSdhAlarmTable,
       "pm1004dcpAlmaccessioSdhAlarmEntry": pm1004dcpAlmaccessioSdhAlarmEntry,
       "pm1004dcpAlmaccessioSdhAlarmIndex": pm1004dcpAlmaccessioSdhAlarmIndex,
       "pm1004dcpAlmFifoErrPortn": pm1004dcpAlmFifoErrPortn,
       "pm1004dcpAlmRxLossOfLockPortn": pm1004dcpAlmRxLossOfLockPortn,
       "pm1004dcpAlmTxLossOfLockPortn": pm1004dcpAlmTxLossOfLockPortn,
       "pm1004dcpAlmClientAisDetPortn": pm1004dcpAlmClientAisDetPortn,
       "pm1004dcpAlmClientRdiDetPortn": pm1004dcpAlmClientRdiDetPortn,
       "pm1004dcpAlmClientOofPortn": pm1004dcpAlmClientOofPortn,
       "pm1004dcpAlmLine": pm1004dcpAlmLine,
       "pm1004dcpAlmLineNurg": pm1004dcpAlmLineNurg,
       "pm1004dcpAlmlineXfp1WarningsTable": pm1004dcpAlmlineXfp1WarningsTable,
       "pm1004dcpAlmlineXfp1WarningsEntry": pm1004dcpAlmlineXfp1WarningsEntry,
       "pm1004dcpAlmlineXfp1WarningsIndex": pm1004dcpAlmlineXfp1WarningsIndex,
       "pm1004dcpAlmTxPowerLowWarningPortn": pm1004dcpAlmTxPowerLowWarningPortn,
       "pm1004dcpAlmTxPowerHighWarningPortn": pm1004dcpAlmTxPowerHighWarningPortn,
       "pm1004dcpAlmTxBiasLowWarningPortn": pm1004dcpAlmTxBiasLowWarningPortn,
       "pm1004dcpAlmTxBiasHighWarningPortn": pm1004dcpAlmTxBiasHighWarningPortn,
       "pm1004dcpAlmTempLowWarningPortn": pm1004dcpAlmTempLowWarningPortn,
       "pm1004dcpAlmTempHighWarningPortn": pm1004dcpAlmTempHighWarningPortn,
       "pm1004dcpAlmRxPowerLowWarningPortn": pm1004dcpAlmRxPowerLowWarningPortn,
       "pm1004dcpAlmRxPowerHighWarningPortn": pm1004dcpAlmRxPowerHighWarningPortn,
       "pm1004dcpAlmlineOtx1TlhWarningsTable": pm1004dcpAlmlineOtx1TlhWarningsTable,
       "pm1004dcpAlmlineOtx1TlhWarningsEntry": pm1004dcpAlmlineOtx1TlhWarningsEntry,
       "pm1004dcpAlmlineOtx1TlhWarningsIndex": pm1004dcpAlmlineOtx1TlhWarningsIndex,
       "pm1004dcpAlmLineModulatorAgingHighWarningPortn": pm1004dcpAlmLineModulatorAgingHighWarningPortn,
       "pm1004dcpAlmLineAgingHighWarningPortn": pm1004dcpAlmLineAgingHighWarningPortn,
       "pm1004dcpAlmLineFreqDevHighWarningPortn": pm1004dcpAlmLineFreqDevHighWarningPortn,
       "pm1004dcpAlmLineLaserTempHighWarningPortn": pm1004dcpAlmLineLaserTempHighWarningPortn,
       "pm1004dcpAlmLineUrg": pm1004dcpAlmLineUrg,
       "pm1004dcpAlmdfrmBerTable": pm1004dcpAlmdfrmBerTable,
       "pm1004dcpAlmdfrmBerEntry": pm1004dcpAlmdfrmBerEntry,
       "pm1004dcpAlmdfrmBerIndex": pm1004dcpAlmdfrmBerIndex,
       "pm1004dcpAlmLineSignalDegradePortn": pm1004dcpAlmLineSignalDegradePortn,
       "pm1004dcpAlmLineSignalFailPortn": pm1004dcpAlmLineSignalFailPortn,
       "pm1004dcpAlmLineDegradePortn": pm1004dcpAlmLineDegradePortn,
       "pm1004dcpAlmlineXfp1AlarmTable": pm1004dcpAlmlineXfp1AlarmTable,
       "pm1004dcpAlmlineXfp1AlarmEntry": pm1004dcpAlmlineXfp1AlarmEntry,
       "pm1004dcpAlmlineXfp1AlarmIndex": pm1004dcpAlmlineXfp1AlarmIndex,
       "pm1004dcpAlmTxPowerLowAlarmPortn": pm1004dcpAlmTxPowerLowAlarmPortn,
       "pm1004dcpAlmTxPowerHighAlarmPortn": pm1004dcpAlmTxPowerHighAlarmPortn,
       "pm1004dcpAlmTxBiasLowAlarmPortn": pm1004dcpAlmTxBiasLowAlarmPortn,
       "pm1004dcpAlmTxBiasHighAlarmPortn": pm1004dcpAlmTxBiasHighAlarmPortn,
       "pm1004dcpAlmTempLowAlarmPortn": pm1004dcpAlmTempLowAlarmPortn,
       "pm1004dcpAlmTempHighAlarmPortn": pm1004dcpAlmTempHighAlarmPortn,
       "pm1004dcpAlmRxPowerLowAlarmPortn": pm1004dcpAlmRxPowerLowAlarmPortn,
       "pm1004dcpAlmRxPowerHighAlarmPortn": pm1004dcpAlmRxPowerHighAlarmPortn,
       "pm1004dcpAlmlineXfp1SupplyAlarmTable": pm1004dcpAlmlineXfp1SupplyAlarmTable,
       "pm1004dcpAlmlineXfp1SupplyAlarmEntry": pm1004dcpAlmlineXfp1SupplyAlarmEntry,
       "pm1004dcpAlmlineXfp1SupplyAlarmIndex": pm1004dcpAlmlineXfp1SupplyAlarmIndex,
       "pm1004dcpAlmVee5LowAlarmPortn": pm1004dcpAlmVee5LowAlarmPortn,
       "pm1004dcpAlmVee5HighAlarmPortn": pm1004dcpAlmVee5HighAlarmPortn,
       "pm1004dcpAlmVcc2LowAlarmPortn": pm1004dcpAlmVcc2LowAlarmPortn,
       "pm1004dcpAlmVcc2HighAlarmPortn": pm1004dcpAlmVcc2HighAlarmPortn,
       "pm1004dcpAlmVcc3LowAlarmPortn": pm1004dcpAlmVcc3LowAlarmPortn,
       "pm1004dcpAlmVcc3HighAlarmPortn": pm1004dcpAlmVcc3HighAlarmPortn,
       "pm1004dcpAlmVcc5LowAlarmPortn": pm1004dcpAlmVcc5LowAlarmPortn,
       "pm1004dcpAlmVcc5HighAlarmPortn": pm1004dcpAlmVcc5HighAlarmPortn,
       "pm1004dcpAlmVee5LowWarningPortn": pm1004dcpAlmVee5LowWarningPortn,
       "pm1004dcpAlmVee5HighWarningPortn": pm1004dcpAlmVee5HighWarningPortn,
       "pm1004dcpAlmVcc2LowWarningPortn": pm1004dcpAlmVcc2LowWarningPortn,
       "pm1004dcpAlmVcc2HighWarningPortn": pm1004dcpAlmVcc2HighWarningPortn,
       "pm1004dcpAlmVcc3LowWarningPortn": pm1004dcpAlmVcc3LowWarningPortn,
       "pm1004dcpAlmVcc3HighWarningPortn": pm1004dcpAlmVcc3HighWarningPortn,
       "pm1004dcpAlmVcc5LowWarningPortn": pm1004dcpAlmVcc5LowWarningPortn,
       "pm1004dcpAlmVcc5HighWarningPortn": pm1004dcpAlmVcc5HighWarningPortn,
       "pm1004dcpAlmlineOtx1TlhAlarmsTable": pm1004dcpAlmlineOtx1TlhAlarmsTable,
       "pm1004dcpAlmlineOtx1TlhAlarmsEntry": pm1004dcpAlmlineOtx1TlhAlarmsEntry,
       "pm1004dcpAlmlineOtx1TlhAlarmsIndex": pm1004dcpAlmlineOtx1TlhAlarmsIndex,
       "pm1004dcpAlmLineModulatorAgingHighAlaPortn": pm1004dcpAlmLineModulatorAgingHighAlaPortn,
       "pm1004dcpAlmLineAgingHighAlaPortn": pm1004dcpAlmLineAgingHighAlaPortn,
       "pm1004dcpAlmLineFreqDevHighAlaPortn": pm1004dcpAlmLineFreqDevHighAlaPortn,
       "pm1004dcpAlmLineLaserTempHighAlaPortn": pm1004dcpAlmLineLaserTempHighAlaPortn,
       "pm1004dcpAlmLineCrit": pm1004dcpAlmLineCrit,
       "pm1004dcpAlmsynthAlmLineTable": pm1004dcpAlmsynthAlmLineTable,
       "pm1004dcpAlmsynthAlmLineEntry": pm1004dcpAlmsynthAlmLineEntry,
       "pm1004dcpAlmsynthAlmLineIndex": pm1004dcpAlmsynthAlmLineIndex,
       "pm1004dcpAlmXfpAbsentPortn": pm1004dcpAlmXfpAbsentPortn,
       "pm1004dcpAlmXfpInitNotComplPortn": pm1004dcpAlmXfpInitNotComplPortn,
       "pm1004dcpAlmLineHwFailPortn": pm1004dcpAlmLineHwFailPortn,
       "pm1004dcpAlmXfpTxOffPortn": pm1004dcpAlmXfpTxOffPortn,
       "pm1004dcpAlmLineLocalOosPortn": pm1004dcpAlmLineLocalOosPortn,
       "pm1004dcpAlmUpRdiInsPortn": pm1004dcpAlmUpRdiInsPortn,
       "pm1004dcpAlmLineDdmWarningPortn": pm1004dcpAlmLineDdmWarningPortn,
       "pm1004dcpAlmLineDdmAlmPortn": pm1004dcpAlmLineDdmAlmPortn,
       "pm1004dcpAlmLineFailPortn": pm1004dcpAlmLineFailPortn,
       "pm1004dcpAlmdfrmAlmTable": pm1004dcpAlmdfrmAlmTable,
       "pm1004dcpAlmdfrmAlmEntry": pm1004dcpAlmdfrmAlmEntry,
       "pm1004dcpAlmdfrmAlmIndex": pm1004dcpAlmdfrmAlmIndex,
       "pm1004dcpAlmDwAisDetPortn": pm1004dcpAlmDwAisDetPortn,
       "pm1004dcpAlmDwRdiDetPortn": pm1004dcpAlmDwRdiDetPortn,
       "pm1004dcpAlmDwOofPortn": pm1004dcpAlmDwOofPortn,
       "pm1004dcpAlmDwLofPortn": pm1004dcpAlmDwLofPortn,
       "pm1004dcpAlmlineSyncAlarmsTable": pm1004dcpAlmlineSyncAlarmsTable,
       "pm1004dcpAlmlineSyncAlarmsEntry": pm1004dcpAlmlineSyncAlarmsEntry,
       "pm1004dcpAlmlineSyncAlarmsIndex": pm1004dcpAlmlineSyncAlarmsIndex,
       "pm1004dcpAlmDwLockerrPortn": pm1004dcpAlmDwLockerrPortn,
       "pm1004dcpAlmUpLockerrPortn": pm1004dcpAlmUpLockerrPortn,
       "pm1004dcpAlmDwLosPortn": pm1004dcpAlmDwLosPortn,
       "pm1004dcpAlmlineXfp1AlarmsTable": pm1004dcpAlmlineXfp1AlarmsTable,
       "pm1004dcpAlmlineXfp1AlarmsEntry": pm1004dcpAlmlineXfp1AlarmsEntry,
       "pm1004dcpAlmlineXfp1AlarmsIndex": pm1004dcpAlmlineXfp1AlarmsIndex,
       "pm1004dcpAlmModNrPortn": pm1004dcpAlmModNrPortn,
       "pm1004dcpAlmRxCdrNotLockedPortn": pm1004dcpAlmRxCdrNotLockedPortn,
       "pm1004dcpAlmRxNrPortn": pm1004dcpAlmRxNrPortn,
       "pm1004dcpAlmTxCdrNotLockedPortn": pm1004dcpAlmTxCdrNotLockedPortn,
       "pm1004dcpAlmTxFaultPortn": pm1004dcpAlmTxFaultPortn,
       "pm1004dcpAlmTxNrPortn": pm1004dcpAlmTxNrPortn,
       "pm1004dcpAlmWavelengthUnlockedPortn": pm1004dcpAlmWavelengthUnlockedPortn,
       "pm1004dcpAlmTecFaultPortn": pm1004dcpAlmTecFaultPortn,
       "pm1004dcpAlmApdSupplyFaultPortn": pm1004dcpAlmApdSupplyFaultPortn,
       "pm1004dcpmeasures": pm1004dcpmeasures,
       "pm1004dcpMesrOther": pm1004dcpMesrOther,
       "pm1004dcpMesrsynth0": pm1004dcpMesrsynth0,
       "pm1004dcpMesrsynth1": pm1004dcpMesrsynth1,
       "pm1004dcpMesrClient": pm1004dcpMesrClient,
       "pm1004dcpMesrtempMeasTable": pm1004dcpMesrtempMeasTable,
       "pm1004dcpMesrtempMeasEntry": pm1004dcpMesrtempMeasEntry,
       "pm1004dcpMesrtempMeasIndex": pm1004dcpMesrtempMeasIndex,
       "pm1004dcpMesrtempMeasPortn": pm1004dcpMesrtempMeasPortn,
       "pm1004dcpMesrvoltMeasTable": pm1004dcpMesrvoltMeasTable,
       "pm1004dcpMesrvoltMeasEntry": pm1004dcpMesrvoltMeasEntry,
       "pm1004dcpMesrvoltMeasIndex": pm1004dcpMesrvoltMeasIndex,
       "pm1004dcpMesrvoltMeasPortn": pm1004dcpMesrvoltMeasPortn,
       "pm1004dcpMesrbiasMeasTable": pm1004dcpMesrbiasMeasTable,
       "pm1004dcpMesrbiasMeasEntry": pm1004dcpMesrbiasMeasEntry,
       "pm1004dcpMesrbiasMeasIndex": pm1004dcpMesrbiasMeasIndex,
       "pm1004dcpMesrbiasMeasPortn": pm1004dcpMesrbiasMeasPortn,
       "pm1004dcpMesrtxpwrMeasTable": pm1004dcpMesrtxpwrMeasTable,
       "pm1004dcpMesrtxpwrMeasEntry": pm1004dcpMesrtxpwrMeasEntry,
       "pm1004dcpMesrtxpwrMeasIndex": pm1004dcpMesrtxpwrMeasIndex,
       "pm1004dcpMesrtxpwrMeasPortn": pm1004dcpMesrtxpwrMeasPortn,
       "pm1004dcpMesrrxpwrMeasTable": pm1004dcpMesrrxpwrMeasTable,
       "pm1004dcpMesrrxpwrMeasEntry": pm1004dcpMesrrxpwrMeasEntry,
       "pm1004dcpMesrrxpwrMeasIndex": pm1004dcpMesrrxpwrMeasIndex,
       "pm1004dcpMesrrxpwrMeasPortn": pm1004dcpMesrrxpwrMeasPortn,
       "pm1004dcpMesrLine": pm1004dcpMesrLine,
       "pm1004dcpMesrxfp1LxModTempMeasTable": pm1004dcpMesrxfp1LxModTempMeasTable,
       "pm1004dcpMesrxfp1LxModTempMeasEntry": pm1004dcpMesrxfp1LxModTempMeasEntry,
       "pm1004dcpMesrxfp1LxModTempMeasIndex": pm1004dcpMesrxfp1LxModTempMeasIndex,
       "pm1004dcpMesrxfp1LxModTempMeasPortn": pm1004dcpMesrxfp1LxModTempMeasPortn,
       "pm1004dcpMesrxfp1ReservedTable": pm1004dcpMesrxfp1ReservedTable,
       "pm1004dcpMesrxfp1ReservedEntry": pm1004dcpMesrxfp1ReservedEntry,
       "pm1004dcpMesrxfp1ReservedIndex": pm1004dcpMesrxfp1ReservedIndex,
       "pm1004dcpMesrxfp1ReservedPortn": pm1004dcpMesrxfp1ReservedPortn,
       "pm1004dcpMesrxfp1LoBiasCurrentMeasTable": pm1004dcpMesrxfp1LoBiasCurrentMeasTable,
       "pm1004dcpMesrxfp1LoBiasCurrentMeasEntry": pm1004dcpMesrxfp1LoBiasCurrentMeasEntry,
       "pm1004dcpMesrxfp1LoBiasCurrentMeasIndex": pm1004dcpMesrxfp1LoBiasCurrentMeasIndex,
       "pm1004dcpMesrxfp1LoBiasCurrentMeasPortn": pm1004dcpMesrxfp1LoBiasCurrentMeasPortn,
       "pm1004dcpMesrxfp1LoTxPowerMeasTable": pm1004dcpMesrxfp1LoTxPowerMeasTable,
       "pm1004dcpMesrxfp1LoTxPowerMeasEntry": pm1004dcpMesrxfp1LoTxPowerMeasEntry,
       "pm1004dcpMesrxfp1LoTxPowerMeasIndex": pm1004dcpMesrxfp1LoTxPowerMeasIndex,
       "pm1004dcpMesrxfp1LoTxPowerMeasPortn": pm1004dcpMesrxfp1LoTxPowerMeasPortn,
       "pm1004dcpMesrxfp1LiRxPowerMeasTable": pm1004dcpMesrxfp1LiRxPowerMeasTable,
       "pm1004dcpMesrxfp1LiRxPowerMeasEntry": pm1004dcpMesrxfp1LiRxPowerMeasEntry,
       "pm1004dcpMesrxfp1LiRxPowerMeasIndex": pm1004dcpMesrxfp1LiRxPowerMeasIndex,
       "pm1004dcpMesrxfp1LiRxPowerMeasPortn": pm1004dcpMesrxfp1LiRxPowerMeasPortn,
       "pm1004dcpMesrxfp1LxAux1MeasTable": pm1004dcpMesrxfp1LxAux1MeasTable,
       "pm1004dcpMesrxfp1LxAux1MeasEntry": pm1004dcpMesrxfp1LxAux1MeasEntry,
       "pm1004dcpMesrxfp1LxAux1MeasIndex": pm1004dcpMesrxfp1LxAux1MeasIndex,
       "pm1004dcpMesrxfp1LxAux1MeasPortn": pm1004dcpMesrxfp1LxAux1MeasPortn,
       "pm1004dcpMesrxfp1LxAux2MeasTable": pm1004dcpMesrxfp1LxAux2MeasTable,
       "pm1004dcpMesrxfp1LxAux2MeasEntry": pm1004dcpMesrxfp1LxAux2MeasEntry,
       "pm1004dcpMesrxfp1LxAux2MeasIndex": pm1004dcpMesrxfp1LxAux2MeasIndex,
       "pm1004dcpMesrxfp1LxAux2MeasPortn": pm1004dcpMesrxfp1LxAux2MeasPortn,
       "pm1004dcpMesrotx1AgingTable": pm1004dcpMesrotx1AgingTable,
       "pm1004dcpMesrotx1AgingEntry": pm1004dcpMesrotx1AgingEntry,
       "pm1004dcpMesrotx1AgingIndex": pm1004dcpMesrotx1AgingIndex,
       "pm1004dcpMesrotx1AgingPortn": pm1004dcpMesrotx1AgingPortn,
       "pm1004dcpMesrotx1LaserTemperatureTable": pm1004dcpMesrotx1LaserTemperatureTable,
       "pm1004dcpMesrotx1LaserTemperatureEntry": pm1004dcpMesrotx1LaserTemperatureEntry,
       "pm1004dcpMesrotx1LaserTemperatureIndex": pm1004dcpMesrotx1LaserTemperatureIndex,
       "pm1004dcpMesrotx1LaserTemperaturePortn": pm1004dcpMesrotx1LaserTemperaturePortn,
       "pm1004dcpMesrotx1FreqDeviationTable": pm1004dcpMesrotx1FreqDeviationTable,
       "pm1004dcpMesrotx1FreqDeviationEntry": pm1004dcpMesrotx1FreqDeviationEntry,
       "pm1004dcpMesrotx1FreqDeviationIndex": pm1004dcpMesrotx1FreqDeviationIndex,
       "pm1004dcpMesrotx1FreqDeviationPortn": pm1004dcpMesrotx1FreqDeviationPortn,
       "pm1004dcpMesrotx1LaserWvlengthTable": pm1004dcpMesrotx1LaserWvlengthTable,
       "pm1004dcpMesrotx1LaserWvlengthEntry": pm1004dcpMesrotx1LaserWvlengthEntry,
       "pm1004dcpMesrotx1LaserWvlengthIndex": pm1004dcpMesrotx1LaserWvlengthIndex,
       "pm1004dcpMesrotx1LaserWvlengthPortn": pm1004dcpMesrotx1LaserWvlengthPortn,
       "pm1004dcpcounters": pm1004dcpcounters,
       "pm1004dcpCntOther": pm1004dcpCntOther,
       "pm1004dcpCntClient": pm1004dcpCntClient,
       "pm1004dcpCntupRaRemCntTable": pm1004dcpCntupRaRemCntTable,
       "pm1004dcpCntupRaRemCntEntry": pm1004dcpCntupRaRemCntEntry,
       "pm1004dcpCntupRaRemCntIndex": pm1004dcpCntupRaRemCntIndex,
       "pm1004dcpCntupRaRemCntValuePortn": pm1004dcpCntupRaRemCntValuePortn,
       "pm1004dcpCntupRaRemCntErrorPortn": pm1004dcpCntupRaRemCntErrorPortn,
       "pm1004dcpCntupRaRemCntOverloadPortn": pm1004dcpCntupRaRemCntOverloadPortn,
       "pm1004dcpCntupRaInsCntTable": pm1004dcpCntupRaInsCntTable,
       "pm1004dcpCntupRaInsCntEntry": pm1004dcpCntupRaInsCntEntry,
       "pm1004dcpCntupRaInsCntIndex": pm1004dcpCntupRaInsCntIndex,
       "pm1004dcpCntupRaInsCntValuePortn": pm1004dcpCntupRaInsCntValuePortn,
       "pm1004dcpCntupRaInsCntErrorPortn": pm1004dcpCntupRaInsCntErrorPortn,
       "pm1004dcpCntupRaInsCntOverloadPortn": pm1004dcpCntupRaInsCntOverloadPortn,
       "pm1004dcpCntupRdErrCntTable": pm1004dcpCntupRdErrCntTable,
       "pm1004dcpCntupRdErrCntEntry": pm1004dcpCntupRdErrCntEntry,
       "pm1004dcpCntupRdErrCntIndex": pm1004dcpCntupRdErrCntIndex,
       "pm1004dcpCntupRdErrCntValuePortn": pm1004dcpCntupRdErrCntValuePortn,
       "pm1004dcpCntupRdErrCntErrorPortn": pm1004dcpCntupRdErrCntErrorPortn,
       "pm1004dcpCntupRdErrCntOverloadPortn": pm1004dcpCntupRdErrCntOverloadPortn,
       "pm1004dcpCntupTimCntTable": pm1004dcpCntupTimCntTable,
       "pm1004dcpCntupTimCntEntry": pm1004dcpCntupTimCntEntry,
       "pm1004dcpCntupTimCntIndex": pm1004dcpCntupTimCntIndex,
       "pm1004dcpCntupTimCntValuePortn": pm1004dcpCntupTimCntValuePortn,
       "pm1004dcpCntupTimCntErrorPortn": pm1004dcpCntupTimCntErrorPortn,
       "pm1004dcpCntupTimCntOverloadPortn": pm1004dcpCntupTimCntOverloadPortn,
       "pm1004dcpCntupCvErrCntTable": pm1004dcpCntupCvErrCntTable,
       "pm1004dcpCntupCvErrCntEntry": pm1004dcpCntupCvErrCntEntry,
       "pm1004dcpCntupCvErrCntIndex": pm1004dcpCntupCvErrCntIndex,
       "pm1004dcpCntupCvErrCntValuePortn": pm1004dcpCntupCvErrCntValuePortn,
       "pm1004dcpCntupCvErrCntErrorPortn": pm1004dcpCntupCvErrCntErrorPortn,
       "pm1004dcpCntupCvErrCntOverloadPortn": pm1004dcpCntupCvErrCntOverloadPortn,
       "pm1004dcpCntdwCbipCntTable": pm1004dcpCntdwCbipCntTable,
       "pm1004dcpCntdwCbipCntEntry": pm1004dcpCntdwCbipCntEntry,
       "pm1004dcpCntdwCbipCntIndex": pm1004dcpCntdwCbipCntIndex,
       "pm1004dcpCntdwCbipCntValuePortn": pm1004dcpCntdwCbipCntValuePortn,
       "pm1004dcpCntdwCbipCntErrorPortn": pm1004dcpCntdwCbipCntErrorPortn,
       "pm1004dcpCntdwCbipCntOverloadPortn": pm1004dcpCntdwCbipCntOverloadPortn,
       "pm1004dcpCntdwTimCntTable": pm1004dcpCntdwTimCntTable,
       "pm1004dcpCntdwTimCntEntry": pm1004dcpCntdwTimCntEntry,
       "pm1004dcpCntdwTimCntIndex": pm1004dcpCntdwTimCntIndex,
       "pm1004dcpCntdwTimCntValuePortn": pm1004dcpCntdwTimCntValuePortn,
       "pm1004dcpCntdwTimCntErrorPortn": pm1004dcpCntdwTimCntErrorPortn,
       "pm1004dcpCntdwTimCntOverloadPortn": pm1004dcpCntdwTimCntOverloadPortn,
       "pm1004dcpCntLine": pm1004dcpCntLine,
       "pm1004dcpCntdfrmB1ErrCntTable": pm1004dcpCntdfrmB1ErrCntTable,
       "pm1004dcpCntdfrmB1ErrCntEntry": pm1004dcpCntdfrmB1ErrCntEntry,
       "pm1004dcpCntdfrmB1ErrCntIndex": pm1004dcpCntdfrmB1ErrCntIndex,
       "pm1004dcpCntdfrmB1ErrCntValuePortn": pm1004dcpCntdfrmB1ErrCntValuePortn,
       "pm1004dcpCntdfrmB1ErrCntErrorPortn": pm1004dcpCntdfrmB1ErrCntErrorPortn,
       "pm1004dcpCntdfrmB1ErrCntOverloadPortn": pm1004dcpCntdfrmB1ErrCntOverloadPortn,
       "pm1004dcpCntdfrmTimCntTable": pm1004dcpCntdfrmTimCntTable,
       "pm1004dcpCntdfrmTimCntEntry": pm1004dcpCntdfrmTimCntEntry,
       "pm1004dcpCntdfrmTimCntIndex": pm1004dcpCntdfrmTimCntIndex,
       "pm1004dcpCntdfrmTimCntValuePortn": pm1004dcpCntdfrmTimCntValuePortn,
       "pm1004dcpCntdfrmTimCntErrorPortn": pm1004dcpCntdfrmTimCntErrorPortn,
       "pm1004dcpCntdfrmTimCntOverloadPortn": pm1004dcpCntdfrmTimCntOverloadPortn,
       "pm1004dcpCntdfrmPrimLineErrCntTable": pm1004dcpCntdfrmPrimLineErrCntTable,
       "pm1004dcpCntdfrmPrimLineErrCntEntry": pm1004dcpCntdfrmPrimLineErrCntEntry,
       "pm1004dcpCntdfrmPrimLineErrCntIndex": pm1004dcpCntdfrmPrimLineErrCntIndex,
       "pm1004dcpCntdfrmPrimLineErrCntValuePortn": pm1004dcpCntdfrmPrimLineErrCntValuePortn,
       "pm1004dcpCntdfrmPrimLineErrCntErrorPortn": pm1004dcpCntdfrmPrimLineErrCntErrorPortn,
       "pm1004dcpCntdfrmPrimLineErrCntOverloadPortn": pm1004dcpCntdfrmPrimLineErrCntOverloadPortn,
       "pm1004dcpCntCountersReset": pm1004dcpCntCountersReset,
       "pm1004dcpCntCountersStop": pm1004dcpCntCountersStop,
       "pm1004dcpcontrolsWrite": pm1004dcpcontrolsWrite,
       "pm1004dcpCtrlOther": pm1004dcpCtrlOther,
       "pm1004dcpCtrlconfMgnt1": pm1004dcpCtrlconfMgnt1,
       "pm1004dcpCtrlConf1Load1": pm1004dcpCtrlConf1Load1,
       "pm1004dcpCtrlConf2Load1": pm1004dcpCtrlConf2Load1,
       "pm1004dcpCtrlConf2Flash1": pm1004dcpCtrlConf2Flash1,
       "pm1004dcpCtrlConf2Clear1": pm1004dcpCtrlConf2Clear1,
       "pm1004dcpCtrlsynth4": pm1004dcpCtrlsynth4,
       "pm1004dcpCtrlCorrelatOn": pm1004dcpCtrlCorrelatOn,
       "pm1004dcpCtrlCorrelatOff": pm1004dcpCtrlCorrelatOff,
       "pm1004dcpCtrlswMgnt": pm1004dcpCtrlswMgnt,
       "pm1004dcpCtrlColdReset": pm1004dcpCtrlColdReset,
       "pm1004dcpCtrlWarmReset": pm1004dcpCtrlWarmReset,
       "pm1004dcpCtrlLoadSwBank1": pm1004dcpCtrlLoadSwBank1,
       "pm1004dcpCtrlLoadSwBank2": pm1004dcpCtrlLoadSwBank2,
       "pm1004dcpCtrlgwMgnt": pm1004dcpCtrlgwMgnt,
       "pm1004dcpCtrlCurrentGwReset": pm1004dcpCtrlCurrentGwReset,
       "pm1004dcpCtrlLoadGwBank1": pm1004dcpCtrlLoadGwBank1,
       "pm1004dcpCtrlLoadGwBank2": pm1004dcpCtrlLoadGwBank2,
       "pm1004dcpCtrlLoadGwBank3": pm1004dcpCtrlLoadGwBank3,
       "pm1004dcpCtrlLoadGwBank4": pm1004dcpCtrlLoadGwBank4,
       "pm1004dcpCtrlledTest": pm1004dcpCtrlledTest,
       "pm1004dcpCtrlGreenLed": pm1004dcpCtrlGreenLed,
       "pm1004dcpCtrlRedLed": pm1004dcpCtrlRedLed,
       "pm1004dcpCtrlLedOff": pm1004dcpCtrlLedOff,
       "pm1004dcpCtrlmoduleOosMode": pm1004dcpCtrlmoduleOosMode,
       "pm1004dcpCtrlModuleOosMode": pm1004dcpCtrlModuleOosMode,
       "pm1004dcpCtrlmoduleDccMgnt": pm1004dcpCtrlmoduleDccMgnt,
       "pm1004dcpCtrlmaintenanceMode": pm1004dcpCtrlmaintenanceMode,
       "pm1004dcpCtrlMaintenanceMode": pm1004dcpCtrlMaintenanceMode,
       "pm1004dcpCtrlClient": pm1004dcpCtrlClient,
       "pm1004dcpCtrlaccessLoopTable": pm1004dcpCtrlaccessLoopTable,
       "pm1004dcpCtrlaccessLoopEntry": pm1004dcpCtrlaccessLoopEntry,
       "pm1004dcpCtrlaccessLoopIndex": pm1004dcpCtrlaccessLoopIndex,
       "pm1004dcpCtrlaccessLoopPortn": pm1004dcpCtrlaccessLoopPortn,
       "pm1004dcpCtrlportOosModeTable": pm1004dcpCtrlportOosModeTable,
       "pm1004dcpCtrlportOosModeEntry": pm1004dcpCtrlportOosModeEntry,
       "pm1004dcpCtrlportOosModeIndex": pm1004dcpCtrlportOosModeIndex,
       "pm1004dcpCtrlportOosModePortn": pm1004dcpCtrlportOosModePortn,
       "pm1004dcpCtrlsfpOnCtrlTable": pm1004dcpCtrlsfpOnCtrlTable,
       "pm1004dcpCtrlsfpOnCtrlEntry": pm1004dcpCtrlsfpOnCtrlEntry,
       "pm1004dcpCtrlsfpOnCtrlIndex": pm1004dcpCtrlsfpOnCtrlIndex,
       "pm1004dcpCtrlsfpOnCtrlPortn": pm1004dcpCtrlsfpOnCtrlPortn,
       "pm1004dcpCtrlsfpOffCtrlTable": pm1004dcpCtrlsfpOffCtrlTable,
       "pm1004dcpCtrlsfpOffCtrlEntry": pm1004dcpCtrlsfpOffCtrlEntry,
       "pm1004dcpCtrlsfpOffCtrlIndex": pm1004dcpCtrlsfpOffCtrlIndex,
       "pm1004dcpCtrlsfpOffCtrlPortn": pm1004dcpCtrlsfpOffCtrlPortn,
       "pm1004dcpCtrlcsfUpInsTable": pm1004dcpCtrlcsfUpInsTable,
       "pm1004dcpCtrlcsfUpInsEntry": pm1004dcpCtrlcsfUpInsEntry,
       "pm1004dcpCtrlcsfUpInsIndex": pm1004dcpCtrlcsfUpInsIndex,
       "pm1004dcpCtrlcsfUpInsPortn": pm1004dcpCtrlcsfUpInsPortn,
       "pm1004dcpCtrlcaisDwInsTable": pm1004dcpCtrlcaisDwInsTable,
       "pm1004dcpCtrlcaisDwInsEntry": pm1004dcpCtrlcaisDwInsEntry,
       "pm1004dcpCtrlcaisDwInsIndex": pm1004dcpCtrlcaisDwInsIndex,
       "pm1004dcpCtrlcaisDwInsPortn": pm1004dcpCtrlcaisDwInsPortn,
       "pm1004dcpCtrlclientAccessTermLoopTable": pm1004dcpCtrlclientAccessTermLoopTable,
       "pm1004dcpCtrlclientAccessTermLoopEntry": pm1004dcpCtrlclientAccessTermLoopEntry,
       "pm1004dcpCtrlclientAccessTermLoopIndex": pm1004dcpCtrlclientAccessTermLoopIndex,
       "pm1004dcpCtrlclientAccessTermLoopPortn": pm1004dcpCtrlclientAccessTermLoopPortn,
       "pm1004dcpCtrlresetCount15PortTable": pm1004dcpCtrlresetCount15PortTable,
       "pm1004dcpCtrlresetCount15PortEntry": pm1004dcpCtrlresetCount15PortEntry,
       "pm1004dcpCtrlresetCount15PortIndex": pm1004dcpCtrlresetCount15PortIndex,
       "pm1004dcpCtrlclientResetAllPerfCount15Portn": pm1004dcpCtrlclientResetAllPerfCount15Portn,
       "pm1004dcpCtrlresetCount24PortTable": pm1004dcpCtrlresetCount24PortTable,
       "pm1004dcpCtrlresetCount24PortEntry": pm1004dcpCtrlresetCount24PortEntry,
       "pm1004dcpCtrlresetCount24PortIndex": pm1004dcpCtrlresetCount24PortIndex,
       "pm1004dcpCtrlclientResetAllPerfCount24Portn": pm1004dcpCtrlclientResetAllPerfCount24Portn,
       "pm1004dcpCtrladddropTsClientARxProtectTable": pm1004dcpCtrladddropTsClientARxProtectTable,
       "pm1004dcpCtrladddropTsClientARxProtectEntry": pm1004dcpCtrladddropTsClientARxProtectEntry,
       "pm1004dcpCtrladddropTsClientARxProtectIndex": pm1004dcpCtrladddropTsClientARxProtectIndex,
       "pm1004dcpCtrladddropTsClientARxProtectPortn": pm1004dcpCtrladddropTsClientARxProtectPortn,
       "pm1004dcpCtrladddropTsPairModeTable": pm1004dcpCtrladddropTsPairModeTable,
       "pm1004dcpCtrladddropTsPairModeEntry": pm1004dcpCtrladddropTsPairModeEntry,
       "pm1004dcpCtrladddropTsPairModeIndex": pm1004dcpCtrladddropTsPairModeIndex,
       "pm1004dcpCtrladddropTsPairModePortn": pm1004dcpCtrladddropTsPairModePortn,
       "pm1004dcpCtrlLine": pm1004dcpCtrlLine,
       "pm1004dcpCtrlcommAccessLoop": pm1004dcpCtrlcommAccessLoop,
       "pm1004dcpCtrlCommAccessloop": pm1004dcpCtrlCommAccessloop,
       "pm1004dcpCtrllineLoop": pm1004dcpCtrllineLoop,
       "pm1004dcpCtrlLineLoop": pm1004dcpCtrlLineLoop,
       "pm1004dcpCtrlmsAis": pm1004dcpCtrlmsAis,
       "pm1004dcpCtrlMsAis": pm1004dcpCtrlMsAis,
       "pm1004dcpCtrlfecDisableTable": pm1004dcpCtrlfecDisableTable,
       "pm1004dcpCtrlfecDisableEntry": pm1004dcpCtrlfecDisableEntry,
       "pm1004dcpCtrlfecDisableIndex": pm1004dcpCtrlfecDisableIndex,
       "pm1004dcpCtrlfecDisablePortn": pm1004dcpCtrlfecDisablePortn,
       "pm1004dcpCtrllineOosModeTable": pm1004dcpCtrllineOosModeTable,
       "pm1004dcpCtrllineOosModeEntry": pm1004dcpCtrllineOosModeEntry,
       "pm1004dcpCtrllineOosModeIndex": pm1004dcpCtrllineOosModeIndex,
       "pm1004dcpCtrllineOosModePortn": pm1004dcpCtrllineOosModePortn,
       "pm1004dcpCtrllineResetCount15LineTable": pm1004dcpCtrllineResetCount15LineTable,
       "pm1004dcpCtrllineResetCount15LineEntry": pm1004dcpCtrllineResetCount15LineEntry,
       "pm1004dcpCtrllineResetCount15LineIndex": pm1004dcpCtrllineResetCount15LineIndex,
       "pm1004dcpCtrlresetAllPerfCount15Portn": pm1004dcpCtrlresetAllPerfCount15Portn,
       "pm1004dcpCtrllineResetCount24LineTable": pm1004dcpCtrllineResetCount24LineTable,
       "pm1004dcpCtrllineResetCount24LineEntry": pm1004dcpCtrllineResetCount24LineEntry,
       "pm1004dcpCtrllineResetCount24LineIndex": pm1004dcpCtrllineResetCount24LineIndex,
       "pm1004dcpCtrlresetAllPerfCount24Portn": pm1004dcpCtrlresetAllPerfCount24Portn,
       "pm1004dcpCtrlxfpOnoffTable": pm1004dcpCtrlxfpOnoffTable,
       "pm1004dcpCtrlxfpOnoffEntry": pm1004dcpCtrlxfpOnoffEntry,
       "pm1004dcpCtrlxfpOnoffIndex": pm1004dcpCtrlxfpOnoffIndex,
       "pm1004dcpCtrlxfpOnoffPortn": pm1004dcpCtrlxfpOnoffPortn,
       "pm1004dcpCtrlxfpLineLoopTable": pm1004dcpCtrlxfpLineLoopTable,
       "pm1004dcpCtrlxfpLineLoopEntry": pm1004dcpCtrlxfpLineLoopEntry,
       "pm1004dcpCtrlxfpLineLoopIndex": pm1004dcpCtrlxfpLineLoopIndex,
       "pm1004dcpCtrlxfpLineLoopPortn": pm1004dcpCtrlxfpLineLoopPortn,
       "pm1004dcpCtrlxfpXfiLoopTable": pm1004dcpCtrlxfpXfiLoopTable,
       "pm1004dcpCtrlxfpXfiLoopEntry": pm1004dcpCtrlxfpXfiLoopEntry,
       "pm1004dcpCtrlxfpXfiLoopIndex": pm1004dcpCtrlxfpXfiLoopIndex,
       "pm1004dcpCtrlxfpXfiLoopPortn": pm1004dcpCtrlxfpXfiLoopPortn,
       "pm1004dcpCtrllineTunableChannelTable": pm1004dcpCtrllineTunableChannelTable,
       "pm1004dcpCtrllineTunableChannelEntry": pm1004dcpCtrllineTunableChannelEntry,
       "pm1004dcpCtrllineTunableChannelIndex": pm1004dcpCtrllineTunableChannelIndex,
       "pm1004dcpCtrllineTunableChannelPortn": pm1004dcpCtrllineTunableChannelPortn,
       "pm1004dcpCtrllinePhotodiodeModeTable": pm1004dcpCtrllinePhotodiodeModeTable,
       "pm1004dcpCtrllinePhotodiodeModeEntry": pm1004dcpCtrllinePhotodiodeModeEntry,
       "pm1004dcpCtrllinePhotodiodeModeIndex": pm1004dcpCtrllinePhotodiodeModeIndex,
       "pm1004dcpCtrllinePhotodiodeModePortn": pm1004dcpCtrllinePhotodiodeModePortn,
       "pm1004dcpCtrllinePhotodiodeValueTable": pm1004dcpCtrllinePhotodiodeValueTable,
       "pm1004dcpCtrllinePhotodiodeValueEntry": pm1004dcpCtrllinePhotodiodeValueEntry,
       "pm1004dcpCtrllinePhotodiodeValueIndex": pm1004dcpCtrllinePhotodiodeValueIndex,
       "pm1004dcpCtrllinePhotodiodeValuePortn": pm1004dcpCtrllinePhotodiodeValuePortn,
       "pm1004dcpCtrllinePowerLaserTable": pm1004dcpCtrllinePowerLaserTable,
       "pm1004dcpCtrllinePowerLaserEntry": pm1004dcpCtrllinePowerLaserEntry,
       "pm1004dcpCtrllinePowerLaserIndex": pm1004dcpCtrllinePowerLaserIndex,
       "pm1004dcpCtrllinePowerLaserPortn": pm1004dcpCtrllinePowerLaserPortn,
       "pm1004dcpri": pm1004dcpri,
       "pm1004dcpriTable": pm1004dcpriTable,
       "pm1004dcpRinvSfpTable": pm1004dcpRinvSfpTable,
       "pm1004dcpRinvSfpEntry": pm1004dcpRinvSfpEntry,
       "pm1004dcpRinvSfpIndex": pm1004dcpRinvSfpIndex,
       "pm1004dcpRinvsfp": pm1004dcpRinvsfp,
       "pm1004dcpRinvLineTable": pm1004dcpRinvLineTable,
       "pm1004dcpRinvLineEntry": pm1004dcpRinvLineEntry,
       "pm1004dcpRinvLineIndex": pm1004dcpRinvLineIndex,
       "pm1004dcpRinvxfpLine": pm1004dcpRinvxfpLine,
       "pm1004dcpRinvReloadInventory": pm1004dcpRinvReloadInventory,
       "pm1004dcpRinvHwPlatform": pm1004dcpRinvHwPlatform,
       "pm1004dcpRinvModulePlatform": pm1004dcpRinvModulePlatform,
       "pm1004dcpRinvSwPlatform": pm1004dcpRinvSwPlatform,
       "pm1004dcpRinvGwPlatform": pm1004dcpRinvGwPlatform,
       "pm1004dcpdownload": pm1004dcpdownload,
       "pm1004dcpDwlOther": pm1004dcpDwlOther,
       "pm1004dcpDwlrestartProcess": pm1004dcpDwlrestartProcess,
       "pm1004dcpDwlWarmRestartProcessed": pm1004dcpDwlWarmRestartProcessed,
       "pm1004dcpDwlColdRestartProcessed": pm1004dcpDwlColdRestartProcessed,
       "pm1004dcpDwlswBanksUsed": pm1004dcpDwlswBanksUsed,
       "pm1004dcpDwlSwBank1Used": pm1004dcpDwlSwBank1Used,
       "pm1004dcpDwlSwBank2Used": pm1004dcpDwlSwBank2Used,
       "pm1004dcpDwlSwBank1Notempty": pm1004dcpDwlSwBank1Notempty,
       "pm1004dcpDwlSwBank2Notempty": pm1004dcpDwlSwBank2Notempty,
       "pm1004dcpDwlgwBanksUsed": pm1004dcpDwlgwBanksUsed,
       "pm1004dcpDwlGwBank1Used": pm1004dcpDwlGwBank1Used,
       "pm1004dcpDwlGwBank2Used": pm1004dcpDwlGwBank2Used,
       "pm1004dcpDwlGwBank3Used": pm1004dcpDwlGwBank3Used,
       "pm1004dcpDwlGwBank4Used": pm1004dcpDwlGwBank4Used,
       "pm1004dcpDwlGwBank1Notempty": pm1004dcpDwlGwBank1Notempty,
       "pm1004dcpDwlGwBank2Notempty": pm1004dcpDwlGwBank2Notempty,
       "pm1004dcpDwlGwBank3Notempty": pm1004dcpDwlGwBank3Notempty,
       "pm1004dcpDwlGwBank4Notempty": pm1004dcpDwlGwBank4Notempty,
       "pm1004dcpDwlClient": pm1004dcpDwlClient,
       "pm1004dcpDwlLine": pm1004dcpDwlLine,
       "pm1004dcpConfig": pm1004dcpConfig,
       "pm1004dcpCfgAccessCAisCsf": pm1004dcpCfgAccessCAisCsf,
       "pm1004dcpCfgClientcaiscsfTable": pm1004dcpCfgClientcaiscsfTable,
       "pm1004dcpCfgClientcaiscsfEntry": pm1004dcpCfgClientcaiscsfEntry,
       "pm1004dcpCfgClientcaiscsfIndex": pm1004dcpCfgClientcaiscsfIndex,
       "pm1004dcpCfgCAisModePortn": pm1004dcpCfgCAisModePortn,
       "pm1004dcpCfgUpAccessioAlmPortn": pm1004dcpCfgUpAccessioAlmPortn,
       "pm1004dcpCfgUpMapperDeAlmPortn": pm1004dcpCfgUpMapperDeAlmPortn,
       "pm1004dcpCfgUpAccessioSdhAlmPortn": pm1004dcpCfgUpAccessioSdhAlmPortn,
       "pm1004dcpCfgDownAccessioAlmPortn": pm1004dcpCfgDownAccessioAlmPortn,
       "pm1004dcpCfgDownMapperDeAlmPortn": pm1004dcpCfgDownMapperDeAlmPortn,
       "pm1004dcpCfgDownDfrmAlmPortn": pm1004dcpCfgDownDfrmAlmPortn,
       "pm1004dcpCfgDownLineSyncAlarmsPortn": pm1004dcpCfgDownLineSyncAlarmsPortn,
       "pm1004dcpCfgDownAccessioSdhAlmPortn": pm1004dcpCfgDownAccessioSdhAlmPortn,
       "pm1004dcpCfgStartup": pm1004dcpCfgStartup,
       "pm1004dcpCfgClientStartupTable": pm1004dcpCfgClientStartupTable,
       "pm1004dcpCfgClientStartupEntry": pm1004dcpCfgClientStartupEntry,
       "pm1004dcpCfgClientStartupIndex": pm1004dcpCfgClientStartupIndex,
       "pm1004dcpCfgSystConfPortPortn": pm1004dcpCfgSystConfPortPortn,
       "pm1004dcpCfgNetConfPortPortn": pm1004dcpCfgNetConfPortPortn,
       "pm1004dcpCfgAdddropConfPortPortn": pm1004dcpCfgAdddropConfPortPortn,
       "pm1004dcptablelineStartup": pm1004dcptablelineStartup,
       "pm1004dcpCfgsystConfLine1": pm1004dcpCfgsystConfLine1,
       "pm1004dcpCfglineOptions1": pm1004dcpCfglineOptions1,
       "pm1004dcpCfgsystConfLine2": pm1004dcpCfgsystConfLine2,
       "pm1004dcpCfglineSelection": pm1004dcpCfglineSelection,
       "pm1004dcpCfglineOptions2": pm1004dcpCfglineOptions2,
       "pm1004dcpCfgXfpTable": pm1004dcpCfgXfpTable,
       "pm1004dcpCfgXfpEntry": pm1004dcpCfgXfpEntry,
       "pm1004dcpCfgXfpIndex": pm1004dcpCfgXfpIndex,
       "pm1004dcpCfgSystConfXfpPortn": pm1004dcpCfgSystConfXfpPortn,
       "pm1004dcpCfgDataRateConfXfpPortn": pm1004dcpCfgDataRateConfXfpPortn,
       "pm1004dcpCfgModPerfConfig": pm1004dcpCfgModPerfConfig,
       "pm1004dcptablemodPerfConfig": pm1004dcptablemodPerfConfig,
       "pm1004dcpCfgperfMode": pm1004dcpCfgperfMode,
       "pm1004dcpCfgJ0Client": pm1004dcpCfgJ0Client,
       "pm1004dcpCfgEmptyTable": pm1004dcpCfgEmptyTable,
       "pm1004dcpCfgEmptyEntry": pm1004dcpCfgEmptyEntry,
       "pm1004dcpCfgEmptyIndex": pm1004dcpCfgEmptyIndex,
       "pm1004dcpCfgClientExpectJ0SetupPortn": pm1004dcpCfgClientExpectJ0SetupPortn,
       "pm1004dcpCfgLabels": pm1004dcpCfgLabels,
       "pm1004dcpCfgLabelclientTable": pm1004dcpCfgLabelclientTable,
       "pm1004dcpCfgLabelclientEntry": pm1004dcpCfgLabelclientEntry,
       "pm1004dcpCfgLabelclientIndex": pm1004dcpCfgLabelclientIndex,
       "pm1004dcpCfgLabelclientPortn": pm1004dcpCfgLabelclientPortn,
       "pm1004dcpCfgLabellineTable": pm1004dcpCfgLabellineTable,
       "pm1004dcpCfgLabellineEntry": pm1004dcpCfgLabellineEntry,
       "pm1004dcpCfgLabellineIndex": pm1004dcpCfgLabellineIndex,
       "pm1004dcpCfgLabellinePortn": pm1004dcpCfgLabellinePortn,
       "pm1004dcpCfgStartuptlh": pm1004dcpCfgStartuptlh,
       "pm1004dcpCfgOtxtlhTable": pm1004dcpCfgOtxtlhTable,
       "pm1004dcpCfgOtxtlhEntry": pm1004dcpCfgOtxtlhEntry,
       "pm1004dcpCfgOtxtlhIndex": pm1004dcpCfgOtxtlhIndex,
       "pm1004dcpCfgNuPortn": pm1004dcpCfgNuPortn,
       "pm1004dcpCfgLineDitherRatePortn": pm1004dcpCfgLineDitherRatePortn,
       "pm1004dcpCfgLineDitherFhzPortn": pm1004dcpCfgLineDitherFhzPortn,
       "pm1004dcpCfgLinePwrLaserPortn": pm1004dcpCfgLinePwrLaserPortn,
       "pm1004dcpCfgLineFCurrentPortn": pm1004dcpCfgLineFCurrentPortn,
       "pm1004dcpCfgLineGridCurrentPortn": pm1004dcpCfgLineGridCurrentPortn,
       "pm1004dcpCfgFPortn": pm1004dcpCfgFPortn,
       "pm1004dcpCfgReservedPortn": pm1004dcpCfgReservedPortn,
       "pm1004dcpCfgLinePhotodiodeModePortn": pm1004dcpCfgLinePhotodiodeModePortn,
       "pm1004dcpCfgLinePhotodiodeValuePortn": pm1004dcpCfgLinePhotodiodeValuePortn,
       "pm1004dcpCfgOther": pm1004dcpCfgOther,
       "pm1004dcptablemoduleOther": pm1004dcptablemoduleOther,
       "pm1004dcpCfgmode": pm1004dcpCfgmode,
       "pm1004dcpCfgadddropTsPairMode1": pm1004dcpCfgadddropTsPairMode1,
       "pm1004dcpCfgadddropTsPairMode2": pm1004dcpCfgadddropTsPairMode2,
       "pm1004dcpCfgadddropTsPairMode3": pm1004dcpCfgadddropTsPairMode3,
       "pm1004dcpCfgadddropTsPairMode4": pm1004dcpCfgadddropTsPairMode4,
       "pm1004dcpCfgStartuptablefive": pm1004dcpCfgStartuptablefive,
       "pm1004dcpCfgOtxtlhcapabilitiesTable": pm1004dcpCfgOtxtlhcapabilitiesTable,
       "pm1004dcpCfgOtxtlhcapabilitiesEntry": pm1004dcpCfgOtxtlhcapabilitiesEntry,
       "pm1004dcpCfgOtxtlhcapabilitiesIndex": pm1004dcpCfgOtxtlhcapabilitiesIndex,
       "pm1004dcpCfgComponentTypePortn": pm1004dcpCfgComponentTypePortn,
       "pm1004dcpCfgMiscellaneousPortn": pm1004dcpCfgMiscellaneousPortn,
       "pm1004dcpCfgFirstChannelPortn": pm1004dcpCfgFirstChannelPortn,
       "pm1004dcpCfgLastChannelPortn": pm1004dcpCfgLastChannelPortn,
       "pm1004dcpCfgGridPortn": pm1004dcpCfgGridPortn,
       "pm1004dcpCfgWriteConfiguration": pm1004dcpCfgWriteConfiguration,
       "pm1004dcptraps": pm1004dcptraps,
       "pm1004dcptrapPortNumber": pm1004dcptrapPortNumber,
       "pm1004dcptrapLineNumber": pm1004dcptrapLineNumber,
       "pm1004dcptrapBoardNumber": pm1004dcptrapBoardNumber,
       "pm1004dcpLineTrapNotUrgentGoesOn": pm1004dcpLineTrapNotUrgentGoesOn,
       "pm1004dcpLineTrapNotUrgentGoesOff": pm1004dcpLineTrapNotUrgentGoesOff,
       "pm1004dcpLineTrapUrgentGoesOn": pm1004dcpLineTrapUrgentGoesOn,
       "pm1004dcpLineTrapUrgentGoesOff": pm1004dcpLineTrapUrgentGoesOff,
       "pm1004dcpLineTrapCritGoesOn": pm1004dcpLineTrapCritGoesOn,
       "pm1004dcpLineTrapCritGoesOff": pm1004dcpLineTrapCritGoesOff,
       "pm1004dcpClientTrapNotUrgentGoesOn": pm1004dcpClientTrapNotUrgentGoesOn,
       "pm1004dcpClientTrapNotUrgentGoesOff": pm1004dcpClientTrapNotUrgentGoesOff,
       "pm1004dcpClientTrapUrgentGoesOn": pm1004dcpClientTrapUrgentGoesOn,
       "pm1004dcpClientTrapUrgentGoesOff": pm1004dcpClientTrapUrgentGoesOff,
       "pm1004dcpClientTrapCritGoesOn": pm1004dcpClientTrapCritGoesOn,
       "pm1004dcpClientTrapCritGoesOff": pm1004dcpClientTrapCritGoesOff,
       "pm1004dcpPowerTrapUrgentGoesOn": pm1004dcpPowerTrapUrgentGoesOn,
       "pm1004dcpPowerTrapUrgentGoesOff": pm1004dcpPowerTrapUrgentGoesOff,
       "pm1004dcpMonitoring": pm1004dcpMonitoring,
       "pm1004dcpMonOther": pm1004dcpMonOther,
       "pm1004dcpMonSync": pm1004dcpMonSync,
       "pm1004dcpPerfEnable": pm1004dcpPerfEnable,
       "pm1004dcpPerfSyncSource": pm1004dcpPerfSyncSource,
       "pm1004dcpPerf15minSync": pm1004dcpPerf15minSync,
       "pm1004dcpPerf24hSync": pm1004dcpPerf24hSync,
       "pm1004dcpMonTimeStamp": pm1004dcpMonTimeStamp,
       "pm1004dcpPerfCurrent15MinElapsedTime": pm1004dcpPerfCurrent15MinElapsedTime,
       "pm1004dcpPerfCurrent24HoursElapsedTime": pm1004dcpPerfCurrent24HoursElapsedTime,
       "pm1004dcpPerfPast15MinElapsedTime": pm1004dcpPerfPast15MinElapsedTime,
       "pm1004dcpPerfPast24HoursElapsedTime": pm1004dcpPerfPast24HoursElapsedTime,
       "pm1004dcpMonClient": pm1004dcpMonClient,
       "pm1004dcpMonClientPerformance": pm1004dcpMonClientPerformance,
       "pm1004dcpPerfUpCurrent15CntTable": pm1004dcpPerfUpCurrent15CntTable,
       "pm1004dcpPerfUpCurrent15CntEntry": pm1004dcpPerfUpCurrent15CntEntry,
       "pm1004dcpPerfUpCurrent15CntIndex": pm1004dcpPerfUpCurrent15CntIndex,
       "pm1004dcpPerfUpCurrent15CntInvCvPortn": pm1004dcpPerfUpCurrent15CntInvCvPortn,
       "pm1004dcpPerfUpCurrent15CntCvValuePortn": pm1004dcpPerfUpCurrent15CntCvValuePortn,
       "pm1004dcpPerfUpCurrent15CntInvEsPortn": pm1004dcpPerfUpCurrent15CntInvEsPortn,
       "pm1004dcpPerfUpCurrent15CntEsValuePortn": pm1004dcpPerfUpCurrent15CntEsValuePortn,
       "pm1004dcpPerfUpCurrent15CntInvSesPortn": pm1004dcpPerfUpCurrent15CntInvSesPortn,
       "pm1004dcpPerfUpCurrent15CntSesValuePortn": pm1004dcpPerfUpCurrent15CntSesValuePortn,
       "pm1004dcpPerfUpCurrent15CntInvSefsPortn": pm1004dcpPerfUpCurrent15CntInvSefsPortn,
       "pm1004dcpPerfUpCurrent15CntSefsValuePortn": pm1004dcpPerfUpCurrent15CntSefsValuePortn,
       "pm1004dcpPerfUpCurrent15CntInvUasPortn": pm1004dcpPerfUpCurrent15CntInvUasPortn,
       "pm1004dcpPerfUpCurrent15CntUasValuePortn": pm1004dcpPerfUpCurrent15CntUasValuePortn,
       "pm1004dcpPerfUpPast15CntTable": pm1004dcpPerfUpPast15CntTable,
       "pm1004dcpPerfUpPast15CntEntry": pm1004dcpPerfUpPast15CntEntry,
       "pm1004dcpPerfUpPast15CntIndex": pm1004dcpPerfUpPast15CntIndex,
       "pm1004dcpPerfUpPast15CntInvCvPortn": pm1004dcpPerfUpPast15CntInvCvPortn,
       "pm1004dcpPerfUpPast15CntCvValuePortn": pm1004dcpPerfUpPast15CntCvValuePortn,
       "pm1004dcpPerfUpPast15CntInvEsPortn": pm1004dcpPerfUpPast15CntInvEsPortn,
       "pm1004dcpPerfUpPast15CntEsValuePortn": pm1004dcpPerfUpPast15CntEsValuePortn,
       "pm1004dcpPerfUpPast15CntInvSesPortn": pm1004dcpPerfUpPast15CntInvSesPortn,
       "pm1004dcpPerfUpPast15CntSesValuePortn": pm1004dcpPerfUpPast15CntSesValuePortn,
       "pm1004dcpPerfUpPast15CntInvSefsPortn": pm1004dcpPerfUpPast15CntInvSefsPortn,
       "pm1004dcpPerfUpPast15CntSefsValuePortn": pm1004dcpPerfUpPast15CntSefsValuePortn,
       "pm1004dcpPerfUpPast15CntInvUasPortn": pm1004dcpPerfUpPast15CntInvUasPortn,
       "pm1004dcpPerfUpPast15CntUasValuePortn": pm1004dcpPerfUpPast15CntUasValuePortn,
       "pm1004dcpPerfUpCurrent24CntTable": pm1004dcpPerfUpCurrent24CntTable,
       "pm1004dcpPerfUpCurrent24CntEntry": pm1004dcpPerfUpCurrent24CntEntry,
       "pm1004dcpPerfUpCurrent24CntIndex": pm1004dcpPerfUpCurrent24CntIndex,
       "pm1004dcpPerfUpCurrent24CntInvCvPortn": pm1004dcpPerfUpCurrent24CntInvCvPortn,
       "pm1004dcpPerfUpCurrent24CntCvValuePortn": pm1004dcpPerfUpCurrent24CntCvValuePortn,
       "pm1004dcpPerfUpCurrent24CntInvEsPortn": pm1004dcpPerfUpCurrent24CntInvEsPortn,
       "pm1004dcpPerfUpCurrent24CntEsValuePortn": pm1004dcpPerfUpCurrent24CntEsValuePortn,
       "pm1004dcpPerfUpCurrent24CntInvSesPortn": pm1004dcpPerfUpCurrent24CntInvSesPortn,
       "pm1004dcpPerfUpCurrent24CntSesValuePortn": pm1004dcpPerfUpCurrent24CntSesValuePortn,
       "pm1004dcpPerfUpCurrent24CntInvSefsPortn": pm1004dcpPerfUpCurrent24CntInvSefsPortn,
       "pm1004dcpPerfUpCurrent24CntSefsValuePortn": pm1004dcpPerfUpCurrent24CntSefsValuePortn,
       "pm1004dcpPerfUpCurrent24CntInvUasPortn": pm1004dcpPerfUpCurrent24CntInvUasPortn,
       "pm1004dcpPerfUpCurrent24CntUasValuePortn": pm1004dcpPerfUpCurrent24CntUasValuePortn,
       "pm1004dcpPerfUpPast24CntTable": pm1004dcpPerfUpPast24CntTable,
       "pm1004dcpPerfUpPast24CntEntry": pm1004dcpPerfUpPast24CntEntry,
       "pm1004dcpPerfUpPast24CntIndex": pm1004dcpPerfUpPast24CntIndex,
       "pm1004dcpPerfUpPast24CntInvCvPortn": pm1004dcpPerfUpPast24CntInvCvPortn,
       "pm1004dcpPerfUpPast24CntCvValuePortn": pm1004dcpPerfUpPast24CntCvValuePortn,
       "pm1004dcpPerfUpPast24CntInvEsPortn": pm1004dcpPerfUpPast24CntInvEsPortn,
       "pm1004dcpPerfUpPast24CntEsValuePortn": pm1004dcpPerfUpPast24CntEsValuePortn,
       "pm1004dcpPerfUpPast24CntInvSesPortn": pm1004dcpPerfUpPast24CntInvSesPortn,
       "pm1004dcpPerfUpPast24CntSesValuePortn": pm1004dcpPerfUpPast24CntSesValuePortn,
       "pm1004dcpPerfUpPast24CntInvSefsPortn": pm1004dcpPerfUpPast24CntInvSefsPortn,
       "pm1004dcpPerfUpPast24CntSefsValuePortn": pm1004dcpPerfUpPast24CntSefsValuePortn,
       "pm1004dcpPerfUpPast24CntInvUasPortn": pm1004dcpPerfUpPast24CntInvUasPortn,
       "pm1004dcpPerfUpPast24CntUasValuePortn": pm1004dcpPerfUpPast24CntUasValuePortn,
       "pm1004dcpMonClientTraceIdentifier": pm1004dcpMonClientTraceIdentifier,
       "pm1004dcpAlmj0AlarmTable": pm1004dcpAlmj0AlarmTable,
       "pm1004dcpAlmj0AlarmEntry": pm1004dcpAlmj0AlarmEntry,
       "pm1004dcpAlmj0AlarmIndex": pm1004dcpAlmj0AlarmIndex,
       "pm1004dcpAlmJ0TimAlarmPortn": pm1004dcpAlmJ0TimAlarmPortn,
       "pm1004dcpAlmJ0TiiAlarmPortn": pm1004dcpAlmJ0TiiAlarmPortn,
       "pm1004dcpAlmCrc7ErrorPortn": pm1004dcpAlmCrc7ErrorPortn,
       "pm1004dcpMonLine": pm1004dcpMonLine,
       "pm1004dcpMonLinePerformance": pm1004dcpMonLinePerformance,
       "pm1004dcpPerfLineCurrent15CntTable": pm1004dcpPerfLineCurrent15CntTable,
       "pm1004dcpPerfLineCurrent15CntEntry": pm1004dcpPerfLineCurrent15CntEntry,
       "pm1004dcpPerfLineCurrent15CntIndex": pm1004dcpPerfLineCurrent15CntIndex,
       "pm1004dcpPerfLineCurrent15CntInvCvPortn": pm1004dcpPerfLineCurrent15CntInvCvPortn,
       "pm1004dcpPerfLineCurrent15CntCvValuePortn": pm1004dcpPerfLineCurrent15CntCvValuePortn,
       "pm1004dcpPerfLineCurrent15CntInvEsPortn": pm1004dcpPerfLineCurrent15CntInvEsPortn,
       "pm1004dcpPerfLineCurrent15CntEsValuePortn": pm1004dcpPerfLineCurrent15CntEsValuePortn,
       "pm1004dcpPerfLineCurrent15CntInvSesPortn": pm1004dcpPerfLineCurrent15CntInvSesPortn,
       "pm1004dcpPerfLineCurrent15CntSesValuePortn": pm1004dcpPerfLineCurrent15CntSesValuePortn,
       "pm1004dcpPerfLineCurrent15CntInvSefsPortn": pm1004dcpPerfLineCurrent15CntInvSefsPortn,
       "pm1004dcpPerfLineCurrent15CntSefsValuePortn": pm1004dcpPerfLineCurrent15CntSefsValuePortn,
       "pm1004dcpPerfLineCurrent15CntInvUasPortn": pm1004dcpPerfLineCurrent15CntInvUasPortn,
       "pm1004dcpPerfLineCurrent15CntUasValuePortn": pm1004dcpPerfLineCurrent15CntUasValuePortn,
       "pm1004dcpPerfLinePast15CntTable": pm1004dcpPerfLinePast15CntTable,
       "pm1004dcpPerfLinePast15CntEntry": pm1004dcpPerfLinePast15CntEntry,
       "pm1004dcpPerfLinePast15CntIndex": pm1004dcpPerfLinePast15CntIndex,
       "pm1004dcpPerfLinePast15CntInvCvPortn": pm1004dcpPerfLinePast15CntInvCvPortn,
       "pm1004dcpPerfLinePast15CntCvValuePortn": pm1004dcpPerfLinePast15CntCvValuePortn,
       "pm1004dcpPerfLinePast15CntInvEsPortn": pm1004dcpPerfLinePast15CntInvEsPortn,
       "pm1004dcpPerfLinePast15CntEsValuePortn": pm1004dcpPerfLinePast15CntEsValuePortn,
       "pm1004dcpPerfLinePast15CntInvSesPortn": pm1004dcpPerfLinePast15CntInvSesPortn,
       "pm1004dcpPerfLinePast15CntSesValuePortn": pm1004dcpPerfLinePast15CntSesValuePortn,
       "pm1004dcpPerfLinePast15CntInvSefsPortn": pm1004dcpPerfLinePast15CntInvSefsPortn,
       "pm1004dcpPerfLinePast15CntSefsValuePortn": pm1004dcpPerfLinePast15CntSefsValuePortn,
       "pm1004dcpPerfLinePast15CntInvUasPortn": pm1004dcpPerfLinePast15CntInvUasPortn,
       "pm1004dcpPerfLinePast15CntUasValuePortn": pm1004dcpPerfLinePast15CntUasValuePortn,
       "pm1004dcpPerfLineCurrent24CntTable": pm1004dcpPerfLineCurrent24CntTable,
       "pm1004dcpPerfLineCurrent24CntEntry": pm1004dcpPerfLineCurrent24CntEntry,
       "pm1004dcpPerfLineCurrent24CntIndex": pm1004dcpPerfLineCurrent24CntIndex,
       "pm1004dcpPerfLineCurrent24CntInvCvPortn": pm1004dcpPerfLineCurrent24CntInvCvPortn,
       "pm1004dcpPerfLineCurrent24CntCvValuePortn": pm1004dcpPerfLineCurrent24CntCvValuePortn,
       "pm1004dcpPerfLineCurrent24CntInvEsPortn": pm1004dcpPerfLineCurrent24CntInvEsPortn,
       "pm1004dcpPerfLineCurrent24CntEsValuePortn": pm1004dcpPerfLineCurrent24CntEsValuePortn,
       "pm1004dcpPerfLineCurrent24CntInvSesPortn": pm1004dcpPerfLineCurrent24CntInvSesPortn,
       "pm1004dcpPerfLineCurrent24CntSesValuePortn": pm1004dcpPerfLineCurrent24CntSesValuePortn,
       "pm1004dcpPerfLineCurrent24CntInvSefsPortn": pm1004dcpPerfLineCurrent24CntInvSefsPortn,
       "pm1004dcpPerfLineCurrent24CntSefsValuePortn": pm1004dcpPerfLineCurrent24CntSefsValuePortn,
       "pm1004dcpPerfLineCurrent24CntInvUasPortn": pm1004dcpPerfLineCurrent24CntInvUasPortn,
       "pm1004dcpPerfLineCurrent24CntUasValuePortn": pm1004dcpPerfLineCurrent24CntUasValuePortn,
       "pm1004dcpPerfLinePast24CntTable": pm1004dcpPerfLinePast24CntTable,
       "pm1004dcpPerfLinePast24CntEntry": pm1004dcpPerfLinePast24CntEntry,
       "pm1004dcpPerfLinePast24CntIndex": pm1004dcpPerfLinePast24CntIndex,
       "pm1004dcpPerfLinePast24CntInvCvPortn": pm1004dcpPerfLinePast24CntInvCvPortn,
       "pm1004dcpPerfLinePast24CntCvValuePortn": pm1004dcpPerfLinePast24CntCvValuePortn,
       "pm1004dcpPerfLinePast24CntInvEsPortn": pm1004dcpPerfLinePast24CntInvEsPortn,
       "pm1004dcpPerfLinePast24CntEsValuePortn": pm1004dcpPerfLinePast24CntEsValuePortn,
       "pm1004dcpPerfLinePast24CntInvSesPortn": pm1004dcpPerfLinePast24CntInvSesPortn,
       "pm1004dcpPerfLinePast24CntSesValuePortn": pm1004dcpPerfLinePast24CntSesValuePortn,
       "pm1004dcpPerfLinePast24CntInvSefsPortn": pm1004dcpPerfLinePast24CntInvSefsPortn,
       "pm1004dcpPerfLinePast24CntSefsValuePortn": pm1004dcpPerfLinePast24CntSefsValuePortn,
       "pm1004dcpPerfLinePast24CntInvUasPortn": pm1004dcpPerfLinePast24CntInvUasPortn,
       "pm1004dcpPerfLinePast24CntUasValuePortn": pm1004dcpPerfLinePast24CntUasValuePortn,
       "pm1004dcpMonLineTraceIdentifier": pm1004dcpMonLineTraceIdentifier}
)
