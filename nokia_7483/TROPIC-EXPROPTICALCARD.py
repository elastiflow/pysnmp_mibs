# SNMP MIB module (TROPIC-EXPROPTICALCARD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-EXPROPTICALCARD.mib
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tnExprOpticalCardMIB,
 tropicExprModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnExprOpticalCardMIB",
    "tropicExprModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(TropicAdminStateType,) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TropicAdminStateType")

(tnDirection,) = mibBuilder.importSymbols(
    "TROPIC-WAVEKEY-MIB",
    "tnDirection")


# MODULE-IDENTITY

tnExprOpticalCardMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tnExprOpticalCardMibModule.setRevisions(
        ("2009-09-25 12:00",
         "2009-11-01 12:00",
         "2009-12-10 12:00",
         "2010-01-04 12:00",
         "2010-01-24 12:00",
         "2010-02-17 12:00",
         "2010-03-24 12:00",
         "2010-04-16 12:00",
         "2010-05-10 12:00",
         "2010-06-04 12:00",
         "2010-06-28 12:00",
         "2010-07-20 12:00",
         "2010-08-02 12:00",
         "2010-08-09 12:00",
         "2010-09-10 12:00",
         "2010-09-20 12:00",
         "2010-09-24 12:00",
         "2010-09-28 12:00",
         "2010-10-17 12:00",
         "2010-10-19 12:00",
         "2010-11-10 12:00",
         "2011-05-04 12:00",
         "2011-05-17 12:00",
         "2011-06-07 12:00",
         "2011-06-13 12:00",
         "2011-06-30 12:00",
         "2011-07-07 12:00",
         "2011-07-19 12:00",
         "2011-08-31 12:00",
         "2011-09-06 12:00",
         "2011-09-16 12:00",
         "2011-11-14 12:00",
         "2011-11-21 12:00",
         "2012-01-10 12:00",
         "2012-01-18 12:00",
         "2012-01-19 12:00",
         "2012-03-18 12:00",
         "2012-03-29 12:00",
         "2012-04-24 12:00",
         "2012-04-27 12:00",
         "2012-05-01 12:00",
         "2012-06-18 12:00",
         "2012-07-24 12:00",
         "2012-08-28 12:00",
         "2012-10-12 12:00",
         "2013-01-24 12:00",
         "2013-02-21 12:00",
         "2013-03-07 12:00",
         "2013-03-16 12:00",
         "2013-04-11 12:00",
         "2013-04-19 12:00",
         "2013-05-21 12:00",
         "2013-05-24 12:00",
         "2013-06-24 12:00",
         "2013-08-12 12:00",
         "2013-09-04 12:00",
         "2013-10-07 12:00",
         "2013-10-10 12:00",
         "2013-11-25 12:00",
         "2014-02-19 12:00",
         "2014-05-06 12:00",
         "2014-05-18 12:00",
         "2014-06-20 12:00",
         "2014-07-07 12:00",
         "2014-08-08 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnExprOpticalCardConf_ObjectIdentity = ObjectIdentity
tnExprOpticalCardConf = _TnExprOpticalCardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 1)
)
_TnExprOpticalCardGroups_ObjectIdentity = ObjectIdentity
tnExprOpticalCardGroups = _TnExprOpticalCardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 1, 1)
)
_TnExprOpticalCardCompliances_ObjectIdentity = ObjectIdentity
tnExprOpticalCardCompliances = _TnExprOpticalCardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 1, 2)
)
_TnExprOpticalCardObjs_ObjectIdentity = ObjectIdentity
tnExprOpticalCardObjs = _TnExprOpticalCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2)
)
_TnExprCardTable_Object = MibTable
tnExprCardTable = _TnExprCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnExprCardTable.setStatus("current")
_TnExprCardEntry_Object = MibTableRow
tnExprCardEntry = _TnExprCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1)
)
tnExprCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnExprCardEntry.setStatus("current")
_TnDcmCardDummy_Type = Integer32
_TnDcmCardDummy_Object = MibTableColumn
tnDcmCardDummy = _TnDcmCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 1),
    _TnDcmCardDummy_Type()
)
tnDcmCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardDummy.setStatus("current")
_TnOpsaCardDummy_Type = Integer32
_TnOpsaCardDummy_Object = MibTableColumn
tnOpsaCardDummy = _TnOpsaCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 2),
    _TnOpsaCardDummy_Type()
)
tnOpsaCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpsaCardDummy.setStatus("current")
_Tn11stmm10CardDummy_Type = Integer32
_Tn11stmm10CardDummy_Object = MibTableColumn
tn11stmm10CardDummy = _Tn11stmm10CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 3),
    _Tn11stmm10CardDummy_Type()
)
tn11stmm10CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11stmm10CardDummy.setStatus("current")
_Tn11star1CardDummy_Type = Integer32
_Tn11star1CardDummy_Object = MibTableColumn
tn11star1CardDummy = _Tn11star1CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 4),
    _Tn11star1CardDummy_Type()
)
tn11star1CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11star1CardDummy.setStatus("current")
_TnAhphgCardDummy_Type = Integer32
_TnAhphgCardDummy_Object = MibTableColumn
tnAhphgCardDummy = _TnAhphgCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 5),
    _TnAhphgCardDummy_Type()
)
tnAhphgCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAhphgCardDummy.setStatus("current")
_TnAlphgCardDummy_Type = Integer32
_TnAlphgCardDummy_Object = MibTableColumn
tnAlphgCardDummy = _TnAlphgCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 6),
    _TnAlphgCardDummy_Type()
)
tnAlphgCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAlphgCardDummy.setStatus("current")
_TnCwr8CardDummy_Type = Integer32
_TnCwr8CardDummy_Object = MibTableColumn
tnCwr8CardDummy = _TnCwr8CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 7),
    _TnCwr8CardDummy_Type()
)
tnCwr8CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCwr8CardDummy.setStatus("current")
_Tn11stge12CardDummy_Type = Integer32
_Tn11stge12CardDummy_Object = MibTableColumn
tn11stge12CardDummy = _Tn11stge12CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 8),
    _Tn11stge12CardDummy_Type()
)
tn11stge12CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11stge12CardDummy.setStatus("current")
_Tn11dpge12CardDummy_Type = Integer32
_Tn11dpge12CardDummy_Object = MibTableColumn
tn11dpge12CardDummy = _Tn11dpge12CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 9),
    _Tn11dpge12CardDummy_Type()
)
tn11dpge12CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11dpge12CardDummy.setStatus("current")
_TnSfd44CardDummy_Type = Integer32
_TnSfd44CardDummy_Object = MibTableColumn
tnSfd44CardDummy = _TnSfd44CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 10),
    _TnSfd44CardDummy_Type()
)
tnSfd44CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd44CardDummy.setStatus("current")
_TnPowerFilterCardDummy_Type = Integer32
_TnPowerFilterCardDummy_Object = MibTableColumn
tnPowerFilterCardDummy = _TnPowerFilterCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 11),
    _TnPowerFilterCardDummy_Type()
)
tnPowerFilterCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerFilterCardDummy.setStatus("current")
_TnSvacCardDummy_Type = Integer32
_TnSvacCardDummy_Object = MibTableColumn
tnSvacCardDummy = _TnSvacCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 12),
    _TnSvacCardDummy_Type()
)
tnSvacCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvacCardDummy.setStatus("current")
_TnSfd5aCardDummy_Type = Integer32
_TnSfd5aCardDummy_Object = MibTableColumn
tnSfd5aCardDummy = _TnSfd5aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 13),
    _TnSfd5aCardDummy_Type()
)
tnSfd5aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5aCardDummy.setStatus("current")
_TnSfd5bCardDummy_Type = Integer32
_TnSfd5bCardDummy_Object = MibTableColumn
tnSfd5bCardDummy = _TnSfd5bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 14),
    _TnSfd5bCardDummy_Type()
)
tnSfd5bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5bCardDummy.setStatus("current")
_TnSfd5cCardDummy_Type = Integer32
_TnSfd5cCardDummy_Object = MibTableColumn
tnSfd5cCardDummy = _TnSfd5cCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 15),
    _TnSfd5cCardDummy_Type()
)
tnSfd5cCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5cCardDummy.setStatus("current")
_TnSfd5dCardDummy_Type = Integer32
_TnSfd5dCardDummy_Object = MibTableColumn
tnSfd5dCardDummy = _TnSfd5dCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 16),
    _TnSfd5dCardDummy_Type()
)
tnSfd5dCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5dCardDummy.setStatus("current")
_TnSfd5eCardDummy_Type = Integer32
_TnSfd5eCardDummy_Object = MibTableColumn
tnSfd5eCardDummy = _TnSfd5eCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 17),
    _TnSfd5eCardDummy_Type()
)
tnSfd5eCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5eCardDummy.setStatus("current")
_TnSfd5fCardDummy_Type = Integer32
_TnSfd5fCardDummy_Object = MibTableColumn
tnSfd5fCardDummy = _TnSfd5fCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 18),
    _TnSfd5fCardDummy_Type()
)
tnSfd5fCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5fCardDummy.setStatus("current")
_TnSfd5gCardDummy_Type = Integer32
_TnSfd5gCardDummy_Object = MibTableColumn
tnSfd5gCardDummy = _TnSfd5gCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 19),
    _TnSfd5gCardDummy_Type()
)
tnSfd5gCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5gCardDummy.setStatus("current")
_TnSfd5hCardDummy_Type = Integer32
_TnSfd5hCardDummy_Object = MibTableColumn
tnSfd5hCardDummy = _TnSfd5hCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 20),
    _TnSfd5hCardDummy_Type()
)
tnSfd5hCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5hCardDummy.setStatus("current")
_TnSfd10aCardDummy_Type = Integer32
_TnSfd10aCardDummy_Object = MibTableColumn
tnSfd10aCardDummy = _TnSfd10aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 21),
    _TnSfd10aCardDummy_Type()
)
tnSfd10aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10aCardDummy.setStatus("current")
_TnSfd10bCardDummy_Type = Integer32
_TnSfd10bCardDummy_Object = MibTableColumn
tnSfd10bCardDummy = _TnSfd10bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 22),
    _TnSfd10bCardDummy_Type()
)
tnSfd10bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10bCardDummy.setStatus("current")
_TnSfd10cCardDummy_Type = Integer32
_TnSfd10cCardDummy_Object = MibTableColumn
tnSfd10cCardDummy = _TnSfd10cCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 23),
    _TnSfd10cCardDummy_Type()
)
tnSfd10cCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10cCardDummy.setStatus("current")
_TnSfd10dCardDummy_Type = Integer32
_TnSfd10dCardDummy_Object = MibTableColumn
tnSfd10dCardDummy = _TnSfd10dCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 24),
    _TnSfd10dCardDummy_Type()
)
tnSfd10dCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10dCardDummy.setStatus("current")
_TnSfc2aCardDummy_Type = Integer32
_TnSfc2aCardDummy_Object = MibTableColumn
tnSfc2aCardDummy = _TnSfc2aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 25),
    _TnSfc2aCardDummy_Type()
)
tnSfc2aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc2aCardDummy.setStatus("current")
_TnSfc2bCardDummy_Type = Integer32
_TnSfc2bCardDummy_Object = MibTableColumn
tnSfc2bCardDummy = _TnSfc2bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 26),
    _TnSfc2bCardDummy_Type()
)
tnSfc2bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc2bCardDummy.setStatus("current")
_TnSfc2cCardDummy_Type = Integer32
_TnSfc2cCardDummy_Object = MibTableColumn
tnSfc2cCardDummy = _TnSfc2cCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 27),
    _TnSfc2cCardDummy_Type()
)
tnSfc2cCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc2cCardDummy.setStatus("current")
_TnSfc2dCardDummy_Type = Integer32
_TnSfc2dCardDummy_Object = MibTableColumn
tnSfc2dCardDummy = _TnSfc2dCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 28),
    _TnSfc2dCardDummy_Type()
)
tnSfc2dCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc2dCardDummy.setStatus("current")
_TnSfc4aCardDummy_Type = Integer32
_TnSfc4aCardDummy_Object = MibTableColumn
tnSfc4aCardDummy = _TnSfc4aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 29),
    _TnSfc4aCardDummy_Type()
)
tnSfc4aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc4aCardDummy.setStatus("current")
_TnSfc4bCardDummy_Type = Integer32
_TnSfc4bCardDummy_Object = MibTableColumn
tnSfc4bCardDummy = _TnSfc4bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 30),
    _TnSfc4bCardDummy_Type()
)
tnSfc4bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc4bCardDummy.setStatus("current")
_TnSfc8CardDummy_Type = Integer32
_TnSfc8CardDummy_Object = MibTableColumn
tnSfc8CardDummy = _TnSfc8CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 31),
    _TnSfc8CardDummy_Type()
)
tnSfc8CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc8CardDummy.setStatus("current")
_TnSfc1aCardDummy_Type = Integer32
_TnSfc1aCardDummy_Object = MibTableColumn
tnSfc1aCardDummy = _TnSfc1aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 32),
    _TnSfc1aCardDummy_Type()
)
tnSfc1aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc1aCardDummy.setStatus("current")
_TnSfc1bCardDummy_Type = Integer32
_TnSfc1bCardDummy_Object = MibTableColumn
tnSfc1bCardDummy = _TnSfc1bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 33),
    _TnSfc1bCardDummy_Type()
)
tnSfc1bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc1bCardDummy.setStatus("current")
_TnSfc1cCardDummy_Type = Integer32
_TnSfc1cCardDummy_Object = MibTableColumn
tnSfc1cCardDummy = _TnSfc1cCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 34),
    _TnSfc1cCardDummy_Type()
)
tnSfc1cCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc1cCardDummy.setStatus("current")
_TnSfc1dCardDummy_Type = Integer32
_TnSfc1dCardDummy_Object = MibTableColumn
tnSfc1dCardDummy = _TnSfc1dCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 35),
    _TnSfc1dCardDummy_Type()
)
tnSfc1dCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc1dCardDummy.setStatus("current")
_TnSfc1eCardDummy_Type = Integer32
_TnSfc1eCardDummy_Object = MibTableColumn
tnSfc1eCardDummy = _TnSfc1eCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 36),
    _TnSfc1eCardDummy_Type()
)
tnSfc1eCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc1eCardDummy.setStatus("current")
_TnSfc1fCardDummy_Type = Integer32
_TnSfc1fCardDummy_Object = MibTableColumn
tnSfc1fCardDummy = _TnSfc1fCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 37),
    _TnSfc1fCardDummy_Type()
)
tnSfc1fCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc1fCardDummy.setStatus("current")
_TnSfc1gCardDummy_Type = Integer32
_TnSfc1gCardDummy_Object = MibTableColumn
tnSfc1gCardDummy = _TnSfc1gCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 38),
    _TnSfc1gCardDummy_Type()
)
tnSfc1gCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc1gCardDummy.setStatus("current")
_TnSfc1hCardDummy_Type = Integer32
_TnSfc1hCardDummy_Object = MibTableColumn
tnSfc1hCardDummy = _TnSfc1hCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 39),
    _TnSfc1hCardDummy_Type()
)
tnSfc1hCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfc1hCardDummy.setStatus("current")
_Tn4dpa4CardDummy_Type = Integer32
_Tn4dpa4CardDummy_Object = MibTableColumn
tn4dpa4CardDummy = _Tn4dpa4CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 40),
    _Tn4dpa4CardDummy_Type()
)
tn4dpa4CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn4dpa4CardDummy.setStatus("current")
_TnCwr8c88CardDummy_Type = Integer32
_TnCwr8c88CardDummy_Object = MibTableColumn
tnCwr8c88CardDummy = _TnCwr8c88CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 41),
    _TnCwr8c88CardDummy_Type()
)
tnCwr8c88CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCwr8c88CardDummy.setStatus("current")
_TnSfd44bCardDummy_Type = Integer32
_TnSfd44bCardDummy_Object = MibTableColumn
tnSfd44bCardDummy = _TnSfd44bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 42),
    _TnSfd44bCardDummy_Type()
)
tnSfd44bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd44bCardDummy.setStatus("current")
_TnItlbCardDummy_Type = Integer32
_TnItlbCardDummy_Object = MibTableColumn
tnItlbCardDummy = _TnItlbCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 43),
    _TnItlbCardDummy_Type()
)
tnItlbCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnItlbCardDummy.setStatus("current")
_TnAhplgCardDummy_Type = Integer32
_TnAhplgCardDummy_Object = MibTableColumn
tnAhplgCardDummy = _TnAhplgCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 44),
    _TnAhplgCardDummy_Type()
)
tnAhplgCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAhplgCardDummy.setStatus("current")
_Tn43stx4CardDummy_Type = Integer32
_Tn43stx4CardDummy_Object = MibTableColumn
tn43stx4CardDummy = _Tn43stx4CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 45),
    _Tn43stx4CardDummy_Type()
)
tn43stx4CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn43stx4CardDummy.setStatus("current")
_TnAlpfgkCardDummy_Type = Integer32
_TnAlpfgkCardDummy_Object = MibTableColumn
tnAlpfgkCardDummy = _TnAlpfgkCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 46),
    _TnAlpfgkCardDummy_Type()
)
tnAlpfgkCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAlpfgkCardDummy.setStatus("current")
_TnOscCardDummy_Type = Integer32
_TnOscCardDummy_Object = MibTableColumn
tnOscCardDummy = _TnOscCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 47),
    _TnOscCardDummy_Type()
)
tnOscCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOscCardDummy.setStatus("current")
_Tn4dpa2CardDummy_Type = Integer32
_Tn4dpa2CardDummy_Object = MibTableColumn
tn4dpa2CardDummy = _Tn4dpa2CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 48),
    _Tn4dpa2CardDummy_Type()
)
tn4dpa2CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn4dpa2CardDummy.setStatus("current")
_TnSfd8aCardDummy_Type = Integer32
_TnSfd8aCardDummy_Object = MibTableColumn
tnSfd8aCardDummy = _TnSfd8aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 49),
    _TnSfd8aCardDummy_Type()
)
tnSfd8aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd8aCardDummy.setStatus("current")
_TnSfd8bCardDummy_Type = Integer32
_TnSfd8bCardDummy_Object = MibTableColumn
tnSfd8bCardDummy = _TnSfd8bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 50),
    _TnSfd8bCardDummy_Type()
)
tnSfd8bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd8bCardDummy.setStatus("current")
_TnSfd8cCardDummy_Type = Integer32
_TnSfd8cCardDummy_Object = MibTableColumn
tnSfd8cCardDummy = _TnSfd8cCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 51),
    _TnSfd8cCardDummy_Type()
)
tnSfd8cCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd8cCardDummy.setStatus("current")
_TnSfd8dCardDummy_Type = Integer32
_TnSfd8dCardDummy_Object = MibTableColumn
tnSfd8dCardDummy = _TnSfd8dCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 52),
    _TnSfd8dCardDummy_Type()
)
tnSfd8dCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd8dCardDummy.setStatus("current")
_Tn43sta1pCardDummy_Type = Integer32
_Tn43sta1pCardDummy_Object = MibTableColumn
tn43sta1pCardDummy = _Tn43sta1pCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 53),
    _Tn43sta1pCardDummy_Type()
)
tn43sta1pCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn43sta1pCardDummy.setStatus("current")
_Tn43stx4pCardDummy_Type = Integer32
_Tn43stx4pCardDummy_Object = MibTableColumn
tn43stx4pCardDummy = _Tn43stx4pCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 54),
    _Tn43stx4pCardDummy_Type()
)
tn43stx4pCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn43stx4pCardDummy.setStatus("current")
_Tn11qpa4CardDummy_Type = Integer32
_Tn11qpa4CardDummy_Object = MibTableColumn
tn11qpa4CardDummy = _Tn11qpa4CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 63),
    _Tn11qpa4CardDummy_Type()
)
tn11qpa4CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11qpa4CardDummy.setStatus("current")
_TnSfd40CardDummy_Type = Integer32
_TnSfd40CardDummy_Object = MibTableColumn
tnSfd40CardDummy = _TnSfd40CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 64),
    _TnSfd40CardDummy_Type()
)
tnSfd40CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd40CardDummy.setStatus("current")
_TnSfd40bCardDummy_Type = Integer32
_TnSfd40bCardDummy_Object = MibTableColumn
tnSfd40bCardDummy = _TnSfd40bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 65),
    _TnSfd40bCardDummy_Type()
)
tnSfd40bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd40bCardDummy.setStatus("current")
_TnA2325aCardDummy_Type = Integer32
_TnA2325aCardDummy_Object = MibTableColumn
tnA2325aCardDummy = _TnA2325aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 66),
    _TnA2325aCardDummy_Type()
)
tnA2325aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnA2325aCardDummy.setStatus("current")
_Tn112scx10CardDummy_Type = Integer32
_Tn112scx10CardDummy_Object = MibTableColumn
tn112scx10CardDummy = _Tn112scx10CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 67),
    _Tn112scx10CardDummy_Type()
)
tn112scx10CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112scx10CardDummy.setStatus("current")
_Tn112sca1CardDummy_Type = Integer32
_Tn112sca1CardDummy_Object = MibTableColumn
tn112sca1CardDummy = _Tn112sca1CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 68),
    _Tn112sca1CardDummy_Type()
)
tn112sca1CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112sca1CardDummy.setStatus("current")
_TnAlpfgtCardDummy_Type = Integer32
_TnAlpfgtCardDummy_Object = MibTableColumn
tnAlpfgtCardDummy = _TnAlpfgtCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 69),
    _TnAlpfgtCardDummy_Type()
)
tnAlpfgtCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAlpfgtCardDummy.setStatus("current")
_TnOsctCardDummy_Type = Integer32
_TnOsctCardDummy_Object = MibTableColumn
tnOsctCardDummy = _TnOsctCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 70),
    _TnOsctCardDummy_Type()
)
tnOsctCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOsctCardDummy.setStatus("current")
_TnWtocmCardDummy_Type = Integer32
_TnWtocmCardDummy_Object = MibTableColumn
tnWtocmCardDummy = _TnWtocmCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 71),
    _TnWtocmCardDummy_Type()
)
tnWtocmCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmCardDummy.setStatus("current")
_TnWr2c88CardDummy_Type = Integer32
_TnWr2c88CardDummy_Object = MibTableColumn
tnWr2c88CardDummy = _TnWr2c88CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 72),
    _TnWr2c88CardDummy_Type()
)
tnWr2c88CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWr2c88CardDummy.setStatus("current")
_TnAm2017bCardDummy_Type = Integer32
_TnAm2017bCardDummy_Object = MibTableColumn
tnAm2017bCardDummy = _TnAm2017bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 73),
    _TnAm2017bCardDummy_Type()
)
tnAm2017bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAm2017bCardDummy.setStatus("current")
_TnAm2325bCardDummy_Type = Integer32
_TnAm2325bCardDummy_Object = MibTableColumn
tnAm2325bCardDummy = _TnAm2325bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 74),
    _TnAm2325bCardDummy_Type()
)
tnAm2325bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAm2325bCardDummy.setStatus("current")
_Tn1dpp21CardDummy_Type = Integer32
_Tn1dpp21CardDummy_Object = MibTableColumn
tn1dpp21CardDummy = _Tn1dpp21CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 75),
    _Tn1dpp21CardDummy_Type()
)
tn1dpp21CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn1dpp21CardDummy.setStatus("current")
_TnSfd4aCardDummy_Type = Integer32
_TnSfd4aCardDummy_Object = MibTableColumn
tnSfd4aCardDummy = _TnSfd4aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 76),
    _TnSfd4aCardDummy_Type()
)
tnSfd4aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd4aCardDummy.setStatus("current")
_TnSfd4bCardDummy_Type = Integer32
_TnSfd4bCardDummy_Object = MibTableColumn
tnSfd4bCardDummy = _TnSfd4bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 77),
    _TnSfd4bCardDummy_Type()
)
tnSfd4bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd4bCardDummy.setStatus("current")
_TnSfd4cCardDummy_Type = Integer32
_TnSfd4cCardDummy_Object = MibTableColumn
tnSfd4cCardDummy = _TnSfd4cCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 78),
    _TnSfd4cCardDummy_Type()
)
tnSfd4cCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd4cCardDummy.setStatus("current")
_TnSfd4dCardDummy_Type = Integer32
_TnSfd4dCardDummy_Object = MibTableColumn
tnSfd4dCardDummy = _TnSfd4dCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 79),
    _TnSfd4dCardDummy_Type()
)
tnSfd4dCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd4dCardDummy.setStatus("current")
_TnSfd4eCardDummy_Type = Integer32
_TnSfd4eCardDummy_Object = MibTableColumn
tnSfd4eCardDummy = _TnSfd4eCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 80),
    _TnSfd4eCardDummy_Type()
)
tnSfd4eCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd4eCardDummy.setStatus("current")
_TnSfd4fCardDummy_Type = Integer32
_TnSfd4fCardDummy_Object = MibTableColumn
tnSfd4fCardDummy = _TnSfd4fCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 81),
    _TnSfd4fCardDummy_Type()
)
tnSfd4fCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd4fCardDummy.setStatus("current")
_TnSfd4gCardDummy_Type = Integer32
_TnSfd4gCardDummy_Object = MibTableColumn
tnSfd4gCardDummy = _TnSfd4gCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 82),
    _TnSfd4gCardDummy_Type()
)
tnSfd4gCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd4gCardDummy.setStatus("current")
_TnSfd4hCardDummy_Type = Integer32
_TnSfd4hCardDummy_Object = MibTableColumn
tnSfd4hCardDummy = _TnSfd4hCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 83),
    _TnSfd4hCardDummy_Type()
)
tnSfd4hCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd4hCardDummy.setStatus("current")
_TnMvacCardDummy_Type = Integer32
_TnMvacCardDummy_Object = MibTableColumn
tnMvacCardDummy = _TnMvacCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 84),
    _TnMvacCardDummy_Type()
)
tnMvacCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMvacCardDummy.setStatus("current")
_TnBusTerminationCardDummy_Type = Integer32
_TnBusTerminationCardDummy_Object = MibTableColumn
tnBusTerminationCardDummy = _TnBusTerminationCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 85),
    _TnBusTerminationCardDummy_Type()
)
tnBusTerminationCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBusTerminationCardDummy.setStatus("current")
_TnFirstLevelControllerCardDummy_Type = Integer32
_TnFirstLevelControllerCardDummy_Object = MibTableColumn
tnFirstLevelControllerCardDummy = _TnFirstLevelControllerCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 86),
    _TnFirstLevelControllerCardDummy_Type()
)
tnFirstLevelControllerCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFirstLevelControllerCardDummy.setStatus("current")
_TnMatrix3T8CardDummy_Type = Integer32
_TnMatrix3T8CardDummy_Object = MibTableColumn
tnMatrix3T8CardDummy = _TnMatrix3T8CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 88),
    _TnMatrix3T8CardDummy_Type()
)
tnMatrix3T8CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMatrix3T8CardDummy.setStatus("current")
_TnMatrix1T9CardDummy_Type = Integer32
_TnMatrix1T9CardDummy_Object = MibTableColumn
tnMatrix1T9CardDummy = _TnMatrix1T9CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 89),
    _TnMatrix1T9CardDummy_Type()
)
tnMatrix1T9CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMatrix1T9CardDummy.setStatus("current")
_TnMatrix0CompactCardDummy_Type = Integer32
_TnMatrix0CompactCardDummy_Object = MibTableColumn
tnMatrix0CompactCardDummy = _TnMatrix0CompactCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 91),
    _TnMatrix0CompactCardDummy_Type()
)
tnMatrix0CompactCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMatrix0CompactCardDummy.setStatus("current")
_Tn43scx4CardDummy_Type = Integer32
_Tn43scx4CardDummy_Object = MibTableColumn
tn43scx4CardDummy = _Tn43scx4CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 92),
    _Tn43scx4CardDummy_Type()
)
tn43scx4CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn43scx4CardDummy.setStatus("current")
_TnRa2pCardDummy_Type = Integer32
_TnRa2pCardDummy_Object = MibTableColumn
tnRa2pCardDummy = _TnRa2pCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 93),
    _TnRa2pCardDummy_Type()
)
tnRa2pCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRa2pCardDummy.setStatus("current")
_TnAm2318aCardDummy_Type = Integer32
_TnAm2318aCardDummy_Object = MibTableColumn
tnAm2318aCardDummy = _TnAm2318aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 94),
    _TnAm2318aCardDummy_Type()
)
tnAm2318aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAm2318aCardDummy.setStatus("current")
_TnAm2125aCardDummy_Type = Integer32
_TnAm2125aCardDummy_Object = MibTableColumn
tnAm2125aCardDummy = _TnAm2125aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 95),
    _TnAm2125aCardDummy_Type()
)
tnAm2125aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAm2125aCardDummy.setStatus("current")
_TnItluCardDummy_Type = Integer32
_TnItluCardDummy_Object = MibTableColumn
tnItluCardDummy = _TnItluCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 96),
    _TnItluCardDummy_Type()
)
tnItluCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnItluCardDummy.setStatus("current")
_TnWr8c88aCardDummy_Type = Integer32
_TnWr8c88aCardDummy_Object = MibTableColumn
tnWr8c88aCardDummy = _TnWr8c88aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 97),
    _TnWr8c88aCardDummy_Type()
)
tnWr8c88aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWr8c88aCardDummy.setStatus("current")
_TnBusTerminationOnlyCardDummy_Type = Integer32
_TnBusTerminationOnlyCardDummy_Object = MibTableColumn
tnBusTerminationOnlyCardDummy = _TnBusTerminationOnlyCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 98),
    _TnBusTerminationOnlyCardDummy_Type()
)
tnBusTerminationOnlyCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBusTerminationOnlyCardDummy.setStatus("current")
_Tn11dpe12eCardDummy_Type = Integer32
_Tn11dpe12eCardDummy_Object = MibTableColumn
tn11dpe12eCardDummy = _Tn11dpe12eCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 99),
    _Tn11dpe12eCardDummy_Type()
)
tn11dpe12eCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11dpe12eCardDummy.setStatus("current")
_Tn112sx10lCardDummy_Type = Integer32
_Tn112sx10lCardDummy_Object = MibTableColumn
tn112sx10lCardDummy = _Tn112sx10lCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 100),
    _Tn112sx10lCardDummy_Type()
)
tn112sx10lCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112sx10lCardDummy.setStatus("current")
_Tn112sa1lCardDummy_Type = Integer32
_Tn112sa1lCardDummy_Object = MibTableColumn
tn112sa1lCardDummy = _Tn112sa1lCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 101),
    _Tn112sa1lCardDummy_Type()
)
tn112sa1lCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112sa1lCardDummy.setStatus("current")
_Tn11dpm12CardDummy_Type = Integer32
_Tn11dpm12CardDummy_Object = MibTableColumn
tn11dpm12CardDummy = _Tn11dpm12CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 102),
    _Tn11dpm12CardDummy_Type()
)
tn11dpm12CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11dpm12CardDummy.setStatus("current")
_TnMesh4CardDummy_Type = Integer32
_TnMesh4CardDummy_Object = MibTableColumn
tnMesh4CardDummy = _TnMesh4CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 103),
    _TnMesh4CardDummy_Type()
)
tnMesh4CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMesh4CardDummy.setStatus("current")
_Tn43sca1CardDummy_Type = Integer32
_Tn43sca1CardDummy_Object = MibTableColumn
tn43sca1CardDummy = _Tn43sca1CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 104),
    _Tn43sca1CardDummy_Type()
)
tn43sca1CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn43sca1CardDummy.setStatus("current")
_Tn43scx4lCardDummy_Type = Integer32
_Tn43scx4lCardDummy_Object = MibTableColumn
tn43scx4lCardDummy = _Tn43scx4lCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 105),
    _Tn43scx4lCardDummy_Type()
)
tn43scx4lCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn43scx4lCardDummy.setStatus("current")
_TnAm2125bCardDummy_Type = Integer32
_TnAm2125bCardDummy_Object = MibTableColumn
tnAm2125bCardDummy = _TnAm2125bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 106),
    _TnAm2125bCardDummy_Type()
)
tnAm2125bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAm2125bCardDummy.setStatus("current")
_TnUniversalMatrixFirstLevelControllerCardDummy_Type = Integer32
_TnUniversalMatrixFirstLevelControllerCardDummy_Object = MibTableColumn
tnUniversalMatrixFirstLevelControllerCardDummy = _TnUniversalMatrixFirstLevelControllerCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 107),
    _TnUniversalMatrixFirstLevelControllerCardDummy_Type()
)
tnUniversalMatrixFirstLevelControllerCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUniversalMatrixFirstLevelControllerCardDummy.setStatus("current")
_TnEndOfShelfMiddleCardDummy_Type = Integer32
_TnEndOfShelfMiddleCardDummy_Object = MibTableColumn
tnEndOfShelfMiddleCardDummy = _TnEndOfShelfMiddleCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 109),
    _TnEndOfShelfMiddleCardDummy_Type()
)
tnEndOfShelfMiddleCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEndOfShelfMiddleCardDummy.setStatus("current")
_Tn112snx10CardDummy_Type = Integer32
_Tn112snx10CardDummy_Object = MibTableColumn
tn112snx10CardDummy = _Tn112snx10CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 111),
    _Tn112snx10CardDummy_Type()
)
tn112snx10CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112snx10CardDummy.setStatus("current")
_Tn112sna1CardDummy_Type = Integer32
_Tn112sna1CardDummy_Object = MibTableColumn
tn112sna1CardDummy = _Tn112sna1CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 112),
    _Tn112sna1CardDummy_Type()
)
tn112sna1CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112sna1CardDummy.setStatus("current")
_Tn1dpp24mCardDummy_Type = Integer32
_Tn1dpp24mCardDummy_Object = MibTableColumn
tn1dpp24mCardDummy = _Tn1dpp24mCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 114),
    _Tn1dpp24mCardDummy_Type()
)
tn1dpp24mCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn1dpp24mCardDummy.setStatus("current")
_Tnul43scupCardDummy_Type = Integer32
_Tnul43scupCardDummy_Object = MibTableColumn
tnul43scupCardDummy = _Tnul43scupCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 115),
    _Tnul43scupCardDummy_Type()
)
tnul43scupCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnul43scupCardDummy.setStatus("current")
_Tnul11qcupCardDummy_Type = Integer32
_Tnul11qcupCardDummy_Object = MibTableColumn
tnul11qcupCardDummy = _Tnul11qcupCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 116),
    _Tnul11qcupCardDummy_Type()
)
tnul11qcupCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnul11qcupCardDummy.setStatus("current")
_Tn11qpen4CardDummy_Type = Integer32
_Tn11qpen4CardDummy_Object = MibTableColumn
tn11qpen4CardDummy = _Tn11qpen4CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 117),
    _Tn11qpen4CardDummy_Type()
)
tn11qpen4CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11qpen4CardDummy.setStatus("current")
_Tn43scx4eCardDummy_Type = Integer32
_Tn43scx4eCardDummy_Object = MibTableColumn
tn43scx4eCardDummy = _Tn43scx4eCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 118),
    _Tn43scx4eCardDummy_Type()
)
tn43scx4eCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn43scx4eCardDummy.setStatus("current")
_Tn43scge1CardDummy_Type = Integer32
_Tn43scge1CardDummy_Object = MibTableColumn
tn43scge1CardDummy = _Tn43scge1CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 119),
    _Tn43scge1CardDummy_Type()
)
tn43scge1CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn43scge1CardDummy.setStatus("current")
_Tn11qpe24CardDummy_Type = Integer32
_Tn11qpe24CardDummy_Object = MibTableColumn
tn11qpe24CardDummy = _Tn11qpe24CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 120),
    _Tn11qpe24CardDummy_Type()
)
tn11qpe24CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11qpe24CardDummy.setStatus("current")
_Tn11star1aCardDummy_Type = Integer32
_Tn11star1aCardDummy_Object = MibTableColumn
tn11star1aCardDummy = _Tn11star1aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 121),
    _Tn11star1aCardDummy_Type()
)
tn11star1aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11star1aCardDummy.setStatus("current")
_TnMvac8bCardDummy_Type = Integer32
_TnMvac8bCardDummy_Object = MibTableColumn
tnMvac8bCardDummy = _TnMvac8bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 122),
    _TnMvac8bCardDummy_Type()
)
tnMvac8bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMvac8bCardDummy.setStatus("current")
_TnWr8c88afCardDummy_Type = Integer32
_TnWr8c88afCardDummy_Object = MibTableColumn
tnWr8c88afCardDummy = _TnWr8c88afCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 123),
    _TnWr8c88afCardDummy_Type()
)
tnWr8c88afCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWr8c88afCardDummy.setStatus("current")
_Tncl10an10gCardDummy_Type = Integer32
_Tncl10an10gCardDummy_Object = MibTableColumn
tncl10an10gCardDummy = _Tncl10an10gCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 124),
    _Tncl10an10gCardDummy_Type()
)
tncl10an10gCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tncl10an10gCardDummy.setStatus("current")
_Tncl24anmCardDummy_Type = Integer32
_Tncl24anmCardDummy_Object = MibTableColumn
tncl24anmCardDummy = _Tncl24anmCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 125),
    _Tncl24anmCardDummy_Type()
)
tncl24anmCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tncl24anmCardDummy.setStatus("current")
_TnOpsbCardDummy_Type = Integer32
_TnOpsbCardDummy_Object = MibTableColumn
tnOpsbCardDummy = _TnOpsbCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 126),
    _TnOpsbCardDummy_Type()
)
tnOpsbCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpsbCardDummy.setStatus("current")
_Tn11dpe12aCardDummy_Type = Integer32
_Tn11dpe12aCardDummy_Object = MibTableColumn
tn11dpe12aCardDummy = _Tn11dpe12aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 127),
    _Tn11dpe12aCardDummy_Type()
)
tn11dpe12aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11dpe12aCardDummy.setStatus("current")
_Tnul130scupCardDummy_Type = Integer32
_Tnul130scupCardDummy_Object = MibTableColumn
tnul130scupCardDummy = _Tnul130scupCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 128),
    _Tnul130scupCardDummy_Type()
)
tnul130scupCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnul130scupCardDummy.setStatus("current")
_Tn130scx10CardDummy_Type = Integer32
_Tn130scx10CardDummy_Object = MibTableColumn
tn130scx10CardDummy = _Tn130scx10CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 129),
    _Tn130scx10CardDummy_Type()
)
tn130scx10CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn130scx10CardDummy.setStatus("current")
_TnUniversalMatrixFirstLevelController1p2TCardDummy_Type = Integer32
_TnUniversalMatrixFirstLevelController1p2TCardDummy_Object = MibTableColumn
tnUniversalMatrixFirstLevelController1p2TCardDummy = _TnUniversalMatrixFirstLevelController1p2TCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 130),
    _TnUniversalMatrixFirstLevelController1p2TCardDummy_Type()
)
tnUniversalMatrixFirstLevelController1p2TCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUniversalMatrixFirstLevelController1p2TCardDummy.setStatus("current")
_TnA2p2125CardDummy_Type = Integer32
_TnA2p2125CardDummy_Object = MibTableColumn
tnA2p2125CardDummy = _TnA2p2125CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 131),
    _TnA2p2125CardDummy_Type()
)
tnA2p2125CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnA2p2125CardDummy.setStatus("current")
_Tn4qpa8CardDummy_Type = Integer32
_Tn4qpa8CardDummy_Object = MibTableColumn
tn4qpa8CardDummy = _Tn4qpa8CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 132),
    _Tn4qpa8CardDummy_Type()
)
tn4qpa8CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn4qpa8CardDummy.setStatus("current")
_TnOt112pdm11CardDummy_Type = Integer32
_TnOt112pdm11CardDummy_Object = MibTableColumn
tnOt112pdm11CardDummy = _TnOt112pdm11CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 133),
    _TnOt112pdm11CardDummy_Type()
)
tnOt112pdm11CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOt112pdm11CardDummy.setStatus("current")
_TnWtocmaCardDummy_Type = Integer32
_TnWtocmaCardDummy_Object = MibTableColumn
tnWtocmaCardDummy = _TnWtocmaCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 134),
    _TnWtocmaCardDummy_Type()
)
tnWtocmaCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmaCardDummy.setStatus("current")
_TnPtpctlCardDummy_Type = Integer32
_TnPtpctlCardDummy_Object = MibTableColumn
tnPtpctlCardDummy = _TnPtpctlCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 135),
    _TnPtpctlCardDummy_Type()
)
tnPtpctlCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardDummy.setStatus("current")
_TnPtpioCardDummy_Type = Integer32
_TnPtpioCardDummy_Object = MibTableColumn
tnPtpioCardDummy = _TnPtpioCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 136),
    _TnPtpioCardDummy_Type()
)
tnPtpioCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpioCardDummy.setStatus("current")
_TnIo24et1gbCardDummy_Type = Integer32
_TnIo24et1gbCardDummy_Object = MibTableColumn
tnIo24et1gbCardDummy = _TnIo24et1gbCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 137),
    _TnIo24et1gbCardDummy_Type()
)
tnIo24et1gbCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo24et1gbCardDummy.setStatus("current")
_TnIo4an10gCardDummy_Type = Integer32
_TnIo4an10gCardDummy_Object = MibTableColumn
tnIo4an10gCardDummy = _TnIo4an10gCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 138),
    _TnIo4an10gCardDummy_Type()
)
tnIo4an10gCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo4an10gCardDummy.setStatus("current")
_TnIo8et1gbCardDummy_Type = Integer32
_TnIo8et1gbCardDummy_Object = MibTableColumn
tnIo8et1gbCardDummy = _TnIo8et1gbCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 139),
    _TnIo8et1gbCardDummy_Type()
)
tnIo8et1gbCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo8et1gbCardDummy.setStatus("current")
_TnIo10et10gCardDummy_Type = Integer32
_TnIo10et10gCardDummy_Object = MibTableColumn
tnIo10et10gCardDummy = _TnIo10et10gCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 140),
    _TnIo10et10gCardDummy_Type()
)
tnIo10et10gCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo10et10gCardDummy.setStatus("current")
_TnUl11qcupcCardDummy_Type = Integer32
_TnUl11qcupcCardDummy_Object = MibTableColumn
tnUl11qcupcCardDummy = _TnUl11qcupcCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 141),
    _TnUl11qcupcCardDummy_Type()
)
tnUl11qcupcCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUl11qcupcCardDummy.setStatus("current")
_TnOt520scx4CardDummy_Type = Integer32
_TnOt520scx4CardDummy_Object = MibTableColumn
tnOt520scx4CardDummy = _TnOt520scx4CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 142),
    _TnOt520scx4CardDummy_Type()
)
tnOt520scx4CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOt520scx4CardDummy.setStatus("current")
_Tn11ope8CardDummy_Type = Integer32
_Tn11ope8CardDummy_Object = MibTableColumn
tn11ope8CardDummy = _Tn11ope8CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 143),
    _Tn11ope8CardDummy_Type()
)
tn11ope8CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11ope8CardDummy.setStatus("current")
_Tn11qce12xCardDummy_Type = Integer32
_Tn11qce12xCardDummy_Object = MibTableColumn
tn11qce12xCardDummy = _Tn11qce12xCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 144),
    _Tn11qce12xCardDummy_Type()
)
tn11qce12xCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn11qce12xCardDummy.setStatus("current")
_TnAm2625aCardDummy_Type = Integer32
_TnAm2625aCardDummy_Object = MibTableColumn
tnAm2625aCardDummy = _TnAm2625aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 145),
    _TnAm2625aCardDummy_Type()
)
tnAm2625aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAm2625aCardDummy.setStatus("current")
_TnAm2032aCardDummy_Type = Integer32
_TnAm2032aCardDummy_Object = MibTableColumn
tnAm2032aCardDummy = _TnAm2032aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 146),
    _TnAm2032aCardDummy_Type()
)
tnAm2032aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAm2032aCardDummy.setStatus("current")
_TnOt260scx2CardDummy_Type = Integer32
_TnOt260scx2CardDummy_Object = MibTableColumn
tnOt260scx2CardDummy = _TnOt260scx2CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 147),
    _TnOt260scx2CardDummy_Type()
)
tnOt260scx2CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOt260scx2CardDummy.setStatus("current")
_TnOt130snx10CardDummy_Type = Integer32
_TnOt130snx10CardDummy_Object = MibTableColumn
tnOt130snx10CardDummy = _TnOt130snx10CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 148),
    _TnOt130snx10CardDummy_Type()
)
tnOt130snx10CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOt130snx10CardDummy.setStatus("current")
_TnIo24anmbCardDummy_Type = Integer32
_TnIo24anmbCardDummy_Object = MibTableColumn
tnIo24anmbCardDummy = _TnIo24anmbCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 149),
    _TnIo24anmbCardDummy_Type()
)
tnIo24anmbCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo24anmbCardDummy.setStatus("current")
_TnOt11dpm8CardDummy_Type = Integer32
_TnOt11dpm8CardDummy_Object = MibTableColumn
tnOt11dpm8CardDummy = _TnOt11dpm8CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 150),
    _TnOt11dpm8CardDummy_Type()
)
tnOt11dpm8CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOt11dpm8CardDummy.setStatus("current")
_TnOt11dpm4mCardDummy_Type = Integer32
_TnOt11dpm4mCardDummy_Object = MibTableColumn
tnOt11dpm4mCardDummy = _TnOt11dpm4mCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 151),
    _TnOt11dpm4mCardDummy_Type()
)
tnOt11dpm4mCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOt11dpm4mCardDummy.setStatus("current")
_TnOt11dpm4eCardDummy_Type = Integer32
_TnOt11dpm4eCardDummy_Object = MibTableColumn
tnOt11dpm4eCardDummy = _TnOt11dpm4eCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 152),
    _TnOt11dpm4eCardDummy_Type()
)
tnOt11dpm4eCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOt11dpm4eCardDummy.setStatus("current")
_TnUl130scupbCardDummy_Type = Integer32
_TnUl130scupbCardDummy_Object = MibTableColumn
tnUl130scupbCardDummy = _TnUl130scupbCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 153),
    _TnUl130scupbCardDummy_Type()
)
tnUl130scupbCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUl130scupbCardDummy.setStatus("current")
_TnOt112sdx11CardDummy_Type = Integer32
_TnOt112sdx11CardDummy_Object = MibTableColumn
tnOt112sdx11CardDummy = _TnOt112sdx11CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 154),
    _TnOt112sdx11CardDummy_Type()
)
tnOt112sdx11CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOt112sdx11CardDummy.setStatus("current")
_TnAa2donwCardDummy_Type = Integer32
_TnAa2donwCardDummy_Object = MibTableColumn
tnAa2donwCardDummy = _TnAa2donwCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 155),
    _TnAa2donwCardDummy_Type()
)
tnAa2donwCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAa2donwCardDummy.setStatus("current")
_TnOt130sca1CardDummy_Type = Integer32
_TnOt130sca1CardDummy_Object = MibTableColumn
tnOt130sca1CardDummy = _TnOt130sca1CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 156),
    _TnOt130sca1CardDummy_Type()
)
tnOt130sca1CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOt130sca1CardDummy.setStatus("current")
_TnIo10an10gbCardDummy_Type = Integer32
_TnIo10an10gbCardDummy_Object = MibTableColumn
tnIo10an10gbCardDummy = _TnIo10an10gbCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 157),
    _TnIo10an10gbCardDummy_Type()
)
tnIo10an10gbCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo10an10gbCardDummy.setStatus("current")
_TnIo10et10gbCardDummy_Type = Integer32
_TnIo10et10gbCardDummy_Object = MibTableColumn
tnIo10et10gbCardDummy = _TnIo10et10gbCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 158),
    _TnIo10et10gbCardDummy_Type()
)
tnIo10et10gbCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo10et10gbCardDummy.setStatus("current")
_TnPsc1x6CardDummy_Type = Integer32
_TnPsc1x6CardDummy_Object = MibTableColumn
tnPsc1x6CardDummy = _TnPsc1x6CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 159),
    _TnPsc1x6CardDummy_Type()
)
tnPsc1x6CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsc1x6CardDummy.setStatus("current")
_TnWr20tfCardDummy_Type = Integer32
_TnWr20tfCardDummy_Object = MibTableColumn
tnWr20tfCardDummy = _TnWr20tfCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 160),
    _TnWr20tfCardDummy_Type()
)
tnWr20tfCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWr20tfCardDummy.setStatus("current")
_TnWtocmfCardDummy_Type = Integer32
_TnWtocmfCardDummy_Object = MibTableColumn
tnWtocmfCardDummy = _TnWtocmfCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 161),
    _TnWtocmfCardDummy_Type()
)
tnWtocmfCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmfCardDummy.setStatus("current")
_TnAswgCardDummy_Type = Integer32
_TnAswgCardDummy_Object = MibTableColumn
tnAswgCardDummy = _TnAswgCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 162),
    _TnAswgCardDummy_Type()
)
tnAswgCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAswgCardDummy.setStatus("current")
_TnA4pswgCardDummy_Type = Integer32
_TnA4pswgCardDummy_Object = MibTableColumn
tnA4pswgCardDummy = _TnA4pswgCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 163),
    _TnA4pswgCardDummy_Type()
)
tnA4pswgCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnA4pswgCardDummy.setStatus("current")
_TnOtdrCardDummy_Type = Integer32
_TnOtdrCardDummy_Object = MibTableColumn
tnOtdrCardDummy = _TnOtdrCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 164),
    _TnOtdrCardDummy_Type()
)
tnOtdrCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtdrCardDummy.setStatus("current")
_TnWr20tfmCardDummy_Type = Integer32
_TnWr20tfmCardDummy_Object = MibTableColumn
tnWr20tfmCardDummy = _TnWr20tfmCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 165),
    _TnWr20tfmCardDummy_Type()
)
tnWr20tfmCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWr20tfmCardDummy.setStatus("current")
_TnAar8aCardDummy_Type = Integer32
_TnAar8aCardDummy_Object = MibTableColumn
tnAar8aCardDummy = _TnAar8aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 166),
    _TnAar8aCardDummy_Type()
)
tnAar8aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAar8aCardDummy.setStatus("current")
_TnMcs8x16CardDummy_Type = Integer32
_TnMcs8x16CardDummy_Object = MibTableColumn
tnMcs8x16CardDummy = _TnMcs8x16CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 167),
    _TnMcs8x16CardDummy_Type()
)
tnMcs8x16CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcs8x16CardDummy.setStatus("current")
_TnMsh8fsmCardDummy_Type = Integer32
_TnMsh8fsmCardDummy_Object = MibTableColumn
tnMsh8fsmCardDummy = _TnMsh8fsmCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 168),
    _TnMsh8fsmCardDummy_Type()
)
tnMsh8fsmCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMsh8fsmCardDummy.setStatus("current")
_TnIo4an100gCardDummy_Type = Integer32
_TnIo4an100gCardDummy_Object = MibTableColumn
tnIo4an100gCardDummy = _TnIo4an100gCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 169),
    _TnIo4an100gCardDummy_Type()
)
tnIo4an100gCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo4an100gCardDummy.setStatus("current")
_TnIo30an10gCardDummy_Type = Integer32
_TnIo30an10gCardDummy_Object = MibTableColumn
tnIo30an10gCardDummy = _TnIo30an10gCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 170),
    _TnIo30an10gCardDummy_Type()
)
tnIo30an10gCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo30an10gCardDummy.setStatus("current")
_TnSfd2aCardDummy_Type = Integer32
_TnSfd2aCardDummy_Object = MibTableColumn
tnSfd2aCardDummy = _TnSfd2aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 171),
    _TnSfd2aCardDummy_Type()
)
tnSfd2aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2aCardDummy.setStatus("current")
_TnSfd2bCardDummy_Type = Integer32
_TnSfd2bCardDummy_Object = MibTableColumn
tnSfd2bCardDummy = _TnSfd2bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 172),
    _TnSfd2bCardDummy_Type()
)
tnSfd2bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2bCardDummy.setStatus("current")
_TnSfd2cCardDummy_Type = Integer32
_TnSfd2cCardDummy_Object = MibTableColumn
tnSfd2cCardDummy = _TnSfd2cCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 173),
    _TnSfd2cCardDummy_Type()
)
tnSfd2cCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2cCardDummy.setStatus("current")
_TnSfd2dCardDummy_Type = Integer32
_TnSfd2dCardDummy_Object = MibTableColumn
tnSfd2dCardDummy = _TnSfd2dCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 174),
    _TnSfd2dCardDummy_Type()
)
tnSfd2dCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2dCardDummy.setStatus("current")
_TnSfd2eCardDummy_Type = Integer32
_TnSfd2eCardDummy_Object = MibTableColumn
tnSfd2eCardDummy = _TnSfd2eCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 175),
    _TnSfd2eCardDummy_Type()
)
tnSfd2eCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2eCardDummy.setStatus("current")
_TnSfd2fCardDummy_Type = Integer32
_TnSfd2fCardDummy_Object = MibTableColumn
tnSfd2fCardDummy = _TnSfd2fCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 176),
    _TnSfd2fCardDummy_Type()
)
tnSfd2fCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2fCardDummy.setStatus("current")
_TnSfd2gCardDummy_Type = Integer32
_TnSfd2gCardDummy_Object = MibTableColumn
tnSfd2gCardDummy = _TnSfd2gCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 177),
    _TnSfd2gCardDummy_Type()
)
tnSfd2gCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2gCardDummy.setStatus("current")
_TnSfd2hCardDummy_Type = Integer32
_TnSfd2hCardDummy_Object = MibTableColumn
tnSfd2hCardDummy = _TnSfd2hCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 178),
    _TnSfd2hCardDummy_Type()
)
tnSfd2hCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2hCardDummy.setStatus("current")
_TnSfd2iCardDummy_Type = Integer32
_TnSfd2iCardDummy_Object = MibTableColumn
tnSfd2iCardDummy = _TnSfd2iCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 179),
    _TnSfd2iCardDummy_Type()
)
tnSfd2iCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2iCardDummy.setStatus("current")
_TnSfd2lCardDummy_Type = Integer32
_TnSfd2lCardDummy_Object = MibTableColumn
tnSfd2lCardDummy = _TnSfd2lCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 180),
    _TnSfd2lCardDummy_Type()
)
tnSfd2lCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2lCardDummy.setStatus("current")
_TnSfd2mCardDummy_Type = Integer32
_TnSfd2mCardDummy_Object = MibTableColumn
tnSfd2mCardDummy = _TnSfd2mCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 181),
    _TnSfd2mCardDummy_Type()
)
tnSfd2mCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2mCardDummy.setStatus("current")
_TnSfd2nCardDummy_Type = Integer32
_TnSfd2nCardDummy_Object = MibTableColumn
tnSfd2nCardDummy = _TnSfd2nCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 182),
    _TnSfd2nCardDummy_Type()
)
tnSfd2nCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2nCardDummy.setStatus("current")
_TnSfd2oCardDummy_Type = Integer32
_TnSfd2oCardDummy_Object = MibTableColumn
tnSfd2oCardDummy = _TnSfd2oCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 183),
    _TnSfd2oCardDummy_Type()
)
tnSfd2oCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2oCardDummy.setStatus("current")
_TnSfd2pCardDummy_Type = Integer32
_TnSfd2pCardDummy_Object = MibTableColumn
tnSfd2pCardDummy = _TnSfd2pCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 184),
    _TnSfd2pCardDummy_Type()
)
tnSfd2pCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2pCardDummy.setStatus("current")
_TnSfd2qCardDummy_Type = Integer32
_TnSfd2qCardDummy_Object = MibTableColumn
tnSfd2qCardDummy = _TnSfd2qCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 185),
    _TnSfd2qCardDummy_Type()
)
tnSfd2qCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2qCardDummy.setStatus("current")
_TnSfd2rCardDummy_Type = Integer32
_TnSfd2rCardDummy_Object = MibTableColumn
tnSfd2rCardDummy = _TnSfd2rCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 186),
    _TnSfd2rCardDummy_Type()
)
tnSfd2rCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd2rCardDummy.setStatus("current")
_TnVwmSfd8aCardDummy_Type = Integer32
_TnVwmSfd8aCardDummy_Object = MibTableColumn
tnVwmSfd8aCardDummy = _TnVwmSfd8aCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 187),
    _TnVwmSfd8aCardDummy_Type()
)
tnVwmSfd8aCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmSfd8aCardDummy.setStatus("current")
_TnVwmSfd8bCardDummy_Type = Integer32
_TnVwmSfd8bCardDummy_Object = MibTableColumn
tnVwmSfd8bCardDummy = _TnVwmSfd8bCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 188),
    _TnVwmSfd8bCardDummy_Type()
)
tnVwmSfd8bCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmSfd8bCardDummy.setStatus("current")
_TnVwmSfd8cCardDummy_Type = Integer32
_TnVwmSfd8cCardDummy_Object = MibTableColumn
tnVwmSfd8cCardDummy = _TnVwmSfd8cCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 189),
    _TnVwmSfd8cCardDummy_Type()
)
tnVwmSfd8cCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmSfd8cCardDummy.setStatus("current")
_TnVwmSfd8dCardDummy_Type = Integer32
_TnVwmSfd8dCardDummy_Object = MibTableColumn
tnVwmSfd8dCardDummy = _TnVwmSfd8dCardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 190),
    _TnVwmSfd8dCardDummy_Type()
)
tnVwmSfd8dCardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmSfd8dCardDummy.setStatus("current")
_TnVwmSfc8CardDummy_Type = Integer32
_TnVwmSfc8CardDummy_Object = MibTableColumn
tnVwmSfc8CardDummy = _TnVwmSfc8CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 191),
    _TnVwmSfc8CardDummy_Type()
)
tnVwmSfc8CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmSfc8CardDummy.setStatus("current")
_TnIo30an300CardDummy_Type = Integer32
_TnIo30an300CardDummy_Object = MibTableColumn
tnIo30an300CardDummy = _TnIo30an300CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 192),
    _TnIo30an300CardDummy_Type()
)
tnIo30an300CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo30an300CardDummy.setStatus("current")
_TnIo4an400CardDummy_Type = Integer32
_TnIo4an400CardDummy_Object = MibTableColumn
tnIo4an400CardDummy = _TnIo4an400CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 193),
    _TnIo4an400CardDummy_Type()
)
tnIo4an400CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIo4an400CardDummy.setStatus("current")
_Tn12p120CardDummy_Type = Integer32
_Tn12p120CardDummy_Object = MibTableColumn
tn12p120CardDummy = _Tn12p120CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 194),
    _Tn12p120CardDummy_Type()
)
tn12p120CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn12p120CardDummy.setStatus("current")
_Tn20p200CardDummy_Type = Integer32
_Tn20p200CardDummy_Object = MibTableColumn
tn20p200CardDummy = _Tn20p200CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 195),
    _Tn20p200CardDummy_Type()
)
tn20p200CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn20p200CardDummy.setStatus("current")
_Tn1ud200CardDummy_Type = Integer32
_Tn1ud200CardDummy_Object = MibTableColumn
tn1ud200CardDummy = _Tn1ud200CardDummy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 1, 1, 196),
    _Tn1ud200CardDummy_Type()
)
tn1ud200CardDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn1ud200CardDummy.setStatus("current")
_TnExprSlotTable_Object = MibTable
tnExprSlotTable = _TnExprSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tnExprSlotTable.setStatus("current")
_TnExprSlotEntry_Object = MibTableRow
tnExprSlotEntry = _TnExprSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 6, 1)
)
tnExprSlotEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnExprSlotEntry.setStatus("current")
_TnExprSlotProgrammedType_Type = ObjectIdentifier
_TnExprSlotProgrammedType_Object = MibTableColumn
tnExprSlotProgrammedType = _TnExprSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 6, 1, 1),
    _TnExprSlotProgrammedType_Type()
)
tnExprSlotProgrammedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnExprSlotProgrammedType.setStatus("current")
_TnExprSlotAdminState_Type = TropicAdminStateType
_TnExprSlotAdminState_Object = MibTableColumn
tnExprSlotAdminState = _TnExprSlotAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 6, 1, 2),
    _TnExprSlotAdminState_Type()
)
tnExprSlotAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnExprSlotAdminState.setStatus("current")
_TnExprOchCrossConnectTable_Object = MibTable
tnExprOchCrossConnectTable = _TnExprOchCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 13)
)
if mibBuilder.loadTexts:
    tnExprOchCrossConnectTable.setStatus("current")
_TnExprOchCrossConnectEntry_Object = MibTableRow
tnExprOchCrossConnectEntry = _TnExprOchCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 13, 1)
)
tnExprOchCrossConnectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnDirection"),
    (0, "TROPIC-EXPROPTICALCARD", "tnExprOchChannel"),
)
if mibBuilder.loadTexts:
    tnExprOchCrossConnectEntry.setStatus("current")
_TnExprOchChannel_Type = Unsigned32
_TnExprOchChannel_Object = MibTableColumn
tnExprOchChannel = _TnExprOchChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 13, 1, 1),
    _TnExprOchChannel_Type()
)
tnExprOchChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnExprOchChannel.setStatus("current")
_TnExprOchCrossConnectEgressIfIndex_Type = InterfaceIndex
_TnExprOchCrossConnectEgressIfIndex_Object = MibTableColumn
tnExprOchCrossConnectEgressIfIndex = _TnExprOchCrossConnectEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 13, 1, 2),
    _TnExprOchCrossConnectEgressIfIndex_Type()
)
tnExprOchCrossConnectEgressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnExprOchCrossConnectEgressIfIndex.setStatus("current")


class _TnExprOchCrossConnectNetworkTrace_Type(OctetString):
    """Custom type tnExprOchCrossConnectNetworkTrace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2047),
    )


_TnExprOchCrossConnectNetworkTrace_Type.__name__ = "OctetString"
_TnExprOchCrossConnectNetworkTrace_Object = MibTableColumn
tnExprOchCrossConnectNetworkTrace = _TnExprOchCrossConnectNetworkTrace_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 13, 1, 3),
    _TnExprOchCrossConnectNetworkTrace_Type()
)
tnExprOchCrossConnectNetworkTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnExprOchCrossConnectNetworkTrace.setStatus("current")
_TnExprShelfTable_Object = MibTable
tnExprShelfTable = _TnExprShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 15)
)
if mibBuilder.loadTexts:
    tnExprShelfTable.setStatus("current")
_TnExprShelfEntry_Object = MibTableRow
tnExprShelfEntry = _TnExprShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 15, 1)
)
tnExprShelfEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnExprShelfEntry.setStatus("current")
_TnExprShelfProgrammedType_Type = ObjectIdentifier
_TnExprShelfProgrammedType_Object = MibTableColumn
tnExprShelfProgrammedType = _TnExprShelfProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 15, 1, 1),
    _TnExprShelfProgrammedType_Type()
)
tnExprShelfProgrammedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnExprShelfProgrammedType.setStatus("current")
_TnExprActiveNetworkElementServiceTable_Object = MibTable
tnExprActiveNetworkElementServiceTable = _TnExprActiveNetworkElementServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 17)
)
if mibBuilder.loadTexts:
    tnExprActiveNetworkElementServiceTable.setStatus("current")
_TnExprActiveNetworkElementServiceEntry_Object = MibTableRow
tnExprActiveNetworkElementServiceEntry = _TnExprActiveNetworkElementServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 17, 1)
)
tnExprActiveNetworkElementServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnExprActiveNetworkElementServiceEntry.setStatus("current")
_TnExprActiveNetworkElementServiceInfo_Type = OctetString
_TnExprActiveNetworkElementServiceInfo_Object = MibTableColumn
tnExprActiveNetworkElementServiceInfo = _TnExprActiveNetworkElementServiceInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 17, 1, 1),
    _TnExprActiveNetworkElementServiceInfo_Type()
)
tnExprActiveNetworkElementServiceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnExprActiveNetworkElementServiceInfo.setStatus("current")
_TnExprPowerMgmtCommsTable_Object = MibTable
tnExprPowerMgmtCommsTable = _TnExprPowerMgmtCommsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 19)
)
if mibBuilder.loadTexts:
    tnExprPowerMgmtCommsTable.setStatus("current")
_TnExprPowerMgmtCommsEntry_Object = MibTableRow
tnExprPowerMgmtCommsEntry = _TnExprPowerMgmtCommsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 19, 1)
)
tnExprPowerMgmtCommsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnDirection"),
    (0, "TROPIC-EXPROPTICALCARD", "tnExprOchChannel"),
)
if mibBuilder.loadTexts:
    tnExprPowerMgmtCommsEntry.setStatus("current")


class _TnExprPowerMgmtCommsPayload_Type(OctetString):
    """Custom type tnExprPowerMgmtCommsPayload based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnExprPowerMgmtCommsPayload_Type.__name__ = "OctetString"
_TnExprPowerMgmtCommsPayload_Object = MibTableColumn
tnExprPowerMgmtCommsPayload = _TnExprPowerMgmtCommsPayload_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 19, 1, 1),
    _TnExprPowerMgmtCommsPayload_Type()
)
tnExprPowerMgmtCommsPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnExprPowerMgmtCommsPayload.setStatus("current")
_TnExprPowerMgmtPerDirectionTable_Object = MibTable
tnExprPowerMgmtPerDirectionTable = _TnExprPowerMgmtPerDirectionTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 20)
)
if mibBuilder.loadTexts:
    tnExprPowerMgmtPerDirectionTable.setStatus("current")
_TnExprPowerMgmtPerDirectionEntry_Object = MibTableRow
tnExprPowerMgmtPerDirectionEntry = _TnExprPowerMgmtPerDirectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 20, 1)
)
tnExprPowerMgmtPerDirectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnDirection"),
)
if mibBuilder.loadTexts:
    tnExprPowerMgmtPerDirectionEntry.setStatus("current")
_TnExprPowerMgmtPerDirectionChannelPowerWithinRangeMask_Type = Unsigned32
_TnExprPowerMgmtPerDirectionChannelPowerWithinRangeMask_Object = MibTableColumn
tnExprPowerMgmtPerDirectionChannelPowerWithinRangeMask = _TnExprPowerMgmtPerDirectionChannelPowerWithinRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 20, 1, 1),
    _TnExprPowerMgmtPerDirectionChannelPowerWithinRangeMask_Type()
)
tnExprPowerMgmtPerDirectionChannelPowerWithinRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnExprPowerMgmtPerDirectionChannelPowerWithinRangeMask.setStatus("current")
_TnExprPowerMgmtPerDirectionChannelPowerWithinRangeBitSet_Type = OctetString
_TnExprPowerMgmtPerDirectionChannelPowerWithinRangeBitSet_Object = MibTableColumn
tnExprPowerMgmtPerDirectionChannelPowerWithinRangeBitSet = _TnExprPowerMgmtPerDirectionChannelPowerWithinRangeBitSet_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 20, 1, 2),
    _TnExprPowerMgmtPerDirectionChannelPowerWithinRangeBitSet_Type()
)
tnExprPowerMgmtPerDirectionChannelPowerWithinRangeBitSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnExprPowerMgmtPerDirectionChannelPowerWithinRangeBitSet.setStatus("current")
_TnExprPortTable_Object = MibTable
tnExprPortTable = _TnExprPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 24)
)
if mibBuilder.loadTexts:
    tnExprPortTable.setStatus("current")
_TnExprPortEntry_Object = MibTableRow
tnExprPortEntry = _TnExprPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 24, 1)
)
tnExprPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnExprPortEntry.setStatus("current")
_TnExprAmpGainTilt_Type = Integer32
_TnExprAmpGainTilt_Object = MibTableColumn
tnExprAmpGainTilt = _TnExprAmpGainTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 24, 1, 1),
    _TnExprAmpGainTilt_Type()
)
tnExprAmpGainTilt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnExprAmpGainTilt.setStatus("current")
if mibBuilder.loadTexts:
    tnExprAmpGainTilt.setUnits("mB")
_TnExprVectoredAddDropAdjustTable_Object = MibTable
tnExprVectoredAddDropAdjustTable = _TnExprVectoredAddDropAdjustTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 25)
)
if mibBuilder.loadTexts:
    tnExprVectoredAddDropAdjustTable.setStatus("current")
_TnExprVectoredAddDropAdjustEntry_Object = MibTableRow
tnExprVectoredAddDropAdjustEntry = _TnExprVectoredAddDropAdjustEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 25, 1)
)
tnExprVectoredAddDropAdjustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnExprVectoredAddDropAdjustEntry.setStatus("current")


class _TnExprVectoredAddDropAdjustStatus_Type(Integer32):
    """Custom type tnExprVectoredAddDropAdjustStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 1),
          ("inProgress", 2),
          ("notInProgress", 3))
    )


_TnExprVectoredAddDropAdjustStatus_Type.__name__ = "Integer32"
_TnExprVectoredAddDropAdjustStatus_Object = MibTableColumn
tnExprVectoredAddDropAdjustStatus = _TnExprVectoredAddDropAdjustStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 25, 1, 1),
    _TnExprVectoredAddDropAdjustStatus_Type()
)
tnExprVectoredAddDropAdjustStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnExprVectoredAddDropAdjustStatus.setStatus("current")
_TnExprVectoredAddDropPowerTable_Object = MibTable
tnExprVectoredAddDropPowerTable = _TnExprVectoredAddDropPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 26)
)
if mibBuilder.loadTexts:
    tnExprVectoredAddDropPowerTable.setStatus("current")
_TnExprVectoredAddDropPowerEntry_Object = MibTableRow
tnExprVectoredAddDropPowerEntry = _TnExprVectoredAddDropPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 26, 1)
)
tnExprVectoredAddDropPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnExprVectoredAddDropPowerEntry.setStatus("current")


class _TnExprVectoredAddDropPowerChMeasuredBitSetOut_Type(OctetString):
    """Custom type tnExprVectoredAddDropPowerChMeasuredBitSetOut based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_TnExprVectoredAddDropPowerChMeasuredBitSetOut_Type.__name__ = "OctetString"
_TnExprVectoredAddDropPowerChMeasuredBitSetOut_Object = MibTableColumn
tnExprVectoredAddDropPowerChMeasuredBitSetOut = _TnExprVectoredAddDropPowerChMeasuredBitSetOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 26, 1, 1),
    _TnExprVectoredAddDropPowerChMeasuredBitSetOut_Type()
)
tnExprVectoredAddDropPowerChMeasuredBitSetOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnExprVectoredAddDropPowerChMeasuredBitSetOut.setStatus("current")
_TnExprVectoredAddDropPowerChAverageMeasuredOut_Type = Integer32
_TnExprVectoredAddDropPowerChAverageMeasuredOut_Object = MibTableColumn
tnExprVectoredAddDropPowerChAverageMeasuredOut = _TnExprVectoredAddDropPowerChAverageMeasuredOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1, 2, 26, 1, 2),
    _TnExprVectoredAddDropPowerChAverageMeasuredOut_Type()
)
tnExprVectoredAddDropPowerChAverageMeasuredOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnExprVectoredAddDropPowerChAverageMeasuredOut.setStatus("current")
if mibBuilder.loadTexts:
    tnExprVectoredAddDropPowerChAverageMeasuredOut.setUnits("mBm")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-EXPROPTICALCARD",
    **{"tnExprOpticalCardMibModule": tnExprOpticalCardMibModule,
       "tnExprOpticalCardConf": tnExprOpticalCardConf,
       "tnExprOpticalCardGroups": tnExprOpticalCardGroups,
       "tnExprOpticalCardCompliances": tnExprOpticalCardCompliances,
       "tnExprOpticalCardObjs": tnExprOpticalCardObjs,
       "tnExprCardTable": tnExprCardTable,
       "tnExprCardEntry": tnExprCardEntry,
       "tnDcmCardDummy": tnDcmCardDummy,
       "tnOpsaCardDummy": tnOpsaCardDummy,
       "tn11stmm10CardDummy": tn11stmm10CardDummy,
       "tn11star1CardDummy": tn11star1CardDummy,
       "tnAhphgCardDummy": tnAhphgCardDummy,
       "tnAlphgCardDummy": tnAlphgCardDummy,
       "tnCwr8CardDummy": tnCwr8CardDummy,
       "tn11stge12CardDummy": tn11stge12CardDummy,
       "tn11dpge12CardDummy": tn11dpge12CardDummy,
       "tnSfd44CardDummy": tnSfd44CardDummy,
       "tnPowerFilterCardDummy": tnPowerFilterCardDummy,
       "tnSvacCardDummy": tnSvacCardDummy,
       "tnSfd5aCardDummy": tnSfd5aCardDummy,
       "tnSfd5bCardDummy": tnSfd5bCardDummy,
       "tnSfd5cCardDummy": tnSfd5cCardDummy,
       "tnSfd5dCardDummy": tnSfd5dCardDummy,
       "tnSfd5eCardDummy": tnSfd5eCardDummy,
       "tnSfd5fCardDummy": tnSfd5fCardDummy,
       "tnSfd5gCardDummy": tnSfd5gCardDummy,
       "tnSfd5hCardDummy": tnSfd5hCardDummy,
       "tnSfd10aCardDummy": tnSfd10aCardDummy,
       "tnSfd10bCardDummy": tnSfd10bCardDummy,
       "tnSfd10cCardDummy": tnSfd10cCardDummy,
       "tnSfd10dCardDummy": tnSfd10dCardDummy,
       "tnSfc2aCardDummy": tnSfc2aCardDummy,
       "tnSfc2bCardDummy": tnSfc2bCardDummy,
       "tnSfc2cCardDummy": tnSfc2cCardDummy,
       "tnSfc2dCardDummy": tnSfc2dCardDummy,
       "tnSfc4aCardDummy": tnSfc4aCardDummy,
       "tnSfc4bCardDummy": tnSfc4bCardDummy,
       "tnSfc8CardDummy": tnSfc8CardDummy,
       "tnSfc1aCardDummy": tnSfc1aCardDummy,
       "tnSfc1bCardDummy": tnSfc1bCardDummy,
       "tnSfc1cCardDummy": tnSfc1cCardDummy,
       "tnSfc1dCardDummy": tnSfc1dCardDummy,
       "tnSfc1eCardDummy": tnSfc1eCardDummy,
       "tnSfc1fCardDummy": tnSfc1fCardDummy,
       "tnSfc1gCardDummy": tnSfc1gCardDummy,
       "tnSfc1hCardDummy": tnSfc1hCardDummy,
       "tn4dpa4CardDummy": tn4dpa4CardDummy,
       "tnCwr8c88CardDummy": tnCwr8c88CardDummy,
       "tnSfd44bCardDummy": tnSfd44bCardDummy,
       "tnItlbCardDummy": tnItlbCardDummy,
       "tnAhplgCardDummy": tnAhplgCardDummy,
       "tn43stx4CardDummy": tn43stx4CardDummy,
       "tnAlpfgkCardDummy": tnAlpfgkCardDummy,
       "tnOscCardDummy": tnOscCardDummy,
       "tn4dpa2CardDummy": tn4dpa2CardDummy,
       "tnSfd8aCardDummy": tnSfd8aCardDummy,
       "tnSfd8bCardDummy": tnSfd8bCardDummy,
       "tnSfd8cCardDummy": tnSfd8cCardDummy,
       "tnSfd8dCardDummy": tnSfd8dCardDummy,
       "tn43sta1pCardDummy": tn43sta1pCardDummy,
       "tn43stx4pCardDummy": tn43stx4pCardDummy,
       "tn11qpa4CardDummy": tn11qpa4CardDummy,
       "tnSfd40CardDummy": tnSfd40CardDummy,
       "tnSfd40bCardDummy": tnSfd40bCardDummy,
       "tnA2325aCardDummy": tnA2325aCardDummy,
       "tn112scx10CardDummy": tn112scx10CardDummy,
       "tn112sca1CardDummy": tn112sca1CardDummy,
       "tnAlpfgtCardDummy": tnAlpfgtCardDummy,
       "tnOsctCardDummy": tnOsctCardDummy,
       "tnWtocmCardDummy": tnWtocmCardDummy,
       "tnWr2c88CardDummy": tnWr2c88CardDummy,
       "tnAm2017bCardDummy": tnAm2017bCardDummy,
       "tnAm2325bCardDummy": tnAm2325bCardDummy,
       "tn1dpp21CardDummy": tn1dpp21CardDummy,
       "tnSfd4aCardDummy": tnSfd4aCardDummy,
       "tnSfd4bCardDummy": tnSfd4bCardDummy,
       "tnSfd4cCardDummy": tnSfd4cCardDummy,
       "tnSfd4dCardDummy": tnSfd4dCardDummy,
       "tnSfd4eCardDummy": tnSfd4eCardDummy,
       "tnSfd4fCardDummy": tnSfd4fCardDummy,
       "tnSfd4gCardDummy": tnSfd4gCardDummy,
       "tnSfd4hCardDummy": tnSfd4hCardDummy,
       "tnMvacCardDummy": tnMvacCardDummy,
       "tnBusTerminationCardDummy": tnBusTerminationCardDummy,
       "tnFirstLevelControllerCardDummy": tnFirstLevelControllerCardDummy,
       "tnMatrix3T8CardDummy": tnMatrix3T8CardDummy,
       "tnMatrix1T9CardDummy": tnMatrix1T9CardDummy,
       "tnMatrix0CompactCardDummy": tnMatrix0CompactCardDummy,
       "tn43scx4CardDummy": tn43scx4CardDummy,
       "tnRa2pCardDummy": tnRa2pCardDummy,
       "tnAm2318aCardDummy": tnAm2318aCardDummy,
       "tnAm2125aCardDummy": tnAm2125aCardDummy,
       "tnItluCardDummy": tnItluCardDummy,
       "tnWr8c88aCardDummy": tnWr8c88aCardDummy,
       "tnBusTerminationOnlyCardDummy": tnBusTerminationOnlyCardDummy,
       "tn11dpe12eCardDummy": tn11dpe12eCardDummy,
       "tn112sx10lCardDummy": tn112sx10lCardDummy,
       "tn112sa1lCardDummy": tn112sa1lCardDummy,
       "tn11dpm12CardDummy": tn11dpm12CardDummy,
       "tnMesh4CardDummy": tnMesh4CardDummy,
       "tn43sca1CardDummy": tn43sca1CardDummy,
       "tn43scx4lCardDummy": tn43scx4lCardDummy,
       "tnAm2125bCardDummy": tnAm2125bCardDummy,
       "tnUniversalMatrixFirstLevelControllerCardDummy": tnUniversalMatrixFirstLevelControllerCardDummy,
       "tnEndOfShelfMiddleCardDummy": tnEndOfShelfMiddleCardDummy,
       "tn112snx10CardDummy": tn112snx10CardDummy,
       "tn112sna1CardDummy": tn112sna1CardDummy,
       "tn1dpp24mCardDummy": tn1dpp24mCardDummy,
       "tnul43scupCardDummy": tnul43scupCardDummy,
       "tnul11qcupCardDummy": tnul11qcupCardDummy,
       "tn11qpen4CardDummy": tn11qpen4CardDummy,
       "tn43scx4eCardDummy": tn43scx4eCardDummy,
       "tn43scge1CardDummy": tn43scge1CardDummy,
       "tn11qpe24CardDummy": tn11qpe24CardDummy,
       "tn11star1aCardDummy": tn11star1aCardDummy,
       "tnMvac8bCardDummy": tnMvac8bCardDummy,
       "tnWr8c88afCardDummy": tnWr8c88afCardDummy,
       "tncl10an10gCardDummy": tncl10an10gCardDummy,
       "tncl24anmCardDummy": tncl24anmCardDummy,
       "tnOpsbCardDummy": tnOpsbCardDummy,
       "tn11dpe12aCardDummy": tn11dpe12aCardDummy,
       "tnul130scupCardDummy": tnul130scupCardDummy,
       "tn130scx10CardDummy": tn130scx10CardDummy,
       "tnUniversalMatrixFirstLevelController1p2TCardDummy": tnUniversalMatrixFirstLevelController1p2TCardDummy,
       "tnA2p2125CardDummy": tnA2p2125CardDummy,
       "tn4qpa8CardDummy": tn4qpa8CardDummy,
       "tnOt112pdm11CardDummy": tnOt112pdm11CardDummy,
       "tnWtocmaCardDummy": tnWtocmaCardDummy,
       "tnPtpctlCardDummy": tnPtpctlCardDummy,
       "tnPtpioCardDummy": tnPtpioCardDummy,
       "tnIo24et1gbCardDummy": tnIo24et1gbCardDummy,
       "tnIo4an10gCardDummy": tnIo4an10gCardDummy,
       "tnIo8et1gbCardDummy": tnIo8et1gbCardDummy,
       "tnIo10et10gCardDummy": tnIo10et10gCardDummy,
       "tnUl11qcupcCardDummy": tnUl11qcupcCardDummy,
       "tnOt520scx4CardDummy": tnOt520scx4CardDummy,
       "tn11ope8CardDummy": tn11ope8CardDummy,
       "tn11qce12xCardDummy": tn11qce12xCardDummy,
       "tnAm2625aCardDummy": tnAm2625aCardDummy,
       "tnAm2032aCardDummy": tnAm2032aCardDummy,
       "tnOt260scx2CardDummy": tnOt260scx2CardDummy,
       "tnOt130snx10CardDummy": tnOt130snx10CardDummy,
       "tnIo24anmbCardDummy": tnIo24anmbCardDummy,
       "tnOt11dpm8CardDummy": tnOt11dpm8CardDummy,
       "tnOt11dpm4mCardDummy": tnOt11dpm4mCardDummy,
       "tnOt11dpm4eCardDummy": tnOt11dpm4eCardDummy,
       "tnUl130scupbCardDummy": tnUl130scupbCardDummy,
       "tnOt112sdx11CardDummy": tnOt112sdx11CardDummy,
       "tnAa2donwCardDummy": tnAa2donwCardDummy,
       "tnOt130sca1CardDummy": tnOt130sca1CardDummy,
       "tnIo10an10gbCardDummy": tnIo10an10gbCardDummy,
       "tnIo10et10gbCardDummy": tnIo10et10gbCardDummy,
       "tnPsc1x6CardDummy": tnPsc1x6CardDummy,
       "tnWr20tfCardDummy": tnWr20tfCardDummy,
       "tnWtocmfCardDummy": tnWtocmfCardDummy,
       "tnAswgCardDummy": tnAswgCardDummy,
       "tnA4pswgCardDummy": tnA4pswgCardDummy,
       "tnOtdrCardDummy": tnOtdrCardDummy,
       "tnWr20tfmCardDummy": tnWr20tfmCardDummy,
       "tnAar8aCardDummy": tnAar8aCardDummy,
       "tnMcs8x16CardDummy": tnMcs8x16CardDummy,
       "tnMsh8fsmCardDummy": tnMsh8fsmCardDummy,
       "tnIo4an100gCardDummy": tnIo4an100gCardDummy,
       "tnIo30an10gCardDummy": tnIo30an10gCardDummy,
       "tnSfd2aCardDummy": tnSfd2aCardDummy,
       "tnSfd2bCardDummy": tnSfd2bCardDummy,
       "tnSfd2cCardDummy": tnSfd2cCardDummy,
       "tnSfd2dCardDummy": tnSfd2dCardDummy,
       "tnSfd2eCardDummy": tnSfd2eCardDummy,
       "tnSfd2fCardDummy": tnSfd2fCardDummy,
       "tnSfd2gCardDummy": tnSfd2gCardDummy,
       "tnSfd2hCardDummy": tnSfd2hCardDummy,
       "tnSfd2iCardDummy": tnSfd2iCardDummy,
       "tnSfd2lCardDummy": tnSfd2lCardDummy,
       "tnSfd2mCardDummy": tnSfd2mCardDummy,
       "tnSfd2nCardDummy": tnSfd2nCardDummy,
       "tnSfd2oCardDummy": tnSfd2oCardDummy,
       "tnSfd2pCardDummy": tnSfd2pCardDummy,
       "tnSfd2qCardDummy": tnSfd2qCardDummy,
       "tnSfd2rCardDummy": tnSfd2rCardDummy,
       "tnVwmSfd8aCardDummy": tnVwmSfd8aCardDummy,
       "tnVwmSfd8bCardDummy": tnVwmSfd8bCardDummy,
       "tnVwmSfd8cCardDummy": tnVwmSfd8cCardDummy,
       "tnVwmSfd8dCardDummy": tnVwmSfd8dCardDummy,
       "tnVwmSfc8CardDummy": tnVwmSfc8CardDummy,
       "tnIo30an300CardDummy": tnIo30an300CardDummy,
       "tnIo4an400CardDummy": tnIo4an400CardDummy,
       "tn12p120CardDummy": tn12p120CardDummy,
       "tn20p200CardDummy": tn20p200CardDummy,
       "tn1ud200CardDummy": tn1ud200CardDummy,
       "tnExprSlotTable": tnExprSlotTable,
       "tnExprSlotEntry": tnExprSlotEntry,
       "tnExprSlotProgrammedType": tnExprSlotProgrammedType,
       "tnExprSlotAdminState": tnExprSlotAdminState,
       "tnExprOchCrossConnectTable": tnExprOchCrossConnectTable,
       "tnExprOchCrossConnectEntry": tnExprOchCrossConnectEntry,
       "tnExprOchChannel": tnExprOchChannel,
       "tnExprOchCrossConnectEgressIfIndex": tnExprOchCrossConnectEgressIfIndex,
       "tnExprOchCrossConnectNetworkTrace": tnExprOchCrossConnectNetworkTrace,
       "tnExprShelfTable": tnExprShelfTable,
       "tnExprShelfEntry": tnExprShelfEntry,
       "tnExprShelfProgrammedType": tnExprShelfProgrammedType,
       "tnExprActiveNetworkElementServiceTable": tnExprActiveNetworkElementServiceTable,
       "tnExprActiveNetworkElementServiceEntry": tnExprActiveNetworkElementServiceEntry,
       "tnExprActiveNetworkElementServiceInfo": tnExprActiveNetworkElementServiceInfo,
       "tnExprPowerMgmtCommsTable": tnExprPowerMgmtCommsTable,
       "tnExprPowerMgmtCommsEntry": tnExprPowerMgmtCommsEntry,
       "tnExprPowerMgmtCommsPayload": tnExprPowerMgmtCommsPayload,
       "tnExprPowerMgmtPerDirectionTable": tnExprPowerMgmtPerDirectionTable,
       "tnExprPowerMgmtPerDirectionEntry": tnExprPowerMgmtPerDirectionEntry,
       "tnExprPowerMgmtPerDirectionChannelPowerWithinRangeMask": tnExprPowerMgmtPerDirectionChannelPowerWithinRangeMask,
       "tnExprPowerMgmtPerDirectionChannelPowerWithinRangeBitSet": tnExprPowerMgmtPerDirectionChannelPowerWithinRangeBitSet,
       "tnExprPortTable": tnExprPortTable,
       "tnExprPortEntry": tnExprPortEntry,
       "tnExprAmpGainTilt": tnExprAmpGainTilt,
       "tnExprVectoredAddDropAdjustTable": tnExprVectoredAddDropAdjustTable,
       "tnExprVectoredAddDropAdjustEntry": tnExprVectoredAddDropAdjustEntry,
       "tnExprVectoredAddDropAdjustStatus": tnExprVectoredAddDropAdjustStatus,
       "tnExprVectoredAddDropPowerTable": tnExprVectoredAddDropPowerTable,
       "tnExprVectoredAddDropPowerEntry": tnExprVectoredAddDropPowerEntry,
       "tnExprVectoredAddDropPowerChMeasuredBitSetOut": tnExprVectoredAddDropPowerChMeasuredBitSetOut,
       "tnExprVectoredAddDropPowerChAverageMeasuredOut": tnExprVectoredAddDropPowerChAverageMeasuredOut}
)
