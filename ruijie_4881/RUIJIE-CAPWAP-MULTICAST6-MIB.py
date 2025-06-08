# SNMP MIB module (RUIJIE-CAPWAP-MULTICAST6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CAPWAP-MULTICAST6-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:45 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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

ruijieCapwapMulticast6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 85)
)
if mibBuilder.loadTexts:
    ruijieCapwapMulticast6MIB.setRevisions(
        ("2010-05-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieCapwapMulticast6MIBObjects_ObjectIdentity = ObjectIdentity
ruijieCapwapMulticast6MIBObjects = _RuijieCapwapMulticast6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 85, 1)
)


class _RuijieCapwapMulticast6WorkingMode_Type(Integer32):
    """Custom type ruijieCapwapMulticast6WorkingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("unicast", 2),
          ("multicast", 3))
    )


_RuijieCapwapMulticast6WorkingMode_Type.__name__ = "Integer32"
_RuijieCapwapMulticast6WorkingMode_Object = MibScalar
ruijieCapwapMulticast6WorkingMode = _RuijieCapwapMulticast6WorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 85, 1, 1),
    _RuijieCapwapMulticast6WorkingMode_Type()
)
ruijieCapwapMulticast6WorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCapwapMulticast6WorkingMode.setStatus("current")
_RuijieCapwapMulticast6Group_Type = InetAddress
_RuijieCapwapMulticast6Group_Object = MibScalar
ruijieCapwapMulticast6Group = _RuijieCapwapMulticast6Group_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 85, 1, 2),
    _RuijieCapwapMulticast6Group_Type()
)
ruijieCapwapMulticast6Group.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCapwapMulticast6Group.setStatus("current")
_RuijieCapwapMulticast6MIBConformance_ObjectIdentity = ObjectIdentity
ruijieCapwapMulticast6MIBConformance = _RuijieCapwapMulticast6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 85, 2)
)
_RuijieCapwapMulticast6MIBCompliances_ObjectIdentity = ObjectIdentity
ruijieCapwapMulticast6MIBCompliances = _RuijieCapwapMulticast6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 85, 2, 1)
)
_RuijieCapwapMulticast6MIBGroups_ObjectIdentity = ObjectIdentity
ruijieCapwapMulticast6MIBGroups = _RuijieCapwapMulticast6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 85, 2, 2)
)

# Managed Objects groups

ruijieCapwapMulticast6MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 85, 2, 2, 1)
)
ruijieCapwapMulticast6MIBGroup.setObjects(
      *(("RUIJIE-CAPWAP-MULTICAST6-MIB", "ruijieCapwapMulticast6WorkingMode"),
        ("RUIJIE-CAPWAP-MULTICAST6-MIB", "ruijieCapwapMulticast6Group"))
)
if mibBuilder.loadTexts:
    ruijieCapwapMulticast6MIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieCapwapMulticast6MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 85, 2, 1, 1)
)
ruijieCapwapMulticast6MIBCompliance.setObjects(
    ("RUIJIE-CAPWAP-MULTICAST6-MIB", "ruijieCapwapMulticast6MIBGroup")
)
if mibBuilder.loadTexts:
    ruijieCapwapMulticast6MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CAPWAP-MULTICAST6-MIB",
    **{"ruijieCapwapMulticast6MIB": ruijieCapwapMulticast6MIB,
       "ruijieCapwapMulticast6MIBObjects": ruijieCapwapMulticast6MIBObjects,
       "ruijieCapwapMulticast6WorkingMode": ruijieCapwapMulticast6WorkingMode,
       "ruijieCapwapMulticast6Group": ruijieCapwapMulticast6Group,
       "ruijieCapwapMulticast6MIBConformance": ruijieCapwapMulticast6MIBConformance,
       "ruijieCapwapMulticast6MIBCompliances": ruijieCapwapMulticast6MIBCompliances,
       "ruijieCapwapMulticast6MIBCompliance": ruijieCapwapMulticast6MIBCompliance,
       "ruijieCapwapMulticast6MIBGroups": ruijieCapwapMulticast6MIBGroups,
       "ruijieCapwapMulticast6MIBGroup": ruijieCapwapMulticast6MIBGroup}
)
