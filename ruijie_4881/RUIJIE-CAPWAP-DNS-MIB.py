# SNMP MIB module (RUIJIE-CAPWAP-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CAPWAP-DNS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:44 2025
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

(ruijieIfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-INTERFACE-MIB",
    "ruijieIfIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieCapwapDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88)
)
if mibBuilder.loadTexts:
    ruijieCapwapDnsMIB.setRevisions(
        ("2010-07-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieCapwapDnsMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCapwapDnsMIBObjects = _RuijieCapwapDnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88, 0)
)
_RuijieCapwapDnsGlobalConfig_ObjectIdentity = ObjectIdentity
ruijieCapwapDnsGlobalConfig = _RuijieCapwapDnsGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88, 0, 1)
)
_RuijieLDnsFirstServer_Type = IpAddress
_RuijieLDnsFirstServer_Object = MibScalar
ruijieLDnsFirstServer = _RuijieLDnsFirstServer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88, 0, 1, 1),
    _RuijieLDnsFirstServer_Type()
)
ruijieLDnsFirstServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLDnsFirstServer.setStatus("current")
_RuijieLDnsSecondServer_Type = IpAddress
_RuijieLDnsSecondServer_Object = MibScalar
ruijieLDnsSecondServer = _RuijieLDnsSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88, 0, 1, 2),
    _RuijieLDnsSecondServer_Type()
)
ruijieLDnsSecondServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLDnsSecondServer.setStatus("current")
_RuijieCapwapDnsMIBConformance_ObjectIdentity = ObjectIdentity
ruijieCapwapDnsMIBConformance = _RuijieCapwapDnsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88, 2)
)
_RuijieCapwapDnsMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieCapwapDnsMIBCompliances = _RuijieCapwapDnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88, 2, 1)
)
_RuijieCapwapDnsMIBGroups_ObjectIdentity = ObjectIdentity
ruijieCapwapDnsMIBGroups = _RuijieCapwapDnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88, 2, 2)
)

# Managed Objects groups

ruijieCapwapDnsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88, 2, 2, 1)
)
ruijieCapwapDnsMIBGroup.setObjects(
      *(("RUIJIE-CAPWAP-DNS-MIB", "ruijieLDnsFirstServer"),
        ("RUIJIE-CAPWAP-DNS-MIB", "ruijieLDnsSecondServer"))
)
if mibBuilder.loadTexts:
    ruijieCapwapDnsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieCapwapDnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 88, 2, 1, 1)
)
ruijieCapwapDnsMIBCompliance.setObjects(
    ("RUIJIE-CAPWAP-DNS-MIB", "ruijieCapwapDnsMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieCapwapDnsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CAPWAP-DNS-MIB",
    **{"ruijieCapwapDnsMIB": ruijieCapwapDnsMIB,
       "ruijieCapwapDnsMIBObjects": ruijieCapwapDnsMIBObjects,
       "ruijieCapwapDnsGlobalConfig": ruijieCapwapDnsGlobalConfig,
       "ruijieLDnsFirstServer": ruijieLDnsFirstServer,
       "ruijieLDnsSecondServer": ruijieLDnsSecondServer,
       "ruijieCapwapDnsMIBConformance": ruijieCapwapDnsMIBConformance,
       "ruijieCapwapDnsMIBCompliances": ruijieCapwapDnsMIBCompliances,
       "ruijieCapwapDnsMIBCompliance": ruijieCapwapDnsMIBCompliance,
       "ruijieCapwapDnsMIBGroups": ruijieCapwapDnsMIBGroups,
       "ruijieCapwapDnsMIBGroup": ruijieCapwapDnsMIBGroup}
)
