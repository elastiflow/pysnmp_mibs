# SNMP MIB module (TROPIC-GMPLS-CPIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-GMPLS-CPIF-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:18 2025
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

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

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

(tnGmplsMIBModules,
 tnGmplsObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnGmplsMIBModules",
    "tnGmplsObjs")


# MODULE-IDENTITY

tnGmplsCpifMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tnGmplsCpifMibModule.setRevisions(
        ("2013-06-27 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnGmplsCpifMIB_ObjectIdentity = ObjectIdentity
tnGmplsCpifMIB = _TnGmplsCpifMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1)
)
_TnGmplsCpifObjs_ObjectIdentity = ObjectIdentity
tnGmplsCpifObjs = _TnGmplsCpifObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1)
)
_TnGmplsCpifAttributeTotal_Type = Integer32
_TnGmplsCpifAttributeTotal_Object = MibScalar
tnGmplsCpifAttributeTotal = _TnGmplsCpifAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 1),
    _TnGmplsCpifAttributeTotal_Type()
)
tnGmplsCpifAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsCpifAttributeTotal.setStatus("current")
_TnGmplsCPNbrTable_Object = MibTable
tnGmplsCPNbrTable = _TnGmplsCPNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnGmplsCPNbrTable.setStatus("current")
_TnGmplsCPNbrEntry_Object = MibTableRow
tnGmplsCPNbrEntry = _TnGmplsCPNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1)
)
tnGmplsCPNbrEntry.setIndexNames(
    (0, "TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrIfId"),
)
if mibBuilder.loadTexts:
    tnGmplsCPNbrEntry.setStatus("current")
_TnGmplsCPNbrIfId_Type = Unsigned32
_TnGmplsCPNbrIfId_Object = MibTableColumn
tnGmplsCPNbrIfId = _TnGmplsCPNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 1),
    _TnGmplsCPNbrIfId_Type()
)
tnGmplsCPNbrIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsCPNbrIfId.setStatus("current")
_TnGmplsCPNbrIfName_Type = DisplayString
_TnGmplsCPNbrIfName_Object = MibTableColumn
tnGmplsCPNbrIfName = _TnGmplsCPNbrIfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 2),
    _TnGmplsCPNbrIfName_Type()
)
tnGmplsCPNbrIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsCPNbrIfName.setStatus("current")
_TnGmplsCPNbrAddrType_Type = InetAddressType
_TnGmplsCPNbrAddrType_Object = MibTableColumn
tnGmplsCPNbrAddrType = _TnGmplsCPNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 3),
    _TnGmplsCPNbrAddrType_Type()
)
tnGmplsCPNbrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsCPNbrAddrType.setStatus("current")
_TnGmplsCPNbrRemoteRouterAddr_Type = InetAddress
_TnGmplsCPNbrRemoteRouterAddr_Object = MibTableColumn
tnGmplsCPNbrRemoteRouterAddr = _TnGmplsCPNbrRemoteRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 4),
    _TnGmplsCPNbrRemoteRouterAddr_Type()
)
tnGmplsCPNbrRemoteRouterAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsCPNbrRemoteRouterAddr.setStatus("current")


class _TnGmplsCPNbrEncaps_Type(Integer32):
    """Custom type tnGmplsCPNbrEncaps based on Integer32"""
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
        *(("none", 1),
          ("ipinip", 2),
          ("gre", 3))
    )


_TnGmplsCPNbrEncaps_Type.__name__ = "Integer32"
_TnGmplsCPNbrEncaps_Object = MibTableColumn
tnGmplsCPNbrEncaps = _TnGmplsCPNbrEncaps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 5),
    _TnGmplsCPNbrEncaps_Type()
)
tnGmplsCPNbrEncaps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsCPNbrEncaps.setStatus("current")
_TnGmplsCPNbrRemoteTEP_Type = InetAddress
_TnGmplsCPNbrRemoteTEP_Object = MibTableColumn
tnGmplsCPNbrRemoteTEP = _TnGmplsCPNbrRemoteTEP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 6),
    _TnGmplsCPNbrRemoteTEP_Type()
)
tnGmplsCPNbrRemoteTEP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsCPNbrRemoteTEP.setStatus("current")
_TnGmplsCPNbrOspfArea_Type = IpAddress
_TnGmplsCPNbrOspfArea_Object = MibTableColumn
tnGmplsCPNbrOspfArea = _TnGmplsCPNbrOspfArea_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 7),
    _TnGmplsCPNbrOspfArea_Type()
)
tnGmplsCPNbrOspfArea.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsCPNbrOspfArea.setStatus("current")


class _TnGmplsCPNbrAdminStatus_Type(Integer32):
    """Custom type tnGmplsCPNbrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_TnGmplsCPNbrAdminStatus_Type.__name__ = "Integer32"
_TnGmplsCPNbrAdminStatus_Object = MibTableColumn
tnGmplsCPNbrAdminStatus = _TnGmplsCPNbrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 8),
    _TnGmplsCPNbrAdminStatus_Type()
)
tnGmplsCPNbrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsCPNbrAdminStatus.setStatus("current")
_TnGmplsCPNbrRemoteCPNodeId_Type = InetAddressIPv4
_TnGmplsCPNbrRemoteCPNodeId_Object = MibTableColumn
tnGmplsCPNbrRemoteCPNodeId = _TnGmplsCPNbrRemoteCPNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 9),
    _TnGmplsCPNbrRemoteCPNodeId_Type()
)
tnGmplsCPNbrRemoteCPNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsCPNbrRemoteCPNodeId.setStatus("current")
_TnGmplsCPNbrRowStatus_Type = RowStatus
_TnGmplsCPNbrRowStatus_Object = MibTableColumn
tnGmplsCPNbrRowStatus = _TnGmplsCPNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 2, 1, 10),
    _TnGmplsCPNbrRowStatus_Type()
)
tnGmplsCPNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsCPNbrRowStatus.setStatus("current")
_TnGmplsRsvpIfTable_Object = MibTable
tnGmplsRsvpIfTable = _TnGmplsRsvpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnGmplsRsvpIfTable.setStatus("current")
_TnGmplsRsvpIfEntry_Object = MibTableRow
tnGmplsRsvpIfEntry = _TnGmplsRsvpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3, 1)
)
tnGmplsRsvpIfEntry.setIndexNames(
    (0, "TROPIC-GMPLS-CPIF-MIB", "tnGmplsRsvpIfId"),
)
if mibBuilder.loadTexts:
    tnGmplsRsvpIfEntry.setStatus("current")
_TnGmplsRsvpIfId_Type = Unsigned32
_TnGmplsRsvpIfId_Object = MibTableColumn
tnGmplsRsvpIfId = _TnGmplsRsvpIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3, 1, 1),
    _TnGmplsRsvpIfId_Type()
)
tnGmplsRsvpIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsRsvpIfId.setStatus("current")
_TnGmplsRsvpIfName_Type = DisplayString
_TnGmplsRsvpIfName_Object = MibTableColumn
tnGmplsRsvpIfName = _TnGmplsRsvpIfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3, 1, 2),
    _TnGmplsRsvpIfName_Type()
)
tnGmplsRsvpIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsRsvpIfName.setStatus("current")


class _TnGmplsRsvpIfType_Type(Integer32):
    """Custom type tnGmplsRsvpIfType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uni", 1),
          ("nni", 2))
    )


_TnGmplsRsvpIfType_Type.__name__ = "Integer32"
_TnGmplsRsvpIfType_Object = MibTableColumn
tnGmplsRsvpIfType = _TnGmplsRsvpIfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3, 1, 3),
    _TnGmplsRsvpIfType_Type()
)
tnGmplsRsvpIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsRsvpIfType.setStatus("current")


class _TnGmplsRsvpIfEncaps_Type(Integer32):
    """Custom type tnGmplsRsvpIfEncaps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ipminimal", 2))
    )


_TnGmplsRsvpIfEncaps_Type.__name__ = "Integer32"
_TnGmplsRsvpIfEncaps_Object = MibTableColumn
tnGmplsRsvpIfEncaps = _TnGmplsRsvpIfEncaps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3, 1, 4),
    _TnGmplsRsvpIfEncaps_Type()
)
tnGmplsRsvpIfEncaps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsRsvpIfEncaps.setStatus("current")
_TnGmplsRsvpIfCPNbr_Type = Unsigned32
_TnGmplsRsvpIfCPNbr_Object = MibTableColumn
tnGmplsRsvpIfCPNbr = _TnGmplsRsvpIfCPNbr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3, 1, 5),
    _TnGmplsRsvpIfCPNbr_Type()
)
tnGmplsRsvpIfCPNbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsRsvpIfCPNbr.setStatus("current")


class _TnGmplsRsvpIfAdminStatus_Type(Integer32):
    """Custom type tnGmplsRsvpIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_TnGmplsRsvpIfAdminStatus_Type.__name__ = "Integer32"
_TnGmplsRsvpIfAdminStatus_Object = MibTableColumn
tnGmplsRsvpIfAdminStatus = _TnGmplsRsvpIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3, 1, 6),
    _TnGmplsRsvpIfAdminStatus_Type()
)
tnGmplsRsvpIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsRsvpIfAdminStatus.setStatus("current")


class _TnGmplsRsvpIfOpState_Type(Integer32):
    """Custom type tnGmplsRsvpIfOpState based on Integer32"""
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
          ("up", 2),
          ("degraded", 3))
    )


_TnGmplsRsvpIfOpState_Type.__name__ = "Integer32"
_TnGmplsRsvpIfOpState_Object = MibTableColumn
tnGmplsRsvpIfOpState = _TnGmplsRsvpIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3, 1, 7),
    _TnGmplsRsvpIfOpState_Type()
)
tnGmplsRsvpIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsRsvpIfOpState.setStatus("current")
_TnGmplsRsvpIfRowStatus_Type = RowStatus
_TnGmplsRsvpIfRowStatus_Object = MibTableColumn
tnGmplsRsvpIfRowStatus = _TnGmplsRsvpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 3, 1, 8),
    _TnGmplsRsvpIfRowStatus_Type()
)
tnGmplsRsvpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsRsvpIfRowStatus.setStatus("current")
_TnGmplsDprIfTable_Object = MibTable
tnGmplsDprIfTable = _TnGmplsDprIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tnGmplsDprIfTable.setStatus("current")
_TnGmplsDprIfEntry_Object = MibTableRow
tnGmplsDprIfEntry = _TnGmplsDprIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1)
)
tnGmplsDprIfEntry.setIndexNames(
    (0, "TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprIfId"),
)
if mibBuilder.loadTexts:
    tnGmplsDprIfEntry.setStatus("current")
_TnGmplsDprIfId_Type = Unsigned32
_TnGmplsDprIfId_Object = MibTableColumn
tnGmplsDprIfId = _TnGmplsDprIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1, 1),
    _TnGmplsDprIfId_Type()
)
tnGmplsDprIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsDprIfId.setStatus("current")
_TnGmplsDprIfName_Type = DisplayString
_TnGmplsDprIfName_Object = MibTableColumn
tnGmplsDprIfName = _TnGmplsDprIfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1, 2),
    _TnGmplsDprIfName_Type()
)
tnGmplsDprIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDprIfName.setStatus("current")


class _TnGmplsDprIfType_Type(Integer32):
    """Custom type tnGmplsDprIfType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("nni", 1)
    )


_TnGmplsDprIfType_Type.__name__ = "Integer32"
_TnGmplsDprIfType_Object = MibTableColumn
tnGmplsDprIfType = _TnGmplsDprIfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1, 3),
    _TnGmplsDprIfType_Type()
)
tnGmplsDprIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDprIfType.setStatus("current")


class _TnGmplsDprIfEncaps_Type(Integer32):
    """Custom type tnGmplsDprIfEncaps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipminimal", 1)
    )


_TnGmplsDprIfEncaps_Type.__name__ = "Integer32"
_TnGmplsDprIfEncaps_Object = MibTableColumn
tnGmplsDprIfEncaps = _TnGmplsDprIfEncaps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1, 4),
    _TnGmplsDprIfEncaps_Type()
)
tnGmplsDprIfEncaps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDprIfEncaps.setStatus("current")
_TnGmplsDprIfCPNbr_Type = Unsigned32
_TnGmplsDprIfCPNbr_Object = MibTableColumn
tnGmplsDprIfCPNbr = _TnGmplsDprIfCPNbr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1, 5),
    _TnGmplsDprIfCPNbr_Type()
)
tnGmplsDprIfCPNbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDprIfCPNbr.setStatus("current")


class _TnGmplsDprIfAdminStatus_Type(Integer32):
    """Custom type tnGmplsDprIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_TnGmplsDprIfAdminStatus_Type.__name__ = "Integer32"
_TnGmplsDprIfAdminStatus_Object = MibTableColumn
tnGmplsDprIfAdminStatus = _TnGmplsDprIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1, 6),
    _TnGmplsDprIfAdminStatus_Type()
)
tnGmplsDprIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDprIfAdminStatus.setStatus("current")


class _TnGmplsDprIfOpState_Type(Integer32):
    """Custom type tnGmplsDprIfOpState based on Integer32"""
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
          ("up", 2),
          ("degraded", 3))
    )


_TnGmplsDprIfOpState_Type.__name__ = "Integer32"
_TnGmplsDprIfOpState_Object = MibTableColumn
tnGmplsDprIfOpState = _TnGmplsDprIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1, 7),
    _TnGmplsDprIfOpState_Type()
)
tnGmplsDprIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsDprIfOpState.setStatus("current")
_TnGmplsDprIfNVMismatch_Type = TruthValue
_TnGmplsDprIfNVMismatch_Object = MibTableColumn
tnGmplsDprIfNVMismatch = _TnGmplsDprIfNVMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1, 8),
    _TnGmplsDprIfNVMismatch_Type()
)
tnGmplsDprIfNVMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsDprIfNVMismatch.setStatus("current")
_TnGmplsDprIfRowStatus_Type = RowStatus
_TnGmplsDprIfRowStatus_Object = MibTableColumn
tnGmplsDprIfRowStatus = _TnGmplsDprIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 4, 1, 9),
    _TnGmplsDprIfRowStatus_Type()
)
tnGmplsDprIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDprIfRowStatus.setStatus("current")
_TnGmplsLmpIfTable_Object = MibTable
tnGmplsLmpIfTable = _TnGmplsLmpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tnGmplsLmpIfTable.setStatus("current")
_TnGmplsLmpIfEntry_Object = MibTableRow
tnGmplsLmpIfEntry = _TnGmplsLmpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1)
)
tnGmplsLmpIfEntry.setIndexNames(
    (0, "TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfId"),
)
if mibBuilder.loadTexts:
    tnGmplsLmpIfEntry.setStatus("current")
_TnGmplsLmpIfId_Type = Unsigned32
_TnGmplsLmpIfId_Object = MibTableColumn
tnGmplsLmpIfId = _TnGmplsLmpIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 1),
    _TnGmplsLmpIfId_Type()
)
tnGmplsLmpIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLmpIfId.setStatus("current")
_TnGmplsLmpIfName_Type = DisplayString
_TnGmplsLmpIfName_Object = MibTableColumn
tnGmplsLmpIfName = _TnGmplsLmpIfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 2),
    _TnGmplsLmpIfName_Type()
)
tnGmplsLmpIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLmpIfName.setStatus("current")
_TnGmplsLmpIfCPNbr_Type = Unsigned32
_TnGmplsLmpIfCPNbr_Object = MibTableColumn
tnGmplsLmpIfCPNbr = _TnGmplsLmpIfCPNbr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 3),
    _TnGmplsLmpIfCPNbr_Type()
)
tnGmplsLmpIfCPNbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLmpIfCPNbr.setStatus("current")
_TnGmplsLmpIfHelloEnabled_Type = TruthValue
_TnGmplsLmpIfHelloEnabled_Object = MibTableColumn
tnGmplsLmpIfHelloEnabled = _TnGmplsLmpIfHelloEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 4),
    _TnGmplsLmpIfHelloEnabled_Type()
)
tnGmplsLmpIfHelloEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLmpIfHelloEnabled.setStatus("current")
_TnGmplsLmpIfLinkPropCorrEnabled_Type = TruthValue
_TnGmplsLmpIfLinkPropCorrEnabled_Object = MibTableColumn
tnGmplsLmpIfLinkPropCorrEnabled = _TnGmplsLmpIfLinkPropCorrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 5),
    _TnGmplsLmpIfLinkPropCorrEnabled_Type()
)
tnGmplsLmpIfLinkPropCorrEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLmpIfLinkPropCorrEnabled.setStatus("current")
_TnGmplsLmpIfTraceMonEnabled_Type = TruthValue
_TnGmplsLmpIfTraceMonEnabled_Object = MibTableColumn
tnGmplsLmpIfTraceMonEnabled = _TnGmplsLmpIfTraceMonEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 6),
    _TnGmplsLmpIfTraceMonEnabled_Type()
)
tnGmplsLmpIfTraceMonEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLmpIfTraceMonEnabled.setStatus("current")
_TnGmplsLmpIfEndPointDiscEnabled_Type = TruthValue
_TnGmplsLmpIfEndPointDiscEnabled_Object = MibTableColumn
tnGmplsLmpIfEndPointDiscEnabled = _TnGmplsLmpIfEndPointDiscEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 7),
    _TnGmplsLmpIfEndPointDiscEnabled_Type()
)
tnGmplsLmpIfEndPointDiscEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLmpIfEndPointDiscEnabled.setStatus("current")


class _TnGmplsLmpIfAdminStatus_Type(Integer32):
    """Custom type tnGmplsLmpIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_TnGmplsLmpIfAdminStatus_Type.__name__ = "Integer32"
_TnGmplsLmpIfAdminStatus_Object = MibTableColumn
tnGmplsLmpIfAdminStatus = _TnGmplsLmpIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 8),
    _TnGmplsLmpIfAdminStatus_Type()
)
tnGmplsLmpIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLmpIfAdminStatus.setStatus("current")


class _TnGmplsLmpIfOpState_Type(Integer32):
    """Custom type tnGmplsLmpIfOpState based on Integer32"""
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
          ("up", 2),
          ("degraded", 3))
    )


_TnGmplsLmpIfOpState_Type.__name__ = "Integer32"
_TnGmplsLmpIfOpState_Object = MibTableColumn
tnGmplsLmpIfOpState = _TnGmplsLmpIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 9),
    _TnGmplsLmpIfOpState_Type()
)
tnGmplsLmpIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLmpIfOpState.setStatus("current")
_TnGmplsLmpIfRowStatus_Type = RowStatus
_TnGmplsLmpIfRowStatus_Object = MibTableColumn
tnGmplsLmpIfRowStatus = _TnGmplsLmpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 1, 5, 1, 10),
    _TnGmplsLmpIfRowStatus_Type()
)
tnGmplsLmpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLmpIfRowStatus.setStatus("current")
_TnGmplsCpifConf_ObjectIdentity = ObjectIdentity
tnGmplsCpifConf = _TnGmplsCpifConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 3)
)
_TnGmplsCpifGroups_ObjectIdentity = ObjectIdentity
tnGmplsCpifGroups = _TnGmplsCpifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 3, 1)
)
_TnGmplsCpifCompliances_ObjectIdentity = ObjectIdentity
tnGmplsCpifCompliances = _TnGmplsCpifCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 3, 2)
)

# Managed Objects groups

tnGmplsCpifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 3, 1, 1)
)
tnGmplsCpifObjsGroup.setObjects(
    ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCpifAttributeTotal")
)
if mibBuilder.loadTexts:
    tnGmplsCpifObjsGroup.setStatus("current")

tnGmplsCPNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 3, 1, 2)
)
tnGmplsCPNbrGroup.setObjects(
      *(("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrIfName"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrAddrType"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrRemoteRouterAddr"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrEncaps"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrRemoteTEP"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrOspfArea"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrAdminStatus"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrRemoteCPNodeId"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsCPNbrGroup.setStatus("current")

tnGmplsRsvpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 3, 1, 3)
)
tnGmplsRsvpGroup.setObjects(
      *(("TROPIC-GMPLS-CPIF-MIB", "tnGmplsRsvpIfName"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsRsvpIfType"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsRsvpIfEncaps"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsRsvpIfCPNbr"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsRsvpIfAdminStatus"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsRsvpIfOpState"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsRsvpIfRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsRsvpGroup.setStatus("current")

tnGmplsDprGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 3, 1, 4)
)
tnGmplsDprGroup.setObjects(
      *(("TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprIfName"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprIfType"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprIfEncaps"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprIfCPNbr"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprIfAdminStatus"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprIfOpState"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprIfNVMismatch"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprIfRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsDprGroup.setStatus("current")

tnGmplsLmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 3, 1, 5)
)
tnGmplsLmpGroup.setObjects(
      *(("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfName"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfCPNbr"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfHelloEnabled"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfLinkPropCorrEnabled"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfTraceMonEnabled"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfEndPointDiscEnabled"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfAdminStatus"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfOpState"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpIfRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsLmpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnGmplsCpifCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 1, 3, 2, 1)
)
tnGmplsCpifCompliance.setObjects(
      *(("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCpifObjsGroup"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsCPNbrGroup"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsRsvpGroup"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsDprGroup"),
        ("TROPIC-GMPLS-CPIF-MIB", "tnGmplsLmpGroup"))
)
if mibBuilder.loadTexts:
    tnGmplsCpifCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-GMPLS-CPIF-MIB",
    **{"tnGmplsCpifMibModule": tnGmplsCpifMibModule,
       "tnGmplsCpifMIB": tnGmplsCpifMIB,
       "tnGmplsCpifObjs": tnGmplsCpifObjs,
       "tnGmplsCpifAttributeTotal": tnGmplsCpifAttributeTotal,
       "tnGmplsCPNbrTable": tnGmplsCPNbrTable,
       "tnGmplsCPNbrEntry": tnGmplsCPNbrEntry,
       "tnGmplsCPNbrIfId": tnGmplsCPNbrIfId,
       "tnGmplsCPNbrIfName": tnGmplsCPNbrIfName,
       "tnGmplsCPNbrAddrType": tnGmplsCPNbrAddrType,
       "tnGmplsCPNbrRemoteRouterAddr": tnGmplsCPNbrRemoteRouterAddr,
       "tnGmplsCPNbrEncaps": tnGmplsCPNbrEncaps,
       "tnGmplsCPNbrRemoteTEP": tnGmplsCPNbrRemoteTEP,
       "tnGmplsCPNbrOspfArea": tnGmplsCPNbrOspfArea,
       "tnGmplsCPNbrAdminStatus": tnGmplsCPNbrAdminStatus,
       "tnGmplsCPNbrRemoteCPNodeId": tnGmplsCPNbrRemoteCPNodeId,
       "tnGmplsCPNbrRowStatus": tnGmplsCPNbrRowStatus,
       "tnGmplsRsvpIfTable": tnGmplsRsvpIfTable,
       "tnGmplsRsvpIfEntry": tnGmplsRsvpIfEntry,
       "tnGmplsRsvpIfId": tnGmplsRsvpIfId,
       "tnGmplsRsvpIfName": tnGmplsRsvpIfName,
       "tnGmplsRsvpIfType": tnGmplsRsvpIfType,
       "tnGmplsRsvpIfEncaps": tnGmplsRsvpIfEncaps,
       "tnGmplsRsvpIfCPNbr": tnGmplsRsvpIfCPNbr,
       "tnGmplsRsvpIfAdminStatus": tnGmplsRsvpIfAdminStatus,
       "tnGmplsRsvpIfOpState": tnGmplsRsvpIfOpState,
       "tnGmplsRsvpIfRowStatus": tnGmplsRsvpIfRowStatus,
       "tnGmplsDprIfTable": tnGmplsDprIfTable,
       "tnGmplsDprIfEntry": tnGmplsDprIfEntry,
       "tnGmplsDprIfId": tnGmplsDprIfId,
       "tnGmplsDprIfName": tnGmplsDprIfName,
       "tnGmplsDprIfType": tnGmplsDprIfType,
       "tnGmplsDprIfEncaps": tnGmplsDprIfEncaps,
       "tnGmplsDprIfCPNbr": tnGmplsDprIfCPNbr,
       "tnGmplsDprIfAdminStatus": tnGmplsDprIfAdminStatus,
       "tnGmplsDprIfOpState": tnGmplsDprIfOpState,
       "tnGmplsDprIfNVMismatch": tnGmplsDprIfNVMismatch,
       "tnGmplsDprIfRowStatus": tnGmplsDprIfRowStatus,
       "tnGmplsLmpIfTable": tnGmplsLmpIfTable,
       "tnGmplsLmpIfEntry": tnGmplsLmpIfEntry,
       "tnGmplsLmpIfId": tnGmplsLmpIfId,
       "tnGmplsLmpIfName": tnGmplsLmpIfName,
       "tnGmplsLmpIfCPNbr": tnGmplsLmpIfCPNbr,
       "tnGmplsLmpIfHelloEnabled": tnGmplsLmpIfHelloEnabled,
       "tnGmplsLmpIfLinkPropCorrEnabled": tnGmplsLmpIfLinkPropCorrEnabled,
       "tnGmplsLmpIfTraceMonEnabled": tnGmplsLmpIfTraceMonEnabled,
       "tnGmplsLmpIfEndPointDiscEnabled": tnGmplsLmpIfEndPointDiscEnabled,
       "tnGmplsLmpIfAdminStatus": tnGmplsLmpIfAdminStatus,
       "tnGmplsLmpIfOpState": tnGmplsLmpIfOpState,
       "tnGmplsLmpIfRowStatus": tnGmplsLmpIfRowStatus,
       "tnGmplsCpifConf": tnGmplsCpifConf,
       "tnGmplsCpifGroups": tnGmplsCpifGroups,
       "tnGmplsCpifObjsGroup": tnGmplsCpifObjsGroup,
       "tnGmplsCPNbrGroup": tnGmplsCPNbrGroup,
       "tnGmplsRsvpGroup": tnGmplsRsvpGroup,
       "tnGmplsDprGroup": tnGmplsDprGroup,
       "tnGmplsLmpGroup": tnGmplsLmpGroup,
       "tnGmplsCpifCompliances": tnGmplsCpifCompliances,
       "tnGmplsCpifCompliance": tnGmplsCpifCompliance}
)
