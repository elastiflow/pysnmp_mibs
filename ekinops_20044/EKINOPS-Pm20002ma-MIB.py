# SNMP MIB module (EKINOPS-Pm20002ma-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm20002ma-MIB.mib
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

modulePm20002ma = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73)
)
if mibBuilder.loadTexts:
    modulePm20002ma.setRevisions(
        ("2015-11-09 00:00",
         "2016-04-20 00:00",
         "2016-04-29 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00",
         "2017-04-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm20002maMultiRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rate100Mhz", 0),
          ("rate250Mhz", 1),
          ("rate500Mhz", 2),
          ("rate1Ghz", 3))
    )



class Pm20002maOtxMode(TextualConvention, Integer32):
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



class Pm20002maOtxGrid(TextualConvention, Integer32):
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



class Pm20002maAdjustValue(TextualConvention, Integer32):
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



class Pm20002maClientProtocol(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("protocolclientvalue0", 0),
          ("protocolclientvalue1", 1),
          ("protocolclientvalue2", 2),
          ("protocolclientvalue3", 3),
          ("protocolclientvalue4", 4),
          ("protocolclientvalue5", 5),
          ("protocolclientvalue6", 6),
          ("protocolclientvalue7", 7),
          ("protocolclientvalue8", 8))
    )



class Pm20002maProtocolMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protocolmodevalue0", 0),
          ("protocolmodevalue1", 1),
          ("protocolmodevalue2", 2),
          ("protocolmodevalue3", 3))
    )



class Pm20002maOtxChannel(TextualConvention, Integer32):
    status = "current"


class Pm20002maOrxChannel(TextualConvention, Integer32):
    status = "current"


class Pm20002maDccMode(TextualConvention, Integer32):
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
        *(("dccNo", 0),
          ("dccLine1", 1),
          ("dccLine2", 2))
    )



class Pm20002maModuleMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unusedmode", 0),
          ("mode200gma", 1),
          ("mode200gmr", 2),
          ("mode100gulh", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Pm20002maalarms_ObjectIdentity = ObjectIdentity
pm20002maalarms = _Pm20002maalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2)
)
_Pm20002maAlmOther_ObjectIdentity = ObjectIdentity
pm20002maAlmOther = _Pm20002maAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1)
)
_Pm20002maAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm20002maAlmOtherNurg = _Pm20002maAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1)
)
_Pm20002maAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm20002maAlmsynthAlm2 = _Pm20002maAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 2)
)
_Pm20002maAlmConfTableSave_Type = EkiOnOff
_Pm20002maAlmConfTableSave_Object = MibScalar
pm20002maAlmConfTableSave = _Pm20002maAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 2, 1),
    _Pm20002maAlmConfTableSave_Type()
)
pm20002maAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmConfTableSave.setStatus("current")
_Pm20002maAlmInvUpload_Type = EkiOnOff
_Pm20002maAlmInvUpload_Object = MibScalar
pm20002maAlmInvUpload = _Pm20002maAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 2, 2),
    _Pm20002maAlmInvUpload_Type()
)
pm20002maAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmInvUpload.setStatus("current")
_Pm20002maAlmConfTableLoad_Type = EkiOnOff
_Pm20002maAlmConfTableLoad_Object = MibScalar
pm20002maAlmConfTableLoad = _Pm20002maAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 2, 3),
    _Pm20002maAlmConfTableLoad_Type()
)
pm20002maAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmConfTableLoad.setStatus("current")
_Pm20002maAlmCorrelatOff_Type = EkiOnOff
_Pm20002maAlmCorrelatOff_Object = MibScalar
pm20002maAlmCorrelatOff = _Pm20002maAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 2, 4),
    _Pm20002maAlmCorrelatOff_Type()
)
pm20002maAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCorrelatOff.setStatus("current")
_Pm20002maAlmMaintenanceOn_Type = EkiOnOff
_Pm20002maAlmMaintenanceOn_Object = MibScalar
pm20002maAlmMaintenanceOn = _Pm20002maAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 2, 5),
    _Pm20002maAlmMaintenanceOn_Type()
)
pm20002maAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMaintenanceOn.setStatus("current")
_Pm20002maAlmclientQsfpWarnDdm_ObjectIdentity = ObjectIdentity
pm20002maAlmclientQsfpWarnDdm = _Pm20002maAlmclientQsfpWarnDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 338)
)
_Pm20002maAlmTrscv1VccLowWng1_Type = EkiOnOff
_Pm20002maAlmTrscv1VccLowWng1_Object = MibScalar
pm20002maAlmTrscv1VccLowWng1 = _Pm20002maAlmTrscv1VccLowWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 338, 1),
    _Pm20002maAlmTrscv1VccLowWng1_Type()
)
pm20002maAlmTrscv1VccLowWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv1VccLowWng1.setStatus("current")
_Pm20002maAlmTrscv1VccHighWng1_Type = EkiOnOff
_Pm20002maAlmTrscv1VccHighWng1_Object = MibScalar
pm20002maAlmTrscv1VccHighWng1 = _Pm20002maAlmTrscv1VccHighWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 338, 2),
    _Pm20002maAlmTrscv1VccHighWng1_Type()
)
pm20002maAlmTrscv1VccHighWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv1VccHighWng1.setStatus("current")
_Pm20002maAlmTrscv1TempLowWng1_Type = EkiOnOff
_Pm20002maAlmTrscv1TempLowWng1_Object = MibScalar
pm20002maAlmTrscv1TempLowWng1 = _Pm20002maAlmTrscv1TempLowWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 338, 3),
    _Pm20002maAlmTrscv1TempLowWng1_Type()
)
pm20002maAlmTrscv1TempLowWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv1TempLowWng1.setStatus("current")
_Pm20002maAlmTrscv1TempHighWng1_Type = EkiOnOff
_Pm20002maAlmTrscv1TempHighWng1_Object = MibScalar
pm20002maAlmTrscv1TempHighWng1 = _Pm20002maAlmTrscv1TempHighWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 338, 4),
    _Pm20002maAlmTrscv1TempHighWng1_Type()
)
pm20002maAlmTrscv1TempHighWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv1TempHighWng1.setStatus("current")
_Pm20002maAlmTrscv2VccLowWng1_Type = EkiOnOff
_Pm20002maAlmTrscv2VccLowWng1_Object = MibScalar
pm20002maAlmTrscv2VccLowWng1 = _Pm20002maAlmTrscv2VccLowWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 338, 5),
    _Pm20002maAlmTrscv2VccLowWng1_Type()
)
pm20002maAlmTrscv2VccLowWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv2VccLowWng1.setStatus("current")
_Pm20002maAlmTrscv2VccHighWng1_Type = EkiOnOff
_Pm20002maAlmTrscv2VccHighWng1_Object = MibScalar
pm20002maAlmTrscv2VccHighWng1 = _Pm20002maAlmTrscv2VccHighWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 338, 6),
    _Pm20002maAlmTrscv2VccHighWng1_Type()
)
pm20002maAlmTrscv2VccHighWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv2VccHighWng1.setStatus("current")
_Pm20002maAlmTrscv2TempLowWng1_Type = EkiOnOff
_Pm20002maAlmTrscv2TempLowWng1_Object = MibScalar
pm20002maAlmTrscv2TempLowWng1 = _Pm20002maAlmTrscv2TempLowWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 338, 7),
    _Pm20002maAlmTrscv2TempLowWng1_Type()
)
pm20002maAlmTrscv2TempLowWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv2TempLowWng1.setStatus("current")
_Pm20002maAlmTrscv2TempHighWng1_Type = EkiOnOff
_Pm20002maAlmTrscv2TempHighWng1_Object = MibScalar
pm20002maAlmTrscv2TempHighWng1 = _Pm20002maAlmTrscv2TempHighWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 1, 338, 8),
    _Pm20002maAlmTrscv2TempHighWng1_Type()
)
pm20002maAlmTrscv2TempHighWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv2TempHighWng1.setStatus("current")
_Pm20002maAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm20002maAlmOtherUrg = _Pm20002maAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2)
)
_Pm20002maAlmmodFanFail_ObjectIdentity = ObjectIdentity
pm20002maAlmmodFanFail = _Pm20002maAlmmodFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 336)
)
_Pm20002maAlmFanFail_Type = EkiOnOff
_Pm20002maAlmFanFail_Object = MibScalar
pm20002maAlmFanFail = _Pm20002maAlmFanFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 336, 1),
    _Pm20002maAlmFanFail_Type()
)
pm20002maAlmFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmFanFail.setStatus("current")
_Pm20002maAlmFanHighSpeed_Type = EkiOnOff
_Pm20002maAlmFanHighSpeed_Object = MibScalar
pm20002maAlmFanHighSpeed = _Pm20002maAlmFanHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 336, 2),
    _Pm20002maAlmFanHighSpeed_Type()
)
pm20002maAlmFanHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmFanHighSpeed.setStatus("current")
_Pm20002maAlmclientQsfpAlarmDdm_ObjectIdentity = ObjectIdentity
pm20002maAlmclientQsfpAlarmDdm = _Pm20002maAlmclientQsfpAlarmDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 337)
)
_Pm20002maAlmTrscv1VccLowAla1_Type = EkiOnOff
_Pm20002maAlmTrscv1VccLowAla1_Object = MibScalar
pm20002maAlmTrscv1VccLowAla1 = _Pm20002maAlmTrscv1VccLowAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 337, 1),
    _Pm20002maAlmTrscv1VccLowAla1_Type()
)
pm20002maAlmTrscv1VccLowAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv1VccLowAla1.setStatus("current")
_Pm20002maAlmTrscv1VccHighAla1_Type = EkiOnOff
_Pm20002maAlmTrscv1VccHighAla1_Object = MibScalar
pm20002maAlmTrscv1VccHighAla1 = _Pm20002maAlmTrscv1VccHighAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 337, 2),
    _Pm20002maAlmTrscv1VccHighAla1_Type()
)
pm20002maAlmTrscv1VccHighAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv1VccHighAla1.setStatus("current")
_Pm20002maAlmTrscv1TempLowAla1_Type = EkiOnOff
_Pm20002maAlmTrscv1TempLowAla1_Object = MibScalar
pm20002maAlmTrscv1TempLowAla1 = _Pm20002maAlmTrscv1TempLowAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 337, 3),
    _Pm20002maAlmTrscv1TempLowAla1_Type()
)
pm20002maAlmTrscv1TempLowAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv1TempLowAla1.setStatus("current")
_Pm20002maAlmTrscv1TempHighAla_Type = EkiOnOff
_Pm20002maAlmTrscv1TempHighAla_Object = MibScalar
pm20002maAlmTrscv1TempHighAla = _Pm20002maAlmTrscv1TempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 337, 4),
    _Pm20002maAlmTrscv1TempHighAla_Type()
)
pm20002maAlmTrscv1TempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv1TempHighAla.setStatus("current")
_Pm20002maAlmTrscv2VccLowAla1_Type = EkiOnOff
_Pm20002maAlmTrscv2VccLowAla1_Object = MibScalar
pm20002maAlmTrscv2VccLowAla1 = _Pm20002maAlmTrscv2VccLowAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 337, 5),
    _Pm20002maAlmTrscv2VccLowAla1_Type()
)
pm20002maAlmTrscv2VccLowAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv2VccLowAla1.setStatus("current")
_Pm20002maAlmTrscv2VccHighAla1_Type = EkiOnOff
_Pm20002maAlmTrscv2VccHighAla1_Object = MibScalar
pm20002maAlmTrscv2VccHighAla1 = _Pm20002maAlmTrscv2VccHighAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 337, 6),
    _Pm20002maAlmTrscv2VccHighAla1_Type()
)
pm20002maAlmTrscv2VccHighAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv2VccHighAla1.setStatus("current")
_Pm20002maAlmTrscv2TempLowAla1_Type = EkiOnOff
_Pm20002maAlmTrscv2TempLowAla1_Object = MibScalar
pm20002maAlmTrscv2TempLowAla1 = _Pm20002maAlmTrscv2TempLowAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 337, 7),
    _Pm20002maAlmTrscv2TempLowAla1_Type()
)
pm20002maAlmTrscv2TempLowAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv2TempLowAla1.setStatus("current")
_Pm20002maAlmTrscv2TempHighAla1_Type = EkiOnOff
_Pm20002maAlmTrscv2TempHighAla1_Object = MibScalar
pm20002maAlmTrscv2TempHighAla1 = _Pm20002maAlmTrscv2TempHighAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 2, 337, 8),
    _Pm20002maAlmTrscv2TempHighAla1_Type()
)
pm20002maAlmTrscv2TempHighAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTrscv2TempHighAla1.setStatus("current")
_Pm20002maAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm20002maAlmOtherCrit = _Pm20002maAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3)
)
_Pm20002maAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm20002maAlmsynthAlm0 = _Pm20002maAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 0)
)
_Pm20002maAlmFailFan_Type = EkiOnOff
_Pm20002maAlmFailFan_Object = MibScalar
pm20002maAlmFailFan = _Pm20002maAlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 0, 2),
    _Pm20002maAlmFailFan_Type()
)
pm20002maAlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmFailFan.setStatus("current")
_Pm20002maAlmModGlobFail_Type = EkiOnOff
_Pm20002maAlmModGlobFail_Object = MibScalar
pm20002maAlmModGlobFail = _Pm20002maAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 0, 9),
    _Pm20002maAlmModGlobFail_Type()
)
pm20002maAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmModGlobFail.setStatus("current")
_Pm20002maAlmDefFuseA_Type = EkiOnOff
_Pm20002maAlmDefFuseA_Object = MibScalar
pm20002maAlmDefFuseA = _Pm20002maAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 0, 15),
    _Pm20002maAlmDefFuseA_Type()
)
pm20002maAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmDefFuseA.setStatus("current")
_Pm20002maAlmDefFuseB_Type = EkiOnOff
_Pm20002maAlmDefFuseB_Object = MibScalar
pm20002maAlmDefFuseB = _Pm20002maAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 0, 16),
    _Pm20002maAlmDefFuseB_Type()
)
pm20002maAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmDefFuseB.setStatus("current")
_Pm20002maAlmclientModuleState_ObjectIdentity = ObjectIdentity
pm20002maAlmclientModuleState = _Pm20002maAlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72)
)
_Pm20002maAlmCfpInitialize_Type = EkiOnOff
_Pm20002maAlmCfpInitialize_Object = MibScalar
pm20002maAlmCfpInitialize = _Pm20002maAlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72, 1),
    _Pm20002maAlmCfpInitialize_Type()
)
pm20002maAlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpInitialize.setStatus("current")
_Pm20002maAlmCfpLowPower_Type = EkiOnOff
_Pm20002maAlmCfpLowPower_Object = MibScalar
pm20002maAlmCfpLowPower = _Pm20002maAlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72, 2),
    _Pm20002maAlmCfpLowPower_Type()
)
pm20002maAlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpLowPower.setStatus("current")
_Pm20002maAlmCfpHighPowerUp_Type = EkiOnOff
_Pm20002maAlmCfpHighPowerUp_Object = MibScalar
pm20002maAlmCfpHighPowerUp = _Pm20002maAlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72, 3),
    _Pm20002maAlmCfpHighPowerUp_Type()
)
pm20002maAlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpHighPowerUp.setStatus("current")
_Pm20002maAlmCfpTxOff_Type = EkiOnOff
_Pm20002maAlmCfpTxOff_Object = MibScalar
pm20002maAlmCfpTxOff = _Pm20002maAlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72, 4),
    _Pm20002maAlmCfpTxOff_Type()
)
pm20002maAlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpTxOff.setStatus("current")
_Pm20002maAlmCfpTxTurnOn_Type = EkiOnOff
_Pm20002maAlmCfpTxTurnOn_Object = MibScalar
pm20002maAlmCfpTxTurnOn = _Pm20002maAlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72, 5),
    _Pm20002maAlmCfpTxTurnOn_Type()
)
pm20002maAlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpTxTurnOn.setStatus("current")
_Pm20002maAlmCfpReady_Type = EkiOnOff
_Pm20002maAlmCfpReady_Object = MibScalar
pm20002maAlmCfpReady = _Pm20002maAlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72, 6),
    _Pm20002maAlmCfpReady_Type()
)
pm20002maAlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpReady.setStatus("current")
_Pm20002maAlmCfpFault_Type = EkiOnOff
_Pm20002maAlmCfpFault_Object = MibScalar
pm20002maAlmCfpFault = _Pm20002maAlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72, 7),
    _Pm20002maAlmCfpFault_Type()
)
pm20002maAlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpFault.setStatus("current")
_Pm20002maAlmCfpTxTurnOff_Type = EkiOnOff
_Pm20002maAlmCfpTxTurnOff_Object = MibScalar
pm20002maAlmCfpTxTurnOff = _Pm20002maAlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72, 8),
    _Pm20002maAlmCfpTxTurnOff_Type()
)
pm20002maAlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpTxTurnOff.setStatus("current")
_Pm20002maAlmCfpHighPowerDown_Type = EkiOnOff
_Pm20002maAlmCfpHighPowerDown_Object = MibScalar
pm20002maAlmCfpHighPowerDown = _Pm20002maAlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 72, 9),
    _Pm20002maAlmCfpHighPowerDown_Type()
)
pm20002maAlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpHighPowerDown.setStatus("current")
_Pm20002maAlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm20002maAlmclientModuleGeneralStatus = _Pm20002maAlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73)
)
_Pm20002maAlmCfpOutOfAlignment_Type = EkiOnOff
_Pm20002maAlmCfpOutOfAlignment_Object = MibScalar
pm20002maAlmCfpOutOfAlignment = _Pm20002maAlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73, 4),
    _Pm20002maAlmCfpOutOfAlignment_Type()
)
pm20002maAlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpOutOfAlignment.setStatus("current")
_Pm20002maAlmCfpRxNetworkLol_Type = EkiOnOff
_Pm20002maAlmCfpRxNetworkLol_Object = MibScalar
pm20002maAlmCfpRxNetworkLol = _Pm20002maAlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73, 5),
    _Pm20002maAlmCfpRxNetworkLol_Type()
)
pm20002maAlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpRxNetworkLol.setStatus("current")
_Pm20002maAlmCfpRxLos_Type = EkiOnOff
_Pm20002maAlmCfpRxLos_Object = MibScalar
pm20002maAlmCfpRxLos = _Pm20002maAlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73, 6),
    _Pm20002maAlmCfpRxLos_Type()
)
pm20002maAlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpRxLos.setStatus("current")
_Pm20002maAlmCfpTxHostLol_Type = EkiOnOff
_Pm20002maAlmCfpTxHostLol_Object = MibScalar
pm20002maAlmCfpTxHostLol = _Pm20002maAlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73, 7),
    _Pm20002maAlmCfpTxHostLol_Type()
)
pm20002maAlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpTxHostLol.setStatus("current")
_Pm20002maAlmCfpTxLosf_Type = EkiOnOff
_Pm20002maAlmCfpTxLosf_Object = MibScalar
pm20002maAlmCfpTxLosf = _Pm20002maAlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73, 8),
    _Pm20002maAlmCfpTxLosf_Type()
)
pm20002maAlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpTxLosf.setStatus("current")
_Pm20002maAlmCfpTxCmuLol_Type = EkiOnOff
_Pm20002maAlmCfpTxCmuLol_Object = MibScalar
pm20002maAlmCfpTxCmuLol = _Pm20002maAlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73, 9),
    _Pm20002maAlmCfpTxCmuLol_Type()
)
pm20002maAlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpTxCmuLol.setStatus("current")
_Pm20002maAlmCfpTxJitterPllLol_Type = EkiOnOff
_Pm20002maAlmCfpTxJitterPllLol_Object = MibScalar
pm20002maAlmCfpTxJitterPllLol = _Pm20002maAlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73, 10),
    _Pm20002maAlmCfpTxJitterPllLol_Type()
)
pm20002maAlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpTxJitterPllLol.setStatus("current")
_Pm20002maAlmCfpLossOfRefclk_Type = EkiOnOff
_Pm20002maAlmCfpLossOfRefclk_Object = MibScalar
pm20002maAlmCfpLossOfRefclk = _Pm20002maAlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73, 11),
    _Pm20002maAlmCfpLossOfRefclk_Type()
)
pm20002maAlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpLossOfRefclk.setStatus("current")
_Pm20002maAlmCfpHwInterlock_Type = EkiOnOff
_Pm20002maAlmCfpHwInterlock_Object = MibScalar
pm20002maAlmCfpHwInterlock = _Pm20002maAlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 73, 14),
    _Pm20002maAlmCfpHwInterlock_Type()
)
pm20002maAlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpHwInterlock.setStatus("current")
_Pm20002maAlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm20002maAlmclientGlobalAlarmSummary = _Pm20002maAlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74)
)
_Pm20002maAlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Pm20002maAlmCfpSoftGlobAlarmTest_Object = MibScalar
pm20002maAlmCfpSoftGlobAlarmTest = _Pm20002maAlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 1),
    _Pm20002maAlmCfpSoftGlobAlarmTest_Type()
)
pm20002maAlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpSoftGlobAlarmTest.setStatus("current")
_Pm20002maAlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm20002maAlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
pm20002maAlmCfpNetworkLaneAlarmWarning2 = _Pm20002maAlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 7),
    _Pm20002maAlmCfpNetworkLaneAlarmWarning2_Type()
)
pm20002maAlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Pm20002maAlmCfpModuleState_Type = EkiOnOff
_Pm20002maAlmCfpModuleState_Object = MibScalar
pm20002maAlmCfpModuleState = _Pm20002maAlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 8),
    _Pm20002maAlmCfpModuleState_Type()
)
pm20002maAlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpModuleState.setStatus("current")
_Pm20002maAlmCfpModuleGeneralStatus_Type = EkiOnOff
_Pm20002maAlmCfpModuleGeneralStatus_Object = MibScalar
pm20002maAlmCfpModuleGeneralStatus = _Pm20002maAlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 9),
    _Pm20002maAlmCfpModuleGeneralStatus_Type()
)
pm20002maAlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpModuleGeneralStatus.setStatus("current")
_Pm20002maAlmCfpModuleFault_Type = EkiOnOff
_Pm20002maAlmCfpModuleFault_Object = MibScalar
pm20002maAlmCfpModuleFault = _Pm20002maAlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 10),
    _Pm20002maAlmCfpModuleFault_Type()
)
pm20002maAlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpModuleFault.setStatus("current")
_Pm20002maAlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Pm20002maAlmCfpModuleAlarmWarning1_Object = MibScalar
pm20002maAlmCfpModuleAlarmWarning1 = _Pm20002maAlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 11),
    _Pm20002maAlmCfpModuleAlarmWarning1_Type()
)
pm20002maAlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpModuleAlarmWarning1.setStatus("current")
_Pm20002maAlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Pm20002maAlmCfpModuleAlarmWarning2_Object = MibScalar
pm20002maAlmCfpModuleAlarmWarning2 = _Pm20002maAlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 12),
    _Pm20002maAlmCfpModuleAlarmWarning2_Type()
)
pm20002maAlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpModuleAlarmWarning2.setStatus("current")
_Pm20002maAlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm20002maAlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
pm20002maAlmCfpNetworkLaneAlarmWarning1 = _Pm20002maAlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 13),
    _Pm20002maAlmCfpNetworkLaneAlarmWarning1_Type()
)
pm20002maAlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Pm20002maAlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Pm20002maAlmCfpNetworkLaneFaultStatus_Object = MibScalar
pm20002maAlmCfpNetworkLaneFaultStatus = _Pm20002maAlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 14),
    _Pm20002maAlmCfpNetworkLaneFaultStatus_Type()
)
pm20002maAlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpNetworkLaneFaultStatus.setStatus("current")
_Pm20002maAlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Pm20002maAlmCfpHostLaneFaultStatus_Object = MibScalar
pm20002maAlmCfpHostLaneFaultStatus = _Pm20002maAlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 15),
    _Pm20002maAlmCfpHostLaneFaultStatus_Type()
)
pm20002maAlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpHostLaneFaultStatus.setStatus("current")
_Pm20002maAlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Pm20002maAlmCfpGlobAlarmAssertion_Object = MibScalar
pm20002maAlmCfpGlobAlarmAssertion = _Pm20002maAlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 74, 16),
    _Pm20002maAlmCfpGlobAlarmAssertion_Type()
)
pm20002maAlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmCfpGlobAlarmAssertion.setStatus("current")
_Pm20002maAlmmsaModuleState_ObjectIdentity = ObjectIdentity
pm20002maAlmmsaModuleState = _Pm20002maAlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78)
)
_Pm20002maAlmMsaInitialize_Type = EkiOnOff
_Pm20002maAlmMsaInitialize_Object = MibScalar
pm20002maAlmMsaInitialize = _Pm20002maAlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78, 1),
    _Pm20002maAlmMsaInitialize_Type()
)
pm20002maAlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaInitialize.setStatus("current")
_Pm20002maAlmMsaLowPower_Type = EkiOnOff
_Pm20002maAlmMsaLowPower_Object = MibScalar
pm20002maAlmMsaLowPower = _Pm20002maAlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78, 2),
    _Pm20002maAlmMsaLowPower_Type()
)
pm20002maAlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaLowPower.setStatus("current")
_Pm20002maAlmMsaHighPowerUp_Type = EkiOnOff
_Pm20002maAlmMsaHighPowerUp_Object = MibScalar
pm20002maAlmMsaHighPowerUp = _Pm20002maAlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78, 3),
    _Pm20002maAlmMsaHighPowerUp_Type()
)
pm20002maAlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaHighPowerUp.setStatus("current")
_Pm20002maAlmMsaTxOff_Type = EkiOnOff
_Pm20002maAlmMsaTxOff_Object = MibScalar
pm20002maAlmMsaTxOff = _Pm20002maAlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78, 4),
    _Pm20002maAlmMsaTxOff_Type()
)
pm20002maAlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaTxOff.setStatus("current")
_Pm20002maAlmMsaTxTurnOn_Type = EkiOnOff
_Pm20002maAlmMsaTxTurnOn_Object = MibScalar
pm20002maAlmMsaTxTurnOn = _Pm20002maAlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78, 5),
    _Pm20002maAlmMsaTxTurnOn_Type()
)
pm20002maAlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaTxTurnOn.setStatus("current")
_Pm20002maAlmMsaReady_Type = EkiOnOff
_Pm20002maAlmMsaReady_Object = MibScalar
pm20002maAlmMsaReady = _Pm20002maAlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78, 6),
    _Pm20002maAlmMsaReady_Type()
)
pm20002maAlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaReady.setStatus("current")
_Pm20002maAlmMsaFault_Type = EkiOnOff
_Pm20002maAlmMsaFault_Object = MibScalar
pm20002maAlmMsaFault = _Pm20002maAlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78, 7),
    _Pm20002maAlmMsaFault_Type()
)
pm20002maAlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaFault.setStatus("current")
_Pm20002maAlmMsaTxTurnOff_Type = EkiOnOff
_Pm20002maAlmMsaTxTurnOff_Object = MibScalar
pm20002maAlmMsaTxTurnOff = _Pm20002maAlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78, 8),
    _Pm20002maAlmMsaTxTurnOff_Type()
)
pm20002maAlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaTxTurnOff.setStatus("current")
_Pm20002maAlmMsaHighPowerDown_Type = EkiOnOff
_Pm20002maAlmMsaHighPowerDown_Object = MibScalar
pm20002maAlmMsaHighPowerDown = _Pm20002maAlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 78, 9),
    _Pm20002maAlmMsaHighPowerDown_Type()
)
pm20002maAlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaHighPowerDown.setStatus("current")
_Pm20002maAlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm20002maAlmmsaModuleGeneralStatus = _Pm20002maAlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79)
)
_Pm20002maAlmMsaOutOfAlignment_Type = EkiOnOff
_Pm20002maAlmMsaOutOfAlignment_Object = MibScalar
pm20002maAlmMsaOutOfAlignment = _Pm20002maAlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79, 4),
    _Pm20002maAlmMsaOutOfAlignment_Type()
)
pm20002maAlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaOutOfAlignment.setStatus("current")
_Pm20002maAlmMsaRxNetworkLol_Type = EkiOnOff
_Pm20002maAlmMsaRxNetworkLol_Object = MibScalar
pm20002maAlmMsaRxNetworkLol = _Pm20002maAlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79, 5),
    _Pm20002maAlmMsaRxNetworkLol_Type()
)
pm20002maAlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaRxNetworkLol.setStatus("current")
_Pm20002maAlmMsaRxLos_Type = EkiOnOff
_Pm20002maAlmMsaRxLos_Object = MibScalar
pm20002maAlmMsaRxLos = _Pm20002maAlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79, 6),
    _Pm20002maAlmMsaRxLos_Type()
)
pm20002maAlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaRxLos.setStatus("current")
_Pm20002maAlmMsaTxHostLol_Type = EkiOnOff
_Pm20002maAlmMsaTxHostLol_Object = MibScalar
pm20002maAlmMsaTxHostLol = _Pm20002maAlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79, 7),
    _Pm20002maAlmMsaTxHostLol_Type()
)
pm20002maAlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaTxHostLol.setStatus("current")
_Pm20002maAlmMsaTxLosf_Type = EkiOnOff
_Pm20002maAlmMsaTxLosf_Object = MibScalar
pm20002maAlmMsaTxLosf = _Pm20002maAlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79, 8),
    _Pm20002maAlmMsaTxLosf_Type()
)
pm20002maAlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaTxLosf.setStatus("current")
_Pm20002maAlmMsaTxCmuLol_Type = EkiOnOff
_Pm20002maAlmMsaTxCmuLol_Object = MibScalar
pm20002maAlmMsaTxCmuLol = _Pm20002maAlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79, 9),
    _Pm20002maAlmMsaTxCmuLol_Type()
)
pm20002maAlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaTxCmuLol.setStatus("current")
_Pm20002maAlmMsaTxJitterPllLol_Type = EkiOnOff
_Pm20002maAlmMsaTxJitterPllLol_Object = MibScalar
pm20002maAlmMsaTxJitterPllLol = _Pm20002maAlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79, 10),
    _Pm20002maAlmMsaTxJitterPllLol_Type()
)
pm20002maAlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaTxJitterPllLol.setStatus("current")
_Pm20002maAlmMsaLossOfRefclk_Type = EkiOnOff
_Pm20002maAlmMsaLossOfRefclk_Object = MibScalar
pm20002maAlmMsaLossOfRefclk = _Pm20002maAlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79, 11),
    _Pm20002maAlmMsaLossOfRefclk_Type()
)
pm20002maAlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaLossOfRefclk.setStatus("current")
_Pm20002maAlmMsaHwInterlock_Type = EkiOnOff
_Pm20002maAlmMsaHwInterlock_Object = MibScalar
pm20002maAlmMsaHwInterlock = _Pm20002maAlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 79, 14),
    _Pm20002maAlmMsaHwInterlock_Type()
)
pm20002maAlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaHwInterlock.setStatus("current")
_Pm20002maAlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm20002maAlmmsaGlobalAlarmSummary = _Pm20002maAlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80)
)
_Pm20002maAlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Pm20002maAlmMsaSoftGlobAlarmTest_Object = MibScalar
pm20002maAlmMsaSoftGlobAlarmTest = _Pm20002maAlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 1),
    _Pm20002maAlmMsaSoftGlobAlarmTest_Type()
)
pm20002maAlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaSoftGlobAlarmTest.setStatus("current")
_Pm20002maAlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Pm20002maAlmMsaNetworkHostAlarmStatus_Object = MibScalar
pm20002maAlmMsaNetworkHostAlarmStatus = _Pm20002maAlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 6),
    _Pm20002maAlmMsaNetworkHostAlarmStatus_Type()
)
pm20002maAlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaNetworkHostAlarmStatus.setStatus("current")
_Pm20002maAlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm20002maAlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
pm20002maAlmMsaNetworkLaneAlarmWarning2 = _Pm20002maAlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 7),
    _Pm20002maAlmMsaNetworkLaneAlarmWarning2_Type()
)
pm20002maAlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Pm20002maAlmMsaModuleState_Type = EkiOnOff
_Pm20002maAlmMsaModuleState_Object = MibScalar
pm20002maAlmMsaModuleState = _Pm20002maAlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 8),
    _Pm20002maAlmMsaModuleState_Type()
)
pm20002maAlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaModuleState.setStatus("current")
_Pm20002maAlmMsaModuleGeneralStatus_Type = EkiOnOff
_Pm20002maAlmMsaModuleGeneralStatus_Object = MibScalar
pm20002maAlmMsaModuleGeneralStatus = _Pm20002maAlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 9),
    _Pm20002maAlmMsaModuleGeneralStatus_Type()
)
pm20002maAlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaModuleGeneralStatus.setStatus("current")
_Pm20002maAlmModuleFault_Type = EkiOnOff
_Pm20002maAlmModuleFault_Object = MibScalar
pm20002maAlmModuleFault = _Pm20002maAlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 10),
    _Pm20002maAlmModuleFault_Type()
)
pm20002maAlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmModuleFault.setStatus("current")
_Pm20002maAlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Pm20002maAlmMsaModuleAlarmWarning1_Object = MibScalar
pm20002maAlmMsaModuleAlarmWarning1 = _Pm20002maAlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 11),
    _Pm20002maAlmMsaModuleAlarmWarning1_Type()
)
pm20002maAlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaModuleAlarmWarning1.setStatus("current")
_Pm20002maAlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Pm20002maAlmMsaModuleAlarmWarning2_Object = MibScalar
pm20002maAlmMsaModuleAlarmWarning2 = _Pm20002maAlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 12),
    _Pm20002maAlmMsaModuleAlarmWarning2_Type()
)
pm20002maAlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaModuleAlarmWarning2.setStatus("current")
_Pm20002maAlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm20002maAlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
pm20002maAlmMsaNetworkLaneAlarmWarning1 = _Pm20002maAlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 13),
    _Pm20002maAlmMsaNetworkLaneAlarmWarning1_Type()
)
pm20002maAlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Pm20002maAlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Pm20002maAlmMsaNetworkLaneFaultStatus_Object = MibScalar
pm20002maAlmMsaNetworkLaneFaultStatus = _Pm20002maAlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 14),
    _Pm20002maAlmMsaNetworkLaneFaultStatus_Type()
)
pm20002maAlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaNetworkLaneFaultStatus.setStatus("current")
_Pm20002maAlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Pm20002maAlmMsaHostLaneFaultStatus_Object = MibScalar
pm20002maAlmMsaHostLaneFaultStatus = _Pm20002maAlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 15),
    _Pm20002maAlmMsaHostLaneFaultStatus_Type()
)
pm20002maAlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaHostLaneFaultStatus.setStatus("current")
_Pm20002maAlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Pm20002maAlmMsaGlobAlarmAssertion_Object = MibScalar
pm20002maAlmMsaGlobAlarmAssertion = _Pm20002maAlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 80, 16),
    _Pm20002maAlmMsaGlobAlarmAssertion_Type()
)
pm20002maAlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmMsaGlobAlarmAssertion.setStatus("current")
_Pm20002maAlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
pm20002maAlmmsaNetworkTxAlignment = _Pm20002maAlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 81)
)
_Pm20002maAlmNetTxTimingFault_Type = EkiOnOff
_Pm20002maAlmNetTxTimingFault_Object = MibScalar
pm20002maAlmNetTxTimingFault = _Pm20002maAlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 81, 12),
    _Pm20002maAlmNetTxTimingFault_Type()
)
pm20002maAlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetTxTimingFault.setStatus("current")
_Pm20002maAlmNetTxReferenceClockFault_Type = EkiOnOff
_Pm20002maAlmNetTxReferenceClockFault_Object = MibScalar
pm20002maAlmNetTxReferenceClockFault = _Pm20002maAlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 81, 13),
    _Pm20002maAlmNetTxReferenceClockFault_Type()
)
pm20002maAlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetTxReferenceClockFault.setStatus("current")
_Pm20002maAlmNetTxCmuLockFault_Type = EkiOnOff
_Pm20002maAlmNetTxCmuLockFault_Object = MibScalar
pm20002maAlmNetTxCmuLockFault = _Pm20002maAlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 81, 14),
    _Pm20002maAlmNetTxCmuLockFault_Type()
)
pm20002maAlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetTxCmuLockFault.setStatus("current")
_Pm20002maAlmNetTxOutOfAlignment_Type = EkiOnOff
_Pm20002maAlmNetTxOutOfAlignment_Object = MibScalar
pm20002maAlmNetTxOutOfAlignment = _Pm20002maAlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 81, 15),
    _Pm20002maAlmNetTxOutOfAlignment_Type()
)
pm20002maAlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetTxOutOfAlignment.setStatus("current")
_Pm20002maAlmNetTxLossOfAlignment_Type = EkiOnOff
_Pm20002maAlmNetTxLossOfAlignment_Object = MibScalar
pm20002maAlmNetTxLossOfAlignment = _Pm20002maAlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 81, 16),
    _Pm20002maAlmNetTxLossOfAlignment_Type()
)
pm20002maAlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetTxLossOfAlignment.setStatus("current")
_Pm20002maAlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
pm20002maAlmmsaNetworkRxAlignment = _Pm20002maAlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 82)
)
_Pm20002maAlmNetRxTimingFault_Type = EkiOnOff
_Pm20002maAlmNetRxTimingFault_Object = MibScalar
pm20002maAlmNetRxTimingFault = _Pm20002maAlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 82, 12),
    _Pm20002maAlmNetRxTimingFault_Type()
)
pm20002maAlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetRxTimingFault.setStatus("current")
_Pm20002maAlmNetRxOutOfAlignment_Type = EkiOnOff
_Pm20002maAlmNetRxOutOfAlignment_Object = MibScalar
pm20002maAlmNetRxOutOfAlignment = _Pm20002maAlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 82, 13),
    _Pm20002maAlmNetRxOutOfAlignment_Type()
)
pm20002maAlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetRxOutOfAlignment.setStatus("current")
_Pm20002maAlmNetRxLossOfAlignment_Type = EkiOnOff
_Pm20002maAlmNetRxLossOfAlignment_Object = MibScalar
pm20002maAlmNetRxLossOfAlignment = _Pm20002maAlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 82, 14),
    _Pm20002maAlmNetRxLossOfAlignment_Type()
)
pm20002maAlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetRxLossOfAlignment.setStatus("current")
_Pm20002maAlmNetRxModemLockFault_Type = EkiOnOff
_Pm20002maAlmNetRxModemLockFault_Object = MibScalar
pm20002maAlmNetRxModemLockFault = _Pm20002maAlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 82, 15),
    _Pm20002maAlmNetRxModemLockFault_Type()
)
pm20002maAlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetRxModemLockFault.setStatus("current")
_Pm20002maAlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Pm20002maAlmNetRxModemSyncDetectFault_Object = MibScalar
pm20002maAlmNetRxModemSyncDetectFault = _Pm20002maAlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 82, 16),
    _Pm20002maAlmNetRxModemSyncDetectFault_Type()
)
pm20002maAlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetRxModemSyncDetectFault.setStatus("current")
_Pm20002maAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
pm20002maAlmmsaNetworkHostNetworkAlarmSummary = _Pm20002maAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 83)
)
_Pm20002maAlmNetworkTxAlignment_Type = EkiOnOff
_Pm20002maAlmNetworkTxAlignment_Object = MibScalar
pm20002maAlmNetworkTxAlignment = _Pm20002maAlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 83, 11),
    _Pm20002maAlmNetworkTxAlignment_Type()
)
pm20002maAlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetworkTxAlignment.setStatus("current")
_Pm20002maAlmNetworkRxAlignment_Type = EkiOnOff
_Pm20002maAlmNetworkRxAlignment_Object = MibScalar
pm20002maAlmNetworkRxAlignment = _Pm20002maAlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 83, 12),
    _Pm20002maAlmNetworkRxAlignment_Type()
)
pm20002maAlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetworkRxAlignment.setStatus("current")
_Pm20002maAlmNetworkRxOtn_Type = EkiOnOff
_Pm20002maAlmNetworkRxOtn_Object = MibScalar
pm20002maAlmNetworkRxOtn = _Pm20002maAlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 83, 13),
    _Pm20002maAlmNetworkRxOtn_Type()
)
pm20002maAlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmNetworkRxOtn.setStatus("current")
_Pm20002maAlmHostRxAlignment_Type = EkiOnOff
_Pm20002maAlmHostRxAlignment_Object = MibScalar
pm20002maAlmHostRxAlignment = _Pm20002maAlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 83, 14),
    _Pm20002maAlmHostRxAlignment_Type()
)
pm20002maAlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostRxAlignment.setStatus("current")
_Pm20002maAlmHostTxAlignment_Type = EkiOnOff
_Pm20002maAlmHostTxAlignment_Object = MibScalar
pm20002maAlmHostTxAlignment = _Pm20002maAlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 83, 15),
    _Pm20002maAlmHostTxAlignment_Type()
)
pm20002maAlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostTxAlignment.setStatus("current")
_Pm20002maAlmHostTxOtnStatus_Type = EkiOnOff
_Pm20002maAlmHostTxOtnStatus_Object = MibScalar
pm20002maAlmHostTxOtnStatus = _Pm20002maAlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 83, 16),
    _Pm20002maAlmHostTxOtnStatus_Type()
)
pm20002maAlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostTxOtnStatus.setStatus("current")
_Pm20002maAlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
pm20002maAlmmsaHostTxAlignment = _Pm20002maAlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 84)
)
_Pm20002maAlmHostTxDeskewLockFault_Type = EkiOnOff
_Pm20002maAlmHostTxDeskewLockFault_Object = MibScalar
pm20002maAlmHostTxDeskewLockFault = _Pm20002maAlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 84, 13),
    _Pm20002maAlmHostTxDeskewLockFault_Type()
)
pm20002maAlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostTxDeskewLockFault.setStatus("current")
_Pm20002maAlmHostTxOutOfAlignment_Type = EkiOnOff
_Pm20002maAlmHostTxOutOfAlignment_Object = MibScalar
pm20002maAlmHostTxOutOfAlignment = _Pm20002maAlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 84, 14),
    _Pm20002maAlmHostTxOutOfAlignment_Type()
)
pm20002maAlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostTxOutOfAlignment.setStatus("current")
_Pm20002maAlmHostTxLossOfAlignment_Type = EkiOnOff
_Pm20002maAlmHostTxLossOfAlignment_Object = MibScalar
pm20002maAlmHostTxLossOfAlignment = _Pm20002maAlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 84, 15),
    _Pm20002maAlmHostTxLossOfAlignment_Type()
)
pm20002maAlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostTxLossOfAlignment.setStatus("current")
_Pm20002maAlmHostTxCdrLockFault_Type = EkiOnOff
_Pm20002maAlmHostTxCdrLockFault_Object = MibScalar
pm20002maAlmHostTxCdrLockFault = _Pm20002maAlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 84, 16),
    _Pm20002maAlmHostTxCdrLockFault_Type()
)
pm20002maAlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostTxCdrLockFault.setStatus("current")
_Pm20002maAlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
pm20002maAlmmsaHostRxAlignment = _Pm20002maAlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 85)
)
_Pm20002maAlmHostRxCmuLockFault_Type = EkiOnOff
_Pm20002maAlmHostRxCmuLockFault_Object = MibScalar
pm20002maAlmHostRxCmuLockFault = _Pm20002maAlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 85, 14),
    _Pm20002maAlmHostRxCmuLockFault_Type()
)
pm20002maAlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostRxCmuLockFault.setStatus("current")
_Pm20002maAlmHostRxOutOfAlignment_Type = EkiOnOff
_Pm20002maAlmHostRxOutOfAlignment_Object = MibScalar
pm20002maAlmHostRxOutOfAlignment = _Pm20002maAlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 85, 15),
    _Pm20002maAlmHostRxOutOfAlignment_Type()
)
pm20002maAlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostRxOutOfAlignment.setStatus("current")
_Pm20002maAlmHostRxLossOfAlignment_Type = EkiOnOff
_Pm20002maAlmHostRxLossOfAlignment_Object = MibScalar
pm20002maAlmHostRxLossOfAlignment = _Pm20002maAlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 1, 3, 85, 16),
    _Pm20002maAlmHostRxLossOfAlignment_Type()
)
pm20002maAlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHostRxLossOfAlignment.setStatus("current")
_Pm20002maAlmClient_ObjectIdentity = ObjectIdentity
pm20002maAlmClient = _Pm20002maAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2)
)
_Pm20002maAlmClientNurg_ObjectIdentity = ObjectIdentity
pm20002maAlmClientNurg = _Pm20002maAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1)
)
_Pm20002maAlmclientSfpWarnDdmTable_Object = MibTable
pm20002maAlmclientSfpWarnDdmTable = _Pm20002maAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1, 272)
)
if mibBuilder.loadTexts:
    pm20002maAlmclientSfpWarnDdmTable.setStatus("current")
_Pm20002maAlmclientSfpWarnDdmEntry_Object = MibTableRow
pm20002maAlmclientSfpWarnDdmEntry = _Pm20002maAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1, 272, 1)
)
pm20002maAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm20002maAlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm20002maAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm20002maAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm20002maAlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm20002maAlmclientSfpWarnDdmIndex = _Pm20002maAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1, 272, 1, 1),
    _Pm20002maAlmclientSfpWarnDdmIndex_Type()
)
pm20002maAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmclientSfpWarnDdmIndex.setStatus("current")
_Pm20002maAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm20002maAlmTxPwLowWngPortn_Object = MibTableColumn
pm20002maAlmTxPwLowWngPortn = _Pm20002maAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1, 272, 1, 2),
    _Pm20002maAlmTxPwLowWngPortn_Type()
)
pm20002maAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxPwLowWngPortn.setStatus("current")
_Pm20002maAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm20002maAlmTxPwrHighWngPortn_Object = MibTableColumn
pm20002maAlmTxPwrHighWngPortn = _Pm20002maAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1, 272, 1, 3),
    _Pm20002maAlmTxPwrHighWngPortn_Type()
)
pm20002maAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxPwrHighWngPortn.setStatus("current")
_Pm20002maAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm20002maAlmTxBiasLowWngPortn_Object = MibTableColumn
pm20002maAlmTxBiasLowWngPortn = _Pm20002maAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1, 272, 1, 4),
    _Pm20002maAlmTxBiasLowWngPortn_Type()
)
pm20002maAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxBiasLowWngPortn.setStatus("current")
_Pm20002maAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm20002maAlmTxBiasHighWngPortn_Object = MibTableColumn
pm20002maAlmTxBiasHighWngPortn = _Pm20002maAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1, 272, 1, 5),
    _Pm20002maAlmTxBiasHighWngPortn_Type()
)
pm20002maAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxBiasHighWngPortn.setStatus("current")
_Pm20002maAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm20002maAlmRxPwrLowWngPortn_Object = MibTableColumn
pm20002maAlmRxPwrLowWngPortn = _Pm20002maAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1, 272, 1, 16),
    _Pm20002maAlmRxPwrLowWngPortn_Type()
)
pm20002maAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxPwrLowWngPortn.setStatus("current")
_Pm20002maAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm20002maAlmRxPwrHighWngPortn_Object = MibTableColumn
pm20002maAlmRxPwrHighWngPortn = _Pm20002maAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 1, 272, 1, 17),
    _Pm20002maAlmRxPwrHighWngPortn_Type()
)
pm20002maAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxPwrHighWngPortn.setStatus("current")
_Pm20002maAlmClientUrg_ObjectIdentity = ObjectIdentity
pm20002maAlmClientUrg = _Pm20002maAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2)
)
_Pm20002maAlmclientHostLaneFaultTable_Object = MibTable
pm20002maAlmclientHostLaneFaultTable = _Pm20002maAlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152)
)
if mibBuilder.loadTexts:
    pm20002maAlmclientHostLaneFaultTable.setStatus("current")
_Pm20002maAlmclientHostLaneFaultEntry_Object = MibTableRow
pm20002maAlmclientHostLaneFaultEntry = _Pm20002maAlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1)
)
pm20002maAlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm20002maAlmclientHostLaneFaultEntry.setStatus("current")


class _Pm20002maAlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pm20002maAlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm20002maAlmclientHostLaneFaultIndex_Object = MibTableColumn
pm20002maAlmclientHostLaneFaultIndex = _Pm20002maAlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1, 1),
    _Pm20002maAlmclientHostLaneFaultIndex_Type()
)
pm20002maAlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmclientHostLaneFaultIndex.setStatus("current")
_Pm20002maAlmClientLossOfSyncPortn_Type = EkiOnOff
_Pm20002maAlmClientLossOfSyncPortn_Object = MibTableColumn
pm20002maAlmClientLossOfSyncPortn = _Pm20002maAlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1, 2),
    _Pm20002maAlmClientLossOfSyncPortn_Type()
)
pm20002maAlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientLossOfSyncPortn.setStatus("current")
_Pm20002maAlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pm20002maAlmClientInputLossOfSigPortn_Object = MibTableColumn
pm20002maAlmClientInputLossOfSigPortn = _Pm20002maAlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1, 3),
    _Pm20002maAlmClientInputLossOfSigPortn_Type()
)
pm20002maAlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientInputLossOfSigPortn.setStatus("current")
_Pm20002maAlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pm20002maAlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pm20002maAlmClientLanesMarkerUnlockPortn = _Pm20002maAlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1, 4),
    _Pm20002maAlmClientLanesMarkerUnlockPortn_Type()
)
pm20002maAlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pm20002maAlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pm20002maAlmClientLanes6466UnlockPortn_Object = MibTableColumn
pm20002maAlmClientLanes6466UnlockPortn = _Pm20002maAlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1, 5),
    _Pm20002maAlmClientLanes6466UnlockPortn_Type()
)
pm20002maAlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientLanes6466UnlockPortn.setStatus("current")
_Pm20002maAlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pm20002maAlmClientLanesNotAlignedPortn_Object = MibTableColumn
pm20002maAlmClientLanesNotAlignedPortn = _Pm20002maAlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1, 6),
    _Pm20002maAlmClientLanesNotAlignedPortn_Type()
)
pm20002maAlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientLanesNotAlignedPortn.setStatus("current")
_Pm20002maAlmClientCsfDetectedPortn_Type = EkiOnOff
_Pm20002maAlmClientCsfDetectedPortn_Object = MibTableColumn
pm20002maAlmClientCsfDetectedPortn = _Pm20002maAlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1, 7),
    _Pm20002maAlmClientCsfDetectedPortn_Type()
)
pm20002maAlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientCsfDetectedPortn.setStatus("current")
_Pm20002maAlmClientTxHostLolPortn_Type = EkiOnOff
_Pm20002maAlmClientTxHostLolPortn_Object = MibTableColumn
pm20002maAlmClientTxHostLolPortn = _Pm20002maAlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1, 10),
    _Pm20002maAlmClientTxHostLolPortn_Type()
)
pm20002maAlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientTxHostLolPortn.setStatus("current")
_Pm20002maAlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm20002maAlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pm20002maAlmClientLaneTxFifoErrorPortn = _Pm20002maAlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 152, 1, 11),
    _Pm20002maAlmClientLaneTxFifoErrorPortn_Type()
)
pm20002maAlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pm20002maAlmclientSfpAlmDdmTable_Object = MibTable
pm20002maAlmclientSfpAlmDdmTable = _Pm20002maAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 240)
)
if mibBuilder.loadTexts:
    pm20002maAlmclientSfpAlmDdmTable.setStatus("current")
_Pm20002maAlmclientSfpAlmDdmEntry_Object = MibTableRow
pm20002maAlmclientSfpAlmDdmEntry = _Pm20002maAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 240, 1)
)
pm20002maAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm20002maAlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm20002maAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm20002maAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm20002maAlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm20002maAlmclientSfpAlmDdmIndex = _Pm20002maAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 240, 1, 1),
    _Pm20002maAlmclientSfpAlmDdmIndex_Type()
)
pm20002maAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmclientSfpAlmDdmIndex.setStatus("current")
_Pm20002maAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm20002maAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm20002maAlmTxPwrLowAlaPortn = _Pm20002maAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 240, 1, 2),
    _Pm20002maAlmTxPwrLowAlaPortn_Type()
)
pm20002maAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxPwrLowAlaPortn.setStatus("current")
_Pm20002maAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm20002maAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm20002maAlmTxPwrHighAlaPortn = _Pm20002maAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 240, 1, 3),
    _Pm20002maAlmTxPwrHighAlaPortn_Type()
)
pm20002maAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxPwrHighAlaPortn.setStatus("current")
_Pm20002maAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm20002maAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm20002maAlmTxBiasLowAlaPortn = _Pm20002maAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 240, 1, 4),
    _Pm20002maAlmTxBiasLowAlaPortn_Type()
)
pm20002maAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxBiasLowAlaPortn.setStatus("current")
_Pm20002maAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm20002maAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm20002maAlmTxBiasHighAlaPortn = _Pm20002maAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 240, 1, 5),
    _Pm20002maAlmTxBiasHighAlaPortn_Type()
)
pm20002maAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxBiasHighAlaPortn.setStatus("current")
_Pm20002maAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm20002maAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm20002maAlmRxPwrLowAlaPortn = _Pm20002maAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 240, 1, 16),
    _Pm20002maAlmRxPwrLowAlaPortn_Type()
)
pm20002maAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxPwrLowAlaPortn.setStatus("current")
_Pm20002maAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm20002maAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm20002maAlmRxPwrHighAlaPortn = _Pm20002maAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 2, 240, 1, 17),
    _Pm20002maAlmRxPwrHighAlaPortn_Type()
)
pm20002maAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxPwrHighAlaPortn.setStatus("current")
_Pm20002maAlmClientCrit_ObjectIdentity = ObjectIdentity
pm20002maAlmClientCrit = _Pm20002maAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3)
)
_Pm20002maAlmsynthAlmPortTable_Object = MibTable
pm20002maAlmsynthAlmPortTable = _Pm20002maAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm20002maAlmsynthAlmPortTable.setStatus("current")
_Pm20002maAlmsynthAlmPortEntry_Object = MibTableRow
pm20002maAlmsynthAlmPortEntry = _Pm20002maAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1)
)
pm20002maAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm20002maAlmsynthAlmPortEntry.setStatus("current")


class _Pm20002maAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm20002maAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm20002maAlmsynthAlmPortIndex_Object = MibTableColumn
pm20002maAlmsynthAlmPortIndex = _Pm20002maAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 1),
    _Pm20002maAlmsynthAlmPortIndex_Type()
)
pm20002maAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmsynthAlmPortIndex.setStatus("current")
_Pm20002maAlmSfpAbsentPortn_Type = EkiOnOff
_Pm20002maAlmSfpAbsentPortn_Object = MibTableColumn
pm20002maAlmSfpAbsentPortn = _Pm20002maAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 2),
    _Pm20002maAlmSfpAbsentPortn_Type()
)
pm20002maAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmSfpAbsentPortn.setStatus("current")
_Pm20002maAlmDdmAbsentPortn_Type = EkiOnOff
_Pm20002maAlmDdmAbsentPortn_Object = MibTableColumn
pm20002maAlmDdmAbsentPortn = _Pm20002maAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 3),
    _Pm20002maAlmDdmAbsentPortn_Type()
)
pm20002maAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmDdmAbsentPortn.setStatus("current")
_Pm20002maAlmHwFailAccPortn_Type = EkiOnOff
_Pm20002maAlmHwFailAccPortn_Object = MibTableColumn
pm20002maAlmHwFailAccPortn = _Pm20002maAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 5),
    _Pm20002maAlmHwFailAccPortn_Type()
)
pm20002maAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmHwFailAccPortn.setStatus("current")
_Pm20002maAlmDwLsdPortn_Type = EkiOnOff
_Pm20002maAlmDwLsdPortn_Object = MibTableColumn
pm20002maAlmDwLsdPortn = _Pm20002maAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 6),
    _Pm20002maAlmDwLsdPortn_Type()
)
pm20002maAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmDwLsdPortn.setStatus("current")
_Pm20002maAlmClientLocalOosPortn_Type = EkiOnOff
_Pm20002maAlmClientLocalOosPortn_Object = MibTableColumn
pm20002maAlmClientLocalOosPortn = _Pm20002maAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 7),
    _Pm20002maAlmClientLocalOosPortn_Type()
)
pm20002maAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientLocalOosPortn.setStatus("current")
_Pm20002maAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm20002maAlmClientRemoteOosPortn_Object = MibTableColumn
pm20002maAlmClientRemoteOosPortn = _Pm20002maAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 8),
    _Pm20002maAlmClientRemoteOosPortn_Type()
)
pm20002maAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmClientRemoteOosPortn.setStatus("current")
_Pm20002maAlmDwCaisPortn_Type = EkiOnOff
_Pm20002maAlmDwCaisPortn_Object = MibTableColumn
pm20002maAlmDwCaisPortn = _Pm20002maAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 9),
    _Pm20002maAlmDwCaisPortn_Type()
)
pm20002maAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmDwCaisPortn.setStatus("current")
_Pm20002maAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm20002maAlmSfpDdmWarningPortn_Object = MibTableColumn
pm20002maAlmSfpDdmWarningPortn = _Pm20002maAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 10),
    _Pm20002maAlmSfpDdmWarningPortn_Type()
)
pm20002maAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmSfpDdmWarningPortn.setStatus("current")
_Pm20002maAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm20002maAlmSfpDdmAlmPortn_Object = MibTableColumn
pm20002maAlmSfpDdmAlmPortn = _Pm20002maAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 11),
    _Pm20002maAlmSfpDdmAlmPortn_Type()
)
pm20002maAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmSfpDdmAlmPortn.setStatus("current")
_Pm20002maAlmFailAccPortn_Type = EkiOnOff
_Pm20002maAlmFailAccPortn_Object = MibTableColumn
pm20002maAlmFailAccPortn = _Pm20002maAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 13),
    _Pm20002maAlmFailAccPortn_Type()
)
pm20002maAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmFailAccPortn.setStatus("current")
_Pm20002maAlmUpCsfPortn_Type = EkiOnOff
_Pm20002maAlmUpCsfPortn_Object = MibTableColumn
pm20002maAlmUpCsfPortn = _Pm20002maAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 2, 3, 8, 1, 17),
    _Pm20002maAlmUpCsfPortn_Type()
)
pm20002maAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmUpCsfPortn.setStatus("current")
_Pm20002maAlmLine_ObjectIdentity = ObjectIdentity
pm20002maAlmLine = _Pm20002maAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3)
)
_Pm20002maAlmLineNurg_ObjectIdentity = ObjectIdentity
pm20002maAlmLineNurg = _Pm20002maAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1)
)
_Pm20002maAlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pm20002maAlmlineNetworkLaneAlarmWarning1Table = _Pm20002maAlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184)
)
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pm20002maAlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pm20002maAlmlineNetworkLaneAlarmWarning1Entry = _Pm20002maAlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1)
)
pm20002maAlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pm20002maAlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pm20002maAlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pm20002maAlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pm20002maAlmlineNetworkLaneAlarmWarning1Index = _Pm20002maAlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 1),
    _Pm20002maAlmlineNetworkLaneAlarmWarning1Index_Type()
)
pm20002maAlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pm20002maAlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm20002maAlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pm20002maAlmLineRxPowerLowAlarmPortn = _Pm20002maAlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 2),
    _Pm20002maAlmLineRxPowerLowAlarmPortn_Type()
)
pm20002maAlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pm20002maAlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pm20002maAlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pm20002maAlmLineRxPowerLowWarningPortn = _Pm20002maAlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 3),
    _Pm20002maAlmLineRxPowerLowWarningPortn_Type()
)
pm20002maAlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxPowerLowWarningPortn.setStatus("current")
_Pm20002maAlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pm20002maAlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pm20002maAlmLineRxPowerHighWarningPortn = _Pm20002maAlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 4),
    _Pm20002maAlmLineRxPowerHighWarningPortn_Type()
)
pm20002maAlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxPowerHighWarningPortn.setStatus("current")
_Pm20002maAlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm20002maAlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pm20002maAlmLineRxPowerHighAlarmPortn = _Pm20002maAlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 5),
    _Pm20002maAlmLineRxPowerHighAlarmPortn_Type()
)
pm20002maAlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pm20002maAlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm20002maAlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
pm20002maAlmLineLaserTempLowAlarmPortn = _Pm20002maAlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 6),
    _Pm20002maAlmLineLaserTempLowAlarmPortn_Type()
)
pm20002maAlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaserTempLowAlarmPortn.setStatus("current")
_Pm20002maAlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Pm20002maAlmLineLaserTempLowWarningPortn_Object = MibTableColumn
pm20002maAlmLineLaserTempLowWarningPortn = _Pm20002maAlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 7),
    _Pm20002maAlmLineLaserTempLowWarningPortn_Type()
)
pm20002maAlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaserTempLowWarningPortn.setStatus("current")
_Pm20002maAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm20002maAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm20002maAlmLineLaserTempHighWarningPortn = _Pm20002maAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 8),
    _Pm20002maAlmLineLaserTempHighWarningPortn_Type()
)
pm20002maAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm20002maAlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm20002maAlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
pm20002maAlmLineLaserTempHighAlarmPortn = _Pm20002maAlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 9),
    _Pm20002maAlmLineLaserTempHighAlarmPortn_Type()
)
pm20002maAlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaserTempHighAlarmPortn.setStatus("current")
_Pm20002maAlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm20002maAlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pm20002maAlmLineTxPowerLowAlarmPortn = _Pm20002maAlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 10),
    _Pm20002maAlmLineTxPowerLowAlarmPortn_Type()
)
pm20002maAlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pm20002maAlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pm20002maAlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pm20002maAlmLineTxPowerLowWarningPortn = _Pm20002maAlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 11),
    _Pm20002maAlmLineTxPowerLowWarningPortn_Type()
)
pm20002maAlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxPowerLowWarningPortn.setStatus("current")
_Pm20002maAlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pm20002maAlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pm20002maAlmLineTxPowerHighWarningPortn = _Pm20002maAlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 12),
    _Pm20002maAlmLineTxPowerHighWarningPortn_Type()
)
pm20002maAlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxPowerHighWarningPortn.setStatus("current")
_Pm20002maAlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm20002maAlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pm20002maAlmLineTxPowerHighAlarmPortn = _Pm20002maAlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 13),
    _Pm20002maAlmLineTxPowerHighAlarmPortn_Type()
)
pm20002maAlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pm20002maAlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Pm20002maAlmLineBiasLowAlarmPortn_Object = MibTableColumn
pm20002maAlmLineBiasLowAlarmPortn = _Pm20002maAlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 14),
    _Pm20002maAlmLineBiasLowAlarmPortn_Type()
)
pm20002maAlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineBiasLowAlarmPortn.setStatus("current")
_Pm20002maAlmLineBiasLowWarningPortn_Type = EkiOnOff
_Pm20002maAlmLineBiasLowWarningPortn_Object = MibTableColumn
pm20002maAlmLineBiasLowWarningPortn = _Pm20002maAlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 15),
    _Pm20002maAlmLineBiasLowWarningPortn_Type()
)
pm20002maAlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineBiasLowWarningPortn.setStatus("current")
_Pm20002maAlmLineBiasHighWarningPortn_Type = EkiOnOff
_Pm20002maAlmLineBiasHighWarningPortn_Object = MibTableColumn
pm20002maAlmLineBiasHighWarningPortn = _Pm20002maAlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 16),
    _Pm20002maAlmLineBiasHighWarningPortn_Type()
)
pm20002maAlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineBiasHighWarningPortn.setStatus("current")
_Pm20002maAlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Pm20002maAlmLineBiasHighAlarmPortn_Object = MibTableColumn
pm20002maAlmLineBiasHighAlarmPortn = _Pm20002maAlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 184, 1, 17),
    _Pm20002maAlmLineBiasHighAlarmPortn_Type()
)
pm20002maAlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineBiasHighAlarmPortn.setStatus("current")
_Pm20002maAlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pm20002maAlmlineNetworkLaneAlarmWarning2Table = _Pm20002maAlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188)
)
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pm20002maAlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pm20002maAlmlineNetworkLaneAlarmWarning2Entry = _Pm20002maAlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1)
)
pm20002maAlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pm20002maAlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pm20002maAlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pm20002maAlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pm20002maAlmlineNetworkLaneAlarmWarning2Index = _Pm20002maAlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 1),
    _Pm20002maAlmlineNetworkLaneAlarmWarning2Index_Type()
)
pm20002maAlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pm20002maAlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Pm20002maAlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
pm20002maAlmTxModulatorBiasLowAlarmPortn = _Pm20002maAlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 2),
    _Pm20002maAlmTxModulatorBiasLowAlarmPortn_Type()
)
pm20002maAlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Pm20002maAlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Pm20002maAlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
pm20002maAlmTxModulatorBiasLowWarningPortn = _Pm20002maAlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 3),
    _Pm20002maAlmTxModulatorBiasLowWarningPortn_Type()
)
pm20002maAlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Pm20002maAlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Pm20002maAlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
pm20002maAlmTxModulatorBiasHighWarningPortn = _Pm20002maAlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 4),
    _Pm20002maAlmTxModulatorBiasHighWarningPortn_Type()
)
pm20002maAlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Pm20002maAlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Pm20002maAlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
pm20002maAlmTxModulatorBiasHighAlarmPortn = _Pm20002maAlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 5),
    _Pm20002maAlmTxModulatorBiasHighAlarmPortn_Type()
)
pm20002maAlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Pm20002maAlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
pm20002maAlmRxLaserTempLowAlarmPortn = _Pm20002maAlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 6),
    _Pm20002maAlmRxLaserTempLowAlarmPortn_Type()
)
pm20002maAlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserTempLowAlarmPortn.setStatus("current")
_Pm20002maAlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserTempLowWarningPortn_Object = MibTableColumn
pm20002maAlmRxLaserTempLowWarningPortn = _Pm20002maAlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 7),
    _Pm20002maAlmRxLaserTempLowWarningPortn_Type()
)
pm20002maAlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserTempLowWarningPortn.setStatus("current")
_Pm20002maAlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserTempHighWarningPortn_Object = MibTableColumn
pm20002maAlmRxLaserTempHighWarningPortn = _Pm20002maAlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 8),
    _Pm20002maAlmRxLaserTempHighWarningPortn_Type()
)
pm20002maAlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserTempHighWarningPortn.setStatus("current")
_Pm20002maAlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
pm20002maAlmRxLaserTempHighAlarmPortn = _Pm20002maAlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 9),
    _Pm20002maAlmRxLaserTempHighAlarmPortn_Type()
)
pm20002maAlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserTempHighAlarmPortn.setStatus("current")
_Pm20002maAlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
pm20002maAlmRxLaserOutputLowAlarmPortn = _Pm20002maAlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 10),
    _Pm20002maAlmRxLaserOutputLowAlarmPortn_Type()
)
pm20002maAlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Pm20002maAlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
pm20002maAlmRxLaserOutputLowWarningPortn = _Pm20002maAlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 11),
    _Pm20002maAlmRxLaserOutputLowWarningPortn_Type()
)
pm20002maAlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserOutputLowWarningPortn.setStatus("current")
_Pm20002maAlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
pm20002maAlmRxLaserOutputHighWarningPortn = _Pm20002maAlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 12),
    _Pm20002maAlmRxLaserOutputHighWarningPortn_Type()
)
pm20002maAlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserOutputHighWarningPortn.setStatus("current")
_Pm20002maAlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
pm20002maAlmRxLaserOutputHighAlarmPortn = _Pm20002maAlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 13),
    _Pm20002maAlmRxLaserOutputHighAlarmPortn_Type()
)
pm20002maAlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Pm20002maAlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
pm20002maAlmRxLaserBiasLowAlarmPortn = _Pm20002maAlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 14),
    _Pm20002maAlmRxLaserBiasLowAlarmPortn_Type()
)
pm20002maAlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Pm20002maAlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
pm20002maAlmRxLaserBiasLowWarningPortn = _Pm20002maAlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 15),
    _Pm20002maAlmRxLaserBiasLowWarningPortn_Type()
)
pm20002maAlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserBiasLowWarningPortn.setStatus("current")
_Pm20002maAlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
pm20002maAlmRxLaserBiasHighWarningPortn = _Pm20002maAlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 16),
    _Pm20002maAlmRxLaserBiasHighWarningPortn_Type()
)
pm20002maAlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserBiasHighWarningPortn.setStatus("current")
_Pm20002maAlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Pm20002maAlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
pm20002maAlmRxLaserBiasHighAlarmPortn = _Pm20002maAlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 1, 188, 1, 17),
    _Pm20002maAlmRxLaserBiasHighAlarmPortn_Type()
)
pm20002maAlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Pm20002maAlmLineUrg_ObjectIdentity = ObjectIdentity
pm20002maAlmLineUrg = _Pm20002maAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2)
)
_Pm20002maAlmlineNetworkLaneFaultTable_Object = MibTable
pm20002maAlmlineNetworkLaneFaultTable = _Pm20002maAlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192)
)
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneFaultTable.setStatus("current")
_Pm20002maAlmlineNetworkLaneFaultEntry_Object = MibTableRow
pm20002maAlmlineNetworkLaneFaultEntry = _Pm20002maAlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1)
)
pm20002maAlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneFaultEntry.setStatus("current")


class _Pm20002maAlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm20002maAlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm20002maAlmlineNetworkLaneFaultIndex_Object = MibTableColumn
pm20002maAlmlineNetworkLaneFaultIndex = _Pm20002maAlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 1),
    _Pm20002maAlmlineNetworkLaneFaultIndex_Type()
)
pm20002maAlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneFaultIndex.setStatus("current")
_Pm20002maAlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneRxTecFaultPortn_Object = MibTableColumn
pm20002maAlmLineLaneRxTecFaultPortn = _Pm20002maAlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 3),
    _Pm20002maAlmLineLaneRxTecFaultPortn_Type()
)
pm20002maAlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneRxTecFaultPortn.setStatus("current")
_Pm20002maAlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
pm20002maAlmLineLaneRxFifoErrorPortn = _Pm20002maAlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 4),
    _Pm20002maAlmLineLaneRxFifoErrorPortn_Type()
)
pm20002maAlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneRxFifoErrorPortn.setStatus("current")
_Pm20002maAlmLineLaneRxLolPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneRxLolPortn_Object = MibTableColumn
pm20002maAlmLineLaneRxLolPortn = _Pm20002maAlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 5),
    _Pm20002maAlmLineLaneRxLolPortn_Type()
)
pm20002maAlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneRxLolPortn.setStatus("current")
_Pm20002maAlmLineLaneRxLosPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneRxLosPortn_Object = MibTableColumn
pm20002maAlmLineLaneRxLosPortn = _Pm20002maAlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 6),
    _Pm20002maAlmLineLaneRxLosPortn_Type()
)
pm20002maAlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneRxLosPortn.setStatus("current")
_Pm20002maAlmLineLaneTxLolPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneTxLolPortn_Object = MibTableColumn
pm20002maAlmLineLaneTxLolPortn = _Pm20002maAlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 8),
    _Pm20002maAlmLineLaneTxLolPortn_Type()
)
pm20002maAlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneTxLolPortn.setStatus("current")
_Pm20002maAlmLineLaneTxLosfPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneTxLosfPortn_Object = MibTableColumn
pm20002maAlmLineLaneTxLosfPortn = _Pm20002maAlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 9),
    _Pm20002maAlmLineLaneTxLosfPortn_Type()
)
pm20002maAlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneTxLosfPortn.setStatus("current")
_Pm20002maAlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
pm20002maAlmLineLaneApdPowerSupplyPortn = _Pm20002maAlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 15),
    _Pm20002maAlmLineLaneApdPowerSupplyPortn_Type()
)
pm20002maAlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Pm20002maAlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm20002maAlmLineLaneWavelengthUnlockedPortn = _Pm20002maAlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 16),
    _Pm20002maAlmLineLaneWavelengthUnlockedPortn_Type()
)
pm20002maAlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Pm20002maAlmLineLaneTecFaultPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneTecFaultPortn_Object = MibTableColumn
pm20002maAlmLineLaneTecFaultPortn = _Pm20002maAlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 192, 1, 17),
    _Pm20002maAlmLineLaneTecFaultPortn_Type()
)
pm20002maAlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneTecFaultPortn.setStatus("current")
_Pm20002maAlmlineHostLaneFaultTable_Object = MibTable
pm20002maAlmlineHostLaneFaultTable = _Pm20002maAlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196)
)
if mibBuilder.loadTexts:
    pm20002maAlmlineHostLaneFaultTable.setStatus("current")
_Pm20002maAlmlineHostLaneFaultEntry_Object = MibTableRow
pm20002maAlmlineHostLaneFaultEntry = _Pm20002maAlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1)
)
pm20002maAlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm20002maAlmlineHostLaneFaultEntry.setStatus("current")


class _Pm20002maAlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pm20002maAlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm20002maAlmlineHostLaneFaultIndex_Object = MibTableColumn
pm20002maAlmlineHostLaneFaultIndex = _Pm20002maAlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1, 1),
    _Pm20002maAlmlineHostLaneFaultIndex_Type()
)
pm20002maAlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmlineHostLaneFaultIndex.setStatus("current")
_Pm20002maAlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pm20002maAlmLineInputLossOfSignalPortn_Object = MibTableColumn
pm20002maAlmLineInputLossOfSignalPortn = _Pm20002maAlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1, 2),
    _Pm20002maAlmLineInputLossOfSignalPortn_Type()
)
pm20002maAlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineInputLossOfSignalPortn.setStatus("current")
_Pm20002maAlmLineLossOfFramePortn_Type = EkiOnOff
_Pm20002maAlmLineLossOfFramePortn_Object = MibTableColumn
pm20002maAlmLineLossOfFramePortn = _Pm20002maAlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1, 3),
    _Pm20002maAlmLineLossOfFramePortn_Type()
)
pm20002maAlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLossOfFramePortn.setStatus("current")
_Pm20002maAlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pm20002maAlmLineSmBdiInsertedPortn_Object = MibTableColumn
pm20002maAlmLineSmBdiInsertedPortn = _Pm20002maAlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1, 4),
    _Pm20002maAlmLineSmBdiInsertedPortn_Type()
)
pm20002maAlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineSmBdiInsertedPortn.setStatus("current")
_Pm20002maAlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pm20002maAlmLineSmBdiDetectedPortn_Object = MibTableColumn
pm20002maAlmLineSmBdiDetectedPortn = _Pm20002maAlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1, 5),
    _Pm20002maAlmLineSmBdiDetectedPortn_Type()
)
pm20002maAlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineSmBdiDetectedPortn.setStatus("current")
_Pm20002maAlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pm20002maAlmLineSmIaeInsertedPortn_Object = MibTableColumn
pm20002maAlmLineSmIaeInsertedPortn = _Pm20002maAlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1, 6),
    _Pm20002maAlmLineSmIaeInsertedPortn_Type()
)
pm20002maAlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineSmIaeInsertedPortn.setStatus("current")
_Pm20002maAlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pm20002maAlmLineSmIaeDetectedPortn_Object = MibTableColumn
pm20002maAlmLineSmIaeDetectedPortn = _Pm20002maAlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1, 7),
    _Pm20002maAlmLineSmIaeDetectedPortn_Type()
)
pm20002maAlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineSmIaeDetectedPortn.setStatus("current")
_Pm20002maAlmLineTxHostLolPortn_Type = EkiOnOff
_Pm20002maAlmLineTxHostLolPortn_Object = MibTableColumn
pm20002maAlmLineTxHostLolPortn = _Pm20002maAlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1, 10),
    _Pm20002maAlmLineTxHostLolPortn_Type()
)
pm20002maAlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxHostLolPortn.setStatus("current")
_Pm20002maAlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm20002maAlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
pm20002maAlmLineLaneTxFifoErrorPortn = _Pm20002maAlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 196, 1, 11),
    _Pm20002maAlmLineLaneTxFifoErrorPortn_Type()
)
pm20002maAlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLaneTxFifoErrorPortn.setStatus("current")
_Pm20002maAlmlineNetworkLaneRxOtnTable_Object = MibTable
pm20002maAlmlineNetworkLaneRxOtnTable = _Pm20002maAlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200)
)
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneRxOtnTable.setStatus("current")
_Pm20002maAlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
pm20002maAlmlineNetworkLaneRxOtnEntry = _Pm20002maAlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1)
)
pm20002maAlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Pm20002maAlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type pm20002maAlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Pm20002maAlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
pm20002maAlmlineNetworkLaneRxOtnIndex = _Pm20002maAlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1, 1),
    _Pm20002maAlmlineNetworkLaneRxOtnIndex_Type()
)
pm20002maAlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Pm20002maAlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Pm20002maAlmLineRxOtnOduAisPortn_Object = MibTableColumn
pm20002maAlmLineRxOtnOduAisPortn = _Pm20002maAlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1, 10),
    _Pm20002maAlmLineRxOtnOduAisPortn_Type()
)
pm20002maAlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxOtnOduAisPortn.setStatus("current")
_Pm20002maAlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Pm20002maAlmLineRxOtnOtuAisPortn_Object = MibTableColumn
pm20002maAlmLineRxOtnOtuAisPortn = _Pm20002maAlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1, 11),
    _Pm20002maAlmLineRxOtnOtuAisPortn_Type()
)
pm20002maAlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxOtnOtuAisPortn.setStatus("current")
_Pm20002maAlmLineRxSmBdiPortn_Type = EkiOnOff
_Pm20002maAlmLineRxSmBdiPortn_Object = MibTableColumn
pm20002maAlmLineRxSmBdiPortn = _Pm20002maAlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1, 12),
    _Pm20002maAlmLineRxSmBdiPortn_Type()
)
pm20002maAlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxSmBdiPortn.setStatus("current")
_Pm20002maAlmLineRxOtnIaePortn_Type = EkiOnOff
_Pm20002maAlmLineRxOtnIaePortn_Object = MibTableColumn
pm20002maAlmLineRxOtnIaePortn = _Pm20002maAlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1, 13),
    _Pm20002maAlmLineRxOtnIaePortn_Type()
)
pm20002maAlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxOtnIaePortn.setStatus("current")
_Pm20002maAlmLineRxOtnOomPortn_Type = EkiOnOff
_Pm20002maAlmLineRxOtnOomPortn_Object = MibTableColumn
pm20002maAlmLineRxOtnOomPortn = _Pm20002maAlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1, 14),
    _Pm20002maAlmLineRxOtnOomPortn_Type()
)
pm20002maAlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxOtnOomPortn.setStatus("current")
_Pm20002maAlmLineRxOtnLomPortn_Type = EkiOnOff
_Pm20002maAlmLineRxOtnLomPortn_Object = MibTableColumn
pm20002maAlmLineRxOtnLomPortn = _Pm20002maAlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1, 15),
    _Pm20002maAlmLineRxOtnLomPortn_Type()
)
pm20002maAlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxOtnLomPortn.setStatus("current")
_Pm20002maAlmLineRxOtnOofPortn_Type = EkiOnOff
_Pm20002maAlmLineRxOtnOofPortn_Object = MibTableColumn
pm20002maAlmLineRxOtnOofPortn = _Pm20002maAlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1, 16),
    _Pm20002maAlmLineRxOtnOofPortn_Type()
)
pm20002maAlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxOtnOofPortn.setStatus("current")
_Pm20002maAlmLineRxOtnLofPortn_Type = EkiOnOff
_Pm20002maAlmLineRxOtnLofPortn_Object = MibTableColumn
pm20002maAlmLineRxOtnLofPortn = _Pm20002maAlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 200, 1, 17),
    _Pm20002maAlmLineRxOtnLofPortn_Type()
)
pm20002maAlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineRxOtnLofPortn.setStatus("current")
_Pm20002maAlmlineHostLaneTxOtnTable_Object = MibTable
pm20002maAlmlineHostLaneTxOtnTable = _Pm20002maAlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204)
)
if mibBuilder.loadTexts:
    pm20002maAlmlineHostLaneTxOtnTable.setStatus("current")
_Pm20002maAlmlineHostLaneTxOtnEntry_Object = MibTableRow
pm20002maAlmlineHostLaneTxOtnEntry = _Pm20002maAlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1)
)
pm20002maAlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm20002maAlmlineHostLaneTxOtnEntry.setStatus("current")


class _Pm20002maAlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type pm20002maAlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Pm20002maAlmlineHostLaneTxOtnIndex_Object = MibTableColumn
pm20002maAlmlineHostLaneTxOtnIndex = _Pm20002maAlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1, 1),
    _Pm20002maAlmlineHostLaneTxOtnIndex_Type()
)
pm20002maAlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmlineHostLaneTxOtnIndex.setStatus("current")
_Pm20002maAlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Pm20002maAlmLineTxOtnOduAisPortn_Object = MibTableColumn
pm20002maAlmLineTxOtnOduAisPortn = _Pm20002maAlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1, 10),
    _Pm20002maAlmLineTxOtnOduAisPortn_Type()
)
pm20002maAlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxOtnOduAisPortn.setStatus("current")
_Pm20002maAlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Pm20002maAlmLineTxOtnOtuAisPortn_Object = MibTableColumn
pm20002maAlmLineTxOtnOtuAisPortn = _Pm20002maAlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1, 11),
    _Pm20002maAlmLineTxOtnOtuAisPortn_Type()
)
pm20002maAlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxOtnOtuAisPortn.setStatus("current")
_Pm20002maAlmLineTxSmBdiPortn_Type = EkiOnOff
_Pm20002maAlmLineTxSmBdiPortn_Object = MibTableColumn
pm20002maAlmLineTxSmBdiPortn = _Pm20002maAlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1, 12),
    _Pm20002maAlmLineTxSmBdiPortn_Type()
)
pm20002maAlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxSmBdiPortn.setStatus("current")
_Pm20002maAlmLineTxOtnIaePortn_Type = EkiOnOff
_Pm20002maAlmLineTxOtnIaePortn_Object = MibTableColumn
pm20002maAlmLineTxOtnIaePortn = _Pm20002maAlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1, 13),
    _Pm20002maAlmLineTxOtnIaePortn_Type()
)
pm20002maAlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxOtnIaePortn.setStatus("current")
_Pm20002maAlmLineTxOtnOomPortn_Type = EkiOnOff
_Pm20002maAlmLineTxOtnOomPortn_Object = MibTableColumn
pm20002maAlmLineTxOtnOomPortn = _Pm20002maAlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1, 14),
    _Pm20002maAlmLineTxOtnOomPortn_Type()
)
pm20002maAlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxOtnOomPortn.setStatus("current")
_Pm20002maAlmLineTxOtnLomPortn_Type = EkiOnOff
_Pm20002maAlmLineTxOtnLomPortn_Object = MibTableColumn
pm20002maAlmLineTxOtnLomPortn = _Pm20002maAlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1, 15),
    _Pm20002maAlmLineTxOtnLomPortn_Type()
)
pm20002maAlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxOtnLomPortn.setStatus("current")
_Pm20002maAlmLineTxOtnOofPortn_Type = EkiOnOff
_Pm20002maAlmLineTxOtnOofPortn_Object = MibTableColumn
pm20002maAlmLineTxOtnOofPortn = _Pm20002maAlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1, 16),
    _Pm20002maAlmLineTxOtnOofPortn_Type()
)
pm20002maAlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxOtnOofPortn.setStatus("current")
_Pm20002maAlmLineTxOtnLofPortn_Type = EkiOnOff
_Pm20002maAlmLineTxOtnLofPortn_Object = MibTableColumn
pm20002maAlmLineTxOtnLofPortn = _Pm20002maAlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 2, 204, 1, 17),
    _Pm20002maAlmLineTxOtnLofPortn_Type()
)
pm20002maAlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineTxOtnLofPortn.setStatus("current")
_Pm20002maAlmLineCrit_ObjectIdentity = ObjectIdentity
pm20002maAlmLineCrit = _Pm20002maAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3)
)
_Pm20002maAlmsynthAlmLineTable_Object = MibTable
pm20002maAlmsynthAlmLineTable = _Pm20002maAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40)
)
if mibBuilder.loadTexts:
    pm20002maAlmsynthAlmLineTable.setStatus("current")
_Pm20002maAlmsynthAlmLineEntry_Object = MibTableRow
pm20002maAlmsynthAlmLineEntry = _Pm20002maAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1)
)
pm20002maAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm20002maAlmsynthAlmLineEntry.setStatus("current")


class _Pm20002maAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm20002maAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm20002maAlmsynthAlmLineIndex_Object = MibTableColumn
pm20002maAlmsynthAlmLineIndex = _Pm20002maAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 1),
    _Pm20002maAlmsynthAlmLineIndex_Type()
)
pm20002maAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmsynthAlmLineIndex.setStatus("current")
_Pm20002maAlmXfpAbsentPortn_Type = EkiOnOff
_Pm20002maAlmXfpAbsentPortn_Object = MibTableColumn
pm20002maAlmXfpAbsentPortn = _Pm20002maAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 2),
    _Pm20002maAlmXfpAbsentPortn_Type()
)
pm20002maAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmXfpAbsentPortn.setStatus("current")
_Pm20002maAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm20002maAlmXfpInitNotComplPortn_Object = MibTableColumn
pm20002maAlmXfpInitNotComplPortn = _Pm20002maAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 3),
    _Pm20002maAlmXfpInitNotComplPortn_Type()
)
pm20002maAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmXfpInitNotComplPortn.setStatus("current")
_Pm20002maAlmLineHwFailPortn_Type = EkiOnOff
_Pm20002maAlmLineHwFailPortn_Object = MibTableColumn
pm20002maAlmLineHwFailPortn = _Pm20002maAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 5),
    _Pm20002maAlmLineHwFailPortn_Type()
)
pm20002maAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineHwFailPortn.setStatus("current")
_Pm20002maAlmXfpTxOffPortn_Type = EkiOnOff
_Pm20002maAlmXfpTxOffPortn_Object = MibTableColumn
pm20002maAlmXfpTxOffPortn = _Pm20002maAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 6),
    _Pm20002maAlmXfpTxOffPortn_Type()
)
pm20002maAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmXfpTxOffPortn.setStatus("current")
_Pm20002maAlmLineLocalOosPortn_Type = EkiOnOff
_Pm20002maAlmLineLocalOosPortn_Object = MibTableColumn
pm20002maAlmLineLocalOosPortn = _Pm20002maAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 7),
    _Pm20002maAlmLineLocalOosPortn_Type()
)
pm20002maAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineLocalOosPortn.setStatus("current")
_Pm20002maAlmUpRdiInsPortn_Type = EkiOnOff
_Pm20002maAlmUpRdiInsPortn_Object = MibTableColumn
pm20002maAlmUpRdiInsPortn = _Pm20002maAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 9),
    _Pm20002maAlmUpRdiInsPortn_Type()
)
pm20002maAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmUpRdiInsPortn.setStatus("current")
_Pm20002maAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm20002maAlmLineDdmWarningPortn_Object = MibTableColumn
pm20002maAlmLineDdmWarningPortn = _Pm20002maAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 10),
    _Pm20002maAlmLineDdmWarningPortn_Type()
)
pm20002maAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineDdmWarningPortn.setStatus("current")
_Pm20002maAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm20002maAlmLineDdmAlmPortn_Object = MibTableColumn
pm20002maAlmLineDdmAlmPortn = _Pm20002maAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 11),
    _Pm20002maAlmLineDdmAlmPortn_Type()
)
pm20002maAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineDdmAlmPortn.setStatus("current")
_Pm20002maAlmLineFailPortn_Type = EkiOnOff
_Pm20002maAlmLineFailPortn_Object = MibTableColumn
pm20002maAlmLineFailPortn = _Pm20002maAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 13),
    _Pm20002maAlmLineFailPortn_Type()
)
pm20002maAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineFailPortn.setStatus("current")
_Pm20002maAlmLineActivePortn_Type = EkiOnOff
_Pm20002maAlmLineActivePortn_Object = MibTableColumn
pm20002maAlmLineActivePortn = _Pm20002maAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 2, 3, 3, 40, 1, 17),
    _Pm20002maAlmLineActivePortn_Type()
)
pm20002maAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maAlmLineActivePortn.setStatus("current")
_Pm20002mameasures_ObjectIdentity = ObjectIdentity
pm20002mameasures = _Pm20002mameasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3)
)
_Pm20002maMesrOther_ObjectIdentity = ObjectIdentity
pm20002maMesrOther = _Pm20002maMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1)
)
_Pm20002maMesrsynth0_Type = EkiMeasureType
_Pm20002maMesrsynth0_Object = MibScalar
pm20002maMesrsynth0 = _Pm20002maMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 0),
    _Pm20002maMesrsynth0_Type()
)
pm20002maMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrsynth0.setStatus("deprecated")
_Pm20002maMesrsynth1_Type = EkiMeasureType
_Pm20002maMesrsynth1_Object = MibScalar
pm20002maMesrsynth1 = _Pm20002maMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 1),
    _Pm20002maMesrsynth1_Type()
)
pm20002maMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrsynth1.setStatus("deprecated")


class _Pm20002maMesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pm20002maMesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pm20002maMesrpmIntervalNumber_Object = MibScalar
pm20002maMesrpmIntervalNumber = _Pm20002maMesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 7),
    _Pm20002maMesrpmIntervalNumber_Type()
)
pm20002maMesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrpmIntervalNumber.setStatus("current")


class _Pm20002maMesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pm20002maMesrlineNetTxLaserOutputPwrAverage = _Pm20002maMesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 196),
    _Pm20002maMesrlineNetTxLaserOutputPwrAverage_Type()
)
pm20002maMesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pm20002maMesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetTxLaserTempAverage_Object = MibScalar
pm20002maMesrlineNetTxLaserTempAverage = _Pm20002maMesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 197),
    _Pm20002maMesrlineNetTxLaserTempAverage_Type()
)
pm20002maMesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserTempAverage.setStatus("current")


class _Pm20002maMesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetTxBiasCurrentAverage_Object = MibScalar
pm20002maMesrlineNetTxBiasCurrentAverage = _Pm20002maMesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 198),
    _Pm20002maMesrlineNetTxBiasCurrentAverage_Type()
)
pm20002maMesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pm20002maMesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetRxInputPwrAverage_Object = MibScalar
pm20002maMesrlineNetRxInputPwrAverage = _Pm20002maMesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 199),
    _Pm20002maMesrlineNetRxInputPwrAverage_Type()
)
pm20002maMesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetRxInputPwrAverage.setStatus("current")


class _Pm20002maMesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pm20002maMesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineResidualChromaticDispAverage_Object = MibScalar
pm20002maMesrlineResidualChromaticDispAverage = _Pm20002maMesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 200),
    _Pm20002maMesrlineResidualChromaticDispAverage_Type()
)
pm20002maMesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineResidualChromaticDispAverage.setStatus("current")


class _Pm20002maMesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pm20002maMesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineDiffGroupDelayAverage_Object = MibScalar
pm20002maMesrlineDiffGroupDelayAverage = _Pm20002maMesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 201),
    _Pm20002maMesrlineDiffGroupDelayAverage_Type()
)
pm20002maMesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineDiffGroupDelayAverage.setStatus("current")


class _Pm20002maMesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pm20002maMesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineQFactorAverage_Object = MibScalar
pm20002maMesrlineQFactorAverage = _Pm20002maMesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 202),
    _Pm20002maMesrlineQFactorAverage_Type()
)
pm20002maMesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineQFactorAverage.setStatus("current")


class _Pm20002maMesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pm20002maMesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineCarrierFreqOffsetAverage_Object = MibScalar
pm20002maMesrlineCarrierFreqOffsetAverage = _Pm20002maMesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 203),
    _Pm20002maMesrlineCarrierFreqOffsetAverage_Type()
)
pm20002maMesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pm20002maMesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pm20002maMesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineOsnrAverage_Object = MibScalar
pm20002maMesrlineOsnrAverage = _Pm20002maMesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 204),
    _Pm20002maMesrlineOsnrAverage_Type()
)
pm20002maMesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineOsnrAverage.setStatus("current")


class _Pm20002maMesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pm20002maMesrlineNetTxLaserOutputPwrMin = _Pm20002maMesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 212),
    _Pm20002maMesrlineNetTxLaserOutputPwrMin_Type()
)
pm20002maMesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pm20002maMesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetTxLaserTempMin_Object = MibScalar
pm20002maMesrlineNetTxLaserTempMin = _Pm20002maMesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 213),
    _Pm20002maMesrlineNetTxLaserTempMin_Type()
)
pm20002maMesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserTempMin.setStatus("current")


class _Pm20002maMesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetTxBiasCurrentMin_Object = MibScalar
pm20002maMesrlineNetTxBiasCurrentMin = _Pm20002maMesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 214),
    _Pm20002maMesrlineNetTxBiasCurrentMin_Type()
)
pm20002maMesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pm20002maMesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetRxInputPwrMin_Object = MibScalar
pm20002maMesrlineNetRxInputPwrMin = _Pm20002maMesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 215),
    _Pm20002maMesrlineNetRxInputPwrMin_Type()
)
pm20002maMesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetRxInputPwrMin.setStatus("current")


class _Pm20002maMesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pm20002maMesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineResidualChromaticDispMin_Object = MibScalar
pm20002maMesrlineResidualChromaticDispMin = _Pm20002maMesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 216),
    _Pm20002maMesrlineResidualChromaticDispMin_Type()
)
pm20002maMesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineResidualChromaticDispMin.setStatus("current")


class _Pm20002maMesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pm20002maMesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineDiffGroupDelayMin_Object = MibScalar
pm20002maMesrlineDiffGroupDelayMin = _Pm20002maMesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 217),
    _Pm20002maMesrlineDiffGroupDelayMin_Type()
)
pm20002maMesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineDiffGroupDelayMin.setStatus("current")


class _Pm20002maMesrlineQFactorMin_Type(Unsigned32):
    """Custom type pm20002maMesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineQFactorMin_Object = MibScalar
pm20002maMesrlineQFactorMin = _Pm20002maMesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 218),
    _Pm20002maMesrlineQFactorMin_Type()
)
pm20002maMesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineQFactorMin.setStatus("current")


class _Pm20002maMesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pm20002maMesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineCarrierFreqOffsetMin_Object = MibScalar
pm20002maMesrlineCarrierFreqOffsetMin = _Pm20002maMesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 219),
    _Pm20002maMesrlineCarrierFreqOffsetMin_Type()
)
pm20002maMesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pm20002maMesrlineOsnrMin_Type(Unsigned32):
    """Custom type pm20002maMesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineOsnrMin_Object = MibScalar
pm20002maMesrlineOsnrMin = _Pm20002maMesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 220),
    _Pm20002maMesrlineOsnrMin_Type()
)
pm20002maMesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineOsnrMin.setStatus("current")


class _Pm20002maMesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pm20002maMesrlineNetTxLaserOutputPwrMax = _Pm20002maMesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 228),
    _Pm20002maMesrlineNetTxLaserOutputPwrMax_Type()
)
pm20002maMesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pm20002maMesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetTxLaserTempMax_Object = MibScalar
pm20002maMesrlineNetTxLaserTempMax = _Pm20002maMesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 229),
    _Pm20002maMesrlineNetTxLaserTempMax_Type()
)
pm20002maMesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserTempMax.setStatus("current")


class _Pm20002maMesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetTxBiasCurrentMax_Object = MibScalar
pm20002maMesrlineNetTxBiasCurrentMax = _Pm20002maMesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 230),
    _Pm20002maMesrlineNetTxBiasCurrentMax_Type()
)
pm20002maMesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pm20002maMesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pm20002maMesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineNetRxInputPwrMax_Object = MibScalar
pm20002maMesrlineNetRxInputPwrMax = _Pm20002maMesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 231),
    _Pm20002maMesrlineNetRxInputPwrMax_Type()
)
pm20002maMesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetRxInputPwrMax.setStatus("current")


class _Pm20002maMesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pm20002maMesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineResidualChromaticDispMax_Object = MibScalar
pm20002maMesrlineResidualChromaticDispMax = _Pm20002maMesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 232),
    _Pm20002maMesrlineResidualChromaticDispMax_Type()
)
pm20002maMesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineResidualChromaticDispMax.setStatus("current")


class _Pm20002maMesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pm20002maMesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineDiffGroupDelayMax_Object = MibScalar
pm20002maMesrlineDiffGroupDelayMax = _Pm20002maMesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 233),
    _Pm20002maMesrlineDiffGroupDelayMax_Type()
)
pm20002maMesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineDiffGroupDelayMax.setStatus("current")


class _Pm20002maMesrlineQFactorMax_Type(Unsigned32):
    """Custom type pm20002maMesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineQFactorMax_Object = MibScalar
pm20002maMesrlineQFactorMax = _Pm20002maMesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 234),
    _Pm20002maMesrlineQFactorMax_Type()
)
pm20002maMesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineQFactorMax.setStatus("current")


class _Pm20002maMesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pm20002maMesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineCarrierFreqOffsetMax_Object = MibScalar
pm20002maMesrlineCarrierFreqOffsetMax = _Pm20002maMesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 235),
    _Pm20002maMesrlineCarrierFreqOffsetMax_Type()
)
pm20002maMesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pm20002maMesrlineOsnrMax_Type(Unsigned32):
    """Custom type pm20002maMesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineOsnrMax_Object = MibScalar
pm20002maMesrlineOsnrMax = _Pm20002maMesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 236),
    _Pm20002maMesrlineOsnrMax_Type()
)
pm20002maMesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineOsnrMax.setStatus("current")


class _Pm20002maMesrtrscv1Temp_Type(Unsigned32):
    """Custom type pm20002maMesrtrscv1Temp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrtrscv1Temp_Type.__name__ = "Unsigned32"
_Pm20002maMesrtrscv1Temp_Object = MibScalar
pm20002maMesrtrscv1Temp = _Pm20002maMesrtrscv1Temp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 252),
    _Pm20002maMesrtrscv1Temp_Type()
)
pm20002maMesrtrscv1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrtrscv1Temp.setStatus("current")


class _Pm20002maMesrtrscv2Temp_Type(Unsigned32):
    """Custom type pm20002maMesrtrscv2Temp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrtrscv2Temp_Type.__name__ = "Unsigned32"
_Pm20002maMesrtrscv2Temp_Object = MibScalar
pm20002maMesrtrscv2Temp = _Pm20002maMesrtrscv2Temp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 253),
    _Pm20002maMesrtrscv2Temp_Type()
)
pm20002maMesrtrscv2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrtrscv2Temp.setStatus("current")


class _Pm20002maMesrtrscv1PowerSupply_Type(Unsigned32):
    """Custom type pm20002maMesrtrscv1PowerSupply based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrtrscv1PowerSupply_Type.__name__ = "Unsigned32"
_Pm20002maMesrtrscv1PowerSupply_Object = MibScalar
pm20002maMesrtrscv1PowerSupply = _Pm20002maMesrtrscv1PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 254),
    _Pm20002maMesrtrscv1PowerSupply_Type()
)
pm20002maMesrtrscv1PowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrtrscv1PowerSupply.setStatus("current")


class _Pm20002maMesrtrscv2PowerSupply_Type(Unsigned32):
    """Custom type pm20002maMesrtrscv2PowerSupply based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrtrscv2PowerSupply_Type.__name__ = "Unsigned32"
_Pm20002maMesrtrscv2PowerSupply_Object = MibScalar
pm20002maMesrtrscv2PowerSupply = _Pm20002maMesrtrscv2PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 1, 255),
    _Pm20002maMesrtrscv2PowerSupply_Type()
)
pm20002maMesrtrscv2PowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrtrscv2PowerSupply.setStatus("current")
_Pm20002maMesrClient_ObjectIdentity = ObjectIdentity
pm20002maMesrClient = _Pm20002maMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2)
)


class _Pm20002maMesrclientCfpTemp_Type(Unsigned32):
    """Custom type pm20002maMesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Pm20002maMesrclientCfpTemp_Object = MibScalar
pm20002maMesrclientCfpTemp = _Pm20002maMesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 8),
    _Pm20002maMesrclientCfpTemp_Type()
)
pm20002maMesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientCfpTemp.setStatus("current")


class _Pm20002maMesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type pm20002maMesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Pm20002maMesrclientCfp3v3Voltage_Object = MibScalar
pm20002maMesrclientCfp3v3Voltage = _Pm20002maMesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 9),
    _Pm20002maMesrclientCfp3v3Voltage_Type()
)
pm20002maMesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientCfp3v3Voltage.setStatus("current")


class _Pm20002maMesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm20002maMesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm20002maMesrclientSoaBiasCurrent_Object = MibScalar
pm20002maMesrclientSoaBiasCurrent = _Pm20002maMesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 10),
    _Pm20002maMesrclientSoaBiasCurrent_Type()
)
pm20002maMesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientSoaBiasCurrent.setStatus("current")
_Pm20002maMesrclientTxPwrMinTable_Object = MibTable
pm20002maMesrclientTxPwrMinTable = _Pm20002maMesrclientTxPwrMinTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm20002maMesrclientTxPwrMinTable.setStatus("current")
_Pm20002maMesrclientTxPwrMinEntry_Object = MibTableRow
pm20002maMesrclientTxPwrMinEntry = _Pm20002maMesrclientTxPwrMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 16, 1)
)
pm20002maMesrclientTxPwrMinEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrclientTxPwrMinIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrclientTxPwrMinEntry.setStatus("current")


class _Pm20002maMesrclientTxPwrMinIndex_Type(Integer32):
    """Custom type pm20002maMesrclientTxPwrMinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrclientTxPwrMinIndex_Type.__name__ = "Integer32"
_Pm20002maMesrclientTxPwrMinIndex_Object = MibTableColumn
pm20002maMesrclientTxPwrMinIndex = _Pm20002maMesrclientTxPwrMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 16, 1, 1),
    _Pm20002maMesrclientTxPwrMinIndex_Type()
)
pm20002maMesrclientTxPwrMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientTxPwrMinIndex.setStatus("current")


class _Pm20002maMesrclientTxPwrMinPortn_Type(Integer32):
    """Custom type pm20002maMesrclientTxPwrMinPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrclientTxPwrMinPortn_Type.__name__ = "Integer32"
_Pm20002maMesrclientTxPwrMinPortn_Object = MibTableColumn
pm20002maMesrclientTxPwrMinPortn = _Pm20002maMesrclientTxPwrMinPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 16, 1, 2),
    _Pm20002maMesrclientTxPwrMinPortn_Type()
)
pm20002maMesrclientTxPwrMinPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientTxPwrMinPortn.setStatus("current")
_Pm20002maMesrclientRxPwrMinTable_Object = MibTable
pm20002maMesrclientRxPwrMinTable = _Pm20002maMesrclientRxPwrMinTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm20002maMesrclientRxPwrMinTable.setStatus("current")
_Pm20002maMesrclientRxPwrMinEntry_Object = MibTableRow
pm20002maMesrclientRxPwrMinEntry = _Pm20002maMesrclientRxPwrMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 48, 1)
)
pm20002maMesrclientRxPwrMinEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrclientRxPwrMinIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrclientRxPwrMinEntry.setStatus("current")


class _Pm20002maMesrclientRxPwrMinIndex_Type(Integer32):
    """Custom type pm20002maMesrclientRxPwrMinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrclientRxPwrMinIndex_Type.__name__ = "Integer32"
_Pm20002maMesrclientRxPwrMinIndex_Object = MibTableColumn
pm20002maMesrclientRxPwrMinIndex = _Pm20002maMesrclientRxPwrMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 48, 1, 1),
    _Pm20002maMesrclientRxPwrMinIndex_Type()
)
pm20002maMesrclientRxPwrMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientRxPwrMinIndex.setStatus("current")


class _Pm20002maMesrclientRxPwrMinPortn_Type(Integer32):
    """Custom type pm20002maMesrclientRxPwrMinPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrclientRxPwrMinPortn_Type.__name__ = "Integer32"
_Pm20002maMesrclientRxPwrMinPortn_Object = MibTableColumn
pm20002maMesrclientRxPwrMinPortn = _Pm20002maMesrclientRxPwrMinPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 48, 1, 2),
    _Pm20002maMesrclientRxPwrMinPortn_Type()
)
pm20002maMesrclientRxPwrMinPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientRxPwrMinPortn.setStatus("current")
_Pm20002maMesrclientTxPwrMaxTable_Object = MibTable
pm20002maMesrclientTxPwrMaxTable = _Pm20002maMesrclientTxPwrMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 80)
)
if mibBuilder.loadTexts:
    pm20002maMesrclientTxPwrMaxTable.setStatus("current")
_Pm20002maMesrclientTxPwrMaxEntry_Object = MibTableRow
pm20002maMesrclientTxPwrMaxEntry = _Pm20002maMesrclientTxPwrMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 80, 1)
)
pm20002maMesrclientTxPwrMaxEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrclientTxPwrMaxIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrclientTxPwrMaxEntry.setStatus("current")


class _Pm20002maMesrclientTxPwrMaxIndex_Type(Integer32):
    """Custom type pm20002maMesrclientTxPwrMaxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrclientTxPwrMaxIndex_Type.__name__ = "Integer32"
_Pm20002maMesrclientTxPwrMaxIndex_Object = MibTableColumn
pm20002maMesrclientTxPwrMaxIndex = _Pm20002maMesrclientTxPwrMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 80, 1, 1),
    _Pm20002maMesrclientTxPwrMaxIndex_Type()
)
pm20002maMesrclientTxPwrMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientTxPwrMaxIndex.setStatus("current")


class _Pm20002maMesrclientTxPwrMaxPortn_Type(Integer32):
    """Custom type pm20002maMesrclientTxPwrMaxPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrclientTxPwrMaxPortn_Type.__name__ = "Integer32"
_Pm20002maMesrclientTxPwrMaxPortn_Object = MibTableColumn
pm20002maMesrclientTxPwrMaxPortn = _Pm20002maMesrclientTxPwrMaxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 80, 1, 2),
    _Pm20002maMesrclientTxPwrMaxPortn_Type()
)
pm20002maMesrclientTxPwrMaxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientTxPwrMaxPortn.setStatus("current")
_Pm20002maMesrclientRxPwrMaxTable_Object = MibTable
pm20002maMesrclientRxPwrMaxTable = _Pm20002maMesrclientRxPwrMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 112)
)
if mibBuilder.loadTexts:
    pm20002maMesrclientRxPwrMaxTable.setStatus("current")
_Pm20002maMesrclientRxPwrMaxEntry_Object = MibTableRow
pm20002maMesrclientRxPwrMaxEntry = _Pm20002maMesrclientRxPwrMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 112, 1)
)
pm20002maMesrclientRxPwrMaxEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrclientRxPwrMaxIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrclientRxPwrMaxEntry.setStatus("current")


class _Pm20002maMesrclientRxPwrMaxIndex_Type(Integer32):
    """Custom type pm20002maMesrclientRxPwrMaxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrclientRxPwrMaxIndex_Type.__name__ = "Integer32"
_Pm20002maMesrclientRxPwrMaxIndex_Object = MibTableColumn
pm20002maMesrclientRxPwrMaxIndex = _Pm20002maMesrclientRxPwrMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 112, 1, 1),
    _Pm20002maMesrclientRxPwrMaxIndex_Type()
)
pm20002maMesrclientRxPwrMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientRxPwrMaxIndex.setStatus("current")


class _Pm20002maMesrclientRxPwrMaxPortn_Type(Integer32):
    """Custom type pm20002maMesrclientRxPwrMaxPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrclientRxPwrMaxPortn_Type.__name__ = "Integer32"
_Pm20002maMesrclientRxPwrMaxPortn_Object = MibTableColumn
pm20002maMesrclientRxPwrMaxPortn = _Pm20002maMesrclientRxPwrMaxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 2, 112, 1, 2),
    _Pm20002maMesrclientRxPwrMaxPortn_Type()
)
pm20002maMesrclientRxPwrMaxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrclientRxPwrMaxPortn.setStatus("current")
_Pm20002maMesrLine_ObjectIdentity = ObjectIdentity
pm20002maMesrLine = _Pm20002maMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3)
)


class _Pm20002maMesrlineMsaTemp_Type(Unsigned32):
    """Custom type pm20002maMesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineMsaTemp_Object = MibScalar
pm20002maMesrlineMsaTemp = _Pm20002maMesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 12),
    _Pm20002maMesrlineMsaTemp_Type()
)
pm20002maMesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineMsaTemp.setStatus("current")


class _Pm20002maMesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type pm20002maMesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineMsa3v3Voltage_Object = MibScalar
pm20002maMesrlineMsa3v3Voltage = _Pm20002maMesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 13),
    _Pm20002maMesrlineMsa3v3Voltage_Type()
)
pm20002maMesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineMsa3v3Voltage.setStatus("current")


class _Pm20002maMesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm20002maMesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm20002maMesrlineSoaBiasCurrent_Object = MibScalar
pm20002maMesrlineSoaBiasCurrent = _Pm20002maMesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 14),
    _Pm20002maMesrlineSoaBiasCurrent_Type()
)
pm20002maMesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineSoaBiasCurrent.setStatus("current")
_Pm20002maMesrlineNetTxLaserOutputPwrTable_Object = MibTable
pm20002maMesrlineNetTxLaserOutputPwrTable = _Pm20002maMesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pm20002maMesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pm20002maMesrlineNetTxLaserOutputPwrEntry = _Pm20002maMesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 144, 1)
)
pm20002maMesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pm20002maMesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pm20002maMesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pm20002maMesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pm20002maMesrlineNetTxLaserOutputPwrIndex = _Pm20002maMesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 144, 1, 1),
    _Pm20002maMesrlineNetTxLaserOutputPwrIndex_Type()
)
pm20002maMesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pm20002maMesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pm20002maMesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pm20002maMesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pm20002maMesrlineNetTxLaserOutputPwrPortn = _Pm20002maMesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 144, 1, 2),
    _Pm20002maMesrlineNetTxLaserOutputPwrPortn_Type()
)
pm20002maMesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pm20002maMesrlineNetTxLaserTempTable_Object = MibTable
pm20002maMesrlineNetTxLaserTempTable = _Pm20002maMesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserTempTable.setStatus("current")
_Pm20002maMesrlineNetTxLaserTempEntry_Object = MibTableRow
pm20002maMesrlineNetTxLaserTempEntry = _Pm20002maMesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 148, 1)
)
pm20002maMesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserTempEntry.setStatus("current")


class _Pm20002maMesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pm20002maMesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pm20002maMesrlineNetTxLaserTempIndex_Object = MibTableColumn
pm20002maMesrlineNetTxLaserTempIndex = _Pm20002maMesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 148, 1, 1),
    _Pm20002maMesrlineNetTxLaserTempIndex_Type()
)
pm20002maMesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserTempIndex.setStatus("current")


class _Pm20002maMesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pm20002maMesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pm20002maMesrlineNetTxLaserTempPortn_Object = MibTableColumn
pm20002maMesrlineNetTxLaserTempPortn = _Pm20002maMesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 148, 1, 2),
    _Pm20002maMesrlineNetTxLaserTempPortn_Type()
)
pm20002maMesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxLaserTempPortn.setStatus("current")
_Pm20002maMesrlineNetTxBiasCurrentTable_Object = MibTable
pm20002maMesrlineNetTxBiasCurrentTable = _Pm20002maMesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxBiasCurrentTable.setStatus("current")
_Pm20002maMesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pm20002maMesrlineNetTxBiasCurrentEntry = _Pm20002maMesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 152, 1)
)
pm20002maMesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pm20002maMesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pm20002maMesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pm20002maMesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pm20002maMesrlineNetTxBiasCurrentIndex = _Pm20002maMesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 152, 1, 1),
    _Pm20002maMesrlineNetTxBiasCurrentIndex_Type()
)
pm20002maMesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pm20002maMesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pm20002maMesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pm20002maMesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pm20002maMesrlineNetTxBiasCurrentPortn = _Pm20002maMesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 152, 1, 2),
    _Pm20002maMesrlineNetTxBiasCurrentPortn_Type()
)
pm20002maMesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pm20002maMesrlineNetRxInputPwrTable_Object = MibTable
pm20002maMesrlineNetRxInputPwrTable = _Pm20002maMesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pm20002maMesrlineNetRxInputPwrTable.setStatus("current")
_Pm20002maMesrlineNetRxInputPwrEntry_Object = MibTableRow
pm20002maMesrlineNetRxInputPwrEntry = _Pm20002maMesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 156, 1)
)
pm20002maMesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrlineNetRxInputPwrEntry.setStatus("current")


class _Pm20002maMesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pm20002maMesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pm20002maMesrlineNetRxInputPwrIndex_Object = MibTableColumn
pm20002maMesrlineNetRxInputPwrIndex = _Pm20002maMesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 156, 1, 1),
    _Pm20002maMesrlineNetRxInputPwrIndex_Type()
)
pm20002maMesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetRxInputPwrIndex.setStatus("current")


class _Pm20002maMesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pm20002maMesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pm20002maMesrlineNetRxInputPwrPortn_Object = MibTableColumn
pm20002maMesrlineNetRxInputPwrPortn = _Pm20002maMesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 156, 1, 2),
    _Pm20002maMesrlineNetRxInputPwrPortn_Type()
)
pm20002maMesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineNetRxInputPwrPortn.setStatus("current")
_Pm20002maMesrlineResidualChromaticDispTable_Object = MibTable
pm20002maMesrlineResidualChromaticDispTable = _Pm20002maMesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm20002maMesrlineResidualChromaticDispTable.setStatus("current")
_Pm20002maMesrlineResidualChromaticDispEntry_Object = MibTableRow
pm20002maMesrlineResidualChromaticDispEntry = _Pm20002maMesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 160, 1)
)
pm20002maMesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrlineResidualChromaticDispEntry.setStatus("current")


class _Pm20002maMesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pm20002maMesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pm20002maMesrlineResidualChromaticDispIndex_Object = MibTableColumn
pm20002maMesrlineResidualChromaticDispIndex = _Pm20002maMesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 160, 1, 1),
    _Pm20002maMesrlineResidualChromaticDispIndex_Type()
)
pm20002maMesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineResidualChromaticDispIndex.setStatus("current")


class _Pm20002maMesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pm20002maMesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pm20002maMesrlineResidualChromaticDispPortn_Object = MibTableColumn
pm20002maMesrlineResidualChromaticDispPortn = _Pm20002maMesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 160, 1, 2),
    _Pm20002maMesrlineResidualChromaticDispPortn_Type()
)
pm20002maMesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineResidualChromaticDispPortn.setStatus("current")
_Pm20002maMesrlineDiffGroupDelayTable_Object = MibTable
pm20002maMesrlineDiffGroupDelayTable = _Pm20002maMesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 164)
)
if mibBuilder.loadTexts:
    pm20002maMesrlineDiffGroupDelayTable.setStatus("current")
_Pm20002maMesrlineDiffGroupDelayEntry_Object = MibTableRow
pm20002maMesrlineDiffGroupDelayEntry = _Pm20002maMesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 164, 1)
)
pm20002maMesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrlineDiffGroupDelayEntry.setStatus("current")


class _Pm20002maMesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pm20002maMesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pm20002maMesrlineDiffGroupDelayIndex_Object = MibTableColumn
pm20002maMesrlineDiffGroupDelayIndex = _Pm20002maMesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 164, 1, 1),
    _Pm20002maMesrlineDiffGroupDelayIndex_Type()
)
pm20002maMesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineDiffGroupDelayIndex.setStatus("current")


class _Pm20002maMesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pm20002maMesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pm20002maMesrlineDiffGroupDelayPortn_Object = MibTableColumn
pm20002maMesrlineDiffGroupDelayPortn = _Pm20002maMesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 164, 1, 2),
    _Pm20002maMesrlineDiffGroupDelayPortn_Type()
)
pm20002maMesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineDiffGroupDelayPortn.setStatus("current")
_Pm20002maMesrlineQFactorTable_Object = MibTable
pm20002maMesrlineQFactorTable = _Pm20002maMesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 168)
)
if mibBuilder.loadTexts:
    pm20002maMesrlineQFactorTable.setStatus("current")
_Pm20002maMesrlineQFactorEntry_Object = MibTableRow
pm20002maMesrlineQFactorEntry = _Pm20002maMesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 168, 1)
)
pm20002maMesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrlineQFactorEntry.setStatus("current")


class _Pm20002maMesrlineQFactorIndex_Type(Integer32):
    """Custom type pm20002maMesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pm20002maMesrlineQFactorIndex_Object = MibTableColumn
pm20002maMesrlineQFactorIndex = _Pm20002maMesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 168, 1, 1),
    _Pm20002maMesrlineQFactorIndex_Type()
)
pm20002maMesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineQFactorIndex.setStatus("current")


class _Pm20002maMesrlineQFactorPortn_Type(Integer32):
    """Custom type pm20002maMesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pm20002maMesrlineQFactorPortn_Object = MibTableColumn
pm20002maMesrlineQFactorPortn = _Pm20002maMesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 168, 1, 2),
    _Pm20002maMesrlineQFactorPortn_Type()
)
pm20002maMesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineQFactorPortn.setStatus("current")
_Pm20002maMesrlineCarrierFreqOffsetTable_Object = MibTable
pm20002maMesrlineCarrierFreqOffsetTable = _Pm20002maMesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 172)
)
if mibBuilder.loadTexts:
    pm20002maMesrlineCarrierFreqOffsetTable.setStatus("current")
_Pm20002maMesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pm20002maMesrlineCarrierFreqOffsetEntry = _Pm20002maMesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 172, 1)
)
pm20002maMesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pm20002maMesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pm20002maMesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pm20002maMesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pm20002maMesrlineCarrierFreqOffsetIndex = _Pm20002maMesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 172, 1, 1),
    _Pm20002maMesrlineCarrierFreqOffsetIndex_Type()
)
pm20002maMesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pm20002maMesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pm20002maMesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pm20002maMesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pm20002maMesrlineCarrierFreqOffsetPortn = _Pm20002maMesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 172, 1, 2),
    _Pm20002maMesrlineCarrierFreqOffsetPortn_Type()
)
pm20002maMesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pm20002maMesrlineOsnrTable_Object = MibTable
pm20002maMesrlineOsnrTable = _Pm20002maMesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 176)
)
if mibBuilder.loadTexts:
    pm20002maMesrlineOsnrTable.setStatus("current")
_Pm20002maMesrlineOsnrEntry_Object = MibTableRow
pm20002maMesrlineOsnrEntry = _Pm20002maMesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 176, 1)
)
pm20002maMesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMesrlineOsnrEntry.setStatus("current")


class _Pm20002maMesrlineOsnrIndex_Type(Integer32):
    """Custom type pm20002maMesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pm20002maMesrlineOsnrIndex_Object = MibTableColumn
pm20002maMesrlineOsnrIndex = _Pm20002maMesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 176, 1, 1),
    _Pm20002maMesrlineOsnrIndex_Type()
)
pm20002maMesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineOsnrIndex.setStatus("current")


class _Pm20002maMesrlineOsnrPortn_Type(Integer32):
    """Custom type pm20002maMesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20002maMesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pm20002maMesrlineOsnrPortn_Object = MibTableColumn
pm20002maMesrlineOsnrPortn = _Pm20002maMesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 3, 3, 176, 1, 2),
    _Pm20002maMesrlineOsnrPortn_Type()
)
pm20002maMesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMesrlineOsnrPortn.setStatus("current")
_Pm20002macounters_ObjectIdentity = ObjectIdentity
pm20002macounters = _Pm20002macounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4)
)
_Pm20002maCntOther_ObjectIdentity = ObjectIdentity
pm20002maCntOther = _Pm20002maCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 1)
)
_Pm20002maCntClient_ObjectIdentity = ObjectIdentity
pm20002maCntClient = _Pm20002maCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2)
)
_Pm20002maCntclientInputErrorCounterTable_Object = MibTable
pm20002maCntclientInputErrorCounterTable = _Pm20002maCntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 112)
)
if mibBuilder.loadTexts:
    pm20002maCntclientInputErrorCounterTable.setStatus("current")
_Pm20002maCntclientInputErrorCounterEntry_Object = MibTableRow
pm20002maCntclientInputErrorCounterEntry = _Pm20002maCntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 112, 1)
)
pm20002maCntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntclientInputErrorCounterEntry.setStatus("current")


class _Pm20002maCntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pm20002maCntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20002maCntclientInputErrorCounterIndex_Object = MibTableColumn
pm20002maCntclientInputErrorCounterIndex = _Pm20002maCntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 112, 1, 1),
    _Pm20002maCntclientInputErrorCounterIndex_Type()
)
pm20002maCntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntclientInputErrorCounterIndex.setStatus("current")
_Pm20002maCntclientInputErrorCounterValuePortn_Type = Counter32
_Pm20002maCntclientInputErrorCounterValuePortn_Object = MibTableColumn
pm20002maCntclientInputErrorCounterValuePortn = _Pm20002maCntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 112, 1, 2),
    _Pm20002maCntclientInputErrorCounterValuePortn_Type()
)
pm20002maCntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntclientInputErrorCounterValuePortn.setStatus("current")
_Pm20002maCntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pm20002maCntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pm20002maCntclientInputErrorCounterErrorPortn = _Pm20002maCntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 112, 1, 3),
    _Pm20002maCntclientInputErrorCounterErrorPortn_Type()
)
pm20002maCntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntclientInputErrorCounterErrorPortn.setStatus("current")
_Pm20002maCntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20002maCntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pm20002maCntclientInputErrorCounterOverloadPortn = _Pm20002maCntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 112, 1, 4),
    _Pm20002maCntclientInputErrorCounterOverloadPortn_Type()
)
pm20002maCntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pm20002maCntclientCbipCounterTable_Object = MibTable
pm20002maCntclientCbipCounterTable = _Pm20002maCntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 144)
)
if mibBuilder.loadTexts:
    pm20002maCntclientCbipCounterTable.setStatus("current")
_Pm20002maCntclientCbipCounterEntry_Object = MibTableRow
pm20002maCntclientCbipCounterEntry = _Pm20002maCntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 144, 1)
)
pm20002maCntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntclientCbipCounterEntry.setStatus("current")


class _Pm20002maCntclientCbipCounterIndex_Type(Integer32):
    """Custom type pm20002maCntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pm20002maCntclientCbipCounterIndex_Object = MibTableColumn
pm20002maCntclientCbipCounterIndex = _Pm20002maCntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 144, 1, 1),
    _Pm20002maCntclientCbipCounterIndex_Type()
)
pm20002maCntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntclientCbipCounterIndex.setStatus("current")
_Pm20002maCntclientCbipCounterValuePortn_Type = Counter32
_Pm20002maCntclientCbipCounterValuePortn_Object = MibTableColumn
pm20002maCntclientCbipCounterValuePortn = _Pm20002maCntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 144, 1, 2),
    _Pm20002maCntclientCbipCounterValuePortn_Type()
)
pm20002maCntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntclientCbipCounterValuePortn.setStatus("current")
_Pm20002maCntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pm20002maCntclientCbipCounterErrorPortn_Object = MibTableColumn
pm20002maCntclientCbipCounterErrorPortn = _Pm20002maCntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 144, 1, 3),
    _Pm20002maCntclientCbipCounterErrorPortn_Type()
)
pm20002maCntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntclientCbipCounterErrorPortn.setStatus("current")
_Pm20002maCntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pm20002maCntclientCbipCounterOverloadPortn_Object = MibTableColumn
pm20002maCntclientCbipCounterOverloadPortn = _Pm20002maCntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 2, 144, 1, 4),
    _Pm20002maCntclientCbipCounterOverloadPortn_Type()
)
pm20002maCntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntclientCbipCounterOverloadPortn.setStatus("current")
_Pm20002maCntLine_ObjectIdentity = ObjectIdentity
pm20002maCntLine = _Pm20002maCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3)
)
_Pm20002maCntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pm20002maCntlocalLineSmBip8ErrorCounterTable = _Pm20002maCntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pm20002maCntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm20002maCntlocalLineSmBip8ErrorCounterEntry = _Pm20002maCntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 192, 1)
)
pm20002maCntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm20002maCntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm20002maCntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20002maCntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm20002maCntlocalLineSmBip8ErrorCounterIndex = _Pm20002maCntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 192, 1, 1),
    _Pm20002maCntlocalLineSmBip8ErrorCounterIndex_Type()
)
pm20002maCntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm20002maCntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm20002maCntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm20002maCntlocalLineSmBip8ErrorCounterValuePortn = _Pm20002maCntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 192, 1, 2),
    _Pm20002maCntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pm20002maCntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm20002maCntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm20002maCntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm20002maCntlocalLineSmBip8ErrorCounterErrorPortn = _Pm20002maCntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 192, 1, 3),
    _Pm20002maCntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pm20002maCntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm20002maCntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20002maCntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm20002maCntlocalLineSmBip8ErrorCounterOverloadPortn = _Pm20002maCntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 192, 1, 4),
    _Pm20002maCntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm20002maCntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm20002maCntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pm20002maCntlocalLineFecCorrectedErrorsCounterTable = _Pm20002maCntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pm20002maCntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pm20002maCntlocalLineFecCorrectedErrorsCounterEntry = _Pm20002maCntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 193, 1)
)
pm20002maCntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pm20002maCntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pm20002maCntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pm20002maCntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pm20002maCntlocalLineFecCorrectedErrorsCounterIndex = _Pm20002maCntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 193, 1, 1),
    _Pm20002maCntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pm20002maCntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pm20002maCntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pm20002maCntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pm20002maCntlocalLineFecCorrectedErrorsCounterValuePortn = _Pm20002maCntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 193, 1, 2),
    _Pm20002maCntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pm20002maCntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pm20002maCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pm20002maCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pm20002maCntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pm20002maCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 193, 1, 3),
    _Pm20002maCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pm20002maCntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pm20002maCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pm20002maCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pm20002maCntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pm20002maCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 193, 1, 4),
    _Pm20002maCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pm20002maCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pm20002maCntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pm20002maCntremoteLineSmBip8ErrorCounterTable = _Pm20002maCntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pm20002maCntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pm20002maCntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm20002maCntremoteLineSmBip8ErrorCounterEntry = _Pm20002maCntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 194, 1)
)
pm20002maCntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm20002maCntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm20002maCntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20002maCntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm20002maCntremoteLineSmBip8ErrorCounterIndex = _Pm20002maCntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 194, 1, 1),
    _Pm20002maCntremoteLineSmBip8ErrorCounterIndex_Type()
)
pm20002maCntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm20002maCntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm20002maCntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm20002maCntremoteLineSmBip8ErrorCounterValuePortn = _Pm20002maCntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 194, 1, 2),
    _Pm20002maCntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pm20002maCntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm20002maCntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm20002maCntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm20002maCntremoteLineSmBip8ErrorCounterErrorPortn = _Pm20002maCntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 194, 1, 3),
    _Pm20002maCntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pm20002maCntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm20002maCntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20002maCntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm20002maCntremoteLineSmBip8ErrorCounterOverloadPortn = _Pm20002maCntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 194, 1, 4),
    _Pm20002maCntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm20002maCntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm20002maCntlineDfrmTimCntTable_Object = MibTable
pm20002maCntlineDfrmTimCntTable = _Pm20002maCntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pm20002maCntlineDfrmTimCntTable.setStatus("current")
_Pm20002maCntlineDfrmTimCntEntry_Object = MibTableRow
pm20002maCntlineDfrmTimCntEntry = _Pm20002maCntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 195, 1)
)
pm20002maCntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntlineDfrmTimCntEntry.setStatus("current")


class _Pm20002maCntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm20002maCntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm20002maCntlineDfrmTimCntIndex_Object = MibTableColumn
pm20002maCntlineDfrmTimCntIndex = _Pm20002maCntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 195, 1, 1),
    _Pm20002maCntlineDfrmTimCntIndex_Type()
)
pm20002maCntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlineDfrmTimCntIndex.setStatus("current")
_Pm20002maCntlineDfrmTimCntValuePortn_Type = Counter64
_Pm20002maCntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm20002maCntlineDfrmTimCntValuePortn = _Pm20002maCntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 195, 1, 2),
    _Pm20002maCntlineDfrmTimCntValuePortn_Type()
)
pm20002maCntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlineDfrmTimCntValuePortn.setStatus("current")
_Pm20002maCntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm20002maCntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm20002maCntlineDfrmTimCntErrorPortn = _Pm20002maCntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 195, 1, 3),
    _Pm20002maCntlineDfrmTimCntErrorPortn_Type()
)
pm20002maCntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm20002maCntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm20002maCntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm20002maCntlineDfrmTimCntOverloadPortn = _Pm20002maCntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 195, 1, 4),
    _Pm20002maCntlineDfrmTimCntOverloadPortn_Type()
)
pm20002maCntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterTable_Object = MibTable
pm20002maCntlocalLineTrscvPreSdFecErrorCounterTable = _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecErrorCounterTable.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterEntry_Object = MibTableRow
pm20002maCntlocalLineTrscvPreSdFecErrorCounterEntry = _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 196, 1)
)
pm20002maCntlocalLineTrscvPreSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecErrorCounterEntry.setStatus("current")


class _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex_Object = MibTableColumn
pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex = _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 196, 1, 1),
    _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex_Type()
)
pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type = Counter64
_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvPreSdFecErrorCounterValuePortn = _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 196, 1, 2),
    _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type()
)
pm20002maCntlocalLineTrscvPreSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecErrorCounterValuePortn.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn = _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 196, 1, 3),
    _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type()
)
pm20002maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20002maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn = _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 196, 1, 4),
    _Pm20002maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type()
)
pm20002maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object = MibTable
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable = _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object = MibTableRow
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry = _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 197, 1)
)
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setStatus("current")


class _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object = MibTableColumn
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex = _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 197, 1, 1),
    _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type()
)
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type = Counter64
_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn = _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 197, 1, 2),
    _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type()
)
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn = _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 197, 1, 3),
    _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type()
)
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn = _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 197, 1, 4),
    _Pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type()
)
pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecBitCounterTable_Object = MibTable
pm20002maCntlocalLineTrscvPreSdFecBitCounterTable = _Pm20002maCntlocalLineTrscvPreSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 198)
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecBitCounterTable.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecBitCounterEntry_Object = MibTableRow
pm20002maCntlocalLineTrscvPreSdFecBitCounterEntry = _Pm20002maCntlocalLineTrscvPreSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 198, 1)
)
pm20002maCntlocalLineTrscvPreSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecBitCounterEntry.setStatus("current")


class _Pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex_Object = MibTableColumn
pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex = _Pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 198, 1, 1),
    _Pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex_Type()
)
pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecBitCounterValuePortn_Type = Counter64
_Pm20002maCntlocalLineTrscvPreSdFecBitCounterValuePortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvPreSdFecBitCounterValuePortn = _Pm20002maCntlocalLineTrscvPreSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 198, 1, 2),
    _Pm20002maCntlocalLineTrscvPreSdFecBitCounterValuePortn_Type()
)
pm20002maCntlocalLineTrscvPreSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecBitCounterValuePortn.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm20002maCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvPreSdFecBitCounterErrorPortn = _Pm20002maCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 198, 1, 3),
    _Pm20002maCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type()
)
pm20002maCntlocalLineTrscvPreSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecBitCounterErrorPortn.setStatus("current")
_Pm20002maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm20002maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn = _Pm20002maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 198, 1, 4),
    _Pm20002maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type()
)
pm20002maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object = MibTable
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterTable = _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 199)
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterTable.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object = MibTableRow
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry = _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 199, 1)
)
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setStatus("current")


class _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object = MibTableColumn
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex = _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 199, 1, 1),
    _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type()
)
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type = Counter64
_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn = _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 199, 1, 2),
    _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type()
)
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn = _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 199, 1, 3),
    _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type()
)
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setStatus("current")
_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn = _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 4, 3, 199, 1, 4),
    _Pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type()
)
pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setStatus("current")
_Pm20002macontrolsWrite_ObjectIdentity = ObjectIdentity
pm20002macontrolsWrite = _Pm20002macontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6)
)
_Pm20002maCtrlOther_ObjectIdentity = ObjectIdentity
pm20002maCtrlOther = _Pm20002maCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1)
)
_Pm20002maCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm20002maCtrlconfMgnt1 = _Pm20002maCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 1)
)
_Pm20002maCtrlConf1Load1_Type = EkiOnOff
_Pm20002maCtrlConf1Load1_Object = MibScalar
pm20002maCtrlConf1Load1 = _Pm20002maCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 1, 1),
    _Pm20002maCtrlConf1Load1_Type()
)
pm20002maCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlConf1Load1.setStatus("current")
_Pm20002maCtrlConf2Load1_Type = EkiOnOff
_Pm20002maCtrlConf2Load1_Object = MibScalar
pm20002maCtrlConf2Load1 = _Pm20002maCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 1, 2),
    _Pm20002maCtrlConf2Load1_Type()
)
pm20002maCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlConf2Load1.setStatus("current")
_Pm20002maCtrlConf2Flash1_Type = EkiOnOff
_Pm20002maCtrlConf2Flash1_Object = MibScalar
pm20002maCtrlConf2Flash1 = _Pm20002maCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 1, 10),
    _Pm20002maCtrlConf2Flash1_Type()
)
pm20002maCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlConf2Flash1.setStatus("current")
_Pm20002maCtrlConf2Clear1_Type = EkiOnOff
_Pm20002maCtrlConf2Clear1_Object = MibScalar
pm20002maCtrlConf2Clear1 = _Pm20002maCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 1, 14),
    _Pm20002maCtrlConf2Clear1_Type()
)
pm20002maCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlConf2Clear1.setStatus("current")
_Pm20002maCtrlsynth4_ObjectIdentity = ObjectIdentity
pm20002maCtrlsynth4 = _Pm20002maCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 4)
)
_Pm20002maCtrlCorrelatOn_Type = EkiOnOff
_Pm20002maCtrlCorrelatOn_Object = MibScalar
pm20002maCtrlCorrelatOn = _Pm20002maCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 4, 1),
    _Pm20002maCtrlCorrelatOn_Type()
)
pm20002maCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlCorrelatOn.setStatus("current")
_Pm20002maCtrlCorrelatOff_Type = EkiOnOff
_Pm20002maCtrlCorrelatOff_Object = MibScalar
pm20002maCtrlCorrelatOff = _Pm20002maCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 4, 2),
    _Pm20002maCtrlCorrelatOff_Type()
)
pm20002maCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlCorrelatOff.setStatus("current")
_Pm20002maCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm20002maCtrlswMgnt = _Pm20002maCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 5)
)
_Pm20002maCtrlColdReset_Type = EkiOnOff
_Pm20002maCtrlColdReset_Object = MibScalar
pm20002maCtrlColdReset = _Pm20002maCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 5, 2),
    _Pm20002maCtrlColdReset_Type()
)
pm20002maCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlColdReset.setStatus("current")
_Pm20002maCtrlWarmReset_Type = EkiOnOff
_Pm20002maCtrlWarmReset_Object = MibScalar
pm20002maCtrlWarmReset = _Pm20002maCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 5, 3),
    _Pm20002maCtrlWarmReset_Type()
)
pm20002maCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlWarmReset.setStatus("current")
_Pm20002maCtrlLoadSwBank1_Type = EkiOnOff
_Pm20002maCtrlLoadSwBank1_Object = MibScalar
pm20002maCtrlLoadSwBank1 = _Pm20002maCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 5, 5),
    _Pm20002maCtrlLoadSwBank1_Type()
)
pm20002maCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlLoadSwBank1.setStatus("current")
_Pm20002maCtrlLoadSwBank2_Type = EkiOnOff
_Pm20002maCtrlLoadSwBank2_Object = MibScalar
pm20002maCtrlLoadSwBank2 = _Pm20002maCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 5, 6),
    _Pm20002maCtrlLoadSwBank2_Type()
)
pm20002maCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlLoadSwBank2.setStatus("current")
_Pm20002maCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm20002maCtrlgwMgnt = _Pm20002maCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 6)
)
_Pm20002maCtrlCurrentGwReset_Type = EkiOnOff
_Pm20002maCtrlCurrentGwReset_Object = MibScalar
pm20002maCtrlCurrentGwReset = _Pm20002maCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 6, 1),
    _Pm20002maCtrlCurrentGwReset_Type()
)
pm20002maCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlCurrentGwReset.setStatus("current")
_Pm20002maCtrlLoadGwBank1_Type = EkiOnOff
_Pm20002maCtrlLoadGwBank1_Object = MibScalar
pm20002maCtrlLoadGwBank1 = _Pm20002maCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 6, 5),
    _Pm20002maCtrlLoadGwBank1_Type()
)
pm20002maCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlLoadGwBank1.setStatus("current")
_Pm20002maCtrlLoadGwBank2_Type = EkiOnOff
_Pm20002maCtrlLoadGwBank2_Object = MibScalar
pm20002maCtrlLoadGwBank2 = _Pm20002maCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 6, 6),
    _Pm20002maCtrlLoadGwBank2_Type()
)
pm20002maCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlLoadGwBank2.setStatus("current")
_Pm20002maCtrlLoadGwBank3_Type = EkiOnOff
_Pm20002maCtrlLoadGwBank3_Object = MibScalar
pm20002maCtrlLoadGwBank3 = _Pm20002maCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 6, 7),
    _Pm20002maCtrlLoadGwBank3_Type()
)
pm20002maCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlLoadGwBank3.setStatus("current")
_Pm20002maCtrlLoadGwBank4_Type = EkiOnOff
_Pm20002maCtrlLoadGwBank4_Object = MibScalar
pm20002maCtrlLoadGwBank4 = _Pm20002maCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 6, 8),
    _Pm20002maCtrlLoadGwBank4_Type()
)
pm20002maCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlLoadGwBank4.setStatus("current")
_Pm20002maCtrlledTest_ObjectIdentity = ObjectIdentity
pm20002maCtrlledTest = _Pm20002maCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 192)
)
_Pm20002maCtrlGreenLed_Type = EkiOnOff
_Pm20002maCtrlGreenLed_Object = MibScalar
pm20002maCtrlGreenLed = _Pm20002maCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 192, 1),
    _Pm20002maCtrlGreenLed_Type()
)
pm20002maCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlGreenLed.setStatus("current")
_Pm20002maCtrlRedLed_Type = EkiOnOff
_Pm20002maCtrlRedLed_Object = MibScalar
pm20002maCtrlRedLed = _Pm20002maCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 192, 2),
    _Pm20002maCtrlRedLed_Type()
)
pm20002maCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlRedLed.setStatus("current")
_Pm20002maCtrlLedOff_Type = EkiOnOff
_Pm20002maCtrlLedOff_Object = MibScalar
pm20002maCtrlLedOff = _Pm20002maCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 192, 3),
    _Pm20002maCtrlLedOff_Type()
)
pm20002maCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlLedOff.setStatus("current")
_Pm20002maCtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pm20002maCtrlinitSwitchMarvell = _Pm20002maCtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 201)
)
_Pm20002maCtrlInitSwitchMarvell_Type = EkiOnOff
_Pm20002maCtrlInitSwitchMarvell_Object = MibScalar
pm20002maCtrlInitSwitchMarvell = _Pm20002maCtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 201, 1),
    _Pm20002maCtrlInitSwitchMarvell_Type()
)
pm20002maCtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlInitSwitchMarvell.setStatus("current")
_Pm20002maCtrlresetCount_ObjectIdentity = ObjectIdentity
pm20002maCtrlresetCount = _Pm20002maCtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 259)
)
_Pm20002maCtrlResetcount_Type = EkiOnOff
_Pm20002maCtrlResetcount_Object = MibScalar
pm20002maCtrlResetcount = _Pm20002maCtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 259, 1),
    _Pm20002maCtrlResetcount_Type()
)
pm20002maCtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlResetcount.setStatus("current")
_Pm20002maCtrlresetRmon_ObjectIdentity = ObjectIdentity
pm20002maCtrlresetRmon = _Pm20002maCtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 260)
)
_Pm20002maCtrlResetrmon_Type = EkiOnOff
_Pm20002maCtrlResetrmon_Object = MibScalar
pm20002maCtrlResetrmon = _Pm20002maCtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 260, 1),
    _Pm20002maCtrlResetrmon_Type()
)
pm20002maCtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlResetrmon.setStatus("current")
_Pm20002maCtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pm20002maCtrlresetMeasurements = _Pm20002maCtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 261)
)
_Pm20002maCtrlResetmeasurements_Type = EkiOnOff
_Pm20002maCtrlResetmeasurements_Object = MibScalar
pm20002maCtrlResetmeasurements = _Pm20002maCtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 1, 261, 1),
    _Pm20002maCtrlResetmeasurements_Type()
)
pm20002maCtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlResetmeasurements.setStatus("current")
_Pm20002maCtrlClient_ObjectIdentity = ObjectIdentity
pm20002maCtrlClient = _Pm20002maCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2)
)
_Pm20002maCtrlaccessLoopTable_Object = MibTable
pm20002maCtrlaccessLoopTable = _Pm20002maCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm20002maCtrlaccessLoopTable.setStatus("current")
_Pm20002maCtrlaccessLoopEntry_Object = MibTableRow
pm20002maCtrlaccessLoopEntry = _Pm20002maCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 16, 1)
)
pm20002maCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlaccessLoopEntry.setStatus("current")


class _Pm20002maCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm20002maCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlaccessLoopIndex_Object = MibTableColumn
pm20002maCtrlaccessLoopIndex = _Pm20002maCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 16, 1, 1),
    _Pm20002maCtrlaccessLoopIndex_Type()
)
pm20002maCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlaccessLoopIndex.setStatus("current")
_Pm20002maCtrlaccessLoopPortn_Type = EkiState
_Pm20002maCtrlaccessLoopPortn_Object = MibTableColumn
pm20002maCtrlaccessLoopPortn = _Pm20002maCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 16, 1, 2),
    _Pm20002maCtrlaccessLoopPortn_Type()
)
pm20002maCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlaccessLoopPortn.setStatus("current")
_Pm20002maCtrlclientLoopToLineTable_Object = MibTable
pm20002maCtrlclientLoopToLineTable = _Pm20002maCtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm20002maCtrlclientLoopToLineTable.setStatus("current")
_Pm20002maCtrlclientLoopToLineEntry_Object = MibTableRow
pm20002maCtrlclientLoopToLineEntry = _Pm20002maCtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 17, 1)
)
pm20002maCtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlclientLoopToLineEntry.setStatus("current")


class _Pm20002maCtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pm20002maCtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlclientLoopToLineIndex_Object = MibTableColumn
pm20002maCtrlclientLoopToLineIndex = _Pm20002maCtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 17, 1, 1),
    _Pm20002maCtrlclientLoopToLineIndex_Type()
)
pm20002maCtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlclientLoopToLineIndex.setStatus("current")
_Pm20002maCtrlclientLoopToLinePortn_Type = EkiState
_Pm20002maCtrlclientLoopToLinePortn_Object = MibTableColumn
pm20002maCtrlclientLoopToLinePortn = _Pm20002maCtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 17, 1, 2),
    _Pm20002maCtrlclientLoopToLinePortn_Type()
)
pm20002maCtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlclientLoopToLinePortn.setStatus("current")
_Pm20002maCtrlcsfUpInsTable_Object = MibTable
pm20002maCtrlcsfUpInsTable = _Pm20002maCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm20002maCtrlcsfUpInsTable.setStatus("current")
_Pm20002maCtrlcsfUpInsEntry_Object = MibTableRow
pm20002maCtrlcsfUpInsEntry = _Pm20002maCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 21, 1)
)
pm20002maCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlcsfUpInsEntry.setStatus("current")


class _Pm20002maCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm20002maCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlcsfUpInsIndex_Object = MibTableColumn
pm20002maCtrlcsfUpInsIndex = _Pm20002maCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 21, 1, 1),
    _Pm20002maCtrlcsfUpInsIndex_Type()
)
pm20002maCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlcsfUpInsIndex.setStatus("current")
_Pm20002maCtrlcsfUpInsPortn_Type = EkiState
_Pm20002maCtrlcsfUpInsPortn_Object = MibTableColumn
pm20002maCtrlcsfUpInsPortn = _Pm20002maCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 21, 1, 2),
    _Pm20002maCtrlcsfUpInsPortn_Type()
)
pm20002maCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlcsfUpInsPortn.setStatus("current")
_Pm20002maCtrlcaisDwInsTable_Object = MibTable
pm20002maCtrlcaisDwInsTable = _Pm20002maCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm20002maCtrlcaisDwInsTable.setStatus("current")
_Pm20002maCtrlcaisDwInsEntry_Object = MibTableRow
pm20002maCtrlcaisDwInsEntry = _Pm20002maCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 22, 1)
)
pm20002maCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlcaisDwInsEntry.setStatus("current")


class _Pm20002maCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm20002maCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlcaisDwInsIndex_Object = MibTableColumn
pm20002maCtrlcaisDwInsIndex = _Pm20002maCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 22, 1, 1),
    _Pm20002maCtrlcaisDwInsIndex_Type()
)
pm20002maCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlcaisDwInsIndex.setStatus("current")
_Pm20002maCtrlcaisDwInsPortn_Type = EkiState
_Pm20002maCtrlcaisDwInsPortn_Object = MibTableColumn
pm20002maCtrlcaisDwInsPortn = _Pm20002maCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 22, 1, 2),
    _Pm20002maCtrlcaisDwInsPortn_Type()
)
pm20002maCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlcaisDwInsPortn.setStatus("current")
_Pm20002maCtrlclientResetAllCountTable_Object = MibTable
pm20002maCtrlclientResetAllCountTable = _Pm20002maCtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 262)
)
if mibBuilder.loadTexts:
    pm20002maCtrlclientResetAllCountTable.setStatus("current")
_Pm20002maCtrlclientResetAllCountEntry_Object = MibTableRow
pm20002maCtrlclientResetAllCountEntry = _Pm20002maCtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 262, 1)
)
pm20002maCtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlclientResetAllCountEntry.setStatus("current")


class _Pm20002maCtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pm20002maCtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlclientResetAllCountIndex_Object = MibTableColumn
pm20002maCtrlclientResetAllCountIndex = _Pm20002maCtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 262, 1, 1),
    _Pm20002maCtrlclientResetAllCountIndex_Type()
)
pm20002maCtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlclientResetAllCountIndex.setStatus("current")
_Pm20002maCtrlclientResetAllCountsPortn_Type = EkiState
_Pm20002maCtrlclientResetAllCountsPortn_Object = MibTableColumn
pm20002maCtrlclientResetAllCountsPortn = _Pm20002maCtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 2, 262, 1, 2),
    _Pm20002maCtrlclientResetAllCountsPortn_Type()
)
pm20002maCtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlclientResetAllCountsPortn.setStatus("current")
_Pm20002maCtrlLine_ObjectIdentity = ObjectIdentity
pm20002maCtrlLine = _Pm20002maCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3)
)
_Pm20002maCtrlcommAccessLoopTable_Object = MibTable
pm20002maCtrlcommAccessLoopTable = _Pm20002maCtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm20002maCtrlcommAccessLoopTable.setStatus("current")
_Pm20002maCtrlcommAccessLoopEntry_Object = MibTableRow
pm20002maCtrlcommAccessLoopEntry = _Pm20002maCtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 64, 1)
)
pm20002maCtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlcommAccessLoopEntry.setStatus("current")


class _Pm20002maCtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pm20002maCtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlcommAccessLoopIndex_Object = MibTableColumn
pm20002maCtrlcommAccessLoopIndex = _Pm20002maCtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 64, 1, 1),
    _Pm20002maCtrlcommAccessLoopIndex_Type()
)
pm20002maCtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlcommAccessLoopIndex.setStatus("current")
_Pm20002maCtrlcommAccessLoopPortn_Type = EkiState
_Pm20002maCtrlcommAccessLoopPortn_Object = MibTableColumn
pm20002maCtrlcommAccessLoopPortn = _Pm20002maCtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 64, 1, 2),
    _Pm20002maCtrlcommAccessLoopPortn_Type()
)
pm20002maCtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlcommAccessLoopPortn.setStatus("current")
_Pm20002maCtrllineLoopTable_Object = MibTable
pm20002maCtrllineLoopTable = _Pm20002maCtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm20002maCtrllineLoopTable.setStatus("current")
_Pm20002maCtrllineLoopEntry_Object = MibTableRow
pm20002maCtrllineLoopEntry = _Pm20002maCtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 66, 1)
)
pm20002maCtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrllineLoopEntry.setStatus("current")


class _Pm20002maCtrllineLoopIndex_Type(Integer32):
    """Custom type pm20002maCtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm20002maCtrllineLoopIndex_Object = MibTableColumn
pm20002maCtrllineLoopIndex = _Pm20002maCtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 66, 1, 1),
    _Pm20002maCtrllineLoopIndex_Type()
)
pm20002maCtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrllineLoopIndex.setStatus("current")
_Pm20002maCtrllineLoopPortn_Type = EkiState
_Pm20002maCtrllineLoopPortn_Object = MibTableColumn
pm20002maCtrllineLoopPortn = _Pm20002maCtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 66, 1, 2),
    _Pm20002maCtrllineLoopPortn_Type()
)
pm20002maCtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrllineLoopPortn.setStatus("current")
_Pm20002maCtrlfecDisableTable_Object = MibTable
pm20002maCtrlfecDisableTable = _Pm20002maCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm20002maCtrlfecDisableTable.setStatus("current")
_Pm20002maCtrlfecDisableEntry_Object = MibTableRow
pm20002maCtrlfecDisableEntry = _Pm20002maCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 69, 1)
)
pm20002maCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlfecDisableEntry.setStatus("current")


class _Pm20002maCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm20002maCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlfecDisableIndex_Object = MibTableColumn
pm20002maCtrlfecDisableIndex = _Pm20002maCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 69, 1, 1),
    _Pm20002maCtrlfecDisableIndex_Type()
)
pm20002maCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlfecDisableIndex.setStatus("current")
_Pm20002maCtrlfecDisablePortn_Type = EkiState
_Pm20002maCtrlfecDisablePortn_Object = MibTableColumn
pm20002maCtrlfecDisablePortn = _Pm20002maCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 69, 1, 2),
    _Pm20002maCtrlfecDisablePortn_Type()
)
pm20002maCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlfecDisablePortn.setStatus("current")
_Pm20002maCtrlmsaLineLoopTable_Object = MibTable
pm20002maCtrlmsaLineLoopTable = _Pm20002maCtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm20002maCtrlmsaLineLoopTable.setStatus("current")
_Pm20002maCtrlmsaLineLoopEntry_Object = MibTableRow
pm20002maCtrlmsaLineLoopEntry = _Pm20002maCtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 209, 1)
)
pm20002maCtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlmsaLineLoopEntry.setStatus("current")


class _Pm20002maCtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pm20002maCtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlmsaLineLoopIndex_Object = MibTableColumn
pm20002maCtrlmsaLineLoopIndex = _Pm20002maCtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 209, 1, 1),
    _Pm20002maCtrlmsaLineLoopIndex_Type()
)
pm20002maCtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlmsaLineLoopIndex.setStatus("current")
_Pm20002maCtrlmsaLineLoopPortn_Type = EkiState
_Pm20002maCtrlmsaLineLoopPortn_Object = MibTableColumn
pm20002maCtrlmsaLineLoopPortn = _Pm20002maCtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 209, 1, 2),
    _Pm20002maCtrlmsaLineLoopPortn_Type()
)
pm20002maCtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlmsaLineLoopPortn.setStatus("current")
_Pm20002maCtrlmsaTxResetTable_Object = MibTable
pm20002maCtrlmsaTxResetTable = _Pm20002maCtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm20002maCtrlmsaTxResetTable.setStatus("current")
_Pm20002maCtrlmsaTxResetEntry_Object = MibTableRow
pm20002maCtrlmsaTxResetEntry = _Pm20002maCtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 210, 1)
)
pm20002maCtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlmsaTxResetEntry.setStatus("current")


class _Pm20002maCtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pm20002maCtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlmsaTxResetIndex_Object = MibTableColumn
pm20002maCtrlmsaTxResetIndex = _Pm20002maCtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 210, 1, 1),
    _Pm20002maCtrlmsaTxResetIndex_Type()
)
pm20002maCtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlmsaTxResetIndex.setStatus("current")
_Pm20002maCtrlmsaTxResetPortn_Type = EkiState
_Pm20002maCtrlmsaTxResetPortn_Object = MibTableColumn
pm20002maCtrlmsaTxResetPortn = _Pm20002maCtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 210, 1, 2),
    _Pm20002maCtrlmsaTxResetPortn_Type()
)
pm20002maCtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlmsaTxResetPortn.setStatus("current")
_Pm20002maCtrlmsaRxResetTable_Object = MibTable
pm20002maCtrlmsaRxResetTable = _Pm20002maCtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pm20002maCtrlmsaRxResetTable.setStatus("current")
_Pm20002maCtrlmsaRxResetEntry_Object = MibTableRow
pm20002maCtrlmsaRxResetEntry = _Pm20002maCtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 211, 1)
)
pm20002maCtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlmsaRxResetEntry.setStatus("current")


class _Pm20002maCtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pm20002maCtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlmsaRxResetIndex_Object = MibTableColumn
pm20002maCtrlmsaRxResetIndex = _Pm20002maCtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 211, 1, 1),
    _Pm20002maCtrlmsaRxResetIndex_Type()
)
pm20002maCtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlmsaRxResetIndex.setStatus("current")
_Pm20002maCtrlmsaRxResetPortn_Type = EkiState
_Pm20002maCtrlmsaRxResetPortn_Object = MibTableColumn
pm20002maCtrlmsaRxResetPortn = _Pm20002maCtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 211, 1, 2),
    _Pm20002maCtrlmsaRxResetPortn_Type()
)
pm20002maCtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlmsaRxResetPortn.setStatus("current")
_Pm20002maCtrlmsaShutdownTable_Object = MibTable
pm20002maCtrlmsaShutdownTable = _Pm20002maCtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm20002maCtrlmsaShutdownTable.setStatus("current")
_Pm20002maCtrlmsaShutdownEntry_Object = MibTableRow
pm20002maCtrlmsaShutdownEntry = _Pm20002maCtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 212, 1)
)
pm20002maCtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrlmsaShutdownEntry.setStatus("current")


class _Pm20002maCtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pm20002maCtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pm20002maCtrlmsaShutdownIndex_Object = MibTableColumn
pm20002maCtrlmsaShutdownIndex = _Pm20002maCtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 212, 1, 1),
    _Pm20002maCtrlmsaShutdownIndex_Type()
)
pm20002maCtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrlmsaShutdownIndex.setStatus("current")
_Pm20002maCtrlmsaShutdownPortn_Type = EkiState
_Pm20002maCtrlmsaShutdownPortn_Object = MibTableColumn
pm20002maCtrlmsaShutdownPortn = _Pm20002maCtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 212, 1, 2),
    _Pm20002maCtrlmsaShutdownPortn_Type()
)
pm20002maCtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrlmsaShutdownPortn.setStatus("current")
_Pm20002maCtrllineResetAllCountTable_Object = MibTable
pm20002maCtrllineResetAllCountTable = _Pm20002maCtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 263)
)
if mibBuilder.loadTexts:
    pm20002maCtrllineResetAllCountTable.setStatus("current")
_Pm20002maCtrllineResetAllCountEntry_Object = MibTableRow
pm20002maCtrllineResetAllCountEntry = _Pm20002maCtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 263, 1)
)
pm20002maCtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCtrllineResetAllCountEntry.setStatus("current")


class _Pm20002maCtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pm20002maCtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pm20002maCtrllineResetAllCountIndex_Object = MibTableColumn
pm20002maCtrllineResetAllCountIndex = _Pm20002maCtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 263, 1, 1),
    _Pm20002maCtrllineResetAllCountIndex_Type()
)
pm20002maCtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCtrllineResetAllCountIndex.setStatus("current")
_Pm20002maCtrllineResetAllCountsPortn_Type = EkiState
_Pm20002maCtrllineResetAllCountsPortn_Object = MibTableColumn
pm20002maCtrllineResetAllCountsPortn = _Pm20002maCtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 6, 3, 263, 1, 2),
    _Pm20002maCtrllineResetAllCountsPortn_Type()
)
pm20002maCtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCtrllineResetAllCountsPortn.setStatus("current")
_Pm20002mari_ObjectIdentity = ObjectIdentity
pm20002mari = _Pm20002mari_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7)
)
_Pm20002mariTable_ObjectIdentity = ObjectIdentity
pm20002mariTable = _Pm20002mariTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 1)
)
_Pm20002maRinvSfpTable_Object = MibTable
pm20002maRinvSfpTable = _Pm20002maRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm20002maRinvSfpTable.setStatus("current")
_Pm20002maRinvSfpEntry_Object = MibTableRow
pm20002maRinvSfpEntry = _Pm20002maRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 1, 1, 1)
)
pm20002maRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm20002maRinvSfpEntry.setStatus("current")


class _Pm20002maRinvSfpIndex_Type(Integer32):
    """Custom type pm20002maRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm20002maRinvSfpIndex_Type.__name__ = "Integer32"
_Pm20002maRinvSfpIndex_Object = MibTableColumn
pm20002maRinvSfpIndex = _Pm20002maRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 1, 1, 1, 1),
    _Pm20002maRinvSfpIndex_Type()
)
pm20002maRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maRinvSfpIndex.setStatus("current")
_Pm20002maRinvsfp_Type = DisplayString
_Pm20002maRinvsfp_Object = MibTableColumn
pm20002maRinvsfp = _Pm20002maRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 1, 1, 1, 2),
    _Pm20002maRinvsfp_Type()
)
pm20002maRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maRinvsfp.setStatus("current")
_Pm20002maRinvLineTable_Object = MibTable
pm20002maRinvLineTable = _Pm20002maRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm20002maRinvLineTable.setStatus("current")
_Pm20002maRinvLineEntry_Object = MibTableRow
pm20002maRinvLineEntry = _Pm20002maRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 1, 2, 1)
)
pm20002maRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm20002maRinvLineEntry.setStatus("current")


class _Pm20002maRinvLineIndex_Type(Integer32):
    """Custom type pm20002maRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm20002maRinvLineIndex_Type.__name__ = "Integer32"
_Pm20002maRinvLineIndex_Object = MibTableColumn
pm20002maRinvLineIndex = _Pm20002maRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 1, 2, 1, 1),
    _Pm20002maRinvLineIndex_Type()
)
pm20002maRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maRinvLineIndex.setStatus("current")
_Pm20002maRinvxfpLine_Type = DisplayString
_Pm20002maRinvxfpLine_Object = MibTableColumn
pm20002maRinvxfpLine = _Pm20002maRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 1, 2, 1, 2),
    _Pm20002maRinvxfpLine_Type()
)
pm20002maRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maRinvxfpLine.setStatus("current")
_Pm20002maRinvReloadInventory_Type = EkiOnOff
_Pm20002maRinvReloadInventory_Object = MibScalar
pm20002maRinvReloadInventory = _Pm20002maRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 2),
    _Pm20002maRinvReloadInventory_Type()
)
pm20002maRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maRinvReloadInventory.setStatus("current")
_Pm20002maRinvHwPlatform_Type = DisplayString
_Pm20002maRinvHwPlatform_Object = MibScalar
pm20002maRinvHwPlatform = _Pm20002maRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 3),
    _Pm20002maRinvHwPlatform_Type()
)
pm20002maRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maRinvHwPlatform.setStatus("current")
_Pm20002maRinvModulePlatform_Type = DisplayString
_Pm20002maRinvModulePlatform_Object = MibScalar
pm20002maRinvModulePlatform = _Pm20002maRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 4),
    _Pm20002maRinvModulePlatform_Type()
)
pm20002maRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maRinvModulePlatform.setStatus("current")
_Pm20002maRinvSwPlatform_Type = DisplayString
_Pm20002maRinvSwPlatform_Object = MibScalar
pm20002maRinvSwPlatform = _Pm20002maRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 5),
    _Pm20002maRinvSwPlatform_Type()
)
pm20002maRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maRinvSwPlatform.setStatus("current")
_Pm20002maRinvGwPlatform_Type = DisplayString
_Pm20002maRinvGwPlatform_Object = MibScalar
pm20002maRinvGwPlatform = _Pm20002maRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 7, 6),
    _Pm20002maRinvGwPlatform_Type()
)
pm20002maRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maRinvGwPlatform.setStatus("current")
_Pm20002madownload_ObjectIdentity = ObjectIdentity
pm20002madownload = _Pm20002madownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8)
)
_Pm20002maDwlOther_ObjectIdentity = ObjectIdentity
pm20002maDwlOther = _Pm20002maDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1)
)
_Pm20002maDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm20002maDwlrestartProcess = _Pm20002maDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 0)
)
_Pm20002maDwlWarmRestartProcessed_Type = EkiOnOff
_Pm20002maDwlWarmRestartProcessed_Object = MibScalar
pm20002maDwlWarmRestartProcessed = _Pm20002maDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 0, 1),
    _Pm20002maDwlWarmRestartProcessed_Type()
)
pm20002maDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlWarmRestartProcessed.setStatus("current")
_Pm20002maDwlColdRestartProcessed_Type = EkiOnOff
_Pm20002maDwlColdRestartProcessed_Object = MibScalar
pm20002maDwlColdRestartProcessed = _Pm20002maDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 0, 2),
    _Pm20002maDwlColdRestartProcessed_Type()
)
pm20002maDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlColdRestartProcessed.setStatus("current")
_Pm20002maDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm20002maDwlswBanksUsed = _Pm20002maDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 1)
)
_Pm20002maDwlSwBank1Used_Type = EkiOnOff
_Pm20002maDwlSwBank1Used_Object = MibScalar
pm20002maDwlSwBank1Used = _Pm20002maDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 1, 1),
    _Pm20002maDwlSwBank1Used_Type()
)
pm20002maDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlSwBank1Used.setStatus("current")
_Pm20002maDwlSwBank2Used_Type = EkiOnOff
_Pm20002maDwlSwBank2Used_Object = MibScalar
pm20002maDwlSwBank2Used = _Pm20002maDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 1, 2),
    _Pm20002maDwlSwBank2Used_Type()
)
pm20002maDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlSwBank2Used.setStatus("current")
_Pm20002maDwlSwBank1Notempty_Type = EkiOnOff
_Pm20002maDwlSwBank1Notempty_Object = MibScalar
pm20002maDwlSwBank1Notempty = _Pm20002maDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 1, 5),
    _Pm20002maDwlSwBank1Notempty_Type()
)
pm20002maDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlSwBank1Notempty.setStatus("current")
_Pm20002maDwlSwBank2Notempty_Type = EkiOnOff
_Pm20002maDwlSwBank2Notempty_Object = MibScalar
pm20002maDwlSwBank2Notempty = _Pm20002maDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 1, 6),
    _Pm20002maDwlSwBank2Notempty_Type()
)
pm20002maDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlSwBank2Notempty.setStatus("current")
_Pm20002maDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm20002maDwlgwBanksUsed = _Pm20002maDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 2)
)
_Pm20002maDwlGwBank1Used_Type = EkiOnOff
_Pm20002maDwlGwBank1Used_Object = MibScalar
pm20002maDwlGwBank1Used = _Pm20002maDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 2, 1),
    _Pm20002maDwlGwBank1Used_Type()
)
pm20002maDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlGwBank1Used.setStatus("current")
_Pm20002maDwlGwBank2Used_Type = EkiOnOff
_Pm20002maDwlGwBank2Used_Object = MibScalar
pm20002maDwlGwBank2Used = _Pm20002maDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 2, 2),
    _Pm20002maDwlGwBank2Used_Type()
)
pm20002maDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlGwBank2Used.setStatus("current")
_Pm20002maDwlGwBank3Used_Type = EkiOnOff
_Pm20002maDwlGwBank3Used_Object = MibScalar
pm20002maDwlGwBank3Used = _Pm20002maDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 2, 3),
    _Pm20002maDwlGwBank3Used_Type()
)
pm20002maDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlGwBank3Used.setStatus("current")
_Pm20002maDwlGwBank4Used_Type = EkiOnOff
_Pm20002maDwlGwBank4Used_Object = MibScalar
pm20002maDwlGwBank4Used = _Pm20002maDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 2, 4),
    _Pm20002maDwlGwBank4Used_Type()
)
pm20002maDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlGwBank4Used.setStatus("current")
_Pm20002maDwlGwBank1Notempty_Type = EkiOnOff
_Pm20002maDwlGwBank1Notempty_Object = MibScalar
pm20002maDwlGwBank1Notempty = _Pm20002maDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 2, 5),
    _Pm20002maDwlGwBank1Notempty_Type()
)
pm20002maDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlGwBank1Notempty.setStatus("current")
_Pm20002maDwlGwBank2Notempty_Type = EkiOnOff
_Pm20002maDwlGwBank2Notempty_Object = MibScalar
pm20002maDwlGwBank2Notempty = _Pm20002maDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 2, 6),
    _Pm20002maDwlGwBank2Notempty_Type()
)
pm20002maDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlGwBank2Notempty.setStatus("current")
_Pm20002maDwlGwBank3Notempty_Type = EkiOnOff
_Pm20002maDwlGwBank3Notempty_Object = MibScalar
pm20002maDwlGwBank3Notempty = _Pm20002maDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 2, 7),
    _Pm20002maDwlGwBank3Notempty_Type()
)
pm20002maDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlGwBank3Notempty.setStatus("current")
_Pm20002maDwlGwBank4Notempty_Type = EkiOnOff
_Pm20002maDwlGwBank4Notempty_Object = MibScalar
pm20002maDwlGwBank4Notempty = _Pm20002maDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 1, 2, 8),
    _Pm20002maDwlGwBank4Notempty_Type()
)
pm20002maDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maDwlGwBank4Notempty.setStatus("current")
_Pm20002maDwlClient_ObjectIdentity = ObjectIdentity
pm20002maDwlClient = _Pm20002maDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 2)
)
_Pm20002maDwlLine_ObjectIdentity = ObjectIdentity
pm20002maDwlLine = _Pm20002maDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 8, 3)
)
_Pm20002maConfig_ObjectIdentity = ObjectIdentity
pm20002maConfig = _Pm20002maConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9)
)
_Pm20002maCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm20002maCfgAccessCAisCsf = _Pm20002maCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 1)
)
_Pm20002maCfgClientcaiscsfTable_Object = MibTable
pm20002maCfgClientcaiscsfTable = _Pm20002maCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm20002maCfgClientcaiscsfTable.setStatus("current")
_Pm20002maCfgClientcaiscsfEntry_Object = MibTableRow
pm20002maCfgClientcaiscsfEntry = _Pm20002maCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 1, 1, 1)
)
pm20002maCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCfgClientcaiscsfEntry.setStatus("current")


class _Pm20002maCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm20002maCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm20002maCfgClientcaiscsfIndex_Object = MibTableColumn
pm20002maCfgClientcaiscsfIndex = _Pm20002maCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 1, 1, 1, 1),
    _Pm20002maCfgClientcaiscsfIndex_Type()
)
pm20002maCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgClientcaiscsfIndex.setStatus("current")


class _Pm20002maCfgReservePortn_Type(Unsigned32):
    """Custom type pm20002maCfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgReservePortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgReservePortn_Object = MibTableColumn
pm20002maCfgReservePortn = _Pm20002maCfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 1, 1, 1, 3),
    _Pm20002maCfgReservePortn_Type()
)
pm20002maCfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgReservePortn.setStatus("current")
_Pm20002maCfgStartup_ObjectIdentity = ObjectIdentity
pm20002maCfgStartup = _Pm20002maCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2)
)
_Pm20002maCfgClientStartupTable_Object = MibTable
pm20002maCfgClientStartupTable = _Pm20002maCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm20002maCfgClientStartupTable.setStatus("current")
_Pm20002maCfgClientStartupEntry_Object = MibTableRow
pm20002maCfgClientStartupEntry = _Pm20002maCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 1, 1)
)
pm20002maCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCfgClientStartupEntry.setStatus("current")


class _Pm20002maCfgClientStartupIndex_Type(Integer32):
    """Custom type pm20002maCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm20002maCfgClientStartupIndex_Object = MibTableColumn
pm20002maCfgClientStartupIndex = _Pm20002maCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 1, 1, 1),
    _Pm20002maCfgClientStartupIndex_Type()
)
pm20002maCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgClientStartupIndex.setStatus("current")


class _Pm20002maCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm20002maCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgSystConfPortPortn_Object = MibTableColumn
pm20002maCfgSystConfPortPortn = _Pm20002maCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 1, 1, 3),
    _Pm20002maCfgSystConfPortPortn_Type()
)
pm20002maCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgSystConfPortPortn.setStatus("current")


class _Pm20002maCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm20002maCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgNetConfPortPortn_Object = MibTableColumn
pm20002maCfgNetConfPortPortn = _Pm20002maCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 1, 1, 4),
    _Pm20002maCfgNetConfPortPortn_Type()
)
pm20002maCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgNetConfPortPortn.setStatus("current")


class _Pm20002maCfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm20002maCfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgOptionsPortPortn_Object = MibTableColumn
pm20002maCfgOptionsPortPortn = _Pm20002maCfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 1, 1, 14),
    _Pm20002maCfgOptionsPortPortn_Type()
)
pm20002maCfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgOptionsPortPortn.setStatus("current")
_Pm20002maCfgLineStartupTable_Object = MibTable
pm20002maCfgLineStartupTable = _Pm20002maCfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm20002maCfgLineStartupTable.setStatus("current")
_Pm20002maCfgLineStartupEntry_Object = MibTableRow
pm20002maCfgLineStartupEntry = _Pm20002maCfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 2, 1)
)
pm20002maCfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCfgLineStartupEntry.setStatus("current")


class _Pm20002maCfgLineStartupIndex_Type(Integer32):
    """Custom type pm20002maCfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCfgLineStartupIndex_Type.__name__ = "Integer32"
_Pm20002maCfgLineStartupIndex_Object = MibTableColumn
pm20002maCfgLineStartupIndex = _Pm20002maCfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 2, 1, 1),
    _Pm20002maCfgLineStartupIndex_Type()
)
pm20002maCfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgLineStartupIndex.setStatus("current")


class _Pm20002maCfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pm20002maCfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgSystConfLinePortn_Object = MibTableColumn
pm20002maCfgSystConfLinePortn = _Pm20002maCfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 2, 1, 3),
    _Pm20002maCfgSystConfLinePortn_Type()
)
pm20002maCfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgSystConfLinePortn.setStatus("current")


class _Pm20002maCfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pm20002maCfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgOptionsLinePortn_Object = MibTableColumn
pm20002maCfgOptionsLinePortn = _Pm20002maCfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 2, 1, 14),
    _Pm20002maCfgOptionsLinePortn_Type()
)
pm20002maCfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgOptionsLinePortn.setStatus("current")
_Pm20002maCfgXfpTable_Object = MibTable
pm20002maCfgXfpTable = _Pm20002maCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm20002maCfgXfpTable.setStatus("current")
_Pm20002maCfgXfpEntry_Object = MibTableRow
pm20002maCfgXfpEntry = _Pm20002maCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 3, 1)
)
pm20002maCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCfgXfpEntry.setStatus("current")


class _Pm20002maCfgXfpIndex_Type(Integer32):
    """Custom type pm20002maCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCfgXfpIndex_Type.__name__ = "Integer32"
_Pm20002maCfgXfpIndex_Object = MibTableColumn
pm20002maCfgXfpIndex = _Pm20002maCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 3, 1, 1),
    _Pm20002maCfgXfpIndex_Type()
)
pm20002maCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgXfpIndex.setStatus("current")


class _Pm20002maCfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pm20002maCfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgSystConfMsaLinePortn_Object = MibTableColumn
pm20002maCfgSystConfMsaLinePortn = _Pm20002maCfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 2, 3, 1, 3),
    _Pm20002maCfgSystConfMsaLinePortn_Type()
)
pm20002maCfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgSystConfMsaLinePortn.setStatus("current")
_Pm20002maCfgLabels_ObjectIdentity = ObjectIdentity
pm20002maCfgLabels = _Pm20002maCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 3)
)
_Pm20002maCfgLabelclientTable_Object = MibTable
pm20002maCfgLabelclientTable = _Pm20002maCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm20002maCfgLabelclientTable.setStatus("current")
_Pm20002maCfgLabelclientEntry_Object = MibTableRow
pm20002maCfgLabelclientEntry = _Pm20002maCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 3, 1, 1)
)
pm20002maCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCfgLabelclientEntry.setStatus("current")


class _Pm20002maCfgLabelclientIndex_Type(Integer32):
    """Custom type pm20002maCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm20002maCfgLabelclientIndex_Object = MibTableColumn
pm20002maCfgLabelclientIndex = _Pm20002maCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 3, 1, 1, 1),
    _Pm20002maCfgLabelclientIndex_Type()
)
pm20002maCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgLabelclientIndex.setStatus("current")


class _Pm20002maCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm20002maCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm20002maCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm20002maCfgLabelclientPortn_Object = MibTableColumn
pm20002maCfgLabelclientPortn = _Pm20002maCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 3, 1, 1, 3),
    _Pm20002maCfgLabelclientPortn_Type()
)
pm20002maCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgLabelclientPortn.setStatus("current")
_Pm20002maCfgLabellineTable_Object = MibTable
pm20002maCfgLabellineTable = _Pm20002maCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm20002maCfgLabellineTable.setStatus("current")
_Pm20002maCfgLabellineEntry_Object = MibTableRow
pm20002maCfgLabellineEntry = _Pm20002maCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 3, 2, 1)
)
pm20002maCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCfgLabellineEntry.setStatus("current")


class _Pm20002maCfgLabellineIndex_Type(Integer32):
    """Custom type pm20002maCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm20002maCfgLabellineIndex_Object = MibTableColumn
pm20002maCfgLabellineIndex = _Pm20002maCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 3, 2, 1, 1),
    _Pm20002maCfgLabellineIndex_Type()
)
pm20002maCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgLabellineIndex.setStatus("current")


class _Pm20002maCfgLabellinePortn_Type(DisplayString):
    """Custom type pm20002maCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm20002maCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm20002maCfgLabellinePortn_Object = MibTableColumn
pm20002maCfgLabellinePortn = _Pm20002maCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 3, 2, 1, 3),
    _Pm20002maCfgLabellinePortn_Type()
)
pm20002maCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgLabellinePortn.setStatus("current")
_Pm20002maCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm20002maCfgStartuptlh = _Pm20002maCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 4)
)
_Pm20002maCfgOtxtlhTable_Object = MibTable
pm20002maCfgOtxtlhTable = _Pm20002maCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm20002maCfgOtxtlhTable.setStatus("current")
_Pm20002maCfgOtxtlhEntry_Object = MibTableRow
pm20002maCfgOtxtlhEntry = _Pm20002maCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 4, 1, 1)
)
pm20002maCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCfgOtxtlhEntry.setStatus("current")


class _Pm20002maCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm20002maCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm20002maCfgOtxtlhIndex_Object = MibTableColumn
pm20002maCfgOtxtlhIndex = _Pm20002maCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 4, 1, 1, 1),
    _Pm20002maCfgOtxtlhIndex_Type()
)
pm20002maCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgOtxtlhIndex.setStatus("current")


class _Pm20002maCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm20002maCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgLinePwrLaserPortn_Object = MibTableColumn
pm20002maCfgLinePwrLaserPortn = _Pm20002maCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 4, 1, 1, 6),
    _Pm20002maCfgLinePwrLaserPortn_Type()
)
pm20002maCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgLinePwrLaserPortn.setStatus("current")


class _Pm20002maCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm20002maCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgLineFCurrentPortn_Object = MibTableColumn
pm20002maCfgLineFCurrentPortn = _Pm20002maCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 4, 1, 1, 7),
    _Pm20002maCfgLineFCurrentPortn_Type()
)
pm20002maCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgLineFCurrentPortn.setStatus("current")


class _Pm20002maCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm20002maCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgLineGridCurrentPortn_Object = MibTableColumn
pm20002maCfgLineGridCurrentPortn = _Pm20002maCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 4, 1, 1, 8),
    _Pm20002maCfgLineGridCurrentPortn_Type()
)
pm20002maCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgLineGridCurrentPortn.setStatus("current")


class _Pm20002maCfgFPortn_Type(Unsigned32):
    """Custom type pm20002maCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgFPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgFPortn_Object = MibTableColumn
pm20002maCfgFPortn = _Pm20002maCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 4, 1, 1, 9),
    _Pm20002maCfgFPortn_Type()
)
pm20002maCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgFPortn.setStatus("current")


class _Pm20002maCfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm20002maCfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgRxLineFCurrentPortn_Object = MibTableColumn
pm20002maCfgRxLineFCurrentPortn = _Pm20002maCfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 4, 1, 1, 10),
    _Pm20002maCfgRxLineFCurrentPortn_Type()
)
pm20002maCfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgRxLineFCurrentPortn.setStatus("current")
_Pm20002maCfgOther_ObjectIdentity = ObjectIdentity
pm20002maCfgOther = _Pm20002maCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 5)
)
_Pm20002matablemoduleOther_ObjectIdentity = ObjectIdentity
pm20002matablemoduleOther = _Pm20002matablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 5, 1)
)


class _Pm20002maCfgmode_Type(Unsigned32):
    """Custom type pm20002maCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgmode_Type.__name__ = "Unsigned32"
_Pm20002maCfgmode_Object = MibScalar
pm20002maCfgmode = _Pm20002maCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 5, 1, 2),
    _Pm20002maCfgmode_Type()
)
pm20002maCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgmode.setStatus("current")


class _Pm20002maCfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type pm20002maCfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm20002maCfgfanLowSpeedThreshold_Object = MibScalar
pm20002maCfgfanLowSpeedThreshold = _Pm20002maCfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 5, 1, 3),
    _Pm20002maCfgfanLowSpeedThreshold_Type()
)
pm20002maCfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgfanLowSpeedThreshold.setStatus("current")


class _Pm20002maCfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pm20002maCfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm20002maCfgfanHighSpeedThreshold_Object = MibScalar
pm20002maCfgfanHighSpeedThreshold = _Pm20002maCfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 5, 1, 4),
    _Pm20002maCfgfanHighSpeedThreshold_Type()
)
pm20002maCfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgfanHighSpeedThreshold.setStatus("current")
_Pm20002maCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm20002maCfgStartuptablefive = _Pm20002maCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 6)
)
_Pm20002maCfgOtxtlhcapabilitiesTable_Object = MibTable
pm20002maCfgOtxtlhcapabilitiesTable = _Pm20002maCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm20002maCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm20002maCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm20002maCfgOtxtlhcapabilitiesEntry = _Pm20002maCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 6, 1, 1)
)
pm20002maCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm20002maCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm20002maCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm20002maCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm20002maCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm20002maCfgOtxtlhcapabilitiesIndex = _Pm20002maCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 6, 1, 1, 1),
    _Pm20002maCfgOtxtlhcapabilitiesIndex_Type()
)
pm20002maCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm20002maCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm20002maCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgComponentTypePortn_Object = MibTableColumn
pm20002maCfgComponentTypePortn = _Pm20002maCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 6, 1, 1, 3),
    _Pm20002maCfgComponentTypePortn_Type()
)
pm20002maCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgComponentTypePortn.setStatus("current")


class _Pm20002maCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm20002maCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgMiscellaneousPortn_Object = MibTableColumn
pm20002maCfgMiscellaneousPortn = _Pm20002maCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 6, 1, 1, 4),
    _Pm20002maCfgMiscellaneousPortn_Type()
)
pm20002maCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgMiscellaneousPortn.setStatus("current")


class _Pm20002maCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm20002maCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgFirstChannelPortn_Object = MibTableColumn
pm20002maCfgFirstChannelPortn = _Pm20002maCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 6, 1, 1, 5),
    _Pm20002maCfgFirstChannelPortn_Type()
)
pm20002maCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgFirstChannelPortn.setStatus("current")


class _Pm20002maCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm20002maCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgLastChannelPortn_Object = MibTableColumn
pm20002maCfgLastChannelPortn = _Pm20002maCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 6, 1, 1, 6),
    _Pm20002maCfgLastChannelPortn_Type()
)
pm20002maCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgLastChannelPortn.setStatus("current")


class _Pm20002maCfgGridPortn_Type(Unsigned32):
    """Custom type pm20002maCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20002maCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm20002maCfgGridPortn_Object = MibTableColumn
pm20002maCfgGridPortn = _Pm20002maCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 6, 1, 1, 7),
    _Pm20002maCfgGridPortn_Type()
)
pm20002maCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maCfgGridPortn.setStatus("current")
_Pm20002maCfgWriteConfiguration_Type = EkiOnOff
_Pm20002maCfgWriteConfiguration_Object = MibScalar
pm20002maCfgWriteConfiguration = _Pm20002maCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 9, 257),
    _Pm20002maCfgWriteConfiguration_Type()
)
pm20002maCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maCfgWriteConfiguration.setStatus("current")
_Pm20002matraps_ObjectIdentity = ObjectIdentity
pm20002matraps = _Pm20002matraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10)
)


class _Pm20002matrapPortNumber_Type(Integer32):
    """Custom type pm20002matrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm20002matrapPortNumber_Type.__name__ = "Integer32"
_Pm20002matrapPortNumber_Object = MibScalar
pm20002matrapPortNumber = _Pm20002matrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 2),
    _Pm20002matrapPortNumber_Type()
)
pm20002matrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002matrapPortNumber.setStatus("current")


class _Pm20002matrapLineNumber_Type(Integer32):
    """Custom type pm20002matrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm20002matrapLineNumber_Type.__name__ = "Integer32"
_Pm20002matrapLineNumber_Object = MibScalar
pm20002matrapLineNumber = _Pm20002matrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 3),
    _Pm20002matrapLineNumber_Type()
)
pm20002matrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002matrapLineNumber.setStatus("current")


class _Pm20002matrapBoardNumber_Type(Integer32):
    """Custom type pm20002matrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm20002matrapBoardNumber_Type.__name__ = "Integer32"
_Pm20002matrapBoardNumber_Object = MibScalar
pm20002matrapBoardNumber = _Pm20002matrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 4),
    _Pm20002matrapBoardNumber_Type()
)
pm20002matrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002matrapBoardNumber.setStatus("current")
_Pm20002maMonitoring_ObjectIdentity = ObjectIdentity
pm20002maMonitoring = _Pm20002maMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11)
)
_Pm20002maMonOther_ObjectIdentity = ObjectIdentity
pm20002maMonOther = _Pm20002maMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 1)
)
_Pm20002maMonRmon_ObjectIdentity = ObjectIdentity
pm20002maMonRmon = _Pm20002maMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 1, 3)
)
_Pm20002maMonClient_ObjectIdentity = ObjectIdentity
pm20002maMonClient = _Pm20002maMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2)
)
_Pm20002maMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm20002maMonClientRmonCounter = _Pm20002maMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4)
)
_Pm20002maMonupRmonBytesCounterClientInputTable_Object = MibTable
pm20002maMonupRmonBytesCounterClientInputTable = _Pm20002maMonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonBytesCounterClientInputTable.setStatus("current")
_Pm20002maMonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pm20002maMonupRmonBytesCounterClientInputEntry = _Pm20002maMonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 16, 1)
)
pm20002maMonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pm20002maMonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pm20002maMonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20002maMonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pm20002maMonupRmonBytesCounterClientInputIndex = _Pm20002maMonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 16, 1, 1),
    _Pm20002maMonupRmonBytesCounterClientInputIndex_Type()
)
pm20002maMonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pm20002maMonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pm20002maMonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pm20002maMonupRmonBytesCounterClientInputValuePortn = _Pm20002maMonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 16, 1, 2),
    _Pm20002maMonupRmonBytesCounterClientInputValuePortn_Type()
)
pm20002maMonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pm20002maMonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20002maMonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pm20002maMonupRmonBytesCounterClientInputErrorPortn = _Pm20002maMonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 16, 1, 3),
    _Pm20002maMonupRmonBytesCounterClientInputErrorPortn_Type()
)
pm20002maMonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pm20002maMonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20002maMonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pm20002maMonupRmonBytesCounterClientInputOverloadPortn = _Pm20002maMonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 16, 1, 4),
    _Pm20002maMonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pm20002maMonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pm20002maMonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm20002maMonupRmonCrcErrorsCounterClientInputTable = _Pm20002maMonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm20002maMonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm20002maMonupRmonCrcErrorsCounterClientInputEntry = _Pm20002maMonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 48, 1)
)
pm20002maMonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm20002maMonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm20002maMonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20002maMonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm20002maMonupRmonCrcErrorsCounterClientInputIndex = _Pm20002maMonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 48, 1, 1),
    _Pm20002maMonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pm20002maMonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm20002maMonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm20002maMonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm20002maMonupRmonCrcErrorsCounterClientInputValuePortn = _Pm20002maMonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 48, 1, 2),
    _Pm20002maMonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm20002maMonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm20002maMonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20002maMonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm20002maMonupRmonCrcErrorsCounterClientInputErrorPortn = _Pm20002maMonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 48, 1, 3),
    _Pm20002maMonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm20002maMonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm20002maMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20002maMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm20002maMonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pm20002maMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 48, 1, 4),
    _Pm20002maMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm20002maMonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm20002maMonupRmonPacketsCounterClientInputTable_Object = MibTable
pm20002maMonupRmonPacketsCounterClientInputTable = _Pm20002maMonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pm20002maMonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm20002maMonupRmonPacketsCounterClientInputEntry = _Pm20002maMonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 80, 1)
)
pm20002maMonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm20002maMonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm20002maMonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20002maMonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm20002maMonupRmonPacketsCounterClientInputIndex = _Pm20002maMonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 80, 1, 1),
    _Pm20002maMonupRmonPacketsCounterClientInputIndex_Type()
)
pm20002maMonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm20002maMonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm20002maMonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm20002maMonupRmonPacketsCounterClientInputValuePortn = _Pm20002maMonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 80, 1, 2),
    _Pm20002maMonupRmonPacketsCounterClientInputValuePortn_Type()
)
pm20002maMonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm20002maMonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20002maMonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm20002maMonupRmonPacketsCounterClientInputErrorPortn = _Pm20002maMonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 80, 1, 3),
    _Pm20002maMonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pm20002maMonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm20002maMonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20002maMonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm20002maMonupRmonPacketsCounterClientInputOverloadPortn = _Pm20002maMonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 80, 1, 4),
    _Pm20002maMonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm20002maMonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pm20002maMonupRmonBroadcastCounterClientInputTable_Object = MibTable
pm20002maMonupRmonBroadcastCounterClientInputTable = _Pm20002maMonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 112)
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pm20002maMonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pm20002maMonupRmonBroadcastCounterClientInputEntry = _Pm20002maMonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 112, 1)
)
pm20002maMonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pm20002maMonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pm20002maMonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20002maMonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pm20002maMonupRmonBroadcastCounterClientInputIndex = _Pm20002maMonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 112, 1, 1),
    _Pm20002maMonupRmonBroadcastCounterClientInputIndex_Type()
)
pm20002maMonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pm20002maMonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pm20002maMonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pm20002maMonupRmonBroadcastCounterClientInputValuePortn = _Pm20002maMonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 112, 1, 2),
    _Pm20002maMonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pm20002maMonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pm20002maMonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20002maMonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pm20002maMonupRmonBroadcastCounterClientInputErrorPortn = _Pm20002maMonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 112, 1, 3),
    _Pm20002maMonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pm20002maMonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pm20002maMonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20002maMonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pm20002maMonupRmonBroadcastCounterClientInputOverloadPortn = _Pm20002maMonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 112, 1, 4),
    _Pm20002maMonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pm20002maMonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pm20002maMonupRmonMulticastCounterClientInputTable_Object = MibTable
pm20002maMonupRmonMulticastCounterClientInputTable = _Pm20002maMonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 144)
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pm20002maMonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pm20002maMonupRmonMulticastCounterClientInputEntry = _Pm20002maMonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 144, 1)
)
pm20002maMonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pm20002maMonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pm20002maMonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20002maMonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pm20002maMonupRmonMulticastCounterClientInputIndex = _Pm20002maMonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 144, 1, 1),
    _Pm20002maMonupRmonMulticastCounterClientInputIndex_Type()
)
pm20002maMonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pm20002maMonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pm20002maMonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pm20002maMonupRmonMulticastCounterClientInputValuePortn = _Pm20002maMonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 144, 1, 2),
    _Pm20002maMonupRmonMulticastCounterClientInputValuePortn_Type()
)
pm20002maMonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pm20002maMonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20002maMonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pm20002maMonupRmonMulticastCounterClientInputErrorPortn = _Pm20002maMonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 144, 1, 3),
    _Pm20002maMonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pm20002maMonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pm20002maMonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20002maMonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pm20002maMonupRmonMulticastCounterClientInputOverloadPortn = _Pm20002maMonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 144, 1, 4),
    _Pm20002maMonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pm20002maMonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pm20002maMonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pm20002maMonupRmonPauseFrameCounterClientInputTable = _Pm20002maMonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pm20002maMonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pm20002maMonupRmonPauseFrameCounterClientInputEntry = _Pm20002maMonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 176, 1)
)
pm20002maMonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pm20002maMonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pm20002maMonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20002maMonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pm20002maMonupRmonPauseFrameCounterClientInputIndex = _Pm20002maMonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 176, 1, 1),
    _Pm20002maMonupRmonPauseFrameCounterClientInputIndex_Type()
)
pm20002maMonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pm20002maMonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pm20002maMonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pm20002maMonupRmonPauseFrameCounterClientInputValuePortn = _Pm20002maMonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 176, 1, 2),
    _Pm20002maMonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pm20002maMonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pm20002maMonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20002maMonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pm20002maMonupRmonPauseFrameCounterClientInputErrorPortn = _Pm20002maMonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 176, 1, 3),
    _Pm20002maMonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pm20002maMonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pm20002maMonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20002maMonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pm20002maMonupRmonPauseFrameCounterClientInputOverloadPortn = _Pm20002maMonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 176, 1, 4),
    _Pm20002maMonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pm20002maMonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pm20002maMonupRmonUnicastCounterClientInputTable_Object = MibTable
pm20002maMonupRmonUnicastCounterClientInputTable = _Pm20002maMonupRmonUnicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 304)
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonUnicastCounterClientInputTable.setStatus("current")
_Pm20002maMonupRmonUnicastCounterClientInputEntry_Object = MibTableRow
pm20002maMonupRmonUnicastCounterClientInputEntry = _Pm20002maMonupRmonUnicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 304, 1)
)
pm20002maMonupRmonUnicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMonupRmonUnicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonUnicastCounterClientInputEntry.setStatus("current")


class _Pm20002maMonupRmonUnicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm20002maMonupRmonUnicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMonupRmonUnicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20002maMonupRmonUnicastCounterClientInputIndex_Object = MibTableColumn
pm20002maMonupRmonUnicastCounterClientInputIndex = _Pm20002maMonupRmonUnicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 304, 1, 1),
    _Pm20002maMonupRmonUnicastCounterClientInputIndex_Type()
)
pm20002maMonupRmonUnicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonUnicastCounterClientInputIndex.setStatus("current")
_Pm20002maMonupRmonUnicastCounterClientInputValuePortn_Type = Counter64
_Pm20002maMonupRmonUnicastCounterClientInputValuePortn_Object = MibTableColumn
pm20002maMonupRmonUnicastCounterClientInputValuePortn = _Pm20002maMonupRmonUnicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 304, 1, 2),
    _Pm20002maMonupRmonUnicastCounterClientInputValuePortn_Type()
)
pm20002maMonupRmonUnicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonUnicastCounterClientInputValuePortn.setStatus("current")
_Pm20002maMonupRmonUnicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20002maMonupRmonUnicastCounterClientInputErrorPortn_Object = MibTableColumn
pm20002maMonupRmonUnicastCounterClientInputErrorPortn = _Pm20002maMonupRmonUnicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 304, 1, 3),
    _Pm20002maMonupRmonUnicastCounterClientInputErrorPortn_Type()
)
pm20002maMonupRmonUnicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonUnicastCounterClientInputErrorPortn.setStatus("current")
_Pm20002maMonupRmonUnicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20002maMonupRmonUnicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm20002maMonupRmonUnicastCounterClientInputOverloadPortn = _Pm20002maMonupRmonUnicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 304, 1, 4),
    _Pm20002maMonupRmonUnicastCounterClientInputOverloadPortn_Type()
)
pm20002maMonupRmonUnicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonUnicastCounterClientInputOverloadPortn.setStatus("current")
_Pm20002maMonupRmonNonunicastCounterClientInputTable_Object = MibTable
pm20002maMonupRmonNonunicastCounterClientInputTable = _Pm20002maMonupRmonNonunicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 336)
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonNonunicastCounterClientInputTable.setStatus("current")
_Pm20002maMonupRmonNonunicastCounterClientInputEntry_Object = MibTableRow
pm20002maMonupRmonNonunicastCounterClientInputEntry = _Pm20002maMonupRmonNonunicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 336, 1)
)
pm20002maMonupRmonNonunicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMonupRmonNonunicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMonupRmonNonunicastCounterClientInputEntry.setStatus("current")


class _Pm20002maMonupRmonNonunicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm20002maMonupRmonNonunicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMonupRmonNonunicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20002maMonupRmonNonunicastCounterClientInputIndex_Object = MibTableColumn
pm20002maMonupRmonNonunicastCounterClientInputIndex = _Pm20002maMonupRmonNonunicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 336, 1, 1),
    _Pm20002maMonupRmonNonunicastCounterClientInputIndex_Type()
)
pm20002maMonupRmonNonunicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonNonunicastCounterClientInputIndex.setStatus("current")
_Pm20002maMonupRmonNonunicastCounterClientInputValuePortn_Type = Counter64
_Pm20002maMonupRmonNonunicastCounterClientInputValuePortn_Object = MibTableColumn
pm20002maMonupRmonNonunicastCounterClientInputValuePortn = _Pm20002maMonupRmonNonunicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 336, 1, 2),
    _Pm20002maMonupRmonNonunicastCounterClientInputValuePortn_Type()
)
pm20002maMonupRmonNonunicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonNonunicastCounterClientInputValuePortn.setStatus("current")
_Pm20002maMonupRmonNonunicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20002maMonupRmonNonunicastCounterClientInputErrorPortn_Object = MibTableColumn
pm20002maMonupRmonNonunicastCounterClientInputErrorPortn = _Pm20002maMonupRmonNonunicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 336, 1, 3),
    _Pm20002maMonupRmonNonunicastCounterClientInputErrorPortn_Type()
)
pm20002maMonupRmonNonunicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonNonunicastCounterClientInputErrorPortn.setStatus("current")
_Pm20002maMonupRmonNonunicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20002maMonupRmonNonunicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm20002maMonupRmonNonunicastCounterClientInputOverloadPortn = _Pm20002maMonupRmonNonunicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 336, 1, 4),
    _Pm20002maMonupRmonNonunicastCounterClientInputOverloadPortn_Type()
)
pm20002maMonupRmonNonunicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMonupRmonNonunicastCounterClientInputOverloadPortn.setStatus("current")
_Pm20002maMondownRmonBytesCounterClientOutputTable_Object = MibTable
pm20002maMondownRmonBytesCounterClientOutputTable = _Pm20002maMondownRmonBytesCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 400)
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonBytesCounterClientOutputTable.setStatus("current")
_Pm20002maMondownRmonBytesCounterClientOutputEntry_Object = MibTableRow
pm20002maMondownRmonBytesCounterClientOutputEntry = _Pm20002maMondownRmonBytesCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 400, 1)
)
pm20002maMondownRmonBytesCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMondownRmonBytesCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonBytesCounterClientOutputEntry.setStatus("current")


class _Pm20002maMondownRmonBytesCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20002maMondownRmonBytesCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMondownRmonBytesCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20002maMondownRmonBytesCounterClientOutputIndex_Object = MibTableColumn
pm20002maMondownRmonBytesCounterClientOutputIndex = _Pm20002maMondownRmonBytesCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 400, 1, 1),
    _Pm20002maMondownRmonBytesCounterClientOutputIndex_Type()
)
pm20002maMondownRmonBytesCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonBytesCounterClientOutputIndex.setStatus("current")
_Pm20002maMondownRmonBytesCounterClientOutputValuePortn_Type = Counter64
_Pm20002maMondownRmonBytesCounterClientOutputValuePortn_Object = MibTableColumn
pm20002maMondownRmonBytesCounterClientOutputValuePortn = _Pm20002maMondownRmonBytesCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 400, 1, 2),
    _Pm20002maMondownRmonBytesCounterClientOutputValuePortn_Type()
)
pm20002maMondownRmonBytesCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonBytesCounterClientOutputValuePortn.setStatus("current")
_Pm20002maMondownRmonBytesCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20002maMondownRmonBytesCounterClientOutputErrorPortn_Object = MibTableColumn
pm20002maMondownRmonBytesCounterClientOutputErrorPortn = _Pm20002maMondownRmonBytesCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 400, 1, 3),
    _Pm20002maMondownRmonBytesCounterClientOutputErrorPortn_Type()
)
pm20002maMondownRmonBytesCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonBytesCounterClientOutputErrorPortn.setStatus("current")
_Pm20002maMondownRmonBytesCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20002maMondownRmonBytesCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20002maMondownRmonBytesCounterClientOutputOverloadPortn = _Pm20002maMondownRmonBytesCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 400, 1, 4),
    _Pm20002maMondownRmonBytesCounterClientOutputOverloadPortn_Type()
)
pm20002maMondownRmonBytesCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonBytesCounterClientOutputOverloadPortn.setStatus("current")
_Pm20002maMondownRmonCrcErrorsCounterClientOutputTable_Object = MibTable
pm20002maMondownRmonCrcErrorsCounterClientOutputTable = _Pm20002maMondownRmonCrcErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 432)
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonCrcErrorsCounterClientOutputTable.setStatus("current")
_Pm20002maMondownRmonCrcErrorsCounterClientOutputEntry_Object = MibTableRow
pm20002maMondownRmonCrcErrorsCounterClientOutputEntry = _Pm20002maMondownRmonCrcErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 432, 1)
)
pm20002maMondownRmonCrcErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMondownRmonCrcErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonCrcErrorsCounterClientOutputEntry.setStatus("current")


class _Pm20002maMondownRmonCrcErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20002maMondownRmonCrcErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMondownRmonCrcErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20002maMondownRmonCrcErrorsCounterClientOutputIndex_Object = MibTableColumn
pm20002maMondownRmonCrcErrorsCounterClientOutputIndex = _Pm20002maMondownRmonCrcErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 432, 1, 1),
    _Pm20002maMondownRmonCrcErrorsCounterClientOutputIndex_Type()
)
pm20002maMondownRmonCrcErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonCrcErrorsCounterClientOutputIndex.setStatus("current")
_Pm20002maMondownRmonCrcErrorsCounterClientOutputValuePortn_Type = Counter64
_Pm20002maMondownRmonCrcErrorsCounterClientOutputValuePortn_Object = MibTableColumn
pm20002maMondownRmonCrcErrorsCounterClientOutputValuePortn = _Pm20002maMondownRmonCrcErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 432, 1, 2),
    _Pm20002maMondownRmonCrcErrorsCounterClientOutputValuePortn_Type()
)
pm20002maMondownRmonCrcErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonCrcErrorsCounterClientOutputValuePortn.setStatus("current")
_Pm20002maMondownRmonCrcErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20002maMondownRmonCrcErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
pm20002maMondownRmonCrcErrorsCounterClientOutputErrorPortn = _Pm20002maMondownRmonCrcErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 432, 1, 3),
    _Pm20002maMondownRmonCrcErrorsCounterClientOutputErrorPortn_Type()
)
pm20002maMondownRmonCrcErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonCrcErrorsCounterClientOutputErrorPortn.setStatus("current")
_Pm20002maMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20002maMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20002maMondownRmonCrcErrorsCounterClientOutputOverloadPortn = _Pm20002maMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 432, 1, 4),
    _Pm20002maMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type()
)
pm20002maMondownRmonCrcErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonCrcErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Pm20002maMondownRmonPacketsCounterClientOutputTable_Object = MibTable
pm20002maMondownRmonPacketsCounterClientOutputTable = _Pm20002maMondownRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 464)
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonPacketsCounterClientOutputTable.setStatus("current")
_Pm20002maMondownRmonPacketsCounterClientOutputEntry_Object = MibTableRow
pm20002maMondownRmonPacketsCounterClientOutputEntry = _Pm20002maMondownRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 464, 1)
)
pm20002maMondownRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMondownRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Pm20002maMondownRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20002maMondownRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMondownRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20002maMondownRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
pm20002maMondownRmonPacketsCounterClientOutputIndex = _Pm20002maMondownRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 464, 1, 1),
    _Pm20002maMondownRmonPacketsCounterClientOutputIndex_Type()
)
pm20002maMondownRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonPacketsCounterClientOutputIndex.setStatus("current")
_Pm20002maMondownRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Pm20002maMondownRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
pm20002maMondownRmonPacketsCounterClientOutputValuePortn = _Pm20002maMondownRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 464, 1, 2),
    _Pm20002maMondownRmonPacketsCounterClientOutputValuePortn_Type()
)
pm20002maMondownRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Pm20002maMondownRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20002maMondownRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
pm20002maMondownRmonPacketsCounterClientOutputErrorPortn = _Pm20002maMondownRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 464, 1, 3),
    _Pm20002maMondownRmonPacketsCounterClientOutputErrorPortn_Type()
)
pm20002maMondownRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Pm20002maMondownRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20002maMondownRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20002maMondownRmonPacketsCounterClientOutputOverloadPortn = _Pm20002maMondownRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 464, 1, 4),
    _Pm20002maMondownRmonPacketsCounterClientOutputOverloadPortn_Type()
)
pm20002maMondownRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")
_Pm20002maMondownRmonBroadcastCounterClientOutputTable_Object = MibTable
pm20002maMondownRmonBroadcastCounterClientOutputTable = _Pm20002maMondownRmonBroadcastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 496)
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonBroadcastCounterClientOutputTable.setStatus("current")
_Pm20002maMondownRmonBroadcastCounterClientOutputEntry_Object = MibTableRow
pm20002maMondownRmonBroadcastCounterClientOutputEntry = _Pm20002maMondownRmonBroadcastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 496, 1)
)
pm20002maMondownRmonBroadcastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMondownRmonBroadcastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonBroadcastCounterClientOutputEntry.setStatus("current")


class _Pm20002maMondownRmonBroadcastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20002maMondownRmonBroadcastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMondownRmonBroadcastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20002maMondownRmonBroadcastCounterClientOutputIndex_Object = MibTableColumn
pm20002maMondownRmonBroadcastCounterClientOutputIndex = _Pm20002maMondownRmonBroadcastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 496, 1, 1),
    _Pm20002maMondownRmonBroadcastCounterClientOutputIndex_Type()
)
pm20002maMondownRmonBroadcastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonBroadcastCounterClientOutputIndex.setStatus("current")
_Pm20002maMondownRmonBroadcastCounterClientOutputValuePortn_Type = Counter64
_Pm20002maMondownRmonBroadcastCounterClientOutputValuePortn_Object = MibTableColumn
pm20002maMondownRmonBroadcastCounterClientOutputValuePortn = _Pm20002maMondownRmonBroadcastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 496, 1, 2),
    _Pm20002maMondownRmonBroadcastCounterClientOutputValuePortn_Type()
)
pm20002maMondownRmonBroadcastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonBroadcastCounterClientOutputValuePortn.setStatus("current")
_Pm20002maMondownRmonBroadcastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20002maMondownRmonBroadcastCounterClientOutputErrorPortn_Object = MibTableColumn
pm20002maMondownRmonBroadcastCounterClientOutputErrorPortn = _Pm20002maMondownRmonBroadcastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 496, 1, 3),
    _Pm20002maMondownRmonBroadcastCounterClientOutputErrorPortn_Type()
)
pm20002maMondownRmonBroadcastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonBroadcastCounterClientOutputErrorPortn.setStatus("current")
_Pm20002maMondownRmonBroadcastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20002maMondownRmonBroadcastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20002maMondownRmonBroadcastCounterClientOutputOverloadPortn = _Pm20002maMondownRmonBroadcastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 496, 1, 4),
    _Pm20002maMondownRmonBroadcastCounterClientOutputOverloadPortn_Type()
)
pm20002maMondownRmonBroadcastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonBroadcastCounterClientOutputOverloadPortn.setStatus("current")
_Pm20002maMondownRmonMulticastCounterClientOutputTable_Object = MibTable
pm20002maMondownRmonMulticastCounterClientOutputTable = _Pm20002maMondownRmonMulticastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 528)
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonMulticastCounterClientOutputTable.setStatus("current")
_Pm20002maMondownRmonMulticastCounterClientOutputEntry_Object = MibTableRow
pm20002maMondownRmonMulticastCounterClientOutputEntry = _Pm20002maMondownRmonMulticastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 528, 1)
)
pm20002maMondownRmonMulticastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMondownRmonMulticastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonMulticastCounterClientOutputEntry.setStatus("current")


class _Pm20002maMondownRmonMulticastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20002maMondownRmonMulticastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMondownRmonMulticastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20002maMondownRmonMulticastCounterClientOutputIndex_Object = MibTableColumn
pm20002maMondownRmonMulticastCounterClientOutputIndex = _Pm20002maMondownRmonMulticastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 528, 1, 1),
    _Pm20002maMondownRmonMulticastCounterClientOutputIndex_Type()
)
pm20002maMondownRmonMulticastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonMulticastCounterClientOutputIndex.setStatus("current")
_Pm20002maMondownRmonMulticastCounterClientOutputValuePortn_Type = Counter64
_Pm20002maMondownRmonMulticastCounterClientOutputValuePortn_Object = MibTableColumn
pm20002maMondownRmonMulticastCounterClientOutputValuePortn = _Pm20002maMondownRmonMulticastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 528, 1, 2),
    _Pm20002maMondownRmonMulticastCounterClientOutputValuePortn_Type()
)
pm20002maMondownRmonMulticastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonMulticastCounterClientOutputValuePortn.setStatus("current")
_Pm20002maMondownRmonMulticastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20002maMondownRmonMulticastCounterClientOutputErrorPortn_Object = MibTableColumn
pm20002maMondownRmonMulticastCounterClientOutputErrorPortn = _Pm20002maMondownRmonMulticastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 528, 1, 3),
    _Pm20002maMondownRmonMulticastCounterClientOutputErrorPortn_Type()
)
pm20002maMondownRmonMulticastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonMulticastCounterClientOutputErrorPortn.setStatus("current")
_Pm20002maMondownRmonMulticastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20002maMondownRmonMulticastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20002maMondownRmonMulticastCounterClientOutputOverloadPortn = _Pm20002maMondownRmonMulticastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 528, 1, 4),
    _Pm20002maMondownRmonMulticastCounterClientOutputOverloadPortn_Type()
)
pm20002maMondownRmonMulticastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonMulticastCounterClientOutputOverloadPortn.setStatus("current")
_Pm20002maMondownRmonPauseFrameCounterClientOutputTable_Object = MibTable
pm20002maMondownRmonPauseFrameCounterClientOutputTable = _Pm20002maMondownRmonPauseFrameCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 560)
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonPauseFrameCounterClientOutputTable.setStatus("current")
_Pm20002maMondownRmonPauseFrameCounterClientOutputEntry_Object = MibTableRow
pm20002maMondownRmonPauseFrameCounterClientOutputEntry = _Pm20002maMondownRmonPauseFrameCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 560, 1)
)
pm20002maMondownRmonPauseFrameCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMondownRmonPauseFrameCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonPauseFrameCounterClientOutputEntry.setStatus("current")


class _Pm20002maMondownRmonPauseFrameCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20002maMondownRmonPauseFrameCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMondownRmonPauseFrameCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20002maMondownRmonPauseFrameCounterClientOutputIndex_Object = MibTableColumn
pm20002maMondownRmonPauseFrameCounterClientOutputIndex = _Pm20002maMondownRmonPauseFrameCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 560, 1, 1),
    _Pm20002maMondownRmonPauseFrameCounterClientOutputIndex_Type()
)
pm20002maMondownRmonPauseFrameCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonPauseFrameCounterClientOutputIndex.setStatus("current")
_Pm20002maMondownRmonPauseFrameCounterClientOutputValuePortn_Type = Counter64
_Pm20002maMondownRmonPauseFrameCounterClientOutputValuePortn_Object = MibTableColumn
pm20002maMondownRmonPauseFrameCounterClientOutputValuePortn = _Pm20002maMondownRmonPauseFrameCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 560, 1, 2),
    _Pm20002maMondownRmonPauseFrameCounterClientOutputValuePortn_Type()
)
pm20002maMondownRmonPauseFrameCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonPauseFrameCounterClientOutputValuePortn.setStatus("current")
_Pm20002maMondownRmonPauseFrameCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20002maMondownRmonPauseFrameCounterClientOutputErrorPortn_Object = MibTableColumn
pm20002maMondownRmonPauseFrameCounterClientOutputErrorPortn = _Pm20002maMondownRmonPauseFrameCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 560, 1, 3),
    _Pm20002maMondownRmonPauseFrameCounterClientOutputErrorPortn_Type()
)
pm20002maMondownRmonPauseFrameCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonPauseFrameCounterClientOutputErrorPortn.setStatus("current")
_Pm20002maMondownRmonPauseFrameCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20002maMondownRmonPauseFrameCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20002maMondownRmonPauseFrameCounterClientOutputOverloadPortn = _Pm20002maMondownRmonPauseFrameCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 560, 1, 4),
    _Pm20002maMondownRmonPauseFrameCounterClientOutputOverloadPortn_Type()
)
pm20002maMondownRmonPauseFrameCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonPauseFrameCounterClientOutputOverloadPortn.setStatus("current")
_Pm20002maMondownRmonUnicastCounterClientOutputTable_Object = MibTable
pm20002maMondownRmonUnicastCounterClientOutputTable = _Pm20002maMondownRmonUnicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 688)
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonUnicastCounterClientOutputTable.setStatus("current")
_Pm20002maMondownRmonUnicastCounterClientOutputEntry_Object = MibTableRow
pm20002maMondownRmonUnicastCounterClientOutputEntry = _Pm20002maMondownRmonUnicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 688, 1)
)
pm20002maMondownRmonUnicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMondownRmonUnicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonUnicastCounterClientOutputEntry.setStatus("current")


class _Pm20002maMondownRmonUnicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20002maMondownRmonUnicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMondownRmonUnicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20002maMondownRmonUnicastCounterClientOutputIndex_Object = MibTableColumn
pm20002maMondownRmonUnicastCounterClientOutputIndex = _Pm20002maMondownRmonUnicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 688, 1, 1),
    _Pm20002maMondownRmonUnicastCounterClientOutputIndex_Type()
)
pm20002maMondownRmonUnicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonUnicastCounterClientOutputIndex.setStatus("current")
_Pm20002maMondownRmonUnicastCounterClientOutputValuePortn_Type = Counter64
_Pm20002maMondownRmonUnicastCounterClientOutputValuePortn_Object = MibTableColumn
pm20002maMondownRmonUnicastCounterClientOutputValuePortn = _Pm20002maMondownRmonUnicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 688, 1, 2),
    _Pm20002maMondownRmonUnicastCounterClientOutputValuePortn_Type()
)
pm20002maMondownRmonUnicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonUnicastCounterClientOutputValuePortn.setStatus("current")
_Pm20002maMondownRmonUnicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20002maMondownRmonUnicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm20002maMondownRmonUnicastCounterClientOutputErrorPortn = _Pm20002maMondownRmonUnicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 688, 1, 3),
    _Pm20002maMondownRmonUnicastCounterClientOutputErrorPortn_Type()
)
pm20002maMondownRmonUnicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonUnicastCounterClientOutputErrorPortn.setStatus("current")
_Pm20002maMondownRmonUnicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20002maMondownRmonUnicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20002maMondownRmonUnicastCounterClientOutputOverloadPortn = _Pm20002maMondownRmonUnicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 688, 1, 4),
    _Pm20002maMondownRmonUnicastCounterClientOutputOverloadPortn_Type()
)
pm20002maMondownRmonUnicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonUnicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm20002maMondownRmonNonunicastCounterClientOutputTable_Object = MibTable
pm20002maMondownRmonNonunicastCounterClientOutputTable = _Pm20002maMondownRmonNonunicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 720)
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonNonunicastCounterClientOutputTable.setStatus("current")
_Pm20002maMondownRmonNonunicastCounterClientOutputEntry_Object = MibTableRow
pm20002maMondownRmonNonunicastCounterClientOutputEntry = _Pm20002maMondownRmonNonunicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 720, 1)
)
pm20002maMondownRmonNonunicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maMondownRmonNonunicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20002maMondownRmonNonunicastCounterClientOutputEntry.setStatus("current")


class _Pm20002maMondownRmonNonunicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20002maMondownRmonNonunicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maMondownRmonNonunicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20002maMondownRmonNonunicastCounterClientOutputIndex_Object = MibTableColumn
pm20002maMondownRmonNonunicastCounterClientOutputIndex = _Pm20002maMondownRmonNonunicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 720, 1, 1),
    _Pm20002maMondownRmonNonunicastCounterClientOutputIndex_Type()
)
pm20002maMondownRmonNonunicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonNonunicastCounterClientOutputIndex.setStatus("current")
_Pm20002maMondownRmonNonunicastCounterClientOutputValuePortn_Type = Counter64
_Pm20002maMondownRmonNonunicastCounterClientOutputValuePortn_Object = MibTableColumn
pm20002maMondownRmonNonunicastCounterClientOutputValuePortn = _Pm20002maMondownRmonNonunicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 720, 1, 2),
    _Pm20002maMondownRmonNonunicastCounterClientOutputValuePortn_Type()
)
pm20002maMondownRmonNonunicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonNonunicastCounterClientOutputValuePortn.setStatus("current")
_Pm20002maMondownRmonNonunicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20002maMondownRmonNonunicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm20002maMondownRmonNonunicastCounterClientOutputErrorPortn = _Pm20002maMondownRmonNonunicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 720, 1, 3),
    _Pm20002maMondownRmonNonunicastCounterClientOutputErrorPortn_Type()
)
pm20002maMondownRmonNonunicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonNonunicastCounterClientOutputErrorPortn.setStatus("current")
_Pm20002maMondownRmonNonunicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20002maMondownRmonNonunicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20002maMondownRmonNonunicastCounterClientOutputOverloadPortn = _Pm20002maMondownRmonNonunicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 2, 4, 720, 1, 4),
    _Pm20002maMondownRmonNonunicastCounterClientOutputOverloadPortn_Type()
)
pm20002maMondownRmonNonunicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maMondownRmonNonunicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm20002maMonPerfOther_ObjectIdentity = ObjectIdentity
pm20002maMonPerfOther = _Pm20002maMonPerfOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5)
)
_Pm20002maMonPerfSync_ObjectIdentity = ObjectIdentity
pm20002maMonPerfSync = _Pm20002maMonPerfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 1)
)
_Pm20002maPerfEnable_Type = EkiOnOff
_Pm20002maPerfEnable_Object = MibScalar
pm20002maPerfEnable = _Pm20002maPerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 1, 257),
    _Pm20002maPerfEnable_Type()
)
pm20002maPerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maPerfEnable.setStatus("current")
_Pm20002maPerf15minSync_Type = EkiOnOff
_Pm20002maPerf15minSync_Object = MibScalar
pm20002maPerf15minSync = _Pm20002maPerf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 1, 259),
    _Pm20002maPerf15minSync_Type()
)
pm20002maPerf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maPerf15minSync.setStatus("current")
_Pm20002maPerf24hSync_Type = EkiOnOff
_Pm20002maPerf24hSync_Object = MibScalar
pm20002maPerf24hSync = _Pm20002maPerf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 1, 260),
    _Pm20002maPerf24hSync_Type()
)
pm20002maPerf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maPerf24hSync.setStatus("current")
_Pm20002maMonPerfTimeStamp_ObjectIdentity = ObjectIdentity
pm20002maMonPerfTimeStamp = _Pm20002maMonPerfTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 2)
)
_Pm20002maPerf15MinShort_Type = EkiOnOff
_Pm20002maPerf15MinShort_Object = MibScalar
pm20002maPerf15MinShort = _Pm20002maPerf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 2, 1),
    _Pm20002maPerf15MinShort_Type()
)
pm20002maPerf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maPerf15MinShort.setStatus("current")
_Pm20002maPerf15MinLong_Type = EkiOnOff
_Pm20002maPerf15MinLong_Object = MibScalar
pm20002maPerf15MinLong = _Pm20002maPerf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 2, 2),
    _Pm20002maPerf15MinLong_Type()
)
pm20002maPerf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maPerf15MinLong.setStatus("current")
_Pm20002maPerf24HoursShort_Type = Counter32
_Pm20002maPerf24HoursShort_Object = MibScalar
pm20002maPerf24HoursShort = _Pm20002maPerf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 2, 5),
    _Pm20002maPerf24HoursShort_Type()
)
pm20002maPerf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maPerf24HoursShort.setStatus("current")
_Pm20002maPerf24HoursLong_Type = Counter32
_Pm20002maPerf24HoursLong_Object = MibScalar
pm20002maPerf24HoursLong = _Pm20002maPerf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 2, 6),
    _Pm20002maPerf24HoursLong_Type()
)
pm20002maPerf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maPerf24HoursLong.setStatus("current")
_Pm20002maPerfCurrent15MinElapsedTime_Type = Counter32
_Pm20002maPerfCurrent15MinElapsedTime_Object = MibScalar
pm20002maPerfCurrent15MinElapsedTime = _Pm20002maPerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 2, 7),
    _Pm20002maPerfCurrent15MinElapsedTime_Type()
)
pm20002maPerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maPerfCurrent15MinElapsedTime.setStatus("current")
_Pm20002maPerfCurrent24HoursElapsedTime_Type = Counter32
_Pm20002maPerfCurrent24HoursElapsedTime_Object = MibScalar
pm20002maPerfCurrent24HoursElapsedTime = _Pm20002maPerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 5, 2, 8),
    _Pm20002maPerfCurrent24HoursElapsedTime_Type()
)
pm20002maPerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20002maPerfCurrent24HoursElapsedTime.setStatus("current")
_Pm20002maMonPerfClient_ObjectIdentity = ObjectIdentity
pm20002maMonPerfClient = _Pm20002maMonPerfClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6)
)
_Pm20002maPerfTelecomInputClientCurrent15StatTable_Object = MibTable
pm20002maPerfTelecomInputClientCurrent15StatTable = _Pm20002maPerfTelecomInputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatTable.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatEntry_Object = MibTableRow
pm20002maPerfTelecomInputClientCurrent15StatEntry = _Pm20002maPerfTelecomInputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1)
)
pm20002maPerfTelecomInputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomInputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatEntry.setStatus("current")


class _Pm20002maPerfTelecomInputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm20002maPerfTelecomInputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomInputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomInputClientCurrent15StatIndex_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatIndex = _Pm20002maPerfTelecomInputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 1),
    _Pm20002maPerfTelecomInputClientCurrent15StatIndex_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatIndex.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatInvCvPortn = _Pm20002maPerfTelecomInputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 2),
    _Pm20002maPerfTelecomInputClientCurrent15StatInvCvPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatCvValuePortn = _Pm20002maPerfTelecomInputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 3),
    _Pm20002maPerfTelecomInputClientCurrent15StatCvValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatInvEsPortn = _Pm20002maPerfTelecomInputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 4),
    _Pm20002maPerfTelecomInputClientCurrent15StatInvEsPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatEsValuePortn = _Pm20002maPerfTelecomInputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 5),
    _Pm20002maPerfTelecomInputClientCurrent15StatEsValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatInvSesPortn = _Pm20002maPerfTelecomInputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 6),
    _Pm20002maPerfTelecomInputClientCurrent15StatInvSesPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatSesValuePortn = _Pm20002maPerfTelecomInputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 7),
    _Pm20002maPerfTelecomInputClientCurrent15StatSesValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatInvSefsPortn = _Pm20002maPerfTelecomInputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 8),
    _Pm20002maPerfTelecomInputClientCurrent15StatInvSefsPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatSefsValuePortn = _Pm20002maPerfTelecomInputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 9),
    _Pm20002maPerfTelecomInputClientCurrent15StatSefsValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatInvUasPortn = _Pm20002maPerfTelecomInputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 10),
    _Pm20002maPerfTelecomInputClientCurrent15StatInvUasPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent15StatUasValuePortn = _Pm20002maPerfTelecomInputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 16, 1, 11),
    _Pm20002maPerfTelecomInputClientCurrent15StatUasValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryPort1Table_Object = MibTable
pm20002maPerfTelecomInputClientPast15StatHistoryPort1Table = _Pm20002maPerfTelecomInputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfTelecomInputClientPast15StatHistoryPort1Entry = _Pm20002maPerfTelecomInputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1)
)
pm20002maPerfTelecomInputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index = _Pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 1),
    _Pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistoryInvCvPort1 = _Pm20002maPerfTelecomInputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 2),
    _Pm20002maPerfTelecomInputClientPast15StatHistoryInvCvPort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistoryCvValuePort1 = _Pm20002maPerfTelecomInputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 3),
    _Pm20002maPerfTelecomInputClientPast15StatHistoryCvValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistoryInvEsPort1 = _Pm20002maPerfTelecomInputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 4),
    _Pm20002maPerfTelecomInputClientPast15StatHistoryInvEsPort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistoryEsValuePort1 = _Pm20002maPerfTelecomInputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 5),
    _Pm20002maPerfTelecomInputClientPast15StatHistoryEsValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistoryInvSesPort1 = _Pm20002maPerfTelecomInputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 6),
    _Pm20002maPerfTelecomInputClientPast15StatHistoryInvSesPort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistorySesValuePort1 = _Pm20002maPerfTelecomInputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 7),
    _Pm20002maPerfTelecomInputClientPast15StatHistorySesValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistoryInvSefsPort1 = _Pm20002maPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 8),
    _Pm20002maPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistorySefsValuePort1 = _Pm20002maPerfTelecomInputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 9),
    _Pm20002maPerfTelecomInputClientPast15StatHistorySefsValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistoryInvUasPort1 = _Pm20002maPerfTelecomInputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 10),
    _Pm20002maPerfTelecomInputClientPast15StatHistoryInvUasPort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast15StatHistoryUasValuePort1 = _Pm20002maPerfTelecomInputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 48, 1, 11),
    _Pm20002maPerfTelecomInputClientPast15StatHistoryUasValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatTable_Object = MibTable
pm20002maPerfTelecomInputClientCurrent24StatTable = _Pm20002maPerfTelecomInputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatTable.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatEntry_Object = MibTableRow
pm20002maPerfTelecomInputClientCurrent24StatEntry = _Pm20002maPerfTelecomInputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1)
)
pm20002maPerfTelecomInputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomInputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatEntry.setStatus("current")


class _Pm20002maPerfTelecomInputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm20002maPerfTelecomInputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomInputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomInputClientCurrent24StatIndex_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatIndex = _Pm20002maPerfTelecomInputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 1),
    _Pm20002maPerfTelecomInputClientCurrent24StatIndex_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatIndex.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatInvCvPortn = _Pm20002maPerfTelecomInputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 2),
    _Pm20002maPerfTelecomInputClientCurrent24StatInvCvPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatCvValuePortn = _Pm20002maPerfTelecomInputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 3),
    _Pm20002maPerfTelecomInputClientCurrent24StatCvValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatInvEsPortn = _Pm20002maPerfTelecomInputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 4),
    _Pm20002maPerfTelecomInputClientCurrent24StatInvEsPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatEsValuePortn = _Pm20002maPerfTelecomInputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 5),
    _Pm20002maPerfTelecomInputClientCurrent24StatEsValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatInvSesPortn = _Pm20002maPerfTelecomInputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 6),
    _Pm20002maPerfTelecomInputClientCurrent24StatInvSesPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatSesValuePortn = _Pm20002maPerfTelecomInputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 7),
    _Pm20002maPerfTelecomInputClientCurrent24StatSesValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatInvSefsPortn = _Pm20002maPerfTelecomInputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 8),
    _Pm20002maPerfTelecomInputClientCurrent24StatInvSefsPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatSefsValuePortn = _Pm20002maPerfTelecomInputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 9),
    _Pm20002maPerfTelecomInputClientCurrent24StatSefsValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatInvUasPortn = _Pm20002maPerfTelecomInputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 10),
    _Pm20002maPerfTelecomInputClientCurrent24StatInvUasPortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm20002maPerfTelecomInputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomInputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm20002maPerfTelecomInputClientCurrent24StatUasValuePortn = _Pm20002maPerfTelecomInputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 80, 1, 11),
    _Pm20002maPerfTelecomInputClientCurrent24StatUasValuePortn_Type()
)
pm20002maPerfTelecomInputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryPort1Table_Object = MibTable
pm20002maPerfTelecomInputClientPast24StatHistoryPort1Table = _Pm20002maPerfTelecomInputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfTelecomInputClientPast24StatHistoryPort1Entry = _Pm20002maPerfTelecomInputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1)
)
pm20002maPerfTelecomInputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index = _Pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 1),
    _Pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistoryInvCvPort1 = _Pm20002maPerfTelecomInputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 2),
    _Pm20002maPerfTelecomInputClientPast24StatHistoryInvCvPort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistoryCvValuePort1 = _Pm20002maPerfTelecomInputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 3),
    _Pm20002maPerfTelecomInputClientPast24StatHistoryCvValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistoryInvEsPort1 = _Pm20002maPerfTelecomInputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 4),
    _Pm20002maPerfTelecomInputClientPast24StatHistoryInvEsPort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistoryEsValuePort1 = _Pm20002maPerfTelecomInputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 5),
    _Pm20002maPerfTelecomInputClientPast24StatHistoryEsValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistoryInvSesPort1 = _Pm20002maPerfTelecomInputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 6),
    _Pm20002maPerfTelecomInputClientPast24StatHistoryInvSesPort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistorySesValuePort1 = _Pm20002maPerfTelecomInputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 7),
    _Pm20002maPerfTelecomInputClientPast24StatHistorySesValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistoryInvSefsPort1 = _Pm20002maPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 8),
    _Pm20002maPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistorySefsValuePort1 = _Pm20002maPerfTelecomInputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 9),
    _Pm20002maPerfTelecomInputClientPast24StatHistorySefsValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20002maPerfTelecomInputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistoryInvUasPort1 = _Pm20002maPerfTelecomInputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 10),
    _Pm20002maPerfTelecomInputClientPast24StatHistoryInvUasPort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm20002maPerfTelecomInputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomInputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm20002maPerfTelecomInputClientPast24StatHistoryUasValuePort1 = _Pm20002maPerfTelecomInputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 112, 1, 11),
    _Pm20002maPerfTelecomInputClientPast24StatHistoryUasValuePort1_Type()
)
pm20002maPerfTelecomInputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomInputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatTable_Object = MibTable
pm20002maPerfTelecomOutputClientCurrent15StatTable = _Pm20002maPerfTelecomOutputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatTable.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatEntry_Object = MibTableRow
pm20002maPerfTelecomOutputClientCurrent15StatEntry = _Pm20002maPerfTelecomOutputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1)
)
pm20002maPerfTelecomOutputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomOutputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatEntry.setStatus("current")


class _Pm20002maPerfTelecomOutputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm20002maPerfTelecomOutputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomOutputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomOutputClientCurrent15StatIndex_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatIndex = _Pm20002maPerfTelecomOutputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 1),
    _Pm20002maPerfTelecomOutputClientCurrent15StatIndex_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatIndex.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatInvCvPortn = _Pm20002maPerfTelecomOutputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 2),
    _Pm20002maPerfTelecomOutputClientCurrent15StatInvCvPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatCvValuePortn = _Pm20002maPerfTelecomOutputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 3),
    _Pm20002maPerfTelecomOutputClientCurrent15StatCvValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatInvEsPortn = _Pm20002maPerfTelecomOutputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 4),
    _Pm20002maPerfTelecomOutputClientCurrent15StatInvEsPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatEsValuePortn = _Pm20002maPerfTelecomOutputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 5),
    _Pm20002maPerfTelecomOutputClientCurrent15StatEsValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatInvSesPortn = _Pm20002maPerfTelecomOutputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 6),
    _Pm20002maPerfTelecomOutputClientCurrent15StatInvSesPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatSesValuePortn = _Pm20002maPerfTelecomOutputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 7),
    _Pm20002maPerfTelecomOutputClientCurrent15StatSesValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatInvSefsPortn = _Pm20002maPerfTelecomOutputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 8),
    _Pm20002maPerfTelecomOutputClientCurrent15StatInvSefsPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatSefsValuePortn = _Pm20002maPerfTelecomOutputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 9),
    _Pm20002maPerfTelecomOutputClientCurrent15StatSefsValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatInvUasPortn = _Pm20002maPerfTelecomOutputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 10),
    _Pm20002maPerfTelecomOutputClientCurrent15StatInvUasPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent15StatUasValuePortn = _Pm20002maPerfTelecomOutputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 144, 1, 11),
    _Pm20002maPerfTelecomOutputClientCurrent15StatUasValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Table_Object = MibTable
pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Table = _Pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Entry = _Pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1)
)
pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index = _Pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 1),
    _Pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistoryInvCvPort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 2),
    _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistoryCvValuePort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 3),
    _Pm20002maPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistoryInvEsPort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 4),
    _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistoryEsValuePort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 5),
    _Pm20002maPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistoryInvSesPort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 6),
    _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistorySesValuePort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 7),
    _Pm20002maPerfTelecomOutputClientPast15StatHistorySesValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 8),
    _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistorySefsValuePort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 9),
    _Pm20002maPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistoryInvUasPort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 10),
    _Pm20002maPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast15StatHistoryUasValuePort1 = _Pm20002maPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 176, 1, 11),
    _Pm20002maPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatTable_Object = MibTable
pm20002maPerfTelecomOutputClientCurrent24StatTable = _Pm20002maPerfTelecomOutputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatTable.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatEntry_Object = MibTableRow
pm20002maPerfTelecomOutputClientCurrent24StatEntry = _Pm20002maPerfTelecomOutputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1)
)
pm20002maPerfTelecomOutputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomOutputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatEntry.setStatus("current")


class _Pm20002maPerfTelecomOutputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm20002maPerfTelecomOutputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomOutputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomOutputClientCurrent24StatIndex_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatIndex = _Pm20002maPerfTelecomOutputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 1),
    _Pm20002maPerfTelecomOutputClientCurrent24StatIndex_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatIndex.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatInvCvPortn = _Pm20002maPerfTelecomOutputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 2),
    _Pm20002maPerfTelecomOutputClientCurrent24StatInvCvPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatCvValuePortn = _Pm20002maPerfTelecomOutputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 3),
    _Pm20002maPerfTelecomOutputClientCurrent24StatCvValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatInvEsPortn = _Pm20002maPerfTelecomOutputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 4),
    _Pm20002maPerfTelecomOutputClientCurrent24StatInvEsPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatEsValuePortn = _Pm20002maPerfTelecomOutputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 5),
    _Pm20002maPerfTelecomOutputClientCurrent24StatEsValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatInvSesPortn = _Pm20002maPerfTelecomOutputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 6),
    _Pm20002maPerfTelecomOutputClientCurrent24StatInvSesPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatSesValuePortn = _Pm20002maPerfTelecomOutputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 7),
    _Pm20002maPerfTelecomOutputClientCurrent24StatSesValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatInvSefsPortn = _Pm20002maPerfTelecomOutputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 8),
    _Pm20002maPerfTelecomOutputClientCurrent24StatInvSefsPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatSefsValuePortn = _Pm20002maPerfTelecomOutputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 9),
    _Pm20002maPerfTelecomOutputClientCurrent24StatSefsValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatInvUasPortn = _Pm20002maPerfTelecomOutputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 10),
    _Pm20002maPerfTelecomOutputClientCurrent24StatInvUasPortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm20002maPerfTelecomOutputClientCurrent24StatUasValuePortn = _Pm20002maPerfTelecomOutputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 208, 1, 11),
    _Pm20002maPerfTelecomOutputClientCurrent24StatUasValuePortn_Type()
)
pm20002maPerfTelecomOutputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Table_Object = MibTable
pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Table = _Pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Entry = _Pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1)
)
pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index = _Pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 1),
    _Pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistoryInvCvPort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 2),
    _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistoryCvValuePort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 3),
    _Pm20002maPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistoryInvEsPort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 4),
    _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistoryEsValuePort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 5),
    _Pm20002maPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistoryInvSesPort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 6),
    _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistorySesValuePort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 7),
    _Pm20002maPerfTelecomOutputClientPast24StatHistorySesValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 8),
    _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistorySefsValuePort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 9),
    _Pm20002maPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20002maPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistoryInvUasPort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 10),
    _Pm20002maPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm20002maPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm20002maPerfTelecomOutputClientPast24StatHistoryUasValuePort1 = _Pm20002maPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 240, 1, 11),
    _Pm20002maPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type()
)
pm20002maPerfTelecomOutputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomOutputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm20002maPerfDatacomClientCurrent15StatTable_Object = MibTable
pm20002maPerfDatacomClientCurrent15StatTable = _Pm20002maPerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848)
)
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientCurrent15StatTable.setStatus("current")
_Pm20002maPerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pm20002maPerfDatacomClientCurrent15StatEntry = _Pm20002maPerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1)
)
pm20002maPerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pm20002maPerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm20002maPerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pm20002maPerfDatacomClientCurrent15StatIndex = _Pm20002maPerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1, 1),
    _Pm20002maPerfDatacomClientCurrent15StatIndex_Type()
)
pm20002maPerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientCurrent15StatIndex.setStatus("current")
_Pm20002maperfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Pm20002maperfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent15StatInCrcCountInvPortn = _Pm20002maperfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1, 4),
    _Pm20002maperfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
pm20002maperfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Pm20002maperfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent15StatInCrcCountPortn = _Pm20002maperfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1, 5),
    _Pm20002maperfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
pm20002maperfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent15StatInPacketCountInvPortn_Type = EkiOnOff
_Pm20002maperfdatacomclientCurrent15StatInPacketCountInvPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent15StatInPacketCountInvPortn = _Pm20002maperfdatacomclientCurrent15StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1, 6),
    _Pm20002maperfdatacomclientCurrent15StatInPacketCountInvPortn_Type()
)
pm20002maperfdatacomclientCurrent15StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent15StatInPacketCountInvPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent15StatInPacketCountPortn_Type = Counter64
_Pm20002maperfdatacomclientCurrent15StatInPacketCountPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent15StatInPacketCountPortn = _Pm20002maperfdatacomclientCurrent15StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1, 7),
    _Pm20002maperfdatacomclientCurrent15StatInPacketCountPortn_Type()
)
pm20002maperfdatacomclientCurrent15StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent15StatInPacketCountPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent15StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm20002maperfdatacomclientCurrent15StatOutCrcCountInvPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent15StatOutCrcCountInvPortn = _Pm20002maperfdatacomclientCurrent15StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1, 28),
    _Pm20002maperfdatacomclientCurrent15StatOutCrcCountInvPortn_Type()
)
pm20002maperfdatacomclientCurrent15StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent15StatOutCrcCountInvPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent15StatOutCrcCountPortn_Type = Counter64
_Pm20002maperfdatacomclientCurrent15StatOutCrcCountPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent15StatOutCrcCountPortn = _Pm20002maperfdatacomclientCurrent15StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1, 29),
    _Pm20002maperfdatacomclientCurrent15StatOutCrcCountPortn_Type()
)
pm20002maperfdatacomclientCurrent15StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent15StatOutCrcCountPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent15StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm20002maperfdatacomclientCurrent15StatOutPacketCountInvPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent15StatOutPacketCountInvPortn = _Pm20002maperfdatacomclientCurrent15StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1, 30),
    _Pm20002maperfdatacomclientCurrent15StatOutPacketCountInvPortn_Type()
)
pm20002maperfdatacomclientCurrent15StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent15StatOutPacketCountInvPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent15StatOutPacketCountPortn_Type = Counter64
_Pm20002maperfdatacomclientCurrent15StatOutPacketCountPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent15StatOutPacketCountPortn = _Pm20002maperfdatacomclientCurrent15StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 848, 1, 31),
    _Pm20002maperfdatacomclientCurrent15StatOutPacketCountPortn_Type()
)
pm20002maperfdatacomclientCurrent15StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent15StatOutPacketCountPortn.setStatus("current")
_Pm20002maPerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pm20002maPerfDatacomClientPast15StatHistoryPort1Table = _Pm20002maPerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880)
)
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfDatacomClientPast15StatHistoryPort1Entry = _Pm20002maPerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1)
)
pm20002maPerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfDatacomClientPast15StatHistoryPort1Index = _Pm20002maPerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1, 1),
    _Pm20002maPerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pm20002maPerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Pm20002maperfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Pm20002maperfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast15StatInCrcCountInvPort1 = _Pm20002maperfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1, 4),
    _Pm20002maperfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
pm20002maperfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Pm20002maperfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Pm20002maperfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast15StatInCrcCountPort1 = _Pm20002maperfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1, 5),
    _Pm20002maperfdatacomclientPast15StatInCrcCountPort1_Type()
)
pm20002maperfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Pm20002maperfdatacomclientPast15StatInPacketCountInvPort1_Type = EkiOnOff
_Pm20002maperfdatacomclientPast15StatInPacketCountInvPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast15StatInPacketCountInvPort1 = _Pm20002maperfdatacomclientPast15StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1, 6),
    _Pm20002maperfdatacomclientPast15StatInPacketCountInvPort1_Type()
)
pm20002maperfdatacomclientPast15StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast15StatInPacketCountInvPort1.setStatus("current")
_Pm20002maperfdatacomclientPast15StatInPacketCountPort1_Type = Counter64
_Pm20002maperfdatacomclientPast15StatInPacketCountPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast15StatInPacketCountPort1 = _Pm20002maperfdatacomclientPast15StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1, 7),
    _Pm20002maperfdatacomclientPast15StatInPacketCountPort1_Type()
)
pm20002maperfdatacomclientPast15StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast15StatInPacketCountPort1.setStatus("current")
_Pm20002maperfdatacomclientPast15StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm20002maperfdatacomclientPast15StatOutCrcCountInvPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast15StatOutCrcCountInvPort1 = _Pm20002maperfdatacomclientPast15StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1, 28),
    _Pm20002maperfdatacomclientPast15StatOutCrcCountInvPort1_Type()
)
pm20002maperfdatacomclientPast15StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast15StatOutCrcCountInvPort1.setStatus("current")
_Pm20002maperfdatacomclientPast15StatOutCrcCountPort1_Type = Counter64
_Pm20002maperfdatacomclientPast15StatOutCrcCountPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast15StatOutCrcCountPort1 = _Pm20002maperfdatacomclientPast15StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1, 29),
    _Pm20002maperfdatacomclientPast15StatOutCrcCountPort1_Type()
)
pm20002maperfdatacomclientPast15StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast15StatOutCrcCountPort1.setStatus("current")
_Pm20002maperfdatacomclientPast15StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm20002maperfdatacomclientPast15StatOutPacketCountInvPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast15StatOutPacketCountInvPort1 = _Pm20002maperfdatacomclientPast15StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1, 30),
    _Pm20002maperfdatacomclientPast15StatOutPacketCountInvPort1_Type()
)
pm20002maperfdatacomclientPast15StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast15StatOutPacketCountInvPort1.setStatus("current")
_Pm20002maperfdatacomclientPast15StatOutPacketCountPort1_Type = Counter64
_Pm20002maperfdatacomclientPast15StatOutPacketCountPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast15StatOutPacketCountPort1 = _Pm20002maperfdatacomclientPast15StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 880, 1, 31),
    _Pm20002maperfdatacomclientPast15StatOutPacketCountPort1_Type()
)
pm20002maperfdatacomclientPast15StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast15StatOutPacketCountPort1.setStatus("current")
_Pm20002maPerfDatacomClientCurrent24StatTable_Object = MibTable
pm20002maPerfDatacomClientCurrent24StatTable = _Pm20002maPerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912)
)
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientCurrent24StatTable.setStatus("current")
_Pm20002maPerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pm20002maPerfDatacomClientCurrent24StatEntry = _Pm20002maPerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1)
)
pm20002maPerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pm20002maPerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm20002maPerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pm20002maPerfDatacomClientCurrent24StatIndex = _Pm20002maPerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1, 1),
    _Pm20002maPerfDatacomClientCurrent24StatIndex_Type()
)
pm20002maPerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientCurrent24StatIndex.setStatus("current")
_Pm20002maperfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Pm20002maperfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent24StatInCrcCountInvPortn = _Pm20002maperfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1, 4),
    _Pm20002maperfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
pm20002maperfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Pm20002maperfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent24StatInCrcCountPortn = _Pm20002maperfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1, 5),
    _Pm20002maperfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
pm20002maperfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent24StatInPacketCountInvPortn_Type = EkiOnOff
_Pm20002maperfdatacomclientCurrent24StatInPacketCountInvPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent24StatInPacketCountInvPortn = _Pm20002maperfdatacomclientCurrent24StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1, 6),
    _Pm20002maperfdatacomclientCurrent24StatInPacketCountInvPortn_Type()
)
pm20002maperfdatacomclientCurrent24StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent24StatInPacketCountInvPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent24StatInPacketCountPortn_Type = Counter64
_Pm20002maperfdatacomclientCurrent24StatInPacketCountPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent24StatInPacketCountPortn = _Pm20002maperfdatacomclientCurrent24StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1, 7),
    _Pm20002maperfdatacomclientCurrent24StatInPacketCountPortn_Type()
)
pm20002maperfdatacomclientCurrent24StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent24StatInPacketCountPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent24StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm20002maperfdatacomclientCurrent24StatOutCrcCountInvPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent24StatOutCrcCountInvPortn = _Pm20002maperfdatacomclientCurrent24StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1, 28),
    _Pm20002maperfdatacomclientCurrent24StatOutCrcCountInvPortn_Type()
)
pm20002maperfdatacomclientCurrent24StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent24StatOutCrcCountInvPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent24StatOutCrcCountPortn_Type = Counter64
_Pm20002maperfdatacomclientCurrent24StatOutCrcCountPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent24StatOutCrcCountPortn = _Pm20002maperfdatacomclientCurrent24StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1, 29),
    _Pm20002maperfdatacomclientCurrent24StatOutCrcCountPortn_Type()
)
pm20002maperfdatacomclientCurrent24StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent24StatOutCrcCountPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent24StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm20002maperfdatacomclientCurrent24StatOutPacketCountInvPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent24StatOutPacketCountInvPortn = _Pm20002maperfdatacomclientCurrent24StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1, 30),
    _Pm20002maperfdatacomclientCurrent24StatOutPacketCountInvPortn_Type()
)
pm20002maperfdatacomclientCurrent24StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent24StatOutPacketCountInvPortn.setStatus("current")
_Pm20002maperfdatacomclientCurrent24StatOutPacketCountPortn_Type = Counter64
_Pm20002maperfdatacomclientCurrent24StatOutPacketCountPortn_Object = MibTableColumn
pm20002maperfdatacomclientCurrent24StatOutPacketCountPortn = _Pm20002maperfdatacomclientCurrent24StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 912, 1, 31),
    _Pm20002maperfdatacomclientCurrent24StatOutPacketCountPortn_Type()
)
pm20002maperfdatacomclientCurrent24StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientCurrent24StatOutPacketCountPortn.setStatus("current")
_Pm20002maPerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pm20002maPerfDatacomClientPast24StatHistoryPort1Table = _Pm20002maPerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944)
)
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfDatacomClientPast24StatHistoryPort1Entry = _Pm20002maPerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1)
)
pm20002maPerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfDatacomClientPast24StatHistoryPort1Index = _Pm20002maPerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1, 1),
    _Pm20002maPerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pm20002maPerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Pm20002maperfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Pm20002maperfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast24StatInCrcCountInvPort1 = _Pm20002maperfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1, 4),
    _Pm20002maperfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
pm20002maperfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Pm20002maperfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Pm20002maperfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast24StatInCrcCountPort1 = _Pm20002maperfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1, 5),
    _Pm20002maperfdatacomclientPast24StatInCrcCountPort1_Type()
)
pm20002maperfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Pm20002maperfdatacomclientPast24StatInPacketCountInvPort1_Type = EkiOnOff
_Pm20002maperfdatacomclientPast24StatInPacketCountInvPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast24StatInPacketCountInvPort1 = _Pm20002maperfdatacomclientPast24StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1, 6),
    _Pm20002maperfdatacomclientPast24StatInPacketCountInvPort1_Type()
)
pm20002maperfdatacomclientPast24StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast24StatInPacketCountInvPort1.setStatus("current")
_Pm20002maperfdatacomclientPast24StatInPacketCountPort1_Type = Counter64
_Pm20002maperfdatacomclientPast24StatInPacketCountPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast24StatInPacketCountPort1 = _Pm20002maperfdatacomclientPast24StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1, 7),
    _Pm20002maperfdatacomclientPast24StatInPacketCountPort1_Type()
)
pm20002maperfdatacomclientPast24StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast24StatInPacketCountPort1.setStatus("current")
_Pm20002maperfdatacomclientPast24StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm20002maperfdatacomclientPast24StatOutCrcCountInvPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast24StatOutCrcCountInvPort1 = _Pm20002maperfdatacomclientPast24StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1, 28),
    _Pm20002maperfdatacomclientPast24StatOutCrcCountInvPort1_Type()
)
pm20002maperfdatacomclientPast24StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast24StatOutCrcCountInvPort1.setStatus("current")
_Pm20002maperfdatacomclientPast24StatOutCrcCountPort1_Type = Counter64
_Pm20002maperfdatacomclientPast24StatOutCrcCountPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast24StatOutCrcCountPort1 = _Pm20002maperfdatacomclientPast24StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1, 29),
    _Pm20002maperfdatacomclientPast24StatOutCrcCountPort1_Type()
)
pm20002maperfdatacomclientPast24StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast24StatOutCrcCountPort1.setStatus("current")
_Pm20002maperfdatacomclientPast24StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm20002maperfdatacomclientPast24StatOutPacketCountInvPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast24StatOutPacketCountInvPort1 = _Pm20002maperfdatacomclientPast24StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1, 30),
    _Pm20002maperfdatacomclientPast24StatOutPacketCountInvPort1_Type()
)
pm20002maperfdatacomclientPast24StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast24StatOutPacketCountInvPort1.setStatus("current")
_Pm20002maperfdatacomclientPast24StatOutPacketCountPort1_Type = Counter64
_Pm20002maperfdatacomclientPast24StatOutPacketCountPort1_Object = MibTableColumn
pm20002maperfdatacomclientPast24StatOutPacketCountPort1 = _Pm20002maperfdatacomclientPast24StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 6, 944, 1, 31),
    _Pm20002maperfdatacomclientPast24StatOutPacketCountPort1_Type()
)
pm20002maperfdatacomclientPast24StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maperfdatacomclientPast24StatOutPacketCountPort1.setStatus("current")
_Pm20002maMonPerfLine_ObjectIdentity = ObjectIdentity
pm20002maMonPerfLine = _Pm20002maMonPerfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7)
)
_Pm20002maPerfTelecomLinePostFecCurrent15StatTable_Object = MibTable
pm20002maPerfTelecomLinePostFecCurrent15StatTable = _Pm20002maPerfTelecomLinePostFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatTable.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatEntry_Object = MibTableRow
pm20002maPerfTelecomLinePostFecCurrent15StatEntry = _Pm20002maPerfTelecomLinePostFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1)
)
pm20002maPerfTelecomLinePostFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomLinePostFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatEntry.setStatus("current")


class _Pm20002maPerfTelecomLinePostFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm20002maPerfTelecomLinePostFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomLinePostFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomLinePostFecCurrent15StatIndex_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatIndex = _Pm20002maPerfTelecomLinePostFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 1),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatIndex_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatIndex.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvCvPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatInvCvPortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 2),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatInvCvPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatInvCvPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatCvValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent15StatCvValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatCvValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 3),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatCvValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatCvValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvEsPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatInvEsPortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 4),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatInvEsPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatInvEsPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatEsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent15StatEsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatEsValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 5),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatEsValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatEsValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvSesPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatInvSesPortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 6),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatInvSesPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatInvSesPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatSesValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent15StatSesValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatSesValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 7),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatSesValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatSesValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatInvSefsPortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 8),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatInvSefsPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatSefsValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 9),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatSefsValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent15StatInvUasPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatInvUasPortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 10),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatInvUasPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatInvUasPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent15StatUasValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent15StatUasValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent15StatUasValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 336, 1, 11),
    _Pm20002maPerfTelecomLinePostFecCurrent15StatUasValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent15StatUasValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Table_Object = MibTable
pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Table = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Entry = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1)
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 1),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 2),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 3),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 4),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 5),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 6),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistorySesValuePort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 7),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistorySesValuePort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 8),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 9),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 10),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1 = _Pm20002maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 337, 1, 11),
    _Pm20002maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatTable_Object = MibTable
pm20002maPerfTelecomLinePostFecCurrent24StatTable = _Pm20002maPerfTelecomLinePostFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatTable.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatEntry_Object = MibTableRow
pm20002maPerfTelecomLinePostFecCurrent24StatEntry = _Pm20002maPerfTelecomLinePostFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1)
)
pm20002maPerfTelecomLinePostFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomLinePostFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatEntry.setStatus("current")


class _Pm20002maPerfTelecomLinePostFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm20002maPerfTelecomLinePostFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomLinePostFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomLinePostFecCurrent24StatIndex_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatIndex = _Pm20002maPerfTelecomLinePostFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 1),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatIndex_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatIndex.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvCvPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatInvCvPortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 2),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatInvCvPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatInvCvPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatCvValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent24StatCvValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatCvValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 3),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatCvValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatCvValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvEsPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatInvEsPortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 4),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatInvEsPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatInvEsPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatEsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent24StatEsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatEsValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 5),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatEsValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatEsValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvSesPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatInvSesPortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 6),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatInvSesPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatInvSesPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatSesValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent24StatSesValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatSesValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 7),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatSesValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatSesValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatInvSefsPortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 8),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatInvSefsPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatSefsValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 9),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatSefsValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecCurrent24StatInvUasPortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatInvUasPortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 10),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatInvUasPortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatInvUasPortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecCurrent24StatUasValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecCurrent24StatUasValuePortn_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecCurrent24StatUasValuePortn = _Pm20002maPerfTelecomLinePostFecCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 338, 1, 11),
    _Pm20002maPerfTelecomLinePostFecCurrent24StatUasValuePortn_Type()
)
pm20002maPerfTelecomLinePostFecCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecCurrent24StatUasValuePortn.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Table_Object = MibTable
pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Table = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Entry = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1)
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 1),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 2),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 3),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 4),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 5),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 6),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistorySesValuePort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 7),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistorySesValuePort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 8),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 9),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 10),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setStatus("current")
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm20002maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1 = _Pm20002maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 339, 1, 11),
    _Pm20002maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type()
)
pm20002maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatTable_Object = MibTable
pm20002maPerfTelecomBerLinePreFecCurrent15StatTable = _Pm20002maPerfTelecomBerLinePreFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 352)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent15StatTable.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatEntry_Object = MibTableRow
pm20002maPerfTelecomBerLinePreFecCurrent15StatEntry = _Pm20002maPerfTelecomBerLinePreFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 352, 1)
)
pm20002maPerfTelecomBerLinePreFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent15StatEntry.setStatus("current")


class _Pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex = _Pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 352, 1, 1),
    _Pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn = _Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 352, 1, 2),
    _Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn = _Pm20002maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 352, 1, 3),
    _Pm20002maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn = _Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 352, 1, 4),
    _Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn = _Pm20002maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 352, 1, 5),
    _Pm20002maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn = _Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 352, 1, 6),
    _Pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn = _Pm20002maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 352, 1, 7),
    _Pm20002maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object = MibTable
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table = _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 353)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry = _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 353, 1)
)
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index = _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 353, 1, 1),
    _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type()
)
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1 = _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 353, 1, 2),
    _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1 = _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 353, 1, 3),
    _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1 = _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 353, 1, 4),
    _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1 = _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 353, 1, 5),
    _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1 = _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 353, 1, 6),
    _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1 = _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 353, 1, 7),
    _Pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatTable_Object = MibTable
pm20002maPerfTelecomBerLinePreFecCurrent24StatTable = _Pm20002maPerfTelecomBerLinePreFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 354)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent24StatTable.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatEntry_Object = MibTableRow
pm20002maPerfTelecomBerLinePreFecCurrent24StatEntry = _Pm20002maPerfTelecomBerLinePreFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 354, 1)
)
pm20002maPerfTelecomBerLinePreFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent24StatEntry.setStatus("current")


class _Pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex = _Pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 354, 1, 1),
    _Pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn = _Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 354, 1, 2),
    _Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn = _Pm20002maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 354, 1, 3),
    _Pm20002maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn = _Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 354, 1, 4),
    _Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn = _Pm20002maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 354, 1, 5),
    _Pm20002maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn = _Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 354, 1, 6),
    _Pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn = _Pm20002maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 354, 1, 7),
    _Pm20002maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type()
)
pm20002maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object = MibTable
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table = _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 355)
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry = _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 355, 1)
)
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20002ma-MIB", "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index = _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 355, 1, 1),
    _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type()
)
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1 = _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 355, 1, 2),
    _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1 = _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 355, 1, 3),
    _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1 = _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 355, 1, 4),
    _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1 = _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 355, 1, 5),
    _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1 = _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 355, 1, 6),
    _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setStatus("current")
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1 = _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 73, 11, 7, 355, 1, 7),
    _Pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type()
)
pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setStatus("current")

# Managed Objects groups


# Notification objects

pm20002maLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 30)
)
pm20002maLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapLineNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm20002maLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 31)
)
pm20002maLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapLineNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm20002maLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 32)
)
pm20002maLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapLineNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm20002maLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 33)
)
pm20002maLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapLineNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm20002maLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 34)
)
pm20002maLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmLineFailPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002maAlmLineHwFailPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapLineNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maLineTrapCritGoesOn.setStatus(
        "current"
    )

pm20002maLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 35)
)
pm20002maLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmLineFailPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002maAlmLineHwFailPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapLineNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maLineTrapCritGoesOff.setStatus(
        "current"
    )

pm20002maClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 40)
)
pm20002maClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapPortNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm20002maClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 41)
)
pm20002maClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapPortNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm20002maClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 42)
)
pm20002maClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapPortNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm20002maClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 43)
)
pm20002maClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapPortNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm20002maClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 44)
)
pm20002maClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmFailAccPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002maAlmHwFailAccPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapPortNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maClientTrapCritGoesOn.setStatus(
        "current"
    )

pm20002maClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 45)
)
pm20002maClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmFailAccPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002maAlmHwFailAccPortn"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapPortNumber"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maClientTrapCritGoesOff.setStatus(
        "current"
    )

pm20002maPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 50)
)
pm20002maPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmDefFuseB"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002maAlmDefFuseA"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm20002maPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 73, 10, 51)
)
pm20002maPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20002ma-MIB", "pm20002maAlmDefFuseB"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002maAlmDefFuseA"),
        ("EKINOPS-Pm20002ma-MIB", "pm20002matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20002maPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm20002ma-MIB",
    **{"Pm20002maMultiRate": Pm20002maMultiRate,
       "Pm20002maOtxMode": Pm20002maOtxMode,
       "Pm20002maOtxGrid": Pm20002maOtxGrid,
       "Pm20002maAdjustValue": Pm20002maAdjustValue,
       "Pm20002maClientProtocol": Pm20002maClientProtocol,
       "Pm20002maProtocolMode": Pm20002maProtocolMode,
       "Pm20002maOtxChannel": Pm20002maOtxChannel,
       "Pm20002maOrxChannel": Pm20002maOrxChannel,
       "Pm20002maDccMode": Pm20002maDccMode,
       "Pm20002maModuleMode": Pm20002maModuleMode,
       "modulePm20002ma": modulePm20002ma,
       "pm20002maalarms": pm20002maalarms,
       "pm20002maAlmOther": pm20002maAlmOther,
       "pm20002maAlmOtherNurg": pm20002maAlmOtherNurg,
       "pm20002maAlmsynthAlm2": pm20002maAlmsynthAlm2,
       "pm20002maAlmConfTableSave": pm20002maAlmConfTableSave,
       "pm20002maAlmInvUpload": pm20002maAlmInvUpload,
       "pm20002maAlmConfTableLoad": pm20002maAlmConfTableLoad,
       "pm20002maAlmCorrelatOff": pm20002maAlmCorrelatOff,
       "pm20002maAlmMaintenanceOn": pm20002maAlmMaintenanceOn,
       "pm20002maAlmclientQsfpWarnDdm": pm20002maAlmclientQsfpWarnDdm,
       "pm20002maAlmTrscv1VccLowWng1": pm20002maAlmTrscv1VccLowWng1,
       "pm20002maAlmTrscv1VccHighWng1": pm20002maAlmTrscv1VccHighWng1,
       "pm20002maAlmTrscv1TempLowWng1": pm20002maAlmTrscv1TempLowWng1,
       "pm20002maAlmTrscv1TempHighWng1": pm20002maAlmTrscv1TempHighWng1,
       "pm20002maAlmTrscv2VccLowWng1": pm20002maAlmTrscv2VccLowWng1,
       "pm20002maAlmTrscv2VccHighWng1": pm20002maAlmTrscv2VccHighWng1,
       "pm20002maAlmTrscv2TempLowWng1": pm20002maAlmTrscv2TempLowWng1,
       "pm20002maAlmTrscv2TempHighWng1": pm20002maAlmTrscv2TempHighWng1,
       "pm20002maAlmOtherUrg": pm20002maAlmOtherUrg,
       "pm20002maAlmmodFanFail": pm20002maAlmmodFanFail,
       "pm20002maAlmFanFail": pm20002maAlmFanFail,
       "pm20002maAlmFanHighSpeed": pm20002maAlmFanHighSpeed,
       "pm20002maAlmclientQsfpAlarmDdm": pm20002maAlmclientQsfpAlarmDdm,
       "pm20002maAlmTrscv1VccLowAla1": pm20002maAlmTrscv1VccLowAla1,
       "pm20002maAlmTrscv1VccHighAla1": pm20002maAlmTrscv1VccHighAla1,
       "pm20002maAlmTrscv1TempLowAla1": pm20002maAlmTrscv1TempLowAla1,
       "pm20002maAlmTrscv1TempHighAla": pm20002maAlmTrscv1TempHighAla,
       "pm20002maAlmTrscv2VccLowAla1": pm20002maAlmTrscv2VccLowAla1,
       "pm20002maAlmTrscv2VccHighAla1": pm20002maAlmTrscv2VccHighAla1,
       "pm20002maAlmTrscv2TempLowAla1": pm20002maAlmTrscv2TempLowAla1,
       "pm20002maAlmTrscv2TempHighAla1": pm20002maAlmTrscv2TempHighAla1,
       "pm20002maAlmOtherCrit": pm20002maAlmOtherCrit,
       "pm20002maAlmsynthAlm0": pm20002maAlmsynthAlm0,
       "pm20002maAlmFailFan": pm20002maAlmFailFan,
       "pm20002maAlmModGlobFail": pm20002maAlmModGlobFail,
       "pm20002maAlmDefFuseA": pm20002maAlmDefFuseA,
       "pm20002maAlmDefFuseB": pm20002maAlmDefFuseB,
       "pm20002maAlmclientModuleState": pm20002maAlmclientModuleState,
       "pm20002maAlmCfpInitialize": pm20002maAlmCfpInitialize,
       "pm20002maAlmCfpLowPower": pm20002maAlmCfpLowPower,
       "pm20002maAlmCfpHighPowerUp": pm20002maAlmCfpHighPowerUp,
       "pm20002maAlmCfpTxOff": pm20002maAlmCfpTxOff,
       "pm20002maAlmCfpTxTurnOn": pm20002maAlmCfpTxTurnOn,
       "pm20002maAlmCfpReady": pm20002maAlmCfpReady,
       "pm20002maAlmCfpFault": pm20002maAlmCfpFault,
       "pm20002maAlmCfpTxTurnOff": pm20002maAlmCfpTxTurnOff,
       "pm20002maAlmCfpHighPowerDown": pm20002maAlmCfpHighPowerDown,
       "pm20002maAlmclientModuleGeneralStatus": pm20002maAlmclientModuleGeneralStatus,
       "pm20002maAlmCfpOutOfAlignment": pm20002maAlmCfpOutOfAlignment,
       "pm20002maAlmCfpRxNetworkLol": pm20002maAlmCfpRxNetworkLol,
       "pm20002maAlmCfpRxLos": pm20002maAlmCfpRxLos,
       "pm20002maAlmCfpTxHostLol": pm20002maAlmCfpTxHostLol,
       "pm20002maAlmCfpTxLosf": pm20002maAlmCfpTxLosf,
       "pm20002maAlmCfpTxCmuLol": pm20002maAlmCfpTxCmuLol,
       "pm20002maAlmCfpTxJitterPllLol": pm20002maAlmCfpTxJitterPllLol,
       "pm20002maAlmCfpLossOfRefclk": pm20002maAlmCfpLossOfRefclk,
       "pm20002maAlmCfpHwInterlock": pm20002maAlmCfpHwInterlock,
       "pm20002maAlmclientGlobalAlarmSummary": pm20002maAlmclientGlobalAlarmSummary,
       "pm20002maAlmCfpSoftGlobAlarmTest": pm20002maAlmCfpSoftGlobAlarmTest,
       "pm20002maAlmCfpNetworkLaneAlarmWarning2": pm20002maAlmCfpNetworkLaneAlarmWarning2,
       "pm20002maAlmCfpModuleState": pm20002maAlmCfpModuleState,
       "pm20002maAlmCfpModuleGeneralStatus": pm20002maAlmCfpModuleGeneralStatus,
       "pm20002maAlmCfpModuleFault": pm20002maAlmCfpModuleFault,
       "pm20002maAlmCfpModuleAlarmWarning1": pm20002maAlmCfpModuleAlarmWarning1,
       "pm20002maAlmCfpModuleAlarmWarning2": pm20002maAlmCfpModuleAlarmWarning2,
       "pm20002maAlmCfpNetworkLaneAlarmWarning1": pm20002maAlmCfpNetworkLaneAlarmWarning1,
       "pm20002maAlmCfpNetworkLaneFaultStatus": pm20002maAlmCfpNetworkLaneFaultStatus,
       "pm20002maAlmCfpHostLaneFaultStatus": pm20002maAlmCfpHostLaneFaultStatus,
       "pm20002maAlmCfpGlobAlarmAssertion": pm20002maAlmCfpGlobAlarmAssertion,
       "pm20002maAlmmsaModuleState": pm20002maAlmmsaModuleState,
       "pm20002maAlmMsaInitialize": pm20002maAlmMsaInitialize,
       "pm20002maAlmMsaLowPower": pm20002maAlmMsaLowPower,
       "pm20002maAlmMsaHighPowerUp": pm20002maAlmMsaHighPowerUp,
       "pm20002maAlmMsaTxOff": pm20002maAlmMsaTxOff,
       "pm20002maAlmMsaTxTurnOn": pm20002maAlmMsaTxTurnOn,
       "pm20002maAlmMsaReady": pm20002maAlmMsaReady,
       "pm20002maAlmMsaFault": pm20002maAlmMsaFault,
       "pm20002maAlmMsaTxTurnOff": pm20002maAlmMsaTxTurnOff,
       "pm20002maAlmMsaHighPowerDown": pm20002maAlmMsaHighPowerDown,
       "pm20002maAlmmsaModuleGeneralStatus": pm20002maAlmmsaModuleGeneralStatus,
       "pm20002maAlmMsaOutOfAlignment": pm20002maAlmMsaOutOfAlignment,
       "pm20002maAlmMsaRxNetworkLol": pm20002maAlmMsaRxNetworkLol,
       "pm20002maAlmMsaRxLos": pm20002maAlmMsaRxLos,
       "pm20002maAlmMsaTxHostLol": pm20002maAlmMsaTxHostLol,
       "pm20002maAlmMsaTxLosf": pm20002maAlmMsaTxLosf,
       "pm20002maAlmMsaTxCmuLol": pm20002maAlmMsaTxCmuLol,
       "pm20002maAlmMsaTxJitterPllLol": pm20002maAlmMsaTxJitterPllLol,
       "pm20002maAlmMsaLossOfRefclk": pm20002maAlmMsaLossOfRefclk,
       "pm20002maAlmMsaHwInterlock": pm20002maAlmMsaHwInterlock,
       "pm20002maAlmmsaGlobalAlarmSummary": pm20002maAlmmsaGlobalAlarmSummary,
       "pm20002maAlmMsaSoftGlobAlarmTest": pm20002maAlmMsaSoftGlobAlarmTest,
       "pm20002maAlmMsaNetworkHostAlarmStatus": pm20002maAlmMsaNetworkHostAlarmStatus,
       "pm20002maAlmMsaNetworkLaneAlarmWarning2": pm20002maAlmMsaNetworkLaneAlarmWarning2,
       "pm20002maAlmMsaModuleState": pm20002maAlmMsaModuleState,
       "pm20002maAlmMsaModuleGeneralStatus": pm20002maAlmMsaModuleGeneralStatus,
       "pm20002maAlmModuleFault": pm20002maAlmModuleFault,
       "pm20002maAlmMsaModuleAlarmWarning1": pm20002maAlmMsaModuleAlarmWarning1,
       "pm20002maAlmMsaModuleAlarmWarning2": pm20002maAlmMsaModuleAlarmWarning2,
       "pm20002maAlmMsaNetworkLaneAlarmWarning1": pm20002maAlmMsaNetworkLaneAlarmWarning1,
       "pm20002maAlmMsaNetworkLaneFaultStatus": pm20002maAlmMsaNetworkLaneFaultStatus,
       "pm20002maAlmMsaHostLaneFaultStatus": pm20002maAlmMsaHostLaneFaultStatus,
       "pm20002maAlmMsaGlobAlarmAssertion": pm20002maAlmMsaGlobAlarmAssertion,
       "pm20002maAlmmsaNetworkTxAlignment": pm20002maAlmmsaNetworkTxAlignment,
       "pm20002maAlmNetTxTimingFault": pm20002maAlmNetTxTimingFault,
       "pm20002maAlmNetTxReferenceClockFault": pm20002maAlmNetTxReferenceClockFault,
       "pm20002maAlmNetTxCmuLockFault": pm20002maAlmNetTxCmuLockFault,
       "pm20002maAlmNetTxOutOfAlignment": pm20002maAlmNetTxOutOfAlignment,
       "pm20002maAlmNetTxLossOfAlignment": pm20002maAlmNetTxLossOfAlignment,
       "pm20002maAlmmsaNetworkRxAlignment": pm20002maAlmmsaNetworkRxAlignment,
       "pm20002maAlmNetRxTimingFault": pm20002maAlmNetRxTimingFault,
       "pm20002maAlmNetRxOutOfAlignment": pm20002maAlmNetRxOutOfAlignment,
       "pm20002maAlmNetRxLossOfAlignment": pm20002maAlmNetRxLossOfAlignment,
       "pm20002maAlmNetRxModemLockFault": pm20002maAlmNetRxModemLockFault,
       "pm20002maAlmNetRxModemSyncDetectFault": pm20002maAlmNetRxModemSyncDetectFault,
       "pm20002maAlmmsaNetworkHostNetworkAlarmSummary": pm20002maAlmmsaNetworkHostNetworkAlarmSummary,
       "pm20002maAlmNetworkTxAlignment": pm20002maAlmNetworkTxAlignment,
       "pm20002maAlmNetworkRxAlignment": pm20002maAlmNetworkRxAlignment,
       "pm20002maAlmNetworkRxOtn": pm20002maAlmNetworkRxOtn,
       "pm20002maAlmHostRxAlignment": pm20002maAlmHostRxAlignment,
       "pm20002maAlmHostTxAlignment": pm20002maAlmHostTxAlignment,
       "pm20002maAlmHostTxOtnStatus": pm20002maAlmHostTxOtnStatus,
       "pm20002maAlmmsaHostTxAlignment": pm20002maAlmmsaHostTxAlignment,
       "pm20002maAlmHostTxDeskewLockFault": pm20002maAlmHostTxDeskewLockFault,
       "pm20002maAlmHostTxOutOfAlignment": pm20002maAlmHostTxOutOfAlignment,
       "pm20002maAlmHostTxLossOfAlignment": pm20002maAlmHostTxLossOfAlignment,
       "pm20002maAlmHostTxCdrLockFault": pm20002maAlmHostTxCdrLockFault,
       "pm20002maAlmmsaHostRxAlignment": pm20002maAlmmsaHostRxAlignment,
       "pm20002maAlmHostRxCmuLockFault": pm20002maAlmHostRxCmuLockFault,
       "pm20002maAlmHostRxOutOfAlignment": pm20002maAlmHostRxOutOfAlignment,
       "pm20002maAlmHostRxLossOfAlignment": pm20002maAlmHostRxLossOfAlignment,
       "pm20002maAlmClient": pm20002maAlmClient,
       "pm20002maAlmClientNurg": pm20002maAlmClientNurg,
       "pm20002maAlmclientSfpWarnDdmTable": pm20002maAlmclientSfpWarnDdmTable,
       "pm20002maAlmclientSfpWarnDdmEntry": pm20002maAlmclientSfpWarnDdmEntry,
       "pm20002maAlmclientSfpWarnDdmIndex": pm20002maAlmclientSfpWarnDdmIndex,
       "pm20002maAlmTxPwLowWngPortn": pm20002maAlmTxPwLowWngPortn,
       "pm20002maAlmTxPwrHighWngPortn": pm20002maAlmTxPwrHighWngPortn,
       "pm20002maAlmTxBiasLowWngPortn": pm20002maAlmTxBiasLowWngPortn,
       "pm20002maAlmTxBiasHighWngPortn": pm20002maAlmTxBiasHighWngPortn,
       "pm20002maAlmRxPwrLowWngPortn": pm20002maAlmRxPwrLowWngPortn,
       "pm20002maAlmRxPwrHighWngPortn": pm20002maAlmRxPwrHighWngPortn,
       "pm20002maAlmClientUrg": pm20002maAlmClientUrg,
       "pm20002maAlmclientHostLaneFaultTable": pm20002maAlmclientHostLaneFaultTable,
       "pm20002maAlmclientHostLaneFaultEntry": pm20002maAlmclientHostLaneFaultEntry,
       "pm20002maAlmclientHostLaneFaultIndex": pm20002maAlmclientHostLaneFaultIndex,
       "pm20002maAlmClientLossOfSyncPortn": pm20002maAlmClientLossOfSyncPortn,
       "pm20002maAlmClientInputLossOfSigPortn": pm20002maAlmClientInputLossOfSigPortn,
       "pm20002maAlmClientLanesMarkerUnlockPortn": pm20002maAlmClientLanesMarkerUnlockPortn,
       "pm20002maAlmClientLanes6466UnlockPortn": pm20002maAlmClientLanes6466UnlockPortn,
       "pm20002maAlmClientLanesNotAlignedPortn": pm20002maAlmClientLanesNotAlignedPortn,
       "pm20002maAlmClientCsfDetectedPortn": pm20002maAlmClientCsfDetectedPortn,
       "pm20002maAlmClientTxHostLolPortn": pm20002maAlmClientTxHostLolPortn,
       "pm20002maAlmClientLaneTxFifoErrorPortn": pm20002maAlmClientLaneTxFifoErrorPortn,
       "pm20002maAlmclientSfpAlmDdmTable": pm20002maAlmclientSfpAlmDdmTable,
       "pm20002maAlmclientSfpAlmDdmEntry": pm20002maAlmclientSfpAlmDdmEntry,
       "pm20002maAlmclientSfpAlmDdmIndex": pm20002maAlmclientSfpAlmDdmIndex,
       "pm20002maAlmTxPwrLowAlaPortn": pm20002maAlmTxPwrLowAlaPortn,
       "pm20002maAlmTxPwrHighAlaPortn": pm20002maAlmTxPwrHighAlaPortn,
       "pm20002maAlmTxBiasLowAlaPortn": pm20002maAlmTxBiasLowAlaPortn,
       "pm20002maAlmTxBiasHighAlaPortn": pm20002maAlmTxBiasHighAlaPortn,
       "pm20002maAlmRxPwrLowAlaPortn": pm20002maAlmRxPwrLowAlaPortn,
       "pm20002maAlmRxPwrHighAlaPortn": pm20002maAlmRxPwrHighAlaPortn,
       "pm20002maAlmClientCrit": pm20002maAlmClientCrit,
       "pm20002maAlmsynthAlmPortTable": pm20002maAlmsynthAlmPortTable,
       "pm20002maAlmsynthAlmPortEntry": pm20002maAlmsynthAlmPortEntry,
       "pm20002maAlmsynthAlmPortIndex": pm20002maAlmsynthAlmPortIndex,
       "pm20002maAlmSfpAbsentPortn": pm20002maAlmSfpAbsentPortn,
       "pm20002maAlmDdmAbsentPortn": pm20002maAlmDdmAbsentPortn,
       "pm20002maAlmHwFailAccPortn": pm20002maAlmHwFailAccPortn,
       "pm20002maAlmDwLsdPortn": pm20002maAlmDwLsdPortn,
       "pm20002maAlmClientLocalOosPortn": pm20002maAlmClientLocalOosPortn,
       "pm20002maAlmClientRemoteOosPortn": pm20002maAlmClientRemoteOosPortn,
       "pm20002maAlmDwCaisPortn": pm20002maAlmDwCaisPortn,
       "pm20002maAlmSfpDdmWarningPortn": pm20002maAlmSfpDdmWarningPortn,
       "pm20002maAlmSfpDdmAlmPortn": pm20002maAlmSfpDdmAlmPortn,
       "pm20002maAlmFailAccPortn": pm20002maAlmFailAccPortn,
       "pm20002maAlmUpCsfPortn": pm20002maAlmUpCsfPortn,
       "pm20002maAlmLine": pm20002maAlmLine,
       "pm20002maAlmLineNurg": pm20002maAlmLineNurg,
       "pm20002maAlmlineNetworkLaneAlarmWarning1Table": pm20002maAlmlineNetworkLaneAlarmWarning1Table,
       "pm20002maAlmlineNetworkLaneAlarmWarning1Entry": pm20002maAlmlineNetworkLaneAlarmWarning1Entry,
       "pm20002maAlmlineNetworkLaneAlarmWarning1Index": pm20002maAlmlineNetworkLaneAlarmWarning1Index,
       "pm20002maAlmLineRxPowerLowAlarmPortn": pm20002maAlmLineRxPowerLowAlarmPortn,
       "pm20002maAlmLineRxPowerLowWarningPortn": pm20002maAlmLineRxPowerLowWarningPortn,
       "pm20002maAlmLineRxPowerHighWarningPortn": pm20002maAlmLineRxPowerHighWarningPortn,
       "pm20002maAlmLineRxPowerHighAlarmPortn": pm20002maAlmLineRxPowerHighAlarmPortn,
       "pm20002maAlmLineLaserTempLowAlarmPortn": pm20002maAlmLineLaserTempLowAlarmPortn,
       "pm20002maAlmLineLaserTempLowWarningPortn": pm20002maAlmLineLaserTempLowWarningPortn,
       "pm20002maAlmLineLaserTempHighWarningPortn": pm20002maAlmLineLaserTempHighWarningPortn,
       "pm20002maAlmLineLaserTempHighAlarmPortn": pm20002maAlmLineLaserTempHighAlarmPortn,
       "pm20002maAlmLineTxPowerLowAlarmPortn": pm20002maAlmLineTxPowerLowAlarmPortn,
       "pm20002maAlmLineTxPowerLowWarningPortn": pm20002maAlmLineTxPowerLowWarningPortn,
       "pm20002maAlmLineTxPowerHighWarningPortn": pm20002maAlmLineTxPowerHighWarningPortn,
       "pm20002maAlmLineTxPowerHighAlarmPortn": pm20002maAlmLineTxPowerHighAlarmPortn,
       "pm20002maAlmLineBiasLowAlarmPortn": pm20002maAlmLineBiasLowAlarmPortn,
       "pm20002maAlmLineBiasLowWarningPortn": pm20002maAlmLineBiasLowWarningPortn,
       "pm20002maAlmLineBiasHighWarningPortn": pm20002maAlmLineBiasHighWarningPortn,
       "pm20002maAlmLineBiasHighAlarmPortn": pm20002maAlmLineBiasHighAlarmPortn,
       "pm20002maAlmlineNetworkLaneAlarmWarning2Table": pm20002maAlmlineNetworkLaneAlarmWarning2Table,
       "pm20002maAlmlineNetworkLaneAlarmWarning2Entry": pm20002maAlmlineNetworkLaneAlarmWarning2Entry,
       "pm20002maAlmlineNetworkLaneAlarmWarning2Index": pm20002maAlmlineNetworkLaneAlarmWarning2Index,
       "pm20002maAlmTxModulatorBiasLowAlarmPortn": pm20002maAlmTxModulatorBiasLowAlarmPortn,
       "pm20002maAlmTxModulatorBiasLowWarningPortn": pm20002maAlmTxModulatorBiasLowWarningPortn,
       "pm20002maAlmTxModulatorBiasHighWarningPortn": pm20002maAlmTxModulatorBiasHighWarningPortn,
       "pm20002maAlmTxModulatorBiasHighAlarmPortn": pm20002maAlmTxModulatorBiasHighAlarmPortn,
       "pm20002maAlmRxLaserTempLowAlarmPortn": pm20002maAlmRxLaserTempLowAlarmPortn,
       "pm20002maAlmRxLaserTempLowWarningPortn": pm20002maAlmRxLaserTempLowWarningPortn,
       "pm20002maAlmRxLaserTempHighWarningPortn": pm20002maAlmRxLaserTempHighWarningPortn,
       "pm20002maAlmRxLaserTempHighAlarmPortn": pm20002maAlmRxLaserTempHighAlarmPortn,
       "pm20002maAlmRxLaserOutputLowAlarmPortn": pm20002maAlmRxLaserOutputLowAlarmPortn,
       "pm20002maAlmRxLaserOutputLowWarningPortn": pm20002maAlmRxLaserOutputLowWarningPortn,
       "pm20002maAlmRxLaserOutputHighWarningPortn": pm20002maAlmRxLaserOutputHighWarningPortn,
       "pm20002maAlmRxLaserOutputHighAlarmPortn": pm20002maAlmRxLaserOutputHighAlarmPortn,
       "pm20002maAlmRxLaserBiasLowAlarmPortn": pm20002maAlmRxLaserBiasLowAlarmPortn,
       "pm20002maAlmRxLaserBiasLowWarningPortn": pm20002maAlmRxLaserBiasLowWarningPortn,
       "pm20002maAlmRxLaserBiasHighWarningPortn": pm20002maAlmRxLaserBiasHighWarningPortn,
       "pm20002maAlmRxLaserBiasHighAlarmPortn": pm20002maAlmRxLaserBiasHighAlarmPortn,
       "pm20002maAlmLineUrg": pm20002maAlmLineUrg,
       "pm20002maAlmlineNetworkLaneFaultTable": pm20002maAlmlineNetworkLaneFaultTable,
       "pm20002maAlmlineNetworkLaneFaultEntry": pm20002maAlmlineNetworkLaneFaultEntry,
       "pm20002maAlmlineNetworkLaneFaultIndex": pm20002maAlmlineNetworkLaneFaultIndex,
       "pm20002maAlmLineLaneRxTecFaultPortn": pm20002maAlmLineLaneRxTecFaultPortn,
       "pm20002maAlmLineLaneRxFifoErrorPortn": pm20002maAlmLineLaneRxFifoErrorPortn,
       "pm20002maAlmLineLaneRxLolPortn": pm20002maAlmLineLaneRxLolPortn,
       "pm20002maAlmLineLaneRxLosPortn": pm20002maAlmLineLaneRxLosPortn,
       "pm20002maAlmLineLaneTxLolPortn": pm20002maAlmLineLaneTxLolPortn,
       "pm20002maAlmLineLaneTxLosfPortn": pm20002maAlmLineLaneTxLosfPortn,
       "pm20002maAlmLineLaneApdPowerSupplyPortn": pm20002maAlmLineLaneApdPowerSupplyPortn,
       "pm20002maAlmLineLaneWavelengthUnlockedPortn": pm20002maAlmLineLaneWavelengthUnlockedPortn,
       "pm20002maAlmLineLaneTecFaultPortn": pm20002maAlmLineLaneTecFaultPortn,
       "pm20002maAlmlineHostLaneFaultTable": pm20002maAlmlineHostLaneFaultTable,
       "pm20002maAlmlineHostLaneFaultEntry": pm20002maAlmlineHostLaneFaultEntry,
       "pm20002maAlmlineHostLaneFaultIndex": pm20002maAlmlineHostLaneFaultIndex,
       "pm20002maAlmLineInputLossOfSignalPortn": pm20002maAlmLineInputLossOfSignalPortn,
       "pm20002maAlmLineLossOfFramePortn": pm20002maAlmLineLossOfFramePortn,
       "pm20002maAlmLineSmBdiInsertedPortn": pm20002maAlmLineSmBdiInsertedPortn,
       "pm20002maAlmLineSmBdiDetectedPortn": pm20002maAlmLineSmBdiDetectedPortn,
       "pm20002maAlmLineSmIaeInsertedPortn": pm20002maAlmLineSmIaeInsertedPortn,
       "pm20002maAlmLineSmIaeDetectedPortn": pm20002maAlmLineSmIaeDetectedPortn,
       "pm20002maAlmLineTxHostLolPortn": pm20002maAlmLineTxHostLolPortn,
       "pm20002maAlmLineLaneTxFifoErrorPortn": pm20002maAlmLineLaneTxFifoErrorPortn,
       "pm20002maAlmlineNetworkLaneRxOtnTable": pm20002maAlmlineNetworkLaneRxOtnTable,
       "pm20002maAlmlineNetworkLaneRxOtnEntry": pm20002maAlmlineNetworkLaneRxOtnEntry,
       "pm20002maAlmlineNetworkLaneRxOtnIndex": pm20002maAlmlineNetworkLaneRxOtnIndex,
       "pm20002maAlmLineRxOtnOduAisPortn": pm20002maAlmLineRxOtnOduAisPortn,
       "pm20002maAlmLineRxOtnOtuAisPortn": pm20002maAlmLineRxOtnOtuAisPortn,
       "pm20002maAlmLineRxSmBdiPortn": pm20002maAlmLineRxSmBdiPortn,
       "pm20002maAlmLineRxOtnIaePortn": pm20002maAlmLineRxOtnIaePortn,
       "pm20002maAlmLineRxOtnOomPortn": pm20002maAlmLineRxOtnOomPortn,
       "pm20002maAlmLineRxOtnLomPortn": pm20002maAlmLineRxOtnLomPortn,
       "pm20002maAlmLineRxOtnOofPortn": pm20002maAlmLineRxOtnOofPortn,
       "pm20002maAlmLineRxOtnLofPortn": pm20002maAlmLineRxOtnLofPortn,
       "pm20002maAlmlineHostLaneTxOtnTable": pm20002maAlmlineHostLaneTxOtnTable,
       "pm20002maAlmlineHostLaneTxOtnEntry": pm20002maAlmlineHostLaneTxOtnEntry,
       "pm20002maAlmlineHostLaneTxOtnIndex": pm20002maAlmlineHostLaneTxOtnIndex,
       "pm20002maAlmLineTxOtnOduAisPortn": pm20002maAlmLineTxOtnOduAisPortn,
       "pm20002maAlmLineTxOtnOtuAisPortn": pm20002maAlmLineTxOtnOtuAisPortn,
       "pm20002maAlmLineTxSmBdiPortn": pm20002maAlmLineTxSmBdiPortn,
       "pm20002maAlmLineTxOtnIaePortn": pm20002maAlmLineTxOtnIaePortn,
       "pm20002maAlmLineTxOtnOomPortn": pm20002maAlmLineTxOtnOomPortn,
       "pm20002maAlmLineTxOtnLomPortn": pm20002maAlmLineTxOtnLomPortn,
       "pm20002maAlmLineTxOtnOofPortn": pm20002maAlmLineTxOtnOofPortn,
       "pm20002maAlmLineTxOtnLofPortn": pm20002maAlmLineTxOtnLofPortn,
       "pm20002maAlmLineCrit": pm20002maAlmLineCrit,
       "pm20002maAlmsynthAlmLineTable": pm20002maAlmsynthAlmLineTable,
       "pm20002maAlmsynthAlmLineEntry": pm20002maAlmsynthAlmLineEntry,
       "pm20002maAlmsynthAlmLineIndex": pm20002maAlmsynthAlmLineIndex,
       "pm20002maAlmXfpAbsentPortn": pm20002maAlmXfpAbsentPortn,
       "pm20002maAlmXfpInitNotComplPortn": pm20002maAlmXfpInitNotComplPortn,
       "pm20002maAlmLineHwFailPortn": pm20002maAlmLineHwFailPortn,
       "pm20002maAlmXfpTxOffPortn": pm20002maAlmXfpTxOffPortn,
       "pm20002maAlmLineLocalOosPortn": pm20002maAlmLineLocalOosPortn,
       "pm20002maAlmUpRdiInsPortn": pm20002maAlmUpRdiInsPortn,
       "pm20002maAlmLineDdmWarningPortn": pm20002maAlmLineDdmWarningPortn,
       "pm20002maAlmLineDdmAlmPortn": pm20002maAlmLineDdmAlmPortn,
       "pm20002maAlmLineFailPortn": pm20002maAlmLineFailPortn,
       "pm20002maAlmLineActivePortn": pm20002maAlmLineActivePortn,
       "pm20002mameasures": pm20002mameasures,
       "pm20002maMesrOther": pm20002maMesrOther,
       "pm20002maMesrsynth0": pm20002maMesrsynth0,
       "pm20002maMesrsynth1": pm20002maMesrsynth1,
       "pm20002maMesrpmIntervalNumber": pm20002maMesrpmIntervalNumber,
       "pm20002maMesrlineNetTxLaserOutputPwrAverage": pm20002maMesrlineNetTxLaserOutputPwrAverage,
       "pm20002maMesrlineNetTxLaserTempAverage": pm20002maMesrlineNetTxLaserTempAverage,
       "pm20002maMesrlineNetTxBiasCurrentAverage": pm20002maMesrlineNetTxBiasCurrentAverage,
       "pm20002maMesrlineNetRxInputPwrAverage": pm20002maMesrlineNetRxInputPwrAverage,
       "pm20002maMesrlineResidualChromaticDispAverage": pm20002maMesrlineResidualChromaticDispAverage,
       "pm20002maMesrlineDiffGroupDelayAverage": pm20002maMesrlineDiffGroupDelayAverage,
       "pm20002maMesrlineQFactorAverage": pm20002maMesrlineQFactorAverage,
       "pm20002maMesrlineCarrierFreqOffsetAverage": pm20002maMesrlineCarrierFreqOffsetAverage,
       "pm20002maMesrlineOsnrAverage": pm20002maMesrlineOsnrAverage,
       "pm20002maMesrlineNetTxLaserOutputPwrMin": pm20002maMesrlineNetTxLaserOutputPwrMin,
       "pm20002maMesrlineNetTxLaserTempMin": pm20002maMesrlineNetTxLaserTempMin,
       "pm20002maMesrlineNetTxBiasCurrentMin": pm20002maMesrlineNetTxBiasCurrentMin,
       "pm20002maMesrlineNetRxInputPwrMin": pm20002maMesrlineNetRxInputPwrMin,
       "pm20002maMesrlineResidualChromaticDispMin": pm20002maMesrlineResidualChromaticDispMin,
       "pm20002maMesrlineDiffGroupDelayMin": pm20002maMesrlineDiffGroupDelayMin,
       "pm20002maMesrlineQFactorMin": pm20002maMesrlineQFactorMin,
       "pm20002maMesrlineCarrierFreqOffsetMin": pm20002maMesrlineCarrierFreqOffsetMin,
       "pm20002maMesrlineOsnrMin": pm20002maMesrlineOsnrMin,
       "pm20002maMesrlineNetTxLaserOutputPwrMax": pm20002maMesrlineNetTxLaserOutputPwrMax,
       "pm20002maMesrlineNetTxLaserTempMax": pm20002maMesrlineNetTxLaserTempMax,
       "pm20002maMesrlineNetTxBiasCurrentMax": pm20002maMesrlineNetTxBiasCurrentMax,
       "pm20002maMesrlineNetRxInputPwrMax": pm20002maMesrlineNetRxInputPwrMax,
       "pm20002maMesrlineResidualChromaticDispMax": pm20002maMesrlineResidualChromaticDispMax,
       "pm20002maMesrlineDiffGroupDelayMax": pm20002maMesrlineDiffGroupDelayMax,
       "pm20002maMesrlineQFactorMax": pm20002maMesrlineQFactorMax,
       "pm20002maMesrlineCarrierFreqOffsetMax": pm20002maMesrlineCarrierFreqOffsetMax,
       "pm20002maMesrlineOsnrMax": pm20002maMesrlineOsnrMax,
       "pm20002maMesrtrscv1Temp": pm20002maMesrtrscv1Temp,
       "pm20002maMesrtrscv2Temp": pm20002maMesrtrscv2Temp,
       "pm20002maMesrtrscv1PowerSupply": pm20002maMesrtrscv1PowerSupply,
       "pm20002maMesrtrscv2PowerSupply": pm20002maMesrtrscv2PowerSupply,
       "pm20002maMesrClient": pm20002maMesrClient,
       "pm20002maMesrclientCfpTemp": pm20002maMesrclientCfpTemp,
       "pm20002maMesrclientCfp3v3Voltage": pm20002maMesrclientCfp3v3Voltage,
       "pm20002maMesrclientSoaBiasCurrent": pm20002maMesrclientSoaBiasCurrent,
       "pm20002maMesrclientTxPwrMinTable": pm20002maMesrclientTxPwrMinTable,
       "pm20002maMesrclientTxPwrMinEntry": pm20002maMesrclientTxPwrMinEntry,
       "pm20002maMesrclientTxPwrMinIndex": pm20002maMesrclientTxPwrMinIndex,
       "pm20002maMesrclientTxPwrMinPortn": pm20002maMesrclientTxPwrMinPortn,
       "pm20002maMesrclientRxPwrMinTable": pm20002maMesrclientRxPwrMinTable,
       "pm20002maMesrclientRxPwrMinEntry": pm20002maMesrclientRxPwrMinEntry,
       "pm20002maMesrclientRxPwrMinIndex": pm20002maMesrclientRxPwrMinIndex,
       "pm20002maMesrclientRxPwrMinPortn": pm20002maMesrclientRxPwrMinPortn,
       "pm20002maMesrclientTxPwrMaxTable": pm20002maMesrclientTxPwrMaxTable,
       "pm20002maMesrclientTxPwrMaxEntry": pm20002maMesrclientTxPwrMaxEntry,
       "pm20002maMesrclientTxPwrMaxIndex": pm20002maMesrclientTxPwrMaxIndex,
       "pm20002maMesrclientTxPwrMaxPortn": pm20002maMesrclientTxPwrMaxPortn,
       "pm20002maMesrclientRxPwrMaxTable": pm20002maMesrclientRxPwrMaxTable,
       "pm20002maMesrclientRxPwrMaxEntry": pm20002maMesrclientRxPwrMaxEntry,
       "pm20002maMesrclientRxPwrMaxIndex": pm20002maMesrclientRxPwrMaxIndex,
       "pm20002maMesrclientRxPwrMaxPortn": pm20002maMesrclientRxPwrMaxPortn,
       "pm20002maMesrLine": pm20002maMesrLine,
       "pm20002maMesrlineMsaTemp": pm20002maMesrlineMsaTemp,
       "pm20002maMesrlineMsa3v3Voltage": pm20002maMesrlineMsa3v3Voltage,
       "pm20002maMesrlineSoaBiasCurrent": pm20002maMesrlineSoaBiasCurrent,
       "pm20002maMesrlineNetTxLaserOutputPwrTable": pm20002maMesrlineNetTxLaserOutputPwrTable,
       "pm20002maMesrlineNetTxLaserOutputPwrEntry": pm20002maMesrlineNetTxLaserOutputPwrEntry,
       "pm20002maMesrlineNetTxLaserOutputPwrIndex": pm20002maMesrlineNetTxLaserOutputPwrIndex,
       "pm20002maMesrlineNetTxLaserOutputPwrPortn": pm20002maMesrlineNetTxLaserOutputPwrPortn,
       "pm20002maMesrlineNetTxLaserTempTable": pm20002maMesrlineNetTxLaserTempTable,
       "pm20002maMesrlineNetTxLaserTempEntry": pm20002maMesrlineNetTxLaserTempEntry,
       "pm20002maMesrlineNetTxLaserTempIndex": pm20002maMesrlineNetTxLaserTempIndex,
       "pm20002maMesrlineNetTxLaserTempPortn": pm20002maMesrlineNetTxLaserTempPortn,
       "pm20002maMesrlineNetTxBiasCurrentTable": pm20002maMesrlineNetTxBiasCurrentTable,
       "pm20002maMesrlineNetTxBiasCurrentEntry": pm20002maMesrlineNetTxBiasCurrentEntry,
       "pm20002maMesrlineNetTxBiasCurrentIndex": pm20002maMesrlineNetTxBiasCurrentIndex,
       "pm20002maMesrlineNetTxBiasCurrentPortn": pm20002maMesrlineNetTxBiasCurrentPortn,
       "pm20002maMesrlineNetRxInputPwrTable": pm20002maMesrlineNetRxInputPwrTable,
       "pm20002maMesrlineNetRxInputPwrEntry": pm20002maMesrlineNetRxInputPwrEntry,
       "pm20002maMesrlineNetRxInputPwrIndex": pm20002maMesrlineNetRxInputPwrIndex,
       "pm20002maMesrlineNetRxInputPwrPortn": pm20002maMesrlineNetRxInputPwrPortn,
       "pm20002maMesrlineResidualChromaticDispTable": pm20002maMesrlineResidualChromaticDispTable,
       "pm20002maMesrlineResidualChromaticDispEntry": pm20002maMesrlineResidualChromaticDispEntry,
       "pm20002maMesrlineResidualChromaticDispIndex": pm20002maMesrlineResidualChromaticDispIndex,
       "pm20002maMesrlineResidualChromaticDispPortn": pm20002maMesrlineResidualChromaticDispPortn,
       "pm20002maMesrlineDiffGroupDelayTable": pm20002maMesrlineDiffGroupDelayTable,
       "pm20002maMesrlineDiffGroupDelayEntry": pm20002maMesrlineDiffGroupDelayEntry,
       "pm20002maMesrlineDiffGroupDelayIndex": pm20002maMesrlineDiffGroupDelayIndex,
       "pm20002maMesrlineDiffGroupDelayPortn": pm20002maMesrlineDiffGroupDelayPortn,
       "pm20002maMesrlineQFactorTable": pm20002maMesrlineQFactorTable,
       "pm20002maMesrlineQFactorEntry": pm20002maMesrlineQFactorEntry,
       "pm20002maMesrlineQFactorIndex": pm20002maMesrlineQFactorIndex,
       "pm20002maMesrlineQFactorPortn": pm20002maMesrlineQFactorPortn,
       "pm20002maMesrlineCarrierFreqOffsetTable": pm20002maMesrlineCarrierFreqOffsetTable,
       "pm20002maMesrlineCarrierFreqOffsetEntry": pm20002maMesrlineCarrierFreqOffsetEntry,
       "pm20002maMesrlineCarrierFreqOffsetIndex": pm20002maMesrlineCarrierFreqOffsetIndex,
       "pm20002maMesrlineCarrierFreqOffsetPortn": pm20002maMesrlineCarrierFreqOffsetPortn,
       "pm20002maMesrlineOsnrTable": pm20002maMesrlineOsnrTable,
       "pm20002maMesrlineOsnrEntry": pm20002maMesrlineOsnrEntry,
       "pm20002maMesrlineOsnrIndex": pm20002maMesrlineOsnrIndex,
       "pm20002maMesrlineOsnrPortn": pm20002maMesrlineOsnrPortn,
       "pm20002macounters": pm20002macounters,
       "pm20002maCntOther": pm20002maCntOther,
       "pm20002maCntClient": pm20002maCntClient,
       "pm20002maCntclientInputErrorCounterTable": pm20002maCntclientInputErrorCounterTable,
       "pm20002maCntclientInputErrorCounterEntry": pm20002maCntclientInputErrorCounterEntry,
       "pm20002maCntclientInputErrorCounterIndex": pm20002maCntclientInputErrorCounterIndex,
       "pm20002maCntclientInputErrorCounterValuePortn": pm20002maCntclientInputErrorCounterValuePortn,
       "pm20002maCntclientInputErrorCounterErrorPortn": pm20002maCntclientInputErrorCounterErrorPortn,
       "pm20002maCntclientInputErrorCounterOverloadPortn": pm20002maCntclientInputErrorCounterOverloadPortn,
       "pm20002maCntclientCbipCounterTable": pm20002maCntclientCbipCounterTable,
       "pm20002maCntclientCbipCounterEntry": pm20002maCntclientCbipCounterEntry,
       "pm20002maCntclientCbipCounterIndex": pm20002maCntclientCbipCounterIndex,
       "pm20002maCntclientCbipCounterValuePortn": pm20002maCntclientCbipCounterValuePortn,
       "pm20002maCntclientCbipCounterErrorPortn": pm20002maCntclientCbipCounterErrorPortn,
       "pm20002maCntclientCbipCounterOverloadPortn": pm20002maCntclientCbipCounterOverloadPortn,
       "pm20002maCntLine": pm20002maCntLine,
       "pm20002maCntlocalLineSmBip8ErrorCounterTable": pm20002maCntlocalLineSmBip8ErrorCounterTable,
       "pm20002maCntlocalLineSmBip8ErrorCounterEntry": pm20002maCntlocalLineSmBip8ErrorCounterEntry,
       "pm20002maCntlocalLineSmBip8ErrorCounterIndex": pm20002maCntlocalLineSmBip8ErrorCounterIndex,
       "pm20002maCntlocalLineSmBip8ErrorCounterValuePortn": pm20002maCntlocalLineSmBip8ErrorCounterValuePortn,
       "pm20002maCntlocalLineSmBip8ErrorCounterErrorPortn": pm20002maCntlocalLineSmBip8ErrorCounterErrorPortn,
       "pm20002maCntlocalLineSmBip8ErrorCounterOverloadPortn": pm20002maCntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pm20002maCntlocalLineFecCorrectedErrorsCounterTable": pm20002maCntlocalLineFecCorrectedErrorsCounterTable,
       "pm20002maCntlocalLineFecCorrectedErrorsCounterEntry": pm20002maCntlocalLineFecCorrectedErrorsCounterEntry,
       "pm20002maCntlocalLineFecCorrectedErrorsCounterIndex": pm20002maCntlocalLineFecCorrectedErrorsCounterIndex,
       "pm20002maCntlocalLineFecCorrectedErrorsCounterValuePortn": pm20002maCntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pm20002maCntlocalLineFecCorrectedErrorsCounterErrorPortn": pm20002maCntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pm20002maCntlocalLineFecCorrectedErrorsCounterOverloadPortn": pm20002maCntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pm20002maCntremoteLineSmBip8ErrorCounterTable": pm20002maCntremoteLineSmBip8ErrorCounterTable,
       "pm20002maCntremoteLineSmBip8ErrorCounterEntry": pm20002maCntremoteLineSmBip8ErrorCounterEntry,
       "pm20002maCntremoteLineSmBip8ErrorCounterIndex": pm20002maCntremoteLineSmBip8ErrorCounterIndex,
       "pm20002maCntremoteLineSmBip8ErrorCounterValuePortn": pm20002maCntremoteLineSmBip8ErrorCounterValuePortn,
       "pm20002maCntremoteLineSmBip8ErrorCounterErrorPortn": pm20002maCntremoteLineSmBip8ErrorCounterErrorPortn,
       "pm20002maCntremoteLineSmBip8ErrorCounterOverloadPortn": pm20002maCntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pm20002maCntlineDfrmTimCntTable": pm20002maCntlineDfrmTimCntTable,
       "pm20002maCntlineDfrmTimCntEntry": pm20002maCntlineDfrmTimCntEntry,
       "pm20002maCntlineDfrmTimCntIndex": pm20002maCntlineDfrmTimCntIndex,
       "pm20002maCntlineDfrmTimCntValuePortn": pm20002maCntlineDfrmTimCntValuePortn,
       "pm20002maCntlineDfrmTimCntErrorPortn": pm20002maCntlineDfrmTimCntErrorPortn,
       "pm20002maCntlineDfrmTimCntOverloadPortn": pm20002maCntlineDfrmTimCntOverloadPortn,
       "pm20002maCntlocalLineTrscvPreSdFecErrorCounterTable": pm20002maCntlocalLineTrscvPreSdFecErrorCounterTable,
       "pm20002maCntlocalLineTrscvPreSdFecErrorCounterEntry": pm20002maCntlocalLineTrscvPreSdFecErrorCounterEntry,
       "pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex": pm20002maCntlocalLineTrscvPreSdFecErrorCounterIndex,
       "pm20002maCntlocalLineTrscvPreSdFecErrorCounterValuePortn": pm20002maCntlocalLineTrscvPreSdFecErrorCounterValuePortn,
       "pm20002maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn": pm20002maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn,
       "pm20002maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn": pm20002maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable": pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry": pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex": pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn": pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn": pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn": pm20002maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn,
       "pm20002maCntlocalLineTrscvPreSdFecBitCounterTable": pm20002maCntlocalLineTrscvPreSdFecBitCounterTable,
       "pm20002maCntlocalLineTrscvPreSdFecBitCounterEntry": pm20002maCntlocalLineTrscvPreSdFecBitCounterEntry,
       "pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex": pm20002maCntlocalLineTrscvPreSdFecBitCounterIndex,
       "pm20002maCntlocalLineTrscvPreSdFecBitCounterValuePortn": pm20002maCntlocalLineTrscvPreSdFecBitCounterValuePortn,
       "pm20002maCntlocalLineTrscvPreSdFecBitCounterErrorPortn": pm20002maCntlocalLineTrscvPreSdFecBitCounterErrorPortn,
       "pm20002maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn": pm20002maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterTable": pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterTable,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry": pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex": pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn": pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn": pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn,
       "pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn": pm20002maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn,
       "pm20002macontrolsWrite": pm20002macontrolsWrite,
       "pm20002maCtrlOther": pm20002maCtrlOther,
       "pm20002maCtrlconfMgnt1": pm20002maCtrlconfMgnt1,
       "pm20002maCtrlConf1Load1": pm20002maCtrlConf1Load1,
       "pm20002maCtrlConf2Load1": pm20002maCtrlConf2Load1,
       "pm20002maCtrlConf2Flash1": pm20002maCtrlConf2Flash1,
       "pm20002maCtrlConf2Clear1": pm20002maCtrlConf2Clear1,
       "pm20002maCtrlsynth4": pm20002maCtrlsynth4,
       "pm20002maCtrlCorrelatOn": pm20002maCtrlCorrelatOn,
       "pm20002maCtrlCorrelatOff": pm20002maCtrlCorrelatOff,
       "pm20002maCtrlswMgnt": pm20002maCtrlswMgnt,
       "pm20002maCtrlColdReset": pm20002maCtrlColdReset,
       "pm20002maCtrlWarmReset": pm20002maCtrlWarmReset,
       "pm20002maCtrlLoadSwBank1": pm20002maCtrlLoadSwBank1,
       "pm20002maCtrlLoadSwBank2": pm20002maCtrlLoadSwBank2,
       "pm20002maCtrlgwMgnt": pm20002maCtrlgwMgnt,
       "pm20002maCtrlCurrentGwReset": pm20002maCtrlCurrentGwReset,
       "pm20002maCtrlLoadGwBank1": pm20002maCtrlLoadGwBank1,
       "pm20002maCtrlLoadGwBank2": pm20002maCtrlLoadGwBank2,
       "pm20002maCtrlLoadGwBank3": pm20002maCtrlLoadGwBank3,
       "pm20002maCtrlLoadGwBank4": pm20002maCtrlLoadGwBank4,
       "pm20002maCtrlledTest": pm20002maCtrlledTest,
       "pm20002maCtrlGreenLed": pm20002maCtrlGreenLed,
       "pm20002maCtrlRedLed": pm20002maCtrlRedLed,
       "pm20002maCtrlLedOff": pm20002maCtrlLedOff,
       "pm20002maCtrlinitSwitchMarvell": pm20002maCtrlinitSwitchMarvell,
       "pm20002maCtrlInitSwitchMarvell": pm20002maCtrlInitSwitchMarvell,
       "pm20002maCtrlresetCount": pm20002maCtrlresetCount,
       "pm20002maCtrlResetcount": pm20002maCtrlResetcount,
       "pm20002maCtrlresetRmon": pm20002maCtrlresetRmon,
       "pm20002maCtrlResetrmon": pm20002maCtrlResetrmon,
       "pm20002maCtrlresetMeasurements": pm20002maCtrlresetMeasurements,
       "pm20002maCtrlResetmeasurements": pm20002maCtrlResetmeasurements,
       "pm20002maCtrlClient": pm20002maCtrlClient,
       "pm20002maCtrlaccessLoopTable": pm20002maCtrlaccessLoopTable,
       "pm20002maCtrlaccessLoopEntry": pm20002maCtrlaccessLoopEntry,
       "pm20002maCtrlaccessLoopIndex": pm20002maCtrlaccessLoopIndex,
       "pm20002maCtrlaccessLoopPortn": pm20002maCtrlaccessLoopPortn,
       "pm20002maCtrlclientLoopToLineTable": pm20002maCtrlclientLoopToLineTable,
       "pm20002maCtrlclientLoopToLineEntry": pm20002maCtrlclientLoopToLineEntry,
       "pm20002maCtrlclientLoopToLineIndex": pm20002maCtrlclientLoopToLineIndex,
       "pm20002maCtrlclientLoopToLinePortn": pm20002maCtrlclientLoopToLinePortn,
       "pm20002maCtrlcsfUpInsTable": pm20002maCtrlcsfUpInsTable,
       "pm20002maCtrlcsfUpInsEntry": pm20002maCtrlcsfUpInsEntry,
       "pm20002maCtrlcsfUpInsIndex": pm20002maCtrlcsfUpInsIndex,
       "pm20002maCtrlcsfUpInsPortn": pm20002maCtrlcsfUpInsPortn,
       "pm20002maCtrlcaisDwInsTable": pm20002maCtrlcaisDwInsTable,
       "pm20002maCtrlcaisDwInsEntry": pm20002maCtrlcaisDwInsEntry,
       "pm20002maCtrlcaisDwInsIndex": pm20002maCtrlcaisDwInsIndex,
       "pm20002maCtrlcaisDwInsPortn": pm20002maCtrlcaisDwInsPortn,
       "pm20002maCtrlclientResetAllCountTable": pm20002maCtrlclientResetAllCountTable,
       "pm20002maCtrlclientResetAllCountEntry": pm20002maCtrlclientResetAllCountEntry,
       "pm20002maCtrlclientResetAllCountIndex": pm20002maCtrlclientResetAllCountIndex,
       "pm20002maCtrlclientResetAllCountsPortn": pm20002maCtrlclientResetAllCountsPortn,
       "pm20002maCtrlLine": pm20002maCtrlLine,
       "pm20002maCtrlcommAccessLoopTable": pm20002maCtrlcommAccessLoopTable,
       "pm20002maCtrlcommAccessLoopEntry": pm20002maCtrlcommAccessLoopEntry,
       "pm20002maCtrlcommAccessLoopIndex": pm20002maCtrlcommAccessLoopIndex,
       "pm20002maCtrlcommAccessLoopPortn": pm20002maCtrlcommAccessLoopPortn,
       "pm20002maCtrllineLoopTable": pm20002maCtrllineLoopTable,
       "pm20002maCtrllineLoopEntry": pm20002maCtrllineLoopEntry,
       "pm20002maCtrllineLoopIndex": pm20002maCtrllineLoopIndex,
       "pm20002maCtrllineLoopPortn": pm20002maCtrllineLoopPortn,
       "pm20002maCtrlfecDisableTable": pm20002maCtrlfecDisableTable,
       "pm20002maCtrlfecDisableEntry": pm20002maCtrlfecDisableEntry,
       "pm20002maCtrlfecDisableIndex": pm20002maCtrlfecDisableIndex,
       "pm20002maCtrlfecDisablePortn": pm20002maCtrlfecDisablePortn,
       "pm20002maCtrlmsaLineLoopTable": pm20002maCtrlmsaLineLoopTable,
       "pm20002maCtrlmsaLineLoopEntry": pm20002maCtrlmsaLineLoopEntry,
       "pm20002maCtrlmsaLineLoopIndex": pm20002maCtrlmsaLineLoopIndex,
       "pm20002maCtrlmsaLineLoopPortn": pm20002maCtrlmsaLineLoopPortn,
       "pm20002maCtrlmsaTxResetTable": pm20002maCtrlmsaTxResetTable,
       "pm20002maCtrlmsaTxResetEntry": pm20002maCtrlmsaTxResetEntry,
       "pm20002maCtrlmsaTxResetIndex": pm20002maCtrlmsaTxResetIndex,
       "pm20002maCtrlmsaTxResetPortn": pm20002maCtrlmsaTxResetPortn,
       "pm20002maCtrlmsaRxResetTable": pm20002maCtrlmsaRxResetTable,
       "pm20002maCtrlmsaRxResetEntry": pm20002maCtrlmsaRxResetEntry,
       "pm20002maCtrlmsaRxResetIndex": pm20002maCtrlmsaRxResetIndex,
       "pm20002maCtrlmsaRxResetPortn": pm20002maCtrlmsaRxResetPortn,
       "pm20002maCtrlmsaShutdownTable": pm20002maCtrlmsaShutdownTable,
       "pm20002maCtrlmsaShutdownEntry": pm20002maCtrlmsaShutdownEntry,
       "pm20002maCtrlmsaShutdownIndex": pm20002maCtrlmsaShutdownIndex,
       "pm20002maCtrlmsaShutdownPortn": pm20002maCtrlmsaShutdownPortn,
       "pm20002maCtrllineResetAllCountTable": pm20002maCtrllineResetAllCountTable,
       "pm20002maCtrllineResetAllCountEntry": pm20002maCtrllineResetAllCountEntry,
       "pm20002maCtrllineResetAllCountIndex": pm20002maCtrllineResetAllCountIndex,
       "pm20002maCtrllineResetAllCountsPortn": pm20002maCtrllineResetAllCountsPortn,
       "pm20002mari": pm20002mari,
       "pm20002mariTable": pm20002mariTable,
       "pm20002maRinvSfpTable": pm20002maRinvSfpTable,
       "pm20002maRinvSfpEntry": pm20002maRinvSfpEntry,
       "pm20002maRinvSfpIndex": pm20002maRinvSfpIndex,
       "pm20002maRinvsfp": pm20002maRinvsfp,
       "pm20002maRinvLineTable": pm20002maRinvLineTable,
       "pm20002maRinvLineEntry": pm20002maRinvLineEntry,
       "pm20002maRinvLineIndex": pm20002maRinvLineIndex,
       "pm20002maRinvxfpLine": pm20002maRinvxfpLine,
       "pm20002maRinvReloadInventory": pm20002maRinvReloadInventory,
       "pm20002maRinvHwPlatform": pm20002maRinvHwPlatform,
       "pm20002maRinvModulePlatform": pm20002maRinvModulePlatform,
       "pm20002maRinvSwPlatform": pm20002maRinvSwPlatform,
       "pm20002maRinvGwPlatform": pm20002maRinvGwPlatform,
       "pm20002madownload": pm20002madownload,
       "pm20002maDwlOther": pm20002maDwlOther,
       "pm20002maDwlrestartProcess": pm20002maDwlrestartProcess,
       "pm20002maDwlWarmRestartProcessed": pm20002maDwlWarmRestartProcessed,
       "pm20002maDwlColdRestartProcessed": pm20002maDwlColdRestartProcessed,
       "pm20002maDwlswBanksUsed": pm20002maDwlswBanksUsed,
       "pm20002maDwlSwBank1Used": pm20002maDwlSwBank1Used,
       "pm20002maDwlSwBank2Used": pm20002maDwlSwBank2Used,
       "pm20002maDwlSwBank1Notempty": pm20002maDwlSwBank1Notempty,
       "pm20002maDwlSwBank2Notempty": pm20002maDwlSwBank2Notempty,
       "pm20002maDwlgwBanksUsed": pm20002maDwlgwBanksUsed,
       "pm20002maDwlGwBank1Used": pm20002maDwlGwBank1Used,
       "pm20002maDwlGwBank2Used": pm20002maDwlGwBank2Used,
       "pm20002maDwlGwBank3Used": pm20002maDwlGwBank3Used,
       "pm20002maDwlGwBank4Used": pm20002maDwlGwBank4Used,
       "pm20002maDwlGwBank1Notempty": pm20002maDwlGwBank1Notempty,
       "pm20002maDwlGwBank2Notempty": pm20002maDwlGwBank2Notempty,
       "pm20002maDwlGwBank3Notempty": pm20002maDwlGwBank3Notempty,
       "pm20002maDwlGwBank4Notempty": pm20002maDwlGwBank4Notempty,
       "pm20002maDwlClient": pm20002maDwlClient,
       "pm20002maDwlLine": pm20002maDwlLine,
       "pm20002maConfig": pm20002maConfig,
       "pm20002maCfgAccessCAisCsf": pm20002maCfgAccessCAisCsf,
       "pm20002maCfgClientcaiscsfTable": pm20002maCfgClientcaiscsfTable,
       "pm20002maCfgClientcaiscsfEntry": pm20002maCfgClientcaiscsfEntry,
       "pm20002maCfgClientcaiscsfIndex": pm20002maCfgClientcaiscsfIndex,
       "pm20002maCfgReservePortn": pm20002maCfgReservePortn,
       "pm20002maCfgStartup": pm20002maCfgStartup,
       "pm20002maCfgClientStartupTable": pm20002maCfgClientStartupTable,
       "pm20002maCfgClientStartupEntry": pm20002maCfgClientStartupEntry,
       "pm20002maCfgClientStartupIndex": pm20002maCfgClientStartupIndex,
       "pm20002maCfgSystConfPortPortn": pm20002maCfgSystConfPortPortn,
       "pm20002maCfgNetConfPortPortn": pm20002maCfgNetConfPortPortn,
       "pm20002maCfgOptionsPortPortn": pm20002maCfgOptionsPortPortn,
       "pm20002maCfgLineStartupTable": pm20002maCfgLineStartupTable,
       "pm20002maCfgLineStartupEntry": pm20002maCfgLineStartupEntry,
       "pm20002maCfgLineStartupIndex": pm20002maCfgLineStartupIndex,
       "pm20002maCfgSystConfLinePortn": pm20002maCfgSystConfLinePortn,
       "pm20002maCfgOptionsLinePortn": pm20002maCfgOptionsLinePortn,
       "pm20002maCfgXfpTable": pm20002maCfgXfpTable,
       "pm20002maCfgXfpEntry": pm20002maCfgXfpEntry,
       "pm20002maCfgXfpIndex": pm20002maCfgXfpIndex,
       "pm20002maCfgSystConfMsaLinePortn": pm20002maCfgSystConfMsaLinePortn,
       "pm20002maCfgLabels": pm20002maCfgLabels,
       "pm20002maCfgLabelclientTable": pm20002maCfgLabelclientTable,
       "pm20002maCfgLabelclientEntry": pm20002maCfgLabelclientEntry,
       "pm20002maCfgLabelclientIndex": pm20002maCfgLabelclientIndex,
       "pm20002maCfgLabelclientPortn": pm20002maCfgLabelclientPortn,
       "pm20002maCfgLabellineTable": pm20002maCfgLabellineTable,
       "pm20002maCfgLabellineEntry": pm20002maCfgLabellineEntry,
       "pm20002maCfgLabellineIndex": pm20002maCfgLabellineIndex,
       "pm20002maCfgLabellinePortn": pm20002maCfgLabellinePortn,
       "pm20002maCfgStartuptlh": pm20002maCfgStartuptlh,
       "pm20002maCfgOtxtlhTable": pm20002maCfgOtxtlhTable,
       "pm20002maCfgOtxtlhEntry": pm20002maCfgOtxtlhEntry,
       "pm20002maCfgOtxtlhIndex": pm20002maCfgOtxtlhIndex,
       "pm20002maCfgLinePwrLaserPortn": pm20002maCfgLinePwrLaserPortn,
       "pm20002maCfgLineFCurrentPortn": pm20002maCfgLineFCurrentPortn,
       "pm20002maCfgLineGridCurrentPortn": pm20002maCfgLineGridCurrentPortn,
       "pm20002maCfgFPortn": pm20002maCfgFPortn,
       "pm20002maCfgRxLineFCurrentPortn": pm20002maCfgRxLineFCurrentPortn,
       "pm20002maCfgOther": pm20002maCfgOther,
       "pm20002matablemoduleOther": pm20002matablemoduleOther,
       "pm20002maCfgmode": pm20002maCfgmode,
       "pm20002maCfgfanLowSpeedThreshold": pm20002maCfgfanLowSpeedThreshold,
       "pm20002maCfgfanHighSpeedThreshold": pm20002maCfgfanHighSpeedThreshold,
       "pm20002maCfgStartuptablefive": pm20002maCfgStartuptablefive,
       "pm20002maCfgOtxtlhcapabilitiesTable": pm20002maCfgOtxtlhcapabilitiesTable,
       "pm20002maCfgOtxtlhcapabilitiesEntry": pm20002maCfgOtxtlhcapabilitiesEntry,
       "pm20002maCfgOtxtlhcapabilitiesIndex": pm20002maCfgOtxtlhcapabilitiesIndex,
       "pm20002maCfgComponentTypePortn": pm20002maCfgComponentTypePortn,
       "pm20002maCfgMiscellaneousPortn": pm20002maCfgMiscellaneousPortn,
       "pm20002maCfgFirstChannelPortn": pm20002maCfgFirstChannelPortn,
       "pm20002maCfgLastChannelPortn": pm20002maCfgLastChannelPortn,
       "pm20002maCfgGridPortn": pm20002maCfgGridPortn,
       "pm20002maCfgWriteConfiguration": pm20002maCfgWriteConfiguration,
       "pm20002matraps": pm20002matraps,
       "pm20002matrapPortNumber": pm20002matrapPortNumber,
       "pm20002matrapLineNumber": pm20002matrapLineNumber,
       "pm20002matrapBoardNumber": pm20002matrapBoardNumber,
       "pm20002maLineTrapNotUrgentGoesOn": pm20002maLineTrapNotUrgentGoesOn,
       "pm20002maLineTrapNotUrgentGoesOff": pm20002maLineTrapNotUrgentGoesOff,
       "pm20002maLineTrapUrgentGoesOn": pm20002maLineTrapUrgentGoesOn,
       "pm20002maLineTrapUrgentGoesOff": pm20002maLineTrapUrgentGoesOff,
       "pm20002maLineTrapCritGoesOn": pm20002maLineTrapCritGoesOn,
       "pm20002maLineTrapCritGoesOff": pm20002maLineTrapCritGoesOff,
       "pm20002maClientTrapNotUrgentGoesOn": pm20002maClientTrapNotUrgentGoesOn,
       "pm20002maClientTrapNotUrgentGoesOff": pm20002maClientTrapNotUrgentGoesOff,
       "pm20002maClientTrapUrgentGoesOn": pm20002maClientTrapUrgentGoesOn,
       "pm20002maClientTrapUrgentGoesOff": pm20002maClientTrapUrgentGoesOff,
       "pm20002maClientTrapCritGoesOn": pm20002maClientTrapCritGoesOn,
       "pm20002maClientTrapCritGoesOff": pm20002maClientTrapCritGoesOff,
       "pm20002maPowerTrapUrgentGoesOn": pm20002maPowerTrapUrgentGoesOn,
       "pm20002maPowerTrapUrgentGoesOff": pm20002maPowerTrapUrgentGoesOff,
       "pm20002maMonitoring": pm20002maMonitoring,
       "pm20002maMonOther": pm20002maMonOther,
       "pm20002maMonRmon": pm20002maMonRmon,
       "pm20002maMonClient": pm20002maMonClient,
       "pm20002maMonClientRmonCounter": pm20002maMonClientRmonCounter,
       "pm20002maMonupRmonBytesCounterClientInputTable": pm20002maMonupRmonBytesCounterClientInputTable,
       "pm20002maMonupRmonBytesCounterClientInputEntry": pm20002maMonupRmonBytesCounterClientInputEntry,
       "pm20002maMonupRmonBytesCounterClientInputIndex": pm20002maMonupRmonBytesCounterClientInputIndex,
       "pm20002maMonupRmonBytesCounterClientInputValuePortn": pm20002maMonupRmonBytesCounterClientInputValuePortn,
       "pm20002maMonupRmonBytesCounterClientInputErrorPortn": pm20002maMonupRmonBytesCounterClientInputErrorPortn,
       "pm20002maMonupRmonBytesCounterClientInputOverloadPortn": pm20002maMonupRmonBytesCounterClientInputOverloadPortn,
       "pm20002maMonupRmonCrcErrorsCounterClientInputTable": pm20002maMonupRmonCrcErrorsCounterClientInputTable,
       "pm20002maMonupRmonCrcErrorsCounterClientInputEntry": pm20002maMonupRmonCrcErrorsCounterClientInputEntry,
       "pm20002maMonupRmonCrcErrorsCounterClientInputIndex": pm20002maMonupRmonCrcErrorsCounterClientInputIndex,
       "pm20002maMonupRmonCrcErrorsCounterClientInputValuePortn": pm20002maMonupRmonCrcErrorsCounterClientInputValuePortn,
       "pm20002maMonupRmonCrcErrorsCounterClientInputErrorPortn": pm20002maMonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pm20002maMonupRmonCrcErrorsCounterClientInputOverloadPortn": pm20002maMonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm20002maMonupRmonPacketsCounterClientInputTable": pm20002maMonupRmonPacketsCounterClientInputTable,
       "pm20002maMonupRmonPacketsCounterClientInputEntry": pm20002maMonupRmonPacketsCounterClientInputEntry,
       "pm20002maMonupRmonPacketsCounterClientInputIndex": pm20002maMonupRmonPacketsCounterClientInputIndex,
       "pm20002maMonupRmonPacketsCounterClientInputValuePortn": pm20002maMonupRmonPacketsCounterClientInputValuePortn,
       "pm20002maMonupRmonPacketsCounterClientInputErrorPortn": pm20002maMonupRmonPacketsCounterClientInputErrorPortn,
       "pm20002maMonupRmonPacketsCounterClientInputOverloadPortn": pm20002maMonupRmonPacketsCounterClientInputOverloadPortn,
       "pm20002maMonupRmonBroadcastCounterClientInputTable": pm20002maMonupRmonBroadcastCounterClientInputTable,
       "pm20002maMonupRmonBroadcastCounterClientInputEntry": pm20002maMonupRmonBroadcastCounterClientInputEntry,
       "pm20002maMonupRmonBroadcastCounterClientInputIndex": pm20002maMonupRmonBroadcastCounterClientInputIndex,
       "pm20002maMonupRmonBroadcastCounterClientInputValuePortn": pm20002maMonupRmonBroadcastCounterClientInputValuePortn,
       "pm20002maMonupRmonBroadcastCounterClientInputErrorPortn": pm20002maMonupRmonBroadcastCounterClientInputErrorPortn,
       "pm20002maMonupRmonBroadcastCounterClientInputOverloadPortn": pm20002maMonupRmonBroadcastCounterClientInputOverloadPortn,
       "pm20002maMonupRmonMulticastCounterClientInputTable": pm20002maMonupRmonMulticastCounterClientInputTable,
       "pm20002maMonupRmonMulticastCounterClientInputEntry": pm20002maMonupRmonMulticastCounterClientInputEntry,
       "pm20002maMonupRmonMulticastCounterClientInputIndex": pm20002maMonupRmonMulticastCounterClientInputIndex,
       "pm20002maMonupRmonMulticastCounterClientInputValuePortn": pm20002maMonupRmonMulticastCounterClientInputValuePortn,
       "pm20002maMonupRmonMulticastCounterClientInputErrorPortn": pm20002maMonupRmonMulticastCounterClientInputErrorPortn,
       "pm20002maMonupRmonMulticastCounterClientInputOverloadPortn": pm20002maMonupRmonMulticastCounterClientInputOverloadPortn,
       "pm20002maMonupRmonPauseFrameCounterClientInputTable": pm20002maMonupRmonPauseFrameCounterClientInputTable,
       "pm20002maMonupRmonPauseFrameCounterClientInputEntry": pm20002maMonupRmonPauseFrameCounterClientInputEntry,
       "pm20002maMonupRmonPauseFrameCounterClientInputIndex": pm20002maMonupRmonPauseFrameCounterClientInputIndex,
       "pm20002maMonupRmonPauseFrameCounterClientInputValuePortn": pm20002maMonupRmonPauseFrameCounterClientInputValuePortn,
       "pm20002maMonupRmonPauseFrameCounterClientInputErrorPortn": pm20002maMonupRmonPauseFrameCounterClientInputErrorPortn,
       "pm20002maMonupRmonPauseFrameCounterClientInputOverloadPortn": pm20002maMonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pm20002maMonupRmonUnicastCounterClientInputTable": pm20002maMonupRmonUnicastCounterClientInputTable,
       "pm20002maMonupRmonUnicastCounterClientInputEntry": pm20002maMonupRmonUnicastCounterClientInputEntry,
       "pm20002maMonupRmonUnicastCounterClientInputIndex": pm20002maMonupRmonUnicastCounterClientInputIndex,
       "pm20002maMonupRmonUnicastCounterClientInputValuePortn": pm20002maMonupRmonUnicastCounterClientInputValuePortn,
       "pm20002maMonupRmonUnicastCounterClientInputErrorPortn": pm20002maMonupRmonUnicastCounterClientInputErrorPortn,
       "pm20002maMonupRmonUnicastCounterClientInputOverloadPortn": pm20002maMonupRmonUnicastCounterClientInputOverloadPortn,
       "pm20002maMonupRmonNonunicastCounterClientInputTable": pm20002maMonupRmonNonunicastCounterClientInputTable,
       "pm20002maMonupRmonNonunicastCounterClientInputEntry": pm20002maMonupRmonNonunicastCounterClientInputEntry,
       "pm20002maMonupRmonNonunicastCounterClientInputIndex": pm20002maMonupRmonNonunicastCounterClientInputIndex,
       "pm20002maMonupRmonNonunicastCounterClientInputValuePortn": pm20002maMonupRmonNonunicastCounterClientInputValuePortn,
       "pm20002maMonupRmonNonunicastCounterClientInputErrorPortn": pm20002maMonupRmonNonunicastCounterClientInputErrorPortn,
       "pm20002maMonupRmonNonunicastCounterClientInputOverloadPortn": pm20002maMonupRmonNonunicastCounterClientInputOverloadPortn,
       "pm20002maMondownRmonBytesCounterClientOutputTable": pm20002maMondownRmonBytesCounterClientOutputTable,
       "pm20002maMondownRmonBytesCounterClientOutputEntry": pm20002maMondownRmonBytesCounterClientOutputEntry,
       "pm20002maMondownRmonBytesCounterClientOutputIndex": pm20002maMondownRmonBytesCounterClientOutputIndex,
       "pm20002maMondownRmonBytesCounterClientOutputValuePortn": pm20002maMondownRmonBytesCounterClientOutputValuePortn,
       "pm20002maMondownRmonBytesCounterClientOutputErrorPortn": pm20002maMondownRmonBytesCounterClientOutputErrorPortn,
       "pm20002maMondownRmonBytesCounterClientOutputOverloadPortn": pm20002maMondownRmonBytesCounterClientOutputOverloadPortn,
       "pm20002maMondownRmonCrcErrorsCounterClientOutputTable": pm20002maMondownRmonCrcErrorsCounterClientOutputTable,
       "pm20002maMondownRmonCrcErrorsCounterClientOutputEntry": pm20002maMondownRmonCrcErrorsCounterClientOutputEntry,
       "pm20002maMondownRmonCrcErrorsCounterClientOutputIndex": pm20002maMondownRmonCrcErrorsCounterClientOutputIndex,
       "pm20002maMondownRmonCrcErrorsCounterClientOutputValuePortn": pm20002maMondownRmonCrcErrorsCounterClientOutputValuePortn,
       "pm20002maMondownRmonCrcErrorsCounterClientOutputErrorPortn": pm20002maMondownRmonCrcErrorsCounterClientOutputErrorPortn,
       "pm20002maMondownRmonCrcErrorsCounterClientOutputOverloadPortn": pm20002maMondownRmonCrcErrorsCounterClientOutputOverloadPortn,
       "pm20002maMondownRmonPacketsCounterClientOutputTable": pm20002maMondownRmonPacketsCounterClientOutputTable,
       "pm20002maMondownRmonPacketsCounterClientOutputEntry": pm20002maMondownRmonPacketsCounterClientOutputEntry,
       "pm20002maMondownRmonPacketsCounterClientOutputIndex": pm20002maMondownRmonPacketsCounterClientOutputIndex,
       "pm20002maMondownRmonPacketsCounterClientOutputValuePortn": pm20002maMondownRmonPacketsCounterClientOutputValuePortn,
       "pm20002maMondownRmonPacketsCounterClientOutputErrorPortn": pm20002maMondownRmonPacketsCounterClientOutputErrorPortn,
       "pm20002maMondownRmonPacketsCounterClientOutputOverloadPortn": pm20002maMondownRmonPacketsCounterClientOutputOverloadPortn,
       "pm20002maMondownRmonBroadcastCounterClientOutputTable": pm20002maMondownRmonBroadcastCounterClientOutputTable,
       "pm20002maMondownRmonBroadcastCounterClientOutputEntry": pm20002maMondownRmonBroadcastCounterClientOutputEntry,
       "pm20002maMondownRmonBroadcastCounterClientOutputIndex": pm20002maMondownRmonBroadcastCounterClientOutputIndex,
       "pm20002maMondownRmonBroadcastCounterClientOutputValuePortn": pm20002maMondownRmonBroadcastCounterClientOutputValuePortn,
       "pm20002maMondownRmonBroadcastCounterClientOutputErrorPortn": pm20002maMondownRmonBroadcastCounterClientOutputErrorPortn,
       "pm20002maMondownRmonBroadcastCounterClientOutputOverloadPortn": pm20002maMondownRmonBroadcastCounterClientOutputOverloadPortn,
       "pm20002maMondownRmonMulticastCounterClientOutputTable": pm20002maMondownRmonMulticastCounterClientOutputTable,
       "pm20002maMondownRmonMulticastCounterClientOutputEntry": pm20002maMondownRmonMulticastCounterClientOutputEntry,
       "pm20002maMondownRmonMulticastCounterClientOutputIndex": pm20002maMondownRmonMulticastCounterClientOutputIndex,
       "pm20002maMondownRmonMulticastCounterClientOutputValuePortn": pm20002maMondownRmonMulticastCounterClientOutputValuePortn,
       "pm20002maMondownRmonMulticastCounterClientOutputErrorPortn": pm20002maMondownRmonMulticastCounterClientOutputErrorPortn,
       "pm20002maMondownRmonMulticastCounterClientOutputOverloadPortn": pm20002maMondownRmonMulticastCounterClientOutputOverloadPortn,
       "pm20002maMondownRmonPauseFrameCounterClientOutputTable": pm20002maMondownRmonPauseFrameCounterClientOutputTable,
       "pm20002maMondownRmonPauseFrameCounterClientOutputEntry": pm20002maMondownRmonPauseFrameCounterClientOutputEntry,
       "pm20002maMondownRmonPauseFrameCounterClientOutputIndex": pm20002maMondownRmonPauseFrameCounterClientOutputIndex,
       "pm20002maMondownRmonPauseFrameCounterClientOutputValuePortn": pm20002maMondownRmonPauseFrameCounterClientOutputValuePortn,
       "pm20002maMondownRmonPauseFrameCounterClientOutputErrorPortn": pm20002maMondownRmonPauseFrameCounterClientOutputErrorPortn,
       "pm20002maMondownRmonPauseFrameCounterClientOutputOverloadPortn": pm20002maMondownRmonPauseFrameCounterClientOutputOverloadPortn,
       "pm20002maMondownRmonUnicastCounterClientOutputTable": pm20002maMondownRmonUnicastCounterClientOutputTable,
       "pm20002maMondownRmonUnicastCounterClientOutputEntry": pm20002maMondownRmonUnicastCounterClientOutputEntry,
       "pm20002maMondownRmonUnicastCounterClientOutputIndex": pm20002maMondownRmonUnicastCounterClientOutputIndex,
       "pm20002maMondownRmonUnicastCounterClientOutputValuePortn": pm20002maMondownRmonUnicastCounterClientOutputValuePortn,
       "pm20002maMondownRmonUnicastCounterClientOutputErrorPortn": pm20002maMondownRmonUnicastCounterClientOutputErrorPortn,
       "pm20002maMondownRmonUnicastCounterClientOutputOverloadPortn": pm20002maMondownRmonUnicastCounterClientOutputOverloadPortn,
       "pm20002maMondownRmonNonunicastCounterClientOutputTable": pm20002maMondownRmonNonunicastCounterClientOutputTable,
       "pm20002maMondownRmonNonunicastCounterClientOutputEntry": pm20002maMondownRmonNonunicastCounterClientOutputEntry,
       "pm20002maMondownRmonNonunicastCounterClientOutputIndex": pm20002maMondownRmonNonunicastCounterClientOutputIndex,
       "pm20002maMondownRmonNonunicastCounterClientOutputValuePortn": pm20002maMondownRmonNonunicastCounterClientOutputValuePortn,
       "pm20002maMondownRmonNonunicastCounterClientOutputErrorPortn": pm20002maMondownRmonNonunicastCounterClientOutputErrorPortn,
       "pm20002maMondownRmonNonunicastCounterClientOutputOverloadPortn": pm20002maMondownRmonNonunicastCounterClientOutputOverloadPortn,
       "pm20002maMonPerfOther": pm20002maMonPerfOther,
       "pm20002maMonPerfSync": pm20002maMonPerfSync,
       "pm20002maPerfEnable": pm20002maPerfEnable,
       "pm20002maPerf15minSync": pm20002maPerf15minSync,
       "pm20002maPerf24hSync": pm20002maPerf24hSync,
       "pm20002maMonPerfTimeStamp": pm20002maMonPerfTimeStamp,
       "pm20002maPerf15MinShort": pm20002maPerf15MinShort,
       "pm20002maPerf15MinLong": pm20002maPerf15MinLong,
       "pm20002maPerf24HoursShort": pm20002maPerf24HoursShort,
       "pm20002maPerf24HoursLong": pm20002maPerf24HoursLong,
       "pm20002maPerfCurrent15MinElapsedTime": pm20002maPerfCurrent15MinElapsedTime,
       "pm20002maPerfCurrent24HoursElapsedTime": pm20002maPerfCurrent24HoursElapsedTime,
       "pm20002maMonPerfClient": pm20002maMonPerfClient,
       "pm20002maPerfTelecomInputClientCurrent15StatTable": pm20002maPerfTelecomInputClientCurrent15StatTable,
       "pm20002maPerfTelecomInputClientCurrent15StatEntry": pm20002maPerfTelecomInputClientCurrent15StatEntry,
       "pm20002maPerfTelecomInputClientCurrent15StatIndex": pm20002maPerfTelecomInputClientCurrent15StatIndex,
       "pm20002maPerfTelecomInputClientCurrent15StatInvCvPortn": pm20002maPerfTelecomInputClientCurrent15StatInvCvPortn,
       "pm20002maPerfTelecomInputClientCurrent15StatCvValuePortn": pm20002maPerfTelecomInputClientCurrent15StatCvValuePortn,
       "pm20002maPerfTelecomInputClientCurrent15StatInvEsPortn": pm20002maPerfTelecomInputClientCurrent15StatInvEsPortn,
       "pm20002maPerfTelecomInputClientCurrent15StatEsValuePortn": pm20002maPerfTelecomInputClientCurrent15StatEsValuePortn,
       "pm20002maPerfTelecomInputClientCurrent15StatInvSesPortn": pm20002maPerfTelecomInputClientCurrent15StatInvSesPortn,
       "pm20002maPerfTelecomInputClientCurrent15StatSesValuePortn": pm20002maPerfTelecomInputClientCurrent15StatSesValuePortn,
       "pm20002maPerfTelecomInputClientCurrent15StatInvSefsPortn": pm20002maPerfTelecomInputClientCurrent15StatInvSefsPortn,
       "pm20002maPerfTelecomInputClientCurrent15StatSefsValuePortn": pm20002maPerfTelecomInputClientCurrent15StatSefsValuePortn,
       "pm20002maPerfTelecomInputClientCurrent15StatInvUasPortn": pm20002maPerfTelecomInputClientCurrent15StatInvUasPortn,
       "pm20002maPerfTelecomInputClientCurrent15StatUasValuePortn": pm20002maPerfTelecomInputClientCurrent15StatUasValuePortn,
       "pm20002maPerfTelecomInputClientPast15StatHistoryPort1Table": pm20002maPerfTelecomInputClientPast15StatHistoryPort1Table,
       "pm20002maPerfTelecomInputClientPast15StatHistoryPort1Entry": pm20002maPerfTelecomInputClientPast15StatHistoryPort1Entry,
       "pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index": pm20002maPerfTelecomInputClientPast15StatHistoryPort1Index,
       "pm20002maPerfTelecomInputClientPast15StatHistoryInvCvPort1": pm20002maPerfTelecomInputClientPast15StatHistoryInvCvPort1,
       "pm20002maPerfTelecomInputClientPast15StatHistoryCvValuePort1": pm20002maPerfTelecomInputClientPast15StatHistoryCvValuePort1,
       "pm20002maPerfTelecomInputClientPast15StatHistoryInvEsPort1": pm20002maPerfTelecomInputClientPast15StatHistoryInvEsPort1,
       "pm20002maPerfTelecomInputClientPast15StatHistoryEsValuePort1": pm20002maPerfTelecomInputClientPast15StatHistoryEsValuePort1,
       "pm20002maPerfTelecomInputClientPast15StatHistoryInvSesPort1": pm20002maPerfTelecomInputClientPast15StatHistoryInvSesPort1,
       "pm20002maPerfTelecomInputClientPast15StatHistorySesValuePort1": pm20002maPerfTelecomInputClientPast15StatHistorySesValuePort1,
       "pm20002maPerfTelecomInputClientPast15StatHistoryInvSefsPort1": pm20002maPerfTelecomInputClientPast15StatHistoryInvSefsPort1,
       "pm20002maPerfTelecomInputClientPast15StatHistorySefsValuePort1": pm20002maPerfTelecomInputClientPast15StatHistorySefsValuePort1,
       "pm20002maPerfTelecomInputClientPast15StatHistoryInvUasPort1": pm20002maPerfTelecomInputClientPast15StatHistoryInvUasPort1,
       "pm20002maPerfTelecomInputClientPast15StatHistoryUasValuePort1": pm20002maPerfTelecomInputClientPast15StatHistoryUasValuePort1,
       "pm20002maPerfTelecomInputClientCurrent24StatTable": pm20002maPerfTelecomInputClientCurrent24StatTable,
       "pm20002maPerfTelecomInputClientCurrent24StatEntry": pm20002maPerfTelecomInputClientCurrent24StatEntry,
       "pm20002maPerfTelecomInputClientCurrent24StatIndex": pm20002maPerfTelecomInputClientCurrent24StatIndex,
       "pm20002maPerfTelecomInputClientCurrent24StatInvCvPortn": pm20002maPerfTelecomInputClientCurrent24StatInvCvPortn,
       "pm20002maPerfTelecomInputClientCurrent24StatCvValuePortn": pm20002maPerfTelecomInputClientCurrent24StatCvValuePortn,
       "pm20002maPerfTelecomInputClientCurrent24StatInvEsPortn": pm20002maPerfTelecomInputClientCurrent24StatInvEsPortn,
       "pm20002maPerfTelecomInputClientCurrent24StatEsValuePortn": pm20002maPerfTelecomInputClientCurrent24StatEsValuePortn,
       "pm20002maPerfTelecomInputClientCurrent24StatInvSesPortn": pm20002maPerfTelecomInputClientCurrent24StatInvSesPortn,
       "pm20002maPerfTelecomInputClientCurrent24StatSesValuePortn": pm20002maPerfTelecomInputClientCurrent24StatSesValuePortn,
       "pm20002maPerfTelecomInputClientCurrent24StatInvSefsPortn": pm20002maPerfTelecomInputClientCurrent24StatInvSefsPortn,
       "pm20002maPerfTelecomInputClientCurrent24StatSefsValuePortn": pm20002maPerfTelecomInputClientCurrent24StatSefsValuePortn,
       "pm20002maPerfTelecomInputClientCurrent24StatInvUasPortn": pm20002maPerfTelecomInputClientCurrent24StatInvUasPortn,
       "pm20002maPerfTelecomInputClientCurrent24StatUasValuePortn": pm20002maPerfTelecomInputClientCurrent24StatUasValuePortn,
       "pm20002maPerfTelecomInputClientPast24StatHistoryPort1Table": pm20002maPerfTelecomInputClientPast24StatHistoryPort1Table,
       "pm20002maPerfTelecomInputClientPast24StatHistoryPort1Entry": pm20002maPerfTelecomInputClientPast24StatHistoryPort1Entry,
       "pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index": pm20002maPerfTelecomInputClientPast24StatHistoryPort1Index,
       "pm20002maPerfTelecomInputClientPast24StatHistoryInvCvPort1": pm20002maPerfTelecomInputClientPast24StatHistoryInvCvPort1,
       "pm20002maPerfTelecomInputClientPast24StatHistoryCvValuePort1": pm20002maPerfTelecomInputClientPast24StatHistoryCvValuePort1,
       "pm20002maPerfTelecomInputClientPast24StatHistoryInvEsPort1": pm20002maPerfTelecomInputClientPast24StatHistoryInvEsPort1,
       "pm20002maPerfTelecomInputClientPast24StatHistoryEsValuePort1": pm20002maPerfTelecomInputClientPast24StatHistoryEsValuePort1,
       "pm20002maPerfTelecomInputClientPast24StatHistoryInvSesPort1": pm20002maPerfTelecomInputClientPast24StatHistoryInvSesPort1,
       "pm20002maPerfTelecomInputClientPast24StatHistorySesValuePort1": pm20002maPerfTelecomInputClientPast24StatHistorySesValuePort1,
       "pm20002maPerfTelecomInputClientPast24StatHistoryInvSefsPort1": pm20002maPerfTelecomInputClientPast24StatHistoryInvSefsPort1,
       "pm20002maPerfTelecomInputClientPast24StatHistorySefsValuePort1": pm20002maPerfTelecomInputClientPast24StatHistorySefsValuePort1,
       "pm20002maPerfTelecomInputClientPast24StatHistoryInvUasPort1": pm20002maPerfTelecomInputClientPast24StatHistoryInvUasPort1,
       "pm20002maPerfTelecomInputClientPast24StatHistoryUasValuePort1": pm20002maPerfTelecomInputClientPast24StatHistoryUasValuePort1,
       "pm20002maPerfTelecomOutputClientCurrent15StatTable": pm20002maPerfTelecomOutputClientCurrent15StatTable,
       "pm20002maPerfTelecomOutputClientCurrent15StatEntry": pm20002maPerfTelecomOutputClientCurrent15StatEntry,
       "pm20002maPerfTelecomOutputClientCurrent15StatIndex": pm20002maPerfTelecomOutputClientCurrent15StatIndex,
       "pm20002maPerfTelecomOutputClientCurrent15StatInvCvPortn": pm20002maPerfTelecomOutputClientCurrent15StatInvCvPortn,
       "pm20002maPerfTelecomOutputClientCurrent15StatCvValuePortn": pm20002maPerfTelecomOutputClientCurrent15StatCvValuePortn,
       "pm20002maPerfTelecomOutputClientCurrent15StatInvEsPortn": pm20002maPerfTelecomOutputClientCurrent15StatInvEsPortn,
       "pm20002maPerfTelecomOutputClientCurrent15StatEsValuePortn": pm20002maPerfTelecomOutputClientCurrent15StatEsValuePortn,
       "pm20002maPerfTelecomOutputClientCurrent15StatInvSesPortn": pm20002maPerfTelecomOutputClientCurrent15StatInvSesPortn,
       "pm20002maPerfTelecomOutputClientCurrent15StatSesValuePortn": pm20002maPerfTelecomOutputClientCurrent15StatSesValuePortn,
       "pm20002maPerfTelecomOutputClientCurrent15StatInvSefsPortn": pm20002maPerfTelecomOutputClientCurrent15StatInvSefsPortn,
       "pm20002maPerfTelecomOutputClientCurrent15StatSefsValuePortn": pm20002maPerfTelecomOutputClientCurrent15StatSefsValuePortn,
       "pm20002maPerfTelecomOutputClientCurrent15StatInvUasPortn": pm20002maPerfTelecomOutputClientCurrent15StatInvUasPortn,
       "pm20002maPerfTelecomOutputClientCurrent15StatUasValuePortn": pm20002maPerfTelecomOutputClientCurrent15StatUasValuePortn,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Table": pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Table,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Entry": pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Entry,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index": pm20002maPerfTelecomOutputClientPast15StatHistoryPort1Index,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryInvCvPort1": pm20002maPerfTelecomOutputClientPast15StatHistoryInvCvPort1,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryCvValuePort1": pm20002maPerfTelecomOutputClientPast15StatHistoryCvValuePort1,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryInvEsPort1": pm20002maPerfTelecomOutputClientPast15StatHistoryInvEsPort1,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryEsValuePort1": pm20002maPerfTelecomOutputClientPast15StatHistoryEsValuePort1,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryInvSesPort1": pm20002maPerfTelecomOutputClientPast15StatHistoryInvSesPort1,
       "pm20002maPerfTelecomOutputClientPast15StatHistorySesValuePort1": pm20002maPerfTelecomOutputClientPast15StatHistorySesValuePort1,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1": pm20002maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1,
       "pm20002maPerfTelecomOutputClientPast15StatHistorySefsValuePort1": pm20002maPerfTelecomOutputClientPast15StatHistorySefsValuePort1,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryInvUasPort1": pm20002maPerfTelecomOutputClientPast15StatHistoryInvUasPort1,
       "pm20002maPerfTelecomOutputClientPast15StatHistoryUasValuePort1": pm20002maPerfTelecomOutputClientPast15StatHistoryUasValuePort1,
       "pm20002maPerfTelecomOutputClientCurrent24StatTable": pm20002maPerfTelecomOutputClientCurrent24StatTable,
       "pm20002maPerfTelecomOutputClientCurrent24StatEntry": pm20002maPerfTelecomOutputClientCurrent24StatEntry,
       "pm20002maPerfTelecomOutputClientCurrent24StatIndex": pm20002maPerfTelecomOutputClientCurrent24StatIndex,
       "pm20002maPerfTelecomOutputClientCurrent24StatInvCvPortn": pm20002maPerfTelecomOutputClientCurrent24StatInvCvPortn,
       "pm20002maPerfTelecomOutputClientCurrent24StatCvValuePortn": pm20002maPerfTelecomOutputClientCurrent24StatCvValuePortn,
       "pm20002maPerfTelecomOutputClientCurrent24StatInvEsPortn": pm20002maPerfTelecomOutputClientCurrent24StatInvEsPortn,
       "pm20002maPerfTelecomOutputClientCurrent24StatEsValuePortn": pm20002maPerfTelecomOutputClientCurrent24StatEsValuePortn,
       "pm20002maPerfTelecomOutputClientCurrent24StatInvSesPortn": pm20002maPerfTelecomOutputClientCurrent24StatInvSesPortn,
       "pm20002maPerfTelecomOutputClientCurrent24StatSesValuePortn": pm20002maPerfTelecomOutputClientCurrent24StatSesValuePortn,
       "pm20002maPerfTelecomOutputClientCurrent24StatInvSefsPortn": pm20002maPerfTelecomOutputClientCurrent24StatInvSefsPortn,
       "pm20002maPerfTelecomOutputClientCurrent24StatSefsValuePortn": pm20002maPerfTelecomOutputClientCurrent24StatSefsValuePortn,
       "pm20002maPerfTelecomOutputClientCurrent24StatInvUasPortn": pm20002maPerfTelecomOutputClientCurrent24StatInvUasPortn,
       "pm20002maPerfTelecomOutputClientCurrent24StatUasValuePortn": pm20002maPerfTelecomOutputClientCurrent24StatUasValuePortn,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Table": pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Table,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Entry": pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Entry,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index": pm20002maPerfTelecomOutputClientPast24StatHistoryPort1Index,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryInvCvPort1": pm20002maPerfTelecomOutputClientPast24StatHistoryInvCvPort1,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryCvValuePort1": pm20002maPerfTelecomOutputClientPast24StatHistoryCvValuePort1,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryInvEsPort1": pm20002maPerfTelecomOutputClientPast24StatHistoryInvEsPort1,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryEsValuePort1": pm20002maPerfTelecomOutputClientPast24StatHistoryEsValuePort1,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryInvSesPort1": pm20002maPerfTelecomOutputClientPast24StatHistoryInvSesPort1,
       "pm20002maPerfTelecomOutputClientPast24StatHistorySesValuePort1": pm20002maPerfTelecomOutputClientPast24StatHistorySesValuePort1,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1": pm20002maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1,
       "pm20002maPerfTelecomOutputClientPast24StatHistorySefsValuePort1": pm20002maPerfTelecomOutputClientPast24StatHistorySefsValuePort1,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryInvUasPort1": pm20002maPerfTelecomOutputClientPast24StatHistoryInvUasPort1,
       "pm20002maPerfTelecomOutputClientPast24StatHistoryUasValuePort1": pm20002maPerfTelecomOutputClientPast24StatHistoryUasValuePort1,
       "pm20002maPerfDatacomClientCurrent15StatTable": pm20002maPerfDatacomClientCurrent15StatTable,
       "pm20002maPerfDatacomClientCurrent15StatEntry": pm20002maPerfDatacomClientCurrent15StatEntry,
       "pm20002maPerfDatacomClientCurrent15StatIndex": pm20002maPerfDatacomClientCurrent15StatIndex,
       "pm20002maperfdatacomclientCurrent15StatInCrcCountInvPortn": pm20002maperfdatacomclientCurrent15StatInCrcCountInvPortn,
       "pm20002maperfdatacomclientCurrent15StatInCrcCountPortn": pm20002maperfdatacomclientCurrent15StatInCrcCountPortn,
       "pm20002maperfdatacomclientCurrent15StatInPacketCountInvPortn": pm20002maperfdatacomclientCurrent15StatInPacketCountInvPortn,
       "pm20002maperfdatacomclientCurrent15StatInPacketCountPortn": pm20002maperfdatacomclientCurrent15StatInPacketCountPortn,
       "pm20002maperfdatacomclientCurrent15StatOutCrcCountInvPortn": pm20002maperfdatacomclientCurrent15StatOutCrcCountInvPortn,
       "pm20002maperfdatacomclientCurrent15StatOutCrcCountPortn": pm20002maperfdatacomclientCurrent15StatOutCrcCountPortn,
       "pm20002maperfdatacomclientCurrent15StatOutPacketCountInvPortn": pm20002maperfdatacomclientCurrent15StatOutPacketCountInvPortn,
       "pm20002maperfdatacomclientCurrent15StatOutPacketCountPortn": pm20002maperfdatacomclientCurrent15StatOutPacketCountPortn,
       "pm20002maPerfDatacomClientPast15StatHistoryPort1Table": pm20002maPerfDatacomClientPast15StatHistoryPort1Table,
       "pm20002maPerfDatacomClientPast15StatHistoryPort1Entry": pm20002maPerfDatacomClientPast15StatHistoryPort1Entry,
       "pm20002maPerfDatacomClientPast15StatHistoryPort1Index": pm20002maPerfDatacomClientPast15StatHistoryPort1Index,
       "pm20002maperfdatacomclientPast15StatInCrcCountInvPort1": pm20002maperfdatacomclientPast15StatInCrcCountInvPort1,
       "pm20002maperfdatacomclientPast15StatInCrcCountPort1": pm20002maperfdatacomclientPast15StatInCrcCountPort1,
       "pm20002maperfdatacomclientPast15StatInPacketCountInvPort1": pm20002maperfdatacomclientPast15StatInPacketCountInvPort1,
       "pm20002maperfdatacomclientPast15StatInPacketCountPort1": pm20002maperfdatacomclientPast15StatInPacketCountPort1,
       "pm20002maperfdatacomclientPast15StatOutCrcCountInvPort1": pm20002maperfdatacomclientPast15StatOutCrcCountInvPort1,
       "pm20002maperfdatacomclientPast15StatOutCrcCountPort1": pm20002maperfdatacomclientPast15StatOutCrcCountPort1,
       "pm20002maperfdatacomclientPast15StatOutPacketCountInvPort1": pm20002maperfdatacomclientPast15StatOutPacketCountInvPort1,
       "pm20002maperfdatacomclientPast15StatOutPacketCountPort1": pm20002maperfdatacomclientPast15StatOutPacketCountPort1,
       "pm20002maPerfDatacomClientCurrent24StatTable": pm20002maPerfDatacomClientCurrent24StatTable,
       "pm20002maPerfDatacomClientCurrent24StatEntry": pm20002maPerfDatacomClientCurrent24StatEntry,
       "pm20002maPerfDatacomClientCurrent24StatIndex": pm20002maPerfDatacomClientCurrent24StatIndex,
       "pm20002maperfdatacomclientCurrent24StatInCrcCountInvPortn": pm20002maperfdatacomclientCurrent24StatInCrcCountInvPortn,
       "pm20002maperfdatacomclientCurrent24StatInCrcCountPortn": pm20002maperfdatacomclientCurrent24StatInCrcCountPortn,
       "pm20002maperfdatacomclientCurrent24StatInPacketCountInvPortn": pm20002maperfdatacomclientCurrent24StatInPacketCountInvPortn,
       "pm20002maperfdatacomclientCurrent24StatInPacketCountPortn": pm20002maperfdatacomclientCurrent24StatInPacketCountPortn,
       "pm20002maperfdatacomclientCurrent24StatOutCrcCountInvPortn": pm20002maperfdatacomclientCurrent24StatOutCrcCountInvPortn,
       "pm20002maperfdatacomclientCurrent24StatOutCrcCountPortn": pm20002maperfdatacomclientCurrent24StatOutCrcCountPortn,
       "pm20002maperfdatacomclientCurrent24StatOutPacketCountInvPortn": pm20002maperfdatacomclientCurrent24StatOutPacketCountInvPortn,
       "pm20002maperfdatacomclientCurrent24StatOutPacketCountPortn": pm20002maperfdatacomclientCurrent24StatOutPacketCountPortn,
       "pm20002maPerfDatacomClientPast24StatHistoryPort1Table": pm20002maPerfDatacomClientPast24StatHistoryPort1Table,
       "pm20002maPerfDatacomClientPast24StatHistoryPort1Entry": pm20002maPerfDatacomClientPast24StatHistoryPort1Entry,
       "pm20002maPerfDatacomClientPast24StatHistoryPort1Index": pm20002maPerfDatacomClientPast24StatHistoryPort1Index,
       "pm20002maperfdatacomclientPast24StatInCrcCountInvPort1": pm20002maperfdatacomclientPast24StatInCrcCountInvPort1,
       "pm20002maperfdatacomclientPast24StatInCrcCountPort1": pm20002maperfdatacomclientPast24StatInCrcCountPort1,
       "pm20002maperfdatacomclientPast24StatInPacketCountInvPort1": pm20002maperfdatacomclientPast24StatInPacketCountInvPort1,
       "pm20002maperfdatacomclientPast24StatInPacketCountPort1": pm20002maperfdatacomclientPast24StatInPacketCountPort1,
       "pm20002maperfdatacomclientPast24StatOutCrcCountInvPort1": pm20002maperfdatacomclientPast24StatOutCrcCountInvPort1,
       "pm20002maperfdatacomclientPast24StatOutCrcCountPort1": pm20002maperfdatacomclientPast24StatOutCrcCountPort1,
       "pm20002maperfdatacomclientPast24StatOutPacketCountInvPort1": pm20002maperfdatacomclientPast24StatOutPacketCountInvPort1,
       "pm20002maperfdatacomclientPast24StatOutPacketCountPort1": pm20002maperfdatacomclientPast24StatOutPacketCountPort1,
       "pm20002maMonPerfLine": pm20002maMonPerfLine,
       "pm20002maPerfTelecomLinePostFecCurrent15StatTable": pm20002maPerfTelecomLinePostFecCurrent15StatTable,
       "pm20002maPerfTelecomLinePostFecCurrent15StatEntry": pm20002maPerfTelecomLinePostFecCurrent15StatEntry,
       "pm20002maPerfTelecomLinePostFecCurrent15StatIndex": pm20002maPerfTelecomLinePostFecCurrent15StatIndex,
       "pm20002maPerfTelecomLinePostFecCurrent15StatInvCvPortn": pm20002maPerfTelecomLinePostFecCurrent15StatInvCvPortn,
       "pm20002maPerfTelecomLinePostFecCurrent15StatCvValuePortn": pm20002maPerfTelecomLinePostFecCurrent15StatCvValuePortn,
       "pm20002maPerfTelecomLinePostFecCurrent15StatInvEsPortn": pm20002maPerfTelecomLinePostFecCurrent15StatInvEsPortn,
       "pm20002maPerfTelecomLinePostFecCurrent15StatEsValuePortn": pm20002maPerfTelecomLinePostFecCurrent15StatEsValuePortn,
       "pm20002maPerfTelecomLinePostFecCurrent15StatInvSesPortn": pm20002maPerfTelecomLinePostFecCurrent15StatInvSesPortn,
       "pm20002maPerfTelecomLinePostFecCurrent15StatSesValuePortn": pm20002maPerfTelecomLinePostFecCurrent15StatSesValuePortn,
       "pm20002maPerfTelecomLinePostFecCurrent15StatInvSefsPortn": pm20002maPerfTelecomLinePostFecCurrent15StatInvSefsPortn,
       "pm20002maPerfTelecomLinePostFecCurrent15StatSefsValuePortn": pm20002maPerfTelecomLinePostFecCurrent15StatSefsValuePortn,
       "pm20002maPerfTelecomLinePostFecCurrent15StatInvUasPortn": pm20002maPerfTelecomLinePostFecCurrent15StatInvUasPortn,
       "pm20002maPerfTelecomLinePostFecCurrent15StatUasValuePortn": pm20002maPerfTelecomLinePostFecCurrent15StatUasValuePortn,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Table": pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Table,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Entry": pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Entry,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index": pm20002maPerfTelecomLinePostFecPast15StatHistoryPort1Index,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1": pm20002maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1": pm20002maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1": pm20002maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1": pm20002maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1": pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1,
       "pm20002maPerfTelecomLinePostFecPast15StatHistorySesValuePort1": pm20002maPerfTelecomLinePostFecPast15StatHistorySesValuePort1,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1": pm20002maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1,
       "pm20002maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1": pm20002maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1": pm20002maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1,
       "pm20002maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1": pm20002maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1,
       "pm20002maPerfTelecomLinePostFecCurrent24StatTable": pm20002maPerfTelecomLinePostFecCurrent24StatTable,
       "pm20002maPerfTelecomLinePostFecCurrent24StatEntry": pm20002maPerfTelecomLinePostFecCurrent24StatEntry,
       "pm20002maPerfTelecomLinePostFecCurrent24StatIndex": pm20002maPerfTelecomLinePostFecCurrent24StatIndex,
       "pm20002maPerfTelecomLinePostFecCurrent24StatInvCvPortn": pm20002maPerfTelecomLinePostFecCurrent24StatInvCvPortn,
       "pm20002maPerfTelecomLinePostFecCurrent24StatCvValuePortn": pm20002maPerfTelecomLinePostFecCurrent24StatCvValuePortn,
       "pm20002maPerfTelecomLinePostFecCurrent24StatInvEsPortn": pm20002maPerfTelecomLinePostFecCurrent24StatInvEsPortn,
       "pm20002maPerfTelecomLinePostFecCurrent24StatEsValuePortn": pm20002maPerfTelecomLinePostFecCurrent24StatEsValuePortn,
       "pm20002maPerfTelecomLinePostFecCurrent24StatInvSesPortn": pm20002maPerfTelecomLinePostFecCurrent24StatInvSesPortn,
       "pm20002maPerfTelecomLinePostFecCurrent24StatSesValuePortn": pm20002maPerfTelecomLinePostFecCurrent24StatSesValuePortn,
       "pm20002maPerfTelecomLinePostFecCurrent24StatInvSefsPortn": pm20002maPerfTelecomLinePostFecCurrent24StatInvSefsPortn,
       "pm20002maPerfTelecomLinePostFecCurrent24StatSefsValuePortn": pm20002maPerfTelecomLinePostFecCurrent24StatSefsValuePortn,
       "pm20002maPerfTelecomLinePostFecCurrent24StatInvUasPortn": pm20002maPerfTelecomLinePostFecCurrent24StatInvUasPortn,
       "pm20002maPerfTelecomLinePostFecCurrent24StatUasValuePortn": pm20002maPerfTelecomLinePostFecCurrent24StatUasValuePortn,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Table": pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Table,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Entry": pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Entry,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index": pm20002maPerfTelecomLinePostFecPast24StatHistoryPort1Index,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1": pm20002maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1": pm20002maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1": pm20002maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1": pm20002maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1": pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1,
       "pm20002maPerfTelecomLinePostFecPast24StatHistorySesValuePort1": pm20002maPerfTelecomLinePostFecPast24StatHistorySesValuePort1,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1": pm20002maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1,
       "pm20002maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1": pm20002maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1": pm20002maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1,
       "pm20002maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1": pm20002maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1,
       "pm20002maPerfTelecomBerLinePreFecCurrent15StatTable": pm20002maPerfTelecomBerLinePreFecCurrent15StatTable,
       "pm20002maPerfTelecomBerLinePreFecCurrent15StatEntry": pm20002maPerfTelecomBerLinePreFecCurrent15StatEntry,
       "pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex": pm20002maPerfTelecomBerLinePreFecCurrent15StatIndex,
       "pm20002maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn": pm20002maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn": pm20002maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn": pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn": pm20002maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn": pm20002maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn": pm20002maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn,
       "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table": pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table,
       "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry": pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry,
       "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index": pm20002maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index,
       "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1": pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1,
       "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1": pm20002maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1,
       "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1": pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1,
       "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1": pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1,
       "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1": pm20002maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1,
       "pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1": pm20002maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1,
       "pm20002maPerfTelecomBerLinePreFecCurrent24StatTable": pm20002maPerfTelecomBerLinePreFecCurrent24StatTable,
       "pm20002maPerfTelecomBerLinePreFecCurrent24StatEntry": pm20002maPerfTelecomBerLinePreFecCurrent24StatEntry,
       "pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex": pm20002maPerfTelecomBerLinePreFecCurrent24StatIndex,
       "pm20002maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn": pm20002maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn": pm20002maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn": pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn": pm20002maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn": pm20002maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn,
       "pm20002maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn": pm20002maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn,
       "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table": pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table,
       "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry": pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry,
       "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index": pm20002maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index,
       "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1": pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1,
       "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1": pm20002maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1,
       "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1": pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1,
       "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1": pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1,
       "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1": pm20002maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1,
       "pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1": pm20002maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1}
)
