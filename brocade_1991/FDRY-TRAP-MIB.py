# SNMP MIB module (FDRY-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FDRY-TRAP-MIB.mib
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

(fdryTrap,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "fdryTrap")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fdryTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    fdryTrapMIB.setRevisions(
        ("2010-06-02 00:00",
         "2008-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SecurityModel(TextualConvention, Integer32):
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
        *(("v1", 1),
          ("v2c", 2),
          ("usm", 3))
    )



class SecurityLevel(TextualConvention, Integer32):
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
        *(("noAuth", 1),
          ("auth", 2),
          ("authPriv", 3))
    )



# MIB Managed Objects in the order of their OIDs

_FdryTrapReceiver_ObjectIdentity = ObjectIdentity
fdryTrapReceiver = _FdryTrapReceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1)
)
_FdryTrapReceiverTable_Object = MibTable
fdryTrapReceiverTable = _FdryTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fdryTrapReceiverTable.setStatus("current")
_FdryTrapReceiverEntry_Object = MibTableRow
fdryTrapReceiverEntry = _FdryTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1)
)
fdryTrapReceiverEntry.setIndexNames(
    (0, "FDRY-TRAP-MIB", "fdryTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    fdryTrapReceiverEntry.setStatus("current")
_FdryTrapReceiverIndex_Type = Unsigned32
_FdryTrapReceiverIndex_Object = MibTableColumn
fdryTrapReceiverIndex = _FdryTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 1),
    _FdryTrapReceiverIndex_Type()
)
fdryTrapReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryTrapReceiverIndex.setStatus("current")


class _FdryTrapReceiverAddrType_Type(InetAddressType):
    """Custom type fdryTrapReceiverAddrType based on InetAddressType"""
    defaultValue = 1


_FdryTrapReceiverAddrType_Type.__name__ = "InetAddressType"
_FdryTrapReceiverAddrType_Object = MibTableColumn
fdryTrapReceiverAddrType = _FdryTrapReceiverAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 2),
    _FdryTrapReceiverAddrType_Type()
)
fdryTrapReceiverAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverAddrType.setStatus("current")
_FdryTrapReceiverAddr_Type = InetAddress
_FdryTrapReceiverAddr_Object = MibTableColumn
fdryTrapReceiverAddr = _FdryTrapReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 3),
    _FdryTrapReceiverAddr_Type()
)
fdryTrapReceiverAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverAddr.setStatus("current")


class _FdryTrapReceiverCommunityOrSecurityName_Type(OctetString):
    """Custom type fdryTrapReceiverCommunityOrSecurityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FdryTrapReceiverCommunityOrSecurityName_Type.__name__ = "OctetString"
_FdryTrapReceiverCommunityOrSecurityName_Object = MibTableColumn
fdryTrapReceiverCommunityOrSecurityName = _FdryTrapReceiverCommunityOrSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 4),
    _FdryTrapReceiverCommunityOrSecurityName_Type()
)
fdryTrapReceiverCommunityOrSecurityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverCommunityOrSecurityName.setStatus("current")


class _FdryTrapReceiverUDPPort_Type(Integer32):
    """Custom type fdryTrapReceiverUDPPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryTrapReceiverUDPPort_Type.__name__ = "Integer32"
_FdryTrapReceiverUDPPort_Object = MibTableColumn
fdryTrapReceiverUDPPort = _FdryTrapReceiverUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 5),
    _FdryTrapReceiverUDPPort_Type()
)
fdryTrapReceiverUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverUDPPort.setStatus("current")


class _FdryTrapReceiverSecurityModel_Type(SecurityModel):
    """Custom type fdryTrapReceiverSecurityModel based on SecurityModel"""
    defaultValue = 1


_FdryTrapReceiverSecurityModel_Type.__name__ = "SecurityModel"
_FdryTrapReceiverSecurityModel_Object = MibTableColumn
fdryTrapReceiverSecurityModel = _FdryTrapReceiverSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 6),
    _FdryTrapReceiverSecurityModel_Type()
)
fdryTrapReceiverSecurityModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverSecurityModel.setStatus("current")


class _FdryTrapReceiverSecurityLevel_Type(SecurityLevel):
    """Custom type fdryTrapReceiverSecurityLevel based on SecurityLevel"""
    defaultValue = 1


_FdryTrapReceiverSecurityLevel_Type.__name__ = "SecurityLevel"
_FdryTrapReceiverSecurityLevel_Object = MibTableColumn
fdryTrapReceiverSecurityLevel = _FdryTrapReceiverSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 7),
    _FdryTrapReceiverSecurityLevel_Type()
)
fdryTrapReceiverSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverSecurityLevel.setStatus("current")
_FdryTrapReceiverRowStatus_Type = RowStatus
_FdryTrapReceiverRowStatus_Object = MibTableColumn
fdryTrapReceiverRowStatus = _FdryTrapReceiverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 8),
    _FdryTrapReceiverRowStatus_Type()
)
fdryTrapReceiverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTrapReceiverRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-TRAP-MIB",
    **{"SecurityModel": SecurityModel,
       "SecurityLevel": SecurityLevel,
       "fdryTrapMIB": fdryTrapMIB,
       "fdryTrapReceiver": fdryTrapReceiver,
       "fdryTrapReceiverTable": fdryTrapReceiverTable,
       "fdryTrapReceiverEntry": fdryTrapReceiverEntry,
       "fdryTrapReceiverIndex": fdryTrapReceiverIndex,
       "fdryTrapReceiverAddrType": fdryTrapReceiverAddrType,
       "fdryTrapReceiverAddr": fdryTrapReceiverAddr,
       "fdryTrapReceiverCommunityOrSecurityName": fdryTrapReceiverCommunityOrSecurityName,
       "fdryTrapReceiverUDPPort": fdryTrapReceiverUDPPort,
       "fdryTrapReceiverSecurityModel": fdryTrapReceiverSecurityModel,
       "fdryTrapReceiverSecurityLevel": fdryTrapReceiverSecurityLevel,
       "fdryTrapReceiverRowStatus": fdryTrapReceiverRowStatus}
)
