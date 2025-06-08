# SNMP MIB module (F5-ALERT-DEF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/f5_12276/F5-ALERT-DEF-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:59:23 2025
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

(f5Compliance,
 platform) = mibBuilder.importSymbols(
    "F5-COMMON-SMI-MIB",
    "f5Compliance",
    "platform")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

f5Alerts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1)
)
if mibBuilder.loadTexts:
    f5Alerts.setRevisions(
        ("2019-08-01 09:41",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class F5Severity(TextualConvention, Integer32):
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7),
          ("na", 8))
    )



class F5CondEffect(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("assert", 1),
          ("event", 2),
          ("other", 9999))
    )



# MIB Managed Objects in the order of their OIDs

_F5AlertObjects_ObjectIdentity = ObjectIdentity
f5AlertObjects = _F5AlertObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0)
)
_F5AlertNotificationObject_ObjectIdentity = ObjectIdentity
f5AlertNotificationObject = _F5AlertNotificationObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1)
)


class _AlertSource_Type(DisplayString):
    """Custom type alertSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertSource_Type.__name__ = "DisplayString"
_AlertSource_Object = MibScalar
alertSource = _AlertSource_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 1),
    _AlertSource_Type()
)
alertSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSource.setStatus("current")
_AlertEffect_Type = F5CondEffect
_AlertEffect_Object = MibScalar
alertEffect = _AlertEffect_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 2),
    _AlertEffect_Type()
)
alertEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertEffect.setStatus("current")
_AlertSeverity_Type = F5Severity
_AlertSeverity_Object = MibScalar
alertSeverity = _AlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 3),
    _AlertSeverity_Type()
)
alertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSeverity.setStatus("current")


class _AlertTimeStamp_Type(DisplayString):
    """Custom type alertTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AlertTimeStamp_Type.__name__ = "DisplayString"
_AlertTimeStamp_Object = MibScalar
alertTimeStamp = _AlertTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 4),
    _AlertTimeStamp_Type()
)
alertTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertTimeStamp.setStatus("current")


class _AlertDescription_Type(DisplayString):
    """Custom type alertDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AlertDescription_Type.__name__ = "DisplayString"
_AlertDescription_Object = MibScalar
alertDescription = _AlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 5),
    _AlertDescription_Type()
)
alertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertDescription.setStatus("current")
_F5AlertNotificationObjectGroup_ObjectIdentity = ObjectIdentity
f5AlertNotificationObjectGroup = _F5AlertNotificationObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2)
)
_F5AlertNotificationGroup_ObjectIdentity = ObjectIdentity
f5AlertNotificationGroup = _F5AlertNotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 3)
)

# Managed Objects groups

alertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2, 1)
)
alertGroup.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    alertGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f5AlertGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12276, 2, 1)
)
f5AlertGroupCompliance.setObjects(
    ("F5-ALERT-DEF-MIB", "alertGroup")
)
if mibBuilder.loadTexts:
    f5AlertGroupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5-ALERT-DEF-MIB",
    **{"F5Severity": F5Severity,
       "F5CondEffect": F5CondEffect,
       "f5Alerts": f5Alerts,
       "f5AlertObjects": f5AlertObjects,
       "f5AlertNotificationObject": f5AlertNotificationObject,
       "alertSource": alertSource,
       "alertEffect": alertEffect,
       "alertSeverity": alertSeverity,
       "alertTimeStamp": alertTimeStamp,
       "alertDescription": alertDescription,
       "f5AlertNotificationObjectGroup": f5AlertNotificationObjectGroup,
       "alertGroup": alertGroup,
       "f5AlertNotificationGroup": f5AlertNotificationGroup,
       "f5AlertGroupCompliance": f5AlertGroupCompliance}
)
