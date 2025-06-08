# SNMP MIB module (RUIJIE-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ACL-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:23 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17)
)
if mibBuilder.loadTexts:
    ruijieAclMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieAclMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAclMIBObjects = _RuijieAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1)
)
_RuijieAclTable_Object = MibTable
ruijieAclTable = _RuijieAclTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieAclTable.setStatus("current")
_RuijieAclEntry_Object = MibTableRow
ruijieAclEntry = _RuijieAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1, 1)
)
ruijieAclEntry.setIndexNames(
    (0, "RUIJIE-ACL-MIB", "ruijieAclName"),
)
if mibBuilder.loadTexts:
    ruijieAclEntry.setStatus("current")


class _RuijieAclName_Type(DisplayString):
    """Custom type ruijieAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieAclName_Type.__name__ = "DisplayString"
_RuijieAclName_Object = MibTableColumn
ruijieAclName = _RuijieAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1, 1, 1),
    _RuijieAclName_Type()
)
ruijieAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclName.setStatus("current")


class _RuijieAclMode_Type(Integer32):
    """Custom type ruijieAclMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acl-ip-standard", 1),
          ("acl-ip-extended", 2),
          ("acl-mac-extended", 3),
          ("acl-expert", 4),
          ("acl-ipv6-extended", 5))
    )


_RuijieAclMode_Type.__name__ = "Integer32"
_RuijieAclMode_Object = MibTableColumn
ruijieAclMode = _RuijieAclMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1, 1, 2),
    _RuijieAclMode_Type()
)
ruijieAclMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAclMode.setStatus("current")
_RuijieAclEntryStatus_Type = ConfigStatus
_RuijieAclEntryStatus_Object = MibTableColumn
ruijieAclEntryStatus = _RuijieAclEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1, 1, 3),
    _RuijieAclEntryStatus_Type()
)
ruijieAclEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAclEntryStatus.setStatus("current")
_RuijieAclIfTable_Object = MibTable
ruijieAclIfTable = _RuijieAclIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieAclIfTable.setStatus("current")
_RuijieAclIfEntry_Object = MibTableRow
ruijieAclIfEntry = _RuijieAclIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1)
)
ruijieAclIfEntry.setIndexNames(
    (0, "RUIJIE-ACL-MIB", "ruijieAclIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieAclIfEntry.setStatus("current")
_RuijieAclIfIndex_Type = IfIndex
_RuijieAclIfIndex_Object = MibTableColumn
ruijieAclIfIndex = _RuijieAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 1),
    _RuijieAclIfIndex_Type()
)
ruijieAclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclIfIndex.setStatus("current")
_RuijieAclIfMaxEntryNum_Type = Integer32
_RuijieAclIfMaxEntryNum_Object = MibTableColumn
ruijieAclIfMaxEntryNum = _RuijieAclIfMaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 2),
    _RuijieAclIfMaxEntryNum_Type()
)
ruijieAclIfMaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclIfMaxEntryNum.setStatus("current")
_RuijieAclIfCurruntEntryNum_Type = Integer32
_RuijieAclIfCurruntEntryNum_Object = MibTableColumn
ruijieAclIfCurruntEntryNum = _RuijieAclIfCurruntEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 3),
    _RuijieAclIfCurruntEntryNum_Type()
)
ruijieAclIfCurruntEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclIfCurruntEntryNum.setStatus("current")


class _RuijieIfInAclName_Type(DisplayString):
    """Custom type ruijieIfInAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieIfInAclName_Type.__name__ = "DisplayString"
_RuijieIfInAclName_Object = MibTableColumn
ruijieIfInAclName = _RuijieIfInAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 4),
    _RuijieIfInAclName_Type()
)
ruijieIfInAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfInAclName.setStatus("current")


class _RuijieIfOutAclName_Type(DisplayString):
    """Custom type ruijieIfOutAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieIfOutAclName_Type.__name__ = "DisplayString"
_RuijieIfOutAclName_Object = MibTableColumn
ruijieIfOutAclName = _RuijieIfOutAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 5),
    _RuijieIfOutAclName_Type()
)
ruijieIfOutAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfOutAclName.setStatus("current")
_RuijieAclIf6MaxEntryNum_Type = Integer32
_RuijieAclIf6MaxEntryNum_Object = MibTableColumn
ruijieAclIf6MaxEntryNum = _RuijieAclIf6MaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 6),
    _RuijieAclIf6MaxEntryNum_Type()
)
ruijieAclIf6MaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclIf6MaxEntryNum.setStatus("current")
_RuijieAclIf6CurruntEntryNum_Type = Integer32
_RuijieAclIf6CurruntEntryNum_Object = MibTableColumn
ruijieAclIf6CurruntEntryNum = _RuijieAclIf6CurruntEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 7),
    _RuijieAclIf6CurruntEntryNum_Type()
)
ruijieAclIf6CurruntEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclIf6CurruntEntryNum.setStatus("current")


class _RuijieIf6InAclName_Type(DisplayString):
    """Custom type ruijieIf6InAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieIf6InAclName_Type.__name__ = "DisplayString"
_RuijieIf6InAclName_Object = MibTableColumn
ruijieIf6InAclName = _RuijieIf6InAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 8),
    _RuijieIf6InAclName_Type()
)
ruijieIf6InAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIf6InAclName.setStatus("current")


class _RuijieIf6OutAclName_Type(DisplayString):
    """Custom type ruijieIf6OutAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieIf6OutAclName_Type.__name__ = "DisplayString"
_RuijieIf6OutAclName_Object = MibTableColumn
ruijieIf6OutAclName = _RuijieIf6OutAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 9),
    _RuijieIf6OutAclName_Type()
)
ruijieIf6OutAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIf6OutAclName.setStatus("current")
_RuijieAceExtTable_Object = MibTable
ruijieAceExtTable = _RuijieAceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieAceExtTable.setStatus("current")
_RuijieAceExtEntry_Object = MibTableRow
ruijieAceExtEntry = _RuijieAceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1)
)
ruijieAceExtEntry.setIndexNames(
    (0, "RUIJIE-ACL-MIB", "ruijieAceExtAclName"),
    (0, "RUIJIE-ACL-MIB", "ruijieAceExtIndex"),
)
if mibBuilder.loadTexts:
    ruijieAceExtEntry.setStatus("current")


class _RuijieAceExtAclName_Type(DisplayString):
    """Custom type ruijieAceExtAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieAceExtAclName_Type.__name__ = "DisplayString"
_RuijieAceExtAclName_Object = MibTableColumn
ruijieAceExtAclName = _RuijieAceExtAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 1),
    _RuijieAceExtAclName_Type()
)
ruijieAceExtAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAceExtAclName.setStatus("current")


class _RuijieAceExtIndex_Type(Integer32):
    """Custom type ruijieAceExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieAceExtIndex_Type.__name__ = "Integer32"
_RuijieAceExtIndex_Object = MibTableColumn
ruijieAceExtIndex = _RuijieAceExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 2),
    _RuijieAceExtIndex_Type()
)
ruijieAceExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAceExtIndex.setStatus("current")


class _RuijieAceExtIfAnyVID_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyVID based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyVID_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyVID_Object = MibTableColumn
ruijieAceExtIfAnyVID = _RuijieAceExtIfAnyVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 3),
    _RuijieAceExtIfAnyVID_Type()
)
ruijieAceExtIfAnyVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyVID.setStatus("current")


class _RuijieAceExtVID_Type(Unsigned32):
    """Custom type ruijieAceExtVID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RuijieAceExtVID_Type.__name__ = "Unsigned32"
_RuijieAceExtVID_Object = MibTableColumn
ruijieAceExtVID = _RuijieAceExtVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 4),
    _RuijieAceExtVID_Type()
)
ruijieAceExtVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtVID.setStatus("current")


class _RuijieAceExtIfAnySourceIp_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceIp based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceIp_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceIp_Object = MibTableColumn
ruijieAceExtIfAnySourceIp = _RuijieAceExtIfAnySourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 5),
    _RuijieAceExtIfAnySourceIp_Type()
)
ruijieAceExtIfAnySourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceIp.setStatus("current")
_RuijieAceExtSourceIp_Type = IpAddress
_RuijieAceExtSourceIp_Object = MibTableColumn
ruijieAceExtSourceIp = _RuijieAceExtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 6),
    _RuijieAceExtSourceIp_Type()
)
ruijieAceExtSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceIp.setStatus("current")


class _RuijieAceExtIfAnySourceWildCard_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceWildCard based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceWildCard_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceWildCard_Object = MibTableColumn
ruijieAceExtIfAnySourceWildCard = _RuijieAceExtIfAnySourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 7),
    _RuijieAceExtIfAnySourceWildCard_Type()
)
ruijieAceExtIfAnySourceWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceWildCard.setStatus("current")
_RuijieAceExtSourceWildCard_Type = IpAddress
_RuijieAceExtSourceWildCard_Object = MibTableColumn
ruijieAceExtSourceWildCard = _RuijieAceExtSourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 8),
    _RuijieAceExtSourceWildCard_Type()
)
ruijieAceExtSourceWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceWildCard.setStatus("current")


class _RuijieAceExtIfAnySourceMacAddr_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceMacAddr based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceMacAddr_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceMacAddr_Object = MibTableColumn
ruijieAceExtIfAnySourceMacAddr = _RuijieAceExtIfAnySourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 9),
    _RuijieAceExtIfAnySourceMacAddr_Type()
)
ruijieAceExtIfAnySourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceMacAddr.setStatus("current")
_RuijieAceExtSourceMacAddr_Type = MacAddress
_RuijieAceExtSourceMacAddr_Object = MibTableColumn
ruijieAceExtSourceMacAddr = _RuijieAceExtSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 10),
    _RuijieAceExtSourceMacAddr_Type()
)
ruijieAceExtSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceMacAddr.setStatus("current")


class _RuijieAceExtIfAnyDestIp_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestIp based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestIp_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestIp_Object = MibTableColumn
ruijieAceExtIfAnyDestIp = _RuijieAceExtIfAnyDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 11),
    _RuijieAceExtIfAnyDestIp_Type()
)
ruijieAceExtIfAnyDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestIp.setStatus("current")
_RuijieAceExtDestIp_Type = IpAddress
_RuijieAceExtDestIp_Object = MibTableColumn
ruijieAceExtDestIp = _RuijieAceExtDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 12),
    _RuijieAceExtDestIp_Type()
)
ruijieAceExtDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestIp.setStatus("current")


class _RuijieAceExtIfAnyDestWildCard_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestWildCard based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestWildCard_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestWildCard_Object = MibTableColumn
ruijieAceExtIfAnyDestWildCard = _RuijieAceExtIfAnyDestWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 13),
    _RuijieAceExtIfAnyDestWildCard_Type()
)
ruijieAceExtIfAnyDestWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestWildCard.setStatus("current")
_RuijieAceExtDestIpWildCard_Type = IpAddress
_RuijieAceExtDestIpWildCard_Object = MibTableColumn
ruijieAceExtDestIpWildCard = _RuijieAceExtDestIpWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 14),
    _RuijieAceExtDestIpWildCard_Type()
)
ruijieAceExtDestIpWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestIpWildCard.setStatus("current")


class _RuijieAceExtIfAnyDestMacAddr_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestMacAddr based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestMacAddr_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestMacAddr_Object = MibTableColumn
ruijieAceExtIfAnyDestMacAddr = _RuijieAceExtIfAnyDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 15),
    _RuijieAceExtIfAnyDestMacAddr_Type()
)
ruijieAceExtIfAnyDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestMacAddr.setStatus("current")
_RuijieAceExtDestMacAddr_Type = MacAddress
_RuijieAceExtDestMacAddr_Object = MibTableColumn
ruijieAceExtDestMacAddr = _RuijieAceExtDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 16),
    _RuijieAceExtDestMacAddr_Type()
)
ruijieAceExtDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestMacAddr.setStatus("current")


class _RuijieAceExtIfAnyEtherLikeType_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyEtherLikeType based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyEtherLikeType_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyEtherLikeType_Object = MibTableColumn
ruijieAceExtIfAnyEtherLikeType = _RuijieAceExtIfAnyEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 17),
    _RuijieAceExtIfAnyEtherLikeType_Type()
)
ruijieAceExtIfAnyEtherLikeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyEtherLikeType.setStatus("current")
_RuijieAceExtEtherLikeType_Type = Integer32
_RuijieAceExtEtherLikeType_Object = MibTableColumn
ruijieAceExtEtherLikeType = _RuijieAceExtEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 18),
    _RuijieAceExtEtherLikeType_Type()
)
ruijieAceExtEtherLikeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtEtherLikeType.setStatus("current")


class _RuijieAceExtIfAnyIpProtocolField_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyIpProtocolField based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyIpProtocolField_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyIpProtocolField_Object = MibTableColumn
ruijieAceExtIfAnyIpProtocolField = _RuijieAceExtIfAnyIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 19),
    _RuijieAceExtIfAnyIpProtocolField_Type()
)
ruijieAceExtIfAnyIpProtocolField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyIpProtocolField.setStatus("current")
_RuijieAceExtIpProtocolField_Type = Integer32
_RuijieAceExtIpProtocolField_Object = MibTableColumn
ruijieAceExtIpProtocolField = _RuijieAceExtIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 20),
    _RuijieAceExtIpProtocolField_Type()
)
ruijieAceExtIpProtocolField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIpProtocolField.setStatus("current")
_RuijieAceExtSourceProtocolPort_Type = Integer32
_RuijieAceExtSourceProtocolPort_Object = MibTableColumn
ruijieAceExtSourceProtocolPort = _RuijieAceExtSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 21),
    _RuijieAceExtSourceProtocolPort_Type()
)
ruijieAceExtSourceProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceProtocolPort.setStatus("current")
_RuijieAceExtDestProtocolPort_Type = Integer32
_RuijieAceExtDestProtocolPort_Object = MibTableColumn
ruijieAceExtDestProtocolPort = _RuijieAceExtDestProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 22),
    _RuijieAceExtDestProtocolPort_Type()
)
ruijieAceExtDestProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestProtocolPort.setStatus("current")


class _RuijieAceExtIfAnyProtocolType_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyProtocolType based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyProtocolType_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyProtocolType_Object = MibTableColumn
ruijieAceExtIfAnyProtocolType = _RuijieAceExtIfAnyProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 23),
    _RuijieAceExtIfAnyProtocolType_Type()
)
ruijieAceExtIfAnyProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyProtocolType.setStatus("current")
_RuijieAceExtProtocolType_Type = Integer32
_RuijieAceExtProtocolType_Object = MibTableColumn
ruijieAceExtProtocolType = _RuijieAceExtProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 24),
    _RuijieAceExtProtocolType_Type()
)
ruijieAceExtProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtProtocolType.setStatus("current")


class _RuijieAceExtFlowAction_Type(Integer32):
    """Custom type ruijieAceExtFlowAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RuijieAceExtFlowAction_Type.__name__ = "Integer32"
_RuijieAceExtFlowAction_Object = MibTableColumn
ruijieAceExtFlowAction = _RuijieAceExtFlowAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 25),
    _RuijieAceExtFlowAction_Type()
)
ruijieAceExtFlowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtFlowAction.setStatus("current")
_RuijieAceExtEntryStauts_Type = RowStatus
_RuijieAceExtEntryStauts_Object = MibTableColumn
ruijieAceExtEntryStauts = _RuijieAceExtEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 26),
    _RuijieAceExtEntryStauts_Type()
)
ruijieAceExtEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtEntryStauts.setStatus("current")


class _RuijieAceExtTimeRangeName_Type(DisplayString):
    """Custom type ruijieAceExtTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieAceExtTimeRangeName_Type.__name__ = "DisplayString"
_RuijieAceExtTimeRangeName_Object = MibTableColumn
ruijieAceExtTimeRangeName = _RuijieAceExtTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 27),
    _RuijieAceExtTimeRangeName_Type()
)
ruijieAceExtTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtTimeRangeName.setStatus("current")


class _RuijieAceExtSourcePortOp_Type(Integer32):
    """Custom type ruijieAceExtSourcePortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noOperator", 1),
          ("lt", 2),
          ("gt", 3),
          ("eq", 4),
          ("neq", 5),
          ("range", 6))
    )


_RuijieAceExtSourcePortOp_Type.__name__ = "Integer32"
_RuijieAceExtSourcePortOp_Object = MibTableColumn
ruijieAceExtSourcePortOp = _RuijieAceExtSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 28),
    _RuijieAceExtSourcePortOp_Type()
)
ruijieAceExtSourcePortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtSourcePortOp.setStatus("current")
_RuijieAceExtSourceProtocolPortRange_Type = Integer32
_RuijieAceExtSourceProtocolPortRange_Object = MibTableColumn
ruijieAceExtSourceProtocolPortRange = _RuijieAceExtSourceProtocolPortRange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 29),
    _RuijieAceExtSourceProtocolPortRange_Type()
)
ruijieAceExtSourceProtocolPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtSourceProtocolPortRange.setStatus("current")


class _RuijieAceExtDestPortOp_Type(Integer32):
    """Custom type ruijieAceExtDestPortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noOperator", 1),
          ("lt", 2),
          ("gt", 3),
          ("eq", 4),
          ("neq", 5),
          ("range", 6))
    )


_RuijieAceExtDestPortOp_Type.__name__ = "Integer32"
_RuijieAceExtDestPortOp_Object = MibTableColumn
ruijieAceExtDestPortOp = _RuijieAceExtDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 30),
    _RuijieAceExtDestPortOp_Type()
)
ruijieAceExtDestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtDestPortOp.setStatus("current")
_RuijieAceExtDestProtocolPortRange_Type = Integer32
_RuijieAceExtDestProtocolPortRange_Object = MibTableColumn
ruijieAceExtDestProtocolPortRange = _RuijieAceExtDestProtocolPortRange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 31),
    _RuijieAceExtDestProtocolPortRange_Type()
)
ruijieAceExtDestProtocolPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtDestProtocolPortRange.setStatus("current")


class _RuijieAceExtIfAnyCos_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyCos based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyCos_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyCos_Object = MibTableColumn
ruijieAceExtIfAnyCos = _RuijieAceExtIfAnyCos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 32),
    _RuijieAceExtIfAnyCos_Type()
)
ruijieAceExtIfAnyCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyCos.setStatus("current")
_RuijieAceExtCos_Type = Integer32
_RuijieAceExtCos_Object = MibTableColumn
ruijieAceExtCos = _RuijieAceExtCos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 33),
    _RuijieAceExtCos_Type()
)
ruijieAceExtCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtCos.setStatus("current")


class _RuijieAceExtIfAnyIpPrec_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyIpPrec based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyIpPrec_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyIpPrec_Object = MibTableColumn
ruijieAceExtIfAnyIpPrec = _RuijieAceExtIfAnyIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 34),
    _RuijieAceExtIfAnyIpPrec_Type()
)
ruijieAceExtIfAnyIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyIpPrec.setStatus("current")
_RuijieAceExtIpPrec_Type = Integer32
_RuijieAceExtIpPrec_Object = MibTableColumn
ruijieAceExtIpPrec = _RuijieAceExtIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 35),
    _RuijieAceExtIpPrec_Type()
)
ruijieAceExtIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIpPrec.setStatus("current")


class _RuijieAceExtIfAnyDscp_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDscp based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDscp_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDscp_Object = MibTableColumn
ruijieAceExtIfAnyDscp = _RuijieAceExtIfAnyDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 36),
    _RuijieAceExtIfAnyDscp_Type()
)
ruijieAceExtIfAnyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDscp.setStatus("current")
_RuijieAceExtDscp_Type = Integer32
_RuijieAceExtDscp_Object = MibTableColumn
ruijieAceExtDscp = _RuijieAceExtDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 37),
    _RuijieAceExtDscp_Type()
)
ruijieAceExtDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtDscp.setStatus("current")


class _RuijieAceExtIfAnyTcpFlag_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyTcpFlag based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyTcpFlag_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyTcpFlag_Object = MibTableColumn
ruijieAceExtIfAnyTcpFlag = _RuijieAceExtIfAnyTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 38),
    _RuijieAceExtIfAnyTcpFlag_Type()
)
ruijieAceExtIfAnyTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyTcpFlag.setStatus("current")
_RuijieAceExtTcpFlag_Type = Integer32
_RuijieAceExtTcpFlag_Object = MibTableColumn
ruijieAceExtTcpFlag = _RuijieAceExtTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 39),
    _RuijieAceExtTcpFlag_Type()
)
ruijieAceExtTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtTcpFlag.setStatus("current")


class _RuijieAceExtIfAnySourceMacAddrWildCard_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceMacAddrWildCard based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceMacAddrWildCard_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceMacAddrWildCard_Object = MibTableColumn
ruijieAceExtIfAnySourceMacAddrWildCard = _RuijieAceExtIfAnySourceMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 40),
    _RuijieAceExtIfAnySourceMacAddrWildCard_Type()
)
ruijieAceExtIfAnySourceMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceMacAddrWildCard.setStatus("current")
_RuijieAceExtSourceMacAddrWildCard_Type = MacAddress
_RuijieAceExtSourceMacAddrWildCard_Object = MibTableColumn
ruijieAceExtSourceMacAddrWildCard = _RuijieAceExtSourceMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 41),
    _RuijieAceExtSourceMacAddrWildCard_Type()
)
ruijieAceExtSourceMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtSourceMacAddrWildCard.setStatus("current")


class _RuijieAceExtIfAnyDestMacAddrWildCard_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestMacAddrWildCard based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestMacAddrWildCard_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestMacAddrWildCard_Object = MibTableColumn
ruijieAceExtIfAnyDestMacAddrWildCard = _RuijieAceExtIfAnyDestMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 42),
    _RuijieAceExtIfAnyDestMacAddrWildCard_Type()
)
ruijieAceExtIfAnyDestMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestMacAddrWildCard.setStatus("current")
_RuijieAceExtDestMacAddrWildCard_Type = MacAddress
_RuijieAceExtDestMacAddrWildCard_Object = MibTableColumn
ruijieAceExtDestMacAddrWildCard = _RuijieAceExtDestMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 43),
    _RuijieAceExtDestMacAddrWildCard_Type()
)
ruijieAceExtDestMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtDestMacAddrWildCard.setStatus("current")


class _RuijieAceExtIfAnySourceIp6_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceIp6 based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceIp6_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceIp6_Object = MibTableColumn
ruijieAceExtIfAnySourceIp6 = _RuijieAceExtIfAnySourceIp6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 44),
    _RuijieAceExtIfAnySourceIp6_Type()
)
ruijieAceExtIfAnySourceIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceIp6.setStatus("current")


class _RuijieAceExtSourceIp6_Type(OctetString):
    """Custom type ruijieAceExtSourceIp6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieAceExtSourceIp6_Type.__name__ = "OctetString"
_RuijieAceExtSourceIp6_Object = MibTableColumn
ruijieAceExtSourceIp6 = _RuijieAceExtSourceIp6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 45),
    _RuijieAceExtSourceIp6_Type()
)
ruijieAceExtSourceIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtSourceIp6.setStatus("current")


class _RuijieAceExtIfAnySourceIp6WildCard_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceIp6WildCard based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceIp6WildCard_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceIp6WildCard_Object = MibTableColumn
ruijieAceExtIfAnySourceIp6WildCard = _RuijieAceExtIfAnySourceIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 46),
    _RuijieAceExtIfAnySourceIp6WildCard_Type()
)
ruijieAceExtIfAnySourceIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceIp6WildCard.setStatus("current")


class _RuijieAceExtSourceIp6WildCard_Type(OctetString):
    """Custom type ruijieAceExtSourceIp6WildCard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieAceExtSourceIp6WildCard_Type.__name__ = "OctetString"
_RuijieAceExtSourceIp6WildCard_Object = MibTableColumn
ruijieAceExtSourceIp6WildCard = _RuijieAceExtSourceIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 47),
    _RuijieAceExtSourceIp6WildCard_Type()
)
ruijieAceExtSourceIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtSourceIp6WildCard.setStatus("current")


class _RuijieAceExtIfAnyDestIp6_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestIp6 based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestIp6_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestIp6_Object = MibTableColumn
ruijieAceExtIfAnyDestIp6 = _RuijieAceExtIfAnyDestIp6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 48),
    _RuijieAceExtIfAnyDestIp6_Type()
)
ruijieAceExtIfAnyDestIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestIp6.setStatus("current")


class _RuijieAceExtDestIp6_Type(OctetString):
    """Custom type ruijieAceExtDestIp6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieAceExtDestIp6_Type.__name__ = "OctetString"
_RuijieAceExtDestIp6_Object = MibTableColumn
ruijieAceExtDestIp6 = _RuijieAceExtDestIp6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 49),
    _RuijieAceExtDestIp6_Type()
)
ruijieAceExtDestIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtDestIp6.setStatus("current")


class _RuijieAceExtIfAnyDestIp6WildCard_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestIp6WildCard based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestIp6WildCard_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestIp6WildCard_Object = MibTableColumn
ruijieAceExtIfAnyDestIp6WildCard = _RuijieAceExtIfAnyDestIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 50),
    _RuijieAceExtIfAnyDestIp6WildCard_Type()
)
ruijieAceExtIfAnyDestIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestIp6WildCard.setStatus("current")


class _RuijieAceExtDestIp6WildCard_Type(OctetString):
    """Custom type ruijieAceExtDestIp6WildCard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieAceExtDestIp6WildCard_Type.__name__ = "OctetString"
_RuijieAceExtDestIp6WildCard_Object = MibTableColumn
ruijieAceExtDestIp6WildCard = _RuijieAceExtDestIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 4, 1, 51),
    _RuijieAceExtDestIp6WildCard_Type()
)
ruijieAceExtDestIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAceExtDestIp6WildCard.setStatus("current")
_RuijieAclMIBConformance_ObjectIdentity = ObjectIdentity
ruijieAclMIBConformance = _RuijieAclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2)
)
_RuijieAclMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieAclMIBCompliances = _RuijieAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2, 1)
)
_RuijieAclMIBGroups_ObjectIdentity = ObjectIdentity
ruijieAclMIBGroups = _RuijieAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2, 2)
)

# Managed Objects groups

ruijieAclMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2, 2, 1)
)
ruijieAclMIBGroup.setObjects(
      *(("RUIJIE-ACL-MIB", "ruijieAclName"),
        ("RUIJIE-ACL-MIB", "ruijieAclMode"),
        ("RUIJIE-ACL-MIB", "ruijieAclEntryStatus"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtAclName"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIndex"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyVID"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtVID"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnySourceIp"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtSourceIp"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnySourceWildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtSourceWildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnySourceMacAddr"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtSourceMacAddr"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyDestIp"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDestIp"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyDestWildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDestIpWildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyDestMacAddr"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDestMacAddr"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyEtherLikeType"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtEtherLikeType"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyIpProtocolField"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIpProtocolField"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtSourceProtocolPort"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDestProtocolPort"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtProtocolType"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtProtocolType"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtFlowAction"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtEntryStauts"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtTimeRangeName"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtSourcePortOp"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtSourceProtocolPortRange"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDestPortOp"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDestProtocolPortRange"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyCos"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtCos"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyIpPrec"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIpPrec"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyDscp"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDscp"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyTcpFlag"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtTcpFlag"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnySourceMacAddrWildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtSourceMacAddrWildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyDestMacAddrWildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDestMacAddrWildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnySourceIp6"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtSourceIp6"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnySourceIp6WildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtSourceIp6WildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyDestIp6"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDestIp6"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtIfAnyDestIp6WildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAceExtDestIp6WildCard"),
        ("RUIJIE-ACL-MIB", "ruijieAclIfIndex"),
        ("RUIJIE-ACL-MIB", "ruijieAclIfMaxEntryNum"),
        ("RUIJIE-ACL-MIB", "ruijieAclIfCurruntEntryNum"),
        ("RUIJIE-ACL-MIB", "ruijieIfInAclName"),
        ("RUIJIE-ACL-MIB", "ruijieIfOutAclName"))
)
if mibBuilder.loadTexts:
    ruijieAclMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2, 1, 1)
)
ruijieAclMIBCompliance.setObjects(
    ("RUIJIE-ACL-MIB", "ruijieAclMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieAclMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ACL-MIB",
    **{"ruijieAclMIB": ruijieAclMIB,
       "ruijieAclMIBObjects": ruijieAclMIBObjects,
       "ruijieAclTable": ruijieAclTable,
       "ruijieAclEntry": ruijieAclEntry,
       "ruijieAclName": ruijieAclName,
       "ruijieAclMode": ruijieAclMode,
       "ruijieAclEntryStatus": ruijieAclEntryStatus,
       "ruijieAclIfTable": ruijieAclIfTable,
       "ruijieAclIfEntry": ruijieAclIfEntry,
       "ruijieAclIfIndex": ruijieAclIfIndex,
       "ruijieAclIfMaxEntryNum": ruijieAclIfMaxEntryNum,
       "ruijieAclIfCurruntEntryNum": ruijieAclIfCurruntEntryNum,
       "ruijieIfInAclName": ruijieIfInAclName,
       "ruijieIfOutAclName": ruijieIfOutAclName,
       "ruijieAclIf6MaxEntryNum": ruijieAclIf6MaxEntryNum,
       "ruijieAclIf6CurruntEntryNum": ruijieAclIf6CurruntEntryNum,
       "ruijieIf6InAclName": ruijieIf6InAclName,
       "ruijieIf6OutAclName": ruijieIf6OutAclName,
       "ruijieAceExtTable": ruijieAceExtTable,
       "ruijieAceExtEntry": ruijieAceExtEntry,
       "ruijieAceExtAclName": ruijieAceExtAclName,
       "ruijieAceExtIndex": ruijieAceExtIndex,
       "ruijieAceExtIfAnyVID": ruijieAceExtIfAnyVID,
       "ruijieAceExtVID": ruijieAceExtVID,
       "ruijieAceExtIfAnySourceIp": ruijieAceExtIfAnySourceIp,
       "ruijieAceExtSourceIp": ruijieAceExtSourceIp,
       "ruijieAceExtIfAnySourceWildCard": ruijieAceExtIfAnySourceWildCard,
       "ruijieAceExtSourceWildCard": ruijieAceExtSourceWildCard,
       "ruijieAceExtIfAnySourceMacAddr": ruijieAceExtIfAnySourceMacAddr,
       "ruijieAceExtSourceMacAddr": ruijieAceExtSourceMacAddr,
       "ruijieAceExtIfAnyDestIp": ruijieAceExtIfAnyDestIp,
       "ruijieAceExtDestIp": ruijieAceExtDestIp,
       "ruijieAceExtIfAnyDestWildCard": ruijieAceExtIfAnyDestWildCard,
       "ruijieAceExtDestIpWildCard": ruijieAceExtDestIpWildCard,
       "ruijieAceExtIfAnyDestMacAddr": ruijieAceExtIfAnyDestMacAddr,
       "ruijieAceExtDestMacAddr": ruijieAceExtDestMacAddr,
       "ruijieAceExtIfAnyEtherLikeType": ruijieAceExtIfAnyEtherLikeType,
       "ruijieAceExtEtherLikeType": ruijieAceExtEtherLikeType,
       "ruijieAceExtIfAnyIpProtocolField": ruijieAceExtIfAnyIpProtocolField,
       "ruijieAceExtIpProtocolField": ruijieAceExtIpProtocolField,
       "ruijieAceExtSourceProtocolPort": ruijieAceExtSourceProtocolPort,
       "ruijieAceExtDestProtocolPort": ruijieAceExtDestProtocolPort,
       "ruijieAceExtIfAnyProtocolType": ruijieAceExtIfAnyProtocolType,
       "ruijieAceExtProtocolType": ruijieAceExtProtocolType,
       "ruijieAceExtFlowAction": ruijieAceExtFlowAction,
       "ruijieAceExtEntryStauts": ruijieAceExtEntryStauts,
       "ruijieAceExtTimeRangeName": ruijieAceExtTimeRangeName,
       "ruijieAceExtSourcePortOp": ruijieAceExtSourcePortOp,
       "ruijieAceExtSourceProtocolPortRange": ruijieAceExtSourceProtocolPortRange,
       "ruijieAceExtDestPortOp": ruijieAceExtDestPortOp,
       "ruijieAceExtDestProtocolPortRange": ruijieAceExtDestProtocolPortRange,
       "ruijieAceExtIfAnyCos": ruijieAceExtIfAnyCos,
       "ruijieAceExtCos": ruijieAceExtCos,
       "ruijieAceExtIfAnyIpPrec": ruijieAceExtIfAnyIpPrec,
       "ruijieAceExtIpPrec": ruijieAceExtIpPrec,
       "ruijieAceExtIfAnyDscp": ruijieAceExtIfAnyDscp,
       "ruijieAceExtDscp": ruijieAceExtDscp,
       "ruijieAceExtIfAnyTcpFlag": ruijieAceExtIfAnyTcpFlag,
       "ruijieAceExtTcpFlag": ruijieAceExtTcpFlag,
       "ruijieAceExtIfAnySourceMacAddrWildCard": ruijieAceExtIfAnySourceMacAddrWildCard,
       "ruijieAceExtSourceMacAddrWildCard": ruijieAceExtSourceMacAddrWildCard,
       "ruijieAceExtIfAnyDestMacAddrWildCard": ruijieAceExtIfAnyDestMacAddrWildCard,
       "ruijieAceExtDestMacAddrWildCard": ruijieAceExtDestMacAddrWildCard,
       "ruijieAceExtIfAnySourceIp6": ruijieAceExtIfAnySourceIp6,
       "ruijieAceExtSourceIp6": ruijieAceExtSourceIp6,
       "ruijieAceExtIfAnySourceIp6WildCard": ruijieAceExtIfAnySourceIp6WildCard,
       "ruijieAceExtSourceIp6WildCard": ruijieAceExtSourceIp6WildCard,
       "ruijieAceExtIfAnyDestIp6": ruijieAceExtIfAnyDestIp6,
       "ruijieAceExtDestIp6": ruijieAceExtDestIp6,
       "ruijieAceExtIfAnyDestIp6WildCard": ruijieAceExtIfAnyDestIp6WildCard,
       "ruijieAceExtDestIp6WildCard": ruijieAceExtDestIp6WildCard,
       "ruijieAclMIBConformance": ruijieAclMIBConformance,
       "ruijieAclMIBCompliances": ruijieAclMIBCompliances,
       "ruijieAclMIBCompliance": ruijieAclMIBCompliance,
       "ruijieAclMIBGroups": ruijieAclMIBGroups,
       "ruijieAclMIBGroup": ruijieAclMIBGroup}
)
