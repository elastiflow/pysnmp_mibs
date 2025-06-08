# SNMP MIB module (RUIJIE-CAPWAP-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CAPWAP-MULTICAST-MIB.mib
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

ruijieCapwapMulticastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 59)
)
if mibBuilder.loadTexts:
    ruijieCapwapMulticastMIB.setRevisions(
        ("2009-10-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieCapwapMulticastMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCapwapMulticastMIBObjects = _RuijieCapwapMulticastMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 59, 1)
)


class _RuijieCapwapMulticastWorkingMode_Type(Integer32):
    """Custom type ruijieCapwapMulticastWorkingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_RuijieCapwapMulticastWorkingMode_Type.__name__ = "Integer32"
_RuijieCapwapMulticastWorkingMode_Object = MibScalar
ruijieCapwapMulticastWorkingMode = _RuijieCapwapMulticastWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 59, 1, 1),
    _RuijieCapwapMulticastWorkingMode_Type()
)
ruijieCapwapMulticastWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCapwapMulticastWorkingMode.setStatus("current")
_RuijieCapwapMulticastGroup_Type = IpAddress
_RuijieCapwapMulticastGroup_Object = MibScalar
ruijieCapwapMulticastGroup = _RuijieCapwapMulticastGroup_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 59, 1, 2),
    _RuijieCapwapMulticastGroup_Type()
)
ruijieCapwapMulticastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCapwapMulticastGroup.setStatus("current")
_RuijieCapwapMulticastMIBConformance_ObjectIdentity = ObjectIdentity
ruijieCapwapMulticastMIBConformance = _RuijieCapwapMulticastMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 59, 2)
)
_RuijieCapwapMulticastMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieCapwapMulticastMIBCompliances = _RuijieCapwapMulticastMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 59, 2, 1)
)
_RuijieCapwapMulticastMIBGroups_ObjectIdentity = ObjectIdentity
ruijieCapwapMulticastMIBGroups = _RuijieCapwapMulticastMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 59, 2, 2)
)

# Managed Objects groups

ruijieCapwapMulticastMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 59, 2, 2, 1)
)
ruijieCapwapMulticastMIBGroup.setObjects(
      *(("RUIJIE-CAPWAP-MULTICAST-MIB", "ruijieCapwapMulticastWorkingMode"),
        ("RUIJIE-CAPWAP-MULTICAST-MIB", "ruijieCapwapMulticastGroup"))
)
if mibBuilder.loadTexts:
    ruijieCapwapMulticastMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieCapwapMulticastMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 59, 2, 1, 1)
)
ruijieCapwapMulticastMIBCompliance.setObjects(
    ("RUIJIE-CAPWAP-MULTICAST-MIB", "ruijieCapwapMulticastMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieCapwapMulticastMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CAPWAP-MULTICAST-MIB",
    **{"ruijieCapwapMulticastMIB": ruijieCapwapMulticastMIB,
       "ruijieCapwapMulticastMIBObjects": ruijieCapwapMulticastMIBObjects,
       "ruijieCapwapMulticastWorkingMode": ruijieCapwapMulticastWorkingMode,
       "ruijieCapwapMulticastGroup": ruijieCapwapMulticastGroup,
       "ruijieCapwapMulticastMIBConformance": ruijieCapwapMulticastMIBConformance,
       "ruijieCapwapMulticastMIBCompliances": ruijieCapwapMulticastMIBCompliances,
       "ruijieCapwapMulticastMIBCompliance": ruijieCapwapMulticastMIBCompliance,
       "ruijieCapwapMulticastMIBGroups": ruijieCapwapMulticastMIBGroups,
       "ruijieCapwapMulticastMIBGroup": ruijieCapwapMulticastMIBGroup}
)
