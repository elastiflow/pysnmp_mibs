# SNMP MIB module (CISCO-SDWAN-PROBE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SDWAN-PROBE-MIB.mib
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

(TextualConvention,
 ciscoMgmt) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "TextualConvention",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSdwanProbeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008)
)
if mibBuilder.loadTexts:
    ciscoSdwanProbeMIB.setRevisions(
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



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


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

_CiscoSdwanProbeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanProbeMIBObjects = _CiscoSdwanProbeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1)
)
_ProbeApplicationsTable_Object = MibTable
probeApplicationsTable = _ProbeApplicationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2)
)
if mibBuilder.loadTexts:
    probeApplicationsTable.setStatus("current")
_ProbeApplicationsEntry_Object = MibTableRow
probeApplicationsEntry = _ProbeApplicationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1)
)
probeApplicationsEntry.setIndexNames(
    (0, "CISCO-SDWAN-PROBE-MIB", "probeApplicationsVpnId"),
    (0, "CISCO-SDWAN-PROBE-MIB", "probeApplicationsAppType"),
    (0, "CISCO-SDWAN-PROBE-MIB", "probeApplicationsAppId"),
)
if mibBuilder.loadTexts:
    probeApplicationsEntry.setStatus("current")
_ProbeApplicationsVpnId_Type = Unsigned32
_ProbeApplicationsVpnId_Object = MibTableColumn
probeApplicationsVpnId = _ProbeApplicationsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 1),
    _ProbeApplicationsVpnId_Type()
)
probeApplicationsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeApplicationsVpnId.setStatus("current")


class _ProbeApplicationsAppType_Type(Integer32):
    """Custom type probeApplicationsAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cxp-app-type-unset", 0),
          ("cxp-app-type-app-id", 1),
          ("cxp-app-type-app-grp", 2),
          ("cxp-app-type-svc-area", 3),
          ("cxp-app-type-region", 4),
          ("cxp-app-type-custom-app-grp", 5))
    )


_ProbeApplicationsAppType_Type.__name__ = "Integer32"
_ProbeApplicationsAppType_Object = MibTableColumn
probeApplicationsAppType = _ProbeApplicationsAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 2),
    _ProbeApplicationsAppType_Type()
)
probeApplicationsAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeApplicationsAppType.setStatus("current")
_ProbeApplicationsAppId_Type = Unsigned32
_ProbeApplicationsAppId_Object = MibTableColumn
probeApplicationsAppId = _ProbeApplicationsAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 3),
    _ProbeApplicationsAppId_Type()
)
probeApplicationsAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeApplicationsAppId.setStatus("current")
_ProbeApplicationsSubAppId_Type = Unsigned32
_ProbeApplicationsSubAppId_Object = MibTableColumn
probeApplicationsSubAppId = _ProbeApplicationsSubAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 4),
    _ProbeApplicationsSubAppId_Type()
)
probeApplicationsSubAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeApplicationsSubAppId.setStatus("current")


class _ProbeApplicationsApp_Type(String):
    """Custom type probeApplicationsApp based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ProbeApplicationsApp_Type.__name__ = "String"
_ProbeApplicationsApp_Object = MibTableColumn
probeApplicationsApp = _ProbeApplicationsApp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 5),
    _ProbeApplicationsApp_Type()
)
probeApplicationsApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeApplicationsApp.setStatus("current")


class _ProbeApplicationsExitType_Type(Integer32):
    """Custom type probeApplicationsExitType based on Integer32"""
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
        *(("cxp-exit-unset", 0),
          ("cxp-exit-gateway", 1),
          ("cxp-exit-local", 2),
          ("cxp-exit-uncomputed", 3),
          ("cxp-exit-none", 4))
    )


_ProbeApplicationsExitType_Type.__name__ = "Integer32"
_ProbeApplicationsExitType_Object = MibTableColumn
probeApplicationsExitType = _ProbeApplicationsExitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 6),
    _ProbeApplicationsExitType_Type()
)
probeApplicationsExitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeApplicationsExitType.setStatus("current")
_ProbeApplicationsGwSysIp_Type = InetAddressIP
_ProbeApplicationsGwSysIp_Object = MibTableColumn
probeApplicationsGwSysIp = _ProbeApplicationsGwSysIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 7),
    _ProbeApplicationsGwSysIp_Type()
)
probeApplicationsGwSysIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeApplicationsGwSysIp.setStatus("current")


class _ProbeApplicationsInterface_Type(String):
    """Custom type probeApplicationsInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ProbeApplicationsInterface_Type.__name__ = "String"
_ProbeApplicationsInterface_Object = MibTableColumn
probeApplicationsInterface = _ProbeApplicationsInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 8),
    _ProbeApplicationsInterface_Type()
)
probeApplicationsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeApplicationsInterface.setStatus("current")
_ProbeApplicationsLatency_Type = Unsigned32
_ProbeApplicationsLatency_Object = MibTableColumn
probeApplicationsLatency = _ProbeApplicationsLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 9),
    _ProbeApplicationsLatency_Type()
)
probeApplicationsLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeApplicationsLatency.setStatus("current")
_ProbeApplicationsLoss_Type = Unsigned32
_ProbeApplicationsLoss_Object = MibTableColumn
probeApplicationsLoss = _ProbeApplicationsLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 10),
    _ProbeApplicationsLoss_Type()
)
probeApplicationsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeApplicationsLoss.setStatus("current")


class _ProbeApplicationsRemoteColor_Type(Integer32):
    """Custom type probeApplicationsRemoteColor based on Integer32"""
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


_ProbeApplicationsRemoteColor_Type.__name__ = "Integer32"
_ProbeApplicationsRemoteColor_Object = MibTableColumn
probeApplicationsRemoteColor = _ProbeApplicationsRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 11),
    _ProbeApplicationsRemoteColor_Type()
)
probeApplicationsRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeApplicationsRemoteColor.setStatus("current")


class _ProbeApplicationsLocalColor_Type(Integer32):
    """Custom type probeApplicationsLocalColor based on Integer32"""
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


_ProbeApplicationsLocalColor_Type.__name__ = "Integer32"
_ProbeApplicationsLocalColor_Object = MibTableColumn
probeApplicationsLocalColor = _ProbeApplicationsLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 12),
    _ProbeApplicationsLocalColor_Type()
)
probeApplicationsLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeApplicationsLocalColor.setStatus("current")
_ProbeLocalTable_Object = MibTable
probeLocalTable = _ProbeLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3)
)
if mibBuilder.loadTexts:
    probeLocalTable.setStatus("current")
_ProbeLocalEntry_Object = MibTableRow
probeLocalEntry = _ProbeLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1)
)
probeLocalEntry.setIndexNames(
    (0, "CISCO-SDWAN-PROBE-MIB", "probeLocalVpnId"),
    (0, "CISCO-SDWAN-PROBE-MIB", "probeLocalAppType"),
    (0, "CISCO-SDWAN-PROBE-MIB", "probeLocalAppId"),
    (0, "CISCO-SDWAN-PROBE-MIB", "probeLocalSubAppId"),
    (0, "CISCO-SDWAN-PROBE-MIB", "probeLocalInterface"),
)
if mibBuilder.loadTexts:
    probeLocalEntry.setStatus("current")
_ProbeLocalVpnId_Type = Unsigned32
_ProbeLocalVpnId_Object = MibTableColumn
probeLocalVpnId = _ProbeLocalVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 1),
    _ProbeLocalVpnId_Type()
)
probeLocalVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeLocalVpnId.setStatus("current")


class _ProbeLocalAppType_Type(Integer32):
    """Custom type probeLocalAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cxp-app-type-unset", 0),
          ("cxp-app-type-app-id", 1),
          ("cxp-app-type-app-grp", 2),
          ("cxp-app-type-svc-area", 3),
          ("cxp-app-type-region", 4),
          ("cxp-app-type-custom-app-grp", 5))
    )


_ProbeLocalAppType_Type.__name__ = "Integer32"
_ProbeLocalAppType_Object = MibTableColumn
probeLocalAppType = _ProbeLocalAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 2),
    _ProbeLocalAppType_Type()
)
probeLocalAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeLocalAppType.setStatus("current")
_ProbeLocalAppId_Type = Unsigned32
_ProbeLocalAppId_Object = MibTableColumn
probeLocalAppId = _ProbeLocalAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 3),
    _ProbeLocalAppId_Type()
)
probeLocalAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeLocalAppId.setStatus("current")
_ProbeLocalSubAppId_Type = Unsigned32
_ProbeLocalSubAppId_Object = MibTableColumn
probeLocalSubAppId = _ProbeLocalSubAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 4),
    _ProbeLocalSubAppId_Type()
)
probeLocalSubAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeLocalSubAppId.setStatus("current")


class _ProbeLocalInterface_Type(String):
    """Custom type probeLocalInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ProbeLocalInterface_Type.__name__ = "String"
_ProbeLocalInterface_Object = MibTableColumn
probeLocalInterface = _ProbeLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 5),
    _ProbeLocalInterface_Type()
)
probeLocalInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeLocalInterface.setStatus("current")


class _ProbeLocalApp_Type(String):
    """Custom type probeLocalApp based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ProbeLocalApp_Type.__name__ = "String"
_ProbeLocalApp_Object = MibTableColumn
probeLocalApp = _ProbeLocalApp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 6),
    _ProbeLocalApp_Type()
)
probeLocalApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeLocalApp.setStatus("current")
_ProbeLocalLatency_Type = Unsigned32
_ProbeLocalLatency_Object = MibTableColumn
probeLocalLatency = _ProbeLocalLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 7),
    _ProbeLocalLatency_Type()
)
probeLocalLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeLocalLatency.setStatus("current")
_ProbeLocalLoss_Type = Unsigned32
_ProbeLocalLoss_Object = MibTableColumn
probeLocalLoss = _ProbeLocalLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 8),
    _ProbeLocalLoss_Type()
)
probeLocalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeLocalLoss.setStatus("current")
_ProbeGatewayTable_Object = MibTable
probeGatewayTable = _ProbeGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4)
)
if mibBuilder.loadTexts:
    probeGatewayTable.setStatus("current")
_ProbeGatewayEntry_Object = MibTableRow
probeGatewayEntry = _ProbeGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1)
)
probeGatewayEntry.setIndexNames(
    (0, "CISCO-SDWAN-PROBE-MIB", "probeGatewayVpnId"),
    (0, "CISCO-SDWAN-PROBE-MIB", "probeGatewayAppType"),
    (0, "CISCO-SDWAN-PROBE-MIB", "probeGatewayAppId"),
)
if mibBuilder.loadTexts:
    probeGatewayEntry.setStatus("current")
_ProbeGatewayVpnId_Type = Unsigned32
_ProbeGatewayVpnId_Object = MibTableColumn
probeGatewayVpnId = _ProbeGatewayVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 1),
    _ProbeGatewayVpnId_Type()
)
probeGatewayVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeGatewayVpnId.setStatus("current")


class _ProbeGatewayAppType_Type(Integer32):
    """Custom type probeGatewayAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cxp-app-type-unset", 0),
          ("cxp-app-type-app-id", 1),
          ("cxp-app-type-app-grp", 2),
          ("cxp-app-type-svc-area", 3),
          ("cxp-app-type-region", 4),
          ("cxp-app-type-custom-app-grp", 5))
    )


_ProbeGatewayAppType_Type.__name__ = "Integer32"
_ProbeGatewayAppType_Object = MibTableColumn
probeGatewayAppType = _ProbeGatewayAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 2),
    _ProbeGatewayAppType_Type()
)
probeGatewayAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeGatewayAppType.setStatus("current")
_ProbeGatewayAppId_Type = Unsigned32
_ProbeGatewayAppId_Object = MibTableColumn
probeGatewayAppId = _ProbeGatewayAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 3),
    _ProbeGatewayAppId_Type()
)
probeGatewayAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeGatewayAppId.setStatus("current")
_ProbeGatewaySubAppId_Type = Unsigned32
_ProbeGatewaySubAppId_Object = MibTableColumn
probeGatewaySubAppId = _ProbeGatewaySubAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 4),
    _ProbeGatewaySubAppId_Type()
)
probeGatewaySubAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probeGatewaySubAppId.setStatus("current")
_ProbeGatewayGwSysIp_Type = InetAddressIP
_ProbeGatewayGwSysIp_Object = MibTableColumn
probeGatewayGwSysIp = _ProbeGatewayGwSysIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 5),
    _ProbeGatewayGwSysIp_Type()
)
probeGatewayGwSysIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeGatewayGwSysIp.setStatus("current")


class _ProbeGatewayApp_Type(String):
    """Custom type probeGatewayApp based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ProbeGatewayApp_Type.__name__ = "String"
_ProbeGatewayApp_Object = MibTableColumn
probeGatewayApp = _ProbeGatewayApp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 6),
    _ProbeGatewayApp_Type()
)
probeGatewayApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeGatewayApp.setStatus("current")
_ProbeGatewayLatency_Type = Unsigned32
_ProbeGatewayLatency_Object = MibTableColumn
probeGatewayLatency = _ProbeGatewayLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 7),
    _ProbeGatewayLatency_Type()
)
probeGatewayLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeGatewayLatency.setStatus("current")
_ProbeGatewayLoss_Type = Unsigned32
_ProbeGatewayLoss_Object = MibTableColumn
probeGatewayLoss = _ProbeGatewayLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 8),
    _ProbeGatewayLoss_Type()
)
probeGatewayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeGatewayLoss.setStatus("current")


class _ProbeGatewayRemoteColor_Type(Integer32):
    """Custom type probeGatewayRemoteColor based on Integer32"""
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


_ProbeGatewayRemoteColor_Type.__name__ = "Integer32"
_ProbeGatewayRemoteColor_Object = MibTableColumn
probeGatewayRemoteColor = _ProbeGatewayRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 9),
    _ProbeGatewayRemoteColor_Type()
)
probeGatewayRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeGatewayRemoteColor.setStatus("current")


class _ProbeGatewayLocalColor_Type(Integer32):
    """Custom type probeGatewayLocalColor based on Integer32"""
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


_ProbeGatewayLocalColor_Type.__name__ = "Integer32"
_ProbeGatewayLocalColor_Object = MibTableColumn
probeGatewayLocalColor = _ProbeGatewayLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 10),
    _ProbeGatewayLocalColor_Type()
)
probeGatewayLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeGatewayLocalColor.setStatus("current")
_CiscoSdwanProbeMIBConform_ObjectIdentity = ObjectIdentity
ciscoSdwanProbeMIBConform = _CiscoSdwanProbeMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 3)
)
_CiscoSdwanProbeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSdwanProbeMIBCompliances = _CiscoSdwanProbeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 1)
)
_CiscoSdwanProbeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSdwanProbeMIBGroups = _CiscoSdwanProbeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 2)
)

# Managed Objects groups

cSdwanProbeApplicationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 2, 1)
)
cSdwanProbeApplicationsGroup.setObjects(
      *(("CISCO-SDWAN-PROBE-MIB", "probeApplicationsApp"),
        ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsExitType"),
        ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsGwSysIp"),
        ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsInterface"),
        ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsLatency"),
        ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsLoss"),
        ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsLocalColor"),
        ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsRemoteColor"))
)
if mibBuilder.loadTexts:
    cSdwanProbeApplicationsGroup.setStatus("current")

cSdwanProbeLocalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 2, 2)
)
cSdwanProbeLocalGroup.setObjects(
      *(("CISCO-SDWAN-PROBE-MIB", "probeLocalApp"),
        ("CISCO-SDWAN-PROBE-MIB", "probeLocalLatency"),
        ("CISCO-SDWAN-PROBE-MIB", "probeLocalLoss"))
)
if mibBuilder.loadTexts:
    cSdwanProbeLocalGroup.setStatus("current")

cSdwanProbeGatewayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 2, 3)
)
cSdwanProbeGatewayGroup.setObjects(
      *(("CISCO-SDWAN-PROBE-MIB", "probeGatewayApp"),
        ("CISCO-SDWAN-PROBE-MIB", "probeGatewayLatency"),
        ("CISCO-SDWAN-PROBE-MIB", "probeGatewayLoss"),
        ("CISCO-SDWAN-PROBE-MIB", "probeGatewayLocalColor"),
        ("CISCO-SDWAN-PROBE-MIB", "probeGatewayRemoteColor"))
)
if mibBuilder.loadTexts:
    cSdwanProbeGatewayGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSdwanProbeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 1, 1)
)
ciscoSdwanProbeMIBCompliance.setObjects(
      *(("CISCO-SDWAN-PROBE-MIB", "cSdwanProbeApplicationsGroup"),
        ("CISCO-SDWAN-PROBE-MIB", "cSdwanProbeLocalGroup"),
        ("CISCO-SDWAN-PROBE-MIB", "cSdwanProbeGatewayGroup"))
)
if mibBuilder.loadTexts:
    ciscoSdwanProbeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDWAN-PROBE-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
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
       "FnfMonitorEnum": FnfMonitorEnum,
       "ColorList": ColorList,
       "NotificationSeverity": NotificationSeverity,
       "VpnId": VpnId,
       "ciscoSdwanProbeMIB": ciscoSdwanProbeMIB,
       "ciscoSdwanProbeMIBObjects": ciscoSdwanProbeMIBObjects,
       "probeApplicationsTable": probeApplicationsTable,
       "probeApplicationsEntry": probeApplicationsEntry,
       "probeApplicationsVpnId": probeApplicationsVpnId,
       "probeApplicationsAppType": probeApplicationsAppType,
       "probeApplicationsAppId": probeApplicationsAppId,
       "probeApplicationsSubAppId": probeApplicationsSubAppId,
       "probeApplicationsApp": probeApplicationsApp,
       "probeApplicationsExitType": probeApplicationsExitType,
       "probeApplicationsGwSysIp": probeApplicationsGwSysIp,
       "probeApplicationsInterface": probeApplicationsInterface,
       "probeApplicationsLatency": probeApplicationsLatency,
       "probeApplicationsLoss": probeApplicationsLoss,
       "probeApplicationsRemoteColor": probeApplicationsRemoteColor,
       "probeApplicationsLocalColor": probeApplicationsLocalColor,
       "probeLocalTable": probeLocalTable,
       "probeLocalEntry": probeLocalEntry,
       "probeLocalVpnId": probeLocalVpnId,
       "probeLocalAppType": probeLocalAppType,
       "probeLocalAppId": probeLocalAppId,
       "probeLocalSubAppId": probeLocalSubAppId,
       "probeLocalInterface": probeLocalInterface,
       "probeLocalApp": probeLocalApp,
       "probeLocalLatency": probeLocalLatency,
       "probeLocalLoss": probeLocalLoss,
       "probeGatewayTable": probeGatewayTable,
       "probeGatewayEntry": probeGatewayEntry,
       "probeGatewayVpnId": probeGatewayVpnId,
       "probeGatewayAppType": probeGatewayAppType,
       "probeGatewayAppId": probeGatewayAppId,
       "probeGatewaySubAppId": probeGatewaySubAppId,
       "probeGatewayGwSysIp": probeGatewayGwSysIp,
       "probeGatewayApp": probeGatewayApp,
       "probeGatewayLatency": probeGatewayLatency,
       "probeGatewayLoss": probeGatewayLoss,
       "probeGatewayRemoteColor": probeGatewayRemoteColor,
       "probeGatewayLocalColor": probeGatewayLocalColor,
       "ciscoSdwanProbeMIBConform": ciscoSdwanProbeMIBConform,
       "ciscoSdwanProbeMIBCompliances": ciscoSdwanProbeMIBCompliances,
       "ciscoSdwanProbeMIBCompliance": ciscoSdwanProbeMIBCompliance,
       "ciscoSdwanProbeMIBGroups": ciscoSdwanProbeMIBGroups,
       "cSdwanProbeApplicationsGroup": cSdwanProbeApplicationsGroup,
       "cSdwanProbeLocalGroup": cSdwanProbeLocalGroup,
       "cSdwanProbeGatewayGroup": cSdwanProbeGatewayGroup}
)
