# SNMP MIB module (WTT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wtg_43223/WTT-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 22:06:24 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

cb52MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cb52Notifications_ObjectIdentity = ObjectIdentity
cb52Notifications = _Cb52Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 0, 0)
)
_Cb52AgentModules_ObjectIdentity = ObjectIdentity
cb52AgentModules = _Cb52AgentModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 0, 1)
)


class _Tmp108_Type(Integer32):
    """Custom type tmp108 based on Integer32"""
    defaultValue = 0


_Tmp108_Type.__name__ = "Integer32"
_Tmp108_Object = MibScalar
tmp108 = _Tmp108_Object(
    (1, 3, 6, 1, 4, 1, 43223, 0, 1, 1),
    _Tmp108_Type()
)
tmp108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp108.setStatus("current")

# Managed Objects groups


# Notification objects

cb52_too_hot = NotificationType(
    (1, 3, 6, 1, 4, 1, 43223, 0, 0, 1)
)
cb52_too_hot.setObjects(
    ("WTT-MIB", "tmp108")
)
if mibBuilder.loadTexts:
    cb52_too_hot.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WTT-MIB",
    **{"cb52MIB": cb52MIB,
       "cb52Notifications": cb52Notifications,
       "cb52-too-hot": cb52_too_hot,
       "cb52AgentModules": cb52AgentModules,
       "tmp108": tmp108}
)
