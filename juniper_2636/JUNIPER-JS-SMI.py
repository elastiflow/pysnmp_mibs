# SNMP MIB module (JUNIPER-JS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-JS-SMI.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:49:54 2025
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

(jnxJsMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxJsMibRoot")

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

_JnxJsSecurity_ObjectIdentity = ObjectIdentity
jnxJsSecurity = _JnxJsSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1)
)
_JnxJsIf_ObjectIdentity = ObjectIdentity
jnxJsIf = _JnxJsIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1)
)
_JnxJsAuth_ObjectIdentity = ObjectIdentity
jnxJsAuth = _JnxJsAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2)
)
_JnxJsCertificates_ObjectIdentity = ObjectIdentity
jnxJsCertificates = _JnxJsCertificates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3)
)
_JnxJsPolicies_ObjectIdentity = ObjectIdentity
jnxJsPolicies = _JnxJsPolicies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4)
)
_JnxJsIPSecVpn_ObjectIdentity = ObjectIdentity
jnxJsIPSecVpn = _JnxJsIPSecVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5)
)
_JnxJsNAT_ObjectIdentity = ObjectIdentity
jnxJsNAT = _JnxJsNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7)
)
_JnxJsScreening_ObjectIdentity = ObjectIdentity
jnxJsScreening = _JnxJsScreening_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8)
)
_JnxJsDhcp_ObjectIdentity = ObjectIdentity
jnxJsDhcp = _JnxJsDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 9)
)
_JnxJsDnsRoot_ObjectIdentity = ObjectIdentity
jnxJsDnsRoot = _JnxJsDnsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10)
)
_JnxJsIdpRoot_ObjectIdentity = ObjectIdentity
jnxJsIdpRoot = _JnxJsIdpRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11)
)
_JnxJsSPUMonitoringRoot_ObjectIdentity = ObjectIdentity
jnxJsSPUMonitoringRoot = _JnxJsSPUMonitoringRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12)
)
_JnxJsUTMRoot_ObjectIdentity = ObjectIdentity
jnxJsUTMRoot = _JnxJsUTMRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13)
)
_JnxJsChassisCluster_ObjectIdentity = ObjectIdentity
jnxJsChassisCluster = _JnxJsChassisCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14)
)
_JnxVoip_ObjectIdentity = ObjectIdentity
jnxVoip = _JnxVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15)
)
_JnxJsPacketMirror_ObjectIdentity = ObjectIdentity
jnxJsPacketMirror = _JnxJsPacketMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16)
)
_JnxLsysSecurityProfile_ObjectIdentity = ObjectIdentity
jnxLsysSecurityProfile = _JnxLsysSecurityProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17)
)
_JnxJsFlow_ObjectIdentity = ObjectIdentity
jnxJsFlow = _JnxJsFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 18)
)
_JnxJsChassisHA_ObjectIdentity = ObjectIdentity
jnxJsChassisHA = _JnxJsChassisHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19)
)
_JnxJsReswatchHA_ObjectIdentity = ObjectIdentity
jnxJsReswatchHA = _JnxJsReswatchHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20)
)
_JnxJsAAMW_ObjectIdentity = ObjectIdentity
jnxJsAAMW = _JnxJsAAMW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 21)
)
_JnxJsSMS_ObjectIdentity = ObjectIdentity
jnxJsSMS = _JnxJsSMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 22)
)
_JnxJsSecIntel_ObjectIdentity = ObjectIdentity
jnxJsSecIntel = _JnxJsSecIntel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 23)
)
_JnxLsysVD_ObjectIdentity = ObjectIdentity
jnxLsysVD = _JnxLsysVD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-SMI",
    **{"jnxJsSecurity": jnxJsSecurity,
       "jnxJsIf": jnxJsIf,
       "jnxJsAuth": jnxJsAuth,
       "jnxJsCertificates": jnxJsCertificates,
       "jnxJsPolicies": jnxJsPolicies,
       "jnxJsIPSecVpn": jnxJsIPSecVpn,
       "jnxJsNAT": jnxJsNAT,
       "jnxJsScreening": jnxJsScreening,
       "jnxJsDhcp": jnxJsDhcp,
       "jnxJsDnsRoot": jnxJsDnsRoot,
       "jnxJsIdpRoot": jnxJsIdpRoot,
       "jnxJsSPUMonitoringRoot": jnxJsSPUMonitoringRoot,
       "jnxJsUTMRoot": jnxJsUTMRoot,
       "jnxJsChassisCluster": jnxJsChassisCluster,
       "jnxVoip": jnxVoip,
       "jnxJsPacketMirror": jnxJsPacketMirror,
       "jnxLsysSecurityProfile": jnxLsysSecurityProfile,
       "jnxJsFlow": jnxJsFlow,
       "jnxJsChassisHA": jnxJsChassisHA,
       "jnxJsReswatchHA": jnxJsReswatchHA,
       "jnxJsAAMW": jnxJsAAMW,
       "jnxJsSMS": jnxJsSMS,
       "jnxJsSecIntel": jnxJsSecIntel,
       "jnxLsysVD": jnxLsysVD}
)
