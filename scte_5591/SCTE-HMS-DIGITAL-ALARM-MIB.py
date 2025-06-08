# SNMP MIB module (SCTE-HMS-DIGITAL-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-DIGITAL-ALARM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:05 2025
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

(heDigitalCommonAlarms,) = mibBuilder.importSymbols(
    "SCTE-HE-DIGITAL-COMMON-MIB",
    "heDigitalCommonAlarms")

(heCommonTrapPrefix,) = mibBuilder.importSymbols(
    "SCTE-HMS-HE-COMMON-MIB",
    "heCommonTrapPrefix")

(HeResetValue,) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-TC-MIB",
    "HeResetValue")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

heDigitalAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    heDigitalAlarmMIB.setRevisions(
        ("2007-08-17 12:00",
         "2007-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DigitalAlarmComponentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 1),
          ("software", 2),
          ("firmware", 3),
          ("video", 4),
          ("audio", 5),
          ("data", 6),
          ("rf", 7),
          ("optical", 8),
          ("qam", 9),
          ("mpeg", 10),
          ("ip", 11),
          ("transportStream", 12),
          ("program", 13),
          ("sdvServer", 14),
          ("sdvManager", 15),
          ("encryptor", 16),
          ("enviromental", 17),
          ("userDefined1", 18),
          ("userDefined2", 19))
    )



class DigitalAlarmCategoryType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("communication", 1),
          ("process", 2),
          ("session", 3),
          ("capacity", 4),
          ("maintenance", 5),
          ("provisioning", 6),
          ("programMgmt", 7),
          ("redundancy", 8),
          ("authentication", 9))
    )



class DigitalAlarmPriorityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("warning", 5),
          ("notice", 6),
          ("alert", 7),
          ("status", 8),
          ("unknown", 9))
    )



class DigitalAlarmStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nominal", 1),
          ("fault", 2),
          ("informational", 3),
          ("diagnostic", 4))
    )



class DigitalTrapRegenerate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapRegenerate", 1),
          ("trapNormal", 2))
    )



class DigitalAlarmAckValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ackAlarm", 1),
          ("clearAck", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DigitalAlarmMIBObjects_ObjectIdentity = ObjectIdentity
digitalAlarmMIBObjects = _DigitalAlarmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1)
)
_DigitalAlarms_ObjectIdentity = ObjectIdentity
digitalAlarms = _DigitalAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1)
)
_DigitalAlarmTable_Object = MibTable
digitalAlarmTable = _DigitalAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    digitalAlarmTable.setStatus("current")
_DigitalAlarmEntry_Object = MibTableRow
digitalAlarmEntry = _DigitalAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1)
)
digitalAlarmEntry.setIndexNames(
    (0, "SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmOID"),
    (0, "SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmInstance"),
)
if mibBuilder.loadTexts:
    digitalAlarmEntry.setStatus("current")
_DigitalAlarmOID_Type = ObjectIdentifier
_DigitalAlarmOID_Object = MibTableColumn
digitalAlarmOID = _DigitalAlarmOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 1),
    _DigitalAlarmOID_Type()
)
digitalAlarmOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalAlarmOID.setStatus("current")
_DigitalAlarmInstance_Type = Unsigned32
_DigitalAlarmInstance_Object = MibTableColumn
digitalAlarmInstance = _DigitalAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 2),
    _DigitalAlarmInstance_Type()
)
digitalAlarmInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalAlarmInstance.setStatus("current")
_DigitalAlarmEntProductID_Type = ObjectIdentifier
_DigitalAlarmEntProductID_Object = MibTableColumn
digitalAlarmEntProductID = _DigitalAlarmEntProductID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 3),
    _DigitalAlarmEntProductID_Type()
)
digitalAlarmEntProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmEntProductID.setStatus("current")
_DigitalAlarmEntDeviceType_Type = SnmpAdminString
_DigitalAlarmEntDeviceType_Object = MibTableColumn
digitalAlarmEntDeviceType = _DigitalAlarmEntDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 4),
    _DigitalAlarmEntDeviceType_Type()
)
digitalAlarmEntDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmEntDeviceType.setStatus("current")


class _DigitalAlarmEntAlias_Type(SnmpAdminString):
    """Custom type digitalAlarmEntAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DigitalAlarmEntAlias_Type.__name__ = "SnmpAdminString"
_DigitalAlarmEntAlias_Object = MibTableColumn
digitalAlarmEntAlias = _DigitalAlarmEntAlias_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 5),
    _DigitalAlarmEntAlias_Type()
)
digitalAlarmEntAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmEntAlias.setStatus("current")
_DigitalAlarmComponent_Type = DigitalAlarmComponentType
_DigitalAlarmComponent_Object = MibTableColumn
digitalAlarmComponent = _DigitalAlarmComponent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 6),
    _DigitalAlarmComponent_Type()
)
digitalAlarmComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmComponent.setStatus("current")
_DigitalAlarmCategory_Type = DigitalAlarmCategoryType
_DigitalAlarmCategory_Object = MibTableColumn
digitalAlarmCategory = _DigitalAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 7),
    _DigitalAlarmCategory_Type()
)
digitalAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmCategory.setStatus("current")
_DigitalAlarmPriority_Type = DigitalAlarmPriorityType
_DigitalAlarmPriority_Object = MibTableColumn
digitalAlarmPriority = _DigitalAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 8),
    _DigitalAlarmPriority_Type()
)
digitalAlarmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmPriority.setStatus("current")
_DigitalAlarmState_Type = DigitalAlarmStateType
_DigitalAlarmState_Object = MibTableColumn
digitalAlarmState = _DigitalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 9),
    _DigitalAlarmState_Type()
)
digitalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmState.setStatus("current")
_DigitalAlarmValueLastChange_Type = Integer32
_DigitalAlarmValueLastChange_Object = MibTableColumn
digitalAlarmValueLastChange = _DigitalAlarmValueLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 10),
    _DigitalAlarmValueLastChange_Type()
)
digitalAlarmValueLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmValueLastChange.setStatus("current")
_DigitalAlarmVendorText_Type = SnmpAdminString
_DigitalAlarmVendorText_Object = MibTableColumn
digitalAlarmVendorText = _DigitalAlarmVendorText_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 11),
    _DigitalAlarmVendorText_Type()
)
digitalAlarmVendorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmVendorText.setStatus("current")


class _DigitalAlarmAlias_Type(SnmpAdminString):
    """Custom type digitalAlarmAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DigitalAlarmAlias_Type.__name__ = "SnmpAdminString"
_DigitalAlarmAlias_Object = MibTableColumn
digitalAlarmAlias = _DigitalAlarmAlias_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 12),
    _DigitalAlarmAlias_Type()
)
digitalAlarmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmAlias.setStatus("current")
_DigitalAlarmInitialTime_Type = DateAndTime
_DigitalAlarmInitialTime_Object = MibTableColumn
digitalAlarmInitialTime = _DigitalAlarmInitialTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 13),
    _DigitalAlarmInitialTime_Type()
)
digitalAlarmInitialTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmInitialTime.setStatus("current")
_DigitalAlarmLastTime_Type = DateAndTime
_DigitalAlarmLastTime_Object = MibTableColumn
digitalAlarmLastTime = _DigitalAlarmLastTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 14),
    _DigitalAlarmLastTime_Type()
)
digitalAlarmLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLastTime.setStatus("current")
_DigitalAlarmCount_Type = Counter32
_DigitalAlarmCount_Object = MibTableColumn
digitalAlarmCount = _DigitalAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 1, 1, 1, 15),
    _DigitalAlarmCount_Type()
)
digitalAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmCount.setStatus("current")
_DigitalAlarmThresholds_ObjectIdentity = ObjectIdentity
digitalAlarmThresholds = _DigitalAlarmThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2)
)
_DigitalAlarmThresholdTable_Object = MibTable
digitalAlarmThresholdTable = _DigitalAlarmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    digitalAlarmThresholdTable.setStatus("current")
_DigitalAlarmThresholdEntry_Object = MibTableRow
digitalAlarmThresholdEntry = _DigitalAlarmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1)
)
digitalAlarmThresholdEntry.setIndexNames(
    (0, "SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmThresholdOID"),
    (0, "SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmThresholdInstance"),
)
if mibBuilder.loadTexts:
    digitalAlarmThresholdEntry.setStatus("current")
_DigitalAlarmThresholdOID_Type = ObjectIdentifier
_DigitalAlarmThresholdOID_Object = MibTableColumn
digitalAlarmThresholdOID = _DigitalAlarmThresholdOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1, 1),
    _DigitalAlarmThresholdOID_Type()
)
digitalAlarmThresholdOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalAlarmThresholdOID.setStatus("current")
_DigitalAlarmThresholdInstance_Type = Unsigned32
_DigitalAlarmThresholdInstance_Object = MibTableColumn
digitalAlarmThresholdInstance = _DigitalAlarmThresholdInstance_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1, 2),
    _DigitalAlarmThresholdInstance_Type()
)
digitalAlarmThresholdInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalAlarmThresholdInstance.setStatus("current")
_DigitalAlarmCritHi_Type = Integer32
_DigitalAlarmCritHi_Object = MibTableColumn
digitalAlarmCritHi = _DigitalAlarmCritHi_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1, 3),
    _DigitalAlarmCritHi_Type()
)
digitalAlarmCritHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmCritHi.setStatus("current")
_DigitalAlarmMajHi_Type = Integer32
_DigitalAlarmMajHi_Object = MibTableColumn
digitalAlarmMajHi = _DigitalAlarmMajHi_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1, 4),
    _DigitalAlarmMajHi_Type()
)
digitalAlarmMajHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmMajHi.setStatus("current")
_DigitalAlarmMinHi_Type = Integer32
_DigitalAlarmMinHi_Object = MibTableColumn
digitalAlarmMinHi = _DigitalAlarmMinHi_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1, 5),
    _DigitalAlarmMinHi_Type()
)
digitalAlarmMinHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmMinHi.setStatus("current")
_DigitalAlarmMinLo_Type = Integer32
_DigitalAlarmMinLo_Object = MibTableColumn
digitalAlarmMinLo = _DigitalAlarmMinLo_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1, 6),
    _DigitalAlarmMinLo_Type()
)
digitalAlarmMinLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmMinLo.setStatus("current")
_DigitalAlarmMajLo_Type = Integer32
_DigitalAlarmMajLo_Object = MibTableColumn
digitalAlarmMajLo = _DigitalAlarmMajLo_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1, 7),
    _DigitalAlarmMajLo_Type()
)
digitalAlarmMajLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmMajLo.setStatus("current")
_DigitalAlarmCritLo_Type = Integer32
_DigitalAlarmCritLo_Object = MibTableColumn
digitalAlarmCritLo = _DigitalAlarmCritLo_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1, 8),
    _DigitalAlarmCritLo_Type()
)
digitalAlarmCritLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmCritLo.setStatus("current")
_DigitalAlarmHysterisis_Type = Integer32
_DigitalAlarmHysterisis_Object = MibTableColumn
digitalAlarmHysterisis = _DigitalAlarmHysterisis_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 2, 1, 1, 9),
    _DigitalAlarmHysterisis_Type()
)
digitalAlarmHysterisis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmHysterisis.setStatus("current")
_DigitalAlarmControl_ObjectIdentity = ObjectIdentity
digitalAlarmControl = _DigitalAlarmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3)
)
_DigitalAlarmControlTable_Object = MibTable
digitalAlarmControlTable = _DigitalAlarmControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    digitalAlarmControlTable.setStatus("current")
_DigitalAlarmControlEntry_Object = MibTableRow
digitalAlarmControlEntry = _DigitalAlarmControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1)
)
digitalAlarmControlEntry.setIndexNames(
    (0, "SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmControlOID"),
    (0, "SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmControlInstance"),
)
if mibBuilder.loadTexts:
    digitalAlarmControlEntry.setStatus("current")
_DigitalAlarmControlOID_Type = ObjectIdentifier
_DigitalAlarmControlOID_Object = MibTableColumn
digitalAlarmControlOID = _DigitalAlarmControlOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 1),
    _DigitalAlarmControlOID_Type()
)
digitalAlarmControlOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalAlarmControlOID.setStatus("current")
_DigitalAlarmControlInstance_Type = Unsigned32
_DigitalAlarmControlInstance_Object = MibTableColumn
digitalAlarmControlInstance = _DigitalAlarmControlInstance_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 2),
    _DigitalAlarmControlInstance_Type()
)
digitalAlarmControlInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalAlarmControlInstance.setStatus("current")
_DigitalAlarmResetCount_Type = HeResetValue
_DigitalAlarmResetCount_Object = MibTableColumn
digitalAlarmResetCount = _DigitalAlarmResetCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 3),
    _DigitalAlarmResetCount_Type()
)
digitalAlarmResetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmResetCount.setStatus("current")
_DigitalAlarmResetInitialTime_Type = HeResetValue
_DigitalAlarmResetInitialTime_Object = MibTableColumn
digitalAlarmResetInitialTime = _DigitalAlarmResetInitialTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 4),
    _DigitalAlarmResetInitialTime_Type()
)
digitalAlarmResetInitialTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmResetInitialTime.setStatus("current")
_DigitalAlarmResetLastTime_Type = HeResetValue
_DigitalAlarmResetLastTime_Object = MibTableColumn
digitalAlarmResetLastTime = _DigitalAlarmResetLastTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 5),
    _DigitalAlarmResetLastTime_Type()
)
digitalAlarmResetLastTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmResetLastTime.setStatus("current")


class _DigitalAlarmReporting_Type(Bits):
    """Custom type digitalAlarmReporting based on Bits"""
    namedValues = NamedValues(
        *(("localLogFile", 0),
          ("syslog", 1),
          ("snmpTrap", 2),
          ("snmpInform", 3),
          ("custom", 4),
          ("disable", 5))
    )

_DigitalAlarmReporting_Type.__name__ = "Bits"
_DigitalAlarmReporting_Object = MibTableColumn
digitalAlarmReporting = _DigitalAlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 6),
    _DigitalAlarmReporting_Type()
)
digitalAlarmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmReporting.setStatus("current")
_DigitalAlarmAck_Type = DigitalAlarmAckValue
_DigitalAlarmAck_Object = MibTableColumn
digitalAlarmAck = _DigitalAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 7),
    _DigitalAlarmAck_Type()
)
digitalAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmAck.setStatus("current")
_DigitalLocalLogMinAlarmLevel_Type = DigitalAlarmPriorityType
_DigitalLocalLogMinAlarmLevel_Object = MibTableColumn
digitalLocalLogMinAlarmLevel = _DigitalLocalLogMinAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 8),
    _DigitalLocalLogMinAlarmLevel_Type()
)
digitalLocalLogMinAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalLocalLogMinAlarmLevel.setStatus("current")
_DigitalSyslogMinAlarmLevel_Type = DigitalAlarmPriorityType
_DigitalSyslogMinAlarmLevel_Object = MibTableColumn
digitalSyslogMinAlarmLevel = _DigitalSyslogMinAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 9),
    _DigitalSyslogMinAlarmLevel_Type()
)
digitalSyslogMinAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalSyslogMinAlarmLevel.setStatus("current")
_DigitalSnmpTrapMinAlarmLevel_Type = DigitalAlarmPriorityType
_DigitalSnmpTrapMinAlarmLevel_Object = MibTableColumn
digitalSnmpTrapMinAlarmLevel = _DigitalSnmpTrapMinAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 10),
    _DigitalSnmpTrapMinAlarmLevel_Type()
)
digitalSnmpTrapMinAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalSnmpTrapMinAlarmLevel.setStatus("current")
_DigitalSnmpInformMinAlarmLevel_Type = DigitalAlarmPriorityType
_DigitalSnmpInformMinAlarmLevel_Object = MibTableColumn
digitalSnmpInformMinAlarmLevel = _DigitalSnmpInformMinAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 11),
    _DigitalSnmpInformMinAlarmLevel_Type()
)
digitalSnmpInformMinAlarmLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalSnmpInformMinAlarmLevel.setStatus("current")
_DigitalCustomMinAlarmLevel_Type = DigitalAlarmPriorityType
_DigitalCustomMinAlarmLevel_Object = MibTableColumn
digitalCustomMinAlarmLevel = _DigitalCustomMinAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 12),
    _DigitalCustomMinAlarmLevel_Type()
)
digitalCustomMinAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalCustomMinAlarmLevel.setStatus("current")
_DigitalLocalLogThrottle_Type = Unsigned32
_DigitalLocalLogThrottle_Object = MibTableColumn
digitalLocalLogThrottle = _DigitalLocalLogThrottle_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 13),
    _DigitalLocalLogThrottle_Type()
)
digitalLocalLogThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalLocalLogThrottle.setStatus("current")
_DigitalSyslogThrottle_Type = Unsigned32
_DigitalSyslogThrottle_Object = MibTableColumn
digitalSyslogThrottle = _DigitalSyslogThrottle_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 14),
    _DigitalSyslogThrottle_Type()
)
digitalSyslogThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalSyslogThrottle.setStatus("current")
_DigitalSnmpTrapThrottle_Type = Unsigned32
_DigitalSnmpTrapThrottle_Object = MibTableColumn
digitalSnmpTrapThrottle = _DigitalSnmpTrapThrottle_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 15),
    _DigitalSnmpTrapThrottle_Type()
)
digitalSnmpTrapThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalSnmpTrapThrottle.setStatus("current")
_DigitalSnmpInformThrottle_Type = Unsigned32
_DigitalSnmpInformThrottle_Object = MibTableColumn
digitalSnmpInformThrottle = _DigitalSnmpInformThrottle_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 16),
    _DigitalSnmpInformThrottle_Type()
)
digitalSnmpInformThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalSnmpInformThrottle.setStatus("current")
_DigitalCustomThrottle_Type = Unsigned32
_DigitalCustomThrottle_Object = MibTableColumn
digitalCustomThrottle = _DigitalCustomThrottle_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 17),
    _DigitalCustomThrottle_Type()
)
digitalCustomThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalCustomThrottle.setStatus("current")
_DigitalAlarmTrapRegenerate_Type = DigitalTrapRegenerate
_DigitalAlarmTrapRegenerate_Object = MibTableColumn
digitalAlarmTrapRegenerate = _DigitalAlarmTrapRegenerate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 18),
    _DigitalAlarmTrapRegenerate_Type()
)
digitalAlarmTrapRegenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalAlarmTrapRegenerate.setStatus("current")
_DigitalActiveAlarmClear_Type = HeResetValue
_DigitalActiveAlarmClear_Object = MibTableColumn
digitalActiveAlarmClear = _DigitalActiveAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 3, 1, 1, 19),
    _DigitalActiveAlarmClear_Type()
)
digitalActiveAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalActiveAlarmClear.setStatus("current")
_DigitalAlarmLog_ObjectIdentity = ObjectIdentity
digitalAlarmLog = _DigitalAlarmLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4)
)
_DigitalAlarmLogTable_Object = MibTable
digitalAlarmLogTable = _DigitalAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    digitalAlarmLogTable.setStatus("current")
_DigitalAlarmLogEntry_Object = MibTableRow
digitalAlarmLogEntry = _DigitalAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1)
)
digitalAlarmLogEntry.setIndexNames(
    (0, "SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogIndex"),
)
if mibBuilder.loadTexts:
    digitalAlarmLogEntry.setStatus("current")


class _DigitalAlarmLogIndex_Type(Integer32):
    """Custom type digitalAlarmLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DigitalAlarmLogIndex_Type.__name__ = "Integer32"
_DigitalAlarmLogIndex_Object = MibTableColumn
digitalAlarmLogIndex = _DigitalAlarmLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 1),
    _DigitalAlarmLogIndex_Type()
)
digitalAlarmLogIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    digitalAlarmLogIndex.setStatus("current")
_DigitalAlarmLogOID_Type = ObjectIdentifier
_DigitalAlarmLogOID_Object = MibTableColumn
digitalAlarmLogOID = _DigitalAlarmLogOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 2),
    _DigitalAlarmLogOID_Type()
)
digitalAlarmLogOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogOID.setStatus("current")
_DigitalAlarmLogInstance_Type = Unsigned32
_DigitalAlarmLogInstance_Object = MibTableColumn
digitalAlarmLogInstance = _DigitalAlarmLogInstance_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 3),
    _DigitalAlarmLogInstance_Type()
)
digitalAlarmLogInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogInstance.setStatus("current")
_DigitalAlarmLogEntProductID_Type = ObjectIdentifier
_DigitalAlarmLogEntProductID_Object = MibTableColumn
digitalAlarmLogEntProductID = _DigitalAlarmLogEntProductID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 4),
    _DigitalAlarmLogEntProductID_Type()
)
digitalAlarmLogEntProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogEntProductID.setStatus("current")
_DigitalAlarmLogEntDeviceType_Type = SnmpAdminString
_DigitalAlarmLogEntDeviceType_Object = MibTableColumn
digitalAlarmLogEntDeviceType = _DigitalAlarmLogEntDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 5),
    _DigitalAlarmLogEntDeviceType_Type()
)
digitalAlarmLogEntDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogEntDeviceType.setStatus("current")


class _DigitalAlarmLogEntAlias_Type(SnmpAdminString):
    """Custom type digitalAlarmLogEntAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DigitalAlarmLogEntAlias_Type.__name__ = "SnmpAdminString"
_DigitalAlarmLogEntAlias_Object = MibTableColumn
digitalAlarmLogEntAlias = _DigitalAlarmLogEntAlias_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 6),
    _DigitalAlarmLogEntAlias_Type()
)
digitalAlarmLogEntAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogEntAlias.setStatus("current")
_DigitalAlarmLogComponent_Type = DigitalAlarmComponentType
_DigitalAlarmLogComponent_Object = MibTableColumn
digitalAlarmLogComponent = _DigitalAlarmLogComponent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 7),
    _DigitalAlarmLogComponent_Type()
)
digitalAlarmLogComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogComponent.setStatus("current")
_DigitalAlarmLogCategory_Type = DigitalAlarmCategoryType
_DigitalAlarmLogCategory_Object = MibTableColumn
digitalAlarmLogCategory = _DigitalAlarmLogCategory_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 8),
    _DigitalAlarmLogCategory_Type()
)
digitalAlarmLogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogCategory.setStatus("current")
_DigitalAlarmLogPriority_Type = DigitalAlarmPriorityType
_DigitalAlarmLogPriority_Object = MibTableColumn
digitalAlarmLogPriority = _DigitalAlarmLogPriority_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 9),
    _DigitalAlarmLogPriority_Type()
)
digitalAlarmLogPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogPriority.setStatus("current")
_DigitalAlarmLogState_Type = DigitalAlarmStateType
_DigitalAlarmLogState_Object = MibTableColumn
digitalAlarmLogState = _DigitalAlarmLogState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 10),
    _DigitalAlarmLogState_Type()
)
digitalAlarmLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogState.setStatus("current")
_DigitalAlarmLogValueLastChange_Type = Integer32
_DigitalAlarmLogValueLastChange_Object = MibTableColumn
digitalAlarmLogValueLastChange = _DigitalAlarmLogValueLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 11),
    _DigitalAlarmLogValueLastChange_Type()
)
digitalAlarmLogValueLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogValueLastChange.setStatus("current")
_DigitalAlarmLogText_Type = DisplayString
_DigitalAlarmLogText_Object = MibTableColumn
digitalAlarmLogText = _DigitalAlarmLogText_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 12),
    _DigitalAlarmLogText_Type()
)
digitalAlarmLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogText.setStatus("current")


class _DigitalAlarmLogAlias_Type(SnmpAdminString):
    """Custom type digitalAlarmLogAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DigitalAlarmLogAlias_Type.__name__ = "SnmpAdminString"
_DigitalAlarmLogAlias_Object = MibTableColumn
digitalAlarmLogAlias = _DigitalAlarmLogAlias_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 13),
    _DigitalAlarmLogAlias_Type()
)
digitalAlarmLogAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogAlias.setStatus("current")
_DigitalAlarmLogLastTime_Type = DateAndTime
_DigitalAlarmLogLastTime_Object = MibTableColumn
digitalAlarmLogLastTime = _DigitalAlarmLogLastTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 1, 4, 1, 1, 14),
    _DigitalAlarmLogLastTime_Type()
)
digitalAlarmLogLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmLogLastTime.setStatus("current")
_DigitalAlarmConformance_ObjectIdentity = ObjectIdentity
digitalAlarmConformance = _DigitalAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 2)
)
_DigitalAlarmCompliances_ObjectIdentity = ObjectIdentity
digitalAlarmCompliances = _DigitalAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 2, 1)
)
_DigitalAlarmGroups_ObjectIdentity = ObjectIdentity
digitalAlarmGroups = _DigitalAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 2, 2)
)

# Managed Objects groups

digitalAlarmStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 2, 2, 1)
)
digitalAlarmStatusGroup.setObjects(
      *(("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmEntAlias"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmAlias"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmCategory"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmComponent"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmCount"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmEntDeviceType"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmEntProductID"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmInitialTime"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLastTime"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmPriority"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmState"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmValueLastChange"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmVendorText"))
)
if mibBuilder.loadTexts:
    digitalAlarmStatusGroup.setStatus("current")

digitalAlarmThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 2, 2, 2)
)
digitalAlarmThresholdGroup.setObjects(
      *(("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmCritLo"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmCritHi"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmHysterisis"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmMajHi"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmMajLo"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmMinHi"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmMinLo"))
)
if mibBuilder.loadTexts:
    digitalAlarmThresholdGroup.setStatus("current")

digitalAlarmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 2, 2, 3)
)
digitalAlarmConfigGroup.setObjects(
      *(("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmAck"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmReporting"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmResetCount"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmResetInitialTime"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmResetLastTime"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalCustomMinAlarmLevel"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalCustomThrottle"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalActiveAlarmClear"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmTrapRegenerate"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalLocalLogThrottle"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalLocalLogMinAlarmLevel"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalSnmpInformThrottle"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalSnmpTrapMinAlarmLevel"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalSnmpTrapThrottle"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalSyslogMinAlarmLevel"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalSyslogThrottle"))
)
if mibBuilder.loadTexts:
    digitalAlarmConfigGroup.setStatus("current")

digitalAlarmLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 2, 2, 4)
)
digitalAlarmLogGroup.setObjects(
      *(("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogAlias"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogCategory"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogComponent"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogEntAlias"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogEntDeviceType"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogEntProductID"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogIndex"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogInstance"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogLastTime"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogOID"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogPriority"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogState"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogText"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogValueLastChange"))
)
if mibBuilder.loadTexts:
    digitalAlarmLogGroup.setStatus("current")


# Notification objects

digitalCommonAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0, 6)
)
digitalCommonAlarmEvent.setObjects(
      *(("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogIndex"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogOID"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogInstance"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmEntProductID"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmEntDeviceType"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmEntAlias"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmComponent"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmCategory"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmPriority"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmState"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmValueLastChange"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmVendorText"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmAlias"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLastTime"))
)
if mibBuilder.loadTexts:
    digitalCommonAlarmEvent.setStatus(
        "current"
    )

digitalCommonAlarmRegen = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0, 7)
)
digitalCommonAlarmRegen.setObjects(
      *(("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogIndex"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogOID"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogInstance"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmEntProductID"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmEntDeviceType"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmEntAlias"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmComponent"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmCategory"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmPriority"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmState"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmValueLastChange"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmVendorText"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmAlias"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLastTime"))
)
if mibBuilder.loadTexts:
    digitalCommonAlarmRegen.setStatus(
        "current"
    )


# Notifications groups

digitalAlarmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 2, 2, 5)
)
digitalAlarmNotificationGroup.setObjects(
      *(("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalCommonAlarmEvent"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalCommonAlarmRegen"))
)
if mibBuilder.loadTexts:
    digitalAlarmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

digitalAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3, 1, 2, 1, 1)
)
digitalAlarmCompliance.setObjects(
      *(("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmConfigGroup"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmLogGroup"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmNotificationGroup"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmStatusGroup"),
        ("SCTE-HMS-DIGITAL-ALARM-MIB", "digitalAlarmThresholdGroup"))
)
if mibBuilder.loadTexts:
    digitalAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-DIGITAL-ALARM-MIB",
    **{"DigitalAlarmComponentType": DigitalAlarmComponentType,
       "DigitalAlarmCategoryType": DigitalAlarmCategoryType,
       "DigitalAlarmPriorityType": DigitalAlarmPriorityType,
       "DigitalAlarmStateType": DigitalAlarmStateType,
       "DigitalTrapRegenerate": DigitalTrapRegenerate,
       "DigitalAlarmAckValue": DigitalAlarmAckValue,
       "digitalCommonAlarmEvent": digitalCommonAlarmEvent,
       "digitalCommonAlarmRegen": digitalCommonAlarmRegen,
       "heDigitalAlarmMIB": heDigitalAlarmMIB,
       "digitalAlarmMIBObjects": digitalAlarmMIBObjects,
       "digitalAlarms": digitalAlarms,
       "digitalAlarmTable": digitalAlarmTable,
       "digitalAlarmEntry": digitalAlarmEntry,
       "digitalAlarmOID": digitalAlarmOID,
       "digitalAlarmInstance": digitalAlarmInstance,
       "digitalAlarmEntProductID": digitalAlarmEntProductID,
       "digitalAlarmEntDeviceType": digitalAlarmEntDeviceType,
       "digitalAlarmEntAlias": digitalAlarmEntAlias,
       "digitalAlarmComponent": digitalAlarmComponent,
       "digitalAlarmCategory": digitalAlarmCategory,
       "digitalAlarmPriority": digitalAlarmPriority,
       "digitalAlarmState": digitalAlarmState,
       "digitalAlarmValueLastChange": digitalAlarmValueLastChange,
       "digitalAlarmVendorText": digitalAlarmVendorText,
       "digitalAlarmAlias": digitalAlarmAlias,
       "digitalAlarmInitialTime": digitalAlarmInitialTime,
       "digitalAlarmLastTime": digitalAlarmLastTime,
       "digitalAlarmCount": digitalAlarmCount,
       "digitalAlarmThresholds": digitalAlarmThresholds,
       "digitalAlarmThresholdTable": digitalAlarmThresholdTable,
       "digitalAlarmThresholdEntry": digitalAlarmThresholdEntry,
       "digitalAlarmThresholdOID": digitalAlarmThresholdOID,
       "digitalAlarmThresholdInstance": digitalAlarmThresholdInstance,
       "digitalAlarmCritHi": digitalAlarmCritHi,
       "digitalAlarmMajHi": digitalAlarmMajHi,
       "digitalAlarmMinHi": digitalAlarmMinHi,
       "digitalAlarmMinLo": digitalAlarmMinLo,
       "digitalAlarmMajLo": digitalAlarmMajLo,
       "digitalAlarmCritLo": digitalAlarmCritLo,
       "digitalAlarmHysterisis": digitalAlarmHysterisis,
       "digitalAlarmControl": digitalAlarmControl,
       "digitalAlarmControlTable": digitalAlarmControlTable,
       "digitalAlarmControlEntry": digitalAlarmControlEntry,
       "digitalAlarmControlOID": digitalAlarmControlOID,
       "digitalAlarmControlInstance": digitalAlarmControlInstance,
       "digitalAlarmResetCount": digitalAlarmResetCount,
       "digitalAlarmResetInitialTime": digitalAlarmResetInitialTime,
       "digitalAlarmResetLastTime": digitalAlarmResetLastTime,
       "digitalAlarmReporting": digitalAlarmReporting,
       "digitalAlarmAck": digitalAlarmAck,
       "digitalLocalLogMinAlarmLevel": digitalLocalLogMinAlarmLevel,
       "digitalSyslogMinAlarmLevel": digitalSyslogMinAlarmLevel,
       "digitalSnmpTrapMinAlarmLevel": digitalSnmpTrapMinAlarmLevel,
       "digitalSnmpInformMinAlarmLevel": digitalSnmpInformMinAlarmLevel,
       "digitalCustomMinAlarmLevel": digitalCustomMinAlarmLevel,
       "digitalLocalLogThrottle": digitalLocalLogThrottle,
       "digitalSyslogThrottle": digitalSyslogThrottle,
       "digitalSnmpTrapThrottle": digitalSnmpTrapThrottle,
       "digitalSnmpInformThrottle": digitalSnmpInformThrottle,
       "digitalCustomThrottle": digitalCustomThrottle,
       "digitalAlarmTrapRegenerate": digitalAlarmTrapRegenerate,
       "digitalActiveAlarmClear": digitalActiveAlarmClear,
       "digitalAlarmLog": digitalAlarmLog,
       "digitalAlarmLogTable": digitalAlarmLogTable,
       "digitalAlarmLogEntry": digitalAlarmLogEntry,
       "digitalAlarmLogIndex": digitalAlarmLogIndex,
       "digitalAlarmLogOID": digitalAlarmLogOID,
       "digitalAlarmLogInstance": digitalAlarmLogInstance,
       "digitalAlarmLogEntProductID": digitalAlarmLogEntProductID,
       "digitalAlarmLogEntDeviceType": digitalAlarmLogEntDeviceType,
       "digitalAlarmLogEntAlias": digitalAlarmLogEntAlias,
       "digitalAlarmLogComponent": digitalAlarmLogComponent,
       "digitalAlarmLogCategory": digitalAlarmLogCategory,
       "digitalAlarmLogPriority": digitalAlarmLogPriority,
       "digitalAlarmLogState": digitalAlarmLogState,
       "digitalAlarmLogValueLastChange": digitalAlarmLogValueLastChange,
       "digitalAlarmLogText": digitalAlarmLogText,
       "digitalAlarmLogAlias": digitalAlarmLogAlias,
       "digitalAlarmLogLastTime": digitalAlarmLogLastTime,
       "digitalAlarmConformance": digitalAlarmConformance,
       "digitalAlarmCompliances": digitalAlarmCompliances,
       "digitalAlarmCompliance": digitalAlarmCompliance,
       "digitalAlarmGroups": digitalAlarmGroups,
       "digitalAlarmStatusGroup": digitalAlarmStatusGroup,
       "digitalAlarmThresholdGroup": digitalAlarmThresholdGroup,
       "digitalAlarmConfigGroup": digitalAlarmConfigGroup,
       "digitalAlarmLogGroup": digitalAlarmLogGroup,
       "digitalAlarmNotificationGroup": digitalAlarmNotificationGroup}
)
