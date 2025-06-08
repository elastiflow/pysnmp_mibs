# SNMP MIB module (CISCO-SDWAN-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SDWAN-POLICY-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:58 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSdwanPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005)
)
if mibBuilder.loadTexts:
    ciscoSdwanPolicyMIB.setRevisions(
        ("2021-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Ipv4Prefix(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d/1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixedLength = 5



class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DestinationIp(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class SourceIp(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class TcpFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("syn", 0)
    )


class DataPolicyDirectionEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("from-service", 0),
          ("from-tunnel", 1),
          ("all", 2))
    )



class DirectionEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 0),
          ("out", 1))
    )



class TransportProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("transport-tcp", 0),
          ("transport-udp", 1))
    )



class ActionDataEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("drop", 1))
    )



class EncapsulationList(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class FnfMonitorEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1),
          ("both", 2))
    )



class ColorList(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class NotificationSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )



class VpnId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSdwanPolicyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSdwanPolicyMIBNotifs = _CiscoSdwanPolicyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 0)
)
_CiscoSdwanPolicyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanPolicyMIBObjects = _CiscoSdwanPolicyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1)
)
_Policy_ObjectIdentity = ObjectIdentity
policy = _Policy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4)
)
_PolicyDataPolicyFilter_ObjectIdentity = ObjectIdentity
policyDataPolicyFilter = _PolicyDataPolicyFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1)
)
_PolicyDataPolicyFilterTable_Object = MibTable
policyDataPolicyFilterTable = _PolicyDataPolicyFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterTable.setStatus("current")
_PolicyDataPolicyFilterEntry_Object = MibTableRow
policyDataPolicyFilterEntry = _PolicyDataPolicyFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 1, 1)
)
policyDataPolicyFilterEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterName"),
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterEntry.setStatus("current")


class _PolicyDataPolicyFilterName_Type(String):
    """Custom type policyDataPolicyFilterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyDataPolicyFilterName_Type.__name__ = "String"
_PolicyDataPolicyFilterName_Object = MibTableColumn
policyDataPolicyFilterName = _PolicyDataPolicyFilterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 1, 1, 1),
    _PolicyDataPolicyFilterName_Type()
)
policyDataPolicyFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterName.setStatus("current")
_PolicyDataPolicyFilterVpnlistTable_Object = MibTable
policyDataPolicyFilterVpnlistTable = _PolicyDataPolicyFilterVpnlistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistTable.setStatus("current")
_PolicyDataPolicyFilterVpnlistEntry_Object = MibTableRow
policyDataPolicyFilterVpnlistEntry = _PolicyDataPolicyFilterVpnlistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 2, 1)
)
policyDataPolicyFilterVpnlistEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistName"),
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistEntry.setStatus("current")


class _PolicyDataPolicyFilterVpnlistName_Type(String):
    """Custom type policyDataPolicyFilterVpnlistName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyDataPolicyFilterVpnlistName_Type.__name__ = "String"
_PolicyDataPolicyFilterVpnlistName_Object = MibTableColumn
policyDataPolicyFilterVpnlistName = _PolicyDataPolicyFilterVpnlistName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 2, 1, 1),
    _PolicyDataPolicyFilterVpnlistName_Type()
)
policyDataPolicyFilterVpnlistName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistName.setStatus("current")
_PolicyDataPolicyFilterVpnlistCounterTable_Object = MibTable
policyDataPolicyFilterVpnlistCounterTable = _PolicyDataPolicyFilterVpnlistCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterTable.setStatus("current")
_PolicyDataPolicyFilterVpnlistCounterEntry_Object = MibTableRow
policyDataPolicyFilterVpnlistCounterEntry = _PolicyDataPolicyFilterVpnlistCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 3, 1)
)
policyDataPolicyFilterVpnlistCounterEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistCounterName"),
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterEntry.setStatus("current")


class _PolicyDataPolicyFilterVpnlistCounterName_Type(String):
    """Custom type policyDataPolicyFilterVpnlistCounterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyDataPolicyFilterVpnlistCounterName_Type.__name__ = "String"
_PolicyDataPolicyFilterVpnlistCounterName_Object = MibTableColumn
policyDataPolicyFilterVpnlistCounterName = _PolicyDataPolicyFilterVpnlistCounterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 3, 1, 1),
    _PolicyDataPolicyFilterVpnlistCounterName_Type()
)
policyDataPolicyFilterVpnlistCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterName.setStatus("current")
_PolicyDataPolicyFilterVpnlistCounterPackets_Type = Counter64
_PolicyDataPolicyFilterVpnlistCounterPackets_Object = MibTableColumn
policyDataPolicyFilterVpnlistCounterPackets = _PolicyDataPolicyFilterVpnlistCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 3, 1, 2),
    _PolicyDataPolicyFilterVpnlistCounterPackets_Type()
)
policyDataPolicyFilterVpnlistCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterPackets.setStatus("current")
_PolicyDataPolicyFilterVpnlistCounterBytes_Type = Counter64
_PolicyDataPolicyFilterVpnlistCounterBytes_Object = MibTableColumn
policyDataPolicyFilterVpnlistCounterBytes = _PolicyDataPolicyFilterVpnlistCounterBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 3, 1, 3),
    _PolicyDataPolicyFilterVpnlistCounterBytes_Type()
)
policyDataPolicyFilterVpnlistCounterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterBytes.setStatus("current")
_PolicyDataPolicyFilterVpnlistPolicerTable_Object = MibTable
policyDataPolicyFilterVpnlistPolicerTable = _PolicyDataPolicyFilterVpnlistPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerTable.setStatus("current")
_PolicyDataPolicyFilterVpnlistPolicerEntry_Object = MibTableRow
policyDataPolicyFilterVpnlistPolicerEntry = _PolicyDataPolicyFilterVpnlistPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 4, 1)
)
policyDataPolicyFilterVpnlistPolicerEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistPolicerName"),
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerEntry.setStatus("current")


class _PolicyDataPolicyFilterVpnlistPolicerName_Type(String):
    """Custom type policyDataPolicyFilterVpnlistPolicerName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PolicyDataPolicyFilterVpnlistPolicerName_Type.__name__ = "String"
_PolicyDataPolicyFilterVpnlistPolicerName_Object = MibTableColumn
policyDataPolicyFilterVpnlistPolicerName = _PolicyDataPolicyFilterVpnlistPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 4, 1, 1),
    _PolicyDataPolicyFilterVpnlistPolicerName_Type()
)
policyDataPolicyFilterVpnlistPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerName.setStatus("current")
_PolicyDataPolicyFilterVpnlistPolicerOosPackets_Type = Counter64
_PolicyDataPolicyFilterVpnlistPolicerOosPackets_Object = MibTableColumn
policyDataPolicyFilterVpnlistPolicerOosPackets = _PolicyDataPolicyFilterVpnlistPolicerOosPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 4, 1, 2),
    _PolicyDataPolicyFilterVpnlistPolicerOosPackets_Type()
)
policyDataPolicyFilterVpnlistPolicerOosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerOosPackets.setStatus("current")
_PolicyDataPolicyFilterVpnlistPolicerOosBytes_Type = Counter64
_PolicyDataPolicyFilterVpnlistPolicerOosBytes_Object = MibTableColumn
policyDataPolicyFilterVpnlistPolicerOosBytes = _PolicyDataPolicyFilterVpnlistPolicerOosBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 1, 4, 1, 3),
    _PolicyDataPolicyFilterVpnlistPolicerOosBytes_Type()
)
policyDataPolicyFilterVpnlistPolicerOosBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerOosBytes.setStatus("current")
_PolicyAppRoutePolicy_ObjectIdentity = ObjectIdentity
policyAppRoutePolicy = _PolicyAppRoutePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2)
)
_PolicyAppRoutePolicyFilterTable_Object = MibTable
policyAppRoutePolicyFilterTable = _PolicyAppRoutePolicyFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterTable.setStatus("current")
_PolicyAppRoutePolicyFilterEntry_Object = MibTableRow
policyAppRoutePolicyFilterEntry = _PolicyAppRoutePolicyFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 1, 1)
)
policyAppRoutePolicyFilterEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterName"),
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterEntry.setStatus("current")


class _PolicyAppRoutePolicyFilterName_Type(String):
    """Custom type policyAppRoutePolicyFilterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAppRoutePolicyFilterName_Type.__name__ = "String"
_PolicyAppRoutePolicyFilterName_Object = MibTableColumn
policyAppRoutePolicyFilterName = _PolicyAppRoutePolicyFilterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 1, 1, 1),
    _PolicyAppRoutePolicyFilterName_Type()
)
policyAppRoutePolicyFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterName.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistTable_Object = MibTable
policyAppRoutePolicyFilterVpnlistTable = _PolicyAppRoutePolicyFilterVpnlistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistTable.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistEntry_Object = MibTableRow
policyAppRoutePolicyFilterVpnlistEntry = _PolicyAppRoutePolicyFilterVpnlistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 2, 1)
)
policyAppRoutePolicyFilterVpnlistEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterVpnlistName"),
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistEntry.setStatus("current")


class _PolicyAppRoutePolicyFilterVpnlistName_Type(String):
    """Custom type policyAppRoutePolicyFilterVpnlistName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyAppRoutePolicyFilterVpnlistName_Type.__name__ = "String"
_PolicyAppRoutePolicyFilterVpnlistName_Object = MibTableColumn
policyAppRoutePolicyFilterVpnlistName = _PolicyAppRoutePolicyFilterVpnlistName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 2, 1, 1),
    _PolicyAppRoutePolicyFilterVpnlistName_Type()
)
policyAppRoutePolicyFilterVpnlistName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistName.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistCounterTable_Object = MibTable
policyAppRoutePolicyFilterVpnlistCounterTable = _PolicyAppRoutePolicyFilterVpnlistCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterTable.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistCounterEntry_Object = MibTableRow
policyAppRoutePolicyFilterVpnlistCounterEntry = _PolicyAppRoutePolicyFilterVpnlistCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 3, 1)
)
policyAppRoutePolicyFilterVpnlistCounterEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterVpnlistName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterVpnlistCounterName"),
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterEntry.setStatus("current")


class _PolicyAppRoutePolicyFilterVpnlistCounterName_Type(String):
    """Custom type policyAppRoutePolicyFilterVpnlistCounterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyAppRoutePolicyFilterVpnlistCounterName_Type.__name__ = "String"
_PolicyAppRoutePolicyFilterVpnlistCounterName_Object = MibTableColumn
policyAppRoutePolicyFilterVpnlistCounterName = _PolicyAppRoutePolicyFilterVpnlistCounterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 3, 1, 1),
    _PolicyAppRoutePolicyFilterVpnlistCounterName_Type()
)
policyAppRoutePolicyFilterVpnlistCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterName.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistCounterPackets_Type = Counter64
_PolicyAppRoutePolicyFilterVpnlistCounterPackets_Object = MibTableColumn
policyAppRoutePolicyFilterVpnlistCounterPackets = _PolicyAppRoutePolicyFilterVpnlistCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 3, 1, 2),
    _PolicyAppRoutePolicyFilterVpnlistCounterPackets_Type()
)
policyAppRoutePolicyFilterVpnlistCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterPackets.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistCounterBytes_Type = Counter64
_PolicyAppRoutePolicyFilterVpnlistCounterBytes_Object = MibTableColumn
policyAppRoutePolicyFilterVpnlistCounterBytes = _PolicyAppRoutePolicyFilterVpnlistCounterBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 2, 3, 1, 3),
    _PolicyAppRoutePolicyFilterVpnlistCounterBytes_Type()
)
policyAppRoutePolicyFilterVpnlistCounterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterBytes.setStatus("current")
_PolicyAccessListNames_ObjectIdentity = ObjectIdentity
policyAccessListNames = _PolicyAccessListNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 3)
)
_PolicyAccessListNamesTable_Object = MibTable
policyAccessListNamesTable = _PolicyAccessListNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    policyAccessListNamesTable.setStatus("current")
_PolicyAccessListNamesEntry_Object = MibTableRow
policyAccessListNamesEntry = _PolicyAccessListNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 3, 1, 1)
)
policyAccessListNamesEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListNamesName"),
)
if mibBuilder.loadTexts:
    policyAccessListNamesEntry.setStatus("current")


class _PolicyAccessListNamesName_Type(String):
    """Custom type policyAccessListNamesName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAccessListNamesName_Type.__name__ = "String"
_PolicyAccessListNamesName_Object = MibTableColumn
policyAccessListNamesName = _PolicyAccessListNamesName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 3, 1, 1, 1),
    _PolicyAccessListNamesName_Type()
)
policyAccessListNamesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListNamesName.setStatus("current")
_PolicyAccessListCounters_ObjectIdentity = ObjectIdentity
policyAccessListCounters = _PolicyAccessListCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 4)
)
_PolicyAccessListCountersTable_Object = MibTable
policyAccessListCountersTable = _PolicyAccessListCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    policyAccessListCountersTable.setStatus("current")
_PolicyAccessListCountersEntry_Object = MibTableRow
policyAccessListCountersEntry = _PolicyAccessListCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 4, 1, 1)
)
policyAccessListCountersEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListCountersName"),
)
if mibBuilder.loadTexts:
    policyAccessListCountersEntry.setStatus("current")


class _PolicyAccessListCountersName_Type(String):
    """Custom type policyAccessListCountersName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAccessListCountersName_Type.__name__ = "String"
_PolicyAccessListCountersName_Object = MibTableColumn
policyAccessListCountersName = _PolicyAccessListCountersName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 4, 1, 1, 1),
    _PolicyAccessListCountersName_Type()
)
policyAccessListCountersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListCountersName.setStatus("current")
_PolicyAccessListCountersAccessPolicyCounterListTable_Object = MibTable
policyAccessListCountersAccessPolicyCounterListTable = _PolicyAccessListCountersAccessPolicyCounterListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListTable.setStatus("current")
_PolicyAccessListCountersAccessPolicyCounterListEntry_Object = MibTableRow
policyAccessListCountersAccessPolicyCounterListEntry = _PolicyAccessListCountersAccessPolicyCounterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 4, 2, 1)
)
policyAccessListCountersAccessPolicyCounterListEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListCountersName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListCountersAccessPolicyCounterListCounterName"),
)
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListEntry.setStatus("current")


class _PolicyAccessListCountersAccessPolicyCounterListCounterName_Type(String):
    """Custom type policyAccessListCountersAccessPolicyCounterListCounterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyAccessListCountersAccessPolicyCounterListCounterName_Type.__name__ = "String"
_PolicyAccessListCountersAccessPolicyCounterListCounterName_Object = MibTableColumn
policyAccessListCountersAccessPolicyCounterListCounterName = _PolicyAccessListCountersAccessPolicyCounterListCounterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 4, 2, 1, 1),
    _PolicyAccessListCountersAccessPolicyCounterListCounterName_Type()
)
policyAccessListCountersAccessPolicyCounterListCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListCounterName.setStatus("current")
_PolicyAccessListCountersAccessPolicyCounterListPackets_Type = Counter64
_PolicyAccessListCountersAccessPolicyCounterListPackets_Object = MibTableColumn
policyAccessListCountersAccessPolicyCounterListPackets = _PolicyAccessListCountersAccessPolicyCounterListPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 4, 2, 1, 2),
    _PolicyAccessListCountersAccessPolicyCounterListPackets_Type()
)
policyAccessListCountersAccessPolicyCounterListPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListPackets.setStatus("current")
_PolicyAccessListCountersAccessPolicyCounterListBytes_Type = Counter64
_PolicyAccessListCountersAccessPolicyCounterListBytes_Object = MibTableColumn
policyAccessListCountersAccessPolicyCounterListBytes = _PolicyAccessListCountersAccessPolicyCounterListBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 4, 2, 1, 3),
    _PolicyAccessListCountersAccessPolicyCounterListBytes_Type()
)
policyAccessListCountersAccessPolicyCounterListBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListBytes.setStatus("current")
_PolicyAccessListPolicers_ObjectIdentity = ObjectIdentity
policyAccessListPolicers = _PolicyAccessListPolicers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 5)
)
_PolicyAccessListPolicersTable_Object = MibTable
policyAccessListPolicersTable = _PolicyAccessListPolicersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    policyAccessListPolicersTable.setStatus("current")
_PolicyAccessListPolicersEntry_Object = MibTableRow
policyAccessListPolicersEntry = _PolicyAccessListPolicersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 5, 1, 1)
)
policyAccessListPolicersEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListPolicersName"),
)
if mibBuilder.loadTexts:
    policyAccessListPolicersEntry.setStatus("current")


class _PolicyAccessListPolicersName_Type(String):
    """Custom type policyAccessListPolicersName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAccessListPolicersName_Type.__name__ = "String"
_PolicyAccessListPolicersName_Object = MibTableColumn
policyAccessListPolicersName = _PolicyAccessListPolicersName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 5, 1, 1, 1),
    _PolicyAccessListPolicersName_Type()
)
policyAccessListPolicersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListPolicersName.setStatus("current")
_PolicyAccessListPolicersAccessPolicyPolicerListTable_Object = MibTable
policyAccessListPolicersAccessPolicyPolicerListTable = _PolicyAccessListPolicersAccessPolicyPolicerListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 5, 2)
)
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListTable.setStatus("current")
_PolicyAccessListPolicersAccessPolicyPolicerListEntry_Object = MibTableRow
policyAccessListPolicersAccessPolicyPolicerListEntry = _PolicyAccessListPolicersAccessPolicyPolicerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 5, 2, 1)
)
policyAccessListPolicersAccessPolicyPolicerListEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListPolicersName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListPolicersAccessPolicyPolicerListPolicerName"),
)
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListEntry.setStatus("current")


class _PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Type(String):
    """Custom type policyAccessListPolicersAccessPolicyPolicerListPolicerName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Type.__name__ = "String"
_PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Object = MibTableColumn
policyAccessListPolicersAccessPolicyPolicerListPolicerName = _PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 5, 2, 1, 1),
    _PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Type()
)
policyAccessListPolicersAccessPolicyPolicerListPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListPolicerName.setStatus("current")
_PolicyAccessListPolicersAccessPolicyPolicerListOosPackets_Type = Counter64
_PolicyAccessListPolicersAccessPolicyPolicerListOosPackets_Object = MibTableColumn
policyAccessListPolicersAccessPolicyPolicerListOosPackets = _PolicyAccessListPolicersAccessPolicyPolicerListOosPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 5, 2, 1, 2),
    _PolicyAccessListPolicersAccessPolicyPolicerListOosPackets_Type()
)
policyAccessListPolicersAccessPolicyPolicerListOosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListOosPackets.setStatus("current")
_PolicyAccessListPolicersAccessPolicyPolicerListOosBytes_Type = Counter64
_PolicyAccessListPolicersAccessPolicyPolicerListOosBytes_Object = MibTableColumn
policyAccessListPolicersAccessPolicyPolicerListOosBytes = _PolicyAccessListPolicersAccessPolicyPolicerListOosBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 5, 2, 1, 3),
    _PolicyAccessListPolicersAccessPolicyPolicerListOosBytes_Type()
)
policyAccessListPolicersAccessPolicyPolicerListOosBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListOosBytes.setStatus("current")
_PolicyAccessListAssociations_ObjectIdentity = ObjectIdentity
policyAccessListAssociations = _PolicyAccessListAssociations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 8)
)
_PolicyAccessListAssociationsTable_Object = MibTable
policyAccessListAssociationsTable = _PolicyAccessListAssociationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    policyAccessListAssociationsTable.setStatus("current")
_PolicyAccessListAssociationsEntry_Object = MibTableRow
policyAccessListAssociationsEntry = _PolicyAccessListAssociationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 8, 1, 1)
)
policyAccessListAssociationsEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListAssociationsName"),
)
if mibBuilder.loadTexts:
    policyAccessListAssociationsEntry.setStatus("current")


class _PolicyAccessListAssociationsName_Type(String):
    """Custom type policyAccessListAssociationsName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAccessListAssociationsName_Type.__name__ = "String"
_PolicyAccessListAssociationsName_Object = MibTableColumn
policyAccessListAssociationsName = _PolicyAccessListAssociationsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 8, 1, 1, 1),
    _PolicyAccessListAssociationsName_Type()
)
policyAccessListAssociationsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListAssociationsName.setStatus("current")
_PolicyAccessListAssociationsAccessPolicyInterfaceListTable_Object = MibTable
policyAccessListAssociationsAccessPolicyInterfaceListTable = _PolicyAccessListAssociationsAccessPolicyInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 8, 2)
)
if mibBuilder.loadTexts:
    policyAccessListAssociationsAccessPolicyInterfaceListTable.setStatus("current")
_PolicyAccessListAssociationsAccessPolicyInterfaceListEntry_Object = MibTableRow
policyAccessListAssociationsAccessPolicyInterfaceListEntry = _PolicyAccessListAssociationsAccessPolicyInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 8, 2, 1)
)
policyAccessListAssociationsAccessPolicyInterfaceListEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListAssociationsName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListAssociationsAccessPolicyInterfaceListIntName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyAccessListAssociationsAccessPolicyInterfaceListIntDir"),
)
if mibBuilder.loadTexts:
    policyAccessListAssociationsAccessPolicyInterfaceListEntry.setStatus("current")


class _PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Type(String):
    """Custom type policyAccessListAssociationsAccessPolicyInterfaceListIntName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Type.__name__ = "String"
_PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Object = MibTableColumn
policyAccessListAssociationsAccessPolicyInterfaceListIntName = _PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 8, 2, 1, 1),
    _PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Type()
)
policyAccessListAssociationsAccessPolicyInterfaceListIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListAssociationsAccessPolicyInterfaceListIntName.setStatus("current")
_PolicyAccessListAssociationsAccessPolicyInterfaceListIntDir_Type = DirectionEnum
_PolicyAccessListAssociationsAccessPolicyInterfaceListIntDir_Object = MibTableColumn
policyAccessListAssociationsAccessPolicyInterfaceListIntDir = _PolicyAccessListAssociationsAccessPolicyInterfaceListIntDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 8, 2, 1, 2),
    _PolicyAccessListAssociationsAccessPolicyInterfaceListIntDir_Type()
)
policyAccessListAssociationsAccessPolicyInterfaceListIntDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListAssociationsAccessPolicyInterfaceListIntDir.setStatus("current")
_PolicyRewriteAssociations_ObjectIdentity = ObjectIdentity
policyRewriteAssociations = _PolicyRewriteAssociations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 9)
)
_PolicyRewriteAssociationsTable_Object = MibTable
policyRewriteAssociationsTable = _PolicyRewriteAssociationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 9, 1)
)
if mibBuilder.loadTexts:
    policyRewriteAssociationsTable.setStatus("current")
_PolicyRewriteAssociationsEntry_Object = MibTableRow
policyRewriteAssociationsEntry = _PolicyRewriteAssociationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 9, 1, 1)
)
policyRewriteAssociationsEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyRewriteAssociationsName"),
)
if mibBuilder.loadTexts:
    policyRewriteAssociationsEntry.setStatus("current")


class _PolicyRewriteAssociationsName_Type(String):
    """Custom type policyRewriteAssociationsName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyRewriteAssociationsName_Type.__name__ = "String"
_PolicyRewriteAssociationsName_Object = MibTableColumn
policyRewriteAssociationsName = _PolicyRewriteAssociationsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 9, 1, 1, 1),
    _PolicyRewriteAssociationsName_Type()
)
policyRewriteAssociationsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyRewriteAssociationsName.setStatus("current")
_PolicyRewriteAssociationsRewriteInterfaceListTable_Object = MibTable
policyRewriteAssociationsRewriteInterfaceListTable = _PolicyRewriteAssociationsRewriteInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 9, 2)
)
if mibBuilder.loadTexts:
    policyRewriteAssociationsRewriteInterfaceListTable.setStatus("current")
_PolicyRewriteAssociationsRewriteInterfaceListEntry_Object = MibTableRow
policyRewriteAssociationsRewriteInterfaceListEntry = _PolicyRewriteAssociationsRewriteInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 9, 2, 1)
)
policyRewriteAssociationsRewriteInterfaceListEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyRewriteAssociationsName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyRewriteAssociationsRewriteInterfaceListInterfaceName"),
)
if mibBuilder.loadTexts:
    policyRewriteAssociationsRewriteInterfaceListEntry.setStatus("current")


class _PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Type(String):
    """Custom type policyRewriteAssociationsRewriteInterfaceListInterfaceName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Type.__name__ = "String"
_PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Object = MibTableColumn
policyRewriteAssociationsRewriteInterfaceListInterfaceName = _PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 9, 2, 1, 1),
    _PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Type()
)
policyRewriteAssociationsRewriteInterfaceListInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyRewriteAssociationsRewriteInterfaceListInterfaceName.setStatus("current")
_PolicyFromVsmart_ObjectIdentity = ObjectIdentity
policyFromVsmart = _PolicyFromVsmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10)
)
_PolicyFromVsmartSlaClassTable_Object = MibTable
policyFromVsmartSlaClassTable = _PolicyFromVsmartSlaClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 2)
)
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassTable.setStatus("current")
_PolicyFromVsmartSlaClassEntry_Object = MibTableRow
policyFromVsmartSlaClassEntry = _PolicyFromVsmartSlaClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 2, 1)
)
policyFromVsmartSlaClassEntry.setIndexNames(
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartSlaClassName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassEntry.setStatus("current")


class _PolicyFromVsmartSlaClassName_Type(String):
    """Custom type policyFromVsmartSlaClassName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartSlaClassName_Type.__name__ = "String"
_PolicyFromVsmartSlaClassName_Object = MibTableColumn
policyFromVsmartSlaClassName = _PolicyFromVsmartSlaClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 2, 1, 1),
    _PolicyFromVsmartSlaClassName_Type()
)
policyFromVsmartSlaClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassName.setStatus("current")


class _PolicyFromVsmartSlaClassLoss_Type(UnsignedByte):
    """Custom type policyFromVsmartSlaClassLoss based on UnsignedByte"""
    subtypeSpec = UnsignedByte.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PolicyFromVsmartSlaClassLoss_Type.__name__ = "UnsignedByte"
_PolicyFromVsmartSlaClassLoss_Object = MibTableColumn
policyFromVsmartSlaClassLoss = _PolicyFromVsmartSlaClassLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 2, 1, 2),
    _PolicyFromVsmartSlaClassLoss_Type()
)
policyFromVsmartSlaClassLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassLoss.setStatus("current")


class _PolicyFromVsmartSlaClassLatency_Type(UnsignedShort):
    """Custom type policyFromVsmartSlaClassLatency based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PolicyFromVsmartSlaClassLatency_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartSlaClassLatency_Object = MibTableColumn
policyFromVsmartSlaClassLatency = _PolicyFromVsmartSlaClassLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 2, 1, 3),
    _PolicyFromVsmartSlaClassLatency_Type()
)
policyFromVsmartSlaClassLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassLatency.setStatus("current")


class _PolicyFromVsmartSlaClassJitter_Type(UnsignedShort):
    """Custom type policyFromVsmartSlaClassJitter based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PolicyFromVsmartSlaClassJitter_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartSlaClassJitter_Object = MibTableColumn
policyFromVsmartSlaClassJitter = _PolicyFromVsmartSlaClassJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 2, 1, 4),
    _PolicyFromVsmartSlaClassJitter_Type()
)
policyFromVsmartSlaClassJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassJitter.setStatus("current")


class _PolicyFromVsmartSlaClassAppProbeClass_Type(String):
    """Custom type policyFromVsmartSlaClassAppProbeClass based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartSlaClassAppProbeClass_Type.__name__ = "String"
_PolicyFromVsmartSlaClassAppProbeClass_Object = MibTableColumn
policyFromVsmartSlaClassAppProbeClass = _PolicyFromVsmartSlaClassAppProbeClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 2, 1, 5),
    _PolicyFromVsmartSlaClassAppProbeClass_Type()
)
policyFromVsmartSlaClassAppProbeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassAppProbeClass.setStatus("current")
_PolicyFromVsmartDataPolicyTable_Object = MibTable
policyFromVsmartDataPolicyTable = _PolicyFromVsmartDataPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 3)
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyTable.setStatus("current")
_PolicyFromVsmartDataPolicyEntry_Object = MibTableRow
policyFromVsmartDataPolicyEntry = _PolicyFromVsmartDataPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 3, 1)
)
policyFromVsmartDataPolicyEntry.setIndexNames(
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyEntry.setStatus("current")


class _PolicyFromVsmartDataPolicyName_Type(String):
    """Custom type policyFromVsmartDataPolicyName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyFromVsmartDataPolicyName_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyName_Object = MibTableColumn
policyFromVsmartDataPolicyName = _PolicyFromVsmartDataPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 3, 1, 1),
    _PolicyFromVsmartDataPolicyName_Type()
)
policyFromVsmartDataPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyName.setStatus("current")
_PolicyFromVsmartDataPolicyDirection_Type = DataPolicyDirectionEnum
_PolicyFromVsmartDataPolicyDirection_Object = MibTableColumn
policyFromVsmartDataPolicyDirection = _PolicyFromVsmartDataPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 3, 1, 2),
    _PolicyFromVsmartDataPolicyDirection_Type()
)
policyFromVsmartDataPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyDirection.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListTable_Object = MibTable
policyFromVsmartDataPolicyVpnListTable = _PolicyFromVsmartDataPolicyVpnListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 4)
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListTable.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListEntry_Object = MibTableRow
policyFromVsmartDataPolicyVpnListEntry = _PolicyFromVsmartDataPolicyVpnListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 4, 1)
)
policyFromVsmartDataPolicyVpnListEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyName"),
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListEntry.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListName_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListName_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListName_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListName = _PolicyFromVsmartDataPolicyVpnListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 4, 1, 1),
    _PolicyFromVsmartDataPolicyVpnListName_Type()
)
policyFromVsmartDataPolicyVpnListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListName.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListDefaultAction_Type(ActionDataEnum):
    """Custom type policyFromVsmartDataPolicyVpnListDefaultAction based on ActionDataEnum"""
    defaultValue = 1


_PolicyFromVsmartDataPolicyVpnListDefaultAction_Type.__name__ = "ActionDataEnum"
_PolicyFromVsmartDataPolicyVpnListDefaultAction_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListDefaultAction = _PolicyFromVsmartDataPolicyVpnListDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 4, 1, 2),
    _PolicyFromVsmartDataPolicyVpnListDefaultAction_Type()
)
policyFromVsmartDataPolicyVpnListDefaultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListDefaultAction.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceTable_Object = MibTable
policyFromVsmartDataPolicyVpnListSequenceTable = _PolicyFromVsmartDataPolicyVpnListSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5)
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceTable.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceEntry_Object = MibTableRow
policyFromVsmartDataPolicyVpnListSequenceEntry = _PolicyFromVsmartDataPolicyVpnListSequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1)
)
policyFromVsmartDataPolicyVpnListSequenceEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceSeqValue"),
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceEntry.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Type(UnsignedShort):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceSeqValue based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceSeqValue = _PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 1),
    _PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Type()
)
policyFromVsmartDataPolicyVpnListSequenceSeqValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceSeqValue.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst = _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 4),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst = _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 5),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst = _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 7),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst = _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 8),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceMatchTcp_Type = TcpFlags
_PolicyFromVsmartDataPolicyVpnListSequenceMatchTcp_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchTcp = _PolicyFromVsmartDataPolicyVpnListSequenceMatchTcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 10),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchTcp_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchTcp.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Type(ActionDataEnum):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionActionValue based on ActionDataEnum"""
    defaultValue = 1


_PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Type.__name__ = "ActionDataEnum"
_PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionActionValue = _PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 11),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionActionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionActionValue.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionCount based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionCount = _PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 12),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionCount.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn_Type = Unsigned32
_PolicyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn = _PolicyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 13),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionCflowd_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionCflowd_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionCflowd = _PolicyFromVsmartDataPolicyVpnListSequenceActionCflowd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 14),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionCflowd_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionCflowd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionCflowd.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 15),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 16),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHop_Type = String
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHop_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 17),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHop_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 18),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Type(Unsigned32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Type.__name__ = "Unsigned32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetVpn = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 19),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetVpn.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel_Type = Unsigned32
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 20),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp_Type = InetAddressIP
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 21),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 22),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 23),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fW", 1),
          ("iDS", 2),
          ("iDP", 3),
          ("netsvc1", 4),
          ("netsvc2", 5),
          ("netsvc3", 6),
          ("netsvc4", 7))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 24),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Type(Unsigned32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Type.__name__ = "Unsigned32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 25),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp_Type = InetAddressIP
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 26),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 27),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst = _PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 28),
    _PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Type()
)
policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 29),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict = _PolicyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 30),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionLog_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionLog_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionLog = _PolicyFromVsmartDataPolicyVpnListSequenceActionLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 31),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionLog_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionLog.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor_Type = ColorList
_PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor = _PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 32),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap_Type = EncapsulationList
_PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap = _PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 33),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict = _PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 34),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization = _PolicyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 35),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6_Type = String
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6 = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 37),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSig_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionSig_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSig = _PolicyFromVsmartDataPolicyVpnListSequenceActionSig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 38),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSig_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSig.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 39),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute = _PolicyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 5, 1, 41),
    _PolicyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable_Object = MibTable
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 6)
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry_Object = MibTableRow
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 6, 1)
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceSeqValue"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum"),
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Type(Unsigned32):
    """Custom type policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Type.__name__ = "Unsigned32"
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 6, 1, 1),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl_Type = Unsigned32
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 6, 1, 2),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp_Type = InetAddressIP
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 6, 1, 3),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 6, 1, 4),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 6, 1, 5),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf_Type = Unsigned32
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 6, 1, 6),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf.setStatus("current")
_PolicyFromVsmartCflowdTemplate_ObjectIdentity = ObjectIdentity
policyFromVsmartCflowdTemplate = _PolicyFromVsmartCflowdTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 7)
)


class _PolicyFromVsmartCflowdTemplateName_Type(String):
    """Custom type policyFromVsmartCflowdTemplateName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyFromVsmartCflowdTemplateName_Type.__name__ = "String"
_PolicyFromVsmartCflowdTemplateName_Object = MibScalar
policyFromVsmartCflowdTemplateName = _PolicyFromVsmartCflowdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 7, 1),
    _PolicyFromVsmartCflowdTemplateName_Type()
)
policyFromVsmartCflowdTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateName.setStatus("current")


class _PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateFlowActiveTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Object = MibScalar
policyFromVsmartCflowdTemplateFlowActiveTimeout = _PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 7, 2),
    _PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Type()
)
policyFromVsmartCflowdTemplateFlowActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateFlowActiveTimeout.setStatus("current")


class _PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateFlowInactiveTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Object = MibScalar
policyFromVsmartCflowdTemplateFlowInactiveTimeout = _PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 7, 3),
    _PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Type()
)
policyFromVsmartCflowdTemplateFlowInactiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateFlowInactiveTimeout.setStatus("current")


class _PolicyFromVsmartCflowdTemplateTemplateRefresh_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateTemplateRefresh based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_PolicyFromVsmartCflowdTemplateTemplateRefresh_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateTemplateRefresh_Object = MibScalar
policyFromVsmartCflowdTemplateTemplateRefresh = _PolicyFromVsmartCflowdTemplateTemplateRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 7, 4),
    _PolicyFromVsmartCflowdTemplateTemplateRefresh_Type()
)
policyFromVsmartCflowdTemplateTemplateRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateTemplateRefresh.setStatus("current")


class _PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateFlowSamplingInterval based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Object = MibScalar
policyFromVsmartCflowdTemplateFlowSamplingInterval = _PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 7, 5),
    _PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Type()
)
policyFromVsmartCflowdTemplateFlowSamplingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateFlowSamplingInterval.setStatus("current")


class _PolicyFromVsmartCflowdTemplateProtocol_Type(FnfMonitorEnum):
    """Custom type policyFromVsmartCflowdTemplateProtocol based on FnfMonitorEnum"""
    defaultValue = 0


_PolicyFromVsmartCflowdTemplateProtocol_Type.__name__ = "FnfMonitorEnum"
_PolicyFromVsmartCflowdTemplateProtocol_Object = MibScalar
policyFromVsmartCflowdTemplateProtocol = _PolicyFromVsmartCflowdTemplateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 7, 6),
    _PolicyFromVsmartCflowdTemplateProtocol_Type()
)
policyFromVsmartCflowdTemplateProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateProtocol.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorTable_Object = MibTable
policyFromVsmartCflowdTemplateCollectorTable = _PolicyFromVsmartCflowdTemplateCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8)
)
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorTable.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorEntry_Object = MibTableRow
policyFromVsmartCflowdTemplateCollectorEntry = _PolicyFromVsmartCflowdTemplateCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1)
)
policyFromVsmartCflowdTemplateCollectorEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorVpn"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorAddress"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorPort"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorTransport"),
)
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorEntry.setStatus("current")


class _PolicyFromVsmartCflowdTemplateCollectorVpn_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateCollectorVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_PolicyFromVsmartCflowdTemplateCollectorVpn_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateCollectorVpn_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorVpn = _PolicyFromVsmartCflowdTemplateCollectorVpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 1),
    _PolicyFromVsmartCflowdTemplateCollectorVpn_Type()
)
policyFromVsmartCflowdTemplateCollectorVpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorVpn.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorAddress_Type = InetAddressIP
_PolicyFromVsmartCflowdTemplateCollectorAddress_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorAddress = _PolicyFromVsmartCflowdTemplateCollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 2),
    _PolicyFromVsmartCflowdTemplateCollectorAddress_Type()
)
policyFromVsmartCflowdTemplateCollectorAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorAddress.setStatus("current")


class _PolicyFromVsmartCflowdTemplateCollectorPort_Type(UnsignedShort):
    """Custom type policyFromVsmartCflowdTemplateCollectorPort based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_PolicyFromVsmartCflowdTemplateCollectorPort_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartCflowdTemplateCollectorPort_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorPort = _PolicyFromVsmartCflowdTemplateCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 3),
    _PolicyFromVsmartCflowdTemplateCollectorPort_Type()
)
policyFromVsmartCflowdTemplateCollectorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorPort.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorTransport_Type = TransportProtocol
_PolicyFromVsmartCflowdTemplateCollectorTransport_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorTransport = _PolicyFromVsmartCflowdTemplateCollectorTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 4),
    _PolicyFromVsmartCflowdTemplateCollectorTransport_Type()
)
policyFromVsmartCflowdTemplateCollectorTransport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorTransport.setStatus("current")


class _PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Type(String):
    """Custom type policyFromVsmartCflowdTemplateCollectorSourceInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Type.__name__ = "String"
_PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorSourceInterface = _PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 5),
    _PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Type()
)
policyFromVsmartCflowdTemplateCollectorSourceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorSourceInterface.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorExportSpreadEnable_Type = TruthValue
_PolicyFromVsmartCflowdTemplateCollectorExportSpreadEnable_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorExportSpreadEnable = _PolicyFromVsmartCflowdTemplateCollectorExportSpreadEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 6),
    _PolicyFromVsmartCflowdTemplateCollectorExportSpreadEnable_Type()
)
policyFromVsmartCflowdTemplateCollectorExportSpreadEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorExportSpreadEnable.setStatus("current")


class _PolicyFromVsmartCflowdTemplateCollectorExportSpreadAppTables_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateCollectorExportSpreadAppTables based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PolicyFromVsmartCflowdTemplateCollectorExportSpreadAppTables_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateCollectorExportSpreadAppTables_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorExportSpreadAppTables = _PolicyFromVsmartCflowdTemplateCollectorExportSpreadAppTables_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 7),
    _PolicyFromVsmartCflowdTemplateCollectorExportSpreadAppTables_Type()
)
policyFromVsmartCflowdTemplateCollectorExportSpreadAppTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorExportSpreadAppTables.setStatus("current")


class _PolicyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PolicyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables = _PolicyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 8),
    _PolicyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables_Type()
)
policyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables.setStatus("current")


class _PolicyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PolicyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables = _PolicyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 9),
    _PolicyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables_Type()
)
policyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorBfdMetricsExport_Type = TruthValue
_PolicyFromVsmartCflowdTemplateCollectorBfdMetricsExport_Object = MibScalar
policyFromVsmartCflowdTemplateCollectorBfdMetricsExport = _PolicyFromVsmartCflowdTemplateCollectorBfdMetricsExport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 10),
    _PolicyFromVsmartCflowdTemplateCollectorBfdMetricsExport_Type()
)
policyFromVsmartCflowdTemplateCollectorBfdMetricsExport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorBfdMetricsExport.setStatus("current")


class _PolicyFromVsmartCflowdTemplateCollectorBFDExportInterval_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateCollectorBFDExportInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_PolicyFromVsmartCflowdTemplateCollectorBFDExportInterval_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateCollectorBFDExportInterval_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorBFDExportInterval = _PolicyFromVsmartCflowdTemplateCollectorBFDExportInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 8, 1, 11),
    _PolicyFromVsmartCflowdTemplateCollectorBFDExportInterval_Type()
)
policyFromVsmartCflowdTemplateCollectorBFDExportInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorBFDExportInterval.setStatus("current")
_PolicyFromVsmartAppRoutePolicyTable_Object = MibTable
policyFromVsmartAppRoutePolicyTable = _PolicyFromVsmartAppRoutePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 9)
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyTable.setStatus("current")
_PolicyFromVsmartAppRoutePolicyEntry_Object = MibTableRow
policyFromVsmartAppRoutePolicyEntry = _PolicyFromVsmartAppRoutePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 9, 1)
)
policyFromVsmartAppRoutePolicyEntry.setIndexNames(
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyEntry.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyName_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyFromVsmartAppRoutePolicyName_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyName_Object = MibTableColumn
policyFromVsmartAppRoutePolicyName = _PolicyFromVsmartAppRoutePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 9, 1, 1),
    _PolicyFromVsmartAppRoutePolicyName_Type()
)
policyFromVsmartAppRoutePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyName.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListTable_Object = MibTable
policyFromVsmartAppRoutePolicyVpnListTable = _PolicyFromVsmartAppRoutePolicyVpnListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 10)
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListTable.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListEntry_Object = MibTableRow
policyFromVsmartAppRoutePolicyVpnListEntry = _PolicyFromVsmartAppRoutePolicyVpnListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 10, 1)
)
policyFromVsmartAppRoutePolicyVpnListEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyName"),
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListEntry.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListName_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListName_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListName_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListName = _PolicyFromVsmartAppRoutePolicyVpnListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 10, 1, 1),
    _PolicyFromVsmartAppRoutePolicyVpnListName_Type()
)
policyFromVsmartAppRoutePolicyVpnListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListName.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName = _PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 10, 1, 13),
    _PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Type()
)
policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceTable_Object = MibTable
policyFromVsmartAppRoutePolicyVpnListSequenceTable = _PolicyFromVsmartAppRoutePolicyVpnListSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11)
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceTable.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceEntry_Object = MibTableRow
policyFromVsmartAppRoutePolicyVpnListSequenceEntry = _PolicyFromVsmartAppRoutePolicyVpnListSequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1)
)
policyFromVsmartAppRoutePolicyVpnListSequenceEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue"),
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceEntry.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Type(UnsignedShort):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65530),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue = _PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 1),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst = _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 4),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst = _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 5),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst = _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 7),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst = _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 8),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceActionCount based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionCount = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 10),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionCount.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 11),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict_Type = TruthValue
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 12),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr_Type = ColorList
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 14),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionLog_Type = TruthValue
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionLog_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionLog = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 15),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionLog_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionLog.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSeqActBackupSlaPrefClr_Type = ColorList
_PolicyFromVsmartAppRoutePolicyVpnListSeqActBackupSlaPrefClr_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSeqActBackupSlaPrefClr = _PolicyFromVsmartAppRoutePolicyVpnListSeqActBackupSlaPrefClr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 16),
    _PolicyFromVsmartAppRoutePolicyVpnListSeqActBackupSlaPrefClr_Type()
)
policyFromVsmartAppRoutePolicyVpnListSeqActBackupSlaPrefClr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSeqActBackupSlaPrefClr.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback_Type = TruthValue
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 11, 1, 17),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback.setStatus("current")
_PolicyFromVsmartPolicerTable_Object = MibTable
policyFromVsmartPolicerTable = _PolicyFromVsmartPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 12)
)
if mibBuilder.loadTexts:
    policyFromVsmartPolicerTable.setStatus("current")
_PolicyFromVsmartPolicerEntry_Object = MibTableRow
policyFromVsmartPolicerEntry = _PolicyFromVsmartPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 12, 1)
)
policyFromVsmartPolicerEntry.setIndexNames(
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartPolicerName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartPolicerEntry.setStatus("current")


class _PolicyFromVsmartPolicerName_Type(String):
    """Custom type policyFromVsmartPolicerName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartPolicerName_Type.__name__ = "String"
_PolicyFromVsmartPolicerName_Object = MibTableColumn
policyFromVsmartPolicerName = _PolicyFromVsmartPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 12, 1, 1),
    _PolicyFromVsmartPolicerName_Type()
)
policyFromVsmartPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartPolicerName.setStatus("current")
_PolicyFromVsmartPolicerRate_Type = Counter64
_PolicyFromVsmartPolicerRate_Object = MibTableColumn
policyFromVsmartPolicerRate = _PolicyFromVsmartPolicerRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 12, 1, 2),
    _PolicyFromVsmartPolicerRate_Type()
)
policyFromVsmartPolicerRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartPolicerRate.setStatus("current")


class _PolicyFromVsmartPolicerBurst_Type(Unsigned32):
    """Custom type policyFromVsmartPolicerBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 10000000),
    )


_PolicyFromVsmartPolicerBurst_Type.__name__ = "Unsigned32"
_PolicyFromVsmartPolicerBurst_Object = MibTableColumn
policyFromVsmartPolicerBurst = _PolicyFromVsmartPolicerBurst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 12, 1, 3),
    _PolicyFromVsmartPolicerBurst_Type()
)
policyFromVsmartPolicerBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartPolicerBurst.setStatus("current")


class _PolicyFromVsmartPolicerExceed_Type(Integer32):
    """Custom type policyFromVsmartPolicerExceed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("remark", 1))
    )


_PolicyFromVsmartPolicerExceed_Type.__name__ = "Integer32"
_PolicyFromVsmartPolicerExceed_Object = MibTableColumn
policyFromVsmartPolicerExceed = _PolicyFromVsmartPolicerExceed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 12, 1, 4),
    _PolicyFromVsmartPolicerExceed_Type()
)
policyFromVsmartPolicerExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartPolicerExceed.setStatus("current")
_PolicyFromVsmartListsVpnListTable_Object = MibTable
policyFromVsmartListsVpnListTable = _PolicyFromVsmartListsVpnListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 13)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListTable.setStatus("current")
_PolicyFromVsmartListsVpnListEntry_Object = MibTableRow
policyFromVsmartListsVpnListEntry = _PolicyFromVsmartListsVpnListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 13, 1)
)
policyFromVsmartListsVpnListEntry.setIndexNames(
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsVpnListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListEntry.setStatus("current")


class _PolicyFromVsmartListsVpnListName_Type(String):
    """Custom type policyFromVsmartListsVpnListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsVpnListName_Type.__name__ = "String"
_PolicyFromVsmartListsVpnListName_Object = MibTableColumn
policyFromVsmartListsVpnListName = _PolicyFromVsmartListsVpnListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 13, 1, 1),
    _PolicyFromVsmartListsVpnListName_Type()
)
policyFromVsmartListsVpnListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListName.setStatus("current")
_PolicyFromVsmartListsVpnListVpnTable_Object = MibTable
policyFromVsmartListsVpnListVpnTable = _PolicyFromVsmartListsVpnListVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 14)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListVpnTable.setStatus("current")
_PolicyFromVsmartListsVpnListVpnEntry_Object = MibTableRow
policyFromVsmartListsVpnListVpnEntry = _PolicyFromVsmartListsVpnListVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 14, 1)
)
policyFromVsmartListsVpnListVpnEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsVpnListName"),
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsVpnListVpnId"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListVpnEntry.setStatus("current")


class _PolicyFromVsmartListsVpnListVpnId_Type(String):
    """Custom type policyFromVsmartListsVpnListVpnId based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsVpnListVpnId_Type.__name__ = "String"
_PolicyFromVsmartListsVpnListVpnId_Object = MibTableColumn
policyFromVsmartListsVpnListVpnId = _PolicyFromVsmartListsVpnListVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 14, 1, 1),
    _PolicyFromVsmartListsVpnListVpnId_Type()
)
policyFromVsmartListsVpnListVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListVpnId.setStatus("current")
_PolicyFromVsmartListsDataPrefixListTable_Object = MibTable
policyFromVsmartListsDataPrefixListTable = _PolicyFromVsmartListsDataPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 15)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListTable.setStatus("current")
_PolicyFromVsmartListsDataPrefixListEntry_Object = MibTableRow
policyFromVsmartListsDataPrefixListEntry = _PolicyFromVsmartListsDataPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 15, 1)
)
policyFromVsmartListsDataPrefixListEntry.setIndexNames(
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsDataPrefixListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListEntry.setStatus("current")


class _PolicyFromVsmartListsDataPrefixListName_Type(String):
    """Custom type policyFromVsmartListsDataPrefixListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsDataPrefixListName_Type.__name__ = "String"
_PolicyFromVsmartListsDataPrefixListName_Object = MibTableColumn
policyFromVsmartListsDataPrefixListName = _PolicyFromVsmartListsDataPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 15, 1, 1),
    _PolicyFromVsmartListsDataPrefixListName_Type()
)
policyFromVsmartListsDataPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListName.setStatus("current")
_PolicyFromVsmartListsDataPrefixListIpPrefixTable_Object = MibTable
policyFromVsmartListsDataPrefixListIpPrefixTable = _PolicyFromVsmartListsDataPrefixListIpPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 16)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListIpPrefixTable.setStatus("current")
_PolicyFromVsmartListsDataPrefixListIpPrefixEntry_Object = MibTableRow
policyFromVsmartListsDataPrefixListIpPrefixEntry = _PolicyFromVsmartListsDataPrefixListIpPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 16, 1)
)
policyFromVsmartListsDataPrefixListIpPrefixEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsDataPrefixListName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsDataPrefixListIpPrefixIp"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListIpPrefixEntry.setStatus("current")
_PolicyFromVsmartListsDataPrefixListIpPrefixIp_Type = Ipv4Prefix
_PolicyFromVsmartListsDataPrefixListIpPrefixIp_Object = MibTableColumn
policyFromVsmartListsDataPrefixListIpPrefixIp = _PolicyFromVsmartListsDataPrefixListIpPrefixIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 16, 1, 1),
    _PolicyFromVsmartListsDataPrefixListIpPrefixIp_Type()
)
policyFromVsmartListsDataPrefixListIpPrefixIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListIpPrefixIp.setStatus("current")
_PolicyFromVsmartListsTlocListTable_Object = MibTable
policyFromVsmartListsTlocListTable = _PolicyFromVsmartListsTlocListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 17)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTable.setStatus("current")
_PolicyFromVsmartListsTlocListEntry_Object = MibTableRow
policyFromVsmartListsTlocListEntry = _PolicyFromVsmartListsTlocListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 17, 1)
)
policyFromVsmartListsTlocListEntry.setIndexNames(
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsTlocListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListEntry.setStatus("current")


class _PolicyFromVsmartListsTlocListName_Type(String):
    """Custom type policyFromVsmartListsTlocListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsTlocListName_Type.__name__ = "String"
_PolicyFromVsmartListsTlocListName_Object = MibTableColumn
policyFromVsmartListsTlocListName = _PolicyFromVsmartListsTlocListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 17, 1, 1),
    _PolicyFromVsmartListsTlocListName_Type()
)
policyFromVsmartListsTlocListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListName.setStatus("current")
_PolicyFromVsmartListsTlocListTlocTable_Object = MibTable
policyFromVsmartListsTlocListTlocTable = _PolicyFromVsmartListsTlocListTlocTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 18)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocTable.setStatus("current")
_PolicyFromVsmartListsTlocListTlocEntry_Object = MibTableRow
policyFromVsmartListsTlocListTlocEntry = _PolicyFromVsmartListsTlocListTlocEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 18, 1)
)
policyFromVsmartListsTlocListTlocEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsTlocListName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsTlocListTlocIp"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsTlocListTlocColor"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsTlocListTlocEncap"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocEntry.setStatus("current")
_PolicyFromVsmartListsTlocListTlocIp_Type = InetAddressIP
_PolicyFromVsmartListsTlocListTlocIp_Object = MibTableColumn
policyFromVsmartListsTlocListTlocIp = _PolicyFromVsmartListsTlocListTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 18, 1, 1),
    _PolicyFromVsmartListsTlocListTlocIp_Type()
)
policyFromVsmartListsTlocListTlocIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocIp.setStatus("current")


class _PolicyFromVsmartListsTlocListTlocColor_Type(Integer32):
    """Custom type policyFromVsmartListsTlocListTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartListsTlocListTlocColor_Type.__name__ = "Integer32"
_PolicyFromVsmartListsTlocListTlocColor_Object = MibTableColumn
policyFromVsmartListsTlocListTlocColor = _PolicyFromVsmartListsTlocListTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 18, 1, 2),
    _PolicyFromVsmartListsTlocListTlocColor_Type()
)
policyFromVsmartListsTlocListTlocColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocColor.setStatus("current")


class _PolicyFromVsmartListsTlocListTlocEncap_Type(Integer32):
    """Custom type policyFromVsmartListsTlocListTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_PolicyFromVsmartListsTlocListTlocEncap_Type.__name__ = "Integer32"
_PolicyFromVsmartListsTlocListTlocEncap_Object = MibTableColumn
policyFromVsmartListsTlocListTlocEncap = _PolicyFromVsmartListsTlocListTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 18, 1, 3),
    _PolicyFromVsmartListsTlocListTlocEncap_Type()
)
policyFromVsmartListsTlocListTlocEncap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocEncap.setStatus("current")
_PolicyFromVsmartListsTlocListTlocPreference_Type = Unsigned32
_PolicyFromVsmartListsTlocListTlocPreference_Object = MibTableColumn
policyFromVsmartListsTlocListTlocPreference = _PolicyFromVsmartListsTlocListTlocPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 18, 1, 4),
    _PolicyFromVsmartListsTlocListTlocPreference_Type()
)
policyFromVsmartListsTlocListTlocPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocPreference.setStatus("current")
_PolicyFromVsmartListsAppProbeClassListTable_Object = MibTable
policyFromVsmartListsAppProbeClassListTable = _PolicyFromVsmartListsAppProbeClassListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 21)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsAppProbeClassListTable.setStatus("current")
_PolicyFromVsmartListsAppProbeClassListEntry_Object = MibTableRow
policyFromVsmartListsAppProbeClassListEntry = _PolicyFromVsmartListsAppProbeClassListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 21, 1)
)
policyFromVsmartListsAppProbeClassListEntry.setIndexNames(
    (1, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsAppProbeClassListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsAppProbeClassListEntry.setStatus("current")


class _PolicyFromVsmartListsAppProbeClassListName_Type(String):
    """Custom type policyFromVsmartListsAppProbeClassListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsAppProbeClassListName_Type.__name__ = "String"
_PolicyFromVsmartListsAppProbeClassListName_Object = MibTableColumn
policyFromVsmartListsAppProbeClassListName = _PolicyFromVsmartListsAppProbeClassListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 21, 1, 1),
    _PolicyFromVsmartListsAppProbeClassListName_Type()
)
policyFromVsmartListsAppProbeClassListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartListsAppProbeClassListName.setStatus("current")


class _PolicyFromVsmartListsAppProbeClassListForwardingClass_Type(String):
    """Custom type policyFromVsmartListsAppProbeClassListForwardingClass based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsAppProbeClassListForwardingClass_Type.__name__ = "String"
_PolicyFromVsmartListsAppProbeClassListForwardingClass_Object = MibTableColumn
policyFromVsmartListsAppProbeClassListForwardingClass = _PolicyFromVsmartListsAppProbeClassListForwardingClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 21, 1, 2),
    _PolicyFromVsmartListsAppProbeClassListForwardingClass_Type()
)
policyFromVsmartListsAppProbeClassListForwardingClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsAppProbeClassListForwardingClass.setStatus("current")
_PolicyFromVsmartListsAppProbeClassColorTable_Object = MibTable
policyFromVsmartListsAppProbeClassColorTable = _PolicyFromVsmartListsAppProbeClassColorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 22)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsAppProbeClassColorTable.setStatus("current")
_PolicyFromVsmartListsAppProbeClassColorEntry_Object = MibTableRow
policyFromVsmartListsAppProbeClassColorEntry = _PolicyFromVsmartListsAppProbeClassColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 22, 1)
)
policyFromVsmartListsAppProbeClassColorEntry.setIndexNames(
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsAppProbeClassListName"),
    (0, "CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsAppProbeClassColorName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsAppProbeClassColorEntry.setStatus("current")


class _PolicyFromVsmartListsAppProbeClassColorName_Type(Integer32):
    """Custom type policyFromVsmartListsAppProbeClassColorName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartListsAppProbeClassColorName_Type.__name__ = "Integer32"
_PolicyFromVsmartListsAppProbeClassColorName_Object = MibTableColumn
policyFromVsmartListsAppProbeClassColorName = _PolicyFromVsmartListsAppProbeClassColorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 22, 1, 1),
    _PolicyFromVsmartListsAppProbeClassColorName_Type()
)
policyFromVsmartListsAppProbeClassColorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartListsAppProbeClassColorName.setStatus("current")


class _PolicyFromVsmartListsAppProbeClassColorDscp_Type(Unsigned32):
    """Custom type policyFromVsmartListsAppProbeClassColorDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PolicyFromVsmartListsAppProbeClassColorDscp_Type.__name__ = "Unsigned32"
_PolicyFromVsmartListsAppProbeClassColorDscp_Object = MibTableColumn
policyFromVsmartListsAppProbeClassColorDscp = _PolicyFromVsmartListsAppProbeClassColorDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 1, 4, 10, 22, 1, 2),
    _PolicyFromVsmartListsAppProbeClassColorDscp_Type()
)
policyFromVsmartListsAppProbeClassColorDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsAppProbeClassColorDscp.setStatus("current")
_CiscoSdwanPolicyMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanPolicyMIBNotifObjects = _CiscoSdwanPolicyMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2)
)
_NetconfNotificationSeverity_Type = NotificationSeverity
_NetconfNotificationSeverity_Object = MibScalar
netconfNotificationSeverity = _NetconfNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 2),
    _NetconfNotificationSeverity_Type()
)
netconfNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netconfNotificationSeverity.setStatus("current")
_CiscoSdwanPolicyVpnId_Type = VpnId
_CiscoSdwanPolicyVpnId_Object = MibScalar
ciscoSdwanPolicyVpnId = _CiscoSdwanPolicyVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 3),
    _CiscoSdwanPolicyVpnId_Type()
)
ciscoSdwanPolicyVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyVpnId.setStatus("current")
_CiscoSdwanPolicyApplication_Type = OctetString
_CiscoSdwanPolicyApplication_Object = MibScalar
ciscoSdwanPolicyApplication = _CiscoSdwanPolicyApplication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 4),
    _CiscoSdwanPolicyApplication_Type()
)
ciscoSdwanPolicyApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyApplication.setStatus("current")
_CiscoSdwanPolicySourceIp_Type = SourceIp
_CiscoSdwanPolicySourceIp_Object = MibScalar
ciscoSdwanPolicySourceIp = _CiscoSdwanPolicySourceIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 5),
    _CiscoSdwanPolicySourceIp_Type()
)
ciscoSdwanPolicySourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicySourceIp.setStatus("current")
_CiscoSdwanPolicySourcePort_Type = Unsigned32
_CiscoSdwanPolicySourcePort_Object = MibScalar
ciscoSdwanPolicySourcePort = _CiscoSdwanPolicySourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 6),
    _CiscoSdwanPolicySourcePort_Type()
)
ciscoSdwanPolicySourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicySourcePort.setStatus("current")
_CiscoSdwanPolicyDestinationIp_Type = DestinationIp
_CiscoSdwanPolicyDestinationIp_Object = MibScalar
ciscoSdwanPolicyDestinationIp = _CiscoSdwanPolicyDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 7),
    _CiscoSdwanPolicyDestinationIp_Type()
)
ciscoSdwanPolicyDestinationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyDestinationIp.setStatus("current")
_CiscoSdwanPolicyDestinationPort_Type = Unsigned32
_CiscoSdwanPolicyDestinationPort_Object = MibScalar
ciscoSdwanPolicyDestinationPort = _CiscoSdwanPolicyDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 8),
    _CiscoSdwanPolicyDestinationPort_Type()
)
ciscoSdwanPolicyDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyDestinationPort.setStatus("current")
_CiscoSdwanPolicyProtocol_Type = Unsigned32
_CiscoSdwanPolicyProtocol_Object = MibScalar
ciscoSdwanPolicyProtocol = _CiscoSdwanPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 9),
    _CiscoSdwanPolicyProtocol_Type()
)
ciscoSdwanPolicyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyProtocol.setStatus("current")
_CiscoSdwanPolicyDscp_Type = Unsigned32
_CiscoSdwanPolicyDscp_Object = MibScalar
ciscoSdwanPolicyDscp = _CiscoSdwanPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 10),
    _CiscoSdwanPolicyDscp_Type()
)
ciscoSdwanPolicyDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyDscp.setStatus("current")
_CiscoSdwanPolicySlaInformation_Type = OctetString
_CiscoSdwanPolicySlaInformation_Object = MibScalar
ciscoSdwanPolicySlaInformation = _CiscoSdwanPolicySlaInformation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 11),
    _CiscoSdwanPolicySlaInformation_Type()
)
ciscoSdwanPolicySlaInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicySlaInformation.setStatus("current")
_CiscoSdwanPolicySlaStatus_Type = OctetString
_CiscoSdwanPolicySlaStatus_Object = MibScalar
ciscoSdwanPolicySlaStatus = _CiscoSdwanPolicySlaStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 12),
    _CiscoSdwanPolicySlaStatus_Type()
)
ciscoSdwanPolicySlaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicySlaStatus.setStatus("current")
_CiscoSdwanPolicyVpnListName_Type = OctetString
_CiscoSdwanPolicyVpnListName_Object = MibScalar
ciscoSdwanPolicyVpnListName = _CiscoSdwanPolicyVpnListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 13),
    _CiscoSdwanPolicyVpnListName_Type()
)
ciscoSdwanPolicyVpnListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyVpnListName.setStatus("current")
_CiscoSdwanPolicyName_Type = OctetString
_CiscoSdwanPolicyName_Object = MibScalar
ciscoSdwanPolicyName = _CiscoSdwanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 14),
    _CiscoSdwanPolicyName_Type()
)
ciscoSdwanPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyName.setStatus("current")
_CiscoSdwanPolicyAccessListName_Type = OctetString
_CiscoSdwanPolicyAccessListName_Object = MibScalar
ciscoSdwanPolicyAccessListName = _CiscoSdwanPolicyAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 15),
    _CiscoSdwanPolicyAccessListName_Type()
)
ciscoSdwanPolicyAccessListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyAccessListName.setStatus("current")
_CiscoSdwanPolicyStatus_Type = OctetString
_CiscoSdwanPolicyStatus_Object = MibScalar
ciscoSdwanPolicyStatus = _CiscoSdwanPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 2, 16),
    _CiscoSdwanPolicyStatus_Type()
)
ciscoSdwanPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanPolicyStatus.setStatus("current")
_CiscoSdwanPolicyMIBConform_ObjectIdentity = ObjectIdentity
ciscoSdwanPolicyMIBConform = _CiscoSdwanPolicyMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3)
)
_CiscoSdwanPolicyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSdwanPolicyMIBCompliances = _CiscoSdwanPolicyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 1)
)
_CiscoSdwanPolicyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSdwanPolicyMIBGroups = _CiscoSdwanPolicyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2)
)

# Managed Objects groups

cSdwanPolicyDataPolicyFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 1)
)
cSdwanPolicyDataPolicyFilterGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyDataPolicyFilterGroup.setStatus("current")

cSdwanPolicyDataPolicyFilterVpnlistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 2)
)
cSdwanPolicyDataPolicyFilterVpnlistGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyDataPolicyFilterVpnlistGroup.setStatus("current")

cSdwanPolicyDataPolicyFilterVpnlistCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 3)
)
cSdwanPolicyDataPolicyFilterVpnlistCounterGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistCounterPackets"),
        ("CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistCounterBytes"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyDataPolicyFilterVpnlistCounterGroup.setStatus("current")

cSdwanPolicyDataPolicyFilterVpnlistPolicerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 4)
)
cSdwanPolicyDataPolicyFilterVpnlistPolicerGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistPolicerOosPackets"),
        ("CISCO-SDWAN-POLICY-MIB", "policyDataPolicyFilterVpnlistPolicerOosBytes"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyDataPolicyFilterVpnlistPolicerGroup.setStatus("current")

cSdwanPolicyAppRoutePolicyFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 5)
)
cSdwanPolicyAppRoutePolicyFilterGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyAppRoutePolicyFilterGroup.setStatus("current")

cSdwanPolicyAppRoutePolicyFilterVpnlistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 6)
)
cSdwanPolicyAppRoutePolicyFilterVpnlistGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterVpnlistName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyAppRoutePolicyFilterVpnlistGroup.setStatus("current")

cSdwanPolicyAppRoutePolicyFilterVpnlistCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 7)
)
cSdwanPolicyAppRoutePolicyFilterVpnlistCounterGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterVpnlistCounterPackets"),
        ("CISCO-SDWAN-POLICY-MIB", "policyAppRoutePolicyFilterVpnlistCounterBytes"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyAppRoutePolicyFilterVpnlistCounterGroup.setStatus("current")

cSdwanPolicyAccessListNamesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 8)
)
cSdwanPolicyAccessListNamesGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyAccessListNamesName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyAccessListNamesGroup.setStatus("current")

cSdwanPolicyAccessListCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 9)
)
cSdwanPolicyAccessListCountersGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyAccessListCountersName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyAccessListCountersGroup.setStatus("current")

cSdwanPolicyAccessListCountersAccessPolicyCounterListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 10)
)
cSdwanPolicyAccessListCountersAccessPolicyCounterListGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyAccessListCountersAccessPolicyCounterListPackets"),
        ("CISCO-SDWAN-POLICY-MIB", "policyAccessListCountersAccessPolicyCounterListBytes"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyAccessListCountersAccessPolicyCounterListGroup.setStatus("current")

cSdwanPolicyAccessListPolicersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 11)
)
cSdwanPolicyAccessListPolicersGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyAccessListPolicersName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyAccessListPolicersGroup.setStatus("current")

cSdwanPolicyAccessListPolicersAccessPolicyPolicerListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 12)
)
cSdwanPolicyAccessListPolicersAccessPolicyPolicerListGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyAccessListPolicersAccessPolicyPolicerListOosPackets"),
        ("CISCO-SDWAN-POLICY-MIB", "policyAccessListPolicersAccessPolicyPolicerListOosBytes"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyAccessListPolicersAccessPolicyPolicerListGroup.setStatus("current")

cSdwanPolicyAccessListAssociationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 13)
)
cSdwanPolicyAccessListAssociationsGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyAccessListAssociationsName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyAccessListAssociationsGroup.setStatus("current")

cSdwanPolicyAccessListAssociationsAccessPolicyInterfaceListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 14)
)
cSdwanPolicyAccessListAssociationsAccessPolicyInterfaceListGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyAccessListAssociationsAccessPolicyInterfaceListIntName"),
        ("CISCO-SDWAN-POLICY-MIB", "policyAccessListAssociationsAccessPolicyInterfaceListIntDir"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyAccessListAssociationsAccessPolicyInterfaceListGroup.setStatus("current")

cSdwanPolicyRewriteAssociationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 15)
)
cSdwanPolicyRewriteAssociationsGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyRewriteAssociationsName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyRewriteAssociationsGroup.setStatus("current")

cSdwanPolicyRewriteAssociationsRewriteInterfaceListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 16)
)
cSdwanPolicyRewriteAssociationsRewriteInterfaceListGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyRewriteAssociationsRewriteInterfaceListInterfaceName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyRewriteAssociationsRewriteInterfaceListGroup.setStatus("current")

cSdwanPolicyFromVsmartSlaClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 17)
)
cSdwanPolicyFromVsmartSlaClassGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartSlaClassLoss"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartSlaClassLatency"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartSlaClassJitter"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartSlaClassAppProbeClass"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartSlaClassGroup.setStatus("current")

cSdwanPolicyFromVsmartListsVpnListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 18)
)
cSdwanPolicyFromVsmartListsVpnListGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsVpnListName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartListsVpnListGroup.setStatus("current")

cSdwanPolicyFromVsmartListsVpnListVpnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 19)
)
cSdwanPolicyFromVsmartListsVpnListVpnGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsVpnListVpnId")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartListsVpnListVpnGroup.setStatus("current")

cSdwanPolicyFromVsmartListsDataPrefixListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 20)
)
cSdwanPolicyFromVsmartListsDataPrefixListGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsDataPrefixListName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartListsDataPrefixListGroup.setStatus("current")

cSdwanPolicyFromVsmartListsDataPrefixListIpPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 21)
)
cSdwanPolicyFromVsmartListsDataPrefixListIpPrefixGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsDataPrefixListIpPrefixIp")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartListsDataPrefixListIpPrefixGroup.setStatus("current")

cSdwanPolicyFromVsmartListsTlocListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 22)
)
cSdwanPolicyFromVsmartListsTlocListGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsTlocListName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartListsTlocListGroup.setStatus("current")

cSdwanPolicyFromVsmartListsTlocListTlocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 23)
)
cSdwanPolicyFromVsmartListsTlocListTlocGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsTlocListTlocPreference")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartListsTlocListTlocGroup.setStatus("current")

cSdwanPolicyFromVsmartListsAppProbeClassListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 24)
)
cSdwanPolicyFromVsmartListsAppProbeClassListGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsAppProbeClassListForwardingClass")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartListsAppProbeClassListGroup.setStatus("current")

cSdwanPolicyFromVsmartListsAppProbeClassColorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 25)
)
cSdwanPolicyFromVsmartListsAppProbeClassColorGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartListsAppProbeClassColorDscp")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartListsAppProbeClassColorGroup.setStatus("current")

cSdwanPolicyNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 26)
)
cSdwanPolicyNotifObjsGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyVpnId"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyApplication"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySourceIp"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySourcePort"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDestinationIp"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDestinationPort"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyProtocol"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDscp"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySlaInformation"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySlaStatus"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyVpnListName"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyName"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyAccessListName"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyStatus"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyNotifObjsGroup.setStatus("current")

cSdwanPolicyFromVsmartDataPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 28)
)
cSdwanPolicyFromVsmartDataPolicyGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyDirection")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartDataPolicyGroup.setStatus("current")

cSdwanPolicyFromVsmartDataPolicyVpnListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 29)
)
cSdwanPolicyFromVsmartDataPolicyVpnListGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListDefaultAction")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartDataPolicyVpnListGroup.setStatus("current")

cSdwanPolicyFromVsmartDataPolicyVpnListSequenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 30)
)
cSdwanPolicyFromVsmartDataPolicyVpnListSequenceGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceMatchTcp"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionActionValue"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionCount"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionCflowd"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetVpn"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionLog"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSig"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartDataPolicyVpnListSequenceGroup.setStatus("current")

cSdwanpolicyFromVsmartDataPolVpnListSeqActSetVipTlocPrLstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 31)
)
cSdwanpolicyFromVsmartDataPolVpnListSeqActSetVipTlocPrLstGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf"))
)
if mibBuilder.loadTexts:
    cSdwanpolicyFromVsmartDataPolVpnListSeqActSetVipTlocPrLstGroup.setStatus("current")

cSdwanPolicyFromVsmartCflowdTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 32)
)
cSdwanPolicyFromVsmartCflowdTemplateGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateName"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateFlowActiveTimeout"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateFlowInactiveTimeout"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateTemplateRefresh"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateFlowSamplingInterval"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateProtocol"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartCflowdTemplateGroup.setStatus("current")

cSdwanPolicyFromVsmartCflowdTemplateCollectorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 33)
)
cSdwanPolicyFromVsmartCflowdTemplateCollectorGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorSourceInterface"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorExportSpreadEnable"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorExportSpreadAppTables"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorBFDMetricsExport"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartCflowdTemplateCollectorBFDExportInterval"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartCflowdTemplateCollectorGroup.setStatus("current")

cSdwanPolicyFromVsmartAppRoutePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 34)
)
cSdwanPolicyFromVsmartAppRoutePolicyGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartAppRoutePolicyGroup.setStatus("current")

cSdwanPolicyFromVsmartAppRoutePolicyVpnListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 35)
)
cSdwanPolicyFromVsmartAppRoutePolicyVpnListGroup.setObjects(
    ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName")
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartAppRoutePolicyVpnListGroup.setStatus("current")

cSdwanPolicyFromVsmartAppRoutePolicyVpnListSequenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 36)
)
cSdwanPolicyFromVsmartAppRoutePolicyVpnListSequenceGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceActionCount"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceActionLog"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartAppRoutePolicyVpnListSequenceGroup.setStatus("current")

cSdwanPolicyFromVsmartPolicerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 37)
)
cSdwanPolicyFromVsmartPolicerGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartPolicerRate"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartPolicerBurst"),
        ("CISCO-SDWAN-POLICY-MIB", "policyFromVsmartPolicerExceed"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyFromVsmartPolicerGroup.setStatus("current")


# Notification objects

ciscoSdwanPolicySlaViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 0, 1)
)
ciscoSdwanPolicySlaViolation.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyVpnId"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyApplication"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySourceIp"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySourcePort"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDestinationIp"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDestinationPort"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyProtocol"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDscp"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySlaInformation"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySlaStatus"))
)
if mibBuilder.loadTexts:
    ciscoSdwanPolicySlaViolation.setStatus(
        "current"
    )

ciscoSdwanPolicySlaViolationPktDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 0, 2)
)
ciscoSdwanPolicySlaViolationPktDrop.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyVpnId"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyApplication"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySourceIp"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySourcePort"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDestinationIp"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDestinationPort"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyProtocol"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDscp"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySlaInformation"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySlaStatus"))
)
if mibBuilder.loadTexts:
    ciscoSdwanPolicySlaViolationPktDrop.setStatus(
        "current"
    )

ciscoSdwanPolicyDataPolicyAssociationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 0, 3)
)
ciscoSdwanPolicyDataPolicyAssociationStatus.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyVpnListName"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyName"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyStatus"))
)
if mibBuilder.loadTexts:
    ciscoSdwanPolicyDataPolicyAssociationStatus.setStatus(
        "current"
    )

ciscoSdwanPolicyAccessListAssociationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 0, 4)
)
ciscoSdwanPolicyAccessListAssociationStatus.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyAccessListName"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyStatus"))
)
if mibBuilder.loadTexts:
    ciscoSdwanPolicyAccessListAssociationStatus.setStatus(
        "current"
    )


# Notifications groups

cSdwanPolicyNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 2, 27)
)
cSdwanPolicyNotifsGroup.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySlaViolation"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicySlaViolationPktDrop"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyDataPolicyAssociationStatus"),
        ("CISCO-SDWAN-POLICY-MIB", "ciscoSdwanPolicyAccessListAssociationStatus"))
)
if mibBuilder.loadTexts:
    cSdwanPolicyNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSdwanPolicyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1005, 3, 1, 1)
)
ciscoSdwanPolicyMIBCompliance.setObjects(
      *(("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyDataPolicyFilterGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyDataPolicyFilterVpnlistGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyDataPolicyFilterVpnlistCounterGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyDataPolicyFilterVpnlistPolicerGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAppRoutePolicyFilterGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAppRoutePolicyFilterVpnlistGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAppRoutePolicyFilterVpnlistCounterGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAccessListNamesGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAccessListCountersGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAccessListCountersAccessPolicyCounterListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAccessListPolicersGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAccessListPolicersAccessPolicyPolicerListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAccessListAssociationsGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyAccessListAssociationsAccessPolicyInterfaceListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyRewriteAssociationsGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyRewriteAssociationsRewriteInterfaceListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartSlaClassGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartListsVpnListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartListsVpnListVpnGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartListsDataPrefixListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartListsDataPrefixListIpPrefixGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartListsTlocListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartListsTlocListTlocGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartListsAppProbeClassListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartListsAppProbeClassColorGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyNotifObjsGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyNotifsGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartDataPolicyGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartDataPolicyVpnListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartDataPolicyVpnListSequenceGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanpolicyFromVsmartDataPolVpnListSeqActSetVipTlocPrLstGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartCflowdTemplateGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartCflowdTemplateCollectorGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartAppRoutePolicyGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartAppRoutePolicyVpnListGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartAppRoutePolicyVpnListSequenceGroup"),
        ("CISCO-SDWAN-POLICY-MIB", "cSdwanPolicyFromVsmartPolicerGroup"))
)
if mibBuilder.loadTexts:
    ciscoSdwanPolicyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDWAN-POLICY-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "Ipv4Prefix": Ipv4Prefix,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "DestinationIp": DestinationIp,
       "SourceIp": SourceIp,
       "TcpFlags": TcpFlags,
       "DataPolicyDirectionEnum": DataPolicyDirectionEnum,
       "DirectionEnum": DirectionEnum,
       "TransportProtocol": TransportProtocol,
       "ActionDataEnum": ActionDataEnum,
       "EncapsulationList": EncapsulationList,
       "FnfMonitorEnum": FnfMonitorEnum,
       "ColorList": ColorList,
       "NotificationSeverity": NotificationSeverity,
       "VpnId": VpnId,
       "ciscoSdwanPolicyMIB": ciscoSdwanPolicyMIB,
       "ciscoSdwanPolicyMIBNotifs": ciscoSdwanPolicyMIBNotifs,
       "ciscoSdwanPolicySlaViolation": ciscoSdwanPolicySlaViolation,
       "ciscoSdwanPolicySlaViolationPktDrop": ciscoSdwanPolicySlaViolationPktDrop,
       "ciscoSdwanPolicyDataPolicyAssociationStatus": ciscoSdwanPolicyDataPolicyAssociationStatus,
       "ciscoSdwanPolicyAccessListAssociationStatus": ciscoSdwanPolicyAccessListAssociationStatus,
       "ciscoSdwanPolicyMIBObjects": ciscoSdwanPolicyMIBObjects,
       "policy": policy,
       "policyDataPolicyFilter": policyDataPolicyFilter,
       "policyDataPolicyFilterTable": policyDataPolicyFilterTable,
       "policyDataPolicyFilterEntry": policyDataPolicyFilterEntry,
       "policyDataPolicyFilterName": policyDataPolicyFilterName,
       "policyDataPolicyFilterVpnlistTable": policyDataPolicyFilterVpnlistTable,
       "policyDataPolicyFilterVpnlistEntry": policyDataPolicyFilterVpnlistEntry,
       "policyDataPolicyFilterVpnlistName": policyDataPolicyFilterVpnlistName,
       "policyDataPolicyFilterVpnlistCounterTable": policyDataPolicyFilterVpnlistCounterTable,
       "policyDataPolicyFilterVpnlistCounterEntry": policyDataPolicyFilterVpnlistCounterEntry,
       "policyDataPolicyFilterVpnlistCounterName": policyDataPolicyFilterVpnlistCounterName,
       "policyDataPolicyFilterVpnlistCounterPackets": policyDataPolicyFilterVpnlistCounterPackets,
       "policyDataPolicyFilterVpnlistCounterBytes": policyDataPolicyFilterVpnlistCounterBytes,
       "policyDataPolicyFilterVpnlistPolicerTable": policyDataPolicyFilterVpnlistPolicerTable,
       "policyDataPolicyFilterVpnlistPolicerEntry": policyDataPolicyFilterVpnlistPolicerEntry,
       "policyDataPolicyFilterVpnlistPolicerName": policyDataPolicyFilterVpnlistPolicerName,
       "policyDataPolicyFilterVpnlistPolicerOosPackets": policyDataPolicyFilterVpnlistPolicerOosPackets,
       "policyDataPolicyFilterVpnlistPolicerOosBytes": policyDataPolicyFilterVpnlistPolicerOosBytes,
       "policyAppRoutePolicy": policyAppRoutePolicy,
       "policyAppRoutePolicyFilterTable": policyAppRoutePolicyFilterTable,
       "policyAppRoutePolicyFilterEntry": policyAppRoutePolicyFilterEntry,
       "policyAppRoutePolicyFilterName": policyAppRoutePolicyFilterName,
       "policyAppRoutePolicyFilterVpnlistTable": policyAppRoutePolicyFilterVpnlistTable,
       "policyAppRoutePolicyFilterVpnlistEntry": policyAppRoutePolicyFilterVpnlistEntry,
       "policyAppRoutePolicyFilterVpnlistName": policyAppRoutePolicyFilterVpnlistName,
       "policyAppRoutePolicyFilterVpnlistCounterTable": policyAppRoutePolicyFilterVpnlistCounterTable,
       "policyAppRoutePolicyFilterVpnlistCounterEntry": policyAppRoutePolicyFilterVpnlistCounterEntry,
       "policyAppRoutePolicyFilterVpnlistCounterName": policyAppRoutePolicyFilterVpnlistCounterName,
       "policyAppRoutePolicyFilterVpnlistCounterPackets": policyAppRoutePolicyFilterVpnlistCounterPackets,
       "policyAppRoutePolicyFilterVpnlistCounterBytes": policyAppRoutePolicyFilterVpnlistCounterBytes,
       "policyAccessListNames": policyAccessListNames,
       "policyAccessListNamesTable": policyAccessListNamesTable,
       "policyAccessListNamesEntry": policyAccessListNamesEntry,
       "policyAccessListNamesName": policyAccessListNamesName,
       "policyAccessListCounters": policyAccessListCounters,
       "policyAccessListCountersTable": policyAccessListCountersTable,
       "policyAccessListCountersEntry": policyAccessListCountersEntry,
       "policyAccessListCountersName": policyAccessListCountersName,
       "policyAccessListCountersAccessPolicyCounterListTable": policyAccessListCountersAccessPolicyCounterListTable,
       "policyAccessListCountersAccessPolicyCounterListEntry": policyAccessListCountersAccessPolicyCounterListEntry,
       "policyAccessListCountersAccessPolicyCounterListCounterName": policyAccessListCountersAccessPolicyCounterListCounterName,
       "policyAccessListCountersAccessPolicyCounterListPackets": policyAccessListCountersAccessPolicyCounterListPackets,
       "policyAccessListCountersAccessPolicyCounterListBytes": policyAccessListCountersAccessPolicyCounterListBytes,
       "policyAccessListPolicers": policyAccessListPolicers,
       "policyAccessListPolicersTable": policyAccessListPolicersTable,
       "policyAccessListPolicersEntry": policyAccessListPolicersEntry,
       "policyAccessListPolicersName": policyAccessListPolicersName,
       "policyAccessListPolicersAccessPolicyPolicerListTable": policyAccessListPolicersAccessPolicyPolicerListTable,
       "policyAccessListPolicersAccessPolicyPolicerListEntry": policyAccessListPolicersAccessPolicyPolicerListEntry,
       "policyAccessListPolicersAccessPolicyPolicerListPolicerName": policyAccessListPolicersAccessPolicyPolicerListPolicerName,
       "policyAccessListPolicersAccessPolicyPolicerListOosPackets": policyAccessListPolicersAccessPolicyPolicerListOosPackets,
       "policyAccessListPolicersAccessPolicyPolicerListOosBytes": policyAccessListPolicersAccessPolicyPolicerListOosBytes,
       "policyAccessListAssociations": policyAccessListAssociations,
       "policyAccessListAssociationsTable": policyAccessListAssociationsTable,
       "policyAccessListAssociationsEntry": policyAccessListAssociationsEntry,
       "policyAccessListAssociationsName": policyAccessListAssociationsName,
       "policyAccessListAssociationsAccessPolicyInterfaceListTable": policyAccessListAssociationsAccessPolicyInterfaceListTable,
       "policyAccessListAssociationsAccessPolicyInterfaceListEntry": policyAccessListAssociationsAccessPolicyInterfaceListEntry,
       "policyAccessListAssociationsAccessPolicyInterfaceListIntName": policyAccessListAssociationsAccessPolicyInterfaceListIntName,
       "policyAccessListAssociationsAccessPolicyInterfaceListIntDir": policyAccessListAssociationsAccessPolicyInterfaceListIntDir,
       "policyRewriteAssociations": policyRewriteAssociations,
       "policyRewriteAssociationsTable": policyRewriteAssociationsTable,
       "policyRewriteAssociationsEntry": policyRewriteAssociationsEntry,
       "policyRewriteAssociationsName": policyRewriteAssociationsName,
       "policyRewriteAssociationsRewriteInterfaceListTable": policyRewriteAssociationsRewriteInterfaceListTable,
       "policyRewriteAssociationsRewriteInterfaceListEntry": policyRewriteAssociationsRewriteInterfaceListEntry,
       "policyRewriteAssociationsRewriteInterfaceListInterfaceName": policyRewriteAssociationsRewriteInterfaceListInterfaceName,
       "policyFromVsmart": policyFromVsmart,
       "policyFromVsmartSlaClassTable": policyFromVsmartSlaClassTable,
       "policyFromVsmartSlaClassEntry": policyFromVsmartSlaClassEntry,
       "policyFromVsmartSlaClassName": policyFromVsmartSlaClassName,
       "policyFromVsmartSlaClassLoss": policyFromVsmartSlaClassLoss,
       "policyFromVsmartSlaClassLatency": policyFromVsmartSlaClassLatency,
       "policyFromVsmartSlaClassJitter": policyFromVsmartSlaClassJitter,
       "policyFromVsmartSlaClassAppProbeClass": policyFromVsmartSlaClassAppProbeClass,
       "policyFromVsmartDataPolicyTable": policyFromVsmartDataPolicyTable,
       "policyFromVsmartDataPolicyEntry": policyFromVsmartDataPolicyEntry,
       "policyFromVsmartDataPolicyName": policyFromVsmartDataPolicyName,
       "policyFromVsmartDataPolicyDirection": policyFromVsmartDataPolicyDirection,
       "policyFromVsmartDataPolicyVpnListTable": policyFromVsmartDataPolicyVpnListTable,
       "policyFromVsmartDataPolicyVpnListEntry": policyFromVsmartDataPolicyVpnListEntry,
       "policyFromVsmartDataPolicyVpnListName": policyFromVsmartDataPolicyVpnListName,
       "policyFromVsmartDataPolicyVpnListDefaultAction": policyFromVsmartDataPolicyVpnListDefaultAction,
       "policyFromVsmartDataPolicyVpnListSequenceTable": policyFromVsmartDataPolicyVpnListSequenceTable,
       "policyFromVsmartDataPolicyVpnListSequenceEntry": policyFromVsmartDataPolicyVpnListSequenceEntry,
       "policyFromVsmartDataPolicyVpnListSequenceSeqValue": policyFromVsmartDataPolicyVpnListSequenceSeqValue,
       "policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst": policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst,
       "policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst": policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst,
       "policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst": policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst,
       "policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst": policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst,
       "policyFromVsmartDataPolicyVpnListSequenceMatchTcp": policyFromVsmartDataPolicyVpnListSequenceMatchTcp,
       "policyFromVsmartDataPolicyVpnListSequenceActionActionValue": policyFromVsmartDataPolicyVpnListSequenceActionActionValue,
       "policyFromVsmartDataPolicyVpnListSequenceActionCount": policyFromVsmartDataPolicyVpnListSequenceActionCount,
       "policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn": policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn,
       "policyFromVsmartDataPolicyVpnListSequenceActionCflowd": policyFromVsmartDataPolicyVpnListSequenceActionCflowd,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor": policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap": policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop": policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer": policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetVpn": policyFromVsmartDataPolicyVpnListSequenceActionSetVpn,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel": policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp": policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor": policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList": policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType": policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn": policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp": policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr": policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr,
       "policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst": policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal": policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal,
       "policyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict": policyFromVsmartDataPolicyVpnListSeqActSetServiceRestrict,
       "policyFromVsmartDataPolicyVpnListSequenceActionLog": policyFromVsmartDataPolicyVpnListSequenceActionLog,
       "policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor": policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListColor,
       "policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap": policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListEncap,
       "policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict": policyFromVsmartDataPolicyVpnListSeqActSetLocalTlocListRestrict,
       "policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization": policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6": policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6,
       "policyFromVsmartDataPolicyVpnListSequenceActionSig": policyFromVsmartDataPolicyVpnListSequenceActionSig,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose": policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopLoose,
       "policyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute": policyFromVsmartDataPolicyVpnListSeqActSigFallbackToRoute,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf,
       "policyFromVsmartCflowdTemplate": policyFromVsmartCflowdTemplate,
       "policyFromVsmartCflowdTemplateName": policyFromVsmartCflowdTemplateName,
       "policyFromVsmartCflowdTemplateFlowActiveTimeout": policyFromVsmartCflowdTemplateFlowActiveTimeout,
       "policyFromVsmartCflowdTemplateFlowInactiveTimeout": policyFromVsmartCflowdTemplateFlowInactiveTimeout,
       "policyFromVsmartCflowdTemplateTemplateRefresh": policyFromVsmartCflowdTemplateTemplateRefresh,
       "policyFromVsmartCflowdTemplateFlowSamplingInterval": policyFromVsmartCflowdTemplateFlowSamplingInterval,
       "policyFromVsmartCflowdTemplateProtocol": policyFromVsmartCflowdTemplateProtocol,
       "policyFromVsmartCflowdTemplateCollectorTable": policyFromVsmartCflowdTemplateCollectorTable,
       "policyFromVsmartCflowdTemplateCollectorEntry": policyFromVsmartCflowdTemplateCollectorEntry,
       "policyFromVsmartCflowdTemplateCollectorVpn": policyFromVsmartCflowdTemplateCollectorVpn,
       "policyFromVsmartCflowdTemplateCollectorAddress": policyFromVsmartCflowdTemplateCollectorAddress,
       "policyFromVsmartCflowdTemplateCollectorPort": policyFromVsmartCflowdTemplateCollectorPort,
       "policyFromVsmartCflowdTemplateCollectorTransport": policyFromVsmartCflowdTemplateCollectorTransport,
       "policyFromVsmartCflowdTemplateCollectorSourceInterface": policyFromVsmartCflowdTemplateCollectorSourceInterface,
       "policyFromVsmartCflowdTemplateCollectorExportSpreadEnable": policyFromVsmartCflowdTemplateCollectorExportSpreadEnable,
       "policyFromVsmartCflowdTemplateCollectorExportSpreadAppTables": policyFromVsmartCflowdTemplateCollectorExportSpreadAppTables,
       "policyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables": policyFromVsmartCflowdTemplateCollectorExportSpreadTlocTables,
       "policyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables": policyFromVsmartCflowdTemplateCollectorExportSpreadOtherTables,
       "policyFromVsmartCflowdTemplateCollectorBfdMetricsExport": policyFromVsmartCflowdTemplateCollectorBfdMetricsExport,
       "policyFromVsmartCflowdTemplateCollectorBFDExportInterval": policyFromVsmartCflowdTemplateCollectorBFDExportInterval,
       "policyFromVsmartAppRoutePolicyTable": policyFromVsmartAppRoutePolicyTable,
       "policyFromVsmartAppRoutePolicyEntry": policyFromVsmartAppRoutePolicyEntry,
       "policyFromVsmartAppRoutePolicyName": policyFromVsmartAppRoutePolicyName,
       "policyFromVsmartAppRoutePolicyVpnListTable": policyFromVsmartAppRoutePolicyVpnListTable,
       "policyFromVsmartAppRoutePolicyVpnListEntry": policyFromVsmartAppRoutePolicyVpnListEntry,
       "policyFromVsmartAppRoutePolicyVpnListName": policyFromVsmartAppRoutePolicyVpnListName,
       "policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName": policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName,
       "policyFromVsmartAppRoutePolicyVpnListSequenceTable": policyFromVsmartAppRoutePolicyVpnListSequenceTable,
       "policyFromVsmartAppRoutePolicyVpnListSequenceEntry": policyFromVsmartAppRoutePolicyVpnListSequenceEntry,
       "policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue": policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue,
       "policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst": policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst,
       "policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst": policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst,
       "policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst": policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst,
       "policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst": policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionCount": policyFromVsmartAppRoutePolicyVpnListSequenceActionCount,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName": policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict": policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr": policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionLog": policyFromVsmartAppRoutePolicyVpnListSequenceActionLog,
       "policyFromVsmartAppRoutePolicyVpnListSeqActBackupSlaPrefClr": policyFromVsmartAppRoutePolicyVpnListSeqActBackupSlaPrefClr,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback": policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClFallback,
       "policyFromVsmartPolicerTable": policyFromVsmartPolicerTable,
       "policyFromVsmartPolicerEntry": policyFromVsmartPolicerEntry,
       "policyFromVsmartPolicerName": policyFromVsmartPolicerName,
       "policyFromVsmartPolicerRate": policyFromVsmartPolicerRate,
       "policyFromVsmartPolicerBurst": policyFromVsmartPolicerBurst,
       "policyFromVsmartPolicerExceed": policyFromVsmartPolicerExceed,
       "policyFromVsmartListsVpnListTable": policyFromVsmartListsVpnListTable,
       "policyFromVsmartListsVpnListEntry": policyFromVsmartListsVpnListEntry,
       "policyFromVsmartListsVpnListName": policyFromVsmartListsVpnListName,
       "policyFromVsmartListsVpnListVpnTable": policyFromVsmartListsVpnListVpnTable,
       "policyFromVsmartListsVpnListVpnEntry": policyFromVsmartListsVpnListVpnEntry,
       "policyFromVsmartListsVpnListVpnId": policyFromVsmartListsVpnListVpnId,
       "policyFromVsmartListsDataPrefixListTable": policyFromVsmartListsDataPrefixListTable,
       "policyFromVsmartListsDataPrefixListEntry": policyFromVsmartListsDataPrefixListEntry,
       "policyFromVsmartListsDataPrefixListName": policyFromVsmartListsDataPrefixListName,
       "policyFromVsmartListsDataPrefixListIpPrefixTable": policyFromVsmartListsDataPrefixListIpPrefixTable,
       "policyFromVsmartListsDataPrefixListIpPrefixEntry": policyFromVsmartListsDataPrefixListIpPrefixEntry,
       "policyFromVsmartListsDataPrefixListIpPrefixIp": policyFromVsmartListsDataPrefixListIpPrefixIp,
       "policyFromVsmartListsTlocListTable": policyFromVsmartListsTlocListTable,
       "policyFromVsmartListsTlocListEntry": policyFromVsmartListsTlocListEntry,
       "policyFromVsmartListsTlocListName": policyFromVsmartListsTlocListName,
       "policyFromVsmartListsTlocListTlocTable": policyFromVsmartListsTlocListTlocTable,
       "policyFromVsmartListsTlocListTlocEntry": policyFromVsmartListsTlocListTlocEntry,
       "policyFromVsmartListsTlocListTlocIp": policyFromVsmartListsTlocListTlocIp,
       "policyFromVsmartListsTlocListTlocColor": policyFromVsmartListsTlocListTlocColor,
       "policyFromVsmartListsTlocListTlocEncap": policyFromVsmartListsTlocListTlocEncap,
       "policyFromVsmartListsTlocListTlocPreference": policyFromVsmartListsTlocListTlocPreference,
       "policyFromVsmartListsAppProbeClassListTable": policyFromVsmartListsAppProbeClassListTable,
       "policyFromVsmartListsAppProbeClassListEntry": policyFromVsmartListsAppProbeClassListEntry,
       "policyFromVsmartListsAppProbeClassListName": policyFromVsmartListsAppProbeClassListName,
       "policyFromVsmartListsAppProbeClassListForwardingClass": policyFromVsmartListsAppProbeClassListForwardingClass,
       "policyFromVsmartListsAppProbeClassColorTable": policyFromVsmartListsAppProbeClassColorTable,
       "policyFromVsmartListsAppProbeClassColorEntry": policyFromVsmartListsAppProbeClassColorEntry,
       "policyFromVsmartListsAppProbeClassColorName": policyFromVsmartListsAppProbeClassColorName,
       "policyFromVsmartListsAppProbeClassColorDscp": policyFromVsmartListsAppProbeClassColorDscp,
       "ciscoSdwanPolicyMIBNotifObjects": ciscoSdwanPolicyMIBNotifObjects,
       "netconfNotificationSeverity": netconfNotificationSeverity,
       "ciscoSdwanPolicyVpnId": ciscoSdwanPolicyVpnId,
       "ciscoSdwanPolicyApplication": ciscoSdwanPolicyApplication,
       "ciscoSdwanPolicySourceIp": ciscoSdwanPolicySourceIp,
       "ciscoSdwanPolicySourcePort": ciscoSdwanPolicySourcePort,
       "ciscoSdwanPolicyDestinationIp": ciscoSdwanPolicyDestinationIp,
       "ciscoSdwanPolicyDestinationPort": ciscoSdwanPolicyDestinationPort,
       "ciscoSdwanPolicyProtocol": ciscoSdwanPolicyProtocol,
       "ciscoSdwanPolicyDscp": ciscoSdwanPolicyDscp,
       "ciscoSdwanPolicySlaInformation": ciscoSdwanPolicySlaInformation,
       "ciscoSdwanPolicySlaStatus": ciscoSdwanPolicySlaStatus,
       "ciscoSdwanPolicyVpnListName": ciscoSdwanPolicyVpnListName,
       "ciscoSdwanPolicyName": ciscoSdwanPolicyName,
       "ciscoSdwanPolicyAccessListName": ciscoSdwanPolicyAccessListName,
       "ciscoSdwanPolicyStatus": ciscoSdwanPolicyStatus,
       "ciscoSdwanPolicyMIBConform": ciscoSdwanPolicyMIBConform,
       "ciscoSdwanPolicyMIBCompliances": ciscoSdwanPolicyMIBCompliances,
       "ciscoSdwanPolicyMIBCompliance": ciscoSdwanPolicyMIBCompliance,
       "ciscoSdwanPolicyMIBGroups": ciscoSdwanPolicyMIBGroups,
       "cSdwanPolicyDataPolicyFilterGroup": cSdwanPolicyDataPolicyFilterGroup,
       "cSdwanPolicyDataPolicyFilterVpnlistGroup": cSdwanPolicyDataPolicyFilterVpnlistGroup,
       "cSdwanPolicyDataPolicyFilterVpnlistCounterGroup": cSdwanPolicyDataPolicyFilterVpnlistCounterGroup,
       "cSdwanPolicyDataPolicyFilterVpnlistPolicerGroup": cSdwanPolicyDataPolicyFilterVpnlistPolicerGroup,
       "cSdwanPolicyAppRoutePolicyFilterGroup": cSdwanPolicyAppRoutePolicyFilterGroup,
       "cSdwanPolicyAppRoutePolicyFilterVpnlistGroup": cSdwanPolicyAppRoutePolicyFilterVpnlistGroup,
       "cSdwanPolicyAppRoutePolicyFilterVpnlistCounterGroup": cSdwanPolicyAppRoutePolicyFilterVpnlistCounterGroup,
       "cSdwanPolicyAccessListNamesGroup": cSdwanPolicyAccessListNamesGroup,
       "cSdwanPolicyAccessListCountersGroup": cSdwanPolicyAccessListCountersGroup,
       "cSdwanPolicyAccessListCountersAccessPolicyCounterListGroup": cSdwanPolicyAccessListCountersAccessPolicyCounterListGroup,
       "cSdwanPolicyAccessListPolicersGroup": cSdwanPolicyAccessListPolicersGroup,
       "cSdwanPolicyAccessListPolicersAccessPolicyPolicerListGroup": cSdwanPolicyAccessListPolicersAccessPolicyPolicerListGroup,
       "cSdwanPolicyAccessListAssociationsGroup": cSdwanPolicyAccessListAssociationsGroup,
       "cSdwanPolicyAccessListAssociationsAccessPolicyInterfaceListGroup": cSdwanPolicyAccessListAssociationsAccessPolicyInterfaceListGroup,
       "cSdwanPolicyRewriteAssociationsGroup": cSdwanPolicyRewriteAssociationsGroup,
       "cSdwanPolicyRewriteAssociationsRewriteInterfaceListGroup": cSdwanPolicyRewriteAssociationsRewriteInterfaceListGroup,
       "cSdwanPolicyFromVsmartSlaClassGroup": cSdwanPolicyFromVsmartSlaClassGroup,
       "cSdwanPolicyFromVsmartListsVpnListGroup": cSdwanPolicyFromVsmartListsVpnListGroup,
       "cSdwanPolicyFromVsmartListsVpnListVpnGroup": cSdwanPolicyFromVsmartListsVpnListVpnGroup,
       "cSdwanPolicyFromVsmartListsDataPrefixListGroup": cSdwanPolicyFromVsmartListsDataPrefixListGroup,
       "cSdwanPolicyFromVsmartListsDataPrefixListIpPrefixGroup": cSdwanPolicyFromVsmartListsDataPrefixListIpPrefixGroup,
       "cSdwanPolicyFromVsmartListsTlocListGroup": cSdwanPolicyFromVsmartListsTlocListGroup,
       "cSdwanPolicyFromVsmartListsTlocListTlocGroup": cSdwanPolicyFromVsmartListsTlocListTlocGroup,
       "cSdwanPolicyFromVsmartListsAppProbeClassListGroup": cSdwanPolicyFromVsmartListsAppProbeClassListGroup,
       "cSdwanPolicyFromVsmartListsAppProbeClassColorGroup": cSdwanPolicyFromVsmartListsAppProbeClassColorGroup,
       "cSdwanPolicyNotifObjsGroup": cSdwanPolicyNotifObjsGroup,
       "cSdwanPolicyNotifsGroup": cSdwanPolicyNotifsGroup,
       "cSdwanPolicyFromVsmartDataPolicyGroup": cSdwanPolicyFromVsmartDataPolicyGroup,
       "cSdwanPolicyFromVsmartDataPolicyVpnListGroup": cSdwanPolicyFromVsmartDataPolicyVpnListGroup,
       "cSdwanPolicyFromVsmartDataPolicyVpnListSequenceGroup": cSdwanPolicyFromVsmartDataPolicyVpnListSequenceGroup,
       "cSdwanpolicyFromVsmartDataPolVpnListSeqActSetVipTlocPrLstGroup": cSdwanpolicyFromVsmartDataPolVpnListSeqActSetVipTlocPrLstGroup,
       "cSdwanPolicyFromVsmartCflowdTemplateGroup": cSdwanPolicyFromVsmartCflowdTemplateGroup,
       "cSdwanPolicyFromVsmartCflowdTemplateCollectorGroup": cSdwanPolicyFromVsmartCflowdTemplateCollectorGroup,
       "cSdwanPolicyFromVsmartAppRoutePolicyGroup": cSdwanPolicyFromVsmartAppRoutePolicyGroup,
       "cSdwanPolicyFromVsmartAppRoutePolicyVpnListGroup": cSdwanPolicyFromVsmartAppRoutePolicyVpnListGroup,
       "cSdwanPolicyFromVsmartAppRoutePolicyVpnListSequenceGroup": cSdwanPolicyFromVsmartAppRoutePolicyVpnListSequenceGroup,
       "cSdwanPolicyFromVsmartPolicerGroup": cSdwanPolicyFromVsmartPolicerGroup}
)
