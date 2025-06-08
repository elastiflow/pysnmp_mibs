# SNMP MIB module (CISCO-LWAPP-WLAN-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-WLAN-POLICY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:06 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoCapwapWlanPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 853)
)
if mibBuilder.loadTexts:
    ciscoCapwapWlanPolicyMIB.setRevisions(
        ("2023-01-23 00:00",
         "2021-01-20 00:00",
         "2019-11-20 00:00",
         "2019-07-23 00:00",
         "2019-03-15 00:00",
         "2019-01-18 00:00",
         "2018-08-20 00:00",
         "2018-03-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappWlanPolicyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappWlanPolicyMIBNotifs = _CiscoLwappWlanPolicyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 0)
)
_CiscoLwappWlanPolicyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappWlanPolicyMIBObjects = _CiscoLwappWlanPolicyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1)
)
_CiscoLwappWlanPolicyConfig_ObjectIdentity = ObjectIdentity
ciscoLwappWlanPolicyConfig = _CiscoLwappWlanPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2)
)
_CLWlanPolicyConfigTable_Object = MibTable
cLWlanPolicyConfigTable = _CLWlanPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLWlanPolicyConfigTable.setStatus("current")
_CLWlanPolicyConfigEntry_Object = MibTableRow
cLWlanPolicyConfigEntry = _CLWlanPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1)
)
cLWlanPolicyConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanWlanPolicyName"),
)
if mibBuilder.loadTexts:
    cLWlanPolicyConfigEntry.setStatus("current")


class _CLWlanWlanPolicyName_Type(SnmpAdminString):
    """Custom type cLWlanWlanPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLWlanWlanPolicyName_Type.__name__ = "SnmpAdminString"
_CLWlanWlanPolicyName_Object = MibTableColumn
cLWlanWlanPolicyName = _CLWlanWlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 1),
    _CLWlanWlanPolicyName_Type()
)
cLWlanWlanPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanWlanPolicyName.setStatus("current")
_CLWlanPlcyRowStatus_Type = RowStatus
_CLWlanPlcyRowStatus_Object = MibTableColumn
cLWlanPlcyRowStatus = _CLWlanPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 2),
    _CLWlanPlcyRowStatus_Type()
)
cLWlanPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanPlcyRowStatus.setStatus("current")


class _CLWlanPolicyDescription_Type(SnmpAdminString):
    """Custom type cLWlanPolicyDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyDescription_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyDescription_Object = MibTableColumn
cLWlanPolicyDescription = _CLWlanPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 3),
    _CLWlanPolicyDescription_Type()
)
cLWlanPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDescription.setStatus("current")


class _CLWlanPolicyInterfaceName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLWlanPolicyInterfaceName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyInterfaceName_Object = MibTableColumn
cLWlanPolicyInterfaceName = _CLWlanPolicyInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 4),
    _CLWlanPolicyInterfaceName_Type()
)
cLWlanPolicyInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyInterfaceName.setStatus("current")


class _CLWlanPolicyCentralSwitchMode_Type(TruthValue):
    """Custom type cLWlanPolicyCentralSwitchMode based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyCentralSwitchMode_Type.__name__ = "TruthValue"
_CLWlanPolicyCentralSwitchMode_Object = MibTableColumn
cLWlanPolicyCentralSwitchMode = _CLWlanPolicyCentralSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 5),
    _CLWlanPolicyCentralSwitchMode_Type()
)
cLWlanPolicyCentralSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyCentralSwitchMode.setStatus("current")


class _CLWlanPolicyCentralAuthMode_Type(TruthValue):
    """Custom type cLWlanPolicyCentralAuthMode based on TruthValue"""
    defaultValue = 1


_CLWlanPolicyCentralAuthMode_Type.__name__ = "TruthValue"
_CLWlanPolicyCentralAuthMode_Object = MibTableColumn
cLWlanPolicyCentralAuthMode = _CLWlanPolicyCentralAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 6),
    _CLWlanPolicyCentralAuthMode_Type()
)
cLWlanPolicyCentralAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyCentralAuthMode.setStatus("current")


class _CLWlanPolicyDhcpCentral_Type(TruthValue):
    """Custom type cLWlanPolicyDhcpCentral based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDhcpCentral_Type.__name__ = "TruthValue"
_CLWlanPolicyDhcpCentral_Object = MibTableColumn
cLWlanPolicyDhcpCentral = _CLWlanPolicyDhcpCentral_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 7),
    _CLWlanPolicyDhcpCentral_Type()
)
cLWlanPolicyDhcpCentral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDhcpCentral.setStatus("current")


class _CLWlanPolicyNatPatEnabled_Type(TruthValue):
    """Custom type cLWlanPolicyNatPatEnabled based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyNatPatEnabled_Type.__name__ = "TruthValue"
_CLWlanPolicyNatPatEnabled_Object = MibTableColumn
cLWlanPolicyNatPatEnabled = _CLWlanPolicyNatPatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 9),
    _CLWlanPolicyNatPatEnabled_Type()
)
cLWlanPolicyNatPatEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyNatPatEnabled.setStatus("current")


class _CLWlanPolicyAssocCentral_Type(TruthValue):
    """Custom type cLWlanPolicyAssocCentral based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyAssocCentral_Type.__name__ = "TruthValue"
_CLWlanPolicyAssocCentral_Object = MibTableColumn
cLWlanPolicyAssocCentral = _CLWlanPolicyAssocCentral_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 10),
    _CLWlanPolicyAssocCentral_Type()
)
cLWlanPolicyAssocCentral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyAssocCentral.setStatus("current")


class _CLWlanPolicyIPv4AclName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyIPv4AclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLWlanPolicyIPv4AclName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyIPv4AclName_Object = MibTableColumn
cLWlanPolicyIPv4AclName = _CLWlanPolicyIPv4AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 11),
    _CLWlanPolicyIPv4AclName_Type()
)
cLWlanPolicyIPv4AclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyIPv4AclName.setStatus("current")


class _CLWlanPolicyIPv6AclName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyIPv6AclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyIPv6AclName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyIPv6AclName_Object = MibTableColumn
cLWlanPolicyIPv6AclName = _CLWlanPolicyIPv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 12),
    _CLWlanPolicyIPv6AclName_Type()
)
cLWlanPolicyIPv6AclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyIPv6AclName.setStatus("current")


class _CLWlanPolicyL2AclName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyL2AclName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyL2AclName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyL2AclName_Object = MibTableColumn
cLWlanPolicyL2AclName = _CLWlanPolicyL2AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 13),
    _CLWlanPolicyL2AclName_Type()
)
cLWlanPolicyL2AclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyL2AclName.setStatus("current")


class _CLWlanPolicySessionTimeout_Type(Unsigned32):
    """Custom type cLWlanPolicySessionTimeout based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 86400),
    )


_CLWlanPolicySessionTimeout_Type.__name__ = "Unsigned32"
_CLWlanPolicySessionTimeout_Object = MibTableColumn
cLWlanPolicySessionTimeout = _CLWlanPolicySessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 14),
    _CLWlanPolicySessionTimeout_Type()
)
cLWlanPolicySessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicySessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanPolicySessionTimeout.setUnits("seconds")


class _CLWlanPolicyUserIdleTimeout_Type(Unsigned32):
    """Custom type cLWlanPolicyUserIdleTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 100000),
    )


_CLWlanPolicyUserIdleTimeout_Type.__name__ = "Unsigned32"
_CLWlanPolicyUserIdleTimeout_Object = MibTableColumn
cLWlanPolicyUserIdleTimeout = _CLWlanPolicyUserIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 15),
    _CLWlanPolicyUserIdleTimeout_Type()
)
cLWlanPolicyUserIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyUserIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanPolicyUserIdleTimeout.setUnits("seconds")


class _CLWlanPolicyClientExclTimeout_Type(Unsigned32):
    """Custom type cLWlanPolicyClientExclTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CLWlanPolicyClientExclTimeout_Type.__name__ = "Unsigned32"
_CLWlanPolicyClientExclTimeout_Object = MibTableColumn
cLWlanPolicyClientExclTimeout = _CLWlanPolicyClientExclTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 16),
    _CLWlanPolicyClientExclTimeout_Type()
)
cLWlanPolicyClientExclTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyClientExclTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanPolicyClientExclTimeout.setUnits("seconds")


class _CLWlanPolicyNativeProfiling_Type(TruthValue):
    """Custom type cLWlanPolicyNativeProfiling based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyNativeProfiling_Type.__name__ = "TruthValue"
_CLWlanPolicyNativeProfiling_Object = MibTableColumn
cLWlanPolicyNativeProfiling = _CLWlanPolicyNativeProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 17),
    _CLWlanPolicyNativeProfiling_Type()
)
cLWlanPolicyNativeProfiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyNativeProfiling.setStatus("current")


class _CLWlanPolicySubscriberPolicyName_Type(SnmpAdminString):
    """Custom type cLWlanPolicySubscriberPolicyName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicySubscriberPolicyName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicySubscriberPolicyName_Object = MibTableColumn
cLWlanPolicySubscriberPolicyName = _CLWlanPolicySubscriberPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 18),
    _CLWlanPolicySubscriberPolicyName_Type()
)
cLWlanPolicySubscriberPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicySubscriberPolicyName.setStatus("current")
_CLWlanPolicyHttpDeviceProfiling_Type = TruthValue
_CLWlanPolicyHttpDeviceProfiling_Object = MibTableColumn
cLWlanPolicyHttpDeviceProfiling = _CLWlanPolicyHttpDeviceProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 19),
    _CLWlanPolicyHttpDeviceProfiling_Type()
)
cLWlanPolicyHttpDeviceProfiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyHttpDeviceProfiling.setStatus("current")
_CLWlanPolicyDHCPDeviceProfiling_Type = TruthValue
_CLWlanPolicyDHCPDeviceProfiling_Object = MibTableColumn
cLWlanPolicyDHCPDeviceProfiling = _CLWlanPolicyDHCPDeviceProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 20),
    _CLWlanPolicyDHCPDeviceProfiling_Type()
)
cLWlanPolicyDHCPDeviceProfiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPDeviceProfiling.setStatus("current")


class _CLWlanPolicyNetflowIPv4InputMonitorName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyNetflowIPv4InputMonitorName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyNetflowIPv4InputMonitorName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyNetflowIPv4InputMonitorName_Object = MibTableColumn
cLWlanPolicyNetflowIPv4InputMonitorName = _CLWlanPolicyNetflowIPv4InputMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 21),
    _CLWlanPolicyNetflowIPv4InputMonitorName_Type()
)
cLWlanPolicyNetflowIPv4InputMonitorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyNetflowIPv4InputMonitorName.setStatus("deprecated")


class _CLWlanPolicyNetflowIPv4OutputMonitorName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyNetflowIPv4OutputMonitorName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyNetflowIPv4OutputMonitorName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyNetflowIPv4OutputMonitorName_Object = MibTableColumn
cLWlanPolicyNetflowIPv4OutputMonitorName = _CLWlanPolicyNetflowIPv4OutputMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 22),
    _CLWlanPolicyNetflowIPv4OutputMonitorName_Type()
)
cLWlanPolicyNetflowIPv4OutputMonitorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyNetflowIPv4OutputMonitorName.setStatus("deprecated")


class _CLWlanPolicyNetflowIPv6InputMonitorName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyNetflowIPv6InputMonitorName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyNetflowIPv6InputMonitorName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyNetflowIPv6InputMonitorName_Object = MibTableColumn
cLWlanPolicyNetflowIPv6InputMonitorName = _CLWlanPolicyNetflowIPv6InputMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 23),
    _CLWlanPolicyNetflowIPv6InputMonitorName_Type()
)
cLWlanPolicyNetflowIPv6InputMonitorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyNetflowIPv6InputMonitorName.setStatus("deprecated")


class _CLWlanPolicyNetflowIPv6OutputMonitorName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyNetflowIPv6OutputMonitorName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyNetflowIPv6OutputMonitorName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyNetflowIPv6OutputMonitorName_Object = MibTableColumn
cLWlanPolicyNetflowIPv6OutputMonitorName = _CLWlanPolicyNetflowIPv6OutputMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 24),
    _CLWlanPolicyNetflowIPv6OutputMonitorName_Type()
)
cLWlanPolicyNetflowIPv6OutputMonitorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyNetflowIPv6OutputMonitorName.setStatus("deprecated")


class _CLWlanPolicyQosPerSSIDInput_Type(SnmpAdminString):
    """Custom type cLWlanPolicyQosPerSSIDInput based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyQosPerSSIDInput_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyQosPerSSIDInput_Object = MibTableColumn
cLWlanPolicyQosPerSSIDInput = _CLWlanPolicyQosPerSSIDInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 25),
    _CLWlanPolicyQosPerSSIDInput_Type()
)
cLWlanPolicyQosPerSSIDInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyQosPerSSIDInput.setStatus("current")


class _CLWlanPolicyQosPerSSIDOutput_Type(SnmpAdminString):
    """Custom type cLWlanPolicyQosPerSSIDOutput based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyQosPerSSIDOutput_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyQosPerSSIDOutput_Object = MibTableColumn
cLWlanPolicyQosPerSSIDOutput = _CLWlanPolicyQosPerSSIDOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 26),
    _CLWlanPolicyQosPerSSIDOutput_Type()
)
cLWlanPolicyQosPerSSIDOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyQosPerSSIDOutput.setStatus("current")


class _CLWlanPolicyQosPerBSSIDInput_Type(SnmpAdminString):
    """Custom type cLWlanPolicyQosPerBSSIDInput based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyQosPerBSSIDInput_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyQosPerBSSIDInput_Object = MibTableColumn
cLWlanPolicyQosPerBSSIDInput = _CLWlanPolicyQosPerBSSIDInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 27),
    _CLWlanPolicyQosPerBSSIDInput_Type()
)
cLWlanPolicyQosPerBSSIDInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyQosPerBSSIDInput.setStatus("current")


class _CLWlanPolicyQosPerBSSIDOutput_Type(SnmpAdminString):
    """Custom type cLWlanPolicyQosPerBSSIDOutput based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyQosPerBSSIDOutput_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyQosPerBSSIDOutput_Object = MibTableColumn
cLWlanPolicyQosPerBSSIDOutput = _CLWlanPolicyQosPerBSSIDOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 28),
    _CLWlanPolicyQosPerBSSIDOutput_Type()
)
cLWlanPolicyQosPerBSSIDOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyQosPerBSSIDOutput.setStatus("current")


class _CLWlanPolicyBlacklistTimeout_Type(Unsigned32):
    """Custom type cLWlanPolicyBlacklistTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CLWlanPolicyBlacklistTimeout_Type.__name__ = "Unsigned32"
_CLWlanPolicyBlacklistTimeout_Object = MibTableColumn
cLWlanPolicyBlacklistTimeout = _CLWlanPolicyBlacklistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 29),
    _CLWlanPolicyBlacklistTimeout_Type()
)
cLWlanPolicyBlacklistTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyBlacklistTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanPolicyBlacklistTimeout.setUnits("seconds")


class _CLWlanPolicyBlacklistingCapability_Type(TruthValue):
    """Custom type cLWlanPolicyBlacklistingCapability based on TruthValue"""
    defaultValue = 1


_CLWlanPolicyBlacklistingCapability_Type.__name__ = "TruthValue"
_CLWlanPolicyBlacklistingCapability_Object = MibTableColumn
cLWlanPolicyBlacklistingCapability = _CLWlanPolicyBlacklistingCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 30),
    _CLWlanPolicyBlacklistingCapability_Type()
)
cLWlanPolicyBlacklistingCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyBlacklistingCapability.setStatus("current")


class _CLWlanPolicyDhcpRequired_Type(Integer32):
    """Custom type cLWlanPolicyDhcpRequired based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CLWlanPolicyDhcpRequired_Type.__name__ = "Integer32"
_CLWlanPolicyDhcpRequired_Object = MibTableColumn
cLWlanPolicyDhcpRequired = _CLWlanPolicyDhcpRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 31),
    _CLWlanPolicyDhcpRequired_Type()
)
cLWlanPolicyDhcpRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDhcpRequired.setStatus("current")
_CLWlanPolicyDhcpServerIpAddress_Type = IpAddress
_CLWlanPolicyDhcpServerIpAddress_Object = MibTableColumn
cLWlanPolicyDhcpServerIpAddress = _CLWlanPolicyDhcpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 32),
    _CLWlanPolicyDhcpServerIpAddress_Type()
)
cLWlanPolicyDhcpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDhcpServerIpAddress.setStatus("current")


class _CLWlanPolicyAaaOverride_Type(TruthValue):
    """Custom type cLWlanPolicyAaaOverride based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyAaaOverride_Type.__name__ = "TruthValue"
_CLWlanPolicyAaaOverride_Object = MibTableColumn
cLWlanPolicyAaaOverride = _CLWlanPolicyAaaOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 33),
    _CLWlanPolicyAaaOverride_Type()
)
cLWlanPolicyAaaOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyAaaOverride.setStatus("current")


class _CLWlanPolicyNac_Type(TruthValue):
    """Custom type cLWlanPolicyNac based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyNac_Type.__name__ = "TruthValue"
_CLWlanPolicyNac_Object = MibTableColumn
cLWlanPolicyNac = _CLWlanPolicyNac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 34),
    _CLWlanPolicyNac_Type()
)
cLWlanPolicyNac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyNac.setStatus("current")


class _CLWlanPolicyStatus_Type(TruthValue):
    """Custom type cLWlanPolicyStatus based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyStatus_Type.__name__ = "TruthValue"
_CLWlanPolicyStatus_Object = MibTableColumn
cLWlanPolicyStatus = _CLWlanPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 35),
    _CLWlanPolicyStatus_Type()
)
cLWlanPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyStatus.setStatus("current")


class _CLWlanPolicyRadiusHttpProfiling_Type(TruthValue):
    """Custom type cLWlanPolicyRadiusHttpProfiling based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyRadiusHttpProfiling_Type.__name__ = "TruthValue"
_CLWlanPolicyRadiusHttpProfiling_Object = MibTableColumn
cLWlanPolicyRadiusHttpProfiling = _CLWlanPolicyRadiusHttpProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 36),
    _CLWlanPolicyRadiusHttpProfiling_Type()
)
cLWlanPolicyRadiusHttpProfiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyRadiusHttpProfiling.setStatus("current")


class _CLWlanPolicyUserIdleThreshold_Type(Unsigned32):
    """Custom type cLWlanPolicyUserIdleThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CLWlanPolicyUserIdleThreshold_Type.__name__ = "Unsigned32"
_CLWlanPolicyUserIdleThreshold_Object = MibTableColumn
cLWlanPolicyUserIdleThreshold = _CLWlanPolicyUserIdleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 37),
    _CLWlanPolicyUserIdleThreshold_Type()
)
cLWlanPolicyUserIdleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyUserIdleThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanPolicyUserIdleThreshold.setUnits("bytes")


class _CLWlanPolicyQosFastlane_Type(Integer32):
    """Custom type cLWlanPolicyQosFastlane based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enterprise", 1),
          ("voice", 2),
          ("guest", 3),
          ("fastlane", 4))
    )


_CLWlanPolicyQosFastlane_Type.__name__ = "Integer32"
_CLWlanPolicyQosFastlane_Object = MibTableColumn
cLWlanPolicyQosFastlane = _CLWlanPolicyQosFastlane_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 38),
    _CLWlanPolicyQosFastlane_Type()
)
cLWlanPolicyQosFastlane.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyQosFastlane.setStatus("current")


class _CLWlanPolicyDHCPOption82Ascii_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Ascii based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Ascii_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Ascii_Object = MibTableColumn
cLWlanPolicyDHCPOption82Ascii = _CLWlanPolicyDHCPOption82Ascii_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 39),
    _CLWlanPolicyDHCPOption82Ascii_Type()
)
cLWlanPolicyDHCPOption82Ascii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Ascii.setStatus("current")


class _CLWlanPolicyDHCPOption82Rid_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Rid based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Rid_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Rid_Object = MibTableColumn
cLWlanPolicyDHCPOption82Rid = _CLWlanPolicyDHCPOption82Rid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 40),
    _CLWlanPolicyDHCPOption82Rid_Type()
)
cLWlanPolicyDHCPOption82Rid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Rid.setStatus("current")


class _CLWlanPolicyDHCPOption82Enable_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Enable based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Enable_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Enable_Object = MibTableColumn
cLWlanPolicyDHCPOption82Enable = _CLWlanPolicyDHCPOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 41),
    _CLWlanPolicyDHCPOption82Enable_Type()
)
cLWlanPolicyDHCPOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Enable.setStatus("current")


class _CLWlanPolicyDHCPOption82Apmac_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Apmac based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Apmac_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Apmac_Object = MibTableColumn
cLWlanPolicyDHCPOption82Apmac = _CLWlanPolicyDHCPOption82Apmac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 42),
    _CLWlanPolicyDHCPOption82Apmac_Type()
)
cLWlanPolicyDHCPOption82Apmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Apmac.setStatus("current")


class _CLWlanPolicyDHCPOption82Apethmac_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Apethmac based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Apethmac_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Apethmac_Object = MibTableColumn
cLWlanPolicyDHCPOption82Apethmac = _CLWlanPolicyDHCPOption82Apethmac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 43),
    _CLWlanPolicyDHCPOption82Apethmac_Type()
)
cLWlanPolicyDHCPOption82Apethmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Apethmac.setStatus("current")


class _CLWlanPolicyDHCPOption82Apname_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Apname based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Apname_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Apname_Object = MibTableColumn
cLWlanPolicyDHCPOption82Apname = _CLWlanPolicyDHCPOption82Apname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 44),
    _CLWlanPolicyDHCPOption82Apname_Type()
)
cLWlanPolicyDHCPOption82Apname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Apname.setStatus("current")


class _CLWlanPolicyDHCPOption82Policytag_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Policytag based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Policytag_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Policytag_Object = MibTableColumn
cLWlanPolicyDHCPOption82Policytag = _CLWlanPolicyDHCPOption82Policytag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 45),
    _CLWlanPolicyDHCPOption82Policytag_Type()
)
cLWlanPolicyDHCPOption82Policytag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Policytag.setStatus("current")


class _CLWlanPolicyDHCPOption82Aplocation_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Aplocation based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Aplocation_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Aplocation_Object = MibTableColumn
cLWlanPolicyDHCPOption82Aplocation = _CLWlanPolicyDHCPOption82Aplocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 46),
    _CLWlanPolicyDHCPOption82Aplocation_Type()
)
cLWlanPolicyDHCPOption82Aplocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Aplocation.setStatus("current")


class _CLWlanPolicyDHCPOption82Vlanid_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Vlanid based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Vlanid_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Vlanid_Object = MibTableColumn
cLWlanPolicyDHCPOption82Vlanid = _CLWlanPolicyDHCPOption82Vlanid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 47),
    _CLWlanPolicyDHCPOption82Vlanid_Type()
)
cLWlanPolicyDHCPOption82Vlanid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Vlanid.setStatus("current")


class _CLWlanPolicyDHCPOption82Ssid_Type(TruthValue):
    """Custom type cLWlanPolicyDHCPOption82Ssid based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyDHCPOption82Ssid_Type.__name__ = "TruthValue"
_CLWlanPolicyDHCPOption82Ssid_Object = MibTableColumn
cLWlanPolicyDHCPOption82Ssid = _CLWlanPolicyDHCPOption82Ssid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 48),
    _CLWlanPolicyDHCPOption82Ssid_Type()
)
cLWlanPolicyDHCPOption82Ssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDHCPOption82Ssid.setStatus("current")


class _CLWlanPolicySplitMacAcl_Type(SnmpAdminString):
    """Custom type cLWlanPolicySplitMacAcl based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_CLWlanPolicySplitMacAcl_Type.__name__ = "SnmpAdminString"
_CLWlanPolicySplitMacAcl_Object = MibTableColumn
cLWlanPolicySplitMacAcl = _CLWlanPolicySplitMacAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 49),
    _CLWlanPolicySplitMacAcl_Type()
)
cLWlanPolicySplitMacAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicySplitMacAcl.setStatus("current")


class _CLWlanPolicyVlanCentralSwitching_Type(TruthValue):
    """Custom type cLWlanPolicyVlanCentralSwitching based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyVlanCentralSwitching_Type.__name__ = "TruthValue"
_CLWlanPolicyVlanCentralSwitching_Object = MibTableColumn
cLWlanPolicyVlanCentralSwitching = _CLWlanPolicyVlanCentralSwitching_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 50),
    _CLWlanPolicyVlanCentralSwitching_Type()
)
cLWlanPolicyVlanCentralSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyVlanCentralSwitching.setStatus("current")


class _CLWlanPolicyPassiveClient_Type(TruthValue):
    """Custom type cLWlanPolicyPassiveClient based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyPassiveClient_Type.__name__ = "TruthValue"
_CLWlanPolicyPassiveClient_Object = MibTableColumn
cLWlanPolicyPassiveClient = _CLWlanPolicyPassiveClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 54),
    _CLWlanPolicyPassiveClient_Type()
)
cLWlanPolicyPassiveClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyPassiveClient.setStatus("current")


class _CLWlanPolicyNBARProtocolDiscovery_Type(TruthValue):
    """Custom type cLWlanPolicyNBARProtocolDiscovery based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyNBARProtocolDiscovery_Type.__name__ = "TruthValue"
_CLWlanPolicyNBARProtocolDiscovery_Object = MibTableColumn
cLWlanPolicyNBARProtocolDiscovery = _CLWlanPolicyNBARProtocolDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 55),
    _CLWlanPolicyNBARProtocolDiscovery_Type()
)
cLWlanPolicyNBARProtocolDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyNBARProtocolDiscovery.setStatus("current")


class _CLWlanPolicyStaticIPMobility_Type(TruthValue):
    """Custom type cLWlanPolicyStaticIPMobility based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyStaticIPMobility_Type.__name__ = "TruthValue"
_CLWlanPolicyStaticIPMobility_Object = MibTableColumn
cLWlanPolicyStaticIPMobility = _CLWlanPolicyStaticIPMobility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 56),
    _CLWlanPolicyStaticIPMobility_Type()
)
cLWlanPolicyStaticIPMobility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyStaticIPMobility.setStatus("current")


class _ClWlanPolicyMobilityAnchor_Type(TruthValue):
    """Custom type clWlanPolicyMobilityAnchor based on TruthValue"""
    defaultValue = 2


_ClWlanPolicyMobilityAnchor_Type.__name__ = "TruthValue"
_ClWlanPolicyMobilityAnchor_Object = MibTableColumn
clWlanPolicyMobilityAnchor = _ClWlanPolicyMobilityAnchor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 57),
    _ClWlanPolicyMobilityAnchor_Type()
)
clWlanPolicyMobilityAnchor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWlanPolicyMobilityAnchor.setStatus("current")


class _CLWlanPolicyBroadcastTagging_Type(TruthValue):
    """Custom type cLWlanPolicyBroadcastTagging based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyBroadcastTagging_Type.__name__ = "TruthValue"
_CLWlanPolicyBroadcastTagging_Object = MibTableColumn
cLWlanPolicyBroadcastTagging = _CLWlanPolicyBroadcastTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 58),
    _CLWlanPolicyBroadcastTagging_Type()
)
cLWlanPolicyBroadcastTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyBroadcastTagging.setStatus("current")


class _CLWlanPolicyWgbVlan_Type(TruthValue):
    """Custom type cLWlanPolicyWgbVlan based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyWgbVlan_Type.__name__ = "TruthValue"
_CLWlanPolicyWgbVlan_Object = MibTableColumn
cLWlanPolicyWgbVlan = _CLWlanPolicyWgbVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 59),
    _CLWlanPolicyWgbVlan_Type()
)
cLWlanPolicyWgbVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyWgbVlan.setStatus("current")


class _CLWlanPolicyReanchorClassmap_Type(SnmpAdminString):
    """Custom type cLWlanPolicyReanchorClassmap based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyReanchorClassmap_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyReanchorClassmap_Object = MibTableColumn
cLWlanPolicyReanchorClassmap = _CLWlanPolicyReanchorClassmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 60),
    _CLWlanPolicyReanchorClassmap_Type()
)
cLWlanPolicyReanchorClassmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyReanchorClassmap.setStatus("current")


class _CLWlanUmbrellaParamMapName_Type(SnmpAdminString):
    """Custom type cLWlanUmbrellaParamMapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanUmbrellaParamMapName_Type.__name__ = "SnmpAdminString"
_CLWlanUmbrellaParamMapName_Object = MibTableColumn
cLWlanUmbrellaParamMapName = _CLWlanUmbrellaParamMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 61),
    _CLWlanUmbrellaParamMapName_Type()
)
cLWlanUmbrellaParamMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanUmbrellaParamMapName.setStatus("current")


class _CLWlanPolicyAccountingList_Type(SnmpAdminString):
    """Custom type cLWlanPolicyAccountingList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyAccountingList_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyAccountingList_Object = MibTableColumn
cLWlanPolicyAccountingList = _CLWlanPolicyAccountingList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 62),
    _CLWlanPolicyAccountingList_Type()
)
cLWlanPolicyAccountingList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyAccountingList.setStatus("current")


class _CLWlanPolicyAAAPolicyName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyAAAPolicyName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyAAAPolicyName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyAAAPolicyName_Object = MibTableColumn
cLWlanPolicyAAAPolicyName = _CLWlanPolicyAAAPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 63),
    _CLWlanPolicyAAAPolicyName_Type()
)
cLWlanPolicyAAAPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyAAAPolicyName.setStatus("current")


class _CLWlanPolicyQosCallSnooping_Type(TruthValue):
    """Custom type cLWlanPolicyQosCallSnooping based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyQosCallSnooping_Type.__name__ = "TruthValue"
_CLWlanPolicyQosCallSnooping_Object = MibTableColumn
cLWlanPolicyQosCallSnooping = _CLWlanPolicyQosCallSnooping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 64),
    _CLWlanPolicyQosCallSnooping_Type()
)
cLWlanPolicyQosCallSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyQosCallSnooping.setStatus("current")


class _CLWlanPolicyDefaultSgt_Type(Unsigned32):
    """Custom type cLWlanPolicyDefaultSgt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65519),
    )


_CLWlanPolicyDefaultSgt_Type.__name__ = "Unsigned32"
_CLWlanPolicyDefaultSgt_Object = MibTableColumn
cLWlanPolicyDefaultSgt = _CLWlanPolicyDefaultSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 65),
    _CLWlanPolicyDefaultSgt_Type()
)
cLWlanPolicyDefaultSgt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyDefaultSgt.setStatus("current")


class _CLWlanPolicyInlineTagging_Type(TruthValue):
    """Custom type cLWlanPolicyInlineTagging based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyInlineTagging_Type.__name__ = "TruthValue"
_CLWlanPolicyInlineTagging_Object = MibTableColumn
cLWlanPolicyInlineTagging = _CLWlanPolicyInlineTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 66),
    _CLWlanPolicyInlineTagging_Type()
)
cLWlanPolicyInlineTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyInlineTagging.setStatus("current")


class _CLWlanPolicySgaclEnforcement_Type(TruthValue):
    """Custom type cLWlanPolicySgaclEnforcement based on TruthValue"""
    defaultValue = 2


_CLWlanPolicySgaclEnforcement_Type.__name__ = "TruthValue"
_CLWlanPolicySgaclEnforcement_Object = MibTableColumn
cLWlanPolicySgaclEnforcement = _CLWlanPolicySgaclEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 67),
    _CLWlanPolicySgaclEnforcement_Type()
)
cLWlanPolicySgaclEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicySgaclEnforcement.setStatus("current")


class _CLWlanPolicyMdnsPolicy_Type(SnmpAdminString):
    """Custom type cLWlanPolicyMdnsPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanPolicyMdnsPolicy_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyMdnsPolicy_Object = MibTableColumn
cLWlanPolicyMdnsPolicy = _CLWlanPolicyMdnsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 68),
    _CLWlanPolicyMdnsPolicy_Type()
)
cLWlanPolicyMdnsPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyMdnsPolicy.setStatus("current")


class _CLWlanPolicyHotspotAnqpServer_Type(SnmpAdminString):
    """Custom type cLWlanPolicyHotspotAnqpServer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CLWlanPolicyHotspotAnqpServer_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyHotspotAnqpServer_Object = MibTableColumn
cLWlanPolicyHotspotAnqpServer = _CLWlanPolicyHotspotAnqpServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 69),
    _CLWlanPolicyHotspotAnqpServer_Type()
)
cLWlanPolicyHotspotAnqpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyHotspotAnqpServer.setStatus("current")


class _CLWlanPolicyNacType_Type(Integer32):
    """Custom type cLWlanPolicyNacType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("radius", 0),
          ("xwf", 1))
    )


_CLWlanPolicyNacType_Type.__name__ = "Integer32"
_CLWlanPolicyNacType_Object = MibTableColumn
cLWlanPolicyNacType = _CLWlanPolicyNacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 70),
    _CLWlanPolicyNacType_Type()
)
cLWlanPolicyNacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyNacType.setStatus("deprecated")


class _CLWlanPolicyARPProxy_Type(TruthValue):
    """Custom type cLWlanPolicyARPProxy based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyARPProxy_Type.__name__ = "TruthValue"
_CLWlanPolicyARPProxy_Object = MibTableColumn
cLWlanPolicyARPProxy = _CLWlanPolicyARPProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 71),
    _CLWlanPolicyARPProxy_Type()
)
cLWlanPolicyARPProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyARPProxy.setStatus("current")


class _CLWlanPolicyIPv6proxy_Type(Integer32):
    """Custom type cLWlanPolicyIPv6proxy based on Integer32"""
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
        *(("noproxy", 1),
          ("dadproxy", 2),
          ("fullproxy", 3))
    )


_CLWlanPolicyIPv6proxy_Type.__name__ = "Integer32"
_CLWlanPolicyIPv6proxy_Object = MibTableColumn
cLWlanPolicyIPv6proxy = _CLWlanPolicyIPv6proxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 72),
    _CLWlanPolicyIPv6proxy_Type()
)
cLWlanPolicyIPv6proxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyIPv6proxy.setStatus("current")


class _CLWlanPolicyMulticastFilter_Type(TruthValue):
    """Custom type cLWlanPolicyMulticastFilter based on TruthValue"""
    defaultValue = 1


_CLWlanPolicyMulticastFilter_Type.__name__ = "TruthValue"
_CLWlanPolicyMulticastFilter_Object = MibTableColumn
cLWlanPolicyMulticastFilter = _CLWlanPolicyMulticastFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 73),
    _CLWlanPolicyMulticastFilter_Type()
)
cLWlanPolicyMulticastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyMulticastFilter.setStatus("current")


class _CLWlanPolicyQBSSLoad_Type(TruthValue):
    """Custom type cLWlanPolicyQBSSLoad based on TruthValue"""
    defaultValue = 1


_CLWlanPolicyQBSSLoad_Type.__name__ = "TruthValue"
_CLWlanPolicyQBSSLoad_Object = MibTableColumn
cLWlanPolicyQBSSLoad = _CLWlanPolicyQBSSLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 74),
    _CLWlanPolicyQBSSLoad_Type()
)
cLWlanPolicyQBSSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyQBSSLoad.setStatus("current")


class _CLWlanPolicyL3Access_Type(TruthValue):
    """Custom type cLWlanPolicyL3Access based on TruthValue"""
    defaultValue = 2


_CLWlanPolicyL3Access_Type.__name__ = "TruthValue"
_CLWlanPolicyL3Access_Object = MibTableColumn
cLWlanPolicyL3Access = _CLWlanPolicyL3Access_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 1, 1, 75),
    _CLWlanPolicyL3Access_Type()
)
cLWlanPolicyL3Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyL3Access.setStatus("current")
_CLWlanPolicyATFPolicyNameConfigTable_Object = MibTable
cLWlanPolicyATFPolicyNameConfigTable = _CLWlanPolicyATFPolicyNameConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLWlanPolicyATFPolicyNameConfigTable.setStatus("current")
_CLWlanPolicyATFPolicyNameConfigEntry_Object = MibTableRow
cLWlanPolicyATFPolicyNameConfigEntry = _CLWlanPolicyATFPolicyNameConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 2, 1)
)
cLWlanPolicyATFPolicyNameConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanWlanPolicyName"),
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBandId"),
)
if mibBuilder.loadTexts:
    cLWlanPolicyATFPolicyNameConfigEntry.setStatus("current")


class _CLWlanPolicyBandId_Type(Unsigned32):
    """Custom type cLWlanPolicyBandId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CLWlanPolicyBandId_Type.__name__ = "Unsigned32"
_CLWlanPolicyBandId_Object = MibTableColumn
cLWlanPolicyBandId = _CLWlanPolicyBandId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 2, 1, 1),
    _CLWlanPolicyBandId_Type()
)
cLWlanPolicyBandId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanPolicyBandId.setStatus("current")
_CLWlanPolicyATFRowStatus_Type = RowStatus
_CLWlanPolicyATFRowStatus_Object = MibTableColumn
cLWlanPolicyATFRowStatus = _CLWlanPolicyATFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 2, 1, 2),
    _CLWlanPolicyATFRowStatus_Type()
)
cLWlanPolicyATFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanPolicyATFRowStatus.setStatus("current")


class _CLWlanPolicyATFPolicyName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyATFPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLWlanPolicyATFPolicyName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyATFPolicyName_Object = MibTableColumn
cLWlanPolicyATFPolicyName = _CLWlanPolicyATFPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 2, 1, 3),
    _CLWlanPolicyATFPolicyName_Type()
)
cLWlanPolicyATFPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyATFPolicyName.setStatus("current")
_CLWlanAaaPolicyConfigTable_Object = MibTable
cLWlanAaaPolicyConfigTable = _CLWlanAaaPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cLWlanAaaPolicyConfigTable.setStatus("current")
_CLWlanAaaPolicyConfigEntry_Object = MibTableRow
cLWlanAaaPolicyConfigEntry = _CLWlanAaaPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1)
)
cLWlanAaaPolicyConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanAaaPolicyName"),
)
if mibBuilder.loadTexts:
    cLWlanAaaPolicyConfigEntry.setStatus("current")


class _CLWlanAaaPolicyName_Type(SnmpAdminString):
    """Custom type cLWlanAaaPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLWlanAaaPolicyName_Type.__name__ = "SnmpAdminString"
_CLWlanAaaPolicyName_Object = MibTableColumn
cLWlanAaaPolicyName = _CLWlanAaaPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1, 1),
    _CLWlanAaaPolicyName_Type()
)
cLWlanAaaPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanAaaPolicyName.setStatus("current")
_CLWlanAaaPolicyRowStatus_Type = RowStatus
_CLWlanAaaPolicyRowStatus_Object = MibTableColumn
cLWlanAaaPolicyRowStatus = _CLWlanAaaPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1, 2),
    _CLWlanAaaPolicyRowStatus_Type()
)
cLWlanAaaPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanAaaPolicyRowStatus.setStatus("current")


class _CLWlanAaaPolicyNasId1_Type(Integer32):
    """Custom type cLWlanAaaPolicyNasId1 based on Integer32"""
    defaultValue = 1

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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("notconfigured", 0),
          ("sysname", 1),
          ("sysip", 2),
          ("sysmac", 3),
          ("apip", 4),
          ("apname", 5),
          ("apmac", 6),
          ("apethmac", 7),
          ("appolicytag", 8),
          ("apsitetag", 9),
          ("ssid", 10),
          ("aplocation", 11),
          ("customstring", 12))
    )


_CLWlanAaaPolicyNasId1_Type.__name__ = "Integer32"
_CLWlanAaaPolicyNasId1_Object = MibTableColumn
cLWlanAaaPolicyNasId1 = _CLWlanAaaPolicyNasId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1, 3),
    _CLWlanAaaPolicyNasId1_Type()
)
cLWlanAaaPolicyNasId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanAaaPolicyNasId1.setStatus("current")


class _CLWlanAaaPolicyNasId2_Type(Integer32):
    """Custom type cLWlanAaaPolicyNasId2 based on Integer32"""
    defaultValue = 0

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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("notconfigured", 0),
          ("sysname", 1),
          ("sysip", 2),
          ("sysmac", 3),
          ("apip", 4),
          ("apname", 5),
          ("apmac", 6),
          ("apethmac", 7),
          ("appolicytag", 8),
          ("apsitetag", 9),
          ("ssid", 10),
          ("aplocation", 11),
          ("customstring", 12))
    )


_CLWlanAaaPolicyNasId2_Type.__name__ = "Integer32"
_CLWlanAaaPolicyNasId2_Object = MibTableColumn
cLWlanAaaPolicyNasId2 = _CLWlanAaaPolicyNasId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1, 4),
    _CLWlanAaaPolicyNasId2_Type()
)
cLWlanAaaPolicyNasId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanAaaPolicyNasId2.setStatus("current")


class _CLWlanAaaPolicyNasId3_Type(Integer32):
    """Custom type cLWlanAaaPolicyNasId3 based on Integer32"""
    defaultValue = 0

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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("notconfigured", 0),
          ("sysname", 1),
          ("sysip", 2),
          ("sysmac", 3),
          ("apip", 4),
          ("apname", 5),
          ("apmac", 6),
          ("apethmac", 7),
          ("appolicytag", 8),
          ("apsitetag", 9),
          ("ssid", 10),
          ("aplocation", 11),
          ("customstring", 12))
    )


_CLWlanAaaPolicyNasId3_Type.__name__ = "Integer32"
_CLWlanAaaPolicyNasId3_Object = MibTableColumn
cLWlanAaaPolicyNasId3 = _CLWlanAaaPolicyNasId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1, 5),
    _CLWlanAaaPolicyNasId3_Type()
)
cLWlanAaaPolicyNasId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanAaaPolicyNasId3.setStatus("current")


class _CLWlanAaaPolicyRealm_Type(TruthValue):
    """Custom type cLWlanAaaPolicyRealm based on TruthValue"""
    defaultValue = 1


_CLWlanAaaPolicyRealm_Type.__name__ = "TruthValue"
_CLWlanAaaPolicyRealm_Object = MibTableColumn
cLWlanAaaPolicyRealm = _CLWlanAaaPolicyRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1, 6),
    _CLWlanAaaPolicyRealm_Type()
)
cLWlanAaaPolicyRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanAaaPolicyRealm.setStatus("current")


class _CLWlanAAAPolicyCustomString1_Type(SnmpAdminString):
    """Custom type cLWlanAAAPolicyCustomString1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 224),
    )


_CLWlanAAAPolicyCustomString1_Type.__name__ = "SnmpAdminString"
_CLWlanAAAPolicyCustomString1_Object = MibTableColumn
cLWlanAAAPolicyCustomString1 = _CLWlanAAAPolicyCustomString1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1, 7),
    _CLWlanAAAPolicyCustomString1_Type()
)
cLWlanAAAPolicyCustomString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanAAAPolicyCustomString1.setStatus("current")


class _CLWlanAAAPolicyCustomString2_Type(SnmpAdminString):
    """Custom type cLWlanAAAPolicyCustomString2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 224),
    )


_CLWlanAAAPolicyCustomString2_Type.__name__ = "SnmpAdminString"
_CLWlanAAAPolicyCustomString2_Object = MibTableColumn
cLWlanAAAPolicyCustomString2 = _CLWlanAAAPolicyCustomString2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1, 8),
    _CLWlanAAAPolicyCustomString2_Type()
)
cLWlanAAAPolicyCustomString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanAAAPolicyCustomString2.setStatus("current")


class _CLWlanAAAPolicyCustomString3_Type(SnmpAdminString):
    """Custom type cLWlanAAAPolicyCustomString3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 224),
    )


_CLWlanAAAPolicyCustomString3_Type.__name__ = "SnmpAdminString"
_CLWlanAAAPolicyCustomString3_Object = MibTableColumn
cLWlanAAAPolicyCustomString3 = _CLWlanAAAPolicyCustomString3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 3, 1, 9),
    _CLWlanAAAPolicyCustomString3_Type()
)
cLWlanAAAPolicyCustomString3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanAAAPolicyCustomString3.setStatus("current")
_CLWlanPolicyMonitorIPv4InConfigTable_Object = MibTable
cLWlanPolicyMonitorIPv4InConfigTable = _CLWlanPolicyMonitorIPv4InConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cLWlanPolicyMonitorIPv4InConfigTable.setStatus("current")
_CLWlanPolicyMonitorIPv4InConfigEntry_Object = MibTableRow
cLWlanPolicyMonitorIPv4InConfigEntry = _CLWlanPolicyMonitorIPv4InConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 4, 1)
)
cLWlanPolicyMonitorIPv4InConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanWlanPolicyName"),
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanMonitorIPv4InName"),
)
if mibBuilder.loadTexts:
    cLWlanPolicyMonitorIPv4InConfigEntry.setStatus("current")


class _CLWlanMonitorIPv4InName_Type(SnmpAdminString):
    """Custom type cLWlanMonitorIPv4InName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLWlanMonitorIPv4InName_Type.__name__ = "SnmpAdminString"
_CLWlanMonitorIPv4InName_Object = MibTableColumn
cLWlanMonitorIPv4InName = _CLWlanMonitorIPv4InName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 4, 1, 1),
    _CLWlanMonitorIPv4InName_Type()
)
cLWlanMonitorIPv4InName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanMonitorIPv4InName.setStatus("current")
_CLWlanMonitorIPv4InRowStatus_Type = RowStatus
_CLWlanMonitorIPv4InRowStatus_Object = MibTableColumn
cLWlanMonitorIPv4InRowStatus = _CLWlanMonitorIPv4InRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 4, 1, 2),
    _CLWlanMonitorIPv4InRowStatus_Type()
)
cLWlanMonitorIPv4InRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMonitorIPv4InRowStatus.setStatus("current")
_CLWlanPolicyMonitorIPv4OutConfigTable_Object = MibTable
cLWlanPolicyMonitorIPv4OutConfigTable = _CLWlanPolicyMonitorIPv4OutConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cLWlanPolicyMonitorIPv4OutConfigTable.setStatus("current")
_CLWlanPolicyMonitorIPv4OutConfigEntry_Object = MibTableRow
cLWlanPolicyMonitorIPv4OutConfigEntry = _CLWlanPolicyMonitorIPv4OutConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 5, 1)
)
cLWlanPolicyMonitorIPv4OutConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanWlanPolicyName"),
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanMonitorIPv4OutName"),
)
if mibBuilder.loadTexts:
    cLWlanPolicyMonitorIPv4OutConfigEntry.setStatus("current")


class _CLWlanMonitorIPv4OutName_Type(SnmpAdminString):
    """Custom type cLWlanMonitorIPv4OutName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLWlanMonitorIPv4OutName_Type.__name__ = "SnmpAdminString"
_CLWlanMonitorIPv4OutName_Object = MibTableColumn
cLWlanMonitorIPv4OutName = _CLWlanMonitorIPv4OutName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 5, 1, 1),
    _CLWlanMonitorIPv4OutName_Type()
)
cLWlanMonitorIPv4OutName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanMonitorIPv4OutName.setStatus("current")
_CLWlanMonitorIPv4OutRowStatus_Type = RowStatus
_CLWlanMonitorIPv4OutRowStatus_Object = MibTableColumn
cLWlanMonitorIPv4OutRowStatus = _CLWlanMonitorIPv4OutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 5, 1, 2),
    _CLWlanMonitorIPv4OutRowStatus_Type()
)
cLWlanMonitorIPv4OutRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMonitorIPv4OutRowStatus.setStatus("current")
_CLWlanPolicyMonitorIPv6InConfigTable_Object = MibTable
cLWlanPolicyMonitorIPv6InConfigTable = _CLWlanPolicyMonitorIPv6InConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cLWlanPolicyMonitorIPv6InConfigTable.setStatus("current")
_CLWlanPolicyMonitorIPv6InConfigEntry_Object = MibTableRow
cLWlanPolicyMonitorIPv6InConfigEntry = _CLWlanPolicyMonitorIPv6InConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 6, 1)
)
cLWlanPolicyMonitorIPv6InConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanWlanPolicyName"),
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanMonitorIPv6InName"),
)
if mibBuilder.loadTexts:
    cLWlanPolicyMonitorIPv6InConfigEntry.setStatus("current")


class _CLWlanMonitorIPv6InName_Type(SnmpAdminString):
    """Custom type cLWlanMonitorIPv6InName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLWlanMonitorIPv6InName_Type.__name__ = "SnmpAdminString"
_CLWlanMonitorIPv6InName_Object = MibTableColumn
cLWlanMonitorIPv6InName = _CLWlanMonitorIPv6InName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 6, 1, 1),
    _CLWlanMonitorIPv6InName_Type()
)
cLWlanMonitorIPv6InName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanMonitorIPv6InName.setStatus("current")
_CLWlanMonitorIPv6InRowStatus_Type = RowStatus
_CLWlanMonitorIPv6InRowStatus_Object = MibTableColumn
cLWlanMonitorIPv6InRowStatus = _CLWlanMonitorIPv6InRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 6, 1, 2),
    _CLWlanMonitorIPv6InRowStatus_Type()
)
cLWlanMonitorIPv6InRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMonitorIPv6InRowStatus.setStatus("current")
_CLWlanPolicyMonitorIPv6OutConfigTable_Object = MibTable
cLWlanPolicyMonitorIPv6OutConfigTable = _CLWlanPolicyMonitorIPv6OutConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cLWlanPolicyMonitorIPv6OutConfigTable.setStatus("current")
_CLWlanPolicyMonitorIPv6OutConfigEntry_Object = MibTableRow
cLWlanPolicyMonitorIPv6OutConfigEntry = _CLWlanPolicyMonitorIPv6OutConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 7, 1)
)
cLWlanPolicyMonitorIPv6OutConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanWlanPolicyName"),
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanMonitorIPv6OutName"),
)
if mibBuilder.loadTexts:
    cLWlanPolicyMonitorIPv6OutConfigEntry.setStatus("current")


class _CLWlanMonitorIPv6OutName_Type(SnmpAdminString):
    """Custom type cLWlanMonitorIPv6OutName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLWlanMonitorIPv6OutName_Type.__name__ = "SnmpAdminString"
_CLWlanMonitorIPv6OutName_Object = MibTableColumn
cLWlanMonitorIPv6OutName = _CLWlanMonitorIPv6OutName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 7, 1, 1),
    _CLWlanMonitorIPv6OutName_Type()
)
cLWlanMonitorIPv6OutName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanMonitorIPv6OutName.setStatus("current")
_CLWlanMonitorIPv6OutRowStatus_Type = RowStatus
_CLWlanMonitorIPv6OutRowStatus_Object = MibTableColumn
cLWlanMonitorIPv6OutRowStatus = _CLWlanMonitorIPv6OutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 7, 1, 2),
    _CLWlanMonitorIPv6OutRowStatus_Type()
)
cLWlanMonitorIPv6OutRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMonitorIPv6OutRowStatus.setStatus("current")
_CLWlanPolicyCalendarProfileTable_Object = MibTable
cLWlanPolicyCalendarProfileTable = _CLWlanPolicyCalendarProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cLWlanPolicyCalendarProfileTable.setStatus("current")
_CLWlanPolicyCalendarProfileEntry_Object = MibTableRow
cLWlanPolicyCalendarProfileEntry = _CLWlanPolicyCalendarProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 8, 1)
)
cLWlanPolicyCalendarProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanWlanPolicyName"),
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCalendarProfileName"),
)
if mibBuilder.loadTexts:
    cLWlanPolicyCalendarProfileEntry.setStatus("current")


class _CLWlanPolicyCalendarProfileName_Type(SnmpAdminString):
    """Custom type cLWlanPolicyCalendarProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLWlanPolicyCalendarProfileName_Type.__name__ = "SnmpAdminString"
_CLWlanPolicyCalendarProfileName_Object = MibTableColumn
cLWlanPolicyCalendarProfileName = _CLWlanPolicyCalendarProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 8, 1, 1),
    _CLWlanPolicyCalendarProfileName_Type()
)
cLWlanPolicyCalendarProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanPolicyCalendarProfileName.setStatus("current")
_CLWlanPolicyCalendarProfileRowStatus_Type = RowStatus
_CLWlanPolicyCalendarProfileRowStatus_Object = MibTableColumn
cLWlanPolicyCalendarProfileRowStatus = _CLWlanPolicyCalendarProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 8, 1, 2),
    _CLWlanPolicyCalendarProfileRowStatus_Type()
)
cLWlanPolicyCalendarProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanPolicyCalendarProfileRowStatus.setStatus("current")


class _CLWlanPolicyCalendarProfileWlan_Type(Integer32):
    """Custom type cLWlanPolicyCalendarProfileWlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("enable", 1))
    )


_CLWlanPolicyCalendarProfileWlan_Type.__name__ = "Integer32"
_CLWlanPolicyCalendarProfileWlan_Object = MibTableColumn
cLWlanPolicyCalendarProfileWlan = _CLWlanPolicyCalendarProfileWlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 8, 1, 3),
    _CLWlanPolicyCalendarProfileWlan_Type()
)
cLWlanPolicyCalendarProfileWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyCalendarProfileWlan.setStatus("current")


class _CLWlanPolicyCalendarProfileClientSession_Type(Integer32):
    """Custom type cLWlanPolicyCalendarProfileClientSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("block", 2))
    )


_CLWlanPolicyCalendarProfileClientSession_Type.__name__ = "Integer32"
_CLWlanPolicyCalendarProfileClientSession_Object = MibTableColumn
cLWlanPolicyCalendarProfileClientSession = _CLWlanPolicyCalendarProfileClientSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 1, 2, 8, 1, 4),
    _CLWlanPolicyCalendarProfileClientSession_Type()
)
cLWlanPolicyCalendarProfileClientSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanPolicyCalendarProfileClientSession.setStatus("current")
_CiscoLwappWlanPolicyConform_ObjectIdentity = ObjectIdentity
ciscoLwappWlanPolicyConform = _CiscoLwappWlanPolicyConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3)
)
_CiscoLwappWlanPolicyCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappWlanPolicyCompliances = _CiscoLwappWlanPolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 1)
)
_CiscoLwappWlanPolicyGroups_ObjectIdentity = ObjectIdentity
ciscoLwappWlanPolicyGroups = _CiscoLwappWlanPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2)
)

# Managed Objects groups

ciscoLwappWlanPolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 1)
)
ciscoLwappWlanPolicyConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPlcyRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDescription"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInterfaceName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralSwitchMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralAuthMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNatPatEnabled"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAssocCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv4AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv6AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyL2AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySessionTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyClientExclTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNativeProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySubscriberPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyHttpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNetflowIPv4InputMonitorName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNetflowIPv4OutputMonitorName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNetflowIPv6InputMonitorName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNetflowIPv6OutputMonitorName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistingCapability"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpRequired"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpServerIpAddress"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAaaOverride"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyRadiusHttpProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleThreshold"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosFastlane"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ascii"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Rid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Enable"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apethmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apname"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Policytag"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Aplocation"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Vlanid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ssid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySplitMacAcl"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyVlanCentralSwitching"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyPassiveClient"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNBARProtocolDiscovery"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStaticIPMobility"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyConfigGroup.setStatus("deprecated")

ciscoLwappWlanPolicyConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 2)
)
ciscoLwappWlanPolicyConfigGroupRev1.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPlcyRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDescription"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInterfaceName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralSwitchMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralAuthMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNatPatEnabled"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAssocCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv4AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv6AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyL2AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySessionTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyClientExclTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNativeProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySubscriberPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyHttpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNetflowIPv4InputMonitorName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNetflowIPv4OutputMonitorName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNetflowIPv6InputMonitorName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNetflowIPv6OutputMonitorName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistingCapability"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpRequired"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpServerIpAddress"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAaaOverride"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyRadiusHttpProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleThreshold"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosFastlane"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ascii"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Rid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Enable"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apethmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apname"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Policytag"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Aplocation"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Vlanid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ssid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySplitMacAcl"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyVlanCentralSwitching"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyPassiveClient"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNBARProtocolDiscovery"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStaticIPMobility"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "clWlanPolicyMobilityAnchor"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBroadcastTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyWgbVlan"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyReanchorClassmap"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanUmbrellaParamMapName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAccountingList"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAAAPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosCallSnooping"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDefaultSgt"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInlineTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySgaclEnforcement"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyConfigGroupRev1.setStatus("deprecated")

ciscoLwappWlanPolicyATFConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 3)
)
ciscoLwappWlanPolicyATFConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyATFRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyATFPolicyName"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyATFConfigGroup.setStatus("current")

ciscoLwappWlanAaaPolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 4)
)
ciscoLwappWlanAaaPolicyConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanAaaPolicyRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanAaaPolicyNasId1"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanAaaPolicyNasId2"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanAaaPolicyNasId3"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanAaaPolicyRealm"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanAaaPolicyConfigGroup.setStatus("current")

ciscoLwappWlanPolicyConfigGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 5)
)
ciscoLwappWlanPolicyConfigGroupRev2.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPlcyRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDescription"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInterfaceName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralSwitchMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralAuthMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNatPatEnabled"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAssocCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv4AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv6AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyL2AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySessionTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyClientExclTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNativeProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySubscriberPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyHttpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistingCapability"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpRequired"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpServerIpAddress"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAaaOverride"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyRadiusHttpProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleThreshold"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosFastlane"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ascii"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Rid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Enable"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apethmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apname"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Policytag"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Aplocation"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Vlanid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ssid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySplitMacAcl"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyVlanCentralSwitching"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyPassiveClient"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNBARProtocolDiscovery"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStaticIPMobility"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "clWlanPolicyMobilityAnchor"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBroadcastTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyWgbVlan"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyReanchorClassmap"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanUmbrellaParamMapName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAccountingList"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAAAPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosCallSnooping"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDefaultSgt"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInlineTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySgaclEnforcement"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyConfigGroupRev2.setStatus("deprecated")

ciscoLwappWlanPolicyConfigGroupFlowMonitor = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 6)
)
ciscoLwappWlanPolicyConfigGroupFlowMonitor.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanMonitorIPv4InRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanMonitorIPv4OutRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanMonitorIPv6InRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanMonitorIPv6OutRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyConfigGroupFlowMonitor.setStatus("current")

ciscoLwappWlanPolicyConfigGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 7)
)
ciscoLwappWlanPolicyConfigGroupRev3.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPlcyRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDescription"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInterfaceName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralSwitchMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralAuthMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNatPatEnabled"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAssocCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv4AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv6AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyL2AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySessionTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyClientExclTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNativeProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySubscriberPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyHttpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistingCapability"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpRequired"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpServerIpAddress"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAaaOverride"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyRadiusHttpProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleThreshold"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosFastlane"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ascii"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Rid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Enable"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apethmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apname"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Policytag"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Aplocation"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Vlanid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ssid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySplitMacAcl"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyVlanCentralSwitching"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyPassiveClient"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNBARProtocolDiscovery"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStaticIPMobility"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "clWlanPolicyMobilityAnchor"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBroadcastTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyWgbVlan"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyReanchorClassmap"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanUmbrellaParamMapName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAccountingList"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAAAPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosCallSnooping"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDefaultSgt"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInlineTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySgaclEnforcement"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyMdnsPolicy"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyHotspotAnqpServer"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyConfigGroupRev3.setStatus("deprecated")

ciscoLwappWlanPolicyConfigGroupCalenderProfile = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 8)
)
ciscoLwappWlanPolicyConfigGroupCalenderProfile.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCalendarProfileRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCalendarProfileWlan"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCalendarProfileClientSession"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyConfigGroupCalenderProfile.setStatus("current")

ciscoLwappWlanPolicyConfigGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 9)
)
ciscoLwappWlanPolicyConfigGroupRev4.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPlcyRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDescription"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInterfaceName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralSwitchMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralAuthMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNatPatEnabled"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAssocCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv4AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv6AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyL2AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySessionTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyClientExclTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNativeProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySubscriberPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyHttpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistingCapability"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpRequired"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpServerIpAddress"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAaaOverride"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyRadiusHttpProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleThreshold"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosFastlane"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ascii"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Rid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Enable"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apethmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apname"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Policytag"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Aplocation"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Vlanid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ssid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySplitMacAcl"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyVlanCentralSwitching"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyPassiveClient"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNBARProtocolDiscovery"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStaticIPMobility"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "clWlanPolicyMobilityAnchor"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBroadcastTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyWgbVlan"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyReanchorClassmap"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanUmbrellaParamMapName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAccountingList"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAAAPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosCallSnooping"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDefaultSgt"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInlineTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySgaclEnforcement"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyMdnsPolicy"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyHotspotAnqpServer"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNacType"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyARPProxy"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv6proxy"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyMulticastFilter"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQBSSLoad"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyConfigGroupRev4.setStatus("deprecated")

ciscoLwappWlanPolicyConfigGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 2, 10)
)
ciscoLwappWlanPolicyConfigGroupRev5.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPlcyRowStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDescription"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInterfaceName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralSwitchMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyCentralAuthMode"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNatPatEnabled"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAssocCentral"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv4AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv6AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyL2AclName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySessionTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyClientExclTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNativeProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySubscriberPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyHttpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDInput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosPerBSSIDOutput"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistTimeout"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBlacklistingCapability"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpRequired"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDhcpServerIpAddress"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAaaOverride"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStatus"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyRadiusHttpProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyUserIdleThreshold"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosFastlane"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ascii"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Rid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Enable"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apethmac"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Apname"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Policytag"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Aplocation"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Vlanid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDHCPOption82Ssid"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySplitMacAcl"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyVlanCentralSwitching"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyPassiveClient"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyNBARProtocolDiscovery"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyStaticIPMobility"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "clWlanPolicyMobilityAnchor"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyBroadcastTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyWgbVlan"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyReanchorClassmap"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanUmbrellaParamMapName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAccountingList"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyAAAPolicyName"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQosCallSnooping"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyDefaultSgt"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyInlineTagging"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicySgaclEnforcement"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyMdnsPolicy"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyHotspotAnqpServer"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyARPProxy"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyIPv6proxy"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyMulticastFilter"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanPolicyQBSSLoad"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyConfigGroupRev5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappWlanPolicyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 1, 1)
)
ciscoLwappWlanPolicyCompliance.setObjects(
    ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyCompliance.setStatus(
        "deprecated"
    )

ciscoLwappWlanPolicyComplianceR01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 1, 2)
)
ciscoLwappWlanPolicyComplianceR01.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupRev1"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyATFConfigGroup"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanAaaPolicyConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyComplianceR01.setStatus(
        "deprecated"
    )

ciscoLwappWlanPolicyComplianceR02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 1, 3)
)
ciscoLwappWlanPolicyComplianceR02.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupRev2"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyATFConfigGroup"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanAaaPolicyConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyComplianceR02.setStatus(
        "deprecated"
    )

ciscoLwappWlanPolicyComplianceR03 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 1, 4)
)
ciscoLwappWlanPolicyComplianceR03.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupRev2"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyATFConfigGroup"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanAaaPolicyConfigGroup"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupFlowMonitor"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyComplianceR03.setStatus(
        "deprecated"
    )

ciscoLwappWlanPolicyComplianceR04 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 1, 5)
)
ciscoLwappWlanPolicyComplianceR04.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupRev3"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyATFConfigGroup"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanAaaPolicyConfigGroup"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupFlowMonitor"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupCalenderProfile"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyComplianceR04.setStatus(
        "deprecated"
    )

ciscoLwappWlanPolicyComplianceR05 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 853, 3, 1, 6)
)
ciscoLwappWlanPolicyComplianceR05.setObjects(
      *(("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupRev4"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyATFConfigGroup"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanAaaPolicyConfigGroup"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupFlowMonitor"),
        ("CISCO-LWAPP-WLAN-POLICY-MIB", "ciscoLwappWlanPolicyConfigGroupCalenderProfile"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanPolicyComplianceR05.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-WLAN-POLICY-MIB",
    **{"ciscoCapwapWlanPolicyMIB": ciscoCapwapWlanPolicyMIB,
       "ciscoLwappWlanPolicyMIBNotifs": ciscoLwappWlanPolicyMIBNotifs,
       "ciscoLwappWlanPolicyMIBObjects": ciscoLwappWlanPolicyMIBObjects,
       "ciscoLwappWlanPolicyConfig": ciscoLwappWlanPolicyConfig,
       "cLWlanPolicyConfigTable": cLWlanPolicyConfigTable,
       "cLWlanPolicyConfigEntry": cLWlanPolicyConfigEntry,
       "cLWlanWlanPolicyName": cLWlanWlanPolicyName,
       "cLWlanPlcyRowStatus": cLWlanPlcyRowStatus,
       "cLWlanPolicyDescription": cLWlanPolicyDescription,
       "cLWlanPolicyInterfaceName": cLWlanPolicyInterfaceName,
       "cLWlanPolicyCentralSwitchMode": cLWlanPolicyCentralSwitchMode,
       "cLWlanPolicyCentralAuthMode": cLWlanPolicyCentralAuthMode,
       "cLWlanPolicyDhcpCentral": cLWlanPolicyDhcpCentral,
       "cLWlanPolicyNatPatEnabled": cLWlanPolicyNatPatEnabled,
       "cLWlanPolicyAssocCentral": cLWlanPolicyAssocCentral,
       "cLWlanPolicyIPv4AclName": cLWlanPolicyIPv4AclName,
       "cLWlanPolicyIPv6AclName": cLWlanPolicyIPv6AclName,
       "cLWlanPolicyL2AclName": cLWlanPolicyL2AclName,
       "cLWlanPolicySessionTimeout": cLWlanPolicySessionTimeout,
       "cLWlanPolicyUserIdleTimeout": cLWlanPolicyUserIdleTimeout,
       "cLWlanPolicyClientExclTimeout": cLWlanPolicyClientExclTimeout,
       "cLWlanPolicyNativeProfiling": cLWlanPolicyNativeProfiling,
       "cLWlanPolicySubscriberPolicyName": cLWlanPolicySubscriberPolicyName,
       "cLWlanPolicyHttpDeviceProfiling": cLWlanPolicyHttpDeviceProfiling,
       "cLWlanPolicyDHCPDeviceProfiling": cLWlanPolicyDHCPDeviceProfiling,
       "cLWlanPolicyNetflowIPv4InputMonitorName": cLWlanPolicyNetflowIPv4InputMonitorName,
       "cLWlanPolicyNetflowIPv4OutputMonitorName": cLWlanPolicyNetflowIPv4OutputMonitorName,
       "cLWlanPolicyNetflowIPv6InputMonitorName": cLWlanPolicyNetflowIPv6InputMonitorName,
       "cLWlanPolicyNetflowIPv6OutputMonitorName": cLWlanPolicyNetflowIPv6OutputMonitorName,
       "cLWlanPolicyQosPerSSIDInput": cLWlanPolicyQosPerSSIDInput,
       "cLWlanPolicyQosPerSSIDOutput": cLWlanPolicyQosPerSSIDOutput,
       "cLWlanPolicyQosPerBSSIDInput": cLWlanPolicyQosPerBSSIDInput,
       "cLWlanPolicyQosPerBSSIDOutput": cLWlanPolicyQosPerBSSIDOutput,
       "cLWlanPolicyBlacklistTimeout": cLWlanPolicyBlacklistTimeout,
       "cLWlanPolicyBlacklistingCapability": cLWlanPolicyBlacklistingCapability,
       "cLWlanPolicyDhcpRequired": cLWlanPolicyDhcpRequired,
       "cLWlanPolicyDhcpServerIpAddress": cLWlanPolicyDhcpServerIpAddress,
       "cLWlanPolicyAaaOverride": cLWlanPolicyAaaOverride,
       "cLWlanPolicyNac": cLWlanPolicyNac,
       "cLWlanPolicyStatus": cLWlanPolicyStatus,
       "cLWlanPolicyRadiusHttpProfiling": cLWlanPolicyRadiusHttpProfiling,
       "cLWlanPolicyUserIdleThreshold": cLWlanPolicyUserIdleThreshold,
       "cLWlanPolicyQosFastlane": cLWlanPolicyQosFastlane,
       "cLWlanPolicyDHCPOption82Ascii": cLWlanPolicyDHCPOption82Ascii,
       "cLWlanPolicyDHCPOption82Rid": cLWlanPolicyDHCPOption82Rid,
       "cLWlanPolicyDHCPOption82Enable": cLWlanPolicyDHCPOption82Enable,
       "cLWlanPolicyDHCPOption82Apmac": cLWlanPolicyDHCPOption82Apmac,
       "cLWlanPolicyDHCPOption82Apethmac": cLWlanPolicyDHCPOption82Apethmac,
       "cLWlanPolicyDHCPOption82Apname": cLWlanPolicyDHCPOption82Apname,
       "cLWlanPolicyDHCPOption82Policytag": cLWlanPolicyDHCPOption82Policytag,
       "cLWlanPolicyDHCPOption82Aplocation": cLWlanPolicyDHCPOption82Aplocation,
       "cLWlanPolicyDHCPOption82Vlanid": cLWlanPolicyDHCPOption82Vlanid,
       "cLWlanPolicyDHCPOption82Ssid": cLWlanPolicyDHCPOption82Ssid,
       "cLWlanPolicySplitMacAcl": cLWlanPolicySplitMacAcl,
       "cLWlanPolicyVlanCentralSwitching": cLWlanPolicyVlanCentralSwitching,
       "cLWlanPolicyPassiveClient": cLWlanPolicyPassiveClient,
       "cLWlanPolicyNBARProtocolDiscovery": cLWlanPolicyNBARProtocolDiscovery,
       "cLWlanPolicyStaticIPMobility": cLWlanPolicyStaticIPMobility,
       "clWlanPolicyMobilityAnchor": clWlanPolicyMobilityAnchor,
       "cLWlanPolicyBroadcastTagging": cLWlanPolicyBroadcastTagging,
       "cLWlanPolicyWgbVlan": cLWlanPolicyWgbVlan,
       "cLWlanPolicyReanchorClassmap": cLWlanPolicyReanchorClassmap,
       "cLWlanUmbrellaParamMapName": cLWlanUmbrellaParamMapName,
       "cLWlanPolicyAccountingList": cLWlanPolicyAccountingList,
       "cLWlanPolicyAAAPolicyName": cLWlanPolicyAAAPolicyName,
       "cLWlanPolicyQosCallSnooping": cLWlanPolicyQosCallSnooping,
       "cLWlanPolicyDefaultSgt": cLWlanPolicyDefaultSgt,
       "cLWlanPolicyInlineTagging": cLWlanPolicyInlineTagging,
       "cLWlanPolicySgaclEnforcement": cLWlanPolicySgaclEnforcement,
       "cLWlanPolicyMdnsPolicy": cLWlanPolicyMdnsPolicy,
       "cLWlanPolicyHotspotAnqpServer": cLWlanPolicyHotspotAnqpServer,
       "cLWlanPolicyNacType": cLWlanPolicyNacType,
       "cLWlanPolicyARPProxy": cLWlanPolicyARPProxy,
       "cLWlanPolicyIPv6proxy": cLWlanPolicyIPv6proxy,
       "cLWlanPolicyMulticastFilter": cLWlanPolicyMulticastFilter,
       "cLWlanPolicyQBSSLoad": cLWlanPolicyQBSSLoad,
       "cLWlanPolicyL3Access": cLWlanPolicyL3Access,
       "cLWlanPolicyATFPolicyNameConfigTable": cLWlanPolicyATFPolicyNameConfigTable,
       "cLWlanPolicyATFPolicyNameConfigEntry": cLWlanPolicyATFPolicyNameConfigEntry,
       "cLWlanPolicyBandId": cLWlanPolicyBandId,
       "cLWlanPolicyATFRowStatus": cLWlanPolicyATFRowStatus,
       "cLWlanPolicyATFPolicyName": cLWlanPolicyATFPolicyName,
       "cLWlanAaaPolicyConfigTable": cLWlanAaaPolicyConfigTable,
       "cLWlanAaaPolicyConfigEntry": cLWlanAaaPolicyConfigEntry,
       "cLWlanAaaPolicyName": cLWlanAaaPolicyName,
       "cLWlanAaaPolicyRowStatus": cLWlanAaaPolicyRowStatus,
       "cLWlanAaaPolicyNasId1": cLWlanAaaPolicyNasId1,
       "cLWlanAaaPolicyNasId2": cLWlanAaaPolicyNasId2,
       "cLWlanAaaPolicyNasId3": cLWlanAaaPolicyNasId3,
       "cLWlanAaaPolicyRealm": cLWlanAaaPolicyRealm,
       "cLWlanAAAPolicyCustomString1": cLWlanAAAPolicyCustomString1,
       "cLWlanAAAPolicyCustomString2": cLWlanAAAPolicyCustomString2,
       "cLWlanAAAPolicyCustomString3": cLWlanAAAPolicyCustomString3,
       "cLWlanPolicyMonitorIPv4InConfigTable": cLWlanPolicyMonitorIPv4InConfigTable,
       "cLWlanPolicyMonitorIPv4InConfigEntry": cLWlanPolicyMonitorIPv4InConfigEntry,
       "cLWlanMonitorIPv4InName": cLWlanMonitorIPv4InName,
       "cLWlanMonitorIPv4InRowStatus": cLWlanMonitorIPv4InRowStatus,
       "cLWlanPolicyMonitorIPv4OutConfigTable": cLWlanPolicyMonitorIPv4OutConfigTable,
       "cLWlanPolicyMonitorIPv4OutConfigEntry": cLWlanPolicyMonitorIPv4OutConfigEntry,
       "cLWlanMonitorIPv4OutName": cLWlanMonitorIPv4OutName,
       "cLWlanMonitorIPv4OutRowStatus": cLWlanMonitorIPv4OutRowStatus,
       "cLWlanPolicyMonitorIPv6InConfigTable": cLWlanPolicyMonitorIPv6InConfigTable,
       "cLWlanPolicyMonitorIPv6InConfigEntry": cLWlanPolicyMonitorIPv6InConfigEntry,
       "cLWlanMonitorIPv6InName": cLWlanMonitorIPv6InName,
       "cLWlanMonitorIPv6InRowStatus": cLWlanMonitorIPv6InRowStatus,
       "cLWlanPolicyMonitorIPv6OutConfigTable": cLWlanPolicyMonitorIPv6OutConfigTable,
       "cLWlanPolicyMonitorIPv6OutConfigEntry": cLWlanPolicyMonitorIPv6OutConfigEntry,
       "cLWlanMonitorIPv6OutName": cLWlanMonitorIPv6OutName,
       "cLWlanMonitorIPv6OutRowStatus": cLWlanMonitorIPv6OutRowStatus,
       "cLWlanPolicyCalendarProfileTable": cLWlanPolicyCalendarProfileTable,
       "cLWlanPolicyCalendarProfileEntry": cLWlanPolicyCalendarProfileEntry,
       "cLWlanPolicyCalendarProfileName": cLWlanPolicyCalendarProfileName,
       "cLWlanPolicyCalendarProfileRowStatus": cLWlanPolicyCalendarProfileRowStatus,
       "cLWlanPolicyCalendarProfileWlan": cLWlanPolicyCalendarProfileWlan,
       "cLWlanPolicyCalendarProfileClientSession": cLWlanPolicyCalendarProfileClientSession,
       "ciscoLwappWlanPolicyConform": ciscoLwappWlanPolicyConform,
       "ciscoLwappWlanPolicyCompliances": ciscoLwappWlanPolicyCompliances,
       "ciscoLwappWlanPolicyCompliance": ciscoLwappWlanPolicyCompliance,
       "ciscoLwappWlanPolicyComplianceR01": ciscoLwappWlanPolicyComplianceR01,
       "ciscoLwappWlanPolicyComplianceR02": ciscoLwappWlanPolicyComplianceR02,
       "ciscoLwappWlanPolicyComplianceR03": ciscoLwappWlanPolicyComplianceR03,
       "ciscoLwappWlanPolicyComplianceR04": ciscoLwappWlanPolicyComplianceR04,
       "ciscoLwappWlanPolicyComplianceR05": ciscoLwappWlanPolicyComplianceR05,
       "ciscoLwappWlanPolicyGroups": ciscoLwappWlanPolicyGroups,
       "ciscoLwappWlanPolicyConfigGroup": ciscoLwappWlanPolicyConfigGroup,
       "ciscoLwappWlanPolicyConfigGroupRev1": ciscoLwappWlanPolicyConfigGroupRev1,
       "ciscoLwappWlanPolicyATFConfigGroup": ciscoLwappWlanPolicyATFConfigGroup,
       "ciscoLwappWlanAaaPolicyConfigGroup": ciscoLwappWlanAaaPolicyConfigGroup,
       "ciscoLwappWlanPolicyConfigGroupRev2": ciscoLwappWlanPolicyConfigGroupRev2,
       "ciscoLwappWlanPolicyConfigGroupFlowMonitor": ciscoLwappWlanPolicyConfigGroupFlowMonitor,
       "ciscoLwappWlanPolicyConfigGroupRev3": ciscoLwappWlanPolicyConfigGroupRev3,
       "ciscoLwappWlanPolicyConfigGroupCalenderProfile": ciscoLwappWlanPolicyConfigGroupCalenderProfile,
       "ciscoLwappWlanPolicyConfigGroupRev4": ciscoLwappWlanPolicyConfigGroupRev4,
       "ciscoLwappWlanPolicyConfigGroupRev5": ciscoLwappWlanPolicyConfigGroupRev5}
)
