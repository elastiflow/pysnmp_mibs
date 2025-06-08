# SNMP MIB module (FDRY-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FDRY-ACL-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:53 2025
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

(fdryAcl,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "fdryAcl")

(FdryVlanIdOrNoneTC,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "FdryVlanIdOrNoneTC")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

fdryAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1)
)
if mibBuilder.loadTexts:
    fdryAclMIB.setRevisions(
        ("2010-06-02 00:00",
         "2008-02-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RtrStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class Action(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )



class Operator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eq", 0),
          ("neq", 1),
          ("lt", 2),
          ("gt", 3),
          ("range", 4),
          ("undefined", 7))
    )



class IpProtocol(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_FdryIpv6Acl_ObjectIdentity = ObjectIdentity
fdryIpv6Acl = _FdryIpv6Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1)
)
_FdryIpv6AclTable_Object = MibTable
fdryIpv6AclTable = _FdryIpv6AclTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fdryIpv6AclTable.setStatus("current")
_FdryIpv6AclEntry_Object = MibTableRow
fdryIpv6AclEntry = _FdryIpv6AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1)
)
fdryIpv6AclEntry.setIndexNames(
    (0, "FDRY-ACL-MIB", "fdryIpv6AclIndex"),
)
if mibBuilder.loadTexts:
    fdryIpv6AclEntry.setStatus("current")
_FdryIpv6AclIndex_Type = Unsigned32
_FdryIpv6AclIndex_Object = MibTableColumn
fdryIpv6AclIndex = _FdryIpv6AclIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 1),
    _FdryIpv6AclIndex_Type()
)
fdryIpv6AclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryIpv6AclIndex.setStatus("current")


class _FdryIpv6AclName_Type(DisplayString):
    """Custom type fdryIpv6AclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 199),
    )


_FdryIpv6AclName_Type.__name__ = "DisplayString"
_FdryIpv6AclName_Object = MibTableColumn
fdryIpv6AclName = _FdryIpv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 2),
    _FdryIpv6AclName_Type()
)
fdryIpv6AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclName.setStatus("current")
_FdryIpv6AclAction_Type = Action
_FdryIpv6AclAction_Object = MibTableColumn
fdryIpv6AclAction = _FdryIpv6AclAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 3),
    _FdryIpv6AclAction_Type()
)
fdryIpv6AclAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclAction.setStatus("current")
_FdryIpv6AclProtocol_Type = IpProtocol
_FdryIpv6AclProtocol_Object = MibTableColumn
fdryIpv6AclProtocol = _FdryIpv6AclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 4),
    _FdryIpv6AclProtocol_Type()
)
fdryIpv6AclProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclProtocol.setStatus("current")
_FdryIpv6AclSourceIp_Type = Ipv6Address
_FdryIpv6AclSourceIp_Object = MibTableColumn
fdryIpv6AclSourceIp = _FdryIpv6AclSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 5),
    _FdryIpv6AclSourceIp_Type()
)
fdryIpv6AclSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclSourceIp.setStatus("current")


class _FdryIpv6AclSourcePrefixLen_Type(Unsigned32):
    """Custom type fdryIpv6AclSourcePrefixLen based on Unsigned32"""
    defaultValue = 64


_FdryIpv6AclSourcePrefixLen_Type.__name__ = "Unsigned32"
_FdryIpv6AclSourcePrefixLen_Object = MibTableColumn
fdryIpv6AclSourcePrefixLen = _FdryIpv6AclSourcePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 6),
    _FdryIpv6AclSourcePrefixLen_Type()
)
fdryIpv6AclSourcePrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclSourcePrefixLen.setStatus("current")
_FdryIpv6AclSourceOperator_Type = Operator
_FdryIpv6AclSourceOperator_Object = MibTableColumn
fdryIpv6AclSourceOperator = _FdryIpv6AclSourceOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 7),
    _FdryIpv6AclSourceOperator_Type()
)
fdryIpv6AclSourceOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclSourceOperator.setStatus("current")


class _FdryIpv6AclSourceOperand1_Type(Unsigned32):
    """Custom type fdryIpv6AclSourceOperand1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryIpv6AclSourceOperand1_Type.__name__ = "Unsigned32"
_FdryIpv6AclSourceOperand1_Object = MibTableColumn
fdryIpv6AclSourceOperand1 = _FdryIpv6AclSourceOperand1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 8),
    _FdryIpv6AclSourceOperand1_Type()
)
fdryIpv6AclSourceOperand1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclSourceOperand1.setStatus("current")


class _FdryIpv6AclSourceOperand2_Type(Unsigned32):
    """Custom type fdryIpv6AclSourceOperand2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryIpv6AclSourceOperand2_Type.__name__ = "Unsigned32"
_FdryIpv6AclSourceOperand2_Object = MibTableColumn
fdryIpv6AclSourceOperand2 = _FdryIpv6AclSourceOperand2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 9),
    _FdryIpv6AclSourceOperand2_Type()
)
fdryIpv6AclSourceOperand2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclSourceOperand2.setStatus("current")
_FdryIpv6AclDestinationIp_Type = Ipv6Address
_FdryIpv6AclDestinationIp_Object = MibTableColumn
fdryIpv6AclDestinationIp = _FdryIpv6AclDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 10),
    _FdryIpv6AclDestinationIp_Type()
)
fdryIpv6AclDestinationIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclDestinationIp.setStatus("current")


class _FdryIpv6AclDestinationPrefixLen_Type(Unsigned32):
    """Custom type fdryIpv6AclDestinationPrefixLen based on Unsigned32"""
    defaultValue = 64


_FdryIpv6AclDestinationPrefixLen_Type.__name__ = "Unsigned32"
_FdryIpv6AclDestinationPrefixLen_Object = MibTableColumn
fdryIpv6AclDestinationPrefixLen = _FdryIpv6AclDestinationPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 11),
    _FdryIpv6AclDestinationPrefixLen_Type()
)
fdryIpv6AclDestinationPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclDestinationPrefixLen.setStatus("current")
_FdryIpv6AclDestinationOperator_Type = Operator
_FdryIpv6AclDestinationOperator_Object = MibTableColumn
fdryIpv6AclDestinationOperator = _FdryIpv6AclDestinationOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 12),
    _FdryIpv6AclDestinationOperator_Type()
)
fdryIpv6AclDestinationOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclDestinationOperator.setStatus("current")


class _FdryIpv6AclDestinationOperand1_Type(Unsigned32):
    """Custom type fdryIpv6AclDestinationOperand1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryIpv6AclDestinationOperand1_Type.__name__ = "Unsigned32"
_FdryIpv6AclDestinationOperand1_Object = MibTableColumn
fdryIpv6AclDestinationOperand1 = _FdryIpv6AclDestinationOperand1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 13),
    _FdryIpv6AclDestinationOperand1_Type()
)
fdryIpv6AclDestinationOperand1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclDestinationOperand1.setStatus("current")


class _FdryIpv6AclDestinationOperand2_Type(Unsigned32):
    """Custom type fdryIpv6AclDestinationOperand2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryIpv6AclDestinationOperand2_Type.__name__ = "Unsigned32"
_FdryIpv6AclDestinationOperand2_Object = MibTableColumn
fdryIpv6AclDestinationOperand2 = _FdryIpv6AclDestinationOperand2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 14),
    _FdryIpv6AclDestinationOperand2_Type()
)
fdryIpv6AclDestinationOperand2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclDestinationOperand2.setStatus("current")
_FdryIpv6AclEstablished_Type = RtrStatus
_FdryIpv6AclEstablished_Object = MibTableColumn
fdryIpv6AclEstablished = _FdryIpv6AclEstablished_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 15),
    _FdryIpv6AclEstablished_Type()
)
fdryIpv6AclEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclEstablished.setStatus("current")
_FdryIpv6AclLogOption_Type = TruthValue
_FdryIpv6AclLogOption_Object = MibTableColumn
fdryIpv6AclLogOption = _FdryIpv6AclLogOption_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 16),
    _FdryIpv6AclLogOption_Type()
)
fdryIpv6AclLogOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclLogOption.setStatus("current")


class _FdryIpv6AclComments_Type(DisplayString):
    """Custom type fdryIpv6AclComments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FdryIpv6AclComments_Type.__name__ = "DisplayString"
_FdryIpv6AclComments_Object = MibTableColumn
fdryIpv6AclComments = _FdryIpv6AclComments_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 17),
    _FdryIpv6AclComments_Type()
)
fdryIpv6AclComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclComments.setStatus("current")
_FdryIpv6AclRowStatus_Type = RowStatus
_FdryIpv6AclRowStatus_Object = MibTableColumn
fdryIpv6AclRowStatus = _FdryIpv6AclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 18),
    _FdryIpv6AclRowStatus_Type()
)
fdryIpv6AclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclRowStatus.setStatus("current")


class _FdryIpv6AclVlanId_Type(FdryVlanIdOrNoneTC):
    """Custom type fdryIpv6AclVlanId based on FdryVlanIdOrNoneTC"""
    defaultValue = 0


_FdryIpv6AclVlanId_Type.__name__ = "FdryVlanIdOrNoneTC"
_FdryIpv6AclVlanId_Object = MibTableColumn
fdryIpv6AclVlanId = _FdryIpv6AclVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 19),
    _FdryIpv6AclVlanId_Type()
)
fdryIpv6AclVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpv6AclVlanId.setStatus("current")
_FdryIpv6AclClauseString_Type = DisplayString
_FdryIpv6AclClauseString_Object = MibTableColumn
fdryIpv6AclClauseString = _FdryIpv6AclClauseString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 20),
    _FdryIpv6AclClauseString_Type()
)
fdryIpv6AclClauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryIpv6AclClauseString.setStatus("current")
_BrcdIpv6AccessListTable_Object = MibTable
brcdIpv6AccessListTable = _BrcdIpv6AccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    brcdIpv6AccessListTable.setStatus("current")
_BrcdIpv6AccessListEntry_Object = MibTableRow
brcdIpv6AccessListEntry = _BrcdIpv6AccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 2, 1)
)
brcdIpv6AccessListEntry.setIndexNames(
    (1, "FDRY-ACL-MIB", "brcdIpv6AccessListName"),
)
if mibBuilder.loadTexts:
    brcdIpv6AccessListEntry.setStatus("current")


class _BrcdIpv6AccessListName_Type(DisplayString):
    """Custom type brcdIpv6AccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 110),
    )


_BrcdIpv6AccessListName_Type.__name__ = "DisplayString"
_BrcdIpv6AccessListName_Object = MibTableColumn
brcdIpv6AccessListName = _BrcdIpv6AccessListName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 2, 1, 1),
    _BrcdIpv6AccessListName_Type()
)
brcdIpv6AccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdIpv6AccessListName.setStatus("current")
_BrcdIpv6AccessListNextIndex_Type = Unsigned32
_BrcdIpv6AccessListNextIndex_Object = MibTableColumn
brcdIpv6AccessListNextIndex = _BrcdIpv6AccessListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 2, 1, 2),
    _BrcdIpv6AccessListNextIndex_Type()
)
brcdIpv6AccessListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdIpv6AccessListNextIndex.setStatus("current")
_BrcdIpv6AccessListRowStatus_Type = RowStatus
_BrcdIpv6AccessListRowStatus_Object = MibTableColumn
brcdIpv6AccessListRowStatus = _BrcdIpv6AccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 2, 1, 3),
    _BrcdIpv6AccessListRowStatus_Type()
)
brcdIpv6AccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdIpv6AccessListRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-ACL-MIB",
    **{"RtrStatus": RtrStatus,
       "Action": Action,
       "Operator": Operator,
       "IpProtocol": IpProtocol,
       "fdryAclMIB": fdryAclMIB,
       "fdryIpv6Acl": fdryIpv6Acl,
       "fdryIpv6AclTable": fdryIpv6AclTable,
       "fdryIpv6AclEntry": fdryIpv6AclEntry,
       "fdryIpv6AclIndex": fdryIpv6AclIndex,
       "fdryIpv6AclName": fdryIpv6AclName,
       "fdryIpv6AclAction": fdryIpv6AclAction,
       "fdryIpv6AclProtocol": fdryIpv6AclProtocol,
       "fdryIpv6AclSourceIp": fdryIpv6AclSourceIp,
       "fdryIpv6AclSourcePrefixLen": fdryIpv6AclSourcePrefixLen,
       "fdryIpv6AclSourceOperator": fdryIpv6AclSourceOperator,
       "fdryIpv6AclSourceOperand1": fdryIpv6AclSourceOperand1,
       "fdryIpv6AclSourceOperand2": fdryIpv6AclSourceOperand2,
       "fdryIpv6AclDestinationIp": fdryIpv6AclDestinationIp,
       "fdryIpv6AclDestinationPrefixLen": fdryIpv6AclDestinationPrefixLen,
       "fdryIpv6AclDestinationOperator": fdryIpv6AclDestinationOperator,
       "fdryIpv6AclDestinationOperand1": fdryIpv6AclDestinationOperand1,
       "fdryIpv6AclDestinationOperand2": fdryIpv6AclDestinationOperand2,
       "fdryIpv6AclEstablished": fdryIpv6AclEstablished,
       "fdryIpv6AclLogOption": fdryIpv6AclLogOption,
       "fdryIpv6AclComments": fdryIpv6AclComments,
       "fdryIpv6AclRowStatus": fdryIpv6AclRowStatus,
       "fdryIpv6AclVlanId": fdryIpv6AclVlanId,
       "fdryIpv6AclClauseString": fdryIpv6AclClauseString,
       "brcdIpv6AccessListTable": brcdIpv6AccessListTable,
       "brcdIpv6AccessListEntry": brcdIpv6AccessListEntry,
       "brcdIpv6AccessListName": brcdIpv6AccessListName,
       "brcdIpv6AccessListNextIndex": brcdIpv6AccessListNextIndex,
       "brcdIpv6AccessListRowStatus": brcdIpv6AccessListRowStatus}
)
