# SNMP MIB module (MMS-10GEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/10gen_41138/MMS-10GEN-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:27:17 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mms_ObjectIdentity = ObjectIdentity
mms = _Mms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41138)
)
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41138, 1)
)
_ServerMIBObjects_ObjectIdentity = ObjectIdentity
serverMIBObjects = _ServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1)
)
_MmsAlertObject_ObjectIdentity = ObjectIdentity
mmsAlertObject = _MmsAlertObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1)
)


class _MmsAlertId_Type(DisplayString):
    """Custom type mmsAlertId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MmsAlertId_Type.__name__ = "DisplayString"
_MmsAlertId_Object = MibScalar
mmsAlertId = _MmsAlertId_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 1),
    _MmsAlertId_Type()
)
mmsAlertId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertId.setStatus("current")


class _MmsAlertGroupName_Type(DisplayString):
    """Custom type mmsAlertGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MmsAlertGroupName_Type.__name__ = "DisplayString"
_MmsAlertGroupName_Object = MibScalar
mmsAlertGroupName = _MmsAlertGroupName_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 2),
    _MmsAlertGroupName_Type()
)
mmsAlertGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertGroupName.setStatus("current")


class _MmsAlertHostId_Type(DisplayString):
    """Custom type mmsAlertHostId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MmsAlertHostId_Type.__name__ = "DisplayString"
_MmsAlertHostId_Object = MibScalar
mmsAlertHostId = _MmsAlertHostId_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 3),
    _MmsAlertHostId_Type()
)
mmsAlertHostId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertHostId.setStatus("current")


class _MmsAlertHostAndPort_Type(DisplayString):
    """Custom type mmsAlertHostAndPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MmsAlertHostAndPort_Type.__name__ = "DisplayString"
_MmsAlertHostAndPort_Object = MibScalar
mmsAlertHostAndPort = _MmsAlertHostAndPort_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 4),
    _MmsAlertHostAndPort_Type()
)
mmsAlertHostAndPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertHostAndPort.setStatus("current")


class _MmsAlertStatus_Type(Integer32):
    """Custom type mmsAlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("new", 1),
          ("reminder", 2),
          ("clear", 3))
    )


_MmsAlertStatus_Type.__name__ = "Integer32"
_MmsAlertStatus_Object = MibScalar
mmsAlertStatus = _MmsAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 5),
    _MmsAlertStatus_Type()
)
mmsAlertStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertStatus.setStatus("current")


class _MmsAlertUrl_Type(DisplayString):
    """Custom type mmsAlertUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MmsAlertUrl_Type.__name__ = "DisplayString"
_MmsAlertUrl_Object = MibScalar
mmsAlertUrl = _MmsAlertUrl_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 6),
    _MmsAlertUrl_Type()
)
mmsAlertUrl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertUrl.setStatus("current")


class _MmsAlertMetricName_Type(DisplayString):
    """Custom type mmsAlertMetricName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MmsAlertMetricName_Type.__name__ = "DisplayString"
_MmsAlertMetricName_Object = MibScalar
mmsAlertMetricName = _MmsAlertMetricName_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 7),
    _MmsAlertMetricName_Type()
)
mmsAlertMetricName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertMetricName.setStatus("current")


class _MmsAlertMetricThreshold_Type(DisplayString):
    """Custom type mmsAlertMetricThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MmsAlertMetricThreshold_Type.__name__ = "DisplayString"
_MmsAlertMetricThreshold_Object = MibScalar
mmsAlertMetricThreshold = _MmsAlertMetricThreshold_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 8),
    _MmsAlertMetricThreshold_Type()
)
mmsAlertMetricThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertMetricThreshold.setStatus("current")


class _MmsAlertMetricValue_Type(DisplayString):
    """Custom type mmsAlertMetricValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MmsAlertMetricValue_Type.__name__ = "DisplayString"
_MmsAlertMetricValue_Object = MibScalar
mmsAlertMetricValue = _MmsAlertMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 9),
    _MmsAlertMetricValue_Type()
)
mmsAlertMetricValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertMetricValue.setStatus("current")


class _MmsAlertReplSetName_Type(DisplayString):
    """Custom type mmsAlertReplSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MmsAlertReplSetName_Type.__name__ = "DisplayString"
_MmsAlertReplSetName_Object = MibScalar
mmsAlertReplSetName = _MmsAlertReplSetName_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 10),
    _MmsAlertReplSetName_Type()
)
mmsAlertReplSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertReplSetName.setStatus("current")


class _MmsAlertSeverity_Type(Integer32):
    """Custom type mmsAlertSeverity based on Integer32"""
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
        *(("debug", 1),
          ("info", 2),
          ("warning", 3),
          ("error", 4),
          ("critical", 5))
    )


_MmsAlertSeverity_Type.__name__ = "Integer32"
_MmsAlertSeverity_Object = MibScalar
mmsAlertSeverity = _MmsAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 11),
    _MmsAlertSeverity_Type()
)
mmsAlertSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertSeverity.setStatus("current")


class _MmsAlertSummary_Type(DisplayString):
    """Custom type mmsAlertSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MmsAlertSummary_Type.__name__ = "DisplayString"
_MmsAlertSummary_Object = MibScalar
mmsAlertSummary = _MmsAlertSummary_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 1, 12),
    _MmsAlertSummary_Type()
)
mmsAlertSummary.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmsAlertSummary.setStatus("current")
_MmsHeartbeatObject_ObjectIdentity = ObjectIdentity
mmsHeartbeatObject = _MmsHeartbeatObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 2)
)


class _MmsHeartbeatHostnameId_Type(DisplayString):
    """Custom type mmsHeartbeatHostnameId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MmsHeartbeatHostnameId_Type.__name__ = "DisplayString"
_MmsHeartbeatHostnameId_Object = MibScalar
mmsHeartbeatHostnameId = _MmsHeartbeatHostnameId_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 2, 1),
    _MmsHeartbeatHostnameId_Type()
)
mmsHeartbeatHostnameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmsHeartbeatHostnameId.setStatus("current")
_MmsHeartbeatInterval_Type = Integer32
_MmsHeartbeatInterval_Object = MibScalar
mmsHeartbeatInterval = _MmsHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 2, 2),
    _MmsHeartbeatInterval_Type()
)
mmsHeartbeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmsHeartbeatInterval.setStatus("current")


class _MmsHeartbeatMessage_Type(DisplayString):
    """Custom type mmsHeartbeatMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MmsHeartbeatMessage_Type.__name__ = "DisplayString"
_MmsHeartbeatMessage_Object = MibScalar
mmsHeartbeatMessage = _MmsHeartbeatMessage_Object(
    (1, 3, 6, 1, 4, 1, 41138, 1, 1, 2, 3),
    _MmsHeartbeatMessage_Type()
)
mmsHeartbeatMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmsHeartbeatMessage.setStatus("current")
_ServerMIBNotifications_ObjectIdentity = ObjectIdentity
serverMIBNotifications = _ServerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41138, 1, 2)
)

# Managed Objects groups


# Notification objects

mmsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 41138, 1, 2, 1)
)
mmsAlert.setObjects(
      *(("MMS-10GEN-MIB", "mmsAlertId"),
        ("MMS-10GEN-MIB", "mmsAlertGroupName"),
        ("MMS-10GEN-MIB", "mmsAlertHostId"),
        ("MMS-10GEN-MIB", "mmsAlertHostAndPort"),
        ("MMS-10GEN-MIB", "mmsAlertStatus"),
        ("MMS-10GEN-MIB", "mmsAlertUrl"),
        ("MMS-10GEN-MIB", "mmsAlertMetricName"),
        ("MMS-10GEN-MIB", "mmsAlertMetricThreshold"),
        ("MMS-10GEN-MIB", "mmsAlertMetricValue"),
        ("MMS-10GEN-MIB", "mmsAlertReplSetName"),
        ("MMS-10GEN-MIB", "mmsAlertSeverity"),
        ("MMS-10GEN-MIB", "mmsAlertSummary"))
)
if mibBuilder.loadTexts:
    mmsAlert.setStatus(
        "current"
    )

mmsHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 41138, 1, 2, 2)
)
mmsHeartbeat.setObjects(
      *(("MMS-10GEN-MIB", "mmsHeartbeatHostnameId"),
        ("MMS-10GEN-MIB", "mmsHeartbeatInterval"),
        ("MMS-10GEN-MIB", "mmsHeartbeatMessage"))
)
if mibBuilder.loadTexts:
    mmsHeartbeat.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MMS-10GEN-MIB",
    **{"mms": mms,
       "server": server,
       "serverMIBObjects": serverMIBObjects,
       "mmsAlertObject": mmsAlertObject,
       "mmsAlertId": mmsAlertId,
       "mmsAlertGroupName": mmsAlertGroupName,
       "mmsAlertHostId": mmsAlertHostId,
       "mmsAlertHostAndPort": mmsAlertHostAndPort,
       "mmsAlertStatus": mmsAlertStatus,
       "mmsAlertUrl": mmsAlertUrl,
       "mmsAlertMetricName": mmsAlertMetricName,
       "mmsAlertMetricThreshold": mmsAlertMetricThreshold,
       "mmsAlertMetricValue": mmsAlertMetricValue,
       "mmsAlertReplSetName": mmsAlertReplSetName,
       "mmsAlertSeverity": mmsAlertSeverity,
       "mmsAlertSummary": mmsAlertSummary,
       "mmsHeartbeatObject": mmsHeartbeatObject,
       "mmsHeartbeatHostnameId": mmsHeartbeatHostnameId,
       "mmsHeartbeatInterval": mmsHeartbeatInterval,
       "mmsHeartbeatMessage": mmsHeartbeatMessage,
       "serverMIBNotifications": serverMIBNotifications,
       "mmsAlert": mmsAlert,
       "mmsHeartbeat": mmsHeartbeat}
)
