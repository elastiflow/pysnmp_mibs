# SNMP MIB module (RUIJIE-IP-MANAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-IP-MANAGE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

ruijieIpManageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12)
)
if mibBuilder.loadTexts:
    ruijieIpManageMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieDhcpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieDhcpMIBObjects = _RuijieDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 1)
)


class _RuijieDhcpRelayAgentGlobalStatus_Type(EnabledStatus):
    """Custom type ruijieDhcpRelayAgentGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieDhcpRelayAgentGlobalStatus_Type.__name__ = "EnabledStatus"
_RuijieDhcpRelayAgentGlobalStatus_Object = MibScalar
ruijieDhcpRelayAgentGlobalStatus = _RuijieDhcpRelayAgentGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 1, 2),
    _RuijieDhcpRelayAgentGlobalStatus_Type()
)
ruijieDhcpRelayAgentGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDhcpRelayAgentGlobalStatus.setStatus("current")
_RuijieDhcpServerIp_Type = IpAddress
_RuijieDhcpServerIp_Object = MibScalar
ruijieDhcpServerIp = _RuijieDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 1, 3),
    _RuijieDhcpServerIp_Type()
)
ruijieDhcpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDhcpServerIp.setStatus("current")
_RuijieIpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIpMIBObjects = _RuijieIpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 2)
)
_RuijieIpDefaultGateWay_Type = IpAddress
_RuijieIpDefaultGateWay_Object = MibScalar
ruijieIpDefaultGateWay = _RuijieIpDefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 2, 1),
    _RuijieIpDefaultGateWay_Type()
)
ruijieIpDefaultGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIpDefaultGateWay.setStatus("current")
_RuijieIpManageMIBConformance_ObjectIdentity = ObjectIdentity
ruijieIpManageMIBConformance = _RuijieIpManageMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3)
)
_RuijieIpManageMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieIpManageMIBCompliances = _RuijieIpManageMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3, 1)
)
_RuijieIpManageMIBGroups_ObjectIdentity = ObjectIdentity
ruijieIpManageMIBGroups = _RuijieIpManageMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3, 2)
)

# Managed Objects groups

ruijieL2L3DhcpManageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3, 2, 1)
)
ruijieL2L3DhcpManageMIBGroup.setObjects(
      *(("RUIJIE-IP-MANAGE-MIB", "ruijieDhcpRelayAgentGlobalStatus"),
        ("RUIJIE-IP-MANAGE-MIB", "ruijieDhcpServerIp"))
)
if mibBuilder.loadTexts:
    ruijieL2L3DhcpManageMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieIpManageMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3, 1, 1)
)
ruijieIpManageMIBCompliance.setObjects(
    ("RUIJIE-IP-MANAGE-MIB", "ruijieL2L3DhcpManageMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieIpManageMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-IP-MANAGE-MIB",
    **{"ruijieIpManageMIB": ruijieIpManageMIB,
       "ruijieDhcpMIBObjects": ruijieDhcpMIBObjects,
       "ruijieDhcpRelayAgentGlobalStatus": ruijieDhcpRelayAgentGlobalStatus,
       "ruijieDhcpServerIp": ruijieDhcpServerIp,
       "ruijieIpMIBObjects": ruijieIpMIBObjects,
       "ruijieIpDefaultGateWay": ruijieIpDefaultGateWay,
       "ruijieIpManageMIBConformance": ruijieIpManageMIBConformance,
       "ruijieIpManageMIBCompliances": ruijieIpManageMIBCompliances,
       "ruijieIpManageMIBCompliance": ruijieIpManageMIBCompliance,
       "ruijieIpManageMIBGroups": ruijieIpManageMIBGroups,
       "ruijieL2L3DhcpManageMIBGroup": ruijieL2L3DhcpManageMIBGroup}
)
