# SNMP MIB module (F3-CAPABILITIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/F3-CAPABILITIES-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:57 2025
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

(f3Capabilities,) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "f3Capabilities")

(VlanIdOrAnyOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrAnyOrNone")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

f3CapabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    f3CapabilityMIB.setRevisions(
        ("2011-07-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F3CapabilityDefinitions_ObjectIdentity = ObjectIdentity
f3CapabilityDefinitions = _F3CapabilityDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

f3BaseStandardsCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f3BaseStandardsCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3BaseStandardsCapabilities.setStatus(
        "current"
    )

f3StandardIfEntityCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    f3StandardIfEntityCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardIfEntityCapabilities.setStatus(
        "current"
    )

f3StandardTargetNotifCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    f3StandardTargetNotifCapabilities.setProductRelease("F3 - Standard Interface and Entity capabilities ")
if mibBuilder.loadTexts:
    f3StandardTargetNotifCapabilities.setStatus(
        "current"
    )

f3StandardSecurityCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    f3StandardSecurityCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardSecurityCapabilities.setStatus(
        "current"
    )

f3StandardRMONCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    f3StandardRMONCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardRMONCapabilities.setStatus(
        "current"
    )

f3StandardCfmCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    f3StandardCfmCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardCfmCapabilities.setStatus(
        "current"
    )

f3StandardBridgeCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    f3StandardBridgeCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardBridgeCapabilities.setStatus(
        "current"
    )

f3StandardLAGCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    f3StandardLAGCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardLAGCapabilities.setStatus(
        "current"
    )

f3CommonVendorSpecificCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    f3CommonVendorSpecificCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3CommonVendorSpecificCapabilities.setStatus(
        "current"
    )

f3FacilityCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    f3FacilityCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3FacilityCapabilities.setStatus(
        "current"
    )

f3Nid206Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    f3Nid206Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid206Capabilities.setStatus(
        "current"
    )

f3Nid201SyncECapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    f3Nid201SyncECapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid201SyncECapabilities.setStatus(
        "current"
    )

f3Nid201NonSyncECapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    f3Nid201NonSyncECapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid201NonSyncECapabilities.setStatus(
        "current"
    )

f3Nid206FCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 14)
)
if mibBuilder.loadTexts:
    f3Nid206FCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid206FCapabilities.setStatus(
        "current"
    )

f3Nid112Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    f3Nid112Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid112Capabilities.setStatus(
        "current"
    )

f3Nid114Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 16)
)
if mibBuilder.loadTexts:
    f3Nid114Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114Capabilities.setStatus(
        "current"
    )

f3EcpaCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 17)
)
if mibBuilder.loadTexts:
    f3EcpaCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3EcpaCapabilities.setStatus(
        "current"
    )

f3EsaCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 18)
)
if mibBuilder.loadTexts:
    f3EsaCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3EsaCapabilities.setStatus(
        "current"
    )

f3BridgeCapabilitiesCmHub = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 19)
)
if mibBuilder.loadTexts:
    f3BridgeCapabilitiesCmHub.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3BridgeCapabilitiesCmHub.setStatus(
        "current"
    )

f3CommonVendorSpecificCapabilitiesCmHub = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 20)
)
if mibBuilder.loadTexts:
    f3CommonVendorSpecificCapabilitiesCmHub.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3CommonVendorSpecificCapabilitiesCmHub.setStatus(
        "current"
    )

f3FacilityCapabilitiesCmHub = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 21)
)
if mibBuilder.loadTexts:
    f3FacilityCapabilitiesCmHub.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3FacilityCapabilitiesCmHub.setStatus(
        "current"
    )

f3EntityCmHubCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 22)
)
if mibBuilder.loadTexts:
    f3EntityCmHubCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3EntityCmHubCapabilities.setStatus(
        "current"
    )

f3Nid206VCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 23)
)
if mibBuilder.loadTexts:
    f3Nid206VCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid206VCapabilities.setStatus(
        "current"
    )

f3NidXG210Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 24)
)
if mibBuilder.loadTexts:
    f3NidXG210Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidXG210Capabilities.setStatus(
        "current"
    )

f3PtpCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 25)
)
if mibBuilder.loadTexts:
    f3PtpCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3PtpCapabilities.setStatus(
        "current"
    )

f3PseudoWireCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 26)
)
if mibBuilder.loadTexts:
    f3PseudoWireCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3PseudoWireCapabilities.setStatus(
        "current"
    )

f3DS1Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 27)
)
if mibBuilder.loadTexts:
    f3DS1Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3DS1Capabilities.setStatus(
        "current"
    )

f3SonetCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 28)
)
if mibBuilder.loadTexts:
    f3SonetCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3SonetCapabilities.setStatus(
        "current"
    )

f3SyncECapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 29)
)
if mibBuilder.loadTexts:
    f3SyncECapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3SyncECapabilities.setStatus(
        "current"
    )

f3CfmCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 30)
)
if mibBuilder.loadTexts:
    f3CfmCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3CfmCapabilities.setStatus(
        "current"
    )

f3LAGCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 31)
)
if mibBuilder.loadTexts:
    f3LAGCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3LAGCapabilities.setStatus(
        "current"
    )

f3PBBCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 32)
)
if mibBuilder.loadTexts:
    f3PBBCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3PBBCapabilities.setStatus(
        "current"
    )

f3Nid1804Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 33)
)
if mibBuilder.loadTexts:
    f3Nid1804Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid1804Capabilities.setStatus(
        "current"
    )

f3Nid3204Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 34)
)
if mibBuilder.loadTexts:
    f3Nid3204Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid3204Capabilities.setStatus(
        "current"
    )

f3BertCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 35)
)
if mibBuilder.loadTexts:
    f3BertCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3BertCapabilities.setStatus(
        "current"
    )

f3NidSyncProbeCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 36)
)
if mibBuilder.loadTexts:
    f3NidSyncProbeCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidSyncProbeCapabilities.setStatus(
        "current"
    )

f3SyncJackCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 37)
)
if mibBuilder.loadTexts:
    f3SyncJackCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3SyncJackCapabilities.setStatus(
        "current"
    )

f3EsmCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 38)
)
if mibBuilder.loadTexts:
    f3EsmCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3EsmCapabilities.setStatus(
        "current"
    )

f3AMPClientCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 39)
)
if mibBuilder.loadTexts:
    f3AMPClientCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3AMPClientCapabilities.setStatus(
        "current"
    )

f3AMPServerCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 40)
)
if mibBuilder.loadTexts:
    f3AMPServerCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3AMPServerCapabilities.setStatus(
        "current"
    )

f3Nid114HCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 41)
)
if mibBuilder.loadTexts:
    f3Nid114HCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114HCapabilities.setStatus(
        "current"
    )

f3Nid114PHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 42)
)
if mibBuilder.loadTexts:
    f3Nid114PHCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114PHCapabilities.setStatus(
        "current"
    )

f3ERPCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 43)
)
if mibBuilder.loadTexts:
    f3ERPCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3ERPCapabilities.setStatus(
        "current"
    )

f3ShgCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 44)
)
if mibBuilder.loadTexts:
    f3ShgCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3ShgCapabilities.setStatus(
        "current"
    )

f3Nid114SCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 45)
)
if mibBuilder.loadTexts:
    f3Nid114SCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114SCapabilities.setStatus(
        "current"
    )

f3Nid114SHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 46)
)
if mibBuilder.loadTexts:
    f3Nid114SHCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114SHCapabilities.setStatus(
        "current"
    )

f3Ipv6Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 47)
)
if mibBuilder.loadTexts:
    f3Ipv6Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Ipv6Capabilities.setStatus(
        "current"
    )

f3SatCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 48)
)
if mibBuilder.loadTexts:
    f3SatCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3SatCapabilities.setStatus(
        "current"
    )

f3JdsuCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 49)
)
if mibBuilder.loadTexts:
    f3JdsuCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3JdsuCapabilities.setStatus(
        "current"
    )

f3PortMirrorCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 50)
)
if mibBuilder.loadTexts:
    f3PortMirrorCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3PortMirrorCapabilities.setStatus(
        "current"
    )

f3JdsuGeneratorCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 51)
)
if mibBuilder.loadTexts:
    f3JdsuGeneratorCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3JdsuGeneratorCapabilities.setStatus(
        "current"
    )

f3TwampCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 52)
)
if mibBuilder.loadTexts:
    f3TwampCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3TwampCapabilities.setStatus(
        "current"
    )

f3OspfCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 53)
)
if mibBuilder.loadTexts:
    f3OspfCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3OspfCapabilities.setStatus(
        "current"
    )

f3Mef35Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 54)
)
if mibBuilder.loadTexts:
    f3Mef35Capabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Mef35Capabilities.setStatus(
        "current"
    )

f3Nid112ProCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 55)
)
if mibBuilder.loadTexts:
    f3Nid112ProCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid112ProCapabilities.setStatus(
        "current"
    )

f3Nid112ProMCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 56)
)
if mibBuilder.loadTexts:
    f3Nid112ProMCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid112ProMCapabilities.setStatus(
        "current"
    )

f3Nid114ProCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 57)
)
if mibBuilder.loadTexts:
    f3Nid114ProCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProCapabilities.setStatus(
        "current"
    )

f3Nid114ProCCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 58)
)
if mibBuilder.loadTexts:
    f3Nid114ProCCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProCCapabilities.setStatus(
        "current"
    )

f3Nid114ProSHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 59)
)
if mibBuilder.loadTexts:
    f3Nid114ProSHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProSHCapabilities.setStatus(
        "current"
    )

f3Nid114ProCSHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 60)
)
if mibBuilder.loadTexts:
    f3Nid114ProCSHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProCSHCapabilities.setStatus(
        "current"
    )

f3Nid114ProHECapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 61)
)
if mibBuilder.loadTexts:
    f3Nid114ProHECapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProHECapabilities.setStatus(
        "current"
    )

f3Nid112ProHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 62)
)
if mibBuilder.loadTexts:
    f3Nid112ProHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid112ProHCapabilities.setStatus(
        "current"
    )

f3ConnectGuardCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 63)
)
if mibBuilder.loadTexts:
    f3ConnectGuardCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3ConnectGuardCapabilities.setStatus(
        "current"
    )

f3L3Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 64)
)
if mibBuilder.loadTexts:
    f3L3Capabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3L3Capabilities.setStatus(
        "current"
    )

f3Nid114GCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 65)
)
if mibBuilder.loadTexts:
    f3Nid114GCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114GCapabilities.setStatus(
        "current"
    )

f3BfdCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 66)
)
if mibBuilder.loadTexts:
    f3BfdCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3BfdCapabilities.setStatus(
        "current"
    )

f3EoMplsCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 67)
)
if mibBuilder.loadTexts:
    f3EoMplsCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3EoMplsCapabilities.setStatus(
        "current"
    )

f3FpmCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 68)
)
if mibBuilder.loadTexts:
    f3FpmCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3FpmCapabilities.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-CAPABILITIES-MIB",
    **{"f3CapabilityMIB": f3CapabilityMIB,
       "f3CapabilityDefinitions": f3CapabilityDefinitions,
       "f3BaseStandardsCapabilities": f3BaseStandardsCapabilities,
       "f3StandardIfEntityCapabilities": f3StandardIfEntityCapabilities,
       "f3StandardTargetNotifCapabilities": f3StandardTargetNotifCapabilities,
       "f3StandardSecurityCapabilities": f3StandardSecurityCapabilities,
       "f3StandardRMONCapabilities": f3StandardRMONCapabilities,
       "f3StandardCfmCapabilities": f3StandardCfmCapabilities,
       "f3StandardBridgeCapabilities": f3StandardBridgeCapabilities,
       "f3StandardLAGCapabilities": f3StandardLAGCapabilities,
       "f3CommonVendorSpecificCapabilities": f3CommonVendorSpecificCapabilities,
       "f3FacilityCapabilities": f3FacilityCapabilities,
       "f3Nid206Capabilities": f3Nid206Capabilities,
       "f3Nid201SyncECapabilities": f3Nid201SyncECapabilities,
       "f3Nid201NonSyncECapabilities": f3Nid201NonSyncECapabilities,
       "f3Nid206FCapabilities": f3Nid206FCapabilities,
       "f3Nid112Capabilities": f3Nid112Capabilities,
       "f3Nid114Capabilities": f3Nid114Capabilities,
       "f3EcpaCapabilities": f3EcpaCapabilities,
       "f3EsaCapabilities": f3EsaCapabilities,
       "f3BridgeCapabilitiesCmHub": f3BridgeCapabilitiesCmHub,
       "f3CommonVendorSpecificCapabilitiesCmHub": f3CommonVendorSpecificCapabilitiesCmHub,
       "f3FacilityCapabilitiesCmHub": f3FacilityCapabilitiesCmHub,
       "f3EntityCmHubCapabilities": f3EntityCmHubCapabilities,
       "f3Nid206VCapabilities": f3Nid206VCapabilities,
       "f3NidXG210Capabilities": f3NidXG210Capabilities,
       "f3PtpCapabilities": f3PtpCapabilities,
       "f3PseudoWireCapabilities": f3PseudoWireCapabilities,
       "f3DS1Capabilities": f3DS1Capabilities,
       "f3SonetCapabilities": f3SonetCapabilities,
       "f3SyncECapabilities": f3SyncECapabilities,
       "f3CfmCapabilities": f3CfmCapabilities,
       "f3LAGCapabilities": f3LAGCapabilities,
       "f3PBBCapabilities": f3PBBCapabilities,
       "f3Nid1804Capabilities": f3Nid1804Capabilities,
       "f3Nid3204Capabilities": f3Nid3204Capabilities,
       "f3BertCapabilities": f3BertCapabilities,
       "f3NidSyncProbeCapabilities": f3NidSyncProbeCapabilities,
       "f3SyncJackCapabilities": f3SyncJackCapabilities,
       "f3EsmCapabilities": f3EsmCapabilities,
       "f3AMPClientCapabilities": f3AMPClientCapabilities,
       "f3AMPServerCapabilities": f3AMPServerCapabilities,
       "f3Nid114HCapabilities": f3Nid114HCapabilities,
       "f3Nid114PHCapabilities": f3Nid114PHCapabilities,
       "f3ERPCapabilities": f3ERPCapabilities,
       "f3ShgCapabilities": f3ShgCapabilities,
       "f3Nid114SCapabilities": f3Nid114SCapabilities,
       "f3Nid114SHCapabilities": f3Nid114SHCapabilities,
       "f3Ipv6Capabilities": f3Ipv6Capabilities,
       "f3SatCapabilities": f3SatCapabilities,
       "f3JdsuCapabilities": f3JdsuCapabilities,
       "f3PortMirrorCapabilities": f3PortMirrorCapabilities,
       "f3JdsuGeneratorCapabilities": f3JdsuGeneratorCapabilities,
       "f3TwampCapabilities": f3TwampCapabilities,
       "f3OspfCapabilities": f3OspfCapabilities,
       "f3Mef35Capabilities": f3Mef35Capabilities,
       "f3Nid112ProCapabilities": f3Nid112ProCapabilities,
       "f3Nid112ProMCapabilities": f3Nid112ProMCapabilities,
       "f3Nid114ProCapabilities": f3Nid114ProCapabilities,
       "f3Nid114ProCCapabilities": f3Nid114ProCCapabilities,
       "f3Nid114ProSHCapabilities": f3Nid114ProSHCapabilities,
       "f3Nid114ProCSHCapabilities": f3Nid114ProCSHCapabilities,
       "f3Nid114ProHECapabilities": f3Nid114ProHECapabilities,
       "f3Nid112ProHCapabilities": f3Nid112ProHCapabilities,
       "f3ConnectGuardCapabilities": f3ConnectGuardCapabilities,
       "f3L3Capabilities": f3L3Capabilities,
       "f3Nid114GCapabilities": f3Nid114GCapabilities,
       "f3BfdCapabilities": f3BfdCapabilities,
       "f3EoMplsCapabilities": f3EoMplsCapabilities,
       "f3FpmCapabilities": f3FpmCapabilities}
)
