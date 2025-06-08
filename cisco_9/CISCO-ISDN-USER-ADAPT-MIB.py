# SNMP MIB module (CISCO-ISDN-USER-ADAPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ISDN-USER-ADAPT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:31:29 2025
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

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIsdnUserAdaptMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 442)
)
if mibBuilder.loadTexts:
    ciscoIsdnUserAdaptMIB.setRevisions(
        ("2004-09-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiusASIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CiusASPIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIsdnUserAdaptMIBNotif_ObjectIdentity = ObjectIdentity
ciscoIsdnUserAdaptMIBNotif = _CiscoIsdnUserAdaptMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 0)
)
_CiscoIsdnUserAdaptMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIsdnUserAdaptMIBObjects = _CiscoIsdnUserAdaptMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1)
)
_CiuaConfig_ObjectIdentity = ObjectIdentity
ciuaConfig = _CiuaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1)
)
_CiuaAsConfigTable_Object = MibTable
ciuaAsConfigTable = _CiuaAsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciuaAsConfigTable.setStatus("current")
_CiuaAsConfigEntry_Object = MibTableRow
ciuaAsConfigEntry = _CiuaAsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1)
)
ciuaAsConfigEntry.setIndexNames(
    (0, "CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsIndex"),
)
if mibBuilder.loadTexts:
    ciuaAsConfigEntry.setStatus("current")
_CiuaAsIndex_Type = CiusASIndex
_CiuaAsIndex_Object = MibTableColumn
ciuaAsIndex = _CiuaAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 1),
    _CiuaAsIndex_Type()
)
ciuaAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciuaAsIndex.setStatus("current")


class _CiuaAsName_Type(SnmpAdminString):
    """Custom type ciuaAsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiuaAsName_Type.__name__ = "SnmpAdminString"
_CiuaAsName_Object = MibTableColumn
ciuaAsName = _CiuaAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 2),
    _CiuaAsName_Type()
)
ciuaAsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsName.setStatus("current")


class _CiuaNumAsp_Type(Gauge32):
    """Custom type ciuaNumAsp based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CiuaNumAsp_Type.__name__ = "Gauge32"
_CiuaNumAsp_Object = MibTableColumn
ciuaNumAsp = _CiuaNumAsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 3),
    _CiuaNumAsp_Type()
)
ciuaNumAsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuaNumAsp.setStatus("current")


class _CiuaAsPrimaryIPType_Type(InetAddressType):
    """Custom type ciuaAsPrimaryIPType based on InetAddressType"""
    defaultValue = 1


_CiuaAsPrimaryIPType_Type.__name__ = "InetAddressType"
_CiuaAsPrimaryIPType_Object = MibTableColumn
ciuaAsPrimaryIPType = _CiuaAsPrimaryIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 4),
    _CiuaAsPrimaryIPType_Type()
)
ciuaAsPrimaryIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsPrimaryIPType.setStatus("current")


class _CiuaAsPrimaryIPAddress_Type(InetAddress):
    """Custom type ciuaAsPrimaryIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CiuaAsPrimaryIPAddress_Type.__name__ = "InetAddress"
_CiuaAsPrimaryIPAddress_Object = MibTableColumn
ciuaAsPrimaryIPAddress = _CiuaAsPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 5),
    _CiuaAsPrimaryIPAddress_Type()
)
ciuaAsPrimaryIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsPrimaryIPAddress.setStatus("current")


class _CiuaAsSecondaryIPType_Type(InetAddressType):
    """Custom type ciuaAsSecondaryIPType based on InetAddressType"""
    defaultValue = 1


_CiuaAsSecondaryIPType_Type.__name__ = "InetAddressType"
_CiuaAsSecondaryIPType_Object = MibTableColumn
ciuaAsSecondaryIPType = _CiuaAsSecondaryIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 6),
    _CiuaAsSecondaryIPType_Type()
)
ciuaAsSecondaryIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsSecondaryIPType.setStatus("current")


class _CiuaAsSecondaryIPAddress_Type(InetAddress):
    """Custom type ciuaAsSecondaryIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CiuaAsSecondaryIPAddress_Type.__name__ = "InetAddress"
_CiuaAsSecondaryIPAddress_Object = MibTableColumn
ciuaAsSecondaryIPAddress = _CiuaAsSecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 7),
    _CiuaAsSecondaryIPAddress_Type()
)
ciuaAsSecondaryIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsSecondaryIPAddress.setStatus("current")


class _CiuaAsSctpPort_Type(CiscoPort):
    """Custom type ciuaAsSctpPort based on CiscoPort"""
    defaultValue = 9900


_CiuaAsSctpPort_Type.__name__ = "CiscoPort"
_CiuaAsSctpPort_Object = MibTableColumn
ciuaAsSctpPort = _CiuaAsSctpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 8),
    _CiuaAsSctpPort_Type()
)
ciuaAsSctpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsSctpPort.setStatus("current")
_CiuaAsSctpStream_Type = Gauge32
_CiuaAsSctpStream_Object = MibTableColumn
ciuaAsSctpStream = _CiuaAsSctpStream_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 9),
    _CiuaAsSctpStream_Type()
)
ciuaAsSctpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuaAsSctpStream.setStatus("current")


class _CiuaAsFailoverTimer_Type(Unsigned32):
    """Custom type ciuaAsFailoverTimer based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_CiuaAsFailoverTimer_Type.__name__ = "Unsigned32"
_CiuaAsFailoverTimer_Object = MibTableColumn
ciuaAsFailoverTimer = _CiuaAsFailoverTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 10),
    _CiuaAsFailoverTimer_Type()
)
ciuaAsFailoverTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsFailoverTimer.setStatus("current")
if mibBuilder.loadTexts:
    ciuaAsFailoverTimer.setUnits("milliseconds")


class _CiuaAsSctpInitRto_Type(Unsigned32):
    """Custom type ciuaAsSctpInitRto based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 20000),
    )


_CiuaAsSctpInitRto_Type.__name__ = "Unsigned32"
_CiuaAsSctpInitRto_Object = MibTableColumn
ciuaAsSctpInitRto = _CiuaAsSctpInitRto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 11),
    _CiuaAsSctpInitRto_Type()
)
ciuaAsSctpInitRto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsSctpInitRto.setStatus("current")
if mibBuilder.loadTexts:
    ciuaAsSctpInitRto.setUnits("milliseconds")


class _CiuaAsMaxInitRetrans_Type(Unsigned32):
    """Custom type ciuaAsMaxInitRetrans based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CiuaAsMaxInitRetrans_Type.__name__ = "Unsigned32"
_CiuaAsMaxInitRetrans_Object = MibTableColumn
ciuaAsMaxInitRetrans = _CiuaAsMaxInitRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 12),
    _CiuaAsMaxInitRetrans_Type()
)
ciuaAsMaxInitRetrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsMaxInitRetrans.setStatus("current")


class _CiuaAsRestartTimer_Type(Unsigned32):
    """Custom type ciuaAsRestartTimer based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 6000),
    )


_CiuaAsRestartTimer_Type.__name__ = "Unsigned32"
_CiuaAsRestartTimer_Object = MibTableColumn
ciuaAsRestartTimer = _CiuaAsRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 13),
    _CiuaAsRestartTimer_Type()
)
ciuaAsRestartTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsRestartTimer.setStatus("current")
if mibBuilder.loadTexts:
    ciuaAsRestartTimer.setUnits("milliseconds")


class _CiuaAsState_Type(Integer32):
    """Custom type ciuaAsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("inActive", 2),
          ("active", 3),
          ("pending", 4))
    )


_CiuaAsState_Type.__name__ = "Integer32"
_CiuaAsState_Object = MibTableColumn
ciuaAsState = _CiuaAsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 14),
    _CiuaAsState_Type()
)
ciuaAsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuaAsState.setStatus("current")
_CiuaAsRowStatus_Type = RowStatus
_CiuaAsRowStatus_Object = MibTableColumn
ciuaAsRowStatus = _CiuaAsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 1, 1, 15),
    _CiuaAsRowStatus_Type()
)
ciuaAsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAsRowStatus.setStatus("current")
_CiuaAspConfigTable_Object = MibTable
ciuaAspConfigTable = _CiuaAspConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciuaAspConfigTable.setStatus("current")
_CiuaAspConfigEntry_Object = MibTableRow
ciuaAspConfigEntry = _CiuaAspConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1)
)
ciuaAspConfigEntry.setIndexNames(
    (0, "CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspIndex"),
)
if mibBuilder.loadTexts:
    ciuaAspConfigEntry.setStatus("current")
_CiuaAspIndex_Type = CiusASPIndex
_CiuaAspIndex_Object = MibTableColumn
ciuaAspIndex = _CiuaAspIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 1),
    _CiuaAspIndex_Type()
)
ciuaAspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciuaAspIndex.setStatus("current")


class _CiuaAspName_Type(SnmpAdminString):
    """Custom type ciuaAspName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiuaAspName_Type.__name__ = "SnmpAdminString"
_CiuaAspName_Object = MibTableColumn
ciuaAspName = _CiuaAspName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 2),
    _CiuaAspName_Type()
)
ciuaAspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspName.setStatus("current")
_CiuaAspAsIndex_Type = CiusASIndex
_CiuaAspAsIndex_Object = MibTableColumn
ciuaAspAsIndex = _CiuaAspAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 3),
    _CiuaAspAsIndex_Type()
)
ciuaAspAsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspAsIndex.setStatus("current")


class _CiuaAspAsName_Type(SnmpAdminString):
    """Custom type ciuaAspAsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiuaAspAsName_Type.__name__ = "SnmpAdminString"
_CiuaAspAsName_Object = MibTableColumn
ciuaAspAsName = _CiuaAspAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 4),
    _CiuaAspAsName_Type()
)
ciuaAspAsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspAsName.setStatus("current")


class _CiuaAspAssocIndex_Type(Unsigned32):
    """Custom type ciuaAspAssocIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiuaAspAssocIndex_Type.__name__ = "Unsigned32"
_CiuaAspAssocIndex_Object = MibTableColumn
ciuaAspAssocIndex = _CiuaAspAssocIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 5),
    _CiuaAspAssocIndex_Type()
)
ciuaAspAssocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuaAspAssocIndex.setStatus("current")


class _CiuaAspPrimaryIPType_Type(InetAddressType):
    """Custom type ciuaAspPrimaryIPType based on InetAddressType"""
    defaultValue = 1


_CiuaAspPrimaryIPType_Type.__name__ = "InetAddressType"
_CiuaAspPrimaryIPType_Object = MibTableColumn
ciuaAspPrimaryIPType = _CiuaAspPrimaryIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 6),
    _CiuaAspPrimaryIPType_Type()
)
ciuaAspPrimaryIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspPrimaryIPType.setStatus("current")


class _CiuaAspPrimaryIPAddress_Type(InetAddress):
    """Custom type ciuaAspPrimaryIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CiuaAspPrimaryIPAddress_Type.__name__ = "InetAddress"
_CiuaAspPrimaryIPAddress_Object = MibTableColumn
ciuaAspPrimaryIPAddress = _CiuaAspPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 7),
    _CiuaAspPrimaryIPAddress_Type()
)
ciuaAspPrimaryIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspPrimaryIPAddress.setStatus("current")


class _CiuaAspSecondaryIPType_Type(InetAddressType):
    """Custom type ciuaAspSecondaryIPType based on InetAddressType"""
    defaultValue = 1


_CiuaAspSecondaryIPType_Type.__name__ = "InetAddressType"
_CiuaAspSecondaryIPType_Object = MibTableColumn
ciuaAspSecondaryIPType = _CiuaAspSecondaryIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 8),
    _CiuaAspSecondaryIPType_Type()
)
ciuaAspSecondaryIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspSecondaryIPType.setStatus("current")


class _CiuaAspSecondaryIPAddress_Type(InetAddress):
    """Custom type ciuaAspSecondaryIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CiuaAspSecondaryIPAddress_Type.__name__ = "InetAddress"
_CiuaAspSecondaryIPAddress_Object = MibTableColumn
ciuaAspSecondaryIPAddress = _CiuaAspSecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 9),
    _CiuaAspSecondaryIPAddress_Type()
)
ciuaAspSecondaryIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspSecondaryIPAddress.setStatus("current")


class _CiuaAspSctpPort_Type(CiscoPort):
    """Custom type ciuaAspSctpPort based on CiscoPort"""
    defaultValue = 9900


_CiuaAspSctpPort_Type.__name__ = "CiscoPort"
_CiuaAspSctpPort_Object = MibTableColumn
ciuaAspSctpPort = _CiuaAspSctpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 10),
    _CiuaAspSctpPort_Type()
)
ciuaAspSctpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspSctpPort.setStatus("current")


class _CiuaAspSctpMaxAssocRetrans_Type(Unsigned32):
    """Custom type ciuaAspSctpMaxAssocRetrans based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_CiuaAspSctpMaxAssocRetrans_Type.__name__ = "Unsigned32"
_CiuaAspSctpMaxAssocRetrans_Object = MibTableColumn
ciuaAspSctpMaxAssocRetrans = _CiuaAspSctpMaxAssocRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 11),
    _CiuaAspSctpMaxAssocRetrans_Type()
)
ciuaAspSctpMaxAssocRetrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspSctpMaxAssocRetrans.setStatus("current")


class _CiuaAspSctpMaxRto_Type(Unsigned32):
    """Custom type ciuaAspSctpMaxRto based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 60000),
    )


_CiuaAspSctpMaxRto_Type.__name__ = "Unsigned32"
_CiuaAspSctpMaxRto_Object = MibTableColumn
ciuaAspSctpMaxRto = _CiuaAspSctpMaxRto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 12),
    _CiuaAspSctpMaxRto_Type()
)
ciuaAspSctpMaxRto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspSctpMaxRto.setStatus("current")
if mibBuilder.loadTexts:
    ciuaAspSctpMaxRto.setUnits("milliseconds")


class _CiuaAspState_Type(Integer32):
    """Custom type ciuaAspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("inActive", 2),
          ("active", 3))
    )


_CiuaAspState_Type.__name__ = "Integer32"
_CiuaAspState_Object = MibTableColumn
ciuaAspState = _CiuaAspState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 13),
    _CiuaAspState_Type()
)
ciuaAspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuaAspState.setStatus("current")
_CiuaAspRowStatus_Type = RowStatus
_CiuaAspRowStatus_Object = MibTableColumn
ciuaAspRowStatus = _CiuaAspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 2, 1, 14),
    _CiuaAspRowStatus_Type()
)
ciuaAspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuaAspRowStatus.setStatus("current")
_CiuaAspIPConfigTable_Object = MibTable
ciuaAspIPConfigTable = _CiuaAspIPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ciuaAspIPConfigTable.setStatus("current")
_CiuaAspIPConfigEntry_Object = MibTableRow
ciuaAspIPConfigEntry = _CiuaAspIPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 3, 1)
)
ciuaAspIPConfigEntry.setIndexNames(
    (0, "CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspIndex"),
    (0, "CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspIpType"),
    (0, "CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspIpAddress"),
)
if mibBuilder.loadTexts:
    ciuaAspIPConfigEntry.setStatus("current")
_CiuaAspIpType_Type = InetAddressType
_CiuaAspIpType_Object = MibTableColumn
ciuaAspIpType = _CiuaAspIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 3, 1, 1),
    _CiuaAspIpType_Type()
)
ciuaAspIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciuaAspIpType.setStatus("current")


class _CiuaAspIpAddress_Type(InetAddress):
    """Custom type ciuaAspIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CiuaAspIpAddress_Type.__name__ = "InetAddress"
_CiuaAspIpAddress_Object = MibTableColumn
ciuaAspIpAddress = _CiuaAspIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 3, 1, 2),
    _CiuaAspIpAddress_Type()
)
ciuaAspIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciuaAspIpAddress.setStatus("current")


class _CiuaAspIPAspName_Type(SnmpAdminString):
    """Custom type ciuaAspIPAspName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiuaAspIPAspName_Type.__name__ = "SnmpAdminString"
_CiuaAspIPAspName_Object = MibTableColumn
ciuaAspIPAspName = _CiuaAspIPAspName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 3, 1, 3),
    _CiuaAspIPAspName_Type()
)
ciuaAspIPAspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuaAspIPAspName.setStatus("current")


class _CiuaAspSctpIPPrecedence_Type(Integer32):
    """Custom type ciuaAspSctpIPPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_CiuaAspSctpIPPrecedence_Type.__name__ = "Integer32"
_CiuaAspSctpIPPrecedence_Object = MibTableColumn
ciuaAspSctpIPPrecedence = _CiuaAspSctpIPPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 3, 1, 4),
    _CiuaAspSctpIPPrecedence_Type()
)
ciuaAspSctpIPPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuaAspSctpIPPrecedence.setStatus("current")


class _CiuaAspSctpIPKeepalive_Type(Unsigned32):
    """Custom type ciuaAspSctpIPKeepalive based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )


_CiuaAspSctpIPKeepalive_Type.__name__ = "Unsigned32"
_CiuaAspSctpIPKeepalive_Object = MibTableColumn
ciuaAspSctpIPKeepalive = _CiuaAspSctpIPKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 3, 1, 5),
    _CiuaAspSctpIPKeepalive_Type()
)
ciuaAspSctpIPKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuaAspSctpIPKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    ciuaAspSctpIPKeepalive.setUnits("milliseconds")


class _CiuaAspSctpIPPathRetrans_Type(Unsigned32):
    """Custom type ciuaAspSctpIPPathRetrans based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_CiuaAspSctpIPPathRetrans_Type.__name__ = "Unsigned32"
_CiuaAspSctpIPPathRetrans_Object = MibTableColumn
ciuaAspSctpIPPathRetrans = _CiuaAspSctpIPPathRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 3, 1, 6),
    _CiuaAspSctpIPPathRetrans_Type()
)
ciuaAspSctpIPPathRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuaAspSctpIPPathRetrans.setStatus("current")


class _CiuaAspSctpIPHBFlag_Type(Integer32):
    """Custom type ciuaAspSctpIPHBFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CiuaAspSctpIPHBFlag_Type.__name__ = "Integer32"
_CiuaAspSctpIPHBFlag_Object = MibTableColumn
ciuaAspSctpIPHBFlag = _CiuaAspSctpIPHBFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 1, 1, 3, 1, 7),
    _CiuaAspSctpIPHBFlag_Type()
)
ciuaAspSctpIPHBFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuaAspSctpIPHBFlag.setStatus("current")
_CiscoIsdnUserAdaptMIBConform_ObjectIdentity = ObjectIdentity
ciscoIsdnUserAdaptMIBConform = _CiscoIsdnUserAdaptMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 2)
)
_CiscoIsdnUserAdaptMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIsdnUserAdaptMIBCompliances = _CiscoIsdnUserAdaptMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 2, 1)
)
_CiscoIsdnUserAdaptMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIsdnUserAdaptMIBGroups = _CiscoIsdnUserAdaptMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 2, 2)
)

# Managed Objects groups

ciuaAsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 2, 2, 1)
)
ciuaAsConfigGroup.setObjects(
      *(("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsName"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaNumAsp"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsPrimaryIPType"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsPrimaryIPAddress"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsSecondaryIPType"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsSecondaryIPAddress"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsSctpPort"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsSctpStream"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsFailoverTimer"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsSctpInitRto"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsMaxInitRetrans"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsRestartTimer"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsState"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsRowStatus"))
)
if mibBuilder.loadTexts:
    ciuaAsConfigGroup.setStatus("current")

ciuaAspConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 2, 2, 2)
)
ciuaAspConfigGroup.setObjects(
      *(("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspName"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspAsIndex"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspAsName"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspAssocIndex"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspPrimaryIPType"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspPrimaryIPAddress"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspSecondaryIPType"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspSecondaryIPAddress"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspSctpPort"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspSctpMaxAssocRetrans"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspSctpMaxRto"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspState"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspRowStatus"))
)
if mibBuilder.loadTexts:
    ciuaAspConfigGroup.setStatus("current")

ciuaAspIPConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 2, 2, 3)
)
ciuaAspIPConfigGroup.setObjects(
      *(("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspIPAspName"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspSctpIPPrecedence"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspSctpIPKeepalive"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspSctpIPPathRetrans"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspSctpIPHBFlag"))
)
if mibBuilder.loadTexts:
    ciuaAspIPConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIsdnUserAdaptMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 442, 2, 1, 1)
)
ciscoIsdnUserAdaptMIBCompliance.setObjects(
      *(("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAsConfigGroup"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspConfigGroup"),
        ("CISCO-ISDN-USER-ADAPT-MIB", "ciuaAspIPConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoIsdnUserAdaptMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ISDN-USER-ADAPT-MIB",
    **{"CiusASIndex": CiusASIndex,
       "CiusASPIndex": CiusASPIndex,
       "ciscoIsdnUserAdaptMIB": ciscoIsdnUserAdaptMIB,
       "ciscoIsdnUserAdaptMIBNotif": ciscoIsdnUserAdaptMIBNotif,
       "ciscoIsdnUserAdaptMIBObjects": ciscoIsdnUserAdaptMIBObjects,
       "ciuaConfig": ciuaConfig,
       "ciuaAsConfigTable": ciuaAsConfigTable,
       "ciuaAsConfigEntry": ciuaAsConfigEntry,
       "ciuaAsIndex": ciuaAsIndex,
       "ciuaAsName": ciuaAsName,
       "ciuaNumAsp": ciuaNumAsp,
       "ciuaAsPrimaryIPType": ciuaAsPrimaryIPType,
       "ciuaAsPrimaryIPAddress": ciuaAsPrimaryIPAddress,
       "ciuaAsSecondaryIPType": ciuaAsSecondaryIPType,
       "ciuaAsSecondaryIPAddress": ciuaAsSecondaryIPAddress,
       "ciuaAsSctpPort": ciuaAsSctpPort,
       "ciuaAsSctpStream": ciuaAsSctpStream,
       "ciuaAsFailoverTimer": ciuaAsFailoverTimer,
       "ciuaAsSctpInitRto": ciuaAsSctpInitRto,
       "ciuaAsMaxInitRetrans": ciuaAsMaxInitRetrans,
       "ciuaAsRestartTimer": ciuaAsRestartTimer,
       "ciuaAsState": ciuaAsState,
       "ciuaAsRowStatus": ciuaAsRowStatus,
       "ciuaAspConfigTable": ciuaAspConfigTable,
       "ciuaAspConfigEntry": ciuaAspConfigEntry,
       "ciuaAspIndex": ciuaAspIndex,
       "ciuaAspName": ciuaAspName,
       "ciuaAspAsIndex": ciuaAspAsIndex,
       "ciuaAspAsName": ciuaAspAsName,
       "ciuaAspAssocIndex": ciuaAspAssocIndex,
       "ciuaAspPrimaryIPType": ciuaAspPrimaryIPType,
       "ciuaAspPrimaryIPAddress": ciuaAspPrimaryIPAddress,
       "ciuaAspSecondaryIPType": ciuaAspSecondaryIPType,
       "ciuaAspSecondaryIPAddress": ciuaAspSecondaryIPAddress,
       "ciuaAspSctpPort": ciuaAspSctpPort,
       "ciuaAspSctpMaxAssocRetrans": ciuaAspSctpMaxAssocRetrans,
       "ciuaAspSctpMaxRto": ciuaAspSctpMaxRto,
       "ciuaAspState": ciuaAspState,
       "ciuaAspRowStatus": ciuaAspRowStatus,
       "ciuaAspIPConfigTable": ciuaAspIPConfigTable,
       "ciuaAspIPConfigEntry": ciuaAspIPConfigEntry,
       "ciuaAspIpType": ciuaAspIpType,
       "ciuaAspIpAddress": ciuaAspIpAddress,
       "ciuaAspIPAspName": ciuaAspIPAspName,
       "ciuaAspSctpIPPrecedence": ciuaAspSctpIPPrecedence,
       "ciuaAspSctpIPKeepalive": ciuaAspSctpIPKeepalive,
       "ciuaAspSctpIPPathRetrans": ciuaAspSctpIPPathRetrans,
       "ciuaAspSctpIPHBFlag": ciuaAspSctpIPHBFlag,
       "ciscoIsdnUserAdaptMIBConform": ciscoIsdnUserAdaptMIBConform,
       "ciscoIsdnUserAdaptMIBCompliances": ciscoIsdnUserAdaptMIBCompliances,
       "ciscoIsdnUserAdaptMIBCompliance": ciscoIsdnUserAdaptMIBCompliance,
       "ciscoIsdnUserAdaptMIBGroups": ciscoIsdnUserAdaptMIBGroups,
       "ciuaAsConfigGroup": ciuaAsConfigGroup,
       "ciuaAspConfigGroup": ciuaAspConfigGroup,
       "ciuaAspIPConfigGroup": ciuaAspIPConfigGroup}
)
