# SNMP MIB module (INFOMICRO-ENTERPRISE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/infomicro_50291/INFOMICRO-ENTERPRISE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:21 2025
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

infomicro = ModuleIdentity(
    (1, 2, 16, 724, 1578918, 12)
)
if mibBuilder.loadTexts:
    infomicro.setRevisions(
        ("2017-07-03 11:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MemberBody_ObjectIdentity = ObjectIdentity
memberBody = _MemberBody_ObjectIdentity(
    (1, 2)
)
_Es_ObjectIdentity = ObjectIdentity
es = _Es_ObjectIdentity(
    (1, 2, 16)
)
_EsNational_ObjectIdentity = ObjectIdentity
esNational = _EsNational_ObjectIdentity(
    (1, 2, 16, 724)
)
_DataConnection_ObjectIdentity = ObjectIdentity
dataConnection = _DataConnection_ObjectIdentity(
    (1, 2, 16, 724, 1578918)
)
_InfomicroEnterpriseMIBConformance_ObjectIdentity = ObjectIdentity
infomicroEnterpriseMIBConformance = _InfomicroEnterpriseMIBConformance_ObjectIdentity(
    (1, 2, 16, 724, 1578918, 12, 0)
)
_InfomicroInfo_ObjectIdentity = ObjectIdentity
infomicroInfo = _InfomicroInfo_ObjectIdentity(
    (1, 2, 16, 724, 1578918, 12, 1)
)
_InfomicroInfoVersion_Type = DisplayString
_InfomicroInfoVersion_Object = MibScalar
infomicroInfoVersion = _InfomicroInfoVersion_Object(
    (1, 2, 16, 724, 1578918, 12, 1, 1),
    _InfomicroInfoVersion_Type()
)
infomicroInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infomicroInfoVersion.setStatus("current")
_DataConnectionTraps_ObjectIdentity = ObjectIdentity
dataConnectionTraps = _DataConnectionTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50291)
)
_InfomicroCR_ObjectIdentity = ObjectIdentity
infomicroCR = _InfomicroCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50291, 12)
)
_InfomicroTraps_ObjectIdentity = ObjectIdentity
infomicroTraps = _InfomicroTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2)
)
_AlarmTrapsPrefix_ObjectIdentity = ObjectIdentity
alarmTrapsPrefix = _AlarmTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0)
)


class _AlarmTrapDisplayName_Type(DisplayString):
    """Custom type alarmTrapDisplayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlarmTrapDisplayName_Type.__name__ = "DisplayString"
_AlarmTrapDisplayName_Object = MibScalar
alarmTrapDisplayName = _AlarmTrapDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 2),
    _AlarmTrapDisplayName_Type()
)
alarmTrapDisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapDisplayName.setStatus("current")
_AlarmTrapAlarmOID_Type = ObjectIdentifier
_AlarmTrapAlarmOID_Object = MibScalar
alarmTrapAlarmOID = _AlarmTrapAlarmOID_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 3),
    _AlarmTrapAlarmOID_Type()
)
alarmTrapAlarmOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapAlarmOID.setStatus("current")
_AlarmTrapResourceID_Type = ObjectIdentifier
_AlarmTrapResourceID_Object = MibScalar
alarmTrapResourceID = _AlarmTrapResourceID_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 4),
    _AlarmTrapResourceID_Type()
)
alarmTrapResourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapResourceID.setStatus("current")


class _AlarmTrapSeverity_Type(DisplayString):
    """Custom type alarmTrapSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_AlarmTrapSeverity_Type.__name__ = "DisplayString"
_AlarmTrapSeverity_Object = MibScalar
alarmTrapSeverity = _AlarmTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 5),
    _AlarmTrapSeverity_Type()
)
alarmTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapSeverity.setStatus("current")


class _AlarmTrapDescription_Type(DisplayString):
    """Custom type alarmTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_AlarmTrapDescription_Type.__name__ = "DisplayString"
_AlarmTrapDescription_Object = MibScalar
alarmTrapDescription = _AlarmTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 6),
    _AlarmTrapDescription_Type()
)
alarmTrapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapDescription.setStatus("current")


class _AlarmTrapDetails_Type(DisplayString):
    """Custom type alarmTrapDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_AlarmTrapDetails_Type.__name__ = "DisplayString"
_AlarmTrapDetails_Object = MibScalar
alarmTrapDetails = _AlarmTrapDetails_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 7),
    _AlarmTrapDetails_Type()
)
alarmTrapDetails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapDetails.setStatus("current")


class _AlarmTrapCause_Type(DisplayString):
    """Custom type alarmTrapCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_AlarmTrapCause_Type.__name__ = "DisplayString"
_AlarmTrapCause_Object = MibScalar
alarmTrapCause = _AlarmTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 8),
    _AlarmTrapCause_Type()
)
alarmTrapCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapCause.setStatus("current")


class _AlarmTrapEffect_Type(DisplayString):
    """Custom type alarmTrapEffect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_AlarmTrapEffect_Type.__name__ = "DisplayString"
_AlarmTrapEffect_Object = MibScalar
alarmTrapEffect = _AlarmTrapEffect_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 9),
    _AlarmTrapEffect_Type()
)
alarmTrapEffect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapEffect.setStatus("current")


class _AlarmTrapAction_Type(DisplayString):
    """Custom type alarmTrapAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_AlarmTrapAction_Type.__name__ = "DisplayString"
_AlarmTrapAction_Object = MibScalar
alarmTrapAction = _AlarmTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 10),
    _AlarmTrapAction_Type()
)
alarmTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapAction.setStatus("current")


class _AlarmTrapHostname_Type(DisplayString):
    """Custom type alarmTrapHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_AlarmTrapHostname_Type.__name__ = "DisplayString"
_AlarmTrapHostname_Object = MibScalar
alarmTrapHostname = _AlarmTrapHostname_Object(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 12),
    _AlarmTrapHostname_Type()
)
alarmTrapHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapHostname.setStatus("current")

# Managed Objects groups

alarmTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 11)
)
alarmTrapGroup.setObjects(
      *(("INFOMICRO-ENTERPRISE-MIB", "infomicroInfoVersion"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapDisplayName"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapAlarmOID"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapResourceID"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapSeverity"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapDescription"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapDetails"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapCause"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapEffect"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapAction"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapHostname"))
)
if mibBuilder.loadTexts:
    alarmTrapGroup.setStatus("current")


# Notification objects

alarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 0, 1)
)
alarmTrap.setObjects(
      *(("INFOMICRO-ENTERPRISE-MIB", "alarmTrapDisplayName"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapAlarmOID"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapResourceID"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapSeverity"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapDescription"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapDetails"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapCause"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapEffect"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapAction"),
        ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapHostname"))
)
if mibBuilder.loadTexts:
    alarmTrap.setStatus(
        "current"
    )


# Notifications groups

alarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 50291, 12, 2, 1)
)
alarmGroup.setObjects(
    ("INFOMICRO-ENTERPRISE-MIB", "alarmTrap")
)
if mibBuilder.loadTexts:
    alarmGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

infomicroEnterpriseMIBCompliance = ModuleCompliance(
    (1, 2, 16, 724, 1578918, 12, 0, 1)
)
infomicroEnterpriseMIBCompliance.setObjects(
    ("INFOMICRO-ENTERPRISE-MIB", "alarmTrapGroup")
)
if mibBuilder.loadTexts:
    infomicroEnterpriseMIBCompliance.setStatus(
        "current"
    )

infomicroEnterpriseMIBCompliance2 = ModuleCompliance(
    (1, 2, 16, 724, 1578918, 12, 0, 2)
)
infomicroEnterpriseMIBCompliance2.setObjects(
    ("INFOMICRO-ENTERPRISE-MIB", "alarmGroup")
)
if mibBuilder.loadTexts:
    infomicroEnterpriseMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFOMICRO-ENTERPRISE-MIB",
    **{"memberBody": memberBody,
       "es": es,
       "esNational": esNational,
       "dataConnection": dataConnection,
       "infomicro": infomicro,
       "infomicroEnterpriseMIBConformance": infomicroEnterpriseMIBConformance,
       "infomicroEnterpriseMIBCompliance": infomicroEnterpriseMIBCompliance,
       "infomicroEnterpriseMIBCompliance2": infomicroEnterpriseMIBCompliance2,
       "infomicroInfo": infomicroInfo,
       "infomicroInfoVersion": infomicroInfoVersion,
       "dataConnectionTraps": dataConnectionTraps,
       "infomicroCR": infomicroCR,
       "infomicroTraps": infomicroTraps,
       "alarmTrapsPrefix": alarmTrapsPrefix,
       "alarmTrap": alarmTrap,
       "alarmTrapDisplayName": alarmTrapDisplayName,
       "alarmTrapAlarmOID": alarmTrapAlarmOID,
       "alarmTrapResourceID": alarmTrapResourceID,
       "alarmTrapSeverity": alarmTrapSeverity,
       "alarmTrapDescription": alarmTrapDescription,
       "alarmTrapDetails": alarmTrapDetails,
       "alarmTrapCause": alarmTrapCause,
       "alarmTrapEffect": alarmTrapEffect,
       "alarmTrapAction": alarmTrapAction,
       "alarmTrapGroup": alarmTrapGroup,
       "alarmTrapHostname": alarmTrapHostname,
       "alarmGroup": alarmGroup}
)
