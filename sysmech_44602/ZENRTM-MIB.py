# SNMP MIB module (ZENRTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/sysmech_44602/ZENRTM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:51:04 2025
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

(sysmech,) = mibBuilder.importSymbols(
    "SYSMECH-MIB",
    "sysmech")


# MODULE-IDENTITY

zenRTM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44602, 1)
)
if mibBuilder.loadTexts:
    zenRTM.setRevisions(
        ("2014-09-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ZrtmonSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("cleared", 5))
    )



class ZrtmonAlarmType(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("communicationsAlarm", 2),
          ("qualityOfServiceAlarm", 3),
          ("processingErrorAlarm", 4),
          ("equipmentAlarm", 5),
          ("environmentalAlarm", 6),
          ("integrityViolation", 7),
          ("operationalViolation", 8),
          ("physicalViolation", 9),
          ("securityServiceOrMechanismViolation", 10),
          ("timeDomainViolation", 11))
    )



class ZrtmonId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )



# MIB Managed Objects in the order of their OIDs

_ZenRTMTraps_ObjectIdentity = ObjectIdentity
zenRTMTraps = _ZenRTMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44602, 1, 0)
)
_ZenRTMTrapInfo_ObjectIdentity = ObjectIdentity
zenRTMTrapInfo = _ZenRTMTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1)
)
_ZRTMManagedObjectName_Type = DisplayString
_ZRTMManagedObjectName_Object = MibScalar
zRTMManagedObjectName = _ZRTMManagedObjectName_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 1),
    _ZRTMManagedObjectName_Type()
)
zRTMManagedObjectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zRTMManagedObjectName.setStatus("current")
_ZRTMManagedObjectId_Type = ZrtmonId
_ZRTMManagedObjectId_Object = MibScalar
zRTMManagedObjectId = _ZRTMManagedObjectId_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 2),
    _ZRTMManagedObjectId_Type()
)
zRTMManagedObjectId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zRTMManagedObjectId.setStatus("current")
_ZRTMManagedObjectType_Type = DisplayString
_ZRTMManagedObjectType_Object = MibScalar
zRTMManagedObjectType = _ZRTMManagedObjectType_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 3),
    _ZRTMManagedObjectType_Type()
)
zRTMManagedObjectType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zRTMManagedObjectType.setStatus("current")
_ZRTMAlarmNotifId_Type = DisplayString
_ZRTMAlarmNotifId_Object = MibScalar
zRTMAlarmNotifId = _ZRTMAlarmNotifId_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 4),
    _ZRTMAlarmNotifId_Type()
)
zRTMAlarmNotifId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zRTMAlarmNotifId.setStatus("current")
_ZRTMAlarmType_Type = ZrtmonAlarmType
_ZRTMAlarmType_Object = MibScalar
zRTMAlarmType = _ZRTMAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 5),
    _ZRTMAlarmType_Type()
)
zRTMAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zRTMAlarmType.setStatus("current")
_ZRTMProbableCause_Type = DisplayString
_ZRTMProbableCause_Object = MibScalar
zRTMProbableCause = _ZRTMProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 6),
    _ZRTMProbableCause_Type()
)
zRTMProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zRTMProbableCause.setStatus("current")
_ZRTMSeverity_Type = ZrtmonSeverity
_ZRTMSeverity_Object = MibScalar
zRTMSeverity = _ZRTMSeverity_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 7),
    _ZRTMSeverity_Type()
)
zRTMSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zRTMSeverity.setStatus("current")
_ZRTMAdditionalText_Type = DisplayString
_ZRTMAdditionalText_Object = MibScalar
zRTMAdditionalText = _ZRTMAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 8),
    _ZRTMAdditionalText_Type()
)
zRTMAdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zRTMAdditionalText.setStatus("current")
_ZRTMAlarmDateAndTime_Type = DateAndTime
_ZRTMAlarmDateAndTime_Object = MibScalar
zRTMAlarmDateAndTime = _ZRTMAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 9),
    _ZRTMAlarmDateAndTime_Type()
)
zRTMAlarmDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zRTMAlarmDateAndTime.setStatus("current")

# Managed Objects groups


# Notification objects

zenRTMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44602, 1, 0, 1)
)
zenRTMAlarm.setObjects(
      *(("ZENRTM-MIB", "zRTMAlarmNotifId"),
        ("ZENRTM-MIB", "zRTMManagedObjectName"),
        ("ZENRTM-MIB", "zRTMManagedObjectId"),
        ("ZENRTM-MIB", "zRTMManagedObjectType"),
        ("ZENRTM-MIB", "zRTMAlarmType"),
        ("ZENRTM-MIB", "zRTMProbableCause"),
        ("ZENRTM-MIB", "zRTMSeverity"),
        ("ZENRTM-MIB", "zRTMAdditionalText"),
        ("ZENRTM-MIB", "zRTMAlarmDateAndTime"))
)
if mibBuilder.loadTexts:
    zenRTMAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZENRTM-MIB",
    **{"ZrtmonSeverity": ZrtmonSeverity,
       "ZrtmonAlarmType": ZrtmonAlarmType,
       "ZrtmonId": ZrtmonId,
       "zenRTM": zenRTM,
       "zenRTMTraps": zenRTMTraps,
       "zenRTMAlarm": zenRTMAlarm,
       "zenRTMTrapInfo": zenRTMTrapInfo,
       "zRTMManagedObjectName": zRTMManagedObjectName,
       "zRTMManagedObjectId": zRTMManagedObjectId,
       "zRTMManagedObjectType": zRTMManagedObjectType,
       "zRTMAlarmNotifId": zRTMAlarmNotifId,
       "zRTMAlarmType": zRTMAlarmType,
       "zRTMProbableCause": zRTMProbableCause,
       "zRTMSeverity": zRTMSeverity,
       "zRTMAdditionalText": zRTMAdditionalText,
       "zRTMAlarmDateAndTime": zRTMAlarmDateAndTime}
)
